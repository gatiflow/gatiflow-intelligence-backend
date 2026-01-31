from datetime import datetime, date
from typing import Dict
import uuid

from auth.storage import get_connection, init_db, reset_if_new_day

DEFAULT_LIMIT = 1000


class APIKeyStore:
    """
    Persistent API Key store backed by SQLite (MVP production-ready).
    """

    def __init__(self):
        init_db()

    def generate_key(self, owner: str, limit: int = DEFAULT_LIMIT) -> str:
        api_key = f"gf_{uuid.uuid4().hex}"
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO api_keys
            (api_key, owner, created_at, daily_limit, requests, last_reset, active)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            api_key,
            owner,
            datetime.utcnow().isoformat(),
            limit,
            0,
            date.today().isoformat(),
            1
        ))

        conn.commit()
        conn.close()
        return api_key

    def validate(self, api_key: str) -> bool:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT active FROM api_keys WHERE api_key = ?",
            (api_key,)
        )
        row = cur.fetchone()
        conn.close()

        return bool(row and row[0])

    def exceeded_limit(self, api_key: str) -> bool:
        reset_if_new_day(api_key)

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT requests, daily_limit
            FROM api_keys
            WHERE api_key = ?
        """, (api_key,))
        row = cur.fetchone()
        conn.close()

        if not row:
            return True

        return row[0] >= row[1]

    def register_request(self, api_key: str):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE api_keys
            SET requests = requests + 1
            WHERE api_key = ?
        """, (api_key,))

        conn.commit()
        conn.close()

    def stats(self, api_key: str) -> Dict:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT owner, daily_limit, requests
            FROM api_keys
            WHERE api_key = ?
        """, (api_key,))
        row = cur.fetchone()
        conn.close()

        if not row:
            return {}

        return {
            "owner": row[0],
            "daily_limit": row[1],
            "requests": row[2],
            "remaining": row[1] - row[2]
        }


api_key_store = APIKeyStore()
