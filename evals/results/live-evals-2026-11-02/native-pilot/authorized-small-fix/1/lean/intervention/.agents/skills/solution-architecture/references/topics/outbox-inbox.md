# Transactional outbox and consumer inbox

## Book material

**Foundation:** Sam Newman — Building Microservices, second edition. **Concept/locator:** Second edition, Chapter 6: Workflow (distributed-workflow context); outbox mechanism verified separately in author pattern material. [Source / locator](https://samnewman.io/books/building_microservices_2nd_edition/). **Evidence basis:** `author-toc`.

A distributed business workflow cannot assume that a local database commit and remote notification succeed atomically. Outbox/inbox is a concrete extension for reliable local commit plus at-least-once delivery and duplicate-safe consumer effects; it is not claimed as a named original EIP pattern.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use only when a committed local change must not lose its downstream intent. Inspect database ownership, relay/consumer transactions, identity, acknowledgment, replay and operating capacity.

## Apply the idea

1. Commit business state and outbox record in one local transaction.
2. Relay the persisted intent with stable event identity; allow crash-driven re-publication.
3. At the consumer atomically persist receipt identity and local effect before acknowledgment, comparing conflicting identity reuse.
4. Define cleanup, lag/retry/quarantine ownership and external-effect reconciliation.

## Worked application

Order O7 and event E7 commit. Relay sends E7 and crashes before marking sent, so sends again. Fulfillment’s inbox/effect transaction applies E7 once. If fulfillment calls a payment provider, its inbox does not atomically include that provider; use its supported idempotency/reconciliation contract.

## Trade-offs and simpler choice

Relay, retained IDs, duplicate traffic and backlog operations are real costs. One local transaction without messaging is preferable when all required effects share its database.

## Verify the decision

Crash at commit/send/mark/consumer-ack boundaries and replay duplicates; confirm accepted intent survives and each local effect is duplicate-safe.

## Further detail

Supplementary pattern: Chris Richardson, [Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html). The author pattern supplies the specific outbox mechanism; it is not attributed to a retrieved Newman passage.
