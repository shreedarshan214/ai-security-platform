"""Flask entrypoint for the AI Security Platform."""

import json
from typing import Any, Dict, List, Optional, Tuple

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

from exceptions import PlatformError, ValidationError
from risk_engine import calculate_risk, generate_alert, make_decision
from scanner import run_asm_scan, run_service_scan

try:
    import requests
except ImportError:  # pragma: no cover - depends on local Python environment
    requests = None  # type: ignore[assignment]

ResponsePayload = Dict[str, Any]
Finding = Dict[str, Any]
FindingList = List[Finding]

TARGET_REQUIRED_MESSAGE = (
    "A target is required. Provide {'target': 'example.com'} in JSON or use ?target=example.com."
)
N8N_WEBHOOK_URL = "https://n8n.example.com/webhook/ai-security-platform" 
WEBHOOK_TIMEOUT_SECONDS = 15

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify(
        {
            "message": "AI Security Platform is running.",
            "endpoints": ["/health", "/scan", "/risk", "/run", "/alert"],
            "examples": {
                "scan": "/scan?target=scanme.nmap.org",
                "risk": "/risk?target=scanme.nmap.org",
                "run": "/run?target=scanme.nmap.org",
                "alert": "/alert?target=scanme.nmap.org",
            },
        }
    )


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})


@app.route("/scan", methods=["GET", "POST"])
def scan():
    payload = _get_payload()
    target = _get_required_target(payload)

    _debug_log("Received /scan request", method=request.method, target=target)
    scan_report = _execute_scan_pipeline(target)
    _debug_log(
        "Completed /scan request",
        target=target,
        vulnerability_count=scan_report["summary"]["vulnerability_count"],
    )
    return jsonify(scan_report)


@app.route("/risk", methods=["GET", "POST"])
def risk():
    payload = _get_payload()
    findings, target = _resolve_findings_from_payload(payload)

    _debug_log(
        "Received /risk request",
        method=request.method,
        target=target,
        finding_count=len(findings),
    )
    response = _build_risk_response(findings, target)
    _debug_log(
        "Completed /risk request",
        target=target,
        risk_level=response["risk"]["level"],
        risk_score=response["risk"]["score"],
    )
    return jsonify(response)


@app.route("/run", methods=["GET", "POST"])
def run():
    payload = _get_payload()
    target = _get_required_target(payload)

    _debug_log("Received /run request", method=request.method, target=target)
    response = _run_pipeline(target)
    _debug_log(
        "Completed /run request",
        target=target,
        status=response["status"],
        risk_level=response["risk"]["level"],
    )
    return jsonify(response)


@app.route("/alert", methods=["GET", "POST"])
def alert():
    payload = _get_payload()
    findings, target = _resolve_findings_from_payload(payload)

    _debug_log(
        "Received /alert request",
        method=request.method,
        target=target,
        finding_count=len(findings),
    )
    risk_summary = calculate_risk(findings)
    decision = make_decision(risk_summary)
    alert_details = generate_alert(risk_summary)

    response = {
        "target": target,
        "risk": risk_summary,
        "decision": decision,
        "alert": alert_details,
    }
    _debug_log(
        "Completed /alert request",
        target=target,
        alert_required=alert_details["required"],
        alert_priority=alert_details["priority"],
    )
    return jsonify(response)


def create_app() -> Flask:
    return app


def _register_error_handlers(flask_app: Flask) -> None:
    @flask_app.errorhandler(PlatformError)
    def handle_platform_error(error: PlatformError):
        return jsonify(error.to_dict()), error.status_code

    @flask_app.errorhandler(HTTPException)
    def handle_http_error(error: HTTPException):
        return (
            jsonify(
                {
                    "error": error.description,
                    "code": error.name.lower().replace(" ", "_"),
                }
            ),
            error.code or 500,
        )

    @flask_app.errorhandler(Exception)
    def handle_unexpected_error(error: Exception):
        flask_app.logger.exception("Unhandled application error", exc_info=error)
        return (
            jsonify(
                {
                    "error": "Internal server error.",
                    "code": "internal_server_error",
                }
            ),
            500,
        )


