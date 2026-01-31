import sqlite3
from datetime import datetime, date

DB_PATH = "gatiflow.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS api_keys (
            api_key TEXT PRIMARY KEY,
            owner TEXT,
            created_at TEXT,
            daily_limit INTEGER,
            requests INTEGER,
            last_reset DATE,
            active INTEGER
        )
    """)

    conn.commit()
    conn.close()


def reset_if_new_day(api_key: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT last_reset FROM api_keys WHERE api_key = ?",
        (api_key,)
    )
    row = cur.fetchone()

    today = date.today().isoformat()

    if row and row[0] != today:
        cur.execute("""
            UPDATE api_keys
            SET requests = 0, last_reset = ?
            WHERE api_key = ?
        """, (today, api_key))

    conn.commit()
    conn.close()
