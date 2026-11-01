# Transaction Script for straightforward operations

## Book material

**Foundation:** Martin Fowler (with contributors) — Patterns of Enterprise Application Architecture. **Concept/locator:** Named pattern: Transaction Script (author catalog identifies Chapter 09). [Source / locator](https://martinfowler.com/eaaCatalog/transactionScript.html). **Evidence basis:** `author-pattern-summary`.

A Transaction Script organizes an application operation as a procedure coordinating its validations/calculations and persistence. It is a legitimate business-logic organization for sufficiently straightforward behavior.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use for cohesive operations with limited interacting rules. Inspect rule duplication, transaction boundaries, existing function/service owners and expected changes.

## Apply the idea

1. Describe the operation’s input, policy checks, atomic effects and output.
2. Keep the flow readable in an owning function, extracting only coherent reused responsibilities.
3. Use existing transaction/persistence facilities and separate transport conversion when valuable.
4. Reconsider a richer model if rule interactions/duplication make the script hard to maintain.

## Worked application

Refund eligibility with captured_on and a fixed accepted calendar interval is a function, not a factory/strategy hierarchy. A publication operation may coordinate authorization, revision and SQL in one clear transaction owner while sharing a precise Rate value.

## Trade-offs and simpler choice

Scripts can duplicate complex rules across operations; a rich domain model can centralize them but costs mapping/lifecycle complexity. Do not add domain objects simply because the feature has a business name.

## Verify the decision

Test observable inputs/results and persisted invariants. Review whether changes remain localized and policy is duplicated across scripts.
