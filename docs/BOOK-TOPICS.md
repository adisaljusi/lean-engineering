# Book material by engineering topic

This catalogue points to reference entries that **explain the material**, not only to book/source pages. Each entry contains the attributed concept, when to use it, required information, application procedure, original worked example, trade-offs/simpler choices and verification. The reference entry is what the agent reads for the decision; source links document provenance and further reading.

Scope: the book-derived engineering topics taught by this library, not a reproduction or exhaustive index of every chapter/pattern in every book. Existing Python guides rely on official language/library documentation rather than an invented Python book. The ambiguous title “API Architecture” remains unresolved; concrete API material uses the identified Mastering API Architecture and Continuous API Management titles.

Source precision is recorded per entry. Public author summaries can substantiate named ideas; publisher/author tables of contents substantiate chapter/topic locators. A verified locator is not a claim that the complete passage was retrieved. GoF entries mark named-pattern synthesis where only book identity was verified. No unavailable page numbers, quotations or claims of reading full books are invented. All procedures/examples are original Lean Engineering applications, not attributed book prescriptions. Entries do not require external book/network access at runtime.

## Find a topic

### solution-architecture

| Topic | Material reference | Book / location |
|---|---|---|
| Dependency direction and business-rule isolation | [Read entry](../solution-architecture/references/topics/dependency-direction.md) | Clean Architecture: A Craftsman’s Guide to Software Structure and Design; Chapter 22: The Clean Architecture — The Dependency Rule; supplemented by the author’s Dependency Rule / boundary-crossing article |
| Quality attributes and architectural trade-offs | [Read entry](../solution-architecture/references/topics/quality-attributes.md) | Fundamentals of Software Architecture (2020); Chapters 4–6: Architecture Characteristics Defined; Identifying Architectural Characteristics; Measuring and Governing Architecture Characteristics |
| Coupling, cohesion and ownership boundaries | [Read entry](../solution-architecture/references/topics/coupling-and-ownership.md) | Software Architecture: The Hard Parts (2021); Chapter 2: Discerning Coupling in Software Architecture; Chapter 3: Architectural Modularity |
| Modular monoliths and distributed services | [Read entry](../solution-architecture/references/topics/monolith-and-services.md) | Building Microservices, second edition; Second edition, Chapters 1–4: What Are Microservices?; How to Model Microservices; Splitting the Monolith; Microservice Communication Styles |
| Incremental migration and compatibility stages | [Read entry](../solution-architecture/references/topics/incremental-migration.md) | Monolith to Microservices; Author topic list: incremental decomposition, migration patterns and database decomposition |
| Workloads, access patterns and indexes | [Read entry](../solution-architecture/references/topics/workloads-and-indexes.md) | Designing Data-Intensive Applications, first edition (2017); Chapter 3: Storage and Retrieval — indexing structures; Transaction Processing or Analytics? |
| Atomicity, isolation and transaction boundaries | [Read entry](../solution-architecture/references/topics/transactions.md) | Designing Data-Intensive Applications, first edition (2017); Chapter 7: Transactions — Preventing Lost Updates; Write Skew and Phantoms; Serializability |
| Consistency guarantees and application invariants | [Read entry](../solution-architecture/references/topics/consistency.md) | Designing Data-Intensive Applications, first edition (2017); Chapter 9: Consistency and Consensus — Consistency Guarantees; Linearizability; Ordering Guarantees |
| Replication and stale-read consequences | [Read entry](../solution-architecture/references/topics/replication.md) | Designing Data-Intensive Applications, first edition (2017); Chapter 5: Replication — Synchronous Versus Asynchronous Replication; Handling Node Outages; Reading Your Own Writes |
| Partitioning, skew and cross-partition invariants | [Read entry](../solution-architecture/references/topics/partitioning.md) | Designing Data-Intensive Applications, first edition (2017); Chapter 6: Partitioning — Skewed Workloads and Relieving Hot Spots; Secondary Indexes; Rebalancing Partitions |
| Batch processing and reproducible inputs | [Read entry](../solution-architecture/references/topics/batch-processing.md) | Designing Data-Intensive Applications, first edition (2017); Chapter 10: Batch Processing — Batch Processing with Unix Tools; The Output of Batch Workflows; Materialization of Intermediate State |
| Streams, checkpoints and derived state | [Read entry](../solution-architecture/references/topics/stream-processing.md) | Designing Data-Intensive Applications, first edition (2017); Chapter 11: Stream Processing — Partitioned Logs; Reasoning About Time; Fault Tolerance |
| Request/reply and synchronous versus asynchronous waiting | [Read entry](../solution-architecture/references/topics/request-reply.md) | Enterprise Integration Patterns; Named pattern: Request-Reply |
| Publish/subscribe and independent consumers | [Read entry](../solution-architecture/references/topics/publish-subscribe.md) | Enterprise Integration Patterns; Named pattern: Publish-Subscribe Channel |
| Message routing and destination policy | [Read entry](../solution-architecture/references/topics/routing.md) | Enterprise Integration Patterns; Named pattern: Message Router |
| Message translation and boundary semantics | [Read entry](../solution-architecture/references/topics/transformation.md) | Enterprise Integration Patterns; Named pattern: Message Translator |
| Correlation, causation and message identity | [Read entry](../solution-architecture/references/topics/correlation.md) | Enterprise Integration Patterns; Named pattern: Correlation Identifier |
| Ordering, causality and revision scope | [Read entry](../solution-architecture/references/topics/ordering.md) | Designing Data-Intensive Applications, first edition (2017); Chapter 9: Consistency and Consensus — Ordering and Causality; Sequence Number Ordering; Total Order Broadcast |
| Idempotent receivers and duplicate effects | [Read entry](../solution-architecture/references/topics/idempotency.md) | Enterprise Integration Patterns; Named pattern: Idempotent Receiver |
| Timeouts, retries and partial failure | [Read entry](../solution-architecture/references/topics/timeouts-and-retries.md) | Designing Data-Intensive Applications, first edition (2017); Chapter 8: The Trouble with Distributed Systems — Faults and Partial Failures; Timeouts and Unbounded Delays |
| Backpressure and bounded concurrency | [Read entry](../solution-architecture/references/topics/backpressure.md) | Building Microservices, second edition; Second edition, Chapter 12: Resiliency; Chapter 13: Scaling |
| Transactional outbox and consumer inbox | [Read entry](../solution-architecture/references/topics/outbox-inbox.md) | Building Microservices, second edition; Second edition, Chapter 6: Workflow (distributed-workflow context); outbox mechanism verified separately in author pattern material |
| Sagas, compensation and workflow ownership | [Read entry](../solution-architecture/references/topics/sagas.md) | Building Microservices, second edition; Second edition, Chapter 6: Workflow — Sagas and distributed transactions |
| CQRS and separate read/write models | [Read entry](../solution-architecture/references/topics/cqrs.md) | Designing Data-Intensive Applications, first edition (2017); Related DDIA material: Chapter 11, Databases and Streams; this named CQRS interpretation is supported by Fowler’s supplementary article |
| Event sourcing and authoritative history | [Read entry](../solution-architecture/references/topics/event-sourcing.md) | Designing Data-Intensive Applications, first edition (2017); Chapter 11: Stream Processing — Event Sourcing; State, Streams, and Immutability |
| Poison messages, quarantine and safe replay | [Read entry](../solution-architecture/references/topics/poison-messages.md) | Enterprise Integration Patterns; Named pattern: Dead Letter Channel |
| Observability and operational responsibility | [Read entry](../solution-architecture/references/topics/observability.md) | Building Microservices, second edition; Second edition, Chapter 10: From Monitoring to Observability; Chapter 12: Resiliency |
| Architecture views, audience and visual communication | [Read entry](../solution-architecture/references/topics/visual-communication.md) | Communication Patterns: A Guide for Developers and Architects (2023); Chapters 1–6: visual communication; Chapter 10: Knowledge Management Principles; Chapter 12: Effective Practices |
| C4 context, container and component views | [Read entry](../solution-architecture/references/topics/c4-views.md) | Mastering API Architecture (2022); Introduction — Using C4 Diagrams; C4 Context Diagram; C4 Container Diagram; C4 Component Diagram |

