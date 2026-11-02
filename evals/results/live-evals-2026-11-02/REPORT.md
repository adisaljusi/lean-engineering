# Evaluation attempt — 2026-11-02

**Behavioral result: indeterminate.** A fresh paired native-skill pilot was actually
attempted on published source `a3ba4fba8df3ba6ce25c14413a1a346f76399214`.
Both subject CLI calls received proxy HTTP CONNECT 403 errors for
`wss://chatgpt.com/backend-api/codex/responses` and timed out after 45 seconds.
Neither produced an answer. No stakeholder or assessor ran; no scores exist.

This is an environment/execution block, not a baseline or treatment engineering
failure. Filesystem isolation succeeded and was preserved. Both arms had identical
fixture inputs; treatment alone had the native skill tree including 48 topic
entries. Their presence is not evidence that the model discovered or read them.
The requested role ID `gpt-6.1` remains unverified: the denied endpoint could not
establish availability. Login status alone is not authentication/connectivity proof.

## Executed results

| Evaluation/check | Actual outcome | Interpretation |
|---|---|---|
| Native `authorized-small-fix`, baseline | Timeout; zero answer bytes; indeterminate | No completed subject behavior |
| Native `authorized-small-fix`, treatment | Timeout; zero answer bytes; indeterminate | No completed subject behavior |
| Stakeholder and independent assessor | Not invoked | No judgments or quality scores |
| Harness | 28 passed, zero skipped | Harness/control checks, including actual filesystem isolation |
| Runnable Python publication example | 6 passed | Local SQLite teaching code only |

Five deterministic checker controls were also executed in isolated contexts:

| Case | Original buggy fixture | Known reference control | Checks per execution |
|---|---|---|---|
| Duplicate webhook | Fail, as expected | Pass | 8 |
| Commission publication | Fail, as expected | Pass | 8 |
| Agreed message correction | Fail, as expected | Pass | 2 |
| Documented refund policy | Fail, as expected | Pass | 3 |
| Corrected refund/resume policy | Fail, as expected | Pass | 3 |

These ten control runs calibrate known checks; they are not outputs of evaluated
agents and do not establish that Lean Engineering improves any behavior. Expected
method counts check oracle completeness, not engineering quality. Raw outputs,
tracebacks and checker hashes are in `checker-controls/` and `checker-summary.json`.
Reference controls come from the existing harness: webhook’s control in
`evals/tests/test_runner.py`, commission’s `commission_control.py`, and simple
message/refund/resume controls matching `evals/tests/test_redesign.py`. All source
identities are fixed by the source commit above.

## Retained evidence

- `invocation.json`: exact command, timeout, exit 2 and source identity.
- `network-readiness.json`: configured model-destination policy, with no secrets.
- `native-pilot/`: original fixtures, treatment intervention/hashes, CLI capability
  results, per-arm raw events/stderr, native session records, zero-byte answer
  files, trajectories, explicit indeterminate/unjudged results and comparison.
- `summary.json`, `harness.txt`, `python-example.txt`: actual limited check results.

No other live scenarios/repetitions were launched after this pilot failed.
The holdout was left untouched. No scoring, role separation or isolation was
weakened to obtain a passing result. The same assistant did not grade its own
skill application as a substitute for an independent model assessment.

## What is needed for behavioral evaluation

The managed environment must permit the authenticated Codex CLI’s HTTPS/WSS model
traffic to `chatgpt.com` through its supported proxy/network configuration.
Allowing similarly named Git-hosting domains is not model endpoint access.
Preserve proxy/CA trust, usable authentication and filesystem isolation, and choose
a model ID the environment actually supports. Do not edit the local policy snapshot
as if that granted access.

Then run a fresh paired pilot using the existing runner (a new output directory):

```sh
python evals/conversations.py \
  --model "$EVAL_MODEL" --actor-model "$EVAL_USER_MODEL" \
  --judge-model "$EVAL_JUDGE_MODEL" \
  --cases authorized-small-fix --pilot authorized-small-fix \
  --output work/native-pilot-with-model-access
```

After inspecting actual outputs, reference reads, independent assertions and role
behavior, a useful next campaign is three fresh repetitions of the small fix,
corrected-resume delivery and multi-document design workflows; contrasting smoke
cases cover distributed settlement, API compatibility and export workload. That
campaign is **not executed** here. Keep failed/indeterminate attempts and original
exposures rather than rerunning until one passes. No effectiveness claim is
available from this attempt.
