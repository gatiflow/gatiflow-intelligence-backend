from fastapi import APIRouter
from auth.storage import get_connection

router = APIRouter(prefix="/v1/admin", tags=["Admin"])


@router.get("/usage")
def get_global_usage():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT api_key, endpoint, method, timestamp
        FROM usage_logs
        ORDER BY timestamp DESC
        LIMIT 500
    """)

    rows = cur.fetchall()
    conn.close()

    return [
        {
            "api_key": r[0],
            "endpoint": r[1],
            "method": r[2],
            "timestamp": r[3]
        }
        for r in rows
    ]
