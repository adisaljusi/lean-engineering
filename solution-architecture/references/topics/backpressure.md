# Backpressure and bounded concurrency

## Book material

**Foundation:** Sam Newman — Building Microservices, second edition. **Concept/locator:** Second edition, Chapter 12: Resiliency; Chapter 13: Scaling. [Source / locator](https://samnewman.io/books/building_microservices_2nd_edition/). **Evidence basis:** `author-toc`.

Resiliency and scaling require controlling the work a service accepts and performs. Adding workers does not remove limits imposed by downstream capacity or by queued work.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when bursts or slow dependencies threaten latency/memory/recovery. Inspect arrival rate, service time, downstream limits, queue growth, retries and admission expectations.

## Apply the idea

1. Measure both active operations and queued/pending work; choose bounds from capacity and accepted latency/recovery targets.
2. Apply admission control, batching or backpressure where overload is observed, with an explicit caller result.
3. Reserve deadlines/cancellation and resource cleanup for admitted work; avoid unbounded retry/task creation.
4. Expose queue age, rejection and saturation so operators can act.

## Worked application

An extraction worker may run at most eight gateway requests, but creating a task for every span still uses unbounded memory. Feed a bounded queue from page batches, persist accepted jobs and reject/defer admission according to the service contract. Eight is an example measured/configured limit, not a universal default.

## Trade-offs and simpler choice

Bounds can defer/reject work and need a fairness policy; durable queues cost operations. Synchronous bounded execution is simpler at low volume with no accepted-work durability requirement.

## Verify the decision

Burst above capacity and slow the gateway; confirm bounded memory/active work, understandable caller status, cancellation cleanup and backlog recovery.

## Further detail

This bounded producer/consumer procedure is original application guidance, not a claimed code listing from Newman. Python asyncio.Queue documentation specifies local queue behavior.
