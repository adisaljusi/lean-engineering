# Coupling, cohesion and ownership boundaries

## Book material

**Foundation:** Neal Ford, Mark Richards, Pramod Sadalage and Zhamak Dehghani — Software Architecture: The Hard Parts (2021). **Concept/locator:** Chapter 2: Discerning Coupling in Software Architecture; Chapter 3: Architectural Modularity. [Source / locator](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/). **Evidence basis:** `publisher-toc`.

Static code dependencies and dynamic runtime coupling both affect what can change or fail independently. Decomposition should create cohesive responsibilities; separating deployments does not itself remove coordination or shared-data coupling.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use before extracting a module/service or attributing a failure boundary. Inspect imports, co-changes, call chains, shared writes, required release coordination and operating owners.

## Apply the idea

1. Map one capability to code, tables, synchronous dependencies and its owning team.
2. Find invariants/shared writes that force coordination and identify the actual dependency rather than count calls.
3. Compare a stronger module boundary with a deployment/data split; include the new runtime coupling introduced.
4. Record what can now change independently and which contracts still coordinate it.

## Worked application

Extraction and review share evidence identity but not model-call runtime. Separate worker capacity can prevent model latency from blocking review; moving both into services that synchronously call the same shared tables would not create independent ownership. Keep the publication invariant with its transaction owner.

## Trade-offs and simpler choice

A service split can move complexity from imports into networks, version skew and on-call work. Cohesive same-process modules are simpler when independent releases or failure isolation are not required.

## Verify the decision

Trace expected changes and dependency outages: does the claimed boundary localize them? Check shared writes and coordinated deployments as well as an import graph.
