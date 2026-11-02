# Batch processing and reproducible inputs

## Book material

**Foundation:** Martin Kleppmann — Designing Data-Intensive Applications, first edition (2017). **Concept/locator:** Chapter 10: Batch Processing — Batch Processing with Unix Tools; The Output of Batch Workflows; Materialization of Intermediate State. [Source / locator](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/). **Evidence basis:** `publisher-toc`.

Batch computation transforms a bounded input dataset into derived output. Explicit inputs and intermediate/output boundaries support reprocessing; implementation choice should follow workload rather than require a distributed framework.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use for exports, fixed-corpus extraction/evaluation or backfills. Inspect input identity/snapshot, ordering, memory, transformation versions and restart requirements.

## Apply the idea

1. Define the bounded input and immutable identities/snapshot that make a run comparable.
2. Choose streaming/local tools before distributed execution when capacity permits.
3. Write outputs/checkpoints with stable run/partition identity and prevent partial output from appearing complete.
4. Define re-run/restart semantics and retain errors/versions needed to explain differences.

## Worked application

Export a tenant’s audit snapshot into a staged artifact, recording snapshot/run identity and transformation version. Finalize only after coverage checks pass. A restart using a new live query is a different snapshot, even if it uses the same filename.

## Trade-offs and simpler choice

Long snapshots can pressure retention/vacuum; materializing inputs costs storage. A small bounded script may suffice, while huge datasets warrant partitioned processing with explicit merge/coverage rules.

## Verify the decision

Interrupt and resume/re-run, compare row coverage/checksums under declared semantics, and ensure partial artifacts are not mistaken for complete exports.
