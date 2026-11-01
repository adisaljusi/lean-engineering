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
| Entities, value objects and precise identity | [identity-and-values](topics/identity-and-values.md) | Domain-Driven Design: Tackling Complexity in the Heart of Software |
| Aggregates, invariants and transaction ownership | [aggregates-and-invariants](topics/aggregates-and-invariants.md) | Domain-Driven Design: Tackling Complexity in the Heart of Software |
| Transaction Script for straightforward operations | [transaction-script](topics/transaction-script.md) | Patterns of Enterprise Application Architecture |
| Domain Model for interacting business rules | [domain-model](topics/domain-model.md) | Patterns of Enterprise Application Architecture |
| Data Mapper and persistence independence | [data-mapper](topics/data-mapper.md) | Patterns of Enterprise Application Architecture |
| Repository as a domain collection boundary | [repository](topics/repository.md) | Patterns of Enterprise Application Architecture |
| Unit of Work and coordinated persistence | [unit-of-work](topics/unit-of-work.md) | Patterns of Enterprise Application Architecture |
| Strategy and replaceable policy | [strategy](topics/strategy.md) | Design Patterns: Elements of Reusable Object-Oriented Software |
| Adapter and an existing incompatible interface | [adapter](topics/adapter.md) | Design Patterns: Elements of Reusable Object-Oriented Software |
| Factory Method and controlled construction | [factory-method](topics/factory-method.md) | Design Patterns: Elements of Reusable Object-Oriented Software |
| Decorator and composable behavior | [decorator](topics/decorator.md) | Design Patterns: Elements of Reusable Object-Oriented Software |
| Algorithm cost and data-structure selection | [algorithm-and-data-structures](topics/algorithm-and-data-structures.md) | Introduction to Algorithms, fourth edition |
| API contracts and consumer-oriented design | [api-contracts](topics/api-contracts.md) | Mastering API Architecture (2022) |
| Schema evolution and backward compatibility | [schema-and-api-evolution](topics/schema-and-api-evolution.md) | Mastering API Architecture (2022) |
| API product lifecycle and consumer change management | [api-lifecycle](topics/api-lifecycle.md) | Continuous API Management, first edition (2018) |
| API governance as explicit decision ownership | [api-governance](topics/api-governance.md) | Continuous API Management, first edition (2018) |
| Bounded contexts, model boundaries and translation | [bounded-contexts](topics/bounded-contexts.md) | Domain-Driven Design: Tackling Complexity in the Heart of Software |
| SOLID as concrete change and contract decisions | [solid](topics/solid.md) | Clean Architecture: A Craftsman’s Guide to Software Structure and Design |
