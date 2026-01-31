from fastapi import APIRouter
from auth.api_key import api_key_store

router = APIRouter(
    prefix="/v1/admin",
    tags=["Admin"]
)


@router.post("/api-keys")
def create_api_key(owner: str):
    """
    Generates a new API Key for a client (MVP admin endpoint).
    """
    return {
        "api_key": api_key_store.generate_key(owner)
    }
