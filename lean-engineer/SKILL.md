---
name: lean-engineer
description: Orchestrate a lightweight architecture-first software engineering lifecycle across requirements, BDD, C4/cloud design, detailed technical design, implementation, testing and evidence verification. Use for end-to-end feature delivery or choosing which Lean Engineering skill comes next.
---

# Lean Engineer Router

Determine intent and inspect existing repository conventions. Route to these independently invocable skills as needed: `grill-with-docs`, `requirements-engineering`, `behavior-specification`, `solution-architecture`, `technical-design`, `implementation-planning`, `test-driven-development`, `code-review`, `evidence-verification`.

Do not blindly run all phases. A small, low-risk fix can proceed directly to a failing test and verification. A new feature with unclear business semantics starts with grilling. Do not create artifacts for ceremony.

Maintain at most three routine documents: `spec.md` (requirements and BDD scenarios), `design.md` (architecture and detailed models), and `plan.md` (testable slices), following repo paths. ADRs only for consequential decisions. Explicitly pause for critical unanswered requirements, approval of acceptance behavior, consequential architectural/data-model decisions, and user authorization to implement.

Preserve decision history and reference earlier approved artifacts. If tests expose a mistaken requirement or design assumption, return to the relevant phase; never silently rewrite approved intent. Completion requires execution-backed verification with residual risks disclosed.

Use a **human-maintainability gate** before implementation and final completion: explain why the number of modules, abstractions and tests is proportionate to the actual change. Prefer limited high-value edge coverage over exhaustive low-risk combinations. If a developer cannot readily understand the flow or diagnose a failing test, simplify it.
