# Implement and prove the selected behavior

Use for authorized delivery. Start from current source and an observable contract; a requested implementation authorizes ordinary reversible technical choices. Design-only requests do not.

Procedure: reproduce with an existing or new meaningful failing check; observe why it failed; change owning code; run the check; inspect and simplify; run relevant regressions. A wrong failure (missing dependency/import) is not evidence the business regression exists. Use existing tools; no test framework migration for a style preference.

## Worked database retry

Public contract: stable event identity; identical retry has one ledger effect; same identity/different amount is conflict; failed effect permits retry. Inspect current schema and transaction behavior. A pre-insert SELECT alone races across connections. Put database uniqueness on event ID and event+effect in one transaction. Catch the specific identity conflict, compare stored payload, and reject altered reuse. Do not catch every IntegrityError as success.

Test identical retry against a real database; test independent connections; inject a failure after event acceptance but before ledger insertion and confirm rollback leaves no half-effect and permits retry. Verify legacy duplicate migration preserves valid history and refuses ambiguous conflicting data. Mocks cannot establish these constraints. A broker/Redis cache is not needed for this local atomic invariant; if effects span services, use the distributed contract and test its partial failures instead.

## Python implementation decisions

Use a function for one operation, a module for cohesive policy, a dataclass for precise data and a stateful class for a real lifecycle. Type hints do not validate JSON; reject invalid units/ranges and unknown values at boundaries. Database constraints enforce shared-write invariants. Name transaction owner; do not hold locks during remote calls. SQLite connection contexts commit/rollback but do not close; use closing or explicit try/finally. Translate expected domain errors at transport boundary; preserve unexpected causes and log IDs/error category without sensitive content.

Async only helps nonblocking I/O. Blocking clients in async handlers block the loop; reuse an appropriate client or bounded executor. Bound both queued work and active calls; cancellation of a wait does not undo an external effect. Stable identity/status/reconciliation handle ambiguous timeouts. Select dict/set/index/streaming by actual cardinality/access patterns; measure before optimizing.

Tests observe stable behavior, not every helper. Keep important domain checks, real changed integrations and critical workflows; omit redundant private-method mirrors. For low-impact edits, existing regression/static checks may suffice. Verify humans can follow the important flow and diagnose a failing check. Further detail: Python sqlite3/contextlib/asyncio documentation at https://docs.python.org/3/ ; DDIA and Enterprise Integration Patterns inform transaction/delivery reasoning. These examples do not establish production behavior.
