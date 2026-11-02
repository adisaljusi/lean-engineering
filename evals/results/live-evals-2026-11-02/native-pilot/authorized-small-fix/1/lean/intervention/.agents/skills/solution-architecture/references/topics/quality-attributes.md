# Quality attributes and architectural trade-offs

## Book material

**Foundation:** Mark Richards and Neal Ford — Fundamentals of Software Architecture (2020). **Concept/locator:** Chapters 4–6: Architecture Characteristics Defined; Identifying Architectural Characteristics; Measuring and Governing Architecture Characteristics. [Source / locator](https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/). **Evidence basis:** `publisher-toc`.

Architecture characteristics derive from business needs and constrain structural choices. Important qualities compete; identifying and measuring them is more useful than claiming every design is scalable, reliable and simple.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when alternatives differ in latency, consistency, recovery, security, deployment or cost. Inspect business consequences, workload, existing measurements and which targets are accepted.

## Apply the idea

1. Express the actual stimulus, workload/environment, required response and measure or explicitly unknown target.
2. Separate hard invariants from preferences; eliminate options violating the former.
3. Compare remaining options on the drivers that distinguish them and expose the cost of each.
4. Name the measurement or changed condition that would justify revisiting the recommendation.

## Worked application

Interactive review must stay usable while extraction jobs wait on model calls. First measure request latency and gateway concurrency. A bounded worker may isolate slow work without a new service boundary. A service split is credible if independent ownership or measured contention remains; “future scale” alone supplies no target.

## Trade-offs and simpler choice

More availability may require accepting stale reads; lower latency may cost storage or operational complexity. For a small local change, a short constraint statement beats a generic weighted scorecard.

## Verify the decision

Check the chosen option against concrete load/recovery scenarios and accepted limits. An unmeasured target is still unknown; a diagram or adjective is not a benchmark.
