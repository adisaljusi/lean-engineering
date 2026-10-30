# Treaty extraction product context

Existing Python monolith, PostgreSQL, object storage, OCR service and model gateway.
A contract bundle contains 10–80 related binder, slip, wording, endorsement and
addendum PDFs. The first demonstration uses three synthetic documents and six
fields: territory, peril, limit amount, limit currency, deductible and commission.

OCR provides immutable document-version/page IDs, UTF-8 text and stable span IDs
with text offsets and page-local bounding boxes. Originals and OCR outputs are
retained in object storage. Reviewers must open exact supporting evidence and
inspect conflicting candidates. A document revision never changes old evidence.
Document relationships, value normalization and human decisions must be traceable.
A new extraction run must be distinguishable from a human-approved result.

Tenant isolation and reviewer authorization are existing application boundaries.
Model and OCR calls can fail, time out, or return malformed data. Duplicate uploads
and run retries occur. No latency, cost or throughput SLA has yet been agreed.
Document precedence, authority of a later unsigned addendum, normalization of
territory/peril names and review roles require domain-owner confirmation.

For architecture: propose alternatives and questions; no implementation is authorized.
For technical design: the accepted architecture is the existing monolith with bounded
model-gateway extraction work and PostgreSQL/object storage; field semantics are
still proposals requiring approval. For delivery planning: the feature direction
and a three-document/six-field starting scope are accepted; detail open domain
rules as explicit dependencies. Produce a plan only. No code is authorized.
