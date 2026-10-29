---
name: technical-design
description: Produce and review concrete technical designs: field-level data definitions, domain and persistence models, data structures, coding patterns, component interfaces, algorithms, error flows and explicit approval before implementation.
---

# Technical Design

Read the approved requirements and solution architecture, plus existing repository modules and conventions. Extend `design.md` with only relevant details:

- **Domain model:** entities, value objects, aggregates, invariants, states, identity, ownership and lifecycle.
- **Data definitions:** every important field's name, meaning, type, nullability, validation, default, constraints, provenance, versioning and approval owner. Distinguish unknown, absent, null and invalid values where significant.
- **Structures and persistence:** collections/DTOs/records/enums, relationships, keys, indexes, transaction boundaries, schema evolution and migration compatibility.
- **Contracts:** public interfaces, function/method signatures where consequential, APIs, events, errors, versioning and boundary transformations.
- **Component design:** class/module responsibilities, dependency direction, layering, and dependency injection or coding patterns only when they solve an identified issue.
- **Execution:** algorithms, state transitions, concurrency control, idempotency, validation, error/recovery paths, performance implications and test seams.

Present at least two realistic design options for difficult decisions. Ask hard questions: Is this an entity or value object? Who owns the source of truth? Should the model be mutable? Why use an abstraction rather than a function? Define acceptance of data semantics with the domain/data owner when available. Mark proposed vs approved definitions.

**Gate:** Do not mark technical design approved or proceed to implementation when material model definitions, contracts or patterns lack human approval. Favor design only to the depth needed to make implementation unambiguous.
