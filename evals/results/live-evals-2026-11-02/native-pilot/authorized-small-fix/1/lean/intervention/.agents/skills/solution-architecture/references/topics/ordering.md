# Ordering, causality and revision scope

## Book material

**Foundation:** Martin Kleppmann — Designing Data-Intensive Applications, first edition (2017). **Concept/locator:** Chapter 9: Consistency and Consensus — Ordering and Causality; Sequence Number Ordering; Total Order Broadcast. [Source / locator](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/). **Evidence basis:** `publisher-toc`.

Ordering guarantees have a scope; causality, sequence numbers and total order are different mechanisms. A timestamp does not automatically provide a reliable business or distributed order.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use for state transitions, concurrent updates and replay. Inspect per-entity identity/revision, producers, delivery reordering, clock assumptions and gap policy.

## Apply the idea

1. State exactly which operations must be ordered and why.
2. Prefer per-entity revision/order over global order when the invariant is local.
3. Define handling of stale, duplicate, missing and concurrent transitions.
4. Keep upload/processing time separate from accepted business effective time.

## Worked application

Published treaty revision 3 cannot be replaced by a late revision 2 projection event. A later unsigned upload cannot outrank signed wording merely by its timestamp. Per-treaty version checks solve the former; domain authority rules solve the latter.

## Trade-offs and simpler choice

Global ordering serializes unrelated work and costs coordination. If operations commute or only current authoritative state matters, explicit revision checks may suffice.

## Verify the decision

Deliver events backwards and with gaps, vary clocks and replay history; verify accepted state and unresolved conflict behavior.
