# C. Design decision

**Start with:** the question to decide, authorization (usually design-only), current system and hard constraints. If the user names a technology, determine whether it is required or merely an option.

1. Inspect the relevant actual topology/code, data ownership, transactions, deployment/configuration and prior decisions. Sketch current responsibilities/flow with sources; explicitly label unknowns.
2. Name business capabilities/owners, invariants and the quality drivers that distinguish choices. Ask about workload/consistency/recovery only if an unanswered target changes the recommendation. Do not invent measurements or legal/business authority.
3. Describe the smallest credible proposal and other viable options for the consequential choice. Compare invariant satisfaction, coupling/failure behavior, compatibility, implementation/operating cost and uncertain assumptions. Do not force two artificial alternatives for an obvious local choice.
4. Select a diagram for the decision: context for scope, sequence for timing/transactions/failure, data flow for provenance, state for lifecycle. Label relationships and owners that matter. Check syntax if tooling supports it, then check semantic consistency with contracts/prose. Do not claim a render from source or parsing.
5. Recommend an option for today. Explain what gets harder, unresolved assumptions, migration/rollout/rollback and proof. Possible future architecture needs adoption triggers and costs; leave speculative implementation out.
6. Provide the next implementer's handoff: accepted vs proposed behavior, boundary/contract changes, first slice and verification. Respect design-only scope. Existing implementation authorization permits ordinary technical follow-through; do not require a fresh approval solely because design ended.

**Useful finish:** a reader can see what problem the choice solves, why it fits the observed system, how to adopt/check it and what would change the recommendation. An ADR is useful for a lasting contentious choice, not required for every answer.
