"""Nmap-backed scanning workflow for the AI Security Platform."""

from ipaddress import ip_address, ip_network
from pathlib import Path
from shutil import which
from typing import Any, Dict, Iterable, List, Sequence
from urllib.parse import urlparse

from exceptions import ScanError, ValidationError

Asset = Dict[str, str]
PortRecord = Dict[str, Any]
Vulnerability = Dict[str, Any]
ScanReport = Dict[str, Any]
HostRecord = Dict[str, Any]
AsmScanResult = Dict[str, Any]
ServiceScanResult = Dict[str, Any]

NMAP_ENGINE = "python-nmap"
DISCOVERY_ARGS = "-sn"
SERVICE_SCAN_ARGS = "-Pn -T4 -sV --version-light --top-ports 100 --script vuln --script-timeout 30s"

PORT_FINDING_RULES: Dict[int, Dict[str, str]] = {
    21: {
        "name": "FTP Service Exposed",
        "severity": "high",
        "category": "remote_access",
        "description": "FTP is open and may allow weakly protected file transfer or anonymous access.",
    },
    22: {
        "name": "SSH Service Exposed",
        "severity": "medium",
        "category": "remote_access",
        "description": "SSH is externally reachable and should be restricted to trusted networks.",
    },
    23: {
        "name": "Telnet Service Exposed",
        "severity": "critical",
        "category": "remote_access",
        "description": "Telnet is open and transmits credentials and commands in plaintext.",
    },
    80: {
        "name": "Unencrypted Web Endpoint",
        "severity": "high",
        "category": "transport_security",
        "description": "HTTP is exposed and may allow plaintext traffic interception.",
    },
    139: {
        "name": "NetBIOS Service Exposed",
        "severity": "medium",
        "category": "lateral_movement",
        "description": "NetBIOS exposure can broaden internal attack surface.",
    },
    445: {
        "name": "SMB Service Exposed",
        "severity": "high",
        "category": "lateral_movement",
        "description": "SMB is reachable and should be tightly controlled to reduce lateral movement risk.",
    },
    3389: {
        "name": "RDP Service Exposed",
        "severity": "high",
        "category": "remote_access",
        "description": "RDP is reachable and should be protected by network restrictions and MFA.",
    },
    5432: {
        "name": "PostgreSQL Service Exposed",
        "severity": "critical",
        "category": "data_exposure",
        "description": "A PostgreSQL service is reachable and may expose sensitive data.",
    },
    6379: {
        "name": "Redis Service Exposed",
        "severity": "critical",
        "category": "data_exposure",
        "description": "Redis is reachable and may expose cached secrets or operational data.",
    },
    8080: {
        "name": "Alternate Web Port Exposed",
        "severity": "medium",
        "category": "attack_surface",
        "description": "A secondary HTTP service is exposed and may bypass primary edge controls.",
    },
    8443: {
        "name": "Management Interface Detected",
        "severity": "high",
        "category": "administration",
        "description": "An alternate HTTPS management interface is exposed to the network.",
    },
    9200: {
        "name": "Elasticsearch API Exposed",
        "severity": "critical",
        "category": "data_exposure",
        "description": "Elasticsearch is reachable and may expose indexed application data.",
    },
}

SERVICE_FINDING_RULES: Dict[str, Dict[str, str]] = {
    "ftp": PORT_FINDING_RULES[21],
    "ssh": PORT_FINDING_RULES[22],
    "telnet": PORT_FINDING_RULES[23],
    "microsoft-ds": PORT_FINDING_RULES[445],
    "ms-wbt-server": PORT_FINDING_RULES[3389],
    "postgresql": PORT_FINDING_RULES[5432],
    "redis": PORT_FINDING_RULES[6379],
}


def build_scan_report(target: str) -> ScanReport:
    """Run host discovery, service detection, and finding extraction with Nmap."""
    asm_scan = run_asm_scan(target)
    service_scan = run_service_scan(
        target,
        assets=asm_scan["assets"],
        discovered_hosts=asm_scan["discovered_hosts"],
    )

    return {
        "target": asm_scan["target"],
        "normalized_target": asm_scan["normalized_target"],
        "asm": asm_scan,
        "service_scan": service_scan,
        "assets": asm_scan["assets"],
        "open_ports": service_scan["open_ports"],
        "vulnerabilities": service_scan["vulnerabilities"],
        "summary": _build_summary(
            asm_scan["assets"],
            service_scan["open_ports"],
            service_scan["vulnerabilities"],
        ),
    }


def scan_target(target: str) -> List[Vulnerability]:
    """Compatibility wrapper for callers that only need findings."""
    return build_scan_report(target)["vulnerabilities"]


