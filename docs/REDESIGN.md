# Operational engineering redesign — 2026-10-30

## Repository and provenance

Remote HEAD still points to `master` at
`c4dba83ef49689fca22d188fc5d196e496972cd2`. The evaluation branch
`eval/automated-quality-comparison` points to
`fc7f9f7022a37c6d30043982917619baea42ca57` and is not an ancestor of master.
`improve/operational-engineering` starts at that evaluation snapshot. Its diff
therefore depends on that unmerged work; comparison against master includes the
evaluation harness as well. No default-branch change or merge is intended.

Historical reports cite `a9a8d60…`, `81be39e…` and short `6473a96` as source commits.
They are absent from fetched history. Direct fetches of the two full SHAs report
“not our ref”; fetching the short ID reports no remote ref. This does not establish
that every original local source state is recoverable, nor that no other clone
has it. Preserve those reports as historical records; use the verified fc7f9f7
snapshot for this revision. Exact fetch results are retained in
`evals/results/redesign/provenance.json`.

## Evidence categories and critique before edits

**Observed model failures: none.** The published evidence has zero subject
answers and independent judgments. Reference controls and prepared inputs are
not behavioral samples. The new original-snapshot pilot also produced no answer:
model-host CONNECT was denied (403), then each arm timed out after 35 seconds.
No stakeholder or assessor ran, and no model ID availability was established.
Requested `gpt-6.1` is an unvalidated configuration value, not proof of access.

**Observed tooling behavior:** all original 22 harness tests pass here, including
the previously skipped live isolation test. Original CLI discovery/install using
skills 1.7.4 finds only nine skills. `technical-design/SKILL.md` contains a plain
YAML description with `designs: field-level`, which the CLI rejects as a nested
mapping. This is a directly reproduced packaging defect, not a model failure.

**Static deficiencies:** the following are grounded in the original files at
fc7f9f7. The expected improvements remain hypotheses until live comparisons run.

| Original file and concrete instruction | Failure mode/rationale | Revision and observable behavior to test |
|---|---|---|
| `grill-with-docs/SKILL.md`: “Ask 2–5” plus broad topic list | Quota and checklist can cause generic/redundant questions | Decision/consequence procedure and worked exchange; ask only unanswered decision-changing questions |
| `lean-engineer/SKILL.md`: explicit phase pauses and “human-maintainability gate”; README lifecycle/gates | Can reopen granted authorization and create routine documents | Scope/authorization carried across entry points; authorized small fix proceeds to useful checks |
| Requirements/acceptance/planning/architecture/technical design endings demand approval | Phase completion is confused with permission | Explicit design-only/implementation distinction; surface consequential uncertainty without repeated approval |
| Architecture mentions DDIA/C4 and selected trade-offs but has no references/examples | Names do not teach choice, failure recovery or diagram construction | Decision, communication, visuals and extraction guides; inspect current system and justify boundaries/consequences |
| Technical design lists models/patterns and hard questions without a method or Python guide | Overmodeling or vague handoff; weak implementation detail | Contracts/Python guides and runnable transactional publication slice |
| Evidence verification says never fix without separate authorization | Can stop already authorized delivery on routine failures | Respect verification-only scope while fixing failures when authorization already exists |
| All skills have no supporting library | No selectively loadable procedure/example | Self-contained per-skill references; no dependency on a shared root file |
| Technical design frontmatter invalid for actual CLI | Individual skill missing from installation | Valid metadata and CLI-tested full/individual installation |

Supporting guidance explains applicability, inputs, procedure, example, costs,
simpler choices and proof. Key examples are targeted commission discovery,
monolith versus distributed settlement, multi-document lineage/adjudication,
API unit/enum evolution and runnable Python revision-checked publication.
Visuals and Python remain supporting capabilities in existing entry points:
architecture owns system views; technical design owns concrete Python/data/API
choices; implementation carries a compact relevant guide. This avoids extra
routing ambiguity. No skill must load the whole library. Individually installed
skills do not depend on companion directories; router fallback is explicit.

## Evaluation critique and changes

The original 14 smoke cases include useful invariants but many are response-only
or from the same treaty domain. The overfactored-layer prompt states its own
obvious defect; no baseline output demonstrates that baseline actually misses it.
Several answer keys favor a lean topology and some preserve approval language
after phase boundaries. They are exploratory instruments, not ground truth.

The original conversational design is substantially stronger: independent
stakeholder/assessor, original evidence, native persistent subject session,
actual SQLite checks, correction and pressure, bounded interaction and retained
indeterminate attempts. Keep this instead of building another orchestrator.
But native installation originally copied only SKILL.md, `run_check` assumed
all private oracles had eight methods, maintainability was report-only, and
smoke `suite_passed` used model scores without enforcing independent checks.
These are static harness deficiencies, not observed subject errors.

Changes:

- Preserve both runners, separate role policies, original/final evidence and
  fresh repeated contexts. Install complete selected/all skill trees and retain
  intervention hashes separately. Smoke remains explicit instruction exposure;
  workflows measure native discovery/application together.
