# Strategy and replaceable policy

## Book material

**Foundation:** Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides — Design Patterns: Elements of Reusable Object-Oriented Software. **Concept/locator:** Named GoF pattern: Strategy; exact chapter/page not retrieved. [Source / locator](https://www.oreilly.com/library/view/design-patterns-elements/0201633612/). **Evidence basis:** `book-synthesis`.

Strategy represents interchangeable ways to perform a behavior behind a common contract. Its benefit is meaningful policy substitution, not adding a hierarchy to one fixed operation.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when several current policies must vary independently from the caller. Inspect the variants, shared contract, state/lifecycle and whether a callable already expresses the boundary.

## Apply the idea

1. Name the actual interchangeable behavior and the invariants each variant must honor.
2. Keep selection/composition separate from the caller’s core operation.
3. Use a callable or small protocol when sufficient; introduce stateful classes only for real state/lifecycle.
4. Do not add hypothetical strategies before a second legitimate policy or boundary exists.

## Worked application

Accepted normalization may use one of two explicitly supported jurisdiction vocabularies. A normalizer callable with version identity can supply that policy while preserving raw evidence. Different broker vendors or one enum validation do not automatically require a StrategyFactory hierarchy.

## Trade-offs and simpler choice

Interchangeability can obscure divergent semantics if the contract is too broad. One explicit function/branch is simpler for a fixed or small local choice.

## Verify the decision

Run the same contract examples for every supported variant, including unknown/conflicting input, and verify selection does not change accepted business authority.
