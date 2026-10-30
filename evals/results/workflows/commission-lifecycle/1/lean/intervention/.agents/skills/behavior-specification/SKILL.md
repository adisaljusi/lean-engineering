---
name: behavior-specification
description: Define behavior-driven acceptance scenarios and testable examples for software features, including domain rules, edge cases, errors, permissions and state changes, before technical design.
---

# Behavior Specification

Transform approved requirements into observable scenarios. Use clear `Given / When / Then` examples with IDs (`AC1 [R1]`). Include happy paths, invalid/boundary inputs, state transitions, permission failures, retries, duplicates and concurrency when applicable. Assert externally visible effects, not private class design.

For each requirement identify at least one acceptance scenario or an explicit other verification method. Use concrete data and expected outputs; detect conflicting and missing rules. Note quality scenarios (performance, recovery, security) separately from functional BDD scenarios. Cucumber syntax is optional; automation-ready behavior is the goal.

Update `spec.md`; present the scenario set for stakeholder approval. Do not generate code or assume business behavior the user has not accepted.
