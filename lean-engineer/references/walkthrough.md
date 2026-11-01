# Worked handoffs: extraction proposal through authorized delivery

This is a worked reasoning and handoff example, not a transcript of an evaluated agent or a claim that model extraction was executed. It shows how a playbook uses the library and how accepted decisions survive a correction/resume. The actual runnable Python transaction example lives in `technical-design` if that companion is installed.

## Starting request and available facts

User: “Design a way to extract treaty changes from related PDFs for review. Start with three documents and six fields. Show how it will work before we implement.”

Repository facts (example): Python application, PostgreSQL, object storage and model gateway; immutable OCR document-version/page/span identities; tenants already isolated; historical terms must remain inspectable. Operations suggests newest-upload wins; underwriting mentions unsigned drafts. No measured workload/latency target. These are example inputs to inspect in a real task, not assumptions to apply to every repository.

## 1. Choose and read

Select playbook C (design decision), borrowing discovery from B only for conflicting source authority. Read current ingestion/publication code, business docs and OCR contracts. Load the discovery method for the unresolved rule; architecture decisions/visuals/extraction guides for this system choice. Do not load API evolution, every messaging pattern or the whole Python guide merely because they exist.

Observed current flow: upload → OCR → current prototype writes a term. Proposed outcome is not yet settled; the existing code may be the defect. State that distinction. Business ownership, not code shape alone, decides whether the write is allowed.

## 2. Resolve the decision with a concrete example

Ask: “Should automatic extraction create a pending suggestion or publish the term? Would a later unsigned 14% draft replace the signed 13% wording?” This changes publication authority. Do not ask which broker to use.

Accepted answer: pending suggestions only; unsigned sources never publish; a same-tenant approver chooses authoritative conflicts with a reason; retained evidence and decisions remain inspectable. The date interval is start-inclusive/end-exclusive. The worked proposal initially uses November 15 through December 1.

Carry this into a compact requirement/example:

```text
R1: ingest a candidate without changing the published term.
AC1: base 1250 bp; extract candidate 1300 bp; public term remains 1250.
R2: publication uses authorized, source-verified human decision.
AC2: an unsigned later candidate is visible for review but cannot publish.
R3: preserve prior evidence/alternatives when an adjudication is corrected.
```

If a material authority rule were still disputed, leave that branch unresolved. Do not call a plausible proposal accepted.

## 3. Apply architecture methods and hand off concrete choices

Inspect the existing transaction/job facilities. Compare modules with durable job rows against a separate bounded worker using the same job contract; compare further services only if ownership/load/failure constraints warrant them. Explain why current infrastructure can preserve evidence and recover accepted jobs, what worker isolation would cost, and what measured latency/recovery need would justify it. An in-memory task alone is insufficient if accepted jobs must survive crash.

Use a proposed data-flow view to show immutable document/OCR → verified candidate references → normalization/conflicts → human decision → revision-checked publication. Use the sequence view for the stale-review transaction if it clarifies concurrency. The companion architecture skill supplies editable source in `examples/extraction.mmd` and `examples/publication.mmd`. Read/check source against the proposed contract and available renderer; do not claim images rendered unless they did.

Concrete technical handoff:

- Evidence: immutable document/OCR/page/span plus half-open code-point offsets, exact quote and declared box coordinates. Validate resolution/text; citation shape is not proof of semantic support.
- Candidate: run, field/section, raw and normalized values with explicit unknown/invalid state, evidence; retain alternatives.
- Decision/publication: actor/reason, scope/date interval, selected candidate and revision; authorize and compare revision within the transaction, append history and move the published pointer atomically.
- Run: exact source/OCR/model/prompt/schema/normalizer identities and retained outputs/attempts. This supports comparison, not guaranteed deterministic model output.

The design-only request ends with recommendation, consequences, assumptions, first slice and proposed verification. No production code or fictional execution result is claimed.

## 4. Incorporate a correction and existing authorization

User: “The effective start is November 1, not November 15. Keep December 1 exclusive. Implement the discussed feature.”

Record the accepted correction and implementation authorization. Update active requirements/examples/design and later date checks to November 1; retain why November 15 was superseded where needed. Do not ask for approval again because planning or technical design begins. If retroactive publication authority remains consequential and unanswered, resolve that rule before dependent publication behavior; implement independent evidence/candidate work meanwhile.

## 5. Plan, implement and verify a slice

Choose a first demonstrable path: three documents → valid candidate references → visible conflict → authorized human decision → publication/history. After reading the actual repository, name its owning files and stable contracts. Use the delivery method to order dependent work, the contracts/Python methods for the uncertain boundary, and implementation/evidence methods to prove it. Avoid creating a foundation framework before the path works.

Checks should target source mismatch, cross-tenant access, pending-vs-published state, unknown-vs-zero, unsigned publication, corrected date boundaries, stale review, duplicate identity and transaction rollback. Select relevant coverage, not an exhaustive Cartesian product. Real database tests prove the local database behavior; fixed-corpus model evaluation is separate. A model mock cannot establish extraction accuracy.

A pause note can say: “Evidence/candidate slice complete at commit X, with command/result Y. Publication revision check remains. Accepted start Nov 1; end Dec 1 exclusive. Implementation authorized; production rollout excluded.” X/Y are placeholders for actual evidence, never proof by themselves.

## 6. Resume and finish at the requested outcome

Read the note and accepted sources, inspect source/diff and relevant evidence, then continue publication/recovery work. Do not repeat the authority interview or restart the first slice because the session changed. Reconcile any discrepancy between state note and actual code/checks before relying on it.

Final handoff reports requested behavior implemented, actual commands/results, unchanged/unverified external boundaries and release risks. A passing SQLite example does not establish PostgreSQL deployment, real OCR accuracy or correct model extraction. If the user requested the complete feature, the first-slice plan alone is not completion; deliver remaining authorized work or identify a concrete blocker.

## Why these handoffs matter

The discovery answer becomes a business invariant; architecture allocates ownership/durability; technical design defines data and atomic operations; implementation realizes the slice; verification checks the same accepted rule. Each step consumes the previous decision rather than re-interviewing the user. The project workflow preserves this chain across sessions without making every task follow all steps.
