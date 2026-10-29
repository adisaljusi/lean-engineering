---
name: test-driven-development
description: Implement approved software changes with red-green-refactor, domain unit tests, real integration tests, critical E2E workflows, regression checks and representative AI evaluations.
---

# Test Driven Development

Work one approved vertical slice at a time. Link the slice to its acceptance scenario and invariants. Where feasible, write a meaningful failing test, execute it and observe the expected failure, implement minimum code, execute the passing test, refactor without behavior change, then run relevant regressions. For infrastructure exploration, allow bounded spikes and convert findings into tests.

Default test policy: unit tests for domain logic and edge cases; real integration tests at affected database/API/queue boundaries; E2E checks for changed critical workflows (service-level E2E is valid for headless systems). Avoid claiming integration coverage from mocks alone. For AI/LLM components add versioned evaluation fixtures, schema checks, quality thresholds, adverse cases and regression samples; do not assume deterministic text.

Follow approved interfaces and repository coding conventions. Revisit design if implementation exposes a faulty assumption; do not silently rewrite business rules. Record actual commands, pass/fail outcomes and omitted tests. Never claim completion without verification.
