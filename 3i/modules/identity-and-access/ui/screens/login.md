---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-IDA-UI-005
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - authentication
figma: null
---

# Screen: Login

Satisfies: FR-AUTH-09, FR-AUTH-13

---

## Purpose

Email and password entry, or a social login option routing to [Social login — DOB capture](social-login-dob-capture.md) on first use.

## Behaviour

Five failed attempts trigger a 15-minute lockout with progressive delay and per-IP rate limiting (FR-AUTH-09). The lockout message states the wait time; it does not distinguish "wrong password" from "account does not exist" on failed attempts generally, to avoid confirming which emails are registered.

**No phone or OTP option anywhere on this screen** (FR-AUTH-13) — email and password, or social, are the only two paths.

Successful login for a Member with more than one learner profile routes to [Profile picker](profile-picker.md). A Member with exactly one profile (themself, if they study, or their sole child) skips the picker's tile-selection step and lands directly on that profile's PIN pad — [3I-DEC-026](/3i/decisions/dec-026-single-profile-skips-picker.md).

## Role Variations

None — identical for Member, Instructor, and Admin. Admin accounts with TOTP enabled ([3I-DEC-007](/3i/decisions/dec-007-rbac-without-hardcoded-roles.md), FR-RBAC-05) see an additional TOTP code step after password success, before session establishment.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).