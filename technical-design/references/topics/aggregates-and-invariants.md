# Aggregates, invariants and transaction ownership

## Book material

**Foundation:** Eric Evans — Domain-Driven Design: Tackling Complexity in the Heart of Software. **Concept/locator:** DDD Reference named pattern: Aggregates; consistency boundary guidance. [Source / locator](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf). **Evidence basis:** `author-reference`.

An aggregate groups related model state under an invariant-owning boundary. Its root controls changes; a useful boundary follows consistency requirements rather than collecting every related object.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## Important distinctions

- Aggregate boundaries describe invariant ownership; entity relationships alone do not decide that every related object must join the aggregate.
- The root controls changes at the boundary. References/read models may expose useful data without granting arbitrary mutation.
- Business rules can require consistency across operations; persistence must enforce the concurrency aspect against all writers, not only well-behaved in-memory objects.

## When to use and what to inspect

Use when several writes must preserve a business rule or ownership is unclear. Inspect allowed transitions, concurrent writers, shared relationships and which effects must commit together.

## Apply the idea

1. State the invariant with concrete data and identify the operation allowed to change it.
2. Keep the consistency boundary as small as the invariant permits.
3. Route mutation through its owner and enforce shared-write constraints/concurrency in persistence.
4. Model cross-boundary progress/failure explicitly instead of stretching one object graph into a distributed transaction.

## Worked application

Publication’s current pointer and appended decision must advance together under a revision check. Immutable OCR pages do not need to be locked or rewritten in that transaction. Grouping every document, candidate and history row into a giant treaty object would increase lock/load cost without protecting another invariant.

## Trade-offs and simpler choice

A large aggregate can serialize unrelated work; too small a boundary can lose atomic rules. Straightforward row/transaction operations may express the invariant without an elaborate object hierarchy.

## Verify the decision

Use concurrent attempts and mid-transaction failure to verify invariant preservation. Inspect bypass writers, not just root methods in unit tests.
