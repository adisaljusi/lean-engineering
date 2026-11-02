---
name: solution-architecture
description: Inspect and design system boundaries, ownership and execution/data flows; compare architectural alternatives, failure behavior, migration and evolution with useful diagrams.
---

# Solution Architecture

Use for consequential system choices or architecture explanation. Inspect the current code, topology, schema, deployment configuration, contracts, operational evidence and previous decisions before recommending changes. Label gaps in evidence; do not invent an as-is architecture.

Choose depth: a local change may need a paragraph and dependency sketch; cross-process/state changes need explicit flows, quality drivers and failure handling. Identify business capabilities and owners, then workload, consistency, recovery, security, cost and team constraints that actually distinguish options.

When applying a named book concept, read its [topic reference entry](references/topic-index.md) for the material and decision procedure. Select only the relevant entry; a book title or source link alone is not guidance.

Select references, do not read the whole library:

- [Architecture decisions](references/decisions.md): module/service boundaries, dependency direction, alternatives, current versus future, migration and worked monolith/distributed choices.
- [Data and communication](references/data-and-communication.md): transactions, workloads, algorithms, messaging, outbox/inbox, recovery, sagas and schema evolution when data or process boundaries matter.
- [Visual architecture](references/visuals.md): choose and validate a diagram for the question; current/proposed flow and multi-document evidence example.
- [Extraction worked example](references/extraction.md): immutable OCR evidence, conflicts, normalization, human decisions and reproducible runs.
- [Sources](references/sources.md): attributed foundations and further reading; methods above are original synthesis, not book excerpts.

Describe the current system and smallest credible change. Compare credible alternatives only for consequential choices; explain recommendation, costs, assumptions, verification and evidence that would change it. Distinguish current, proposed and possible future architecture. Future options need adoption triggers and operating costs, not speculative implementation.

Include compatibility, rollout/rollback, ownership and observability where affected. Use an existing design note or ADR only when useful. Match actual authorization: design-only stops at a proposal; authorized implementation proceeds without phase approval. Avoid both unjustified infrastructure and omitting necessary durability, isolation or recovery to look simple.
