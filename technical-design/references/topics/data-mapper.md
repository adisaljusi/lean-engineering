# Data Mapper and persistence independence

## Book material

**Foundation:** Martin Fowler (with contributors) — Patterns of Enterprise Application Architecture. **Concept/locator:** Named pattern: Data Mapper. [Source / locator](https://martinfowler.com/eaaCatalog/dataMapper.html). **Evidence basis:** `author-pattern-summary`.

Data Mapper separates an in-memory domain model from its database representation. It addresses a real mismatch between object responsibilities/structures and persistence, rather than serving as mandatory plumbing.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when a meaningful domain model and schema evolve differently. Inspect loading/writing needs, relationships, query cost, existing ORM facilities and transaction ownership.

## Apply the idea

1. Name which persistence detail currently leaks into or constrains business policy.
2. Define the conversion/loading boundary for the affected model and reuse the existing mapper/ORM if suitable.
3. Keep transaction and identity/loading behavior explicit; avoid hiding uncontrolled queries.
4. Check whether direct rows/records would be simpler for a read-only or CRUD operation.

## Worked application

A publication decision model can use precise values and transitions while a mapper persists rows/foreign keys/history. The mapper must preserve candidate/source identity and unknown values; returning an ORM row as the supposed domain boundary leaves the dependency leak unresolved.

## Trade-offs and simpler choice

Mapping adds conversion and performance risks, including excessive queries. Direct SQL/read DTOs are often better for reporting projections without independent domain behavior.

## Verify the decision

Test model↔persistence round trips, relationships and query behavior against a real database, including null/unknown/version cases.
