---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-24
id: 3I-IDA-UI-018
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - authentication
  - account
figma: null
---

# Screen: Login & Security

Satisfies: FR-AUTH-06 (email change path), FR-AUTH-08 (password change)

---

## Purpose

Where a Member, Instructor, or Admin updates their own email or password. Reached from [Account Settings](account-settings.md). Introduced by [3I-DEC-032](/3i/decisions/dec-032-account-settings-hub.md) — the underlying rule for email changes was already settled in the requirements ("Email changes require re-verification," [`auth-registration-and-authentication.md`](../requirements/auth-registration-and-authentication.md#email-changes-require-re-verification)) but had no screen to live on.

## Content

Two sections on one screen:

**Change email.** Current email shown, read-only. A "Change email" action opens a form: new email, current password (to confirm identity before changing a credential). On submit, this triggers the same mandatory-verification path as registration (FR-AUTH-06) — routes to [Email verification](email-verification.md), framed as "confirm your new email" per that screen's existing email-change behaviour. **The account's prior verified state and full access are preserved until the new address confirms** — this does not drop the account to a blocked state mid-change, consistent with what `email-verification.md` already specifies.

**Change password.** Current password, new password, confirm new password. Same policy as registration (FR-AUTH-08): 10 characters minimum, no forced composition rules, checked against the Have I Been Pwned corpus via k-anonymity. No strength meter, matching [Registration — Adult](registration-adult.md)'s existing treatment of the same field.

## Behaviour

Both actions require the **current password** to confirm identity before changing a credential — this is not the same requirement as [Password reset](password-reset.md), which exists specifically for someone who has lost their password. A Member who still has their password uses this screen instead of the reset flow.

A successful password change does **not** require re-verifying email — the two credentials are independent; only an email change re-triggers verification.

## Role Variations

Any authenticated role — Member, Instructor, Admin all manage their own login credentials identically. No role-specific behaviour.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
