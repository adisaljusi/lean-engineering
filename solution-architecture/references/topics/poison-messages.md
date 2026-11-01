# Poison messages, quarantine and safe replay

## Book material

**Foundation:** Gregor Hohpe and Bobby Woolf — Enterprise Integration Patterns. **Concept/locator:** Named pattern: Dead Letter Channel. [Source / locator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html). **Evidence basis:** `author-pattern-summary`.

A Dead Letter Channel makes undeliverable messages explicit instead of losing them in normal delivery. Application poison-message handling also needs diagnosis, ownership and safe reprocessing; putting a message in a queue does not resolve it.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when malformed/permanently failing work can block progress or exhaust retries. Inspect failure classification, retry budget, sensitive payload storage, operator authority and replay identity.

## Apply the idea

1. Separate transient delivery failures from invalid/unsupported commands and exhausted work.
2. Persist a diagnosable failure reference with original identity, reason, attempts and an accountable owner.
3. Prevent one poison message from silently blocking unrelated work while preserving required ordering/invariants.
4. Specify correction/replay and authorization; replay must preserve duplicate-effect safety.

## Worked application

An extraction candidate references an unsupported OCR schema. Retrying the same parser forever cannot fix it. Keep the run/evidence identity and explicit failure; after a compatible translator is deployed, replay the same logical work without duplicating accepted candidates or bypassing human publication.

## Trade-offs and simpler choice

Quarantine creates storage, privacy and operational duties. A direct synchronous validation error is simpler when no durable work has been accepted.

## Verify the decision

Inject invalid messages and retry exhaustion, then rehearse diagnosis, correction and replay. Verify no silent loss, uncontrolled retry loop or duplicated effect.
