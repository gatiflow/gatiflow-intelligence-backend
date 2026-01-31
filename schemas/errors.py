from typing import Optional, Dict, Any
from datetime import datetime, timezone


def error_response(
    *,
    message: str,
    code: str,
    http_status: int,
    request_id: Optional[str] = None,
    details: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    return {
        "status": "error",
        "error": {
            "message": message,
            "code": code,
            "http_status": http_status,
            "request_id": request_id,
            "details": details or {}
        },
        "metadata": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "provider": "GatiFlow Intelligence API",
            "version": "v1"
        }
    }
