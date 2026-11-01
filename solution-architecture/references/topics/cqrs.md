# CQRS and separate read/write models

## Book material

**Foundation:** Martin Kleppmann — Designing Data-Intensive Applications, first edition (2017). **Concept/locator:** Related DDIA material: Chapter 11, Databases and Streams; this named CQRS interpretation is supported by Fowler’s supplementary article. [Source / locator](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/). **Evidence basis:** `publisher-toc`.

CQRS separates the model used to perform updates from the model used to answer queries. It can help divergent read/write needs but does not require separate services/databases or event sourcing.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## Important distinctions

- Command/query separation within one object is not automatically CQRS with distinct models.
- CQRS does not imply event sourcing, asynchronous messaging or separate databases; those are separate decisions.
- A faster read projection still needs a declared freshness/rebuild contract and cannot silently replace the authoritative write invariant.

## When to use and what to inspect

Use when read shapes/performance or domain write behavior genuinely diverge. Inspect current queries, update invariants, allowed projection lag, rebuilding and failure expectations.

## Apply the idea

1. Identify the concrete read problem a query/view cannot already solve.
2. Keep write invariants with the authoritative owner; specify how the read model is derived.
3. Define lag, rebuild, versioning and source-of-truth behavior before splitting storage/deployment.
4. Compare the operational/change cost with the simplest query/index alternative.

## Worked application

Reviewers need a conflict list grouped by field across candidates, while publication updates a revision-checked decision. A SQL projection/view may satisfy that read shape. A separately maintained search index is warranted only by actual query/latency needs and must not authorize publication from stale state.

## Trade-offs and simpler choice

Projection lag, dual models and rebuilds add risk. A single schema with different query functions is often enough; do not add CQRS because an API has both GET and POST.

## Verify the decision

Compare projection rebuild with authoritative data, delay updates and test that stale reads cannot violate publication invariants.

## Further detail

Martin Fowler, [CQRS](https://martinfowler.com/bliki/CQRS.html), explicitly discusses differing read/update models and complexity. No claim is made that CQRS is a named chapter in DDIA.
