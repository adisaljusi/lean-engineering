---
name: grill-with-docs
description: Deeply interview stakeholders about feature ideas, product rules and engineering design while reading repository documentation, maintaining domain vocabulary and surfacing ambiguities before implementation.
---

# Grill With Docs

First inspect relevant repo code, tests, docs, schemas and ADRs; do not ask questions already answered there. Restate what you know and distinguish facts from guesses. Ask 2–5 focused questions per round, selecting high-risk branches first. Challenge vague statements using examples and counterexamples; continue until critical branches resolve.

Probe desired outcome, user roles, domain terms, invariants, lifecycle, ownership, conflicting rules, retries, duplicates, concurrency, authorization, failure behavior, integration contracts, migrations, volume, consistency, security, audit and observable proof of correctness. Avoid jumping into implementation patterns.

Record a concise glossary, decisions, assumptions and unresolved questions in existing project docs or the feature spec. Add ADR proposals only when a significant design choice emerges. Do not approve assumptions on the user's behalf. End with candidate acceptance scenarios and ask whether to specify them.
