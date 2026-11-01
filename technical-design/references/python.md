# Practical Python decisions

Use for implementing an accepted design, especially at resource, data or concurrency boundaries. Inspect Python version, pyproject/lockfiles, module layout, typing/test tools and dependency policy first. Reuse them; do not introduce a formatter/framework merely to express preferences.

## Choose representations and boundaries

Use functions for stateless transformations and cohesive modules for related behavior. Use a dataclass for a named data record; frozen data reduces accidental mutation but does not validate values or make nested collections immutable. Use a class when identity/state/resource lifecycle or several coherent operations warrant it. Avoid a class per command, forwarding wrappers and helpers extracted solely to shorten lines.

Type hints explain contracts but do not validate network/JSON input. At boundaries validate shape, units, ranges and authorization using existing libraries (Pydantic if already present, explicit checks for a small input). Parse decimals/dates once, reject ambiguous values and preserve unknown/null distinctions. Python bool is an int subclass: reject it for quantities where true is not 1. Enforce cross-writer constraints in the database too.

A Protocol can express a real boundary: for example `ModelGateway.extract(request) -> ExtractionResult` if vendor adapters differ and application policy must not depend on them. Inject the adapter through a function argument/constructor. Do not add a container or interface for every collaborator. ABC/GoF strategy patterns are warranted by substitutable behavior, not a desire for pattern vocabulary. Prefer a callable for one operation unless a richer protocol helps.

## Transactions, exceptions and resources

Name the connection/transaction owner; keep transactions short and atomic for shared invariants. A SQLite connection context commits/rolls back but does NOT close the connection: use `contextlib.closing` as well. PostgreSQL/ORM context behavior differs; check the library. Handle unique conflicts narrowly, compare stored payload on retry and let unexpected database failures propagate with context. Do not swallow all IntegrityErrors as duplicate success.

Define stable domain errors where callers need distinctions (invalid input, permission denied, stale revision, transient dependency failure). Map them to transport errors at the boundary. Preserve causes (`raise ... from exc`) when translating. Never log credentials or full sensitive documents. Include correlation/run/entity identity, operation, revision and error category so humans can diagnose failures.

## Sync, async and bounded work

Use synchronous code for synchronous libraries/small local work. Async helps overlapping I/O when dependencies support it; it does not speed CPU-bound Python. A blocking HTTP/DB call inside `async def` blocks the event loop. Reuse an async client or a bounded thread executor where safe; don't share thread-affine connections. CPU work may need processes or a durable worker when measured. Bound queued work as well as active calls: a semaphore around millions of eagerly created tasks still consumes memory. Use a bounded producer/consumer queue or limited batches.

Resource ownership includes cancellation: `async with` for clients, try/finally for cleanup, propagate cancellation, set network deadlines and avoid canceling a local wait as if it undid a remote side effect. Record durable status and reconcile ambiguous results. Structured concurrency can help related task lifetime on supported Python versions; do not require a new runtime without cause.

## Workload and algorithms

Choose by access pattern/cardinality: list for ordered traversal, dict/set for expected constant-time lookup, deque for FIFO, heapq for a bounded top-k. Sorting is O(n log n) and uses memory; avoid sorting everything for one maximum. A quadratic join of spans can dominate extraction; group/index by section/field or let the database filter. Stream large pages/batches and measure representative size/skew. Reuse standard libraries/database indexes before inventing structures.

## Packaging and verification

Keep production configuration explicit and validate required settings at startup. Reuse repository entry points, dependency locks and environment conventions; no generic starter framework. Do not read configuration/secrets on import when it prevents normal testing or leaks global state.

Test domain invariants with values, database integration with real constraints/rollback and independent connections for races, contracts with old/new consumers and critical workflows across meaningful boundaries. Avoid a test per private method or excessive mocks. Use existing logging/type/lint/test commands if available. A runnable standard-library publication slice is bundled in `examples/`; it demonstrates transactions/revision conflicts and explicitly limits its scope.

Further detail: Python docs on dataclasses, typing.Protocol, contextlib, sqlite3, asyncio task cancellation/queues, heapq and packaging at https://docs.python.org/3/ and https://packaging.python.org/ . These procedures are original synthesis; Python version/library behavior must be checked against the target repository.

For book-derived concepts used here, select the relevant entry in the [topic index](topic-index.md), including domain identity/invariants, persistence patterns, SOLID/GoF choices, algorithms and API contracts/evolution. The topic entries distinguish attributed ideas from original application examples; Python API behavior remains grounded in its official documentation.
