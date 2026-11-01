# Explicit workflows over an independent method library

Revision: 2026-11-01. This follows the user's correction that the reference library
still lacked a clear account of how work should be performed and handed forward.
It addresses a static usability deficiency and a requested product direction, not
an observed model failure or measured superiority over other systems.

## What was missing

The prior revision added substantive individual guides, but `lean-engineer` still
mainly listed skill names and proportionality rules. The user/resuming agent had
to infer the procedure connecting discovery, architecture, planning, delivery and
verification, the evidence each consumes, and what to do with a correction. A
reference collection is useful only if it is discoverable and usable at that
moment; more subject headings alone do not solve this.

## Structure implemented

| Layer | Purpose | What is concrete |
|---|---|---|
| Methods | Independently useful engineering techniques | Existing owning-skill procedures and examples; installed method catalog maps decision → guide → required facts → useful result |
| Task playbooks | Perform one requested outcome | Direct change, feature delivery, design decision, investigation; starting context, actions, branching, rework, finish and authorization boundaries |
| Optional project workflow | Repeat/resume across longer work when requested | Existing artifact locations, accepted decisions/authorization, actual progress/evidence, unresolved issue and next action; inspect actual state on resume |

No additional skill, command dispatcher, installer, hook, mandatory state file or
agent framework was introduced. `lean-engineer` carries its own playbook/index/
walkthrough/resume references for individual installation; detailed engineering
methods remain in their owning skills. Missing companions do not make the basic
workflow unusable. Installing the library or invoking one task does not adopt a
permanent project policy.

The router now explicitly selects and loads the relevant procedure. The four task procedures are separate files so a small fix does not load the longer feature/design material. A method-only
request can use its owning skill directly. References are loaded for the current
decision, not all at once. The worked extraction walkthrough shows the actual
handoff content and how corrected dates/accepted intent pass into implementation
and verification. The planning guide now includes a concrete local eligibility
task with file/contract examples, actions, a check command and failure branching.
Illustrative commands/results are distinguished from actual execution.

## Methodology sources inspected

Sources were inspected as design research, not installed or invoked skills. The
examples, wording and composition in Lean Engineering are original. The sources'
workflow rules do not govern this repository. No external commands, agent
permissions or destructive recovery instructions were adopted.

- [Superpowers README](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/README.md),
  [writing plans](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/writing-plans/SKILL.md),
  [executing plans](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/executing-plans/SKILL.md),
  [systematic debugging](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/systematic-debugging/SKILL.md).
- The inspected [GSD repository README](https://github.com/gsd-build/get-shit-done/blob/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815/README.md)
  redirects to GSD Core. That old repository is archived; it was not treated as
  the current active workflow source.
- [GSD Core README](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/README.md),
  [planning how-to](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/how-to/plan-a-phase.md),
  [recovery how-to](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/how-to/recover-and-troubleshoot.md),
  [phase-loop explanation](https://github.com/open-gsd/gsd-core/blob/72c4e14dfa56ecc98c04b3fd6736bea2dd3195dc/docs/explanation/the-phase-loop.md).

Pinned source identities and fetched-content hashes are retained in
`evals/results/workflow-followup/research.json`. Public source claims about model
context quality or overall effectiveness are not accepted as measured findings
for Lean Engineering.

| Concrete source lesson | Lean Engineering application | Deliberate difference |
|---|---|---|
| Superpowers planning specifies files, interfaces, actions and verification, not just “plan this” | Concrete task handoff and existing file/contract/check expectations | No compulsory plan template, per-step commit ritual, task duration or new approval after planning |
| Superpowers execution distinguishes a code error from a plan/spec contradiction | Playbook branches remedy a defect or revisit the affected decision with evidence | No mandatory executor/reviewer machinery or inherited model-selection policy |
| Superpowers debugging traces a symptom, compares evidence and tests hypotheses | Investigation playbook with reproduction, boundary tracing, discriminating check and remedy | No rigid attempt quota or automatic architecture rewrite; incident mitigation is explicit |
| GSD Core separates task-oriented how-tos, references and explanation | Usage guide plus method library and explicit task procedures | No copied slash-command interface or claim that external tools are available |
| GSD Core preserves context/progress and restores sessions from artifacts | Compact handoff and resume procedure checking decisions against actual source/evidence | Reuse existing issue/docs; no mandatory `.planning/` tree or duplicate source of truth |
| GSD Core explains both overlarge and overly fragmented phases | Proportionate slices/playbook entry at the current decision | Ordinary small fixes do not adopt a full project loop |

## Evaluation and verification

Two smoke cases exercise method-only scope and resuming a corrected authorized
feature. A new native conversational workflow starts from stale session notes,
a later accepted 45-day correction and current 14-day code. It must inspect the
sources, preserve history/authorization, implement the correction and verify it
without restarting interviews or adopting a framework. Its real-database-free
Python date contract uses the existing checker interface, with correct/buggy
controls in the harness. It measures behavior and evidence, not reference names,
file counts or ritual narration. Existing small-fix, documented-feature and
complex business workflows remain contrasting cases; the reserved holdout is
unchanged.

The installation check now requires the index, methods, walkthrough, project guide and four separate task procedures in a router-only
installation with companions absent. This proves files/links and the existing
fallback instruction are available; model application remains unverified.
The existing runners still require isolated subjects, separate stakeholder and
assessor roles, original evidence and comparable contexts. No new evaluator
platform was built.

See `evals/results/workflow-followup/validation.json` for actual checks and their
scope. No behavioral improvement is claimed: model hosts remain outside the
configured network policy, and the prior CONNECT-403 pilot is retained. New
preparations make no model calls and receive no scores. A supported live pilot
must still inspect method/reference reads, accepted-decision continuity and
role behavior before a repeated comparison campaign.
