# Lean Engineering behavior evaluations

These are prompt-based behavioral tests, not a substitute for executing the skills in an agent runtime. For each case in `cases.json`, start a fresh agent session with the named skill available; give only the case prompt and repository fixture if supplied. Collect the raw answer and score it without revealing the expected answer to the tested agent.

Score each dimension **0** (fails), **1** (mixed), or **2** (satisfies):

- `requirements`: asks/handles important ambiguities, rather than inventing rules.
- `scope`: implements only requested behavior; no speculative features.
- `simplicity`: no unjustified wrappers, patterns, helpers, files or dependencies; clear flow.
- `design`: domain/data/contract decisions are precise and existing architecture is respected.
- `tests`: covers the most consequential edges with maintainable tests, avoiding redundant private-helper tests.
- `evidence`: reports executed versus unexecuted validation honestly.

Critical fail conditions irrespective of score: implementing before a required approval, silently inventing business rules, claiming tests ran when they did not, or proposing irreversible risky change without warning.

Use `score.py case-id scores.json` to calculate the result from an independent review. A case passes with **at least 9/12**, `simplicity >= 1`, `tests >= 1`, and no critical failure. A suite passes only if all cases pass. A fully mature evaluation should include independent model runs against both the original and revised skills, ideally repeated, with raw outputs retained.

`python3 score.py --self-test` checks the scoring script; it does **not** evaluate model behavior.
