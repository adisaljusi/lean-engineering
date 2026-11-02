# D. Investigation and remedy

**Start with:** expected versus actual behavior, authorization, available logs/reproduction and the affected system. During an incident, use authorized reversible mitigation to reduce impact while preserving evidence; label mitigation separately from a demonstrated cause.

1. Reproduce or characterize the symptom with a concrete request, data, command, version and environment. Read the complete relevant error and recent changes. Never dump secrets or whole sensitive payloads as diagnostic evidence.
2. Trace the failing path and compare the nearest working case. Observe input/output and state at the boundary where behavior diverges, with safe identifiers and targeted instrumentation. Distinguish business-rule, code, configuration, external service and environment hypotheses.
3. State a falsifiable hypothesis and the smallest check that distinguishes it from another credible cause. Change one relevant variable where feasible. If the check does not support it, retain the result and revise the hypothesis; do not stack guessed fixes.
4. When the cause is supported, add/reuse a regression at a stable boundary and implement the proportionate remedy if authorized. A diagnosis-only request ends with cause/evidence/remedy recommendation. Do not rewrite unrelated architecture to cure a local symptom.
5. Verify the original symptom and consequential nearby behavior/recovery. If reproduction is unavailable or intermittent, state what is known, what remains uncertain and the next discriminating observation. A timeout/error message alone does not prove which component caused it.

**Useful finish:** the symptom is connected to evidence and a checked remedy, or an honest bounded diagnosis/next experiment. Repeated disconfirming results justify revisiting assumptions, not an arbitrary attempt quota or automatic architecture rewrite.

**Example:** duplicate webhook rows may reflect a retry, a race or legacy data. Sequential retries passing does not rule out races. Two independent connections and a uniqueness/transaction inspection distinguish them. Retrying in Redis would hide rather than establish the database cause if the same invariant still races.
