# Publish/subscribe and independent consumers

## Book material

**Foundation:** Gregor Hohpe and Bobby Woolf — Enterprise Integration Patterns. **Concept/locator:** Named pattern: Publish-Subscribe Channel. [Source / locator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html). **Evidence basis:** `author-pattern-summary`.

Publish-Subscribe Channel distributes a fact to interested receivers instead of addressing one worker. The topology expresses fan-out, not a universal exactly-once processing guarantee.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when independently owned consumers react to a fact. Inspect consumer responsibilities, subscriptions/durability, ordering, replay and publication authority.

## Apply the idea

1. Publish an accepted fact rather than a command whose several consumers might all perform the same effect.
2. Define each consumer’s state, version contract and failure/retry responsibility.
3. Specify whether absent/offline subscribers retain history and for how long.
4. Keep authoritative state separate from lagging consumer projections.

## Worked application

After a publication commits, search and audit notification consumers may independently react. Neither is authorized to republish the commission, and failure of notification must not undo the accepted business decision. Local notifications with one caller may not need a broker.

## Trade-offs and simpler choice

Fan-out increases delivery, schema and replay obligations. Direct calls or one durable job are simpler when there is one owner and no independent-consumer requirement.

## Verify the decision

Exercise an offline consumer, duplicates, changed schemas and replay; verify one consumer failure does not silently lose another’s required work.
