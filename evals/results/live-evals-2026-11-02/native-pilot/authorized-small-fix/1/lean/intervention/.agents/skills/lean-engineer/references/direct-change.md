# A. Direct change

**Start with:** agreed behavior, implementation authorization and a bounded owner. If meaning is disputed, use B only for that dispute; if cause is unknown, use D.

1. Read the request/accepted correction and owning code, caller/contract and regression. Confirm the intended text/data/behavior from available evidence. Check local tooling and existing changes before editing.
2. Reproduce the relevant defect. An existing failing test can supply the regression. For a low-impact text/config edit use its existing check or direct comparison rather than invent a test framework.
3. Change the owning code and necessary regression. Keep API/data semantics stable unless the accepted task changes them. Introduce a boundary only for a current responsibility/invariant.
4. Run the focused check and relevant regressions. If they fail, inspect why: code defect → remedy and rerun; wrong expected business result → surface the actual decision; unavailable dependency → report that boundary unverified and complete independent work.
5. Review the diff against the requested scope and report implemented behavior, exact check outcomes and limits. Continue ordinary authorized fixes without asking again. Publishing/deploying follows the user's actual authorization, not this playbook's ending.

**Useful finish:** the agreed result is in the owning code and demonstrated at the affected boundary, or an explicit blocker/limit is recorded. A green unrelated test or changed file alone does not establish the behavior.

**Short example:** a handler returns `Curency is invalid`; the agreed response is `Currency is invalid`. Read the handler/response contract, change the literal, update/use the response regression and run it. A design document and a stakeholder interview decide nothing here.