def discover_assets(target: str) -> List[Asset]:
    """Discover reachable hosts and hostnames using Nmap host discovery."""
    return run_asm_scan(target)["assets"]


def run_asm_scan(target: str) -> AsmScanResult:
    """Run a real ASM discovery pass with python-nmap."""
    validated_target = _validate_target(target)
    normalized_target = _normalize_target(validated_target)
    port_scanner = _create_port_scanner()

    discovered_hosts = _run_host_discovery(port_scanner, normalized_target)
    host_records = _collect_host_records(port_scanner)
    assets = _build_assets(normalized_target, host_records)

    return {
        "target": validated_target,
        "normalized_target": normalized_target,
        "engine": NMAP_ENGINE,
        "discovery_args": DISCOVERY_ARGS,
        "discovered_hosts": discovered_hosts,
        "assets": assets,
        "summary": {
            "asset_count": len(assets),
            "discovered_host_count": len(discovered_hosts),
        },
    }


def scan_open_ports(target: str, assets: List[Asset] | None = None) -> List[PortRecord]:
    """Enumerate real open ports and service details with Nmap."""
    return run_service_scan(target, assets=assets)["open_ports"]


def scan_vulnerabilities(
    target: str,
    assets: List[Asset],
    open_ports: List[PortRecord],
) -> List[Vulnerability]:
    """Derive findings from Nmap scripts and observed open services."""
    del open_ports

    return run_service_scan(target, assets=assets)["vulnerabilities"]


def run_service_scan(
    target: str,
    assets: List[Asset] | None = None,
    discovered_hosts: List[str] | None = None,
) -> ServiceScanResult:
    """Run a real Nmap service and NSE scan for the target."""
    validated_target = _validate_target(target)
    normalized_target = _normalize_target(validated_target)
    port_scanner = _create_port_scanner()

    resolved_discovered_hosts = discovered_hosts
    if resolved_discovered_hosts is None:
        resolved_discovered_hosts = _run_host_discovery(port_scanner, normalized_target)

    scan_targets = resolved_discovered_hosts or [normalized_target]
    host_records = _scan_hosts(port_scanner, scan_targets)
    resolved_assets = assets or _build_assets(normalized_target, host_records)
    open_ports = _extract_open_ports(host_records)
    vulnerabilities = _extract_vulnerabilities(normalized_target, resolved_assets, open_ports, host_records)

    return {
        "target": validated_target,
        "normalized_target": normalized_target,
        "engine": NMAP_ENGINE,
        "service_scan_args": SERVICE_SCAN_ARGS,
        "scan_targets": scan_targets,
        "open_ports": open_ports,
        "vulnerabilities": vulnerabilities,
        "summary": {
            "open_port_count": len(open_ports),
            "vulnerability_count": len(vulnerabilities),
        },
    }


def _create_port_scanner() -> Any:
    nmap_module = _load_nmap_module()
    nmap_binary = _find_nmap_binary()

    if nmap_binary is None:
        raise ScanError(
            "Nmap executable was not found. Install Nmap and ensure the 'nmap' command is available."
        )

    try:
        return nmap_module.PortScanner(nmap_search_path=(nmap_binary,))
    except Exception as exc:  # pragma: no cover - depends on local Nmap install
        raise ScanError(f"Failed to initialize Nmap scanner: {exc}") from exc


def _load_nmap_module() -> Any:
    try:
        import nmap  # type: ignore
    except ImportError as exc:  # pragma: no cover - depends on local Python environment
        raise ScanError(
            "python-nmap is not installed. Install project requirements before running scans."
        ) from exc

    return nmap


def _find_nmap_binary() -> str | None:
    discovered = which("nmap") or which("nmap.exe")
    if discovered:
        return discovered

    candidate_paths = (
        Path("C:/Program Files (x86)/Nmap/nmap.exe"),
        Path("C:/Program Files/Nmap/nmap.exe"),
    )
    for candidate in candidate_paths:
        if candidate.exists():
            return str(candidate)

    return None


def _run_host_discovery(port_scanner: Any, target: str) -> List[str]:
    try:
        port_scanner.scan(hosts=target, arguments=DISCOVERY_ARGS)
    except Exception as exc:  # pragma: no cover - depends on local Nmap install and target reachability
        raise ScanError(f"Nmap host discovery failed for '{target}': {exc}") from exc

    discovered_hosts: List[str] = []
    for host in port_scanner.all_hosts():
        host_record = port_scanner[host]
        if _safe_host_state(host_record) == "up":
            discovered_hosts.append(host)

    return discovered_hosts


