---
name: evidence-verification
description: Independently verify a feature against requirements, BDD acceptance scenarios, approved domain/data design, architecture, automated tests and operational checks using executed evidence.
---

# Evidence Verification

Inspect approved `spec.md`, `design.md`, `plan.md`, relevant ADRs, source changes and CI/runtime evidence. Build a compact `Requirement → Scenario → Test/check → Evidence → Status` matrix. Execute feasible targeted and regression tests and record exact commands with outcomes; report inaccessible environments and unrun tests as **Not verified**, never Pass.

Confirm behavior, domain invariants, data definitions and schemas, architectural contracts and dependency direction. Check applicable migration/backward compatibility, authorization/privacy, consistency/idempotency, failure/retry recovery, observability, performance targets, unit/integration/E2E coverage and AI evaluation thresholds.

Classify findings `Verified`, `Failed`, `Not verified`. Separate code written from behavior demonstrated. Provide release confidence, residual risks, skipped checks and approval deviations. Do not fix findings without separate authorization.
