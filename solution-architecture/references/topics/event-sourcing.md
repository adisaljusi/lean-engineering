# Event sourcing and authoritative history

## Book material

**Foundation:** Martin Kleppmann — Designing Data-Intensive Applications, first edition (2017). **Concept/locator:** Chapter 11: Stream Processing — Event Sourcing; State, Streams, and Immutability. [Source / locator](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/). **Evidence basis:** `publisher-toc`.

Event sourcing stores domain changes as authoritative events from which state is derived. It differs from keeping an audit log alongside mutable authoritative state, and from retaining immutable source evidence.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when business reconstruction, temporal reasoning or replay justifies an event model. Inspect event meaning, corrections, schema evolution, side effects, projections and retention/privacy constraints.

## Apply the idea

1. Decide whether events or current rows are authoritative and state why reconstruction is required.
2. Define event identity/order and correction semantics without rewriting historical meaning.
3. Version event readers/projections and separate replay from external side effects.
4. Budget snapshots, rebuilds, reconciliation and operating/debugging tools.

## Worked application

Keeping OCR versions and publication decision history does not require event-sourcing the whole portal. If authoritative policy changes must reconstruct the exact business state at past revisions, a domain-event model may be credible; replaying those events must not resend payments or notifications accidentally.

## Trade-offs and simpler choice

Event schema evolution and replay safety are expensive. Current state plus append-only decision/audit rows is simpler for ordinary history requirements.

## Verify the decision

Rebuild state at known revisions, apply corrections, read old event versions and replay without duplicate external effects. Check retention/deletion implications explicitly.

## Further detail

Further pattern discussion: Martin Fowler, [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html).
