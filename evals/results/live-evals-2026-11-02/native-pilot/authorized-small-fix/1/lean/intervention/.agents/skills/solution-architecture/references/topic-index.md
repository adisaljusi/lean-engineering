# Topic reference entries

Choose the entry for the current decision and read that file only. Each entry explains the attributed book idea, when it applies, information to inspect, a procedure, an original worked application, trade-offs/simpler choices and verification. These are engineering reference notes, not book excerpts or substitutes for reading the books.

## Source precision

- `author-summary`, `author-pattern-summary`, `author-reference`: public author material was inspected for the named idea. The DDD Reference is Evans’ companion summary, not the full book.
- `publisher-toc`, `author-toc`: the named book/chapter/topic locator was verified. The technical interpretation is attributed synthesis; full passages were not retrieved.
- `publisher-overview`, `author-overview`: identity/scope was checked; no exact chapter/page claim is made.
- `book-synthesis`: the named established pattern is synthesized; the fetched catalog verified book identity, not its full pattern text or precise location.

No unverified chapter/page numbers or quotations are supplied. “Apply”/example/check sections are original Lean Engineering guidance, not claims that a book mandates this exact procedure or implementation. Further/supplementary material is labeled separately, including outbox, CQRS and C4 attribution.

| Topic / decision | Material to load | Book foundation |
|---|---|---|
| Dependency direction and business-rule isolation | [dependency-direction](topics/dependency-direction.md) | Clean Architecture: A Craftsman’s Guide to Software Structure and Design |
| Quality attributes and architectural trade-offs | [quality-attributes](topics/quality-attributes.md) | Fundamentals of Software Architecture (2020) |
| Coupling, cohesion and ownership boundaries | [coupling-and-ownership](topics/coupling-and-ownership.md) | Software Architecture: The Hard Parts (2021) |
| Modular monoliths and distributed services | [monolith-and-services](topics/monolith-and-services.md) | Building Microservices, second edition |
| Incremental migration and compatibility stages | [incremental-migration](topics/incremental-migration.md) | Monolith to Microservices |
| Workloads, access patterns and indexes | [workloads-and-indexes](topics/workloads-and-indexes.md) | Designing Data-Intensive Applications, first edition (2017) |
| Atomicity, isolation and transaction boundaries | [transactions](topics/transactions.md) | Designing Data-Intensive Applications, first edition (2017) |
| Consistency guarantees and application invariants | [consistency](topics/consistency.md) | Designing Data-Intensive Applications, first edition (2017) |
| Replication and stale-read consequences | [replication](topics/replication.md) | Designing Data-Intensive Applications, first edition (2017) |
| Partitioning, skew and cross-partition invariants | [partitioning](topics/partitioning.md) | Designing Data-Intensive Applications, first edition (2017) |
| Batch processing and reproducible inputs | [batch-processing](topics/batch-processing.md) | Designing Data-Intensive Applications, first edition (2017) |
| Streams, checkpoints and derived state | [stream-processing](topics/stream-processing.md) | Designing Data-Intensive Applications, first edition (2017) |
| Request/reply and synchronous versus asynchronous waiting | [request-reply](topics/request-reply.md) | Enterprise Integration Patterns |
| Publish/subscribe and independent consumers | [publish-subscribe](topics/publish-subscribe.md) | Enterprise Integration Patterns |
| Message routing and destination policy | [routing](topics/routing.md) | Enterprise Integration Patterns |
| Message translation and boundary semantics | [transformation](topics/transformation.md) | Enterprise Integration Patterns |
| Correlation, causation and message identity | [correlation](topics/correlation.md) | Enterprise Integration Patterns |
| Ordering, causality and revision scope | [ordering](topics/ordering.md) | Designing Data-Intensive Applications, first edition (2017) |
| Idempotent receivers and duplicate effects | [idempotency](topics/idempotency.md) | Enterprise Integration Patterns |
| Timeouts, retries and partial failure | [timeouts-and-retries](topics/timeouts-and-retries.md) | Designing Data-Intensive Applications, first edition (2017) |
| Backpressure and bounded concurrency | [backpressure](topics/backpressure.md) | Building Microservices, second edition |
| Transactional outbox and consumer inbox | [outbox-inbox](topics/outbox-inbox.md) | Building Microservices, second edition |
| Sagas, compensation and workflow ownership | [sagas](topics/sagas.md) | Building Microservices, second edition |
| CQRS and separate read/write models | [cqrs](topics/cqrs.md) | Designing Data-Intensive Applications, first edition (2017) |
| Event sourcing and authoritative history | [event-sourcing](topics/event-sourcing.md) | Designing Data-Intensive Applications, first edition (2017) |
| Poison messages, quarantine and safe replay | [poison-messages](topics/poison-messages.md) | Enterprise Integration Patterns |
| Observability and operational responsibility | [observability](topics/observability.md) | Building Microservices, second edition |
| Architecture views, audience and visual communication | [visual-communication](topics/visual-communication.md) | Communication Patterns: A Guide for Developers and Architects (2023) |
| C4 context, container and component views | [c4-views](topics/c4-views.md) | Mastering API Architecture (2022) |
