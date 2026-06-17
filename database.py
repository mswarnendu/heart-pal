import sqlite3
import pandas as pd
from datetime import datetime
 

def get_db():
    conn = sqlite3.connect("heart_app.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS history (
            username TEXT,
            date TEXT,
            risk_score REAL
        )
    """)
    return conn


def already_submitted_this_month(username):
    conn = get_db()
    month = datetime.now().strftime("%Y-%m")
    row = conn.execute("""
        SELECT 1 FROM history
        WHERE username = ? AND strftime('%Y-%m', date) = ?
    """, (username, month)).fetchone()
    conn.close()
    return row is not None


def save_result(username, risk_score):
    conn = get_db()
    conn.execute("""
        INSERT INTO history (username, date, risk_score)
        VALUES (?, ?, ?)
    """, (username, datetime.now().strftime("%Y-%m-%d"), risk_score))
    conn.commit()
    conn.close()


def get_user_history(username):
    conn = get_db()
    df = pd.read_sql("""
        SELECT date, risk_score FROM history
        WHERE username = ? ORDER BY date
    """, conn, params=(username,))
    conn.close()
    return df
