# Method library: which reference teaches the next action?

Read this index when a task needs a method beyond the selected playbook. Choose by the decision, then read that method's guide before using it. A method is an engineering procedure; a skill is its discoverable entry point. Naming DDD, TDD or a workflow is not performing the method.

The table's paths are relative to each **owning installed skill**, not this directory. Find that skill in the agent's catalog and resolve from its installed location. Load only the guides relevant to today's decision. No companion is required to install `lean-engineer`.

| Decision / method | Owning skill and guide | Inputs to inspect | Concrete result / readiness to continue |
|---|---|---|---|
| Decide what to ask | `grill-with-docs`: `references/discovery.md` | Request, docs/code/tests, prior answers, conflicting sources | Decision-changing questions with consequences; accepted answers separated from assumptions |
| Define behavior | `requirements-engineering`: `references/requirements.md` | Domain facts, accepted decisions, existing contracts | Precise actors/units/states/invariants and observable examples; material disputes visible |
| Select acceptance examples | `behavior-specification`: `references/acceptance.md` | Accepted rules, boundaries, current coverage | Representative data and expected effects; coverage by risk, no invented expected policy |
| Choose system boundaries | `solution-architecture`: `references/decisions.md` | Current topology/code/schema, ownership, quality constraints | Current/proposed distinction, credible alternatives, recommendation/costs/revisit evidence |
| Choose data/communication behavior | `solution-architecture`: `references/data-and-communication.md` | Workload, invariants, transactions, failure/ownership boundaries | Persistence/communication contract including recovery, ordering and duplicate semantics |
| Explain a flow visually | `solution-architecture`: `references/visuals.md` | The question, actual/proposed flow and contracts | One useful editable view consistent with prose; syntax/render limits reported |
| Design evidence and adjudication | `solution-architecture`: `references/extraction.md` | Immutable source/OCR versions, candidates, authority/review rules | Provenance, conflicts, normalization, correction/publication and reproducible-run flow |
| Define data/API compatibility | `technical-design`: `references/contracts.md` | Field meaning/units, clients, schemas, writes, lifecycle | Precise invariants/error contracts and compatible migration/rollback |
| Implement proportionately in Python | `technical-design`: `references/python.md` | Owning modules, Python version, data/resource boundaries and tooling | Chosen functions/records/classes, validation, resource/transaction/concurrency ownership |
| Order delivery increments | `implementation-planning`: `references/delivery.md` | Outcome, existing source, dependencies and risks | First demonstrable slice, real file/contract changes and meaningful checks |
| Implement and test | `test-driven-development`: `references/implementation.md` | Authorized behavior, reproduction/regression, affected integration | Verified changed behavior; meaningful failing/passing checks when applicable |
| Review a change | `code-review`: `references/review.md` | Actual diff, callers/contracts and execution evidence | Actionable defects/risks separated from optional improvements |
| Establish confidence | `evidence-verification`: `references/evidence.md` | Accepted outcomes, source, actual check results/environment | Verified/Failed/Not verified with evidence and consequential limits |

## Applying a method

1. State the immediate decision or observable change, not the name of a lifecycle phase.
2. Read the owning guide and the task evidence it requires. The guide supplies the procedure; the repository supplies the facts.
3. Perform the procedure at the needed depth. Keep concrete decisions, examples and evidence, not a transcript of every checklist item.
4. Check that its result answers the next engineer's question: what is accepted, why this choice, how to implement/check it, and what is unresolved?
5. Pass those results into the next needed method. Do not restart discovery or ask for approval because the skill name changed.

For example, the architecture method's result is a chosen boundary and its consequences. Technical design then defines the affected contract and transaction; it does not reopen whether implementation is authorized. Verification reads the accepted contract and actual results; it does not require newly created architecture documents.

## When a companion is unavailable

Follow the selected local playbook in `workflows.md`, which includes a complete basic procedure. Inspect facts, make the next decision, perform authorized work and check the result directly. For a complex method the catalog cannot supply, consult available authoritative repository/library documentation and state the limitation; do not pretend the absent guide was read. Do not install external frameworks or load a source checkout as an implicit dependency. Ask only if missing consequential knowledge actually blocks safe progress.

Method outputs can live in conversation, an issue, existing design notes or code/tests. A new document is justified by handoff, risk or a user's request, not by the number of methods used.
