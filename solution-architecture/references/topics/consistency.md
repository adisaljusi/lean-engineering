# Consistency guarantees and application invariants

## Book material

**Foundation:** Martin Kleppmann — Designing Data-Intensive Applications, first edition (2017). **Concept/locator:** Chapter 9: Consistency and Consensus — Consistency Guarantees; Linearizability; Ordering Guarantees. [Source / locator](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/). **Evidence basis:** `publisher-toc`.

Consistency guarantees constrain which observations and orderings clients may see. Linearizability, causal/order guarantees and transaction isolation answer different questions; “strong consistency” needs a concrete required behavior.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## Important distinctions

- Linearizability gives operations a single order consistent with real-time completion constraints; serializability concerns transaction interleavings.
- Causality constrains dependent operations without necessarily ordering unrelated work globally.
- A coordination service can help implement a requirement, but its use does not prove the whole end-to-end application has that guarantee.

## When to use and what to inspect

Use when distributed reads/writes or derived state may violate user expectations. Inspect the invariant, read/write paths, replica lag, failure model and accepted staleness.

## Apply the idea

1. Describe the observation that must never happen, such as seeing an older published decision after confirmation.
2. Choose the necessary guarantee for that operation, not a blanket requirement for every query.
3. Identify the coordination/availability/latency cost and the behavior during failure.
4. State how clients recognize stale, pending or unavailable results.

## Worked application

After an approver publishes revision 3, the confirmation screen must not read revision 2 from a lagging replica. Route that read to the writer or enforce a suitable revision/read mechanism. A reporting dashboard may legitimately lag if it labels the revision and the business accepts the delay.

## Trade-offs and simpler choice

Coordination can cost latency/availability; eventual consistency requires explicit stale-state handling. A single writer database is simpler when it satisfies the requirement.

## Verify the decision

Test post-write reads, replica delay and failure behavior for the specific operation. Do not use a broker order claim as evidence of linearizable publication.