def _get_payload() -> ResponsePayload:
    payload: ResponsePayload = {}
    json_payload = request.get_json(silent=True)

    if json_payload is None:
        if (request.content_length or 0) > 0:
            raise ValidationError("Request body must be valid JSON.")
    else:
        if not isinstance(json_payload, dict):
            raise ValidationError("Request body must be a JSON object.")
        payload.update(json_payload)

    payload.update(_get_query_payload())
    return payload


def _get_query_payload() -> ResponsePayload:
    query_payload: ResponsePayload = {}

    target = request.args.get("target")
    if target is not None:
        query_payload["target"] = target

    for key in ("findings", "vulnerabilities"):
        raw_value = request.args.get(key)
        if raw_value is not None:
            query_payload[key] = _parse_query_json(key, raw_value)

    return query_payload


def _parse_query_json(field_name: str, raw_value: str) -> Any:
    try:
        return json.loads(raw_value)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Query parameter '{field_name}' must contain valid JSON.") from exc


def _get_required_target(
    payload: ResponsePayload,
    error_message: str = TARGET_REQUIRED_MESSAGE,
) -> str:
    target = _read_optional_target(payload)
    if target is None:
        raise ValidationError(error_message)
    return target


def _read_optional_target(payload: ResponsePayload) -> Optional[str]:
    raw_target = payload.get("target")
    if raw_target is None:
        return None
    if not isinstance(raw_target, str):
        raise ValidationError("Target must be provided as a string.")

    target = raw_target.strip()
    return target or None


def _resolve_findings_from_payload(payload: ResponsePayload) -> Tuple[FindingList, Optional[str]]:
    findings = payload.get("findings")
    if findings is None:
        findings = payload.get("vulnerabilities")

    if findings is not None:
        return _validate_findings_payload(findings), _read_optional_target(payload)

    target = _get_required_target(payload, "A target or findings list is required.")
    scan_report = _execute_scan_pipeline(target)
    return scan_report["vulnerabilities"], target


def _validate_findings_payload(findings: Any) -> FindingList:
    if not isinstance(findings, list):
        raise ValidationError("Findings must be provided as a list.")

    normalized_findings: FindingList = []
    for index, finding in enumerate(findings):
        if not isinstance(finding, dict):
            raise ValidationError(f"Finding at index {index} must be a JSON object.")
        normalized_findings.append(finding)

    return normalized_findings


def _build_risk_response(findings: FindingList, target: Optional[str]) -> ResponsePayload:
    return {
        "target": target,
        "findings": findings,
        "vulnerabilities": findings,
        "risk": calculate_risk(findings),
    }


def _execute_scan_pipeline(target: str) -> ResponsePayload:
    _debug_log("Starting ASM scan with python-nmap", target=target)
    asm_scan = run_asm_scan(target)
    assets = asm_scan["assets"]
    _debug_log(
        "ASM scan completed",
        target=target,
        engine=asm_scan["engine"],
        asset_count=asm_scan["summary"]["asset_count"],
        discovered_host_count=asm_scan["summary"]["discovered_host_count"],
    )

    _debug_log("Starting service and vulnerability scan", target=target)
    service_scan = run_service_scan(
        target,
        assets=assets,
        discovered_hosts=asm_scan["discovered_hosts"],
    )
    open_ports = service_scan["open_ports"]
    vulnerabilities = service_scan["vulnerabilities"]
    _debug_log(
        "Service and vulnerability scan completed",
        target=target,
        engine=service_scan["engine"],
        open_port_count=service_scan["summary"]["open_port_count"],
        vulnerability_count=len(vulnerabilities),
    )

    return {
        "target": target,
        "asm": asm_scan,
        "service_scan": service_scan,
        "assets": assets,
        "open_ports": open_ports,
        "vulnerabilities": vulnerabilities,
        "findings": vulnerabilities,
        "summary": _build_scan_summary(assets, open_ports, vulnerabilities),
    }


def _build_scan_summary(
    assets: List[Dict[str, Any]],
    open_ports: List[Dict[str, Any]],
    vulnerabilities: FindingList,
) -> Dict[str, int]:
    return {
        "asset_count": len(assets),
        "open_port_count": len(open_ports),
        "vulnerability_count": len(vulnerabilities),
    }


