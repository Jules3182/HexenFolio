import sqlite3
from datetime import datetime

DB_PATH = "data/history.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS portfolio_history (
            timestamp TEXT PRIMARY KEY,
            total_value REAL
        )
    """)
    conn.commit()
    conn.close()

def record_snapshot(total_value: float):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO portfolio_history VALUES (?, ?)",
        (datetime.utcnow().isoformat(), total_value)
    )
    conn.commit()
    conn.close()

def get_history(limit: int = 500):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT timestamp, total_value
        FROM portfolio_history
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))
    rows = cur.fetchall()
    conn.close()

    return [
        {"timestamp": ts, "total_value": val}
        for ts, val in reversed(rows)
    ]