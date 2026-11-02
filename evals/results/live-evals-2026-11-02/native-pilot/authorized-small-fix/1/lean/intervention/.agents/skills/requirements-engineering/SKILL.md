---
name: requirements-engineering
description: Define precise business behavior, scope and consequential quality requirements from available evidence and stakeholder decisions.
---

# Requirements Engineering

Inspect existing capabilities, terminology, contracts, tests and accepted decisions. Use when behavior needs a durable definition or a requirements handoff is requested; reuse an existing issue/spec for small changes.

Define outcome, actors, scope and business meaning before prescribing technology. Give stable IDs when traceability is useful. State triggers, invariants, identity, ownership, permissions, lifecycle, exceptions and compatibility only where relevant. Distinguish unknown from zero, upload time from effective time, and proposals from published state.

Use concrete examples to expose contradictions. Ask only about unknowns that change this decision; preserve accepted answers across handoffs. Mark facts, proposals, assumptions and unresolved rules plainly. A contradictory stakeholder wish is not approved policy. Do not invent numerical latency, retention or accuracy targets.

Load [requirements and acceptance](references/requirements.md) for rules involving dates, approvals, evidence or multiple stakeholders. It shows how to turn decisions into verifiable statements without designing infrastructure.

A useful result fits the repository's conventions and gives the next engineer observable behavior, important quality constraints, source/decision traceability and remaining questions. Quality attributes should name workload, stimulus, response and measure, or explicitly identify an unknown target. Do not require formal approval for every specification update; use the actual user authorization and consequence of changing accepted behavior. Requirements work alone does not authorize implementation.