def _scan_hosts(port_scanner: Any, targets: Sequence[str]) -> List[HostRecord]:
    host_records: List[HostRecord] = []

    for target in targets:
        try:
            port_scanner.scan(hosts=target, arguments=SERVICE_SCAN_ARGS)
        except Exception as exc:  # pragma: no cover - depends on local Nmap install and target reachability
            raise ScanError(f"Nmap service scan failed for '{target}': {exc}") from exc

        host_records.extend(_collect_host_records(port_scanner))

    return _deduplicate_host_records(host_records)


def _collect_host_records(port_scanner: Any) -> List[HostRecord]:
    host_records: List[HostRecord] = []

    for host in port_scanner.all_hosts():
        host_entry = port_scanner[host]
        protocols: Dict[str, Dict[int, Dict[str, Any]]] = {}

        for protocol in _safe_all_protocols(host_entry):
            protocol_records: Dict[int, Dict[str, Any]] = {}
            for port, details in host_entry.get(protocol, {}).items():
                if isinstance(port, int):
                    protocol_records[port] = dict(details)
            if protocol_records:
                protocols[protocol] = protocol_records

        host_records.append(
            {
                "host": host,
                "state": _safe_host_state(host_entry),
                "addresses": _normalize_addresses(host_entry.get("addresses", {})),
                "hostnames": _normalize_hostnames(host_entry),
                "host_scripts": _normalize_host_scripts(host_entry.get("hostscript", [])),
                "protocols": protocols,
            }
        )

    return host_records


def _build_assets(normalized_target: str, host_records: List[HostRecord]) -> List[Asset]:
    assets: List[Asset] = []

    if _asset_kind(normalized_target) in {"domain", "ip"}:
        assets.append(
            _make_asset(
                _asset_kind(normalized_target),
                normalized_target,
                "user_input",
                "primary",
            )
        )

    for record in host_records:
        for address_value in record["addresses"].values():
            assets.append(_make_asset("ip", address_value, "nmap_discovery", "discovered_host"))

        for hostname in record["hostnames"]:
            assets.append(_make_asset("domain", hostname, "nmap_reverse_dns", "resolved_name"))

        host_value = record.get("host")
        if isinstance(host_value, str) and _asset_kind(host_value) in {"domain", "ip"}:
            source = "nmap_scan"
            role = "resolved_target"
            assets.append(_make_asset(_asset_kind(host_value), host_value, source, role))

    return _deduplicate_assets(assets)


def _extract_open_ports(host_records: List[HostRecord]) -> List[PortRecord]:
    open_ports: List[PortRecord] = []

    for record in host_records:
        asset = _preferred_asset_for_host(record)

        for protocol, ports in record["protocols"].items():
            for port, details in sorted(ports.items()):
                if str(details.get("state", "")).lower() != "open":
                    continue

                open_ports.append(
                    _make_port(
                        asset=asset,
                        port=port,
                        protocol=protocol,
                        service=str(details.get("name") or "unknown"),
                        product=str(details.get("product") or ""),
                        version=str(details.get("version") or ""),
                        extrainfo=str(details.get("extrainfo") or ""),
                    )
                )

    return _deduplicate_ports(open_ports)


def _extract_vulnerabilities(
    target: str,
    assets: List[Asset],
    open_ports: List[PortRecord],
    host_records: List[HostRecord],
) -> List[Vulnerability]:
    vulnerabilities: List[Vulnerability] = []
    asset_names = {asset["value"] for asset in assets}

    vulnerabilities.extend(_extract_nse_findings(host_records))
    vulnerabilities.extend(_extract_port_findings(open_ports))

    admin_asset = next((name for name in asset_names if name.startswith(("admin.", "auth."))), None)
    if admin_asset:
        vulnerabilities.append(
            _make_vulnerability(
                name="Sensitive Authentication Surface",
                severity="medium",
                asset=admin_asset,
                category="identity",
                description="Administrative or authentication endpoints were discovered during enumeration.",
            )
        )

    if not vulnerabilities:
        vulnerabilities.append(
            _make_vulnerability(
                name="No Material Findings From Nmap Scan",
                severity="low",
                asset=target,
                category="baseline",
                description="The Nmap scan completed without any notable exposed services or NSE findings.",
            )
        )

    return _deduplicate_vulnerabilities(vulnerabilities)


