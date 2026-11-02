# Dependency direction and business-rule isolation

## Book material

**Foundation:** Robert C. Martin — Clean Architecture: A Craftsman’s Guide to Software Structure and Design. **Concept/locator:** Chapter 22: The Clean Architecture — The Dependency Rule; supplemented by the author’s Dependency Rule / boundary-crossing article. [Source / locator](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html). **Evidence basis:** `author-summary`.

Business policy should not depend on volatile framework, transport or database representations. Control can call outward while source dependencies point toward an inward-owned contract; crossing a boundary need not imply a fixed number of layers.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## Important distinctions

- Source dependency and runtime control flow can point in different directions through an inward-owned interface.
- Entities/general policy, application use cases and outer mechanisms have different reasons to change; they are not mandated package counts.
- Passing a framework-owned request/row inward can preserve the dependency even when the function signature looks abstract.

## When to use and what to inspect

Use when transport/storage change leaks into business rules or policy needs independent verification. Inspect imports, call flow, shared types, current adapters and what actually changes together.

## Apply the idea

1. Trace one business operation and distinguish policy decisions from I/O and conversion.
2. Keep policy inputs/results independent of framework request/ORM row types where that boundary has value.
3. If policy calls a volatile collaborator, define the smallest inward-owned callable/protocol and supply the adapter from the composition point.
4. Retain a direct function/SQL path when there is no independent policy or adapter volatility worth isolating.

## Worked application

Publication authority must be identical from HTTP and a batch tool. Both parse their input into a tenant/actor/revision command and call the same policy operation. SQL and HTTP exception mapping remain outside it. Changing the web framework should not change who can publish. An unchanged forwarding service class adds no such protection.

## Trade-offs and simpler choice

Ports and conversion cost code and navigation. One policy function and an existing transaction owner may be sufficient; do not reproduce four circles as four packages for a literal correction.

## Verify the decision

Exercise the policy with concrete domain values without starting HTTP. Inspect dependency direction and also run the real persistence/authorization path; isolated unit tests alone cannot establish adapter correctness.

Book chapter location also verified in the [Clean Architecture publisher table of contents](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/). The author article supports the explanation; neither link establishes full-book access.
