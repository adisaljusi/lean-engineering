# Message translation and boundary semantics

## Book material

**Foundation:** Gregor Hohpe and Bobby Woolf — Enterprise Integration Patterns. **Concept/locator:** Named pattern: Message Translator. [Source / locator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html). **Evidence basis:** `author-pattern-summary`.

A Message Translator converts between representations used by different applications. Conversion must respect meaning, not merely rename similarly spelled fields.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use for vendor/domain/API format boundaries. Inspect units, unknown/null behavior, identity, schema versions, authority and information that conversion could lose.

## Apply the idea

1. Define source and target meaning with concrete values before choosing conversion code.
2. Translate at the boundary and preserve raw/provenance information when later adjudication needs it.
3. Reject or mark unsupported/ambiguous values instead of inventing defaults.
4. Version/test conversion behavior when old and new producers coexist.

## Worked application

A vendor emits commission “12.5%”; the application needs 1250 integer basis points. Parse exactly, preserve the raw claim/evidence and distinguish missing from zero. Converting “12.505%” by silent rounding changes a business fact and requires an explicit accepted rule.

## Trade-offs and simpler choice

A universal canonical model can spread coupling and require unnecessary conversions. A small boundary function is simpler for one integration; it should still have precise error semantics.

## Verify the decision

Check boundary values, unknowns, incompatible units, version skew and semantic round trips where possible; string-shape/schema validation alone is insufficient.