def _extract_nse_findings(host_records: List[HostRecord]) -> List[Vulnerability]:
    findings: List[Vulnerability] = []

    for record in host_records:
        asset = _preferred_asset_for_host(record)

        for script in record["host_scripts"]:
            findings.append(
                _make_vulnerability(
                    name=f"Nmap NSE Finding: {script['name']}",
                    severity=_infer_script_severity(script["name"], script["output"]),
                    asset=asset,
                    category="nmap_nse",
                    description=_format_script_output(script["output"]),
                )
            )

        for protocol, ports in record["protocols"].items():
            for port, details in ports.items():
                scripts = details.get("script", {})
                if not isinstance(scripts, dict):
                    continue

                for script_name, script_output in scripts.items():
                    findings.append(
                        _make_vulnerability(
                            name=f"Nmap NSE Finding: {script_name}",
                            severity=_infer_script_severity(script_name, script_output),
                            asset=asset,
                            category="nmap_nse",
                            description=_format_script_output(script_output),
                            port=port,
                            protocol=protocol,
                        )
                    )

    return findings


def _extract_port_findings(open_ports: List[PortRecord]) -> List[Vulnerability]:
    findings: List[Vulnerability] = []

    for port_record in open_ports:
        rule = PORT_FINDING_RULES.get(port_record["port"])
        if rule is None:
            rule = SERVICE_FINDING_RULES.get(str(port_record.get("service", "")).lower())
        if rule is None:
            continue

        findings.append(
            _make_vulnerability(
                name=rule["name"],
                severity=rule["severity"],
                asset=port_record["asset"],
                category=rule["category"],
                description=rule["description"],
                port=port_record["port"],
                protocol=port_record["protocol"],
            )
        )

    return findings


def _build_summary(
    assets: List[Asset],
    open_ports: List[PortRecord],
    vulnerabilities: List[Vulnerability],
) -> Dict[str, int]:
    return {
        "asset_count": len(assets),
        "open_port_count": len(open_ports),
        "vulnerability_count": len(vulnerabilities),
    }


def _validate_target(target: str) -> str:
    if not isinstance(target, str):
        raise ValidationError("Target must be provided as a string.")

    cleaned_target = target.strip()
    if not cleaned_target:
        raise ValidationError("Target must not be empty.")

    if any(character.isspace() for character in cleaned_target):
        raise ScanError("Target must be a hostname, IP, CIDR, or URL without spaces.")

    return cleaned_target


def _normalize_target(target: str) -> str:
    cleaned_target = target.strip()

    if "://" in cleaned_target:
        parsed = urlparse(cleaned_target)
        if not parsed.hostname:
            raise ScanError("Could not parse a valid hostname from target URL.")
        return parsed.hostname.lower()

    if _looks_like_host_and_port(cleaned_target):
        host, _, _ = cleaned_target.rpartition(":")
        return host.lower()

    return cleaned_target.lower()


def _looks_like_host_and_port(target: str) -> bool:
    if target.count(":") != 1 or "/" in target:
        return False

    host, _, port = target.rpartition(":")
    return bool(host) and port.isdigit()


def _safe_host_state(host_entry: Any) -> str:
    if hasattr(host_entry, "state"):
        try:
            return str(host_entry.state()).lower()
        except Exception:
            return "unknown"
    return "unknown"


def _safe_all_protocols(host_entry: Any) -> Iterable[str]:
    if hasattr(host_entry, "all_protocols"):
        try:
            return [str(protocol) for protocol in host_entry.all_protocols()]
        except Exception:
            return []
    return []


def _normalize_addresses(addresses: Any) -> Dict[str, str]:
    if not isinstance(addresses, dict):
        return {}
    return {
        str(address_type): str(value)
        for address_type, value in addresses.items()
        if isinstance(value, str) and value
    }


def _normalize_hostnames(host_entry: Any) -> List[str]:
    normalized_hostnames: List[str] = []
    raw_hostnames = host_entry.get("hostnames", [])

    if isinstance(raw_hostnames, list):
        for item in raw_hostnames:
            if isinstance(item, dict):
                hostname = str(item.get("name") or "").strip().lower()
                if hostname:
                    normalized_hostnames.append(hostname)

    if hasattr(host_entry, "hostname"):
        try:
            hostname = str(host_entry.hostname() or "").strip().lower()
        except Exception:
            hostname = ""
        if hostname:
            normalized_hostnames.append(hostname)

    return _deduplicate_strings(normalized_hostnames)


def _normalize_host_scripts(host_scripts: Any) -> List[Dict[str, str]]:
    normalized_scripts: List[Dict[str, str]] = []

    if isinstance(host_scripts, dict):
        host_scripts = [{"id": key, "output": value} for key, value in host_scripts.items()]

    if not isinstance(host_scripts, list):
        return normalized_scripts

    for item in host_scripts:
        if not isinstance(item, dict):
            continue
        script_name = str(item.get("id") or item.get("name") or "").strip()
        script_output = _format_script_output(item.get("output", ""))
        if script_name and script_output:
            normalized_scripts.append({"name": script_name, "output": script_output})

    return normalized_scripts


