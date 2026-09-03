"""Shared application exceptions."""

from typing import Any, Dict


class PlatformError(Exception):
    """Base class for predictable API errors."""

    default_status_code = 400
    default_error_code = "platform_error"

    def __init__(self, message: str, status_code: int | None = None, error_code: str | None = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code or self.default_status_code
        self.error_code = error_code or self.default_error_code

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error": self.message,
            "code": self.error_code,
        }


class ValidationError(PlatformError):
    default_status_code = 400
    default_error_code = "validation_error"


class ScanError(PlatformError):
    default_status_code = 422
    default_error_code = "scan_error"


class RiskEngineError(PlatformError):
    default_status_code = 422
    default_error_code = "risk_engine_error"
