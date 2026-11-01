# Refund eligibility handoff

Existing Python service and unittest, with no payment calls in scope. `eligible(captured_on, requested_on)` returns bool; inputs are date objects already in the resolved business timezone. None means uncaptured and is never eligible; requests before capture are ineligible.

Read `decisions.md` for the accepted policy and authorization; the older `handoff.md` is a session summary, not authority to override a later accepted correction. Preserve this README and decisions.md.
