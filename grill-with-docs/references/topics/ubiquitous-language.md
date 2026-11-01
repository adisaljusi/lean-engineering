# Ubiquitous language and business meaning

## Book material

**Foundation:** Eric Evans — Domain-Driven Design: Tackling Complexity in the Heart of Software. **Concept/locator:** DDD Reference named pattern: Ubiquitous Language; language within Bounded Context. [Source / locator](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf). **Evidence basis:** `author-reference`.

A shared domain language connects conversation and the model within its context. Ambiguous terms hide conflicting rules; refining language should change concrete examples/behavior rather than add jargon.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when a feature word such as automatic, approved, effective or rate has competing interpretations. Inspect domain docs, tests/code and already accepted stakeholder decisions first.

## Apply the idea

1. Identify the ambiguous term and the immediate decision that its meaning changes.
2. Use a concrete example/counterexample to distinguish interpretations.
3. Record the accepted meaning with its owner/source and update affected examples/contracts.
4. Carry that meaning across handoffs; do not ask again under another skill name.

## Worked application

“Automatic commission update” could mean creating a pending candidate or publishing a new effective term. Ask whether a later unsigned 14% draft may replace signed 13% wording. Once the owner answers proposal-only, the accepted word “automatic” must not silently turn into publication during design or implementation.

## Trade-offs and simpler choice

An exhaustive glossary/questionnaire can obscure the real decision. A short precise sentence and example suffice for a small feature; an agreed typo needs no language workshop.

## Verify the decision

Check that requirements, examples, fields, transitions and final behavior use the same accepted meaning. Conflicting stakeholder wishes remain unresolved rather than becoming technical defaults.
