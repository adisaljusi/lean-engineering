# Partitioning, skew and cross-partition invariants

## Book material

**Foundation:** Martin Kleppmann — Designing Data-Intensive Applications, first edition (2017). **Concept/locator:** Chapter 6: Partitioning — Skewed Workloads and Relieving Hot Spots; Secondary Indexes; Rebalancing Partitions. [Source / locator](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/). **Evidence basis:** `publisher-toc`.

Partitioning divides data/work among nodes. Key choice affects routing, range access, hotspots, indexes and rebalancing; cross-partition operations often add coordination.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## Important distinctions

- Range partitioning supports ordered access but can create hot ranges; hashing spreads many keys but complicates range queries.
- Local versus distributed secondary indexes shift query and write work differently.
- Partitioning and replication solve different problems: dividing data is not the same as maintaining redundant copies.
- Rebalancing is part of normal operation, not an afterthought once traffic grows.

## When to use and what to inspect

Use when a single database/partition no longer meets a measured storage or throughput requirement. Inspect tenant/key distribution, queries, invariant scope and growth/skew.

## Apply the idea

1. Measure the bottleneck and check simpler query/index/capacity options first.
2. Choose a partition key against both access patterns and skew, including unusually large tenants.
3. Identify uniqueness/transactions spanning partitions and how they remain correct.
4. Plan routing/rebalancing and failure recovery before assigning capacity gains.

## Worked application

Partitioning extraction runs by tenant preserves most tenant-local access, but one very large tenant can still overload a partition. Splitting by run may distribute work while making treaty-wide queries and constraints more expensive. Compare those actual operations before choosing.

## Trade-offs and simpler choice

Cross-partition joins, rebalancing and global uniqueness cost complexity. Keep one database when measured capacity is sufficient; partitioning is not a substitute for an index.

## Verify the decision

Benchmark skewed workloads and rehearse rebalancing/outage while checking complete queries and invariant enforcement.
