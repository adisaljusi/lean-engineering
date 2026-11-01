# Request/reply and synchronous versus asynchronous waiting

## Book material

**Foundation:** Gregor Hohpe and Bobby Woolf — Enterprise Integration Patterns. **Concept/locator:** Named pattern: Request-Reply. [Source / locator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html). **Evidence basis:** `author-pattern-summary`.

Request-Reply connects a request to a response. Messaging can implement the conversation asynchronously; request/reply semantics and a blocking network call are not the same architectural decision.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when a caller needs a result from another owner. Inspect result timing, acceptance/completion distinction, deadlines, retry identity and how replies are matched.

## Apply the idea

1. Decide whether the caller needs completion now or merely durable acceptance and a later status.
2. Define request/result/error contracts and correlation across transport boundaries.
3. Bound waits and specify the ambiguous outcome when a timeout occurs after remote acceptance.
4. Use persisted jobs/status only when asynchronous completion/durability warrants them.

## Worked application

OCR extraction can return a durable run ID and expose later completion rather than hold an HTTP request for minutes. Reviewing a current published value can remain a short synchronous read. Both provide results, but only the long-running path needs accepted-vs-completed state.

## Trade-offs and simpler choice

Async request/reply adds state, correlation and cleanup; sync calls couple availability/latency. A local call is simpler when no process boundary is needed.

## Verify the decision

Test success, rejected request, lost/late reply and timeout after acceptance; confirm retries do not create new work accidentally.
