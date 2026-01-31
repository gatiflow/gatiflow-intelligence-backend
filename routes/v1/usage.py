from fastapi import APIRouter, Depends
from auth.dependencies import require_api_key
from auth.storage import get_connection

router = APIRouter(prefix="/v1/usage", tags=["Usage"])


@router.get("")
def get_my_usage(api_key: str = Depends(require_api_key)):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT endpoint, method, timestamp
        FROM usage_logs
        WHERE api_key = ?
        ORDER BY timestamp DESC
        LIMIT 100
    """, (api_key,))

    rows = cur.fetchall()
    conn.close()

    return [
        {
            "endpoint": r[0],
            "method": r[1],
            "timestamp": r[2]
        }
        for r in rows
    ]
