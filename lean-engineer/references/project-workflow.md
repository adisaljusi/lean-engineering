# Optional project workflow

Use when the user/team wants a repeatable process across a larger task or several sessions. This is an optional way to compose the method library and task playbooks. It needs no framework installation, agent hooks, special command syntax, mandatory subagents or new state schema. Individual skills remain independently usable.

## Adopt only the conventions that pay for themselves

1. Read current project/process instructions and existing issue/spec/design/plan/CI artifacts. Reuse their ownership, locations and statuses. A conversation asking for one task's workflow is not permission to install permanent project rules.
2. State the active outcome/scope and the applicable playbook from `workflows.md`. Carry forward accepted facts and authorization. A project roadmap can hold future work, but it does not authorize implementation of every future idea.
3. Identify where a human/resuming agent will find decisions and evidence. For a short task the existing issue/conversation is sufficient. For long work keep a compact note in an existing feature artifact; ask no separate permission for an ordinary task note within authorized scope.
4. Run the task playbook. Select detailed methods by the immediate decision, not a fixed sequence. When a slice completes, record its actual result and next dependency. A plan checkbox means completed work only when its evidence supports that meaning.
5. At a handoff or session boundary, save the smallest state that lets the next actor continue correctly. Avoid copying the full conversation or engineering library.

## Minimum useful handoff

Use these fields in an existing issue/note when they are needed; this is an example shape, not a required new file or serialization format:

```text
Outcome/scope: implement proposal-only ingestion; publication rules already accepted.
Authorization: user authorized implementation in the accepted delivery request;
               production rollout is outside this task.
Accepted decisions: source/path/turn, precise meaning, important corrections.
Current state: implementation slice and owning files; branch/commit if relevant.
Evidence: command + environment + result + artifact; skipped/unrun limits.
Unresolved: exact decision/check, consequence, owner; independent work remaining.
Next action: concrete step and what result determines the following action.
```

Distinguish accepted decisions from proposals/assumptions and completed checks from planned checks. A correction supersedes earlier active behavior while retaining its reason/history where useful. Do not convert a proposed design into accepted policy because it appeared in a handoff.

## Resume procedure

1. Read the handoff, referenced accepted sources and project instructions before asking the user to repeat them.
2. Inspect actual source/diff/branch state and relevant existing check artifacts. If a note says “complete” but the effect/check is missing, state the discrepancy and verify the affected claim. Do not blindly trust either the note or a green process exit.
3. Preserve valid decisions and authorization; do not reopen them under another skill name. If actual state or a newer accepted correction contradicts the note, reconcile that narrow discrepancy with evidence. Do not silently rewrite material business policy.
4. Load the method needed for the recorded next decision and continue authorized work. Re-run a check when changed code/environment or uncertain evidence warrants it, not merely because a new session began.
5. Update progress/evidence as work changes. On final delivery, explain demonstrated behavior and remaining release/operational limits; do not merge/deploy by default.

## Example of resuming without restarting

Handoff says: immutable evidence ingestion is verified; accepted policy is pending proposals plus human publication; user authorized implementation. Remaining: stale-review revision check and database integration. A new session reads the evidence contract and current transaction, implements/reuses a revision predicate, tests stale concurrent decisions and rollback, then reports real results. It does not ask whether “automatic” means publish, demand new specs, rerun completed ingestion work without cause, or infer deployment authorization.

## Adaptation and failure handling

For a small fix, collapse this to the issue and existing regression; there is no roadmap/milestone ritual. For a consequential migration, add compatibility stages, data/backfill reconciliation and explicit rollback/irreversible points. If parallel execution is authorized and available, keep shared contracts/ownership explicit and reconcile each result against original evidence; otherwise execute inline. Never assume extra agents, particular model names or unverified context-window limits.

If evidence fails, preserve the failure and resolve it within authorized scope. If an accepted business decision must change, explain consequence and get the needed decision before dependent work. If a resource is unavailable, record Not verified and the concrete next check rather than marking a phase complete. A team may have an explicit approval policy; honor the actual policy without inventing one at every step.

Framework capability here means repeatable selection, handoffs, correction and evidence across tasks. It does not mean a compulsory lifecycle, a second database of project truth or a command runner.
