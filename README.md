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

See `evals/` for eight adversarial prompts, including three advanced multi-document Deep Agents extraction scenarios focused on architecture, technical data/evidence design and incremental delivery. Run each with the target skill in a fresh agent session, preserve its answer, and score it independently using the 0–2 rubric. `python3 evals/score.py --self-test` validates the scorer only; it is not a behavioral test of an AI agent.

This ZIP is a distributable draft, not an automatically installed skill set. Behavioral validation requires running the skills in a supported coding-agent environment.
