from datetime import datetime
from typing import Dict
import uuid


class APIKeyStore:
    """
    In-memory API Key store with usage and rate limit control (MVP).
    """

    DEFAULT_LIMIT = 1000  # requests per day (MVP / Free plan)

    def __init__(self):
        self.keys: Dict[str, Dict] = {}

    def generate_key(self, owner: str, limit: int = None) -> str:
        api_key = f"gf_{uuid.uuid4().hex}"
        self.keys[api_key] = {
            "owner": owner,
            "created_at": datetime.utcnow().isoformat(),
            "requests": 0,
            "daily_limit": limit or self.DEFAULT_LIMIT,
            "active": True,
        }
        return api_key

    def validate(self, api_key: str) -> bool:
        return api_key in self.keys and self.keys[api_key]["active"]

    def register_request(self, api_key: str):
        if api_key in self.keys:
            self.keys[api_key]["requests"] += 1

    def exceeded_limit(self, api_key: str) -> bool:
        key = self.keys.get(api_key)
        if not key:
            return True
        return key["requests"] >= key["daily_limit"]

    def stats(self, api_key: str) -> Dict:
        return self.keys.get(api_key, {})


api_key_store = APIKeyStore()
