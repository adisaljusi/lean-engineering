"""Private oracle control, not a generated agent sample or proposed production code."""
import datetime
import json
from pathlib import Path
import sqlite3


def connect(path):
    conn = sqlite3.connect(path)
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS sections (tenant TEXT, treaty TEXT, section TEXT,
            base_rate INTEGER, PRIMARY KEY(tenant, treaty, section));
        CREATE TABLE IF NOT EXISTS changes (id TEXT PRIMARY KEY, tenant TEXT, treaty TEXT,
            section TEXT, payload TEXT, status TEXT, reason TEXT, published_seq INTEGER);
        INSERT OR IGNORE INTO sections VALUES ('Org-A', 'T-42', 'property', 1250);
        INSERT OR IGNORE INTO sections VALUES ('Org-A', 'T-42', 'casualty', 1000);
    ''')
    return conn


def propose_change(conn, actor, change):
    if actor['role'] not in ('reviewer', 'approver'):
        raise PermissionError('Role cannot propose')
    rate = change['rate']
    if type(rate) is not int or not 0 <= rate <= 10000:
        raise ValueError('Invalid rate')
    start = datetime.date.fromisoformat(change['start'])
    if change.get('end') and datetime.date.fromisoformat(change['end']) <= start:
        raise ValueError('Invalid interval')
    rate_on(conn, actor, change['treaty'], change['section'], change['start'])
    ref = change['source']
    sources = json.loads(Path(__file__).with_name('sources.json').read_text())
    try:
        text = sources[ref['document_version']]['pages'][ref['page_id']]['spans'][ref['span_id']]['text']
    except KeyError as exc:
        raise ValueError('Invalid evidence') from exc
    if ref['quote'] != text:
        raise ValueError('Invalid quote')
    old = conn.execute('SELECT tenant, payload, status FROM changes WHERE id=?', (change['id'],)).fetchone()
    if old:
        if old[0] != actor['tenant']:
            raise PermissionError('Wrong tenant')
        if json.loads(old[1]) != change:
            raise ValueError('ID reuse')
        return {'id': change['id'], 'status': old[2]}
    with conn:
        conn.execute("INSERT INTO changes VALUES (?, ?, ?, ?, ?, 'pending', '', NULL)",
                     (change['id'], actor['tenant'], change['treaty'], change['section'], json.dumps(change)))
    return {'id': change['id'], 'status': 'pending'}


def publish_change(conn, actor, change_id, reason=''):
    row = conn.execute('SELECT tenant, payload, status FROM changes WHERE id=?', (change_id,)).fetchone()
    if not row or row[0] != actor['tenant'] or actor['role'] != 'approver':
        raise PermissionError('Cannot publish')
    change = json.loads(row[1])
    sources = json.loads(Path(__file__).with_name('sources.json').read_text())
    if not sources[change['source']['document_version']]['signed']:
        raise ValueError('Unsigned source')
    if row[2] == 'published':
        return {'id': change_id, 'status': 'published'}
    for other in list_changes(conn, actor, change['treaty'], change['section']):
        overlap = (change['start'] < (other.get('end') or '9999-12-31') and
                   other['start'] < (change.get('end') or '9999-12-31'))
        if (other['id'] != change_id and other['rate'] != change['rate'] and overlap and
            sources[other['source']['document_version']]['signed'] and not reason.strip()):
            raise ValueError('Conflict needs explicit reason')
    with conn:
        seq = conn.execute('SELECT COALESCE(MAX(published_seq), 0)+1 FROM changes').fetchone()[0]
        conn.execute("UPDATE changes SET status='published', reason=?, published_seq=? WHERE id=?", (reason, seq, change_id))
    return {'id': change_id, 'status': 'published'}


def rate_on(conn, actor, treaty, section, day):
    datetime.date.fromisoformat(day)
    base = conn.execute('SELECT base_rate FROM sections WHERE tenant=? AND treaty=? AND section=?',
                        (actor['tenant'], treaty, section)).fetchone()
    if not base:
        raise KeyError('Section not found')
    for payload, in conn.execute("SELECT payload FROM changes WHERE tenant=? AND treaty=? AND section=? AND status='published' ORDER BY published_seq DESC",
                                (actor['tenant'], treaty, section)):
        change = json.loads(payload)
        if change['start'] <= day and (not change.get('end') or day < change['end']):
            return change['rate']
    return base[0]


def list_changes(conn, actor, treaty, section):
    return [dict(json.loads(p), status=s, reason=r) for p, s, r in
            conn.execute('SELECT payload, status, reason FROM changes WHERE tenant=? AND treaty=? AND section=? ORDER BY id',
                         (actor['tenant'], treaty, section))]
