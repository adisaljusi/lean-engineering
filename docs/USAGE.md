# Using the methods, task playbooks and optional project workflow

The library supplies procedures for engineering decisions. A task playbook composes
only the procedures needed for one outcome. The optional project workflow adds
shared progress, decisions and resumable handoffs when requested. The same skills
work in all three; no new command system or framework installation is required.

## Pick the amount of coordination you need

| Need | How to ask | What should happen |
|---|---|---|
| Resolve one architecture choice | “Use solution-architecture. Inspect the current system and recommend a design; do not implement.” | Load the relevant method, inspect facts, compare credible options, explain consequences and verification |
| Ship an agreed correction | “Use lean-engineer to fix the agreed message and verify it.” | Direct-change playbook; existing owner/regression; no new interview or design documents |
| Deliver a feature | “Use lean-engineer to implement the documented refund policy.” | Read existing answers, make examples concrete, implement and verify; questions only for actual consequential gaps |
| Investigate a defect | “Use lean-engineer to diagnose why retries create duplicate effects. Implement a fix if supported by the evidence.” | Reproduce/trace/hypothesis/check, then authorized remedy and regression |
| Coordinate longer work | “Use the project workflow for this feature; keep decisions and a resumable handoff in our existing issue.” | Applicable task playbook plus compact state; accepted answers/authorization survive sessions |

These are ordinary natural-language requests, not invented slash commands. You can
also ask for a plan or review only. Neither a playbook nor project mode overrides
that scope. Adoption of a shared repository policy needs the user's/team's actual
request; installing the skills does not create one.

## Book material for a particular topic

Use the [topic catalogue](BOOK-TOPICS.md), then read the entry relevant to the current decision. For example, DDIA transaction material explains atomicity/isolation and concurrent anomalies before its publication/rollback procedure. DDD entries explain identity, values, aggregates and context boundaries. GoF entries explain the actual substitution/construction/wrapping problem before recommending a Python representation. Book/source citations alone do not fulfill this step.

Each entry states what source/locator was verified and separates attributed synthesis from original application. The installed index stays inside its owning skill. No full-book load, external framework or runtime book download is required.

## Direct reference map

Read the guide for the current decision. Its procedure/examples are the source of
how to do the work, rather than an instruction to follow a named book or pattern.

| Work to do | Procedure / worked reference |
|---|---|
| Read evidence and choose questions | [Decision-led discovery](../grill-with-docs/references/discovery.md) |
| Define precise behavior | [Requirements handoff](../requirements-engineering/references/requirements.md) |
| Select representative acceptance examples | [Acceptance examples](../behavior-specification/references/acceptance.md) |
| Inspect current architecture and decide boundaries | [Architecture procedure and choices](../solution-architecture/references/decisions.md) |
| Decide workload/consistency/communication/recovery | [Data and communication](../solution-architecture/references/data-and-communication.md) |
| Select, create and check a diagram | [Visual architecture](../solution-architecture/references/visuals.md) |
| Design immutable evidence, conflicts and human publication | [Multi-document example](../solution-architecture/references/extraction.md) |
| Define concrete models/contracts and compatible changes | [Data and API contracts](../technical-design/references/contracts.md) |
| Select Python representations/resources/concurrency | [Python decisions](../technical-design/references/python.md), [runnable transaction example](../technical-design/examples/README.md) |
| Plan an implementable increment | [Delivery method and concrete task](../implementation-planning/references/delivery.md) |
| Implement and verify at meaningful boundaries | [Implementation method](../test-driven-development/references/implementation.md) |
| Review actual behavior and design costs | [Review procedure](../code-review/references/review.md) |
| Establish demonstrated confidence | [Evidence and limits](../evidence-verification/references/evidence.md) |

The installed router carries its own [method index](../lean-engineer/references/methods.md)
and [task procedures](../lean-engineer/references/workflows.md), so it still has a
usable workflow if companions are absent. Detailed references live inside each
owning skill and arrive with an individual installation. Resolve them from the
agent's installed catalog, not this development checkout. External literature and
frameworks are further research, never runtime dependencies.

## Follow one task without inventing a lifecycle

Read [task playbooks](../lean-engineer/references/workflows.md) and select A/B/C/D.
Each states its starting information, concrete sequence, branches and useful
finish. Enter where work actually is: accepted requirements are inputs; a known
failure may already have its regression. The playbook tells you when to use a
method, when evidence invalidates a decision, and when work is blocked.

For example, a documented feature does not need another requirements interview.
An unresolved publication-authority rule does need a decision before a dependent
implementation. A failing transaction check needs diagnosis/remedy, not another
approval round. An implementation request permits ordinary reversible coding
choices; it does not automatically permit deployment or destructive migration.

[The worked extraction walkthrough](../lean-engineer/references/walkthrough.md)
shows actual handoff content: source facts → targeted authority question →
accepted invariant/example → architecture and data contract → corrected date and
implementation authorization → slice/checks → resumable next action. It is an
illustration, not a transcript of a successful behavioral evaluation.

## Compose a project process when it is useful

Read [optional project workflow](../lean-engineer/references/project-workflow.md).
Reuse the project's issue/spec/ADR/plan locations and CI evidence. Keep enough state
to recover scope, accepted decisions, authorization, actual progress/evidence,
unresolved issues and the next action. A single feature note can hold it all.

On resume, read that state and its accepted sources; inspect actual code/diff and
check evidence before trusting “done”; continue the next authorized action.
Reconcile corrections narrowly instead of restarting discovery. Existing policies
still apply, but there is no mandatory roadmap, state file, approval count,
question count, subagent count or fixed sequence of documents.

The [workflow design note](WORKFLOW-DESIGN.md) identifies the concrete lessons
examined in Superpowers and GSD, their pinned sources, deliberate differences and
validation limits. No comparative effectiveness is claimed.
