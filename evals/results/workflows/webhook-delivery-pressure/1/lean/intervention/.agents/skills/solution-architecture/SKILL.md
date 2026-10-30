---
name: solution-architecture
description: Review and design C4, cloud and domain-level solution architecture using DDIA principles, explicit quality drivers, system boundaries, data ownership, alternatives and ADRs.
---

# Solution Architecture

Read approved `spec.md`, existing topology and architectural constraints. Start with actors, external dependencies, bounded contexts and ownership. Use C4 system context and container diagrams where they clarify relationships; component/dynamic/deployment views only when useful. Preserve current system conventions.

Compare simplest viable design with credible alternatives. Assess actual quality drivers and applicable DDIA trade-offs: consistency, transactions, replication, ordering, concurrency, idempotency, retries, backpressure, availability, schema evolution and recovery. Do not introduce microservices, queues, events, new databases or agents without a requirement justifying their cost.

For relevant cloud systems, describe deployables, IAM/trust boundaries, networking, secrets, monitoring, deployment/rollback, resilience, scaling and cost. Record high-impact decisions as lightweight ADRs: context, choice, alternatives, consequences, revisit trigger.

Write the solution-architecture portion of `design.md`; obtain approval before detailed implementation planning. Do not confuse feature architecture with a company-wide enterprise architecture rewrite.
