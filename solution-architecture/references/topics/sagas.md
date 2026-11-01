# Sagas, compensation and workflow ownership

## Book material

**Foundation:** Sam Newman — Building Microservices, second edition. **Concept/locator:** Second edition, Chapter 6: Workflow — Sagas and distributed transactions. [Source / locator](https://samnewman.io/books/building_microservices_2nd_edition/). **Evidence basis:** `author-toc`.

A saga coordinates a business process through local transactions and compensating actions where one atomic transaction is unavailable. Compensation changes business state; it is not erasing committed history.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## Important distinctions

- A local rollback and a business compensation differ: a compensation occurs after a prior action committed and may have legal/financial consequences.
- Orchestration makes progression explicit in a coordinator; choreography distributes reactions and needs clear ownership for stalled/cyclic flows.
- Isolation across the whole saga is not supplied by local transactions. Concurrent processes can observe interim state, so reservations/status rules may be necessary.

## When to use and what to inspect

Use for multi-owner operations requiring progress/reconciliation across failures. Inspect invariants, allowed interim states, compensation authority, timeout policy and the operating owner.

## Apply the idea

1. List local commits and the business meaning of failure after each.
2. Resolve permitted compensation/manual outcomes before implementing them; do not invent refund or legal policy.
3. Choose orchestration for explicit progress/recovery ownership or choreography when independent reactions remain understandable; expose dependencies either way.
4. Persist progress/identity and make steps/compensations retry-safe.

## Worked application

Settlement accepts an order, reserves stock and requests payment. If payment succeeds but fulfillment fails, “undo payment” is not an implementation detail: the domain owner must decide refund, retry fulfillment or manual review. A coordinator can expose that unresolved state without fabricating a successful completion.

## Trade-offs and simpler choice

Orchestration adds coordinator ownership; choreography can hide cycles and stalled responsibility. Keep one transaction if business data/ownership permit it, and avoid sagas for ordinary local CRUD.

## Verify the decision

Fail each step before/after commit, repeat compensation and lose acknowledgments. Check allowed final/interim states and an operator’s ability to reconcile stalled work.
