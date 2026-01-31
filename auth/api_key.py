from fastapi import Header, HTTPException, Request
from typing import Optional, Dict
import time

# Simples e intencionalmente estático (MVP)
API_KEYS: Dict[str, Dict] = {
    "free-demo-key": {
        "plan": "free",
        "rate_limit": 60  # requests / minute
    },
    "pro-demo-key": {
        "plan": "pro",
        "rate_limit": 300
    },
    "enterprise-demo-key": {
        "plan": "enterprise",
        "rate_limit": 2000
    }
}

# Controle em memória (suficiente para MVP)
RATE_LIMIT_BUCKET: Dict[str, Dict] = {}


def get_api_key(
    request: Request,
    x_api_key: Optional[str] = Header(None)
):
    if not x_api_key or x_api_key not in API_KEYS:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API Key"
        )

    plan_data = API_KEYS[x_api_key]
    limit = plan_data["rate_limit"]
    window = 60  # seconds
    now = time.time()

    bucket = RATE_LIMIT_BUCKET.setdefault(x_api_key, {
        "count": 0,
        "reset": now + window
    })

    if now > bucket["reset"]:
        bucket["count"] = 0
        bucket["reset"] = now + window

    if bucket["count"] >= limit:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded"
        )

    bucket["count"] += 1

    request.state.plan = plan_data["plan"]
    request.state.rate_limit = limit
    request.state.rate_remaining = limit - bucket["count"]

    return x_api_key
