---
name: lean-engineer
description: Choose and carry out proportionate engineering work, from a small authorized fix to discovery, architecture, implementation and verification of a complex feature.
---

# Lean Engineer

Read the request, conversation decisions, repository instructions, relevant code/tests/docs and current architecture. Establish the requested result and authorization: advice, design, review, or implementation. Start at the current decision; the skill names below are entry points, not a mandatory sequence.

- Agreed small fix: inspect the owning code and regression, implement within scope, run the relevant check. No new interview, specification or architecture document is needed.
- Unclear business behavior: use `grill-with-docs`; inspect existing answers before asking what would change the immediate decision.
- Requirements or acceptance handoff requested: use `requirements-engineering` or `behavior-specification`.
- Consequential boundaries/data flows: use `solution-architecture`; concrete semantics, contracts or Python choices: `technical-design`.
- Several dependent implementation steps: use `implementation-planning`. Authorized delivery: use `test-driven-development`, then appropriate review and `evidence-verification`.

Discover companions through the agent's available-skills catalog. If one is absent, do the needed work directly: inspect evidence, resolve consequential unknowns, compare credible options, implement authorized changes and verify. Do not claim to load unavailable skills or resolve paths in the source checkout. Supporting guides belong to their installed skill directories.

Carry accepted answers forward across turns and artifacts. A correction updates affected examples, contracts and checks; retain the reason where useful. Do not ask for the same decision again under another skill. An implementation request authorizes ordinary reversible implementation choices. A design-only request does not. Surface unresolved consequential business/security/data-loss decisions; seek consent for destructive or externally consequential actions when not already authorized. Never pause merely because a phase ended.

Use existing artifacts and conventions. Create a document only when it helps a human decide, implement or operate the change. Report what changed, why it fits now, executed verification and remaining limits. Check that humans can follow the important flow and diagnose failures; do not equate quality with fewer modules or more tests.
