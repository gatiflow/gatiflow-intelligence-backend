from fastapi import Header, HTTPException, Response
from auth.api_key import api_key_store


def require_api_key(
    response: Response,
    x_api_key: str = Header(...)
):
    if not api_key_store.validate(x_api_key):
        raise HTTPException(
            status_code=401,
            detail="Invalid or inactive API Key"
        )

    if api_key_store.exceeded_limit(x_api_key):
        raise HTTPException(
            status_code=429,
            detail="Daily API rate limit exceeded"
        )

    api_key_store.register_request(x_api_key)

    stats = api_key_store.stats(x_api_key)

    response.headers["X-RateLimit-Limit"] = str(stats["daily_limit"])
    response.headers["X-RateLimit-Remaining"] = str(stats["remaining"])

    return x_api_key
