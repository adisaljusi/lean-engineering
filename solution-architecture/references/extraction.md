# Worked design: multi-document evidence and review

Problem: normalize six treaty fields from 3 representative documents initially, later 10–80 related PDFs, without hiding conflicting terms or fabricating evidence. Inputs: current Python/PostgreSQL/object-store/gateway architecture, immutable OCR examples, tenant rules and accepted human publication policy. No measured need for a service or agent per field.

## Discovery that changes this design

Read domain rules first. If unanswered, ask whether “automatic” means candidate extraction or publication; whether an unsigned later upload can be authoritative; who resolves conflicts; and what date/section scope applies. These change correctness, unlike choosing a broker prematurely. Ask workload/recovery targets when they distinguish request processing, durable jobs and worker capacity. Record unknown measurements; do not invent accuracy/SLA promises.

Assume for this worked proposal: candidates may conflict; authorized humans select with reasons; signed authority is a business rule, never upload order. A corrected decision must leave old evidence/history inspectable. These are example assumptions to resolve in a real task, not universal treaty policy.

## Proposed model and flow

Use `examples/extraction.mmd` for lineage and `examples/publication.mmd` for stale review. Current architecture must be inspected separately; these are proposed examples.

- Document version: tenant, logical document identity, immutable bytes hash/version, declared signed status and metadata authority. A new upload is not automatically a new business truth.
- OCR page version: document version, OCR engine/config version, page ID, text, width/height and coordinate system. In this example offsets are Unicode code points in that immutable text, [start,end); boxes are normalized [x1,y1,x2,y2] in [0,1], top-left origin. Pixel/rotation transforms belong to the viewer adapter. Do not silently mix byte/UTF-16 offsets or pixels.
- Evidence reference: document/OCR/page/span identity, start/end, exact quote and box. Validate resolution and exact `text[start:end] == quote`; verify box bounds. Referential validity does not prove the quote supports a semantic claim; assess that separately.
- Candidate: run, field/section, raw value, typed normalized value or explicit unknown/invalid state, evidence references, normalizer version. Preserve alternatives; normalization must not erase source text or infer missing values.
- Decision: selected candidate(s), scope/effective dates, actor, reason, revision and prior decision. Append corrections; do not rewrite immutable candidates. Publication points to an accepted decision in an authorization/revision-checking transaction.
- Run manifest: exact source/OCR IDs, model identifier, prompt/schema/normalizer versions, settings, job attempts and outputs. Retain outputs for comparison; identical inputs do not guarantee bitwise model output.

Procedure: immutable ingest → durable run acceptance → bounded extraction → deterministic reference/type validation → conflict grouping by field/section/time → human evidence review → atomic revision-checked publication. Do not keep locks open during model calls or human review. Persist job identity/status and retry transient gateway failures with bounds; partial failures remain visible and retryable. Never publish a partially accepted run by accident.

## Alternatives, evolution and verification

A single extraction pass is simpler for a small corpus but may exceed context/budget. Bounded document/section extraction plus consolidation fits larger corpora; it costs reconciliation and candidate deduplication. Separate agents are credible only for distinct tools/context/failure isolation with demonstrated benefit. A vector index may help retrieval at measured scale but cannot replace exact source identity or authority policy.

Start with existing modules and storage; introduce a separately bounded worker if measured model latency/CPU harms interactive service or crash recovery requires it. Adopt more infrastructure only with capacity/ownership/recovery evidence and operating cost. Retaining review history is not a reason to add event sourcing or a graph database.

Verify exact span resolution, invalid/contradictory citations, unsupported semantic claims, unknown versus zero, conflict visibility, cross-tenant preview denial, stale review, replay/idempotency and restart after partial work. Compare runs on fixed source versions and a small human-labeled set with difficult cases and a separate holdout; report precision/recall or task-specific error categories where justified, not citation counts. Test viewer page/box alignment visually. A synthetic example does not establish real OCR accuracy.

Sources: DDIA for immutable data/recovery, Evans for identity/invariants, integration literature for durable work, C4 for views (bibliographic details in the bundled sources guide). The example/model are original, not extracted from those works.
