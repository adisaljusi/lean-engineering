# Lean Engineering behavior evaluations

For conversational, action-based evaluations inspired by Superpowers, start with
[`WORKFLOWS.md`](WORKFLOWS.md) and `conversations.py`. It adds three workflows with
native persistent subject sessions, an adaptive stakeholder, private independent
assessment and real repository checks. The cases below remain the smaller smoke
suite; adding prompts alone is not a substitute for workflow evaluation.

`score.py` validates independently supplied scores; its self-test **does not run an
AI agent**. `runner.py` runs paired, fresh Codex CLI sessions and retains evidence.
The fourteen tasks come from `cases.json`. Only `prompt` and the public fixture reach
the tested agent. `expect`, `trap`, the rubric, held-out checks and sibling results
are absent from its filesystem. Treatment appends the exact relevant `SKILL.md`;
baseline receives the same task/context without skill instructions.

## Skill coverage

| Skill | Cases |
|---|---|
| `grill-with-docs` | `discovery-commission-change` |
| `requirements-engineering` | `requirements-commission-proposals`, `requirements-conflicting-stakeholders` |
| `behavior-specification` | `acceptance-commission-publication` |
| `lean-engineer` | `routing-ambiguous-business-feature`, `routing-small-approved-fix` |
| `solution-architecture` | `deepagent-multidoc-architecture` |
| `technical-design` | `treaty-addendum`, `deepagent-multidoc-technical-design` |
| `implementation-planning` | `small-validation`, `deepagent-multidoc-delivery` |
| `test-driven-development` | `duplicate-webhook` |
| `code-review` | `review-overfactored` |
| `evidence-verification` | `verification-honesty` |

The business scenarios use stakeholder notes, accepted decisions, or an approved
specification as appropriate to the phase. They assess source use, missing or
contradictory rules, role/tenant permissions, rate and effective-date semantics,
preserved history/evidence, verifiable requirements, concrete acceptance examples,
and proportionate workflow selection. The judge receives both original fixture
files and final artifacts so rewriting the source cannot conceal a changed rule.

These are single-turn evaluations: discovery tests a useful first question round,
not a completed interview. They do not demonstrate adaptation to stakeholder
answers, convergence over multiple rounds, or an end-to-end approval lifecycle.
Those require the separate conversation path described in `WORKFLOWS.md`, which
uses the same stakeholder policy and facts for both variants and retains their
adaptive exchanges. No conversational evaluation has been executed here.

## Run

Requirements: Python 3.10+, Codex CLI supporting the flags shown by
`codex exec --help` (developed against 0.163.0), a working login or `OPENAI_API_KEY`,
model-network access, and Linux with bubblewrap (`bwrap`) and user/PID namespaces
permitted. No Python packages are needed. Authentication uses the existing auth
file as a read-only mount or the API key environment variable; secrets are not
copied into results. No configuration or credentials are invented by the runner.
The official default provider is used; arbitrary gateway/provider configs are not
supported by this minimal runner. Keep the inherited session proxy and CA trust.

First choose a model ID that your environment actually supports, then run a pilot:

```sh
export EVAL_MODEL='your-supported-model-id'
python3 evals/runner.py --model "$EVAL_MODEL" --judge-model "$EVAL_MODEL" \
  --cases review-overfactored --pilot review-overfactored \
  --output work/evals-pilot
```

Only proceed to the full suite after inspecting the pilot's raw artifacts,
checks and independent judgment. The suite also runs its pilot first and blocks
subsequent live calls if the pilot execution or configured judge fails:

```sh
python3 evals/runner.py --model "$EVAL_MODEL" --judge-model "$EVAL_MODEL" \
  --repeats 3 --seed 0 --output work/evals-suite
```

Use `--cases` for a subset, including the `--pilot` case. The default pilot is
`review-overfactored`. Repeats and randomized pair order reduce order effects;
they do not make a stochastic model deterministic. Both variants use an explicit
identical model ID, medium reasoning effort, the same CLI configuration, timeout,
fixture bytes and tool availability. Each runs in a separate mount/PID namespace,
with fresh workspace, runtime, temporary directory and ephemeral Codex session.
The host repository, home, rules, installed Lean skills and previous answers are
not mounted. Apps, web search and multi-agent tools are disabled for both variants.
No unsafe sandbox bypass flags are used. The judge runs separately, with a
read-only empty workspace and a blind artifact bundle; labels and skill prompts
are withheld. The same model ID in a **new independent session** is supported;
a different judge model can be supplied with `--judge-model`.

For the business requirements subset, use discovery as its pilot:

```sh
python3 evals/runner.py --model "$EVAL_MODEL" --judge-model "$EVAL_MODEL" \
  --pilot discovery-commission-change \
  --cases discovery-commission-change requirements-commission-proposals \
    requirements-conflicting-stakeholders acceptance-commission-publication \
    routing-ambiguous-business-feature routing-small-approved-fix \
  --output work/evals-business
```

`--prepare-only` creates paired inputs and records every result as not executed.
It does not call a model. Missing CLI/isolation support likewise records blocked
cases instead of silently weakening isolation. Fresh output paths are required;
previous raw evidence is never overwritten. Exit 0 means preparation completed,
or all requested judgments completed. Exit 2 means evaluation is incomplete;
it is **not** a behavioral score. `suite_passed` separately applies the legacy
rubric gate to each variant, or is null if judgment is incomplete.

## Evidence and scoring

