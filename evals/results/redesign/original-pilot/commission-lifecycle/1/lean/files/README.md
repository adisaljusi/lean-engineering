# Treaty commission portal

Existing Python monolith, SQLite local persistence, standard-library tests.
Run `python3 -m unittest discover -v`. Production PostgreSQL and HTTP integration
are outside this local fixture. The tenant/role context is already authenticated
by the HTTP boundary; the service still owns its business authorization checks.

The current prototype stores proposals but immediately updates a section's rate.
Stakeholders have requested a proper addendum workflow. Business decisions must be
settled with the product owner before changing application code. Read the existing
stakeholder notes. Keep existing public entry points; a backward-compatible schema
extension is allowed. Follow the monolith's conventions, not a new framework.

## Existing API boundary used by callers

- `connect(path)` -> connection; example treaty T-42 in Org-A has property at
  1250 basis points and casualty at 1000. One basis point is 0.01 percentage point.
- `propose_change(conn, actor, change)` -> `{id, status}`.
- `publish_change(conn, actor, change_id, reason='')` -> `{id, status}`.
- `rate_on(conn, actor, treaty, section, day)` -> integer basis points.
- `list_changes(conn, actor, treaty, section)` -> candidate dictionaries retaining
  submitted fields plus `status` and `reason` for this tenant/treaty/section.

Actors are `{tenant, role}`. Roles in the portal are `reviewer` and `approver`.
A candidate has `id`, `treaty`, `section`, `rate` (basis points or None), `start`,
optional `end`, and `source` with `document_version`, `page_id`, `span_id`, `quote`.
Dates use YYYY-MM-DD. Invalid business input raises ValueError, unauthorized
operations raise PermissionError, and an inaccessible/missing section may raise
KeyError. Sources in `sources.json` are immutable OCR records. Do not change them
to make an extraction or a proposed rate appear supported.
