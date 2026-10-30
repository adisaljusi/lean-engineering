"""Runnable teaching slice: reviewed publication, Python 3.10+ and SQLite.

Caller owns/ closes connection. This does not implement source ingestion, tenant
identity verification, multi-interval precedence, HTTP, or distributed delivery.
"""
from dataclasses import dataclass
import sqlite3


class StaleReview(Exception):
    """Another accepted decision changed the reviewed revision."""


@dataclass(frozen=True)
class Rate:
    bps: int

    def __post_init__(self):
        if type(self.bps) is not int or not 0 <= self.bps <= 10000:
            raise ValueError("rate must be integer basis points in 0..10000")


def initialize(conn: sqlite3.Connection) -> None:
    # Schema setup is separate from request transactions. No executescript in
    # publication: sqlite3.executescript may commit an existing transaction.
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS sections (
            tenant TEXT NOT NULL,
            section TEXT NOT NULL,
            bps INTEGER NOT NULL CHECK (typeof(bps) = 'integer' AND bps BETWEEN 0 AND 10000),
            revision INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY (tenant, section)
        );
        CREATE TABLE IF NOT EXISTS decisions (
            tenant TEXT NOT NULL,
            section TEXT NOT NULL,
            request_id TEXT NOT NULL,
            expected_revision INTEGER NOT NULL,
            bps INTEGER NOT NULL CHECK (typeof(bps) = 'integer' AND bps BETWEEN 0 AND 10000),
            reason TEXT NOT NULL CHECK (length(trim(reason)) > 0),
            actor_id TEXT NOT NULL,
            PRIMARY KEY (tenant, request_id),
            FOREIGN KEY (tenant, section) REFERENCES sections (tenant, section)
        );
    """)
    conn.execute("PRAGMA foreign_keys = ON")


def publish(conn: sqlite3.Connection, *, tenant: str, section: str,
            actor_id: str, role: str, request_id: str,
            expected_revision: int, rate: Rate, reason: str) -> int:
    """Commit one reviewed decision, or reject stale/conflicting retry.

    tenant/actor_id/role must come from trusted authentication, not request JSON.
    An identical retry returns the committed revision, even if state moved on.
    The connection must not already own another transaction.
    """
    if conn.in_transaction:
        raise RuntimeError("publish must own its transaction")
    if role != "approver":
        raise PermissionError("approver required")
    if not actor_id or not request_id or not reason.strip():
        raise ValueError("actor, request identity and reason are required")
    if type(expected_revision) is not int or expected_revision < 0:
        raise ValueError("invalid revision")
    payload = (section, expected_revision, rate.bps, reason, actor_id)
    try:
        # Serialize this small SQLite write; compare-and-update protects the
        # revision contract too. Other databases need their own lock behavior.
        conn.execute("BEGIN IMMEDIATE")
        previous = conn.execute(
            "SELECT section, expected_revision, bps, reason, actor_id "
            "FROM decisions WHERE tenant=? AND request_id=?",
            (tenant, request_id),
        ).fetchone()
        if previous is not None:
            if previous != payload:
                raise ValueError("request identity reused with different data")
            conn.commit()
            return expected_revision + 1
        changed = conn.execute(
            "UPDATE sections SET bps=?, revision=revision+1 "
            "WHERE tenant=? AND section=? AND revision=?",
            (rate.bps, tenant, section, expected_revision),
        )
        if changed.rowcount != 1:
            raise StaleReview("section missing or review revision changed")
        conn.execute(
            "INSERT INTO decisions VALUES (?, ?, ?, ?, ?, ?, ?)",
            (tenant, section, request_id, expected_revision, rate.bps, reason, actor_id),
        )
        conn.commit()
        return expected_revision + 1
    except BaseException:
        conn.rollback()
        raise
