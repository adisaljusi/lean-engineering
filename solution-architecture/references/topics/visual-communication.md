# Architecture views, audience and visual communication

## Book material

**Foundation:** Jacqui Read — Communication Patterns: A Guide for Developers and Architects (2023). **Concept/locator:** Chapters 1–6: visual communication; Chapter 10: Knowledge Management Principles; Chapter 12: Effective Practices. [Source / locator](https://www.oreilly.com/library/view/communication-patterns/9781098140533/). **Evidence basis:** `publisher-toc`.

Diagrams communicate to particular audiences. Consistent abstraction, clear relationships, accessible labels and a coherent narrative matter more than using an impressive notation or putting every detail into one picture.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when relationships, timing or provenance are hard to understand in prose. Inspect the audience’s question, current/proposed facts, contracts and available rendering tools.

## Apply the idea

1. Choose a view for the question: context, deployment, dependency, sequence, data flow, state or ER—not all views by default.
2. Keep a coherent abstraction level and label current/proposed scope, owners and important relationships.
3. Walk a concrete success/failure example through the source and surrounding contract; use labels/legend instead of color alone.
4. Parse/render with available tools and inspect readability; report unrendered output honestly.

## Worked application

An underwriter needs evidence and adjudication flow, not a Kubernetes diagram. A data-flow view separates immutable OCR from candidate alternatives and mutable decisions. An implementer investigating stale review needs a sequence view showing revision check, transaction and failure response.

## Trade-offs and simpler choice

A crowded all-in-one diagram obscures the decision. A short paragraph or a single focused view is simpler for a local fix; additional notation adds a learning cost.

## Verify the decision

Ask whether the intended reader can trace the concrete example, identify authority/failure behavior and match it to prose/schema. Syntax success alone does not prove that.

## Further detail

C4 view definitions are from Simon Brown’s C4 model, not attributed to Jacqui Read as its originator. Editable examples/render limits remain in this skill’s visuals guide.
