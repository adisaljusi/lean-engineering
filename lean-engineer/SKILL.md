---
name: lean-engineer
description: Use concrete task playbooks to carry out engineering work, compose independent methods, or optionally coordinate a project across decisions, implementation, verification and session handoffs.
---

# Lean Engineer

Select the requested use:

- **One method:** invoke its owning skill directly; use the [method catalog](references/methods.md) to find its procedure when needed.
- **One task:** read [task playbooks](references/workflows.md), choose direct change, feature delivery, design decision or investigation, and follow its concrete procedure at the current decision.
- **A shared project process:** when requested, read [optional project workflow](references/project-workflow.md) for coordination, progress and resume over those playbooks. This does not install project rules or require tracking files by default.

When a handoff/correction is unclear, read the [worked delivery walkthrough](references/walkthrough.md). Load only the selected playbook/methods; do not read every reference for every task. Ordinary use of this router selects a task playbook, not permanent framework adoption.

Read the request, conversation decisions, repository instructions, relevant code/tests/docs and current architecture. Establish the requested result and authorization: advice, design, review, or implementation. Start at the current decision; the skill names below are entry points, not a mandatory sequence.

- Agreed small fix: load [direct-change procedure](references/direct-change.md), then inspect the owning code and regression, implement within scope, run the relevant check. No new interview, specification or architecture document is needed.
- Unclear business behavior or dependent feature work: load [feature-delivery procedure](references/feature-delivery.md); use `grill-with-docs`; inspect existing answers before asking what would change the immediate decision.
- Requirements or acceptance handoff requested: use `requirements-engineering` or `behavior-specification`.
- Consequential boundaries/data flows: load [design-decision procedure](references/design-decision.md); use `solution-architecture`; concrete semantics, contracts or Python choices: `technical-design`.
- Uncertain failure cause: load [investigation procedure](references/investigation.md) before choosing a remedy.
- Several dependent implementation steps: use `implementation-planning`. Authorized delivery: use `test-driven-development`, then appropriate review and `evidence-verification`.

Discover companions through the agent's available-skills catalog. If one is absent, do the needed work directly: inspect evidence, resolve consequential unknowns, compare credible options, implement authorized changes and verify. Do not claim to load unavailable skills or resolve paths in the source checkout. Supporting guides belong to their installed skill directories.

Carry accepted answers forward across turns and artifacts. A correction updates affected examples, contracts and checks; retain the reason where useful. Do not ask for the same decision again under another skill. An implementation request authorizes ordinary reversible implementation choices. A design-only request does not. Surface unresolved consequential business/security/data-loss decisions; seek consent for destructive or externally consequential actions when not already authorized. Never pause merely because a phase ended.

Use existing artifacts and conventions. Create a document only when it helps a human decide, implement or operate the change. Report what changed, why it fits now, executed verification and remaining limits. Check that humans can follow the important flow and diagnose failures; do not equate quality with fewer modules or more tests.
