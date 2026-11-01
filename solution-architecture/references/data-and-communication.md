# Data, workload and communication

Use when storage/process boundaries affect correctness, capacity or recovery. Gather cardinality, access paths, size/skew, latency, outage duration, invariants, retention and operators. Original synthesis informed by DDIA, Enterprise Integration Patterns and the bundled sources.

## Workload and representation

List dominant queries with selectivity/order. Start with existing indexes/libraries; measure a representative query plan and memory/latency before adding storage. Indexes speed reads but cost writes/storage. A hash set has expected O(1) membership at memory cost; sorted structures support ranges at O(log n) lookup and potentially costly insertion. A database index may avoid loading data entirely. Nested candidate comparison is O(n²): 80 documents may be trivial; thousands of spans each change n. Partition by treaty/section/field before comparing; stream rather than build cross-products.

Example: 4 million historical span IDs, 200 references in a run. Do not load every ID into a Python set per request. Resolve the 200 via tenant/version-scoped indexed queries and compare immutable text. Inspect query plan and benchmark realistic skew. Cache only if latency warrants invalidation/retention cost.

Choose transactions by invariant: publication pointer+decision must be atomic. Ask the actual anomaly: can two reviewers both publish against revision 2? Use atomic revision predicates/locking and verify with independent connections. Keep locks short; never wait on humans/models inside a database transaction.

Replication aids reads/availability but stale reads may violate read-after-publication. Route critical reads to writer or use an appropriate consistency mechanism; quantify tolerated staleness. Partitioning changes cross-partition uniqueness/transactions and creates skew/rebalancing cost. Prefer one database until workload/storage/availability warrants it. Batch fits bounded reproducible reprocessing; streams fit ongoing incremental updates. Both need checkpoints/input versions and replay safety.

## Communication by contract

| Mode | Applies when | Handle |
|---|---|---|
| Sync request/reply | Caller needs result now and may fail on dependency outage | Deadline, ambiguous timeout, bounded retries, authorization/load shedding |
| Durable command/job | One owner eventually performs accepted work | Acceptance vs completion, leases, retries/status/idempotency |
| Pub/sub | Independent consumers react to facts | Per-consumer delivery, compatibility/replay, no assumed global order |
| Event stream | Retained per-key history/replay required | Partition/order scope, offsets, lag, retention/rebuild |

A queue does not make a transaction atomic. Define durable acceptance, acknowledgment and retry ownership. Bound queues/concurrency; apply admission control/backpressure rather than exhaust memory. A timeout bounds waiting, not necessarily remote work. Propagate cancellation/deadlines where supported; reconcile ambiguous outcomes by identity. Retry transient failures with bounded exponential delay/jitter, not invalid commands forever. Quarantine poison messages with reason/owner/safe replay; never silently discard financial work. Correlation IDs connect request/reply/async steps; they do not authorize access.

## Delivery trace and pattern selection

Order O7 and outbox E7 commit atomically. Relay publishes E7 and crashes before marking sent, so publishes again. Consumer inserts inbox E7 and effect in one transaction, acknowledges after commit. Duplicate E7 has no new effect; same ID/different payload is an integrity error. For an external charge, SQL inbox alone cannot ensure exactly-once effect: use provider idempotency or reconcile outcome.

Outbox prevents local commit/notification divergence at the cost of relay, retention, lag and duplicate handling. Inbox protects duplicate-sensitive consumers with storage/expiry cost. Prefer a local transaction when all effects share a database and async work is unnecessary. Define ordering scope (often order ID), revision/gap handling and stale-transition policy. Never imply global order for free.

- Saga: use when multi-owner business actions cannot be atomic and need compensation/reconciliation. Specify commits, timeouts, compensation and manual unresolved states. Compensation is a new action, not erased history. Orchestration clarifies progress/recovery ownership; choreography reduces central coupling but can hide cycles/responsibility. Prefer one transaction if possible.
- CQRS: separate read/write models when shapes/scaling justify projection lag, rebuild and contract costs. A SQL query/view may suffice; separate stores are not required.
- Event sourcing: use when business reconstruction from authoritative events warrants evolving schemas, snapshots, projection rebuilds and correction semantics. Audit rows/current state are simpler for ordinary history. Retained evidence alone does not warrant event sourcing.
- Routing/transformation: route commands to owners and transform transport at boundaries. Avoid a generic integration bus for one caller or exposing internal tables as external schemas.

## Evolution and proof

Expand first: accept old/new representations with conflict rules, deploy compatible readers, backfill/reconcile, migrate producers, observe old usage, then remove support. Additive fields can break strict decoders; enum additions can break exhaustive clients. Test actual consumers. State rollback's irreversible point.

Verify duplicate/reordered delivery, retry exhaustion, timeout after remote success, crashes around commit/ack, version skew and backlog recovery. Measure throughput/oldest pending age under representative bursts. Log correlation/run IDs, revisions, status and diagnosable errors without sensitive text; name operator/alert response. Missing operational responsibility is a design gap even with a tidy happy-path diagram.

## Topic material before choosing a data/integration pattern

Read the relevant entry for its attributed idea, applicability, procedure and example; do not load all entries by default.

- [Workloads, access patterns and indexes](topics/workloads-and-indexes.md).
- [Atomicity, isolation and transaction boundaries](topics/transactions.md).
- [Consistency guarantees and application invariants](topics/consistency.md).
- [Replication and stale-read consequences](topics/replication.md).
- [Partitioning, skew and cross-partition invariants](topics/partitioning.md).
- [Batch processing and reproducible inputs](topics/batch-processing.md).
- [Streams, checkpoints and derived state](topics/stream-processing.md).
- [Request/reply and synchronous versus asynchronous waiting](topics/request-reply.md).
- [Publish/subscribe and independent consumers](topics/publish-subscribe.md).
- [Message routing and destination policy](topics/routing.md).
- [Message translation and boundary semantics](topics/transformation.md).
- [Correlation, causation and message identity](topics/correlation.md).
- [Ordering, causality and revision scope](topics/ordering.md).
- [Idempotent receivers and duplicate effects](topics/idempotency.md).
- [Timeouts, retries and partial failure](topics/timeouts-and-retries.md).
- [Backpressure and bounded concurrency](topics/backpressure.md).
- [Transactional outbox and consumer inbox](topics/outbox-inbox.md).
- [Sagas, compensation and workflow ownership](topics/sagas.md).
- [CQRS and separate read/write models](topics/cqrs.md).
- [Event sourcing and authoritative history](topics/event-sourcing.md).
- [Poison messages, quarantine and safe replay](topics/poison-messages.md).
- [Observability and operational responsibility](topics/observability.md).
