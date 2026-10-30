# Decide what to ask

The problem is committing to consequential behavior without evidence, or making the user repeat information the engineer can read. Apply this method when a real unknown affects the current decision.

## Procedure

1. Name today's outcome: understand a feature, choose architecture, implement an agreed change, or diagnose a failure. Capture scope and authorization already given.
2. Read relevant entry points/callers, domain notes, schemas, contracts, tests and past decisions. Record where answers came from and whether they describe current behavior or intended policy. Code can contain a bug; a test is not necessarily authority to change a business rule.
3. For each unknown write privately: “If A, choose X; if B, choose Y.” If neither branch changes today's work, defer the question.
4. Assess consequence and reversibility. A missing UI label can use an explicit working assumption. Whether an upload publishes a financial term, crosses tenants or deletes history needs resolution before dependent implementation.
5. Ask the smallest connected set enabling progress. Concrete alternatives help; allow the user to correct both. Explain the consequence briefly when useful. No question quota.
6. Carry answers forward. After a correction, update affected behavior/examples/checks. Keep rejected interpretations where they explain a meaningful decision.

## Worked exchange: automatic commission changes

Repository facts: commission is a percentage on a named treaty section; tenants see only their own treaties; history remains inspectable. Operations says “last upload wins”; underwriting mentions unsigned drafts. The task asks for a proposal before coding.

Useful first response: “The docs establish section-level percentages, tenant isolation and retained history. Operations and underwriting disagree about authority. Does automatic create a pending suggestion or publish a new value? For example, should a later unsigned 14% draft replace the signed 13% term? This determines whether ingestion may change published terms.”

User: “Suggest only; an approver publishes. Unsigned drafts never publish.”

Next decision: proposal lifecycle and date scope, not broker selection. Ask: “For a 13% proposal effective November 1 through December 1, should November 1 use 13% and December 1 return to the previous value? Can a retroactive interval be approved?” If docs already specify half-open intervals, cite them and ask only about retroactivity.

User corrects the start from November 15 to November 1. Record the accepted start and exclusive end; previous start is superseded. Update requirements, dates and verification. Do not ask again in technical design. A later implementation request authorizes ordinary code choices; a design-only limit applies until changed.

## Result, trade-offs and verification

A compact note: Fact: tenant isolation (README). Decision: approvers publish suggestions (user turn). Assumption: reuse existing date parser (reversible technical choice). Unresolved: whether conflicting signed candidates require a reason (changes review behavior). Next: resolve conflict policy; meanwhile inspect current publication transaction.

Check every question: is it unanswered, does it change today's choice, does it expose the practical consequence? An exhaustive questionnaire delays decisions and obscures risk. For an agreed typo, inspect/fix/verify is simpler. Further foundation: Eric Evans, *Domain-Driven Design* (2003), shared language and boundaries. This method and exchange are original synthesis, not a quotation.
