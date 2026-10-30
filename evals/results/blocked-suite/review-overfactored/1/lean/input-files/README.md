# Customer lookup design review

`customer.py` is the proposed design behind the single-customer endpoint. This is
a review-only request. There are no approved code changes. The concept includes
one mock-based forwarding test per layer; no executable test suite was supplied.
The only stated operation is lookup by ID. No alternate strategies or independent
lifecycle/authorization requirements for the forwarding layers have been supplied.
