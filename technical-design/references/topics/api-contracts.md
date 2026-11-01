# API contracts and consumer-oriented design

## Book material

**Foundation:** James Gough, Daniel Bryant and Matthew Auburn — Mastering API Architecture (2022). **Concept/locator:** Chapters 1–2: Design, Build, and Specify APIs; Testing APIs. [Source / locator](https://www.oreilly.com/library/view/mastering-api-architecture/9781492090625/). **Evidence basis:** `publisher-toc`.

An API is an exchange contract whose behavior, formats and errors must be understandable to its consumers. A schema helps specify an interface; contract, component and integration tests establish different properties.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use for public/internal API creation or changed boundaries. Inspect actual consumers, operations, field meanings/units, error and authorization behavior, existing specifications and tests.

## Apply the idea

1. Define the consumer action and exchange including unknown/error/permission states.
2. Specify precise representation and error semantics using existing project tooling.
3. Separate schema/contract checks from real implementation/integration checks.
4. Keep internal table/ORM structure private unless deliberately part of the contract.

## Worked application

Shipping clients receive weight_kg as a decimal string and a limited status enum. A generated schema does not prove clients accept a new enum value. Preserve old semantics and define the precise grams/unknown representation before selecting a versioning strategy.

## Trade-offs and simpler choice

Contract tooling/governance costs should match consumer scale. A small internal function may need documented types and focused tests rather than an API gateway or governance platform.

## Verify the decision

Exercise representative old/new consumers, actual errors/authorization, schema behavior and a real integration path. A stub contract passing is not proof of service behavior.
