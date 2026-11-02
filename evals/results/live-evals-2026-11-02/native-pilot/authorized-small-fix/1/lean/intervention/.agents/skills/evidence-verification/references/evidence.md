# Evidence and release confidence

Use when someone needs to know what behavior has actually been demonstrated. Inputs: request, accepted rules, diff, environment, check commands/results and original evidence. Do not require new spec/design/plan files.

1. Identify consequential changed behavior and affected boundaries.
2. Select the smallest meaningful checks: domain, real database/API integration, compatibility, critical workflow or operational recovery as relevant.
3. Execute feasible checks and retain command/environment/outcome. Inspect discovery counts and skipped/missing/crashed checks.
4. Assign Verified, Failed or Not verified to behaviors, not simply to the feature as a whole.
5. Explain residual risk and the next useful check. Remedy failures when fixes are already authorized; verification-only scope does not authorize implementation.

Worked result: unit rate validation passed; real SQLite transaction/retry tests passed; PostgreSQL migration/integration skipped because no supported server; no production HTTP check. Rate validation and local transaction semantics are verified in that environment. PostgreSQL and deployment remain not verified. A passing unit suite cannot override a concrete integration failure. A design-only answer can be reviewed for contract/diagram consistency without claiming execution.

A compact requirement → check → evidence → status mapping helps complicated handoffs; a paragraph suffices for one behavior. Record actual process exit and test counts: zero tests, skipped tests, empty output or a crash are not successful behavioral verification. A reference control passing establishes something about the checker, not a model's behavior. Prepared model prompts and successful harness tests do not establish skill effectiveness.

Prefer existing CI artifacts over rerunning expensive suites without a changed reason. Do not infer production reliability from a synthetic corpus or local database. Further foundations: Python unittest result semantics https://docs.python.org/3/library/unittest.html and repository-specific integration documentation; choose evidence according to the actual contract.
