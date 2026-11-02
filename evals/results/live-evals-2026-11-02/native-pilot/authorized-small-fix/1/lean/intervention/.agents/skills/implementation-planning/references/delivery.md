# Plan demonstrable increments

Use when dependencies or rollout risk need coordination. Inputs: requested outcome/authorization, existing implementation, accepted rules, current contracts and available checks.

1. Identify the first user-observable result and highest-risk assumption. Avoid a stack of foundation-only tasks.
2. Name actual files/modules to change after inspecting them. State contracts/invariants and meaningful verification; do not invent a source tree.
3. Order increments by dependency and feedback, each small enough to demonstrate. Include migration, compatibility, rollout and rollback where affected.
4. Check every added responsibility/dependency against today's requirements. Keep genuine failure/ownership boundaries; defer speculative extension points.
5. Continue authorized implementation; a plan-only request ends with the plan.

## Worked extraction slice

Existing Python application, PostgreSQL, object storage and model gateway. First deliver 3 documents/6 fields to a reviewer with source-verifiable evidence and visible conflicts. Inspect actual file names before using this outline.

- Ingestion/evidence slice: persist immutable document/OCR version/page/span identity and exact quote/box semantics. Demonstrate loading all three documents and resolving a selected span; reject corrupt references and cross-tenant access.
- Candidate-to-review slice: bounded gateway calls produce typed candidates; deterministic validation keeps raw text and conflicting alternatives. Demonstrate one conflict and one missing value without silent precedence or zero defaults. Stub gateway only for transport-independent checks; use a separately labeled small model evaluation for extraction quality.
- Decision-to-publication slice: authorized human selects with reason; revision check rejects stale review; persist decision/history atomically. Demonstrate correction retaining original evidence and independent-connection conflict.
- Recovery/scale slice: accepted work survives worker restart, retries are idempotent, concurrency/queue bounds match measured gateway limits. Benchmark 80 representative PDFs before adding infrastructure. Record unmeasured targets.

Each slice touches the existing owner and its stable tests, not a service per field. A separate worker is credible if latency/resource isolation requires it; include deployment/on-call/rollback cost then. For schema expansion deploy compatible readers first, backfill/reconcile, migrate writers and observe old use before contraction. Rollback stops being trivial after destructive removal: mark that point and retain a recovery plan.

Verify by walking the flow and checking whether every consequential rule has a planned proof and every migration has a compatible intermediate state. A local typo is better handled directly with its existing regression. Further foundation: Newman, *Monolith to Microservices* (incremental migration), and Ford/Richards/Sadalage/Dehghani, *Software Architecture: The Hard Parts* (coupling/trade-offs). This plan is an original example.

## Turn a slice into an executable task

The planner supplies decisions the implementer cannot infer safely. After reading the source, state: outcome/invariant; files and responsibilities; inputs/contracts; concrete change; verification command and expected behavior; relevant dependency/rollout; and what to do if evidence contradicts the plan. Use an existing issue/checklist if sufficient. Do not paste complete function bodies when contract/examples determine them.

Worked local task (illustrative file names, not commands to run in an arbitrary repository): `app.py` contains `eligible(captured_on, requested_on)` and `test_app.py` uses unittest. README accepts captured-only eligibility for calendar days 0 through 30 inclusive; None and negative elapsed days are ineligible. Implementation is authorized.

1. Read README, `app.py`, `test_app.py` and callers to preserve the bool contract and already-resolved business dates. No new timezone/payment question is needed.
2. Add/reuse behavior examples for None and elapsed days -1, 0, 30, 31, including a month/year boundary. Assert the bool result, not a helper call.
3. Run `python -m unittest -v test_app.py` from the owning project. Before the fix, the boundary cases should expose over-permissive eligibility; an import error is not the intended regression. If no relevant case fails, inspect the test and current implementation before guessing.
4. Change the existing function to enforce the accepted date interval without new infrastructure. Keep unknown distinct from zero days.
5. Run the focused regression and appropriate existing callers/contract tests. Review the diff for scope. Retain actual command/outcome and any unverified boundary; do not declare that the example's predicted output occurred.

The task handoff is enough when another engineer can locate the owner, preserve meaning, make the change and check it without choosing new business policy. If dates are not actually resolved as assumed, return to that specific contract question. If code is requested, continue into this task rather than stopping because the plan exists.
