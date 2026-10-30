# Review decisions, not pattern vocabulary

Use on an actual diff/design with accepted behavior and surrounding callers/contracts. Procedure: establish requested scope; trace one important flow; inspect changed invariants/failure paths; check integration/migration/authorization; then assess whether responsibilities and tests make sense to a human. Execute feasible checks when useful, labeling scope honestly.

Worked excessive complexity: Controller → Facade → Coordinator → Manager → StrategyFactory → Strategy → Repository forwards the same customer ID with no policy. Each hop obscures ownership and tests often mirror implementation. Ask which hop owns a real rule, transaction, substitution or failure boundary. Propose endpoint → existing lookup function/database (or existing meaningful service boundary); retain behavior tests for found/missing/forbidden. Do not demand this exact structure if actual responsibilities differ.

Worked justified complexity: independently deployed fulfillment must survive a day-long outage without losing committed orders. A durable outbox/relay, consumer deduplication and recovery owner add code but satisfy the invariant. Rejecting them simply because “queues are complex” misses the failure requirement. Check atomic acceptance, duplicates, acknowledgments, retention/version compatibility and backlog recovery rather than count layers.

For a finding give location, concrete trigger, observed/likely consequence, evidence and remedy. Distinguish demonstrated bug, uncertainty requiring a check and optional improvement. A concrete correctness defect remains a defect under an otherwise favorable score. For a small reviewed patch use a short result; do not create an architecture assessment document for ceremony.

Verify review coverage against changed contracts and actual evidence. Source foundations: Martin's dependency direction, Fowler's enterprise patterns and Newman's service trade-offs; the examples are original. Pattern names are prompts to inspect responsibilities, never proof of quality.
