---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-26
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

### Post-Login Routing

**Role-context priority, per [3I-DEC-041](/3i/decisions/dec-041-role-context-switch.md), evaluated in this order:**

1. **Approved Instructor role exists** → [Instructor Dashboard](/3i/modules/instructors/ui/screens/instructor-dashboard.md), regardless of whether this Account also holds learner profiles. A role-context switch on the [Account Menu](../components.md#account-menu) is available if it does.
2. **A `pending` InstructorApplication exists, no approved role yet** → [Instructor Application Status](/3i/modules/instructors/ui/screens/instructor-application-status.md), shown on every login while pending.
3. **Neither** → the ordinary Member flow: [Profile picker](profile-picker.md) for more than one profile, or the single-profile PIN skip ([3I-DEC-026](/3i/decisions/dec-026-single-profile-skips-picker.md)) landing on [Learner Dashboard](learner-dashboard.md).

**With a course reference (arrived via [Course Detail](/3i/modules/catalogue/ui/screens/course-detail.md)'s enrolment CTA):** per [3I-DEC-034](/3i/decisions/dec-034-login-preserves-course-intent.md), this overrides case 3 specifically — profile selection happens, then the Member lands on [Enrol \& Waitlist](/3i/modules/learning-delivery/ui/screens/enrol-and-waitlist.md) instead of [Learner Dashboard](learner-dashboard.md). Cases 1 and 2 take priority over this override — an approved instructor or a pending applicant lands in their respective instructor-context screen regardless of an incidental course reference, since a course-intent redirect is a Member-context concern.

**"Don't have an account? Register" does not carry a course reference forward** — registering drops it entirely, per [3I-DEC-034](/3i/decisions/dec-034-login-preserves-course-intent.md)'s scoping.

## Role Variations

None for the login form itself — identical for Member, Instructor, and Admin. Admin accounts with TOTP enabled ([3I-DEC-007](/3i/decisions/dec-007-rbac-without-hardcoded-roles.md), FR-RBAC-05) see an additional TOTP code step after password success, before session establishment. Post-login destination varies per the routing table above.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