Each variant retains `prompt.txt`, original fixture files and hashes, final files
and hashes, changed/deleted file paths, `answer.txt`, raw JSONL events, stderr,
execution status, test commands/results, model settings and the skill hash.
`capabilities.json` records actual local probes. `comparison.json` records source,
runner, case and rubric identities, UTC start time, pair order, judgments, score
differences and suite outcomes. `report.md` renders all requested comparison
metrics with evidence paths. Files/counts/LOC are never converted into quality
scores. Results are exploratory unless repeat coverage justifies stronger claims.

Deterministic checks for `duplicate-webhook` run generated tests and eight held-out
SQLite checks **after generation**: retry uniqueness, separate events, conflicting
payloads, database enforcement, rollback/recovery, concurrent connections, and
safe upgrade of legacy duplicates. These establish only the local database
contract, not PostgreSQL, HTTP integration or a production rollout. The checks are
validated by a known-buggy fixture and a correct reference control in harness
tests. Controls and stub model responses are **not behavioral evaluations**.

Other tasks request plans, designs, reviews or verification judgments. Their
nonempty-output/file-mutation checks establish artifact availability only;
semantic correctness requires an independent judge. The Deep Agents fixture has
three synthetic immutable OCR pages with stable span IDs, explicit offset/box
units and conflicting source text. It is design context, not a tested OCR or
extraction pipeline. Difficult tasks may legitimately need substantial complexity.

The judge uses `rubric.md` and a strict JSON response schema, with evidence-backed
0/1/2 scores and reasons for requirements, scope, design, simplicity, testing,
evidence and **maintainability**. The requested six metrics are rendered in the
report; scope remains in JSON for compatibility. Maintainability is an additional
reported dimension, not silently inserted into the original 12-point score.
The existing `score.evaluate` gate is reused: at least 9/12, simplicity >= 1,
tests >= 1, and no critical failure. Critical failures include unauthorized coding,
invented material rules, false execution claims and unflagged irreversible risk.
For noncoding tasks, testing quality means an appropriate proposed verification
strategy. A plan is never credited as executed code. Missing/failed/invalid
judgments remain unscored, not zero or pass. Judge errors and bias remain possible;
inspect the raw evidence and calibrate with human review before making claims.

For manual independent review, retain the reviewer's identity and evidence and
supply the original six dimensions plus `critical_failure` to:

```sh
python3 evals/score.py CASE_ID scores.json
```

This command validates supplied scores only. Do not replace blocked independent
judging with the generating agent grading its own output.

## Checks

```sh
python3 evals/score.py --self-test
python3 -m unittest discover -s evals/tests -v
python3 -m compileall -q evals
```

The harness tests cover leakage protection, fresh paired inputs, pilot gating,
raw preservation, invalid judgments, process timeout, fixture evidence integrity,
checker controls and the isolation command. The live filesystem isolation test
is skipped with a concrete reason when namespaces are unsupported. Live Codex
and judge execution still need a successful pilot; mocks do not prove them.

See `REPORT.md` and `results/` for this environment's actual outcomes and limits.

## Operational-guidance redesign (2026-10-30)

The revised collection is behaviorally unvalidated. Historical results above and
in REPORT.md are preserved; they are not evidence of improvement. There are now
21 smoke definitions: 20 development cases plus one author-visible reserved
holdout (`holdout-device-conflicts`). Default runs exclude `holdout: true`;
explicitly select it with `--cases` and `--pilot` only after freezing instructions
and criteria. One small reserved case is not a statistically representative or
blind holdout; do not claim it is. Keep future unseen cases with an independent
owner before a confirmatory campaign.

Added contrasting cases cover actual authorized typo implementation, a refund
feature with all answers in README, a modest clinic monolith, independently owned
distributed settlement with durable recovery needs, strict-client API evolution
and a 50-million-row snapshot export. These exercise constraints and reasoning,
not a required topology. Original multi-document cases remain. New implementation
oracles have per-case expected counts (2 and 3), alongside the existing 8-check
oracles. Counts validate completeness of a known checker, never engineering
quality or subject test quantity.

Treatment in the smoke runner still explicitly receives its selected SKILL.md;
it now also receives that skill's complete directory under `.agents/skills`.
Its prompt identifies the installed reference root. The intervention and hashes
are retained separately from application artifacts. This is an instructed
application experiment, not native skill discovery. Native discovery remains
the workflow runner's intervention. Both run in fresh isolated workspaces with
no source checkout mounted.

The legacy six-dimension 9/12 score remains for historical comparison. New verdicts
also require nonzero requirements, design and maintainability. Independent
required-check failures force fail even with a favorable judge. Empty, skipped,
missing, wrong-count, timeout and crashed required checks cannot pass. Known
concrete failures remain recorded even if other evidence is incomplete.
`--prepare-only` now exits 2, as does an indeterminate evaluation; exit 1 is a
completed failed evaluation, exit 0 a completed passing evaluation. This changes
the old preparation-success exit convention. Do not compare new verdicts against
historical legacy-only verdicts without identifying the policy change.

The rubric now assesses unnecessary questioning/reapproval, existing answers,
justified complexity, practical Python and diagram/contract consistency. A judge
can still be wrong: independently review pilot evidence and calibrate more than
one plausible architecture before a repeated campaign. Do not alter scores or
isolation to obtain a pass. Source/evidence details: `docs/REDESIGN.md` and
`results/redesign/`.
