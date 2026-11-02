# Bounded contexts, model boundaries and translation

## Book material

**Foundation:** Eric Evans — Domain-Driven Design: Tackling Complexity in the Heart of Software. **Concept/locator:** DDD Reference named patterns: Bounded Context; Context Map; Anti-Corruption Layer. [Source / locator](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf). **Evidence basis:** `author-reference`.

A bounded context makes the scope of a model/language explicit. The same term can carry different meanings in different contexts; integration should acknowledge that boundary rather than force one universal object model.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when teams/capabilities disagree on meaning or share objects with incompatible responsibilities. Inspect vocabulary, rule ownership, lifecycle and integration contracts.

## Apply the idea

1. Map where the same term has a distinct meaning and who owns each rule.
2. Define each model’s boundary and current relationship to neighboring contexts.
3. Translate at the boundary, preserving identity/authority semantics that must not be lost.
4. Do not equate a bounded context automatically with a new service, schema or class hierarchy.

## Worked application

An extracted “commission” is a candidate claim with evidence and uncertainty; a published commission is an authorized effective business term. Reusing one mutable object for both encourages premature publication. Separate responsibilities/contracts can exist inside the same application.

## Trade-offs and simpler choice

Boundary translation costs mapping and shared-language work. A single cohesive model is simpler when meaning/ownership actually coincide; do not split merely because two nouns differ.

## Verify the decision

Walk a correction and disputed source through both models: are identity, authority and unresolved alternatives preserved? Check translation examples against both owners.
