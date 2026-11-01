# Repository as a domain collection boundary

## Book material

**Foundation:** Martin Fowler (with contributors) — Patterns of Enterprise Application Architecture. **Concept/locator:** Named pattern: Repository. [Source / locator](https://martinfowler.com/eaaCatalog/repository.html). **Evidence basis:** `author-pattern-summary`.

A Repository offers collection-like access between domain and data mapping responsibilities. It can centralize meaningful query policy without forcing a generic CRUD interface over every table.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use where repeated domain-oriented access or persistence independence warrants a boundary. Inspect repeated queries, access control scope, caller needs and existing repository/ORM APIs.

## Apply the idea

1. Identify the query/collection semantics callers actually need, including tenant and lifecycle scope.
2. Expose those domain-oriented operations instead of forwarding every ORM method.
3. Keep loading cost and transaction ownership visible; do not conceal pagination or remote failure.
4. Reuse direct queries for simple projections or a lone operation with no abstraction benefit.

## Worked application

A decision operation needs “load reviewable candidate in this tenant at this revision,” not an unscoped generic get(id). The repository can enforce consistent query scope while authorization policy remains explicit. A wrapper that only renames ORM.get creates no such value.

## Trade-offs and simpler choice

Generic repositories can hide useful database features and grow into forwarding layers. Existing query functions are simpler when they already express stable access semantics.

## Verify the decision

Exercise tenant/lifecycle filtering and missing/stale results with real persistence; check callers cannot accidentally use unscoped access.
