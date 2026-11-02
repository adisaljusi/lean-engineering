# Replication and stale-read consequences

## Book material

**Foundation:** Martin Kleppmann — Designing Data-Intensive Applications, first edition (2017). **Concept/locator:** Chapter 5: Replication — Synchronous Versus Asynchronous Replication; Handling Node Outages; Reading Your Own Writes. [Source / locator](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/). **Evidence basis:** `publisher-toc`.

Replication maintains copies for availability or read capacity. Leader/follower and other replication approaches differ in failure and conflict behavior; asynchronous propagation introduces observable lag.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## Important distinctions

- Synchronous versus asynchronous acknowledgment changes latency and what a confirmed write guarantees about copies.
- Reading your own writes, monotonic reads and consistent-prefix reads are different user-visible expectations.
- Multi-leader or leaderless writes introduce conflict/concurrent-version questions; a quorum label alone does not settle all failure/interleaving behavior.

## When to use and what to inspect

Use when adopting replicas or relying on their reads/failover. Inspect write authority, lag, read-after-write needs, conflict policy, failover/data-loss limits and current operations.

## Apply the idea

1. Separate reads that tolerate staleness from those requiring a recent confirmed revision.
2. Define where writes are accepted and what acknowledgment guarantees about replication.
3. Specify failover and conflicting-write behavior rather than assuming copies stay identical.
4. Monitor lag and rehearse the recovery behavior users depend on.

## Worked application

Review publication confirms a signed decision at the writer. Evidence browsing can read immutable copies, but the current publication pointer needs a fresh read after confirmation. A replica useful for reporting cannot silently serve stale authorization decisions.

## Trade-offs and simpler choice

Synchronous replication can raise latency and reduce write availability; asynchronous copies can lose recent writes on some failovers. Avoid replicas until an availability/read requirement warrants their cost.

## Verify the decision

Introduce lag and leader loss, then check confirmation/read behavior and recovery against accepted data-loss/staleness limits.
