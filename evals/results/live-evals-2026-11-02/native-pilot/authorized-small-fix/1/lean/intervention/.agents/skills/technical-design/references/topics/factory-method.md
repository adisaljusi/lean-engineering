# Factory Method and controlled construction

## Book material

**Foundation:** Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides — Design Patterns: Elements of Reusable Object-Oriented Software. **Concept/locator:** Named GoF pattern: Factory Method; exact chapter/page not retrieved. [Source / locator](https://www.oreilly.com/library/view/design-patterns-elements/0201633612/). **Evidence basis:** `book-synthesis`.

Factory Method lets a creator declare a construction operation while subclasses choose the concrete product through that operation. A generic factory helper and the specific GoF inheritance pattern are not interchangeable names.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when an actual creator/extension lifecycle must vary product construction. Inspect supported products, creation responsibility, configuration and whether ordinary composition is enough.

## Apply the idea

1. Name the construction variation that current requirements need.
2. Keep caller-visible contracts independent of the product’s concrete construction.
3. Prefer explicit construction/configuration or a simple callable unless a creator hierarchy is actually useful.
4. Keep side effects, resource ownership and configuration failure visible at creation.

## Worked application

The application currently supports one PostgreSQL client and one model gateway. Construct them at startup and pass them to the operation; there is no factory hierarchy to justify. If an existing plugin creator genuinely selects different supported gateway products, a creation extension point may fit.

## Trade-offs and simpler choice

A factory hierarchy for one product adds indirection and speculative extension cost. A function returning a configured client is often simpler, and should not be mislabeled the full GoF pattern.

## Verify the decision

Test supported product construction/configuration errors and cleanup, then verify the resulting products honor the client contract.
