# Runnable Python publication slice

Run from this installed examples directory with Python 3.10+:

```sh
python -m unittest -v test_publication.py
```

Standard library only; no package installation. Caller closes connections, and `publish` owns a short transaction. The frozen Rate record carries a precise invariant; database constraints protect stored ranges. An atomic revision check and appended decision prevent stale human review from silently winning. A stable tenant-scoped request ID makes identical retries safe and rejects changed payloads. The integration tests exercise a real file database, independent connections, rollback after update and permission/tenant scope.

This is a deliberately bounded example, not a production treaty portal: authenticated tenant/role/actor are trusted inputs from an external boundary. Missing section and stale revision share an error to avoid leaking other tenants. It does not implement evidence verification, effective-date overlap/precedence, ingestion, UI or distributed messaging. Add those only with accepted rules and corresponding checks; do not mistake these passing tests for the full extraction workflow. SQLite locking is not proof of PostgreSQL behavior.

A function plus record is enough here. A generic repository, DI container, event sourcing or per-operation classes would obscure transaction ownership without solving another requirement. For a two-line validation fix, this example itself is more structure than needed.
