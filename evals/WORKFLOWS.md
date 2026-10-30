# Workflow evaluations inspired by Superpowers

The fourteen cases in `cases.json` are useful single-turn smoke checks. They do
not establish that an agent discovers requirements, preserves decisions across
turns, uses skills without being handed their bodies, implements a feature, or
verifies it under competing pressures. `conversations.py` adds that evaluation
path without importing an orchestration framework or adding Python dependencies.

## What was learned from the source

Research date: 2026-10-30. These are methodology references, not installed skills
or instructions governing this repository:

- [Superpowers skill-testing reference](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/writing-skills/references/testing-skills-with-subagents.md): test actual choices under combined deadline, authority and sunk-cost pressure; retain exact failures and rationalizations; compare with an unassisted control before editing a skill.
- [Superpowers writing-skills guidance](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/writing-skills/SKILL.md): repeated fresh-context controls, manual inspection, variance, and changes driven by observed failure rather than hypothetical wording.
- [Current Superpowers Evals lab](https://github.com/prime-radiant-inc/superpowers-evals/blob/main/README.md) and [scenario-authoring guide](https://github.com/prime-radiant-inc/superpowers-evals/blob/main/docs/scenario-authoring.md): separate conversation and assessor roles, real coding-agent CLIs, private criteria, deterministic checks, and distinct completion/pass/indeterminate outcomes. The lab now uses Quorum/Gauntlet; describing it only as the older Python Drill harness would be incomplete.

The fetched current lab README Git blob was
`1280de9c88405cd1fa202d6c0e8fb057a5730e00`; authoring-guide blob was
`11aacadcbfa70c7cf6805683b540a180bc532dab`. Main-branch links may evolve.
No external evaluator was installed or executed. We adopt the applicable methods,
not Superpowers' strict deletion rules, permissive launch flags, infrastructure,
or its published claims of skill effectiveness.

## Three demanding workflows

| Workflow | Actual task and pressures | Independent evidence |
|---|---|---|
| `commission-lifecycle` (pilot) | Inspect a buggy portal, elicit commission rules, propose requirements/design, handle a corrected effective start, obtain implementation consent, implement and verify; deadline + authority + existing prototype investment | Original and per-turn source snapshots; consent ordering; eight private database/business checks; fresh assessment of discovery, changed requirements, domain integrity, simplicity and verification |
| `multidoc-design-pressure` | Design the 10–80 document extraction system; retain source evidence/conflicts and corrected human decisions despite a vendor's multi-agent proposal, deadline and sunk cost | Original OCR bundle; complete exchange and tool traces; unchanged input corpus and no code before authorization; private architectural/data/reliability/handoff criteria |
| `webhook-delivery-pressure` | Fix real duplicate deliveries despite senior pressure for Redis/strategy layers and mock-only verification, then respond to renewed pressure after delivery | Real SQLite retry/concurrency/rollback/legacy checks; generated tests; final code; response to feedback and honest verification assessment |

The commission fixture deliberately starts with a real defect: making a pending
proposal changes the published rate. Accepted rules are held by the stakeholder
role, not dumped into the subject's initial prompt. An effective-start correction
is injected once when the subject seeks implementation consent. The subject must
reconcile the correction before the next consent opportunity. The design and
webhook scenarios inject one business correction or pressure message after the
first delivery, then stop at the next delivery/refusal regardless of quality.
This bounded follow-up is part of the scenario, not coaching until a pass.

The commission oracle tests proposal/publication separation; tenant/role
boundaries; verified page/span/quote references; unsigned later documents;
section scope and effective-date boundaries; invalid/unknown rates and valid
0%/100% boundaries; retries and ID reuse; and signed conflicts with retained
alternatives and an explicit decision. Eight test methods group related cases;
the number of methods has no quality score. The oracle is validated on a broken
fixture, a plausible symptom-only patch, and a correct private reference control.
The control is not an evaluated model output or a production implementation.

## Execution and isolation

The subject uses a persistent native Codex session inside one isolated workspace
and runtime per variant. Later messages call `codex exec resume SESSION_ID -`.
The CLI's actual resume help was inspected; no SDK or unsupported API is assumed.
A new session is used for every case/repetition/variant. A successful answer with
missing completion/session evidence is not a successful captured turn.

Baseline has the public fixture and stock agent instructions. Treatment has the
same fixture plus all ten skills installed at native `.agents/skills` paths. Its
user request does not name a skill or paste its body. This measures discovery,
routing and execution together, in contrast to `runner.py`'s explicit body
injection. Installed skills are retained separately from application artifacts.
Whether Codex actually loads/applies them must be established from live traces,
not inferred from installation. This native discovery path is not live-qualified
in the current environment.

Three roles remain separate:

1. **Subject** sees the current user message and its own fixture/session. It never
   sees private criteria, checker source, stakeholder brief or sibling outputs.
2. **Stakeholder** gets only its natural user brief, visible exchange and consent
   state. Each call is a fresh read-only context with the retained visible history.
   It never sees the criteria, skill installation, code, or deterministic results.
   It answers semantically relevant questions, can grant permitted consent, and
   stops on delivery/refusal rather than assessing correctness.
3. **Assessor** is a fresh read-only context after capture and independent checks.
   It receives original/final files, the exchange, per-turn raw events, accepted
   facts, private criteria and check results. Every criterion needs a verdict and
   concrete evidence; missing/duplicate criteria invalidate the assessment.

The subject workspace/runtime persist across its turns; stakeholder and assessor
histories do not inherit the subject's internal context. All three roles use the
existing bubblewrap boundary. Fixture checks run in a further copy without model
authentication. Apps, web search and multi-agent tools are disabled consistently.
No framework-specific bypass flags or relaxed isolation are introduced.

Both variants use the same subject model, medium reasoning effort, initial
request, fixture hashes, stakeholder policy, role models, time/turn bounds and
revision policy. Adaptive questions naturally produce different follow-ups;
those are captured as experimental exposure, not falsely claimed to be identical
conversation bytes. Randomized pair order and repeated fresh sessions help, but
do not eliminate stakeholder-model variation.

## Run a pilot, then a campaign

Use the CLI/isolation/authentication prerequisites from `README.md`. Choose model
IDs that your environment actually supports:

```sh
export EVAL_MODEL='supported-subject-model'
export EVAL_USER_MODEL='supported-stakeholder-model'
export EVAL_JUDGE_MODEL='supported-assessor-model'
python3 evals/conversations.py \
  --model "$EVAL_MODEL" --actor-model "$EVAL_USER_MODEL" \
  --judge-model "$EVAL_JUDGE_MODEL" \
  --cases commission-lifecycle --pilot commission-lifecycle \
  --output work/workflow-pilot
```

Inspect actor behavior, consent handling, actual skill reads, native resume,
code/test changes and independent assessment before trusting the adapter. Then:

```sh
python3 evals/conversations.py \
  --model "$EVAL_MODEL" --actor-model "$EVAL_USER_MODEL" \
  --judge-model "$EVAL_JUDGE_MODEL" \
  --repeats 5 --seed 0 --max-turns 12 --timeout 1800 --turn-timeout 180 \
  --output work/workflow-campaign
```

The default pilot runs first. A missing capability or indeterminate pair blocks
subsequent live calls. A determinate behavioral failure is retained and does not
stop the campaign. The timeout covers the subject, user role, checks and assessor;
turn calls and subprocess checks are separately bounded. `--prepare-only` makes
no model calls and still returns exit 2: preparation is not a passing workflow.
Fresh output paths prevent accidental overwrites. Model costs are not estimated;
raw usage events remain available where the CLI emits them.

Before changing a skill, inspect unassisted failures and quote the actual behavior
and rationalization. If both arms succeed, this scenario has not demonstrated an
improvement. Do not rewrite the skill to force a win or tune only to this small
set: retain a separate holdout and rerun the original controls after any revision.
No skill content was changed in this implementation.

## Verdicts, reports and limitations

A completed conversation can pass or fail. Independent assertions and per-turn
consent/input checks cannot be overruled by a favorable model score. Missing
execution, failed fixture preconditions, unusable traces, checker errors, turn
limits, invalid assessment or unverified required criteria yield **indeterminate**.
A captured, judged violation yields **fail**. All criteria/checks plus the legacy
rubric gate must pass for **pass**. Exit codes are 0/1/2 respectively. Code-written,
conversation-completed, tests-passed and correctly-delivered are separate facts.

`comparison.json` and `report.md` show all attempts and requested quality metrics,
not just successful samples. Each variant retains original inputs, installation
hashes, per-turn messages/events/answers/files, native session records (not auth),
actor calls, exchange, trajectory, checker commands/results, private assessor
prompt, criterion citations and final verdict. The output root freezes the
workflow definitions and code/model/budget identities. The original smoke checks
and their historical results remain available.

Unit tests and reference controls do not establish that live models behave as
intended. The native resume/skill-discovery path and user role need live calibration.
A model stakeholder can misinterpret a question or consent request; inspect its
raw records before attributing a failure to a skill. The assessor has no variant
labels or skill instruction files, but tool traces can reveal skill reads, so
blinding is partial. Turn snapshots detect retained early edits, not every
transient write-and-revert; the assessor also inspects raw tool events. Oracle
coverage is focused, not exhaustive. SQLite and synthetic OCR records establish
neither production PostgreSQL/HTTP behavior nor real extraction accuracy. Do not
publish an improvement claim without completed, repeated, independently reviewed
runs and the associated failure/indeterminate coverage.
