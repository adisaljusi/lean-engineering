# Message routing and destination policy

## Book material

**Foundation:** Gregor Hohpe and Bobby Woolf — Enterprise Integration Patterns. **Concept/locator:** Named pattern: Message Router. [Source / locator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageRouter.html). **Evidence basis:** `author-pattern-summary`.

A Message Router chooses where a message goes while separating that routing decision from the surrounding processing steps. Routing and transforming the message’s meaning are distinct responsibilities.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when messages have several legitimate destinations or processing paths. Inspect route authority, version/type discrimination, tenant isolation and unknown-route handling.

## Apply the idea

1. Make routing criteria explicit from trusted envelope/business data.
2. Keep the route decision testable and separate from payload normalization.
3. Specify one-vs-many destinations and how unknown/unsupported routes are handled.
4. Reuse existing dispatch code unless an independent integration boundary warrants more.

## Worked application

Signed publication events route to accepted downstream consumers; unsigned draft candidates route only to review. A filename hint must not grant publication authority. Unknown schema versions go to an explicit rejection/quarantine path rather than an arbitrary default.

## Trade-offs and simpler choice

A generic bus/registry can obscure ownership for two static routes. A simple explicit dispatch function is preferable until routing complexity or independent ownership justifies more.

## Verify the decision

Test every consequential route, untrusted discriminator and unknown version; verify that routing does not bypass tenant/business authorization.
