# Observability and operational responsibility

## Book material

**Foundation:** Sam Newman — Building Microservices, second edition. **Concept/locator:** Second edition, Chapter 10: From Monitoring to Observability; Chapter 12: Resiliency. [Source / locator](https://samnewman.io/books/building_microservices_2nd_edition/). **Evidence basis:** `author-toc`.

Observability extends beyond static monitoring to understanding service behavior and diagnosing interactions. A distributed design needs an operational owner and usable failure/recovery evidence, not only a happy-path topology.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when adding runtime boundaries, durable work or failure modes. Inspect current logging/metrics/tracing, incident questions, privacy, SLOs and on-call responsibility.

## Apply the idea

1. List the questions an operator must answer: accepted, executing, stalled, failed, retried or published?
2. Emit safe operation/run/entity/revision linkage and measure meaningful latency, backlog age, errors and saturation.
3. Define alert meaning, owner and response/replay procedure rather than a dashboard count.
4. Check the failure path with the same evidence an operator will actually have.

## Worked application

For a stalled extraction run, operations must find its accepted input versions, pending page jobs, gateway attempt/error and current decision revision without reading sensitive PDF text from logs. Oldest pending age is more useful than a worker process merely being alive.

## Trade-offs and simpler choice

High-cardinality telemetry and sensitive payload logging have cost/privacy risks. Existing structured logs and a few actionable measures may suffice for a small service.

## Verify the decision

Rehearse a timeout, poison job and worker restart using retained telemetry; confirm the responsible operator can diagnose/recover within accepted requirements.
