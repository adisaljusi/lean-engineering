---
name: technical-design
description: Make concrete domain, data, API, algorithm and Python implementation decisions with precise semantics and proportionate boundaries.
---

# Technical Design

Inspect accepted behavior, current architecture, modules, schemas, dependencies and tests. Use for decisions that need more detail before safe implementation, not a mandatory document step.

Choose the uncertain boundary. Define only consequential fields: meaning, identity, type/unit, unknown/null/invalid distinctions, owner, constraints, provenance and lifecycle. Place invariants with the owning business operation and enforce shared-write invariants in the database. Explain transaction boundaries and failures. Avoid turning every noun into a class.

Load selectively:

- [Data and API contracts](references/contracts.md) for identity/invariants, persistence boundaries, concurrency, compatibility and expand/migrate/contract changes.
- [Practical Python](references/python.md) for functions/modules/classes, validation, protocols, resources, errors, async, algorithms, packaging and tests.
- [Runnable publication example](examples/README.md) when precise domain values, SQLite transactions and stale human decisions need a concrete implementation. The code is a teaching slice, not a production framework.

For a difficult choice compare credible options against actual workload and constraints. Prefer a function or cohesive module until identity/state, lifecycle or a real substitutable boundary warrants more. Make data flow and failure behavior understandable. Reuse project tools and established interfaces; do not add wrappers, generic repositories or dependencies to express style preferences.

A useful result gives implementable semantics, key signatures/schema constraints where needed, alternatives and consequences, meaningful checks, remaining assumptions and rollout implications. Distinguish proposed from accepted definitions. Ask only about unresolved consequential meaning; implementation already requested authorizes ordinary technical decisions. Respect explicit design-only limits.
