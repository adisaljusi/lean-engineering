---
name: grill-with-docs
description: Resolve consequential unknowns in a feature or design using repository evidence and targeted stakeholder questions before committing to behavior.
---

# Discovery With Evidence

Use when an unknown affects the current product or engineering decision. Read the request, accepted decisions and relevant docs, code, contracts, schemas, tests and ADRs first. A typo with agreed behavior does not need discovery.

For each unknown, identify the decision its answer changes and the consequence of guessing. Resolve consequential authorization, privacy, security and data-loss uncertainty now when it affects the work. Defer unrelated future choices. Use an explicit reversible working assumption for low-consequence gaps; never treat it as accepted policy.

Ask the smallest useful set, without a quota. Prefer a business example: “Does automatic create a proposal or publish the rate? That determines whether human review is required.” Avoid choosing brokers before settling publication meaning. Explain why a question matters when that helps the user answer. Do not repeat questions answered in documentation or earlier turns; cite that evidence and ask only about a real contradiction.

Load [decision-led discovery](references/discovery.md) for ambiguous features, conflicting sources or changing decisions. It provides a procedure and worked exchange.

Record known facts with sources, accepted decisions, explicit assumptions and unresolved issues in the existing feature notes or conversation. Update them after corrections. Return the immediate decision, targeted questions (if any), and useful candidate observable examples. Continue independent authorized work while awaiting an answer; do not implement behavior dependent on an unresolved consequential rule. Do not demand a new interview, spec or approval because discovery ended.
