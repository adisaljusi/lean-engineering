# Examples that expose errors

Use when prose hides a boundary or transition. Inputs: accepted rules, concrete data, public contracts and existing coverage. Choose representative partitions rather than every combination. Assert results and persisted effects, not private method calls.

## Publication examples

- AC1 [R1]: Given published property rate 1250 bp, when a reviewer proposes 1300 for Nov 1 through Dec 1, then the proposal is pending and public value stays 1250.
- AC2 [R2]: Given that proposal, when a reviewer or another tenant's approver publishes it, then access is denied and publication/history is unchanged.
- AC3 [R3]: None and 10001 fail without mutation; 0 and 10000 are valid. These are semantic boundaries, not test quantity targets.
- AC4 [R4]: Given published 1300 during [Nov 1,Dec 1), Oct 31 and Dec 1 retain prior behavior, Nov 1/30 use 1300 and other sections are unchanged.
- AC5 [R5]: Given conflicting signed candidates, when the approver selects one with the required reason, both candidates/evidence remain inspectable and publication points to that decision. A later unsigned draft cannot silently win.
- AC6: Given review at revision 2, when adjudication advances to revision 3, publication using revision 2 fails with a stale-decision result. Use only if this concurrency policy is accepted; otherwise ask.
- AC7: Retrying identical publication has no duplicate effect; reuse of identity with different data is rejected if that is the agreed contract.

For database concurrency, use independent connections and assert final invariants. For evidence, resolve immutable version/page/span and compare exact text. Latency under load is a separate quality check with agreed workload/threshold. Link consequential rules to an example or another named verification method.

Avoid inventing expected policy, tests per private helper and mocks claiming transaction proof. A simpler existing regression suffices for a message correction. Verify by rule/risk, not scenario count. Further syntax: https://cucumber.io/docs/gherkin/reference/; syntax alone does not make an acceptance contract.
