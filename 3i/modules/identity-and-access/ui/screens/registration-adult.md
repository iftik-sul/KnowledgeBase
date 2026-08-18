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

---

## Purpose

The registration form for a date of birth resolving to 18+. The default path — no guardian fields, no block.

## Fields

First name, last name, email, password, date of birth, locale (FR-AUTH-01). See [validation-rules.md](../validation-rules.md) for field-level rules.

Social login (Google, Apple) offered as an alternative entry point — selecting it skips password entry but still requires date of birth on first login, routing to [Social login — DOB capture](social-login-dob-capture.md) rather than this form directly.

## Behaviour

Date of birth is evaluated on submit, before any other field is validated further, since it determines which of the three registration paths the person is actually on. An 18+ result proceeds to account creation and triggers [Email verification](email-verification.md); a 13–17 result redirects to [Registration — 13–17 standalone](registration-standalone-teen.md) rather than continuing on this screen; an under-13 result redirects to [Registration blocked — under 13](registration-blocked-under-13.md).

## Role Variations

None — public only.

## Contrast and RTL

Standard form contrast, 4.5:1 minimum (NFR-12). Full RTL mirroring for Arabic and Urdu (FR-LOC-04): field order, label alignment, and the locale selector itself all mirror.
