# Schema evolution and backward compatibility

## Book material

**Foundation:** James Gough, Daniel Bryant and Matthew Auburn — Mastering API Architecture (2022). **Concept/locator:** Chapter 1: Design, Build, and Specify APIs — API Versioning; Detecting Changes. [Source / locator](https://www.oreilly.com/library/view/mastering-api-architecture/9781492090625/). **Evidence basis:** `publisher-toc`.

API versioning and change detection must account for consumers, not just producer schemas. Compatibility also depends on behavior and supported client decoders, so adding a field or enum is not universally safe.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## Important distinctions

- Backward compatibility concerns a new reader/server handling old inputs/clients; forward compatibility concerns old readers tolerating newer data. Name the direction for the actual exchange.
- Wire compatibility, generated-type compatibility and behavioral compatibility are separate checks.
- Historical stored values and queued events can outlive a deployment, so compatibility is more than two live service versions.
- A version number is a policy/selection mechanism, not proof that a change preserves a consumer contract.

## When to use and what to inspect

Use when fields, enum values, units, errors or stored/event schemas evolve. Inspect strict/lenient clients, release control, old data/messages, overlap window and rollback.

## Apply the idea

1. Inventory consumers/readers/writers and define old/new semantics with concrete values.
2. Choose an expand/compatible representation or versioned contract according to actual client behavior.
3. Deploy compatible readers first, backfill/reconcile, migrate producers and observe old use before contraction.
4. State conflict rules, deprecation conditions and the irreversible rollback point.

## Worked application

Old shipping clients reject status held. A new enum cannot be silently added to their existing response. A versioned/negotiated representation may protect them while newer clients receive held and integer grams; mapping held to sent would invent accepted behavior.

## Trade-offs and simpler choice

Supporting two representations costs implementation/telemetry and may delay removal. Keeping the existing contract is simpler if no consumer requires the new representation.

## Verify the decision

Run strict old and new consumers across mixed versions, unknown/null values, conflicting dual fields and rollback. Test stored/message replay too where affected.

## Further detail

Related book material: Kleppmann, DDIA first edition, [Chapter 4: Encoding and Evolution](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/), including dataflow through databases, services and messages. Locator verified from publisher TOC; full passages not retrieved.
