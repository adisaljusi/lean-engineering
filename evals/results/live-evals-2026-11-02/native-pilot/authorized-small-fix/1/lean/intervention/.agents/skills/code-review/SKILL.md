---
name: code-review
description: Review the actual change for behavioral correctness, maintainability, security, compatibility and justified complexity using concrete evidence.
---

# Engineering Code Review

Inspect the diff and affected callers, contracts, schema, tests and accepted decisions. Use review-only scope when requested; authorization to implement or fix also permits ordinary remedies. Do not invent missing spec/design documents as a review prerequisite.

First establish changed behavior and invariants: permissions, data semantics, transactions, compatibility and likely failure paths. Then inspect cohesion, dependency direction, errors/resources/concurrency, operability and whether humans can understand and change the flow. Verify claims against actual code and execution evidence.

Load [review decisions](references/review.md) for a concrete procedure and examples of excessive versus justified complexity.

For each significant abstraction ask what responsibility, invariant or operational constraint it owns. Suggest inlining a wrapper that forwards unchanged calls without policy; preserve boundaries that isolate business rules or partial failure. Pattern names, test counts, line counts and fewer files are not evidence of quality.

Return actionable findings with location, trigger, consequence, evidence and remedy. Separate demonstrated defects, uncertain risks requiring verification and optional improvements. Prioritize consequential problems; avoid style-only tooling changes and speculative rewrites. A favorable overall impression cannot erase a concrete correctness or security defect. Report scope/verification limits and do not claim tests ran unless supported by actual results.
