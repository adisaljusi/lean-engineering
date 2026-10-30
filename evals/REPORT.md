# Lean Engineering evaluation report

## Operational-guidance revision (2026-10-30)

The revised skills and live adapter remain **behaviorally unvalidated**. The
original snapshot now passes all 22 harness tests including isolation, but a
bounded live pilot received model-host proxy CONNECT 403 errors and both subject
arms timed out without answers. No stakeholder/assessor calls or scores exist.
The revised harness has 28 passing tests and its Python example has six; these
are limited code/checker results, not evidence of skill effectiveness. CLI testing
reproduced a missing technical-design skill on master (invalid description YAML)
and verifies remote installation of all ten revised self-contained skills, an
individual skill with its examples/references, and the router alone. The quoted
repository `#ref` source is required for the slash-containing branch name.

See [the redesign critique and proof](../docs/REDESIGN.md) and
[retained evidence](results/redesign/). Historical reports below are preserved
with their original source IDs and limitations; several local source IDs are not
fetchable from origin. New content changes address static deficiencies requested
by the user; they are not justified by observed agent failures.

---

**Finding: undetermined.** No scenario generated a model answer, and no independent
judge ran. There is no evidence yet that Lean Engineering improves or harms
correctness, simplicity, architecture or maintainability. No scores were invented.

## Conversational workflow upgrade (2026-10-30)

The user's comparison with Superpowers exposed a methodological gap: more
single-turn prompts do not test sustained engineering behavior. The fourteen
existing cases remain smoke checks. A separate `conversations.py` path now
implements bounded conversations with a stakeholder role, a persistent native
Codex subject session, independent repository checks and a fresh assessor.

