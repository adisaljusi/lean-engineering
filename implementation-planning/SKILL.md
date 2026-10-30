---
name: implementation-planning
description: Plan dependent engineering work as demonstrable increments with concrete file changes, compatibility and risk-based verification.
---

# Implementation Planning

Inspect the requested outcome, accepted decisions, owning source, tests, CI and repository conventions. Use a plan when work has dependent steps, migration risk or a requested handoff. A tiny agreed fix needs only the direct change and existing regression check.

Start with the smallest demonstrable behavior across affected boundaries. For each useful increment state touched modules, behavior/contract, dependencies, verification and any rollout/rollback. Use existing requirement IDs if available. Avoid foundation-only tasks that postpone discovering whether the flow works.

Load [delivery planning](references/delivery.md) for staged migrations or multi-document extraction. It includes a concrete slice and verification procedure.

Check each proposed module/interface/dependency against a current responsibility, invariant or operational need. Retain meaningful boundaries; do not minimize file or function counts blindly. Prioritize domain invariants, changed contracts, real integration failure paths and critical workflows. Explain consequential omissions, not every theoretical test combination.

Return actionable steps using existing issue/docs conventions; no required spec/design/plan trilogy. A planning-only request stops at the plan. An implementation request already permits ordinary reversible work: continue into implementation without requesting approval because planning ended. Surface a material behavior change or destructive action when it falls outside existing authorization.
