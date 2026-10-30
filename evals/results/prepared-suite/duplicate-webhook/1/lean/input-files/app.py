"""Existing webhook persistence API. SQLite is the local evaluation database."""
import sqlite3


def connect(path):
    conn = sqlite3.connect(path, timeout=5)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS events (event_id TEXT NOT NULL, amount INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS ledger (event_id TEXT NOT NULL, amount INTEGER NOT NULL);
    """)
    return conn


def handle_event(conn, event):
    with conn:
        conn.execute("INSERT INTO events VALUES (?, ?)", (event["id"], event["amount"]))
        conn.execute("INSERT INTO ledger VALUES (?, ?)", (event["id"], event["amount"]))
    return 200
