# Modular monoliths and distributed services

## Book material

**Foundation:** Sam Newman — Building Microservices, second edition. **Concept/locator:** Second edition, Chapters 1–4: What Are Microservices?; How to Model Microservices; Splitting the Monolith; Microservice Communication Styles. [Source / locator](https://samnewman.io/books/building_microservices_2nd_edition/). **Evidence basis:** `author-toc`.

Microservices are independently deployable services shaped around business responsibilities. Useful boundaries require information hiding, cohesion and manageable coupling; distribution brings communication, testing and operating consequences.

This is attributed synthesis, not a quotation or a claim that the full passage was retrieved. The procedure and example below are original applications; they are not examples copied from the book.

## When to use and what to inspect

Use when choosing deployment boundaries. Inspect team ownership, release cadence, shared invariants, workload/failure isolation and current operating capabilities.

## Apply the idea

1. Identify the capability and data owner before choosing a deployment unit.
2. Check whether same-process modules/worker resource isolation satisfy the actual need.
3. For a service option define its data/contract, failure response, deployment and operational owner.
4. Recommend against present constraints and state a concrete adoption/reconsideration trigger.

## Worked application

A two-person clinic releasing one application gains little from separate booking/waitlist services when booking invariants share a database transaction. Independently regulated settlement with its own store and 24-hour outage tolerance does warrant a distributed contract. Both recommendations follow the constraints rather than a preferred topology.

## Trade-offs and simpler choice

A monolith shares process/deployment failures; a service adds latency, duplicates, version skew and tracing/recovery work. Do not omit necessary durability merely to keep the design local.

## Verify the decision

Check atomic invariants, independent-release claims and outage recovery with the chosen boundaries. Measure isolation benefits instead of inferring them from service count.
