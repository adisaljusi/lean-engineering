# From decisions to verifiable requirements

Use when multiple rules or actors make implicit behavior dangerous. Inputs are accepted decisions/sources, existing contracts and business examples. A short issue suffices for a local change.

1. State the outcome in business terms; separate solution suggestions from constraints.
2. Identify actors, scope and decision owners. Reconcile conflicting sources; the latest message is not automatically approved policy.
3. Express invariants and observable transitions. Define identity, units and temporal boundaries where consequential.
4. Attach an example and verification method to each important rule. Stable IDs help multi-person handoffs.
5. Express quality scenarios as stimulus, workload, response and measure. Unknown targets stay unknown; identify the measurement/decision needed.
6. Check compatibility, history, permissions and corrections before calling behavior settled.

## Worked handoff

Accepted: ingestion proposes; same-tenant approvers publish; integer basis points represent rates, None is unknown; intervals are [start, end). No payment calculation.

| ID | Observable rule | Example/proof |
|---|---|---|
| R1 | Ingestion creates pending proposals without publication | Base 1250; propose 1300; public value remains 1250 |
| R2 | Only same-tenant approvers publish | Reviewer and other-tenant approver cannot change it |
| R3 | Publishable rate is known and in 0..10000 bp | 0 valid; None and 10001 rejected without mutation |
| R4 | Change affects only its section during [start,end) | Nov 1/30 use 1300; Dec 1 retains prior behavior |
| R5 | Keep selected/conflicting evidence and decision history | Corrected adjudication adds a decision; source unchanged |

If source authority is disputed, mark selection policy unresolved rather than invent legal precedence. These requirements do not choose a queue, schema or service split.

Quality example: “After worker crash, accepted proposals remain recoverable without duplicate publication.” Recovery-time target is unagreed. Measure current recovery and ask for a target if it affects storage/operations. Do not invent a five-second SLA.

Detail helps consequential handoffs but duplicated specs drift when an issue and existing tests already define behavior. Verify each rule against an accepted source and an observable example; check dates, units, actors and unknowns consistently. Evans' *Domain-Driven Design* provides the shared-language foundation; the procedure is original synthesis.
