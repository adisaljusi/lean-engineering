# Correlation, causation and message identity

## Book material

**Foundation:** Gregor Hohpe and Bobby Woolf — Enterprise Integration Patterns. **Concept/locator:** Named pattern: Correlation Identifier. [Source / locator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CorrelationIdentifier.html). **Evidence basis:** `author-pattern-summary`.

Correlation Identifier lets a receiver associate a reply with its request. It is not the same as the identity used to deduplicate an effect, nor is a correlation value an authorization credential.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use across async steps or request/reply. Inspect request identity, delivery attempts, workflow/run identity, tracing, tenant boundaries and retention.

## Apply the idea

1. Define which identifier names logical work, which names an attempt and which links the response/workflow.
2. Persist enough linkage to diagnose/reconcile ambiguous outcomes without treating new attempts as new business operations.
3. Validate tenant/access independently from all tracing/correlation fields.
4. Propagate useful IDs in safe logs/status and limit retained sensitive payload.

## Worked application

Run R has extraction command C and retry attempts A1/A2. Both attempts must update the same logical candidate operation; assigning a new business ID on A2 could duplicate it. A reply includes C’s correlation so it cannot be attached to another run.

## Trade-offs and simpler choice

Too many interchangeable ID fields make diagnosis harder. For a local synchronous operation, existing request/entity IDs may suffice; add distinct identities only for distinct lifecycles.

## Verify the decision

Send interleaved replies/retries and verify they attach to the correct work with no duplicated effect or cross-tenant lookup.
