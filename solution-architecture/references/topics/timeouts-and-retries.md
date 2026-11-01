# Timeouts, retries and partial failure

## Book material

**Foundation:** Martin Kleppmann — Designing Data-Intensive Applications, first edition (2017). **Concept/locator:** Chapter 8: The Trouble with Distributed Systems — Faults and Partial Failures; Timeouts and Unbounded Delays. [Source / locator](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/). **Evidence basis:** `publisher-toc`.

In distributed systems, a missing response leaves uncertainty: a remote operation may have failed, succeeded or still be running. Timeouts detect a bounded wait, not proof that no effect occurred.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use for any remote operation with retries/cancellation. Inspect total deadline, failure categories, stable identity, side effects, provider status lookup and recovery ownership.

## Apply the idea

1. Set a total operation budget and propagate supported deadlines; distinguish invalid/permanent failures from transient ones.
2. Retry only safe/reconcilable operations with stable identity, bounded attempts and backoff/jitter.
3. Treat timeout-after-acceptance as an unknown outcome and reconcile before creating another business effect.
4. Keep cancellation/cleanup explicit; stopping the local wait need not stop remote work.

## Worked application

The model gateway accepts extraction command C but its reply is lost. Retrying as C can recover/status-check the same work; submitting C2 blindly can duplicate cost/candidates. A timed-out external charge needs provider-supported idempotency/status reconciliation, not another unkeyed charge.

## Trade-offs and simpler choice

Retries amplify load during outages and may increase latency/cost. For a short read, returning a clear temporary failure can be simpler than durable retry infrastructure.

## Verify the decision

Simulate loss before/after acceptance, slow replies and retry exhaustion; verify one business effect and an inspectable unknown/recoverable state.
