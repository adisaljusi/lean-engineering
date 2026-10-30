# Architecture decisions from evidence

Architecture addresses costly interactions among responsibilities, deployment, data and quality constraints. Use when a choice changes ownership, failure modes or long-lived contracts. For a local fix keep only the affected dependency and behavior.

## Procedure

1. Inspect entry points, calls/imports, schemas, deployables, configuration, operational evidence and previous decisions. Separate observed structure from inference. Name capabilities and operational owners.
2. Trace an important request and its data through owners/transactions. Identify shared writes, synchronous waits, asynchronous acknowledgments and trust boundaries.
3. Choose drivers distinguishing options: workload/skew, tail latency, allowed staleness, invariants, crash recovery, availability, privacy, cost and team ownership. Use concrete scenarios, not a generic qualities checklist.
4. Find the smallest credible change; compare serious alternatives for consequential choices. State constraints met, failure modes, implementation/operating costs and uncertainty. An option violating a hard invariant is not a cheap winner.
5. Recommend for today's evidence. Give consequences, verification and revisit triggers with measurable/organizational conditions.
6. For migrations specify compatibility window, backfill/dual-write hazards, ownership cutover, rollout, rollback and irreversible points. Verify old/new clients and data before removal.

## Boundaries and dependencies

Following Robert C. Martin's *Clean Architecture*, isolate business policy from volatile transport/storage where that volatility has real cost. A Python HTTP handler parses input and calls a domain function; a transaction-owning service supplies state and persists results. Domain code need not import FastAPI or vendor SDKs. A small CRUD handler may use SQL directly where no independent policy needs isolation. Introduce a port for actual adapter substitution, independent policy or a meaningful test seam; no interface per function.

Following Evans' DDD, boundaries follow language, invariants, ownership and lifecycle. “Customer” in billing/support may have different responsibilities. Do not turn every noun into an entity. Keep an atomic invariant in one transaction-owning boundary unless distributed cost is justified. Same-process modules can own tables and expose operations rather than permitting arbitrary cross-writes.

Newman's microservices work and *Software Architecture: The Hard Parts* inform the split: a service is an operational/ownership boundary. Independent deployment, scaling or failure isolation may warrant it. Costs include network latency, partial failure, eventual consistency, contract evolution, debugging and on-call work. A modular monolith fits coordinated releases/shared invariants. Measure coupling through changes and runtime dependencies, not box counts.

## Worked choice: reviewed extraction today

Observed: Python application, PostgreSQL, object storage, model gateway, one team. Need: 10–80 PDFs/run, preserved evidence and human review. Workload/recovery targets unmeasured.

| Option | Fit | Cost |
|---|---|---|
| Existing modules + durable job rows | Existing storage and transactions; crash recovery possible | Polling/leases, expiry, shared deployment/scaling |
| Separate worker on same job contract | Isolates slow model I/O and worker crashes | Another deployable/operator and versioned contract |
| Service/document type + broker | No independent ownership/scaling evidence yet | Distributed joins, duplicates, tracing and rollout |

Recommend modules plus durable acceptance; a worker deployable if requests cannot cover measured model latency. Reuse existing workers when available. An in-memory background task does not survive crash. Verify restart recovery, gateway bounds, tenant isolation and evidence. Revisit service ownership when independent release/SLO needs emerge or measured extraction load harms interactive latency despite resource isolation. Adopt a broker only with a benefit over durable storage and ownership/replay policy.

## Worked choice: distributed settlement

Facts: payments/fulfillment independently own databases; acceptance must survive a 24-hour fulfillment outage; committed orders must not lose fulfillment requests; notifications may be eventually consistent. No shared distributed transaction.

Credible options: existing broker with transactional outbox at order owner; or persisted HTTP dispatcher with sufficient outage capacity/retry operations. Both must retain accepted work and deduplicate effects. Recommend the existing broker when buffering, fan-out and replay are already operated capabilities: order+outbox atomic commit, relay with stable event ID, consumer inbox+effect atomic commit, acknowledgment after commit. Delivery is at least once; uniqueness makes the local effect idempotent.

Costs: stale state, duplicate traffic, version compatibility, replay and on-call ownership. If stock must be reserved before charging, settle compensation/reconciliation policy; messaging does not solve the business rule. Verify publish-before-mark crash, duplicates, outage recovery and version skew. One process/database is simpler if independent ownership/outage constraints disappear; do not merge regulated stores merely to simplify a diagram.

A useful decision explains problem/current facts, options, choice/why now, costs, assumptions, migration/verification and revisit evidence. Use an ADR/table when useful, not mandatory forms. Attribution/further reading: the bundled sources guide.
