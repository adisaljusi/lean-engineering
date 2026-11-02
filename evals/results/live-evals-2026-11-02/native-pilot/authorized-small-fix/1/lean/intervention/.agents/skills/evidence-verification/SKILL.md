---
name: evidence-verification
description: Verify requested engineering behavior with executed checks and inspectable evidence; distinguish implemented, failed and unverified boundaries.
---

# Evidence Verification

Inspect the request, accepted behavior, relevant source/contracts, available tests and CI/runtime evidence. Use existing artifacts; do not require spec.md, design.md or plan.md when they add no value.

Choose checks by the changed contract and consequence of failure. Execute feasible targeted/regression checks and record command, environment, result and scope. For data boundaries check database constraints and rollback; for compatibility check old/new consumers; for distributed changes check duplicates, timeouts and recovery when affected. Unit mocks alone prove neither integration nor production behavior.

Load [evidence and limits](references/evidence.md) for a compact procedure, status examples and release reasoning.

Report Verified, Failed or Not verified for important behaviors. A skipped, empty, missing or crashed check is not Pass. Separate code written, local behavior demonstrated and operational readiness. Give residual risks and the smallest useful next check. For design-only work inspect consistency, references and proposed verification without demanding fictional execution.

If fixes are already authorized, remedy reversible failures and rerun affected checks. In a verification-only request report findings; do not expand into implementation without authorization. Do not require new consent merely because a verification phase ended. Completion claims must match the evidence, including unexecuted model evaluations and unsupported environments.