This follows the methods documented by
[Superpowers skill testing](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/writing-skills/references/testing-skills-with-subagents.md)
and the current
[Superpowers Evals authoring guide](https://github.com/prime-radiant-inc/superpowers-evals/blob/main/docs/scenario-authoring.md).
It does not install Quorum/Gauntlet or claim to have run their evaluations.
Research, design, reproducible commands and limits are in `WORKFLOWS.md`.

| Workflow | What the subject must actually do | Baseline / Lean result |
|---|---|---|
| `commission-lifecycle` | Discover business rules in a real prototype, handle a changed effective date, seek consent, implement the approved workflow and verify it | Both not executed; indeterminate |
| `multidoc-design-pressure` | Resolve domain uncertainties and deliver a source-verifiable multi-document architecture/handoff despite vendor, deadline and sunk-cost pressures | Both not executed; indeterminate |
| `webhook-delivery-pressure` | Deliver the database-backed fix and respond to senior pressure for extra layers and mock-only verification | Both not executed; indeterminate |

The treatment installs all ten skills in native project `.agents/skills` paths;
it does not receive skill bodies or names in its user request. The baseline
receives the same request and repository without those skills. The stakeholder
sees its brief and visible exchange, not private criteria or the subject's code.
A separate assessor receives immutable inputs, final/per-turn artifacts, raw
execution events, the exchange and independent check results. Every criterion
requires a verdict and evidence. Successful conversation completion is separate
from a passing grade. Independent failures cannot be overridden by a model score.

The new commission oracle checks eight grouped business/database behaviors:
pending versus published state; roles and tenants; exact source references and
quotes; unsigned later uploads; effective-date/section boundaries; invalid or
unknown rates and valid 0%/100% boundaries; retries and ID reuse; and explicit
conflict decisions retaining alternatives/evidence. A private reference control
passes all eight; the original buggy prototype and a plausible premature-
publication patch fail. These are checker controls, not model outputs.

**Actual checks:** 22 harness tests: **21 passed, one live-isolation test skipped**.
The commission fixture's existing smoke test passed. Scorer self-test, compilation
and whitespace checks passed. The native resume CLI help is available; live
resume, skill discovery and stakeholder behavior remain unqualified.

The live invocation selected the commission pilot first. The isolation probe
still failed with `bwrap: setting up uid map: Read-only file system`, so no
subject, stakeholder or assessor model was launched. All three workflows retain
six paired prepared contexts, equal original fixture/request hashes and explicit
unexecuted/unjudged status. The runner returned exit 2. Requested role model ID
`gpt-5.4` was not validated or invoked. No new model-connectivity probe was needed
once isolation failed; earlier network-failure evidence is retained separately.

Evidence: `results/workflows/report.md` includes all three six-metric comparison
tables; `comparison.json` retains verdicts; `capabilities.json` and `invocation.json`
record the block; `*-check.json` retain actual checks; `integrity.json` records
zero subject turns, stakeholder calls, assessor calls and assigned scores. The
source commit is `a9a8d60d692f108f627455c6f5d44ca04415827d`.

The next supported run must first qualify the native discovery/resume adapter and
stakeholder on one pilot, inspect actor disclosure/consent decisions, then repeat
paired workflows (the documented campaign uses five repetitions). Adaptive
exchanges differ by subject behavior even with the same actor policy. Trace-based
skill reads can reveal the arm to the assessor, so blinding is partial. Turn
snapshots cannot by themselves prove absence of transient writes. These limits
are explicit; there is still no measured Lean Engineering improvement or observed
agent failure justifying a skill edit.

## Business requirements coverage expansion (2026-10-30)

The original eight cases did not directly cover `grill-with-docs`,
`requirements-engineering`, `behavior-specification` or `lean-engineer`.
Six cases now fill that gap, bringing the suite to **14 cases covering all ten
skills**. Coverage does not establish effectiveness; no new behavioral scores
exist.

| New case | What it assesses |
|---|---|
| `discovery-commission-change` | Use existing domain facts, expose contradictory stakeholder assumptions, ask the next consequential questions |
| `requirements-commission-proposals` | Turn accepted decisions into precise, traceable business requirements without inventing policy or architecture |
| `requirements-conflicting-stakeholders` | Keep disputed rules unresolved instead of calling a contradictory specification final |
| `acceptance-commission-publication` | Concrete requirement-linked scenarios for roles, tenants, rates, effective dates, evidence, retries and stale review |
| `routing-ambiguous-business-feature` | Start with discovery and appropriate approval dependencies for unresolved business behavior |
| `routing-small-approved-fix` | Bypass unnecessary lifecycle ceremony for an agreed, low-risk correction |

Three small public fixtures provide stakeholder messages, accepted decisions and
an approved specification at the appropriate lifecycle stage. They distinguish
commission percentages from payments, unknown from zero, upload order from
business effective dates, proposed from published values, and stakeholder wishes
from approved policy. Candidate conflicts, source evidence and history remain
business requirements rather than a reason to mandate particular technology.

Independent judging now receives the original fixture documents as well as final
artifacts. A new harness test verifies that rewriting or deleting an accepted
rule cannot hide the original rule from the judge. The phase-aware rubric assesses
verifiable business behavior and document handoff quality; it does not demand
code, database schemas or executable tests from a requirements/discovery task.
A coverage test ensures every repository skill has at least one scenario.

Actual follow-up checks: **14 harness tests: 13 passed, one live-isolation test
skipped**. Scorer self-test, compilation and whitespace checks passed. The new
six-case invocation returned exit 2 because isolation is still unavailable.
All twelve paired contexts retain identical fixture inputs and explicit
`not_executed`/`not_judged` statuses. No model requests or independent judgments
were performed by this invocation, and no scores were assigned. The requested
`gpt-5.4` model remains an unverified configured ID, not evidence of availability.

Evidence and all six requested metric tables:
`results/business-requirements/report.md`, `comparison.json`, `capabilities.json`,
`invocation.json`, `integrity.json`, per-case artifacts and the `*-check.json` logs.
The source commit for this invocation is `6473a96`; previous raw results are
retained unchanged.

These scenarios assess a **single discovery round or specification handoff**.
They do not test adapting to stakeholder replies, interview convergence or the
complete approval-to-delivery lifecycle. Such testing needs a controlled,
identical stakeholder-response protocol for both variants. At this stage no full conversational business-requirements evaluation had been
implemented or executed; the later workflow upgrade above adds that path but is
still not executed.

The original results below describe the initial eight-case run and its checks.

## Delivered

A standard-library runner (`evals/runner.py`) executes paired Codex CLI
sessions, captures inputs/artifacts/logs/hashes, runs deterministic checks, requests
independent schema-constrained judging, and writes JSON/Markdown comparisons.
Fixtures cover a real SQLite webhook API, an overfactored customer lookup and
three related synthetic OCR documents. All eight original prompts are retained;
only public fixture paths were added to `cases.json`. Skills and `score.py` were
left unchanged.

The original ten skills describe a selective lifecycle with explicit approval
gates, proportional architecture, risk-based tests, simplification and honest
verification. The original scorer validates six manually supplied dimensions;
it never calls an agent. Maintainability is now separately judged and reported,
while the original 9/12 gate remains explicitly identified as the legacy gate.

## Initial checks (2026-10-29)

| Check | Actual result |
|---|---|
| Original `python3 evals/score.py --self-test` | Passed; score validation only |
| Original `python3 -m unittest discover -v` | 0 tests; exit 5, `NO TESTS RAN` |
| New harness tests, `python3 -m unittest discover -s evals/tests -v` | 12 discovered: 11 passed, 1 skipped |
| Public webhook fixture smoke test | 1 passed |
| Held-out checker against correct reference control | 8 passed, asserted by harness test |
| Held-out checker against original buggy fixture | 2 passed, 6 failed, as expected for a negative control |
| `python3 -m compileall -q evals` | Passed |
| `git diff --check` | Passed |
| Prepared-suite input/output integrity | All 8 cases / 16 contexts validated; equal paired fixture hashes, no scores |
| Scenario agent execution | **Not executed** |
| Independent rubric judging | **Not executed** |

The negative-control failures detect repeated ledger effects, absent database
uniqueness, conflicting payload acceptance, concurrent duplicate inserts, and
unsafe legacy handling. They are defects in an intentionally buggy fixture,
**not failures by a baseline or treatment agent**. Harness stubs and the correct
reference are test controls, not behavioral samples.

## Why execution is blocked

Codex CLI 0.163.0 is installed, reports a ChatGPT login, and supports noninteractive
execution and structured-output flags. A first probe failed to initialize its
read-only runtime. A fresh writable runtime fixed initialization and emitted
`thread.started` / `turn.started`, but an `EVAL_READY` request produced no answer:
WebSocket attempts reported `Operation not permitted`, followed by HTTPS
connection failures and a 40-second timeout. Starting a thread is not completing
an evaluation. Current environment readiness reports no configured API secrets,
runtime variables or outbound identities; the restricted network policy does not
allow the ChatGPT/OpenAI model hosts. Login alone did not establish usable access.

The independent filesystem probe also failed with
`bwrap: setting up uid map: Read-only file system`. Codex workspace-write mode alone
would allow reading sibling results and grading files. The runner therefore
requires a separate mount/PID namespace and refuses live calls when it cannot
establish it. Its live filesystem-isolation test is the one skipped harness test.
No network policy or sandbox bypass was attempted.

The requested pilot, `review-overfactored`, was recorded as blocked (runner exit
2). Remaining cases were prepared without model calls because the pilot did not
work. `prepared-suite` is the final all-case preparation from committed runner
source. Earlier pilot/preparation records are retained. The requested model IDs
in prepared metadata are `gpt-5.4` for both generation and independent judging;
**availability of that model was not verified and no scenario request was sent**.
The unsuccessful connectivity probe used the CLI default, whose resolved model
was not established.

## Scenario comparisons

N/E means **not evaluated**, not zero or pass. All numerical differences are
unavailable. The evidence paths below contain exact prepared prompts, original
fixtures, file snapshots, hashes and explicit blocked/unjudged statuses. The
architecture/planning/review scenarios require semantic judging; nonempty text
alone would not prove their correctness.

### deepagent-multidoc-architecture

| Metric | Baseline | Lean Engineering |
|---|---|---|
| Requirements correctness | N/E | N/E |
| Architecture quality | N/E | N/E |
| Simplicity | N/E | N/E |
| Maintainability | N/E | N/E |
| Testing quality | N/E | N/E |
| Verification evidence | N/E | N/E |
| Overall assessment | Not executed | Not executed |

Evidence: `results/prepared-suite/deepagent-multidoc-architecture/1/{baseline,lean}/`.

### deepagent-multidoc-delivery

| Metric | Baseline | Lean Engineering |
|---|---|---|
| Requirements correctness | N/E | N/E |
| Architecture quality | N/E | N/E |
| Simplicity | N/E | N/E |
| Maintainability | N/E | N/E |
| Testing quality | N/E | N/E |
| Verification evidence | N/E | N/E |
| Overall assessment | Not executed | Not executed |

Evidence: `results/prepared-suite/deepagent-multidoc-delivery/1/{baseline,lean}/`.

### deepagent-multidoc-technical-design

| Metric | Baseline | Lean Engineering |
|---|---|---|
| Requirements correctness | N/E | N/E |
| Architecture quality | N/E | N/E |
| Simplicity | N/E | N/E |
| Maintainability | N/E | N/E |
| Testing quality | N/E | N/E |
| Verification evidence | N/E | N/E |
| Overall assessment | Not executed | Not executed |

Evidence: `results/prepared-suite/deepagent-multidoc-technical-design/1/{baseline,lean}/`.

### duplicate-webhook

| Metric | Baseline | Lean Engineering |
|---|---|---|
| Requirements correctness | N/E | N/E |
| Architecture quality | N/E | N/E |
| Simplicity | N/E | N/E |
| Maintainability | N/E | N/E |
| Testing quality | N/E | N/E |
| Verification evidence | N/E | N/E |
| Overall assessment | Not executed | Not executed |

Evidence: `results/prepared-suite/duplicate-webhook/1/{baseline,lean}/`.

### review-overfactored

| Metric | Baseline | Lean Engineering |
|---|---|---|
| Requirements correctness | N/E | N/E |
| Architecture quality | N/E | N/E |
| Simplicity | N/E | N/E |
| Maintainability | N/E | N/E |
| Testing quality | N/E | N/E |
| Verification evidence | N/E | N/E |
| Overall assessment | Not executed | Not executed |

Evidence: `results/prepared-suite/review-overfactored/1/{baseline,lean}/`.

### small-validation

| Metric | Baseline | Lean Engineering |
|---|---|---|
| Requirements correctness | N/E | N/E |
| Architecture quality | N/E | N/E |
| Simplicity | N/E | N/E |
| Maintainability | N/E | N/E |
| Testing quality | N/E | N/E |
| Verification evidence | N/E | N/E |
| Overall assessment | Not executed | Not executed |

Evidence: `results/prepared-suite/small-validation/1/{baseline,lean}/`.

### treaty-addendum

| Metric | Baseline | Lean Engineering |
|---|---|---|
| Requirements correctness | N/E | N/E |
| Architecture quality | N/E | N/E |
| Simplicity | N/E | N/E |
| Maintainability | N/E | N/E |
| Testing quality | N/E | N/E |
| Verification evidence | N/E | N/E |
| Overall assessment | Not executed | Not executed |

Evidence: `results/prepared-suite/treaty-addendum/1/{baseline,lean}/`.

### verification-honesty

| Metric | Baseline | Lean Engineering |
|---|---|---|
| Requirements correctness | N/E | N/E |
| Architecture quality | N/E | N/E |
| Simplicity | N/E | N/E |
| Maintainability | N/E | N/E |
| Testing quality | N/E | N/E |
| Verification evidence | N/E | N/E |
| Overall assessment | Not executed | Not executed |

Evidence: `results/prepared-suite/verification-honesty/1/{baseline,lean}/`.

## Recommendations grounded in these results

1. Make supported model access and filesystem isolation available before rerunning
   the pilot. These are the observed blockers; changing skill text cannot resolve
   them. Use Linux with working bubblewrap user/PID namespaces and authorized
   model-host access with the existing proxy/CA setup and valid authentication.
2. Keep the newly automated evidence pipeline. The former self-test and zero-test
   discovery could not answer the behavioral question. Preserve raw artifacts,
   independent judging and explicit unverified statuses in future runs.
3. Retain the real-database retry/concurrency/rollback checks. Their negative and
   positive controls establish that the checker can distinguish consequential
   correctness failures without rewarding helper count or test count.

**No content changes to Lean Engineering are justified by observed agent failures,
because no agent outputs exist.** In the next supported run, use the five priority
cases to identify specific misses before editing skills: unjustified forwarding
layers, lost immutable span/version references, discarded conflict alternatives,
silent precedence assumptions or oversized delivery plans. These are hypotheses
to test, not measured deficiencies. Change the relevant skill only after a
reproducible miss, then rerun the same paired cases and inspect concrete evidence.

## Reproduce and remaining limits

Follow `evals/README.md`: choose a model ID actually supported by the environment,
run `review-overfactored` alone with a fresh independent judge, inspect the pilot,
then run the current fourteen-case suite with at least three repeats. Both variants receive the
same fixture bytes, model, medium reasoning effort, tools and timeout; treatment
alone receives the relevant skill content. The judge sees neither variant labels
nor skill prompts. Rubric/checker material is withheld until generation exits.

Live end-to-end Codex and judge execution remains unverified here. CLI option
support and mocked harness tests do not prove successful live integration. The
webhook fixture uses SQLite, so passing it would not establish PostgreSQL or HTTP
integration behavior. The Deep Agents artifacts evaluate designs; the synthetic
OCR fixture does not demonstrate OCR/extraction accuracy, production reliability,
or a working reviewer UI. Model judging needs human calibration and repeated
samples before asserting an improvement. Prepared contexts and a successful
runner process are not successful behavioral evaluations.

Raw evidence: `results/environment/` (connectivity, original checks, final check
logs and checker negative control), `results/pilot/` (blocked pilot), and
`results/prepared-suite/` (final structured comparison and all eight paired inputs).
The runner source commit for the final preparation is
`81be39e5a2705c60b54e00a4f392a8c33b1c71e3`; all results and this report are committed separately
on `eval/automated-quality-comparison`.
