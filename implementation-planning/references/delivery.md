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
