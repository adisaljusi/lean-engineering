# Workloads, access patterns and indexes

## Book material

**Foundation:** Martin Kleppmann — Designing Data-Intensive Applications, first edition (2017). **Concept/locator:** Chapter 3: Storage and Retrieval — indexing structures; Transaction Processing or Analytics?. [Source / locator](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/). **Evidence basis:** `publisher-toc`.

Storage structures serve access patterns at different read, write and space costs. Transactional point/range access and analytical scans put different demands on layout and indexes.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use before adding a store, cache or in-memory representation. Inspect cardinality, row size, predicates, ordering, selectivity/skew, write rate, current indexes and query plans.

## Apply the idea

1. Write the dominant query including tenant scope and deterministic ordering.
2. Inspect its current execution plan and measure representative volume/skew.
3. Compare an existing index/query improvement against new storage, including write/storage and invalidation costs.
4. Bound application memory and batch size; only add a new store if the measured requirement remains unmet.

## Worked application

An audit export has 50 million rows and a (tenant, occurred_at, id) index. Filter one tenant, use the timestamp/id tie-breaker and stream bounded results rather than load/sort everything in Python. A single timestamp cursor can skip tied records. Snapshot and restart semantics remain separate decisions.

## Trade-offs and simpler choice

Indexes consume disk and write throughput; a cache introduces staleness/invalidation. An existing database query often beats a new service or loading a global hash set.

## Verify the decision

Inspect query plan, memory and throughput with representative row size/skew. Verify exact row coverage and tenant isolation, not only a fast small-fixture run.
