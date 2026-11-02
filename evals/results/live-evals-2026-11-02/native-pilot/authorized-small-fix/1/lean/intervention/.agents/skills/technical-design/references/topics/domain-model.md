# Domain Model for interacting business rules

## Book material

**Foundation:** Martin Fowler (with contributors) — Patterns of Enterprise Application Architecture. **Concept/locator:** Named pattern: Domain Model (author catalog identifies Chapter 09). [Source / locator](https://martinfowler.com/eaaCatalog/domainModel.html). **Evidence basis:** `author-pattern-summary`.

A Domain Model combines business data and behavior in an object model. Its value comes from organizing interacting rules and lifecycle responsibilities, not from replacing every function with a class.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when multiple operations share complex invariants/state transitions. Inspect actual rule interactions, identity, lifecycle, persistence mismatch and existing policy duplication.

## Apply the idea

1. Model the small set of decisions/relationships that enforce the accepted rules.
2. Keep meaningful operations with their invariant owner and represent simple descriptions as values.
3. Separate storage/transport details when they would distort the model.
4. Compare the comprehensibility of this model with a direct transaction script for today’s behavior.

## Worked application

A decision lifecycle may reject unsigned evidence, require authority and reason, and invalidate stale review across several operations. Centralizing those transitions can reduce divergent scripts. A lone percentage range check remains a value/function; it does not need an entity graph.

## Trade-offs and simpler choice

Richer models cost mapping, loading and navigation; an anemic object wrapper can add cost without centralizing rules. Prefer a script where interactions remain simple.

## Verify the decision

Check legal/illegal transitions and the same rule through all entry points. Verify the actual persistence integration, not only object methods.
