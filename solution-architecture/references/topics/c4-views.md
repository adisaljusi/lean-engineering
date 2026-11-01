# C4 context, container and component views

## Book material

**Foundation:** James Gough, Daniel Bryant and Matthew Auburn — Mastering API Architecture (2022). **Concept/locator:** Introduction — Using C4 Diagrams; C4 Context Diagram; C4 Container Diagram; C4 Component Diagram. [Source / locator](https://www.oreilly.com/library/view/mastering-api-architecture/9781492090625/). **Evidence basis:** `publisher-toc`.

C4 views describe a system at distinct structural levels. A context view explains scope/actors/dependencies; containers show applications and stores; components show responsibilities inside a container. The C4 model originates with Simon Brown.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when an architecture question requires scope or structure at a particular level. Inspect current deployables, external actors/stores, owning modules and the audience’s decision.

## Apply the idea

1. Choose context for system scope, containers for applications/stores, or components for internal responsibilities.
2. Label current/proposed and keep one abstraction level coherent; a C4 container is not necessarily a Docker container.
3. Name responsibilities and label relations with action/data and important trust/ownership boundaries.
4. Use a sequence/data-flow/state view separately when timing, provenance or lifecycle is the question; no need to generate all levels.

## Worked application

For extraction, a container view can show the existing application, worker, PostgreSQL, object storage and model gateway. It cannot by itself explain a stale-review transaction or immutable span provenance; use the focused sequence/data-flow example for that decision.

## Trade-offs and simpler choice

More levels cost maintenance and can drift from code. A context sketch or short paragraph is simpler for a narrow question. Do not label arbitrary boxes “C4” without explaining scope/relationships.

## Verify the decision

Compare the view to observed deployment/code/contracts and trace a concrete flow. Validate supported diagram syntax/rendering separately from architectural correctness.

## Further detail

Authoritative supplemental definitions: Simon Brown, [C4 diagrams](https://c4model.com/diagrams). Mermaid rendering/use instructions remain in this skill’s visuals guide.