def _run_pipeline(target: str) -> ResponsePayload:
    scan_report = _execute_scan_pipeline(target)
    vulnerabilities = scan_report["vulnerabilities"]

    _debug_log("Starting risk calculation", target=target, finding_count=len(vulnerabilities))
    risk_summary = calculate_risk(vulnerabilities)
    _debug_log(
        "Risk calculation completed",
        target=target,
        risk_level=risk_summary["level"],
        risk_score=risk_summary["score"],
    )

    decision = make_decision(risk_summary)
    _debug_log("Decision completed", target=target, action=decision["action"])

    alert_details = generate_alert(risk_summary)
    _debug_log(
        "Alert generation completed",
        target=target,
        alert_required=alert_details["required"],
        alert_priority=alert_details["priority"],
    )

    webhook_result = _send_risk_webhook(target, risk_summary, vulnerabilities)

    response = dict(scan_report)
    response["risk"] = risk_summary
    response["decision"] = decision
    response["alert"] = alert_details
    response["webhook"] = webhook_result
    response["status"] = "completed"
    response["pipeline"] = {
        "asm_scan": {
            "engine": scan_report["asm"]["engine"],
            "discovered_hosts": scan_report["asm"]["discovered_hosts"],
            "assets": scan_report["assets"],
            "asset_count": scan_report["summary"]["asset_count"],
        },
        "port_scan": {
            "engine": scan_report["service_scan"]["engine"],
            "scan_targets": scan_report["service_scan"]["scan_targets"],
            "open_ports": scan_report["open_ports"],
            "open_port_count": scan_report["summary"]["open_port_count"],
        },
        "vulnerability_scan": {
            "engine": scan_report["service_scan"]["engine"],
            "vulnerabilities": vulnerabilities,
            "vulnerability_count": scan_report["summary"]["vulnerability_count"],
        },
        "risk_calculation": risk_summary,
        "decision": decision,
    }
    return response


def _send_risk_webhook(
    target: str,
    risk_summary: Dict[str, Any],
    findings: FindingList,
) -> Dict[str, Any]:
    risk_level = str(risk_summary.get("level", "")).lower()
    risk_score = risk_summary.get("score", 0)

    payload = {
        "target": target,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "findings": findings,
        "webhook": {
            "triggered": True,
            "reason": "all_events_mode",
        },
    }

    _debug_log(
        "Triggering n8n webhook for risk event",
        target=target,
        risk_score=risk_score,
        risk_level=risk_level,
        webhook_url=N8N_WEBHOOK_URL,
    )

    if requests is None:
        error_message = "requests library is not installed."
        _debug_log(
            "n8n webhook failed",
            target=target,
            risk_score=risk_score,
            risk_level=risk_level,
            error=error_message,
        )
        return {
            "triggered": True,
            "success": False,
            "reason": "all_events_mode",
            "url": N8N_WEBHOOK_URL,
            "error": error_message,
        }

    try:
        response = requests.post(
            N8N_WEBHOOK_URL,
            json=payload,
            timeout=WEBHOOK_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        _debug_log(
            "n8n webhook failed",
            target=target,
            risk_score=risk_score,
            risk_level=risk_level,
            error=str(exc),
        )
        return {
            "triggered": True,
            "success": False,
            "reason": "all_events_mode",
            "url": N8N_WEBHOOK_URL,
            "error": str(exc),
        }
    except Exception as exc:
        _debug_log(
            "Unexpected webhook error",
            target=target,
            risk_score=risk_score,
            risk_level=risk_level,
            error=str(exc),
        )
        return {
            "triggered": True,
            "success": False,
            "reason": "all_events_mode",
            "url": N8N_WEBHOOK_URL,
            "error": str(exc),
        }

    _debug_log(
        "n8n webhook triggered successfully",
        target=target,
        risk_score=risk_score,
        risk_level=risk_level,
        status_code=response.status_code,
    )
    return {
        "triggered": True,
        "success": True,
        "reason": "all_events_mode",
        "url": N8N_WEBHOOK_URL,
        "status_code": response.status_code,
    }


def _debug_log(message: str, **context: Any) -> None:
    if context:
        details = ", ".join(f"{key}={value!r}" for key, value in context.items())
        log_message = f"[DEBUG] {message} | {details}"
    else:
        log_message = f"[DEBUG] {message}"

    if context:
        try:
            print(log_message, flush=True)
        except OSError:
            app.logger.info(log_message)
        return

    try:
        print(log_message, flush=True)
    except OSError:
        app.logger.info(log_message)


_register_error_handlers(app)


if __name__ == "__main__":
    app.run(debug=True)
