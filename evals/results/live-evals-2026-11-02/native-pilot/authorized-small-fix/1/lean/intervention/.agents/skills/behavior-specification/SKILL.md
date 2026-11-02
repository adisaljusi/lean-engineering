---
name: behavior-specification
description: Turn accepted behavior into concrete acceptance examples and meaningful verification at stable boundaries.
---

# Behavior Specification

Read the request, accepted requirements, domain examples and existing tests. Use when behavior needs examples or an acceptance handoff, not to manufacture a BDD layer for every fix.

Select examples by risk: main outcome, changed boundary, plausible error, authorization, state transition and retry/concurrency effects where consequential. Use actual values and observable outputs, with Given/When/Then if useful. Link to requirement IDs when present. Cover each consequential rule with an example or another named verification method; do not enumerate a Cartesian product.

Load [acceptance examples](references/acceptance.md) for publication, effective dates, conflicting evidence or retry behavior.

Preserve accepted semantics. If an expected result is unknown, explain the missing decision rather than inventing an answer or asking the entire requirements interview again. Tests should observe stable contracts, persisted effects and user outcomes, not private method calls. Quality scenarios can specify bounded latency or recovery under a stated workload separately from functional examples.

Return a compact, reviewable scenario set and real unresolved rules. Do not claim automation or execution from prose. If implementation is already authorized, use the examples to implement and verify; do not impose a fresh approval stop merely for finishing scenarios.
