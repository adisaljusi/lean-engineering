# Algorithm cost and data-structure selection

## Book material

**Foundation:** Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein — Introduction to Algorithms, fourth edition. **Concept/locator:** Algorithm analysis and data structures; no chapter/page locator claimed. [Source / locator](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/). **Evidence basis:** `publisher-overview`.

Algorithm analysis relates resource growth to input size and operations; data structures trade access, update and memory costs. Complexity notation supports a workload decision rather than replacing measurement.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when cardinality/access shape changes design or a measured bottleneck exists. Inspect real n, data size/skew, operation frequencies, library/database support and memory budget.

## Apply the idea

1. State the dominant operation: membership, ranges, ordered traversal, grouping, top-k or joins.
2. Compare asymptotic cost and practical memory/I/O for candidate representations.
3. Use existing standard-library/database structures and avoid loading data that can be filtered/indexed at its owner.
4. Measure representative data/skew and keep the simplest representation that meets requirements.

## Worked application

Comparing c candidate spans against h historical spans costs O(c × h), becoming quadratic when both populations grow together. Group by tenant/treaty/field and resolve only referenced IDs with an index. For one run’s small candidate set a dict/set can suffice; a 50-million-row export needs bounded iteration and database ordering, not a global Python sort.

## Trade-offs and simpler choice

Hash structures cost memory and do not provide range ordering; indexes cost writes/storage. A list scan can be clearer and fast enough for a genuinely small fixed collection.

## Verify the decision

Benchmark growth and memory with realistic inputs, verify exact matching/coverage, and inspect the query plan before claiming an optimization.

## Further detail

Official Python collections/heapq documentation describes available implementations. The publisher verifies the fourth-edition book identity; no chapter/page passage verification is claimed.