- Add actual small-fix and documented-refund delivery; contrast modest clinic
  boundaries with separately owned outage-tolerant settlement; add strict-client
  API evolution and large snapshot export. Existing complex discovery and
  multi-document cases remain. Judge constraints, reasoning and consequences,
  allowing both justified simpler and richer designs.
- Case-owned expected checks replace the magic eight. Missing/empty/skipped/
  wrong-count/crashed checks cannot pass. Concrete oracle failure cannot be
  overridden by a favorable assessor. Preserve legacy scores, but require
  nonzero requirements/design/maintainability for revised verdicts.
- Assess redundant questioning, repeated permission, retained decisions, diagrams,
  Python and stakeholder policy. Faulty role exposure makes the experiment
  indeterminate; hidden brief facts do not prove disclosure. Human calibration
  remains required and assessor traces can reveal the treatment.
- Reserve one author-visible offline-device conflict case outside default runs.
  Do not tune against its outcomes. It is neither blind nor representative;
  independent unseen holdouts are still needed before confirmatory claims.

No score rewards file/function/test/question/citation/diagram counts. The number
of expected oracle methods is checker-completeness metadata, not a quality score.
Preparation returns exit 2; revised pass/fail policy is explicitly versioned and
cannot be silently compared to historical legacy-only results.

## Validation and limits

| Check | Actual result | Scope |
|---|---|---|
| Original harness | 22 passed, no skips | Includes working isolation here |
| Revised harness | 28 passed, no skips | Harness/control correctness only |
| Python example | 6 passed | SQLite teaching slice, also from single-skill install |
| Skills/local links | 10 skills, 15 links valid | Self-contained selected directories |
| Remote CLI discovery | 10 skills | Descriptions parsed, technical-design present |
| Remote full/single/router installation | Passed in temporary projects | Installed skill hashes match published source |
| Diagram syntax | Both parsed | Mermaid 11.17.2 + JSDOM 26.1.0 |
| Diagram image render | Blocked | Browser policy denies CLI file URL |
| Scorer/compile/whitespace | Passed | No behavioral inference |
| Live original pilot | Both subjects timed out; no answers/scores | Model-host proxy CONNECT 403 |
| Revised preparations | 5 smoke + 3 workflow pairs, no model calls | Frozen inputs/manifests only |

CLI branch-source testing also found that a `/tree/improve/operational-engineering`
URL is interpreted as branch `improve` plus a path in skills 1.7.4. The supported
quoted `https://github.com/adisaljusi/lean-engineering.git#improve/operational-engineering`
form passes. README uses that form. Failed URL-install attempts and the successful
remote run are retained separately; no custom installer or extra branch is needed.
Router-only testing establishes instruction/file availability, not correct model
fallback behavior.

Actual results and raw commands are in `evals/results/redesign/`. The final
installation check passed against published commit `0e7f00f` of the improvement branch in temporary
projects outside the checkout. It checks full set, individual technical design,
router without companions, relative reference availability and installed example
execution. This does not prove native model discovery or correct fallback use.
Codex is the tested filesystem target; other agent runtimes remain unsupported
by this verification.

Both Mermaid sources pass syntax parsing using Mermaid 11.17.2 and JSDOM 26.1.0.
Mermaid CLI 11.12.0 help/version works; rendering with system Chromium was blocked
by browser policy (`ERR_BLOCKED_BY_ADMINISTRATOR` on its file URL). No rendered
image/readability verification is claimed; source/prose consistency was manually
reviewed. No sandbox/policy workaround was used.

The Python slice exercises real SQLite revision/transaction/retry behavior and
states its missing production concerns. It is not the full treaty workflow.
Harness tests, example success, parser checks and packaging checks establish
those limited properties, not engineering behavior improvement. The revised
skills, stakeholder and live adapter are **behaviorally unvalidated**. Next:
provide supported model-host access, qualify one fresh paired native pilot,
inspect actual reference reads/role exposures, then repeat comparable campaigns
with independent assessment and unseen cases. Preserve all failures and
indeterminate attempts; do not lower isolation/scoring to produce a win.

## Workflow clarity follow-up (2026-11-01)

The user identified a remaining gap: method guides alone did not specify how to
perform and hand off work. The follow-up adds separately loaded task procedures,
a method-to-reference catalog, a worked correction/delivery/resume walkthrough
and optional project coordination. Individual methods and router-only use remain
available. See [usage](USAGE.md), [research/rationale](WORKFLOW-DESIGN.md) and
`evals/results/workflow-followup/` for this revision's evidence. Earlier counts
and validation above describe the October 30 snapshot, not the follow-up.

## Book-material follow-up (2026-11-02)

The user clarified that references must explain the material inside the books for
each topic, not merely list sources. The [topic catalogue](BOOK-TOPICS.md) now
routes to 48 substantive topic entries across architecture, technical design and
discovery. Each distinguishes the attributed idea from original procedure,
worked application, trade-offs/simpler choices and verification. Important
transaction/consistency/model distinctions are explicit. Publisher/author
TOCs verify named locators; author summaries support named concepts; unavailable
full passages and exact pages are not claimed. GoF/algorithm synthesis records
its narrower source basis. The bibliography remains attribution and is no longer
the only route to book material. Individual skill packaging and raw evidence
are recorded under `evals/results/book-topics/`; no behavioral effect is claimed.
