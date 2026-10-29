---
name: code-review
description: Review changes on two independent axes, specification compliance and engineering quality, including layering, SOLID, domain invariants, security, test coverage and unnecessary complexity.
---

# Engineering Code Review

Review the actual diff and relevant surrounding code, not the author's claims. First review **specification compliance**: link `R*/AC*` to changes, detect missing behaviors, invalid assumptions, compatibility regressions and inadequate tests. Then review **engineering quality** separately: cohesion, naming, complexity, dependency direction, boundaries, model correctness, data safety, security, concurrency, resource handling and observability.

Apply repository conventions and proportionate Clean Code/SOLID principles, not arbitrary style preferences. Identify unjustified architectural complexity and missing failure-path coverage. Give actionable findings with file/line locations, severity, reproducible evidence and recommended remedy. Distinguish bugs from optional improvements. Do not mutate code during review-only requests. Critical correctness/security findings block completion.

Perform a **simplification pass**: for each added file, class, wrapper, helper, interface, configuration option or dependency, ask what would break if it were removed or inlined. Flag needless indirection, speculative extension points, micro-functions that obscure flow, repeated error handling and tests coupled to implementation details. Do not reward fewer lines blindly: retain decomposition that expresses real boundaries, domain invariants or test seams. Report the simplest viable alternative and rough change footprint when complexity seems unjustified.
