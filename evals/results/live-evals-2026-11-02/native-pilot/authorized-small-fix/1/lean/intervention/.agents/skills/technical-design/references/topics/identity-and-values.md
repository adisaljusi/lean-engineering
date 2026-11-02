# Entities, value objects and precise identity

## Book material

**Foundation:** Eric Evans — Domain-Driven Design: Tackling Complexity in the Heart of Software. **Concept/locator:** DDD Reference named patterns: Entities; Value Objects. [Source / locator](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf). **Evidence basis:** `author-reference`.

Entities preserve identity through change; value objects are described by their attributes/meaning. The distinction is about the domain lifecycle, not whether a programming language uses a class.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when equality, mutation, references or persistence identity affect behavior. Inspect domain terms, units, lifecycle, who changes data and what must remain identifiable.

## Apply the idea

1. Ask whether two instances with the same attributes are interchangeable in the business.
2. Assign stable identity to things whose continuity matters; use value equality for replaceable descriptions.
3. Define units and unknown/invalid distinctions explicitly at boundaries.
4. Choose a record/dataclass/function representation before adding behavioral hierarchy.

## Worked application

Two rate values of 1300 basis points can compare equal. Two extracted candidates both saying 1300 are not interchangeable: they have different source evidence/run identities and may have different authority. Preserve candidate identity while keeping rate semantics precise.

## Trade-offs and simpler choice

Turning every noun into an entity/class adds accidental identity and mutable state. A simple immutable value record is preferable for units/ranges without an independent lifecycle.

## Verify the decision

Test equality and update/reference behavior with actual domain examples, including equal values with distinct evidence identity.
