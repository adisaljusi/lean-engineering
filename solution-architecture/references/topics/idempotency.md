# Idempotent receivers and duplicate effects

## Book material

**Foundation:** Gregor Hohpe and Bobby Woolf — Enterprise Integration Patterns. **Concept/locator:** Named pattern: Idempotent Receiver. [Source / locator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html). **Evidence basis:** `author-pattern-summary`.

An Idempotent Receiver makes repeated delivery safe through deduplication or effect semantics. “Sent once” is not proof that a consumer receives or applies work once.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use for retries, redelivery, duplicate submissions or replay. Inspect identity scope, payload comparison, atomic effect boundary and deduplication retention.

## Apply the idea

1. Choose a stable identity for the business operation, scoped to the actual owner/tenant.
2. Atomically enforce identity and apply local effects; on retry compare the accepted payload.
3. Reject same identity/different content instead of silently accepting a conflicting retry.
4. For external effects use the provider’s supported idempotency/reconciliation contract; local deduplication alone is insufficient.

## Worked application

Webhook E7 records amount 100 and one ledger effect. Three identical retries return the agreed success without new effects. E7 with amount 101 returns conflict. Two independent connections cannot both insert the original effect because the database owns the invariant.

## Trade-offs and simpler choice

Retained identities cost storage and need lifecycle/expiry decisions. For a naturally idempotent “set state at revision” operation, semantic idempotency may be simpler than a separate cache.

## Verify the decision

Check concurrent duplicates, changed payload reuse, crash/rollback and retry after ambiguous external outcome—not only sequential mocked requests.
