---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-18
id: 3I-IDA-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - registration
---

# Screen: Registration — Adult

Satisfies: FR-AUTH-01, FR-AUTH-02, FR-AUTH-06, FR-AUTH-07, FR-AUTH-08

**Per [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md): this is now the only account-creation path in the platform.** There is no longer a 13–17 branch. Date of birth resolves to exactly two outcomes: 18+ continues here, anything under 18 redirects to [Registration blocked — under 18](registration-blocked-under-13.md).

---

## Purpose

The single registration form. Anyone completing it successfully becomes a full adult account holder — whether or not they ever add a child profile is irrelevant to what gets created here.

## Fields

First name, last name, email, password, date of birth, locale (FR-AUTH-01). See [validation-rules.md](../validation-rules.md) for field-level rules.

Social login (Google, Apple) offered as an alternative entry point — selecting it skips password entry but still requires date of birth on first login, routing to [Social login — DOB capture](social-login-dob-capture.md) rather than this form directly.

**No guardian fields exist anywhere on this screen.** [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) removed the concept of a self-declared, unverified guardian entirely — every guardian relationship on the platform now exists only between a verified adult account and a profile created beneath it via [Profile create/edit](profile-create-edit.md).

## Behaviour

Date of birth is evaluated on submit, before any other field is validated further, since it determines the only fork this screen has:

- **18+** → proceeds to account creation, triggers [Email verification](email-verification.md).
- **Under 18, any age** → redirects to [Registration blocked — under 18](registration-blocked-under-13.md). No account is created, no data from this form is retained beyond what FR-AUTH-04 already requires for the blocked-attempt record.

## Role Variations

None — public only.

## Contrast and RTL

Standard form contrast, 4.5:1 minimum (NFR-12). Full RTL mirroring for Arabic and Urdu (FR-LOC-04): field order, label alignment, and the locale selector itself all mirror.
