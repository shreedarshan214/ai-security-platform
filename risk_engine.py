"""Risk scoring and response helpers for the AI Security Platform."""

from typing import Any, Dict, List, Tuple

from exceptions import RiskEngineError

Finding = Dict[str, Any]
RiskSummary = Dict[str, Any]

SEVERITY_WEIGHTS = {
    "low": 5,
    "medium": 15,
    "high": 30,
    "critical": 45,
}

COUNT_WEIGHT = 4
MAX_SEVERITY_SCORE = 80
MAX_COUNT_SCORE = 20


def calculate_risk(findings: List[Finding]) -> RiskSummary:
    """Calculate a normalized risk score from a list of vulnerabilities."""
    normalized_findings = _normalize_findings(findings)
    finding_count = len(normalized_findings)
    severity_breakdown = _build_severity_breakdown(normalized_findings)

    severity_score = min(
        MAX_SEVERITY_SCORE,
        sum(SEVERITY_WEIGHTS[_normalize_severity(item.get("severity"))] for item in normalized_findings),
    )
    count_score = min(MAX_COUNT_SCORE, finding_count * COUNT_WEIGHT)
    score = min(100, severity_score + count_score)
    level = _score_to_level(score)

    return {
        "score": score,
        "level": level,
        "finding_count": finding_count,
        "severity_score": severity_score,
        "count_score": count_score,
        "severity_breakdown": severity_breakdown,
    }


def make_decision(risk: RiskSummary) -> Dict[str, str]:
    """Map a risk summary to an action-oriented decision."""
    score, level = _extract_risk_inputs(risk)

    if score >= 80 or level == "critical":
        action = "block_and_escalate"
        disposition = "fail"
        rationale = "Critical risk requires immediate containment and escalation."
    elif score >= 50 or level == "high":
        action = "manual_review"
        disposition = "review"
        rationale = "High risk findings need analyst review before approval."
    elif score >= 20 or level == "medium":
        action = "monitor"
        disposition = "observe"
        rationale = "Moderate risk was detected. Monitor and remediate in the next cycle."
    else:
        action = "allow"
        disposition = "pass"
        rationale = "Risk is low enough to continue under normal monitoring."

    return {
        "action": action,
        "disposition": disposition,
        "rationale": rationale,
    }


def generate_alert(risk: RiskSummary) -> Dict[str, Any]:
    """Create an alert payload derived from the current risk summary."""
    _, level = _extract_risk_inputs(risk)
    decision = make_decision(risk)
    alert_required = level in {"high", "critical"}

    if level == "critical":
        priority = "immediate"
        message = "Critical risk detected. Escalate and respond immediately."
    elif level == "high":
        priority = "high"
        message = "High risk detected. Security review is recommended."
    elif level == "medium":
        priority = "medium"
        message = "Medium risk detected. Monitor and investigate soon."
    else:
        priority = "low"
        message = "Risk is currently low. Continue routine monitoring."

    return {
        "required": alert_required,
        "priority": priority,
        "message": message,
        "decision": decision,
    }


def _normalize_findings(findings: List[Finding]) -> List[Finding]:
    if not isinstance(findings, list):
        raise RiskEngineError("Findings must be provided as a list.")

    normalized_findings: List[Finding] = []
    for index, finding in enumerate(findings):
        if not isinstance(finding, dict):
            raise RiskEngineError(f"Finding at index {index} must be a dictionary.")
        normalized_findings.append(finding)

    return normalized_findings


def _build_severity_breakdown(findings: List[Finding]) -> Dict[str, int]:
    breakdown = {
        "low": 0,
        "medium": 0,
        "high": 0,
        "critical": 0,
    }

    for item in findings:
        breakdown[_normalize_severity(item.get("severity"))] += 1

    return breakdown


def _extract_risk_inputs(risk: RiskSummary) -> Tuple[int, str]:
    if not isinstance(risk, dict):
        raise RiskEngineError("Risk summary must be a dictionary.")

    raw_score = risk.get("score", 0)
    if not isinstance(raw_score, (int, float)):
        raise RiskEngineError("Risk score must be numeric.")

    score = max(0, min(100, int(raw_score)))
    level = _normalize_level(risk.get("level")) or _score_to_level(score)
    return score, level


def _normalize_severity(severity: Any) -> str:
    normalized = str(severity or "low").lower()
    if normalized in SEVERITY_WEIGHTS:
        return normalized
    return "low"


def _normalize_level(level: Any) -> str | None:
    if level is None:
        return None

    normalized = str(level).lower()
    if normalized in {"low", "medium", "high", "critical"}:
        return normalized
    return None


def _score_to_level(score: int) -> str:
    if score >= 80:
        return "critical"
    if score >= 50:
        return "high"
    if score >= 20:
        return "medium"
    return "low"
