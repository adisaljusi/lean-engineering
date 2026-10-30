# Accepted stakeholder decisions: commission proposals

The product owner and underwriting owner accepted these business decisions.
They authorize requirements documentation, not architecture or implementation.

Reviewers may create a commission change proposal for one identified section of
one treaty in their own organization. Only users with the approver role may
publish a proposal. Existing tenant access rules apply to every operation.
Unsigned addenda may be attached for review but cannot support publication.

A proposal identifies its treaty, section, signed source document version and
supporting page/text span, a rate expressed as a percentage, and effective dates.
Valid rates include 0 and 100 percent. A missing rate means unknown, not zero.
The effective start is a required calendar date. The optional end excludes that
date from the interval; when present it must be later than the start. Dates are
business calendar dates, not instants inferred from upload timestamps.

An unapproved proposal must never change published commission. Publishing an
approved change affects only its section and effective interval. Previously
published decisions and their supporting sources must remain inspectable.
Corrections can be proposed with an earlier effective start; they still require
approval and must not erase history. Nothing here defines a legal payment amount.

Repeated submission of the same source document version, treaty, section, rate
and effective interval must return the existing proposal, not create a second
proposal. Disagreeing signed sources for the same section and overlapping
interval require an explicit approver decision retaining both alternatives and
their evidence; upload order alone cannot decide the conflict.

The first delivery supports commission proposals and publication only. It does
not calculate payments, reinterpret treaty limits or automate legal precedence.
Latency, daily document volume, retention duration and extraction accuracy targets
have not yet been agreed. Record these as open quality targets with relevant
owners instead of supplying assumed numerical commitments.
