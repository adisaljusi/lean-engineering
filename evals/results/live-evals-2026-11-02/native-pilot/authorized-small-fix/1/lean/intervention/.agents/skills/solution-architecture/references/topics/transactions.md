# Atomicity, isolation and transaction boundaries

## Book material

**Foundation:** Martin Kleppmann — Designing Data-Intensive Applications, first edition (2017). **Concept/locator:** Chapter 7: Transactions — Preventing Lost Updates; Write Skew and Phantoms; Serializability. [Source / locator](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/). **Evidence basis:** `publisher-toc`.

Atomicity groups effects against partial failure; isolation controls interference among concurrent operations. A transaction label does not identify every anomaly an application must prevent.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## Important distinctions

- Atomicity prevents a partially applied local transaction; durability concerns committed data surviving the stated failure model.
- ACID consistency means preserving application/database invariants, not the same guarantee as linearizable distributed reads.
- Snapshot isolation can avoid some read anomalies while still permitting write skew. A lost-update check and a cross-row invariant may need different concurrency control.
- Serializability constrains concurrent outcomes as though transactions executed serially; it does not mean a remote side effect automatically joins the transaction.

## When to use and what to inspect

Use for shared-write invariants or race-sensitive workflows. Inspect all writers, required atomic effects, isolation/locking behavior and how failures are surfaced.

## Apply the idea

1. State the invariant and the concrete concurrent interleaving that could violate it.
2. Place the effects in a local transaction and use database constraints, locks or revision predicates for the specific anomaly.
3. Keep network/human waiting outside the transaction; compare the revision again at commit.
4. Handle conflicts distinctly from unexpected storage failures and specify safe retry semantics.

## Worked application

Two reviewers read revision 2. Publishing must append its decision and update the current pointer only if revision is still 2. The second reviewer then sees a stale-review conflict instead of overwriting revision 3. If decision insertion fails, the pointer change must roll back too.

## Trade-offs and simpler choice

Long locks hurt concurrency; optimistic control may require user retry. A single conditional update can be simpler than a new domain framework, but a pre-write SELECT alone does not prevent races.

## Verify the decision

Use independent connections to force the interleaving; inject failure between effects and confirm rollback/retry. Check the actual database behavior rather than treating SQLite proof as PostgreSQL proof.
