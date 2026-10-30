---
name: test-driven-development
description: Implement authorized changes with meaningful failing checks, proportionate Python/code design, real boundary tests and honest regression evidence.
---

# Test Driven Development

Read accepted intent, owning code, existing tests and project tooling. For authorized implementation choose the smallest useful slice; no new specification or approval is required just to begin coding. Respect design-only requests.

Where useful, reproduce the defect with a meaningful failing check, observe the expected failure, implement, observe success and refactor for clarity. An existing failing regression can supply the red step. For low-impact text/config changes use appropriate existing checks; do not add tests that merely mirror the edit. Bounded spikes are appropriate when the unknown is technical; convert consequential findings into stable checks.

Load [implementation and verification](references/implementation.md) for choosing test boundaries, real database failure checks, Python responsibilities and resource/concurrency risks.

Test domain invariants at stable boundaries and persistence/API/queue behavior with real integrations where those contracts change. Mocks isolate unavailable collaborators but do not prove transaction or delivery semantics. Add critical workflow coverage when the changed path warrants it. For model components use versioned inputs, meaningful adverse cases and repeated evaluation; deterministic schema checks do not establish extraction quality.

Keep humans able to follow the flow: cohesive functions/modules, explicit data semantics, no forwarding hierarchies, class-per-operation frameworks or private-method test mirrors. Reuse repository libraries and tooling. Explain material discoveries that change accepted behavior rather than silently rewriting it. Record executed commands/outcomes and unverified boundaries; never turn a test plan into a success claim.
