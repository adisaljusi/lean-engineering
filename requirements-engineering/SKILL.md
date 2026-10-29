---
name: requirements-engineering
description: Turn a clarified feature idea into precise functional and non-functional requirements, business rules, scope, traceable IDs and measurable quality constraints before architecture or coding.
---

# Requirements Engineering

Read domain docs, existing capabilities, constraints and stakeholder decisions. Document outcome, actors, in-scope and excluded behavior; distinguish business rules from solution ideas. Give each requirement an ID (`R1`, `R2`). Define domain language, invariants, triggers, states, authorization, exceptions and dependencies.

Capture quality attributes only when they matter: latency, throughput, availability, recovery, security/privacy, auditability, interoperability, cost and maintainability. Express measurable scenarios or explicitly mark targets unknown. Identify affected existing behavior and compatibility constraints. Ask about contradictions rather than inventing answers.

Produce/update `spec.md` under repository conventions. Gate: no material ambiguity is silently assumed. Do not design services, database tables or algorithms in the requirements phase.
