---
name: implementation-planning
description: Convert approved specs and technical design into concise test-first vertical slices with explicit code organization, Clean Code, SOLID, dependency direction, layers, interfaces and verification tasks.
---

# Implementation Planning

Inspect existing source tree, tests, build and CI conventions before planning. Confirm requirements, BDD scenarios, C4 architecture and significant technical models are accepted. Produce `plan.md` containing small independently demonstrable slices linked to `R*` and `AC*` identifiers.

For each slice specify touched files/modules, responsibilities, interfaces/contracts, input/output definitions, expected failing tests, implementation steps, integration dependencies and exit checks. Identify any migration, rollout, rollback or operational changes. Prefer vertical changes delivering observable behavior over broad technical-layer tasks.

Explicitly assess **engineering design quality**: descriptive naming, cohesion, minimal duplication, functions/classes with focused responsibility, separation of concerns, SOLID where useful, dependency direction, test seams, and error handling. Prefer established layering or hexagonal boundaries when suited to the repo, but do not impose ceremony or new abstractions for small features. Flag divergence from existing patterns and justify it.

Use YAGNI and KISS. Avoid implementation transcripts, speculative abstractions or unchecked TODOs. Ensure every requirement has a planned proof and every new module has a clear owner. Do not implement until the user authorizes work.
