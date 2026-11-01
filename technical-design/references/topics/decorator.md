# Decorator and composable behavior

## Book material

**Foundation:** Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides — Design Patterns: Elements of Reusable Object-Oriented Software. **Concept/locator:** Named GoF pattern: Decorator; exact chapter/page not retrieved. [Source / locator](https://www.oreilly.com/library/view/design-patterns-elements/0201633612/). **Evidence basis:** `book-synthesis`.

Decorator adds responsibilities around an object through a compatible interface. Layered wrappers are useful only when the added behavior and composition order have an understandable contract.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use for genuinely reusable surrounding behavior. Inspect error handling, context/resource ownership, side effects and whether ordering changes semantics.

## Apply the idea

1. Name the responsibility being added and the contract it preserves.
2. Make composition/order explicit, especially for retries, transactions, logging and authorization.
3. Keep domain decisions in their owner rather than hide them inside generic wrappers.
4. Use a direct context manager/function or existing middleware when that makes the flow clearer.

## Worked application

A timing wrapper can measure a gateway call, but a retry wrapper around publication can duplicate effects if identity/transaction semantics are not established first. “Composable decorators” does not make an unsafe retry safe or allow authorization to move after the effect.

## Trade-offs and simpler choice

Stacked wrappers hide control/error flow and can repeat validation or retry at multiple layers. One explicit operation with a context manager is simpler when behavior is not reused.

## Verify the decision

Test the observable behavior under failure and actual wrapper order; inspect counts of external effects, not merely that each wrapper was called.
