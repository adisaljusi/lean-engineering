# Webhook service

Python standard library; run `python3 -m unittest discover -v`.
`connect(path)` opens the existing SQLite persistence layer; `handle_event(conn, event)`
is the public API. Events have a stable string `id` and integer `amount` (minor units).
The input is already authenticated and validated at the HTTP boundary.

Approved behavior: return 200 on first delivery and identical retries, persisting
one event and one ledger effect per event ID. A retry with the same ID but a
different amount returns 409 without changing either row. Database failures must
propagate and roll back both writes so a later retry can succeed. The database
must enforce event ID uniqueness, including independent concurrent connections.
Existing deployments can have duplicate identical events/ledger effects: migrate
these safely; do not silently choose among conflicting amounts.

Implementation and the focused tests are authorized. Keep the public signatures
and existing tables. Do not add infrastructure. SQLite is the evaluation fixture;
production PostgreSQL compatibility is outside this fixture's demonstrated scope.
