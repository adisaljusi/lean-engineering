# Streams, checkpoints and derived state

## Book material

**Foundation:** Martin Kleppmann — Designing Data-Intensive Applications, first edition (2017). **Concept/locator:** Chapter 11: Stream Processing — Partitioned Logs; Reasoning About Time; Fault Tolerance. [Source / locator](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/). **Evidence basis:** `publisher-toc`.

Stream processing continuously derives state from events. Retained logs, time/order and checkpoint semantics determine replay and failure behavior; delivery alone does not make a projection correct.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## Important distinctions

- Event time describes the source event; processing time describes when the processor observes it. Delayed data makes them diverge.
- A retained partitioned log enables replay within its retention/order scope; a transient notification channel need not.
- A checkpoint records processing progress, but a sink effect and checkpoint can diverge on crash unless their protocol or effect semantics handles replay.
- A projection is derived state, not automatically the source of business authority.

## When to use and what to inspect

Use when continuing updates or replayable per-key history are required. Inspect event identity, partitioning/order scope, retention, event/processing time, late data and sink effects.

## Apply the idea

1. Define what the event represents and which entity/key owns order.
2. Specify late/duplicate/gap handling and when a result is considered complete enough for its consumer.
3. Coordinate checkpoint progress with sink effects or make replay idempotent.
4. Expose lag and retained-history limits; define rebuild/correction behavior.

## Worked application

A search projection consumes published-decision events by treaty revision. Replaying revision 3 must not duplicate documents; revision 2 arriving later cannot replace it. The projection can lag while the authoritative publication transaction remains current.

## Trade-offs and simpler choice

Stream systems add retention, offset, replay and operational duties. Periodic batch refresh or a direct database query is simpler when continuous low-lag updates are unnecessary.

## Verify the decision

Crash around checkpoint/sink commit, replay duplicates and deliver out of order. Compare rebuilt state with the authoritative accepted history.