### technical-design

| Topic | Material reference | Book / location |
|---|---|---|
| Entities, value objects and precise identity | [Read entry](../technical-design/references/topics/identity-and-values.md) | Domain-Driven Design: Tackling Complexity in the Heart of Software; DDD Reference named patterns: Entities; Value Objects |
| Aggregates, invariants and transaction ownership | [Read entry](../technical-design/references/topics/aggregates-and-invariants.md) | Domain-Driven Design: Tackling Complexity in the Heart of Software; DDD Reference named pattern: Aggregates; consistency boundary guidance |
| Transaction Script for straightforward operations | [Read entry](../technical-design/references/topics/transaction-script.md) | Patterns of Enterprise Application Architecture; Named pattern: Transaction Script (author catalog identifies Chapter 09) |
| Domain Model for interacting business rules | [Read entry](../technical-design/references/topics/domain-model.md) | Patterns of Enterprise Application Architecture; Named pattern: Domain Model (author catalog identifies Chapter 09) |
| Data Mapper and persistence independence | [Read entry](../technical-design/references/topics/data-mapper.md) | Patterns of Enterprise Application Architecture; Named pattern: Data Mapper |
| Repository as a domain collection boundary | [Read entry](../technical-design/references/topics/repository.md) | Patterns of Enterprise Application Architecture; Named pattern: Repository |
| Unit of Work and coordinated persistence | [Read entry](../technical-design/references/topics/unit-of-work.md) | Patterns of Enterprise Application Architecture; Named pattern: Unit of Work |
| Strategy and replaceable policy | [Read entry](../technical-design/references/topics/strategy.md) | Design Patterns: Elements of Reusable Object-Oriented Software; Named GoF pattern: Strategy; exact chapter/page not retrieved |
| Adapter and an existing incompatible interface | [Read entry](../technical-design/references/topics/adapter.md) | Design Patterns: Elements of Reusable Object-Oriented Software; Named GoF pattern: Adapter; exact chapter/page not retrieved |
| Factory Method and controlled construction | [Read entry](../technical-design/references/topics/factory-method.md) | Design Patterns: Elements of Reusable Object-Oriented Software; Named GoF pattern: Factory Method; exact chapter/page not retrieved |
| Decorator and composable behavior | [Read entry](../technical-design/references/topics/decorator.md) | Design Patterns: Elements of Reusable Object-Oriented Software; Named GoF pattern: Decorator; exact chapter/page not retrieved |
| Algorithm cost and data-structure selection | [Read entry](../technical-design/references/topics/algorithm-and-data-structures.md) | Introduction to Algorithms, fourth edition; Algorithm analysis and data structures; no chapter/page locator claimed |
| API contracts and consumer-oriented design | [Read entry](../technical-design/references/topics/api-contracts.md) | Mastering API Architecture (2022); Chapters 1–2: Design, Build, and Specify APIs; Testing APIs |
| Schema evolution and backward compatibility | [Read entry](../technical-design/references/topics/schema-and-api-evolution.md) | Mastering API Architecture (2022); Chapter 1: Design, Build, and Specify APIs — API Versioning; Detecting Changes |
| API product lifecycle and consumer change management | [Read entry](../technical-design/references/topics/api-lifecycle.md) | Continuous API Management, first edition (2018); First edition, Chapters 3–6: The API as a Product; The Ten Pillars of an API Product; Continuous API Improvement; The API Product Lifecycle |
| API governance as explicit decision ownership | [Read entry](../technical-design/references/topics/api-governance.md) | Continuous API Management, first edition (2018); First edition, Chapter 2: API Governance — governing decisions; centralization/decentralization; governance patterns |
| Bounded contexts, model boundaries and translation | [Read entry](../technical-design/references/topics/bounded-contexts.md) | Domain-Driven Design: Tackling Complexity in the Heart of Software; DDD Reference named patterns: Bounded Context; Context Map; Anti-Corruption Layer |
| SOLID as concrete change and contract decisions | [Read entry](../technical-design/references/topics/solid.md) | Clean Architecture: A Craftsman’s Guide to Software Structure and Design; Part III, Chapters 7–11: SRP, OCP, LSP, ISP and DIP |

### grill-with-docs

| Topic | Material reference | Book / location |
|---|---|---|
| Ubiquitous language and business meaning | [Read entry](../grill-with-docs/references/topics/ubiquitous-language.md) | Domain-Driven Design: Tackling Complexity in the Heart of Software; DDD Reference named pattern: Ubiquitous Language; language within Bounded Context |

## Relation to workflows and validation

[Task playbooks](../lean-engineer/references/workflows.md) select work and handoffs; topic entries supply the material for a specific engineering decision. They remain independently installed with their owning skills. Read one relevant entry, not an entire book library on every task.

The [bibliography](../solution-architecture/references/sources.md) remains useful for attribution. Actual research/access and packaging/static checks for these topic entries are retained under `evals/results/book-topics/`. No new model-behavior or effectiveness result is inferred from their presence.
