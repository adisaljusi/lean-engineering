"""Existing commission portal persistence API; proposed changes currently overwrite rates."""
import json
import sqlite3


def connect(path):
    conn = sqlite3.connect(path)
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS sections (
            tenant TEXT, treaty TEXT, section TEXT, base_rate INTEGER,
            PRIMARY KEY (tenant, treaty, section));
        CREATE TABLE IF NOT EXISTS changes (
            id TEXT PRIMARY KEY, tenant TEXT, treaty TEXT, section TEXT,
            payload TEXT, status TEXT, reason TEXT);
        INSERT OR IGNORE INTO sections VALUES ('Org-A', 'T-42', 'property', 1250);
        INSERT OR IGNORE INTO sections VALUES ('Org-A', 'T-42', 'casualty', 1000);
    ''')
    return conn


def propose_change(conn, actor, change):
    with conn:
        conn.execute('INSERT INTO changes VALUES (?, ?, ?, ?, ?, ?, ?)',
                     (change['id'], actor['tenant'], change['treaty'], change['section'],
                      json.dumps(change), 'pending', ''))
        conn.execute('UPDATE sections SET base_rate=? WHERE tenant=? AND treaty=? AND section=?',
                     (change['rate'], actor['tenant'], change['treaty'], change['section']))
    return {'id': change['id'], 'status': 'pending'}


def publish_change(conn, actor, change_id, reason=''):
    with conn:
        conn.execute("UPDATE changes SET status='published', reason=? WHERE id=?", (reason, change_id))
    return {'id': change_id, 'status': 'published'}


def rate_on(conn, actor, treaty, section, day):
    row = conn.execute('SELECT base_rate FROM sections WHERE tenant=? AND treaty=? AND section=?',
                       (actor['tenant'], treaty, section)).fetchone()
    if row is None:
        raise KeyError('Section not found')
    return row[0]


def list_changes(conn, actor, treaty, section):
    rows = conn.execute('SELECT payload, status, reason FROM changes WHERE tenant=? AND treaty=? AND section=? ORDER BY id',
                        (actor['tenant'], treaty, section)).fetchall()
    return [dict(json.loads(payload), status=status, reason=reason) for payload, status, reason in rows]