def _preferred_asset_for_host(record: HostRecord) -> str:
    hostnames = record.get("hostnames", [])
    if isinstance(hostnames, list) and hostnames:
        return str(hostnames[0])

    addresses = record.get("addresses", {})
    if isinstance(addresses, dict):
        for key in ("ipv4", "ipv6", "mac"):
            if key in addresses:
                return str(addresses[key])

    return str(record.get("host") or "unknown-host")


def _asset_kind(value: str) -> str:
    if _is_network_target(value):
        return "network"

    try:
        ip_address(value)
    except ValueError:
        return "domain"
    return "ip"


def _make_asset(asset_type: str, value: str, source: str, role: str) -> Asset:
    return {
        "type": asset_type,
        "value": value,
        "source": source,
        "role": role,
    }


def _make_port(
    asset: str,
    port: int,
    protocol: str,
    service: str,
    product: str = "",
    version: str = "",
    extrainfo: str = "",
) -> PortRecord:
    port_record: PortRecord = {
        "asset": asset,
        "port": port,
        "protocol": protocol,
        "service": service,
        "state": "open",
    }

    if product:
        port_record["product"] = product
    if version:
        port_record["version"] = version
    if extrainfo:
        port_record["extrainfo"] = extrainfo

    return port_record


def _make_vulnerability(
    name: str,
    severity: str,
    asset: str,
    category: str,
    description: str,
    port: int | None = None,
    protocol: str | None = None,
) -> Vulnerability:
    vulnerability: Vulnerability = {
        "name": name,
        "severity": severity,
        "asset": asset,
        "category": category,
        "description": description,
    }

    if port is not None:
        vulnerability["port"] = port
    if protocol is not None:
        vulnerability["protocol"] = protocol

    return vulnerability


def _infer_script_severity(script_name: str, script_output: Any) -> str:
    combined = f"{script_name} {_format_script_output(script_output)}".lower()

    if any(keyword in combined for keyword in ("critical", "remote code execution", "rce", "backdoor")):
        return "critical"
    if any(keyword in combined for keyword in ("vulnerable", "cve-", "authentication bypass", "sql injection")):
        return "high"
    if any(keyword in combined for keyword in ("default credentials", "weak", "anonymous", "exposed")):
        return "medium"
    return "medium"


def _format_script_output(script_output: Any) -> str:
    formatted = str(script_output).strip().replace("\r", " ").replace("\n", " ")
    return " ".join(formatted.split())[:400]


def _deduplicate_assets(assets: List[Asset]) -> List[Asset]:
    unique_assets: List[Asset] = []
    seen = set()

    for asset in assets:
        key = (asset["type"], asset["value"])
        if key not in seen:
            seen.add(key)
            unique_assets.append(asset)

    return unique_assets


def _deduplicate_ports(port_entries: List[PortRecord]) -> List[PortRecord]:
    unique_entries: List[PortRecord] = []
    seen = set()

    for entry in port_entries:
        key = (entry["asset"], entry["port"], entry["protocol"])
        if key not in seen:
            seen.add(key)
            unique_entries.append(entry)

    return unique_entries


def _deduplicate_vulnerabilities(vulnerabilities: List[Vulnerability]) -> List[Vulnerability]:
    unique_vulnerabilities: List[Vulnerability] = []
    seen = set()

    for vulnerability in vulnerabilities:
        key = (
            vulnerability.get("name"),
            vulnerability.get("asset"),
            vulnerability.get("port"),
            vulnerability.get("protocol"),
        )
        if key not in seen:
            seen.add(key)
            unique_vulnerabilities.append(vulnerability)

    return unique_vulnerabilities


def _deduplicate_host_records(host_records: List[HostRecord]) -> List[HostRecord]:
    unique_records: List[HostRecord] = []
    seen = set()

    for record in host_records:
        key = (
            record.get("host"),
            tuple(sorted(record.get("addresses", {}).items())),
        )
        if key not in seen:
            seen.add(key)
            unique_records.append(record)

    return unique_records


def _deduplicate_strings(values: List[str]) -> List[str]:
    ordered_values: List[str] = []
    seen = set()

    for value in values:
        if value not in seen:
            seen.add(value)
            ordered_values.append(value)

    return ordered_values


def _is_network_target(target: str) -> bool:
    try:
        ip_network(target, strict=False)
    except ValueError:
        return False
    return "/" in target
