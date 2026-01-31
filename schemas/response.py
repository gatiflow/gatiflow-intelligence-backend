from typing import Any, Dict
from datetime import datetime, timezone


def response_envelope(
    data: Any,
    status: str = "success",
    message: str = "Request processed successfully"
) -> Dict[str, Any]:
    return {
        "status": status,
        "message": message,
        "metadata": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "provider": "GatiFlow Intelligence API",
            "version": "v1"
        },
        "data": data
    }
