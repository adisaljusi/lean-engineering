# Lean Engineering

Ten composable skills for thoughtful engineering: read the existing system,
resolve consequential uncertainty, explain choices, implement authorized work and
verify it. Small changes stay small; difficult constraints can justify richer
architecture. Skill names are entry points, not a mandatory lifecycle.

## Install

From your project, the intended interactive installation is:

```sh
npx skills add adisaljusi/lean-engineering
```

**This improvement branch depends on the unmerged evaluation branch.** Until it
is merged, the command above installs unchanged `master`, which currently exposes
only nine skills because its technical-design description has invalid YAML.
Install the revised ten skills from this branch explicitly:

```sh
npx skills add 'https://github.com/adisaljusi/lean-engineering.git#improve/operational-engineering'
```

Verified CLI selection syntax (1.7.4; Node 24.19.0 used here):

```sh
# List without installation
npx skills@1.7.4 add 'https://github.com/adisaljusi/lean-engineering.git#improve/operational-engineering' --list
# Full set, project-local, copied to Codex's native .agents/skills location
npx skills@1.7.4 add 'https://github.com/adisaljusi/lean-engineering.git#improve/operational-engineering' --skill '*' --agent codex --copy -y
# One skill, including its own references and runnable examples
npx skills@1.7.4 add 'https://github.com/adisaljusi/lean-engineering.git#improve/operational-engineering' --skill technical-design --agent codex --copy -y
```

The quoted `#ref` form preserves the slash in the branch name. In CLI 1.7.4, a
`/tree/improve/operational-engineering` URL is parsed as branch `improve` and a
subdirectory, and fails. Omit selection flags for the interactive skill/agent chooser. No custom installer
or runtime is needed. Each directory contains its own supporting files; no shared
checkout path or development symlink is required. Use the agent's installed-skill
catalog; `lean-engineer` works without companions by doing the needed steps
directly. Other agent runtime discovery is unverified here. Installation/file
checks do not prove an agent reads or applies a skill.

## How to use the library

Use a method on its own, follow a task playbook, or optionally compose the same
methods into a project workflow. No additional framework/runtime is required.

| Use | Example request | Reference that teaches how |
|---|---|---|
| One method | “Use solution-architecture to compare these options; design only.” | The skill's decision/data-flow/visual guides |
| Task workflow | “Use lean-engineer to implement this feature from the existing docs.” | [Task playbooks](lean-engineer/references/workflows.md): direct change, feature, design or investigation |
| Ongoing project | “Use Lean Engineering's project workflow for this feature and preserve a resumable handoff.” | [Optional project workflow](lean-engineer/references/project-workflow.md) |

Playbooks define inputs, ordered actions, branching/rework, useful results and
stopping conditions. The [method catalog](lean-engineer/references/methods.md)
routes each decision to its substantive guide. The [worked walkthrough](lean-engineer/references/walkthrough.md)
shows discovery → architecture/data decisions → corrected intent → authorized
implementation/verification → resume, without resetting accepted decisions.
See [the usage guide](docs/USAGE.md) for direct links and adoption examples.
Naming a skill or pattern is not a substitute for reading/applying its method.

## Choose the next useful work

| Need | Entry point |
|---|---|
| Route/deliver a change | `lean-engineer` |
| Resolve business/design unknowns | `grill-with-docs` |
| Precise behavior and examples | `requirements-engineering`, `behavior-specification` |
| Boundaries, flows, alternatives, diagrams and evolution | `solution-architecture` |
| Concrete data/API/algorithm/Python decisions | `technical-design` |
| Dependent delivery increments | `implementation-planning` |
| Authorized implementation and useful tests | `test-driven-development` |
| Review correctness/maintainability | `code-review` |
| Execution-backed confidence and limits | `evidence-verification` |

Each SKILL.md tells you which supporting guide to load for which decision. Visual
architecture is bundled with architecture; Python with technical design and
implementation. Neither needs an extra skill or mandatory engineering library.
Existing decisions and user authorization carry across skill boundaries. Use
existing issues/docs; create a design/ADR/plan only when it helps the work.

## Book material by topic

The [topic catalogue](docs/BOOK-TOPICS.md) links to dedicated entries explaining
book concepts and how to use them: dependency direction, SOLID, transactions,
replication, partitioning, domain identity/invariants, messaging patterns,
persistence/design patterns, API evolution and more. Each has a concrete method,
worked application, costs/simpler choices, verification and an honest source
basis/locator. These are substantive reference notes, not a bibliography or
claims of access to unavailable full books. Select entries through each owning
skill's topic index; individual installation includes them.

## Examples and validation

- Targeted commission discovery: `grill-with-docs/references/discovery.md`.
- Monolith/distributed decisions: `solution-architecture/references/decisions.md`.
- Evidence/conflict/human-review design and editable diagrams:
  `solution-architecture/references/extraction.md` and `examples/` in that skill.
- Runnable Python publication with transactions/stale review:
  `technical-design/examples/README.md`.

```sh
python scripts/validate_skills.py
python -m unittest discover -s technical-design/examples -v
python -m unittest discover -s evals/tests -v
python evals/score.py --self-test
```

[Redesign critique, rationale and validation](docs/REDESIGN.md) separates static
instruction deficiencies, actual installation/harness observations and hypotheses
requiring behavioral evaluation. [Evaluation guide](evals/README.md) and
[workflow guide](evals/WORKFLOWS.md) explain fresh baseline/treatment comparisons,
independent stakeholders/assessors and retained failures/indeterminate attempts.
The revised skills and live adapter remain **behaviorally unvalidated**. The live
pilot hit model-host proxy denials; no scores or improvement claim are reported.
