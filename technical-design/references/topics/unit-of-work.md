# Unit of Work and coordinated persistence

## Book material

**Foundation:** Martin Fowler (with contributors) — Patterns of Enterprise Application Architecture. **Concept/locator:** Named pattern: Unit of Work. [Source / locator](https://martinfowler.com/eaaCatalog/unitOfWork.html). **Evidence basis:** `author-pattern-summary`.

A Unit of Work tracks model changes associated with a business transaction and coordinates their persistence. Tracking changes and owning a database transaction are related responsibilities, but a new UoW abstraction is not always needed.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when multiple model changes must be flushed consistently. Inspect existing ORM/session behavior, transaction scope, concurrency conflicts and resource lifetime.

## Apply the idea

1. Identify all changes that belong to one business commit and who owns that scope.
2. Reuse the existing session/transaction facility for tracking/flush if it already supplies it.
3. Define commit/rollback/conflict behavior and close resources at the correct boundary.
4. Do not keep a database transaction open across a human interaction or slow remote call.

## Worked application

Appending an adjudication and moving the publication pointer must commit together. An existing ORM session can track both; explicit SQL with one short transaction may also suffice. Introducing a separate UoW interface that just forwards commit does not itself protect the revision invariant.

## Trade-offs and simpler choice

Extra tracking abstractions add lifetime and hidden-flush complexity. A transaction context is simpler for a small script when object-change tracking is unnecessary.

## Verify the decision

Force failure after the first change, stale revision and flush errors; confirm no partial commit and resources are released.
