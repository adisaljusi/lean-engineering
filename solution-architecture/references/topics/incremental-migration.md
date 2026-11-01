# Incremental migration and compatibility stages

## Book material

**Foundation:** Sam Newman — Monolith to Microservices. **Concept/locator:** Author topic list: incremental decomposition, migration patterns and database decomposition. [Source / locator](https://samnewman.io/books/monolith-to-microservices/). **Evidence basis:** `author-overview`.

Moving away from a monolith is an evolutionary change to a running system. Incremental decomposition must account for continued behavior and for the referential, transactional and failure consequences of moving data.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use for a consequential boundary/data migration. Inspect current callers, writers, data ownership, transaction invariants, rollback constraints and deployment order.

## Apply the idea

1. Choose one bounded capability and an interception/compatibility boundary while preserving the current contract.
2. Identify the source of truth at each stage and how data is copied/reconciled without accidental dual ownership.
3. Roll out a reversible traffic/ownership change and compare behavior before retiring the old path.
4. Name destructive or irreversible steps and the recovery evidence required before them.

## Worked application

Move extraction execution to a worker while the application still owns job acceptance and review/publication. Deploy a backward-compatible job reader first, then route a limited set of new jobs and compare outputs/recovery. Do not move publication tables at the same time unless their invariants require it.

## Trade-offs and simpler choice

Temporary adapters and migration states cost code and operations, but reduce big-bang risk. If a module boundary solves the problem, avoid the migration entirely.

## Verify the decision

Exercise old/new clients and pending work across version skew. Reconcile data before cutover and demonstrate rollback up to its stated irreversible point; backup existence alone is not a recovery test.
