# Adapter and an existing incompatible interface

## Book material

**Foundation:** Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides — Design Patterns: Elements of Reusable Object-Oriented Software. **Concept/locator:** Named GoF pattern: Adapter; exact chapter/page not retrieved. [Source / locator](https://www.oreilly.com/library/view/design-patterns-elements/0201633612/). **Evidence basis:** `book-synthesis`.

Adapter makes an existing interface usable through the interface a client needs. The point is an actual incompatibility at a boundary, not a wrapper around every collaborator.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when a vendor/library interface differs from the application contract. Inspect input/output meaning, errors, resource lifetime, versioning and current caller needs.

## Apply the idea

1. Specify the application-facing operation and the concrete incompatibility.
2. Translate inputs, outputs and expected errors without leaking vendor objects into policy.
3. Preserve identity, units and failure/timeout semantics; expose unsupported behavior honestly.
4. Keep composition at the existing boundary instead of inserting multiple forwarding layers.

## Worked application

A model SDK returns vendor-specific citation objects. An adapter converts them into candidate evidence references, then the application independently verifies exact source spans. The adapter must not label a model-generated explanation as verified evidence merely to fit the target type.

## Trade-offs and simpler choice

Adapters add mapping and can conceal useful capabilities. Call the existing API directly when it already matches the needed boundary and no independent policy is exposed to volatility.

## Verify the decision

Use contract examples against the adapter and representative real vendor responses/errors; mocks alone do not establish integration compatibility.
