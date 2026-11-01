# SOLID as concrete change and contract decisions

## Book material

**Foundation:** Robert C. Martin — Clean Architecture: A Craftsman’s Guide to Software Structure and Design. **Concept/locator:** Part III, Chapters 7–11: SRP, OCP, LSP, ISP and DIP. [Source / locator](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/). **Evidence basis:** `publisher-toc`.

SOLID separates reasons to change and protects substitutable contracts: responsibility, extension, substitution, interface scope and dependency direction. These principles do not require an interface/class hierarchy for every function.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when responsibilities or caller contracts are coupled in a costly way. Inspect actual change history, variants, caller needs, exceptions and imports; do not apply all five as a ritual checklist.

## Apply the idea

1. SRP: identify distinct stakeholders/reasons that change a module and separate only when this coupling causes cost.
2. OCP: isolate a real variation behind a stable contract; LSP: require variants to preserve caller-visible behavior, preconditions and error expectations.
3. ISP: offer a caller the operations it actually needs; DIP: let stable policy own the boundary instead of importing volatile adapter types.
4. Compare the result with a cohesive function/module and remove interfaces that protect no real variation or policy.

## Worked application

A publication policy must work from HTTP and batch without knowing either request type (DIP). A gateway adapter cannot silently return an unverified claim where callers expect source-verified evidence (LSP). Splitting one handler into seven forwarding classes creates no independent responsibility or safe substitution.

## Trade-offs and simpler choice

Excess abstractions increase navigation and can hide behavior. For one fixed validation rule, a function with precise inputs/results is often the right expression of these principles.

## Verify the decision

Exercise the same caller contracts across supported variants, inspect dependency direction and see whether an actual change is localized. Test semantics, not whether every principle name appears in the design.
