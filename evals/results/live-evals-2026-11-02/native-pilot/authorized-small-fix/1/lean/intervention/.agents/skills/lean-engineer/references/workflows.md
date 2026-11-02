# Task playbooks

Use one playbook for the requested outcome. Enter at the first unresolved decision; completed/accepted work is input, not a reason to repeat a step. These are ordered procedures with explicit branching, not mandatory phases for all tasks. For detailed methods use the companion catalog in `methods.md`; this file also works when only `lean-engineer` is installed.

## Select the playbook

| Situation now | Start here | Depth / useful result |
|---|---|---|
| Agreed small change or known defect | [A: direct change](direct-change.md) | Owning code + useful regression; usually no new document |
| Feature has unknown business meaning or several dependent changes | [B: feature delivery](feature-delivery.md) | Resolve only consequential gaps, then demonstrable increments |
| Architecture/design decision requested | [C: design decision](design-decision.md) | Inspected current state, alternatives/consequences and actionable handoff |
| Failure cause is uncertain | [D: investigation](investigation.md) | Reproduction, discriminating evidence, cause/limitation and verified remedy if authorized |
| Work spans sessions and a shared process is requested | Apply `project-workflow.md` over the appropriate task playbook | Minimal durable decision/progress state, no extra runtime |

A request for “Lean Engineering” alone selects the proportionate task playbook. It does not opt the project into permanent process rules, install hooks or create tracking files.

Read the selected playbook only. The four procedures are separate so an agreed small fix does not load the feature/design/investigation material. Use `methods.md` only when the next decision needs its more detailed procedure.

## Continue, revisit, pause, finish

- Continue when the next action is understood, reversible and authorized.
- Revisit only the affected decision when new evidence invalidates it; update its consumers (examples/contracts/code/checks), not the entire lifecycle.
- Pause dependent work when a consequential unknown, ungranted external/destructive action or inaccessible required resource prevents sound progress. State the exact decision/check blocked and keep independent work moving.
- Finish at the user's requested outcome with evidence and limits. Completed steps do not by themselves establish success or permission to publish.

These playbooks are original Lean Engineering guidance. External methodology research and deliberate differences are documented in the repository's workflow-design note; using these playbooks requires neither Superpowers nor GSD.
