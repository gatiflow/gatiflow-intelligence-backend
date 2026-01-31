from datetime import datetime
from typing import Dict
import uuid


class APIKeyStore:
    """
    Simple in-memory API Key store (MVP).
    Can be replaced later by Redis / Database without breaking contracts.
    """

    def __init__(self):
        self.keys: Dict[str, Dict] = {}

    def generate_key(self, owner: str) -> str:
        api_key = f"gf_{uuid.uuid4().hex}"
        self.keys[api_key] = {
            "owner": owner,
            "created_at": datetime.utcnow().isoformat(),
            "requests": 0,
            "active": True,
        }
        return api_key

    def validate(self, api_key: str) -> bool:
        return api_key in self.keys and self.keys[api_key]["active"]

    def register_request(self, api_key: str):
        if api_key in self.keys:
            self.keys[api_key]["requests"] += 1

    def stats(self, api_key: str) -> Dict:
        return self.keys.get(api_key, {})


api_key_store = APIKeyStore()
