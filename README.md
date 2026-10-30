# Lean Engineering v2

Ten composable agent skills for architecture-first, behavior-driven, test-evidenced software engineering. Inspired by modular skill workflows, without copying their source instructions.

## Usage

Install each subdirectory as a separate skill in your agent's supported skills location. Invoke `lean-engineer` for the full workflow or choose a single skill for focused work. Each skill is standalone and uses existing repository conventions.

## Suggested lifecycle

`lean-engineer` routes: `grill-with-docs` → `requirements-engineering` → `behavior-specification` → `solution-architecture` → `technical-design` → `implementation-planning` → `test-driven-development` → `code-review` → `evidence-verification`.

Human review gates: unresolved critical requirements, acceptance specification, material architecture/data-model decisions, and authorization to implement. Small changes may use a subset of the skills.

## Artifact budget

Keep routine feature documents to `spec.md`, `design.md`, `plan.md` (in project conventions or `specs/<feature>/`). Record consequential decisions in ADRs. Never create empty documents to satisfy a ritual.

## Principles

Repository conventions first. Domain models before technology. C4/cloud/data architecture as relevant; explicit technical models, contracts and data definitions. Apply Clean Code, SOLID, layered/hexagonal architecture selectively. Prefer simple reversible designs. Tests and executed evidence over assertions. No implementation without approval; no success claim for unrun checks.

## Validation exercises

1. Ambiguous addendum processing: `grill-with-docs` must ask about contract identity, versioning, precedence, duplicates and audit provenance before designing.
2. Data-model approval: `technical-design` must define types, invariants, nullability, ownership, evolution and alternatives, then stop for review.
3. Planning: `implementation-planning` must identify files/modules, dependencies, tests and vertical slices, without inventing architectural patterns.
4. Verification: `evidence-verification` must classify skipped integration checks as Not verified, not Passed.

## Behavioral evals

For conversational workflow testing inspired by Superpowers, see
`evals/WORKFLOWS.md`: three action-based scenarios exercise discovery, changed
requirements, approval gates, implementation and verification under pressure.

See `evals/` for fourteen adversarial scenarios covering all ten skills and a small standard-library runner
that compares fresh baseline and skill-instructed Codex sessions, preserves raw
artifacts, runs held-out database checks, and requests independent rubric judging.
Start with the pilot procedure in `evals/README.md`. Execution requires supported
Codex access and filesystem isolation; blocked cases are reported as not executed.
`python3 evals/score.py --self-test` validates supplied-score handling only and
is not a behavioral evaluation. Actual local results are in `evals/REPORT.md`.

Install the skills in your supported coding-agent environment to use them outside
the isolated evaluations.
