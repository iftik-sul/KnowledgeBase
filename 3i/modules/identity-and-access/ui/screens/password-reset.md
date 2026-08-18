---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-18
id: 3I-IDA-UI-007
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - authentication
---

# Screen: Password Reset

Satisfies: FR-AUTH-10

---

## Purpose

Standard two-step reset: request by email, then set a new password from a single-use token link.

## Behaviour

Reset tokens are single-use with a 30-minute expiry (FR-AUTH-10). An expired or already-used token routes back to the request step with a neutral message ("this link is no longer valid, request a new one") rather than distinguishing expiry from reuse, since the distinction has no legitimate use to the person resetting and some value to an attacker probing token state.

The request step does not confirm whether the submitted email is registered (same principle as [Login](login.md)) — the confirmation message is identical whether or not the address exists.

New password entry uses the same rules as registration (FR-AUTH-08): 10 characters minimum, no composition rule, breach-checked via k-anonymity.

## Role Variations

None — identical for every authenticated role.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
