# API governance as explicit decision ownership

## Book material

**Foundation:** Mehdi Medjaoui, Erik Wilde, Ronnie Mitra and Mike Amundsen — Continuous API Management, first edition (2018). **Concept/locator:** First edition, Chapter 2: API Governance — governing decisions; centralization/decentralization; governance patterns. [Source / locator](https://www.oreilly.com/library/view/continuous-api-management/9781492043546/). **Evidence basis:** `publisher-toc`.

API governance concerns how decisions are made across an API landscape. Centralized, automated and collaborative approaches have different costs; governance is not equivalent to approval meetings for every change.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when cross-team standards/compatibility decisions repeatedly diverge. Inspect actual consumers, ownership, decision scope, enforceable constraints and current review/automation.

## Apply the idea

1. Identify which decisions require consistency across teams and which can remain local.
2. Assign accountable owners and a lightweight way to resolve exceptions/conflicts.
3. Automate objective contract/style compatibility checks where useful, while leaving business meaning to responsible people.
4. Review whether the process reduces actual integration risk without blocking ordinary local work.

## Worked application

Two shipping teams repeatedly disagree on units and deprecation guarantees. A shared precise-unit/compatibility policy and consumer contract check can prevent breakage. Requiring an architecture board to approve each validation message does not address that cross-team problem.

## Trade-offs and simpler choice

Central rules can bottleneck teams; unconstrained local choices can fragment consumer experience. Existing repository conventions plus explicit exception ownership may be sufficient.

## Verify the decision

Trace a representative change/exception through the decision owners and checks; verify consumer risk is addressed and no approval is invented beyond the actual policy.
