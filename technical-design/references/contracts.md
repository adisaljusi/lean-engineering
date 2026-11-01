# Domain, persistence and API contracts

Use when identity, invariants, shared writes or compatibility affect safety. Inspect actual schemas, clients, tests and owners before choosing a pattern.

## Procedure

1. Write the invariant with business data: a publication references an authorized reviewed decision at a known revision; a rate is integer basis points, not float money; unknown is distinct from zero.
2. Identify who may change it and the smallest atomic boundary. A domain function can validate one value, but two processes need database constraints/transactional concurrency control for shared invariants.
3. Define identity/lifecycle. Entities have continuity independent of attributes; values compare by meaning. Use records/dataclasses for simple data, not a class per property. Choose aggregate boundaries from invariants, not object graphs.
4. Specify input/output units, nullability, errors and ownership at external boundaries. Validate transport shape, then business meaning. Do not turn persistence exceptions into ambiguous success.
5. Compare credible representations and migration cost. Verify with actual old/new consumers and real database behavior.

## Worked API evolution: basis points

Current clients send `commission_percent: "12.50"`; new clients need precise `commission_bps: 1250`. Keep public semantics and old clients while upgrading. Inspect decoder behavior and generated clients; do not assume additive fields are safe.

Option A: retain percent contract, parse with Decimal and convert exactly at boundary. Simplest if no new consumer requirement. Option B: expand to accept a new bps field with explicit conflict behavior, then deprecate old representation. Option C: new versioned endpoint when strict clients cannot handle expansion or meanings change substantially. The right choice depends on client control/release cadence.

For B, accept one field; if both appear require exact agreement or reject according to a documented contract. Reject bool/fractional bps, nonfinite values and unknown when publication requires a rate. Do not round an invalid 12.505% silently. Store canonical integer bps with NOT NULL/CHECK where required; keep unknown nullable only for explicitly incomplete candidates. Server responses follow negotiated/versioned contract. Deploy compatible readers first, observe old usage, backfill/reconcile, migrate writers, then remove only under an agreed policy. Rollback remains possible until old data/contract is removed. Test old client, new client, mixed conflicting request, boundaries 0/10000, missing/null and version skew.

## Transactions and patterns

A unique key prevents duplicate identity; retry semantics also compare payload to reject same ID/different content. Optimistic locking uses `UPDATE ... WHERE revision = expected` and checks affected rows, with decision history in the same transaction. An ORM unit of work or a simple transaction context can own this; a new generic repository is unnecessary for one operation. A data mapper earns its cost when domain/storage models truly diverge; transaction script fits straightforward operations. These are applications of Fowler's enterprise patterns, not reasons to create layers.

Public APIs need consumer-oriented resources/operations, stable error contracts, compatibility policy and observability appropriate to the organization. A small internal API may use a documented schema and contract tests; a large ecosystem may require review, lifecycle ownership, version/deprecation telemetry and staged rollout. Neither needs governance meetings for each handler. Do not leak internal table shapes by accident.

Further detail: Eric Evans, *Domain-Driven Design*; Martin Fowler, *Patterns of Enterprise Application Architecture* (https://martinfowler.com/eaaCatalog/); OpenAPI specification https://spec.openapis.org/oas/latest.html; Gough/Bryant/Auburn, *Mastering API Architecture*. Examples and procedures are original synthesis; no chapter/page claims.

For book-derived concepts used here, select the relevant entry in the [topic index](topic-index.md), including domain identity/invariants, persistence patterns, SOLID/GoF choices, algorithms and API contracts/evolution. The topic entries distinguish attributed ideas from original application examples; Python API behavior remains grounded in its official documentation.
