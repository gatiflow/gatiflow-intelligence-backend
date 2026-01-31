from fastapi import Header, HTTPException
from auth.api_key import api_key_store


def require_api_key(x_api_key: str = Header(...)):
    """
    Dependency that validates API Key and tracks usage.
    """
    if not api_key_store.validate(x_api_key):
        raise HTTPException(
            status_code=401,
            detail="Invalid or inactive API Key"
        )

    api_key_store.register_request(x_api_key)
    return x_api_key
