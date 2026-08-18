---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-18
id: 3I-IDA-UI-000
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - matrix
---

# Identity and Access — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

**The learner profile is not a matrix column.** It does not log in and holds no permissions of its own — it is a **context** selected inside a Member's authenticated session, not a separate authenticated role. Screens that vary by which profile is active are marked accordingly rather than given a column.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Public** | No session |
| **Member** | The renamed Account holder role — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md) |
| **Instructor** | |
| **Admin** | |

---

## Matrix

| Screen | Public | Member | Instructor | Admin |
| :---- | :---: | :---: | :---: | :---: |
| [Registration — adult](screens/registration-adult.md) | ● | | | |
| [Registration — 13–17 standalone](screens/registration-standalone-teen.md) | ● | | | |
| [Registration blocked — under 13](screens/registration-blocked-under-13.md) | ● | | | |
| [Email verification](screens/email-verification.md) | ● | ● | ● | ● |
| [Login](screens/login.md) | ● | | | |
| [Social login — DOB capture](screens/social-login-dob-capture.md) | ● | | | |
| [Password reset](screens/password-reset.md) | ● | | | |
| [Profile picker](screens/profile-picker.md) | | ● | | |
| [Profile create / edit](screens/profile-create-edit.md) | | ● | | |
| [Guardian dashboard](screens/guardian-dashboard.md) | | ● | | |
| [Profile deletion confirmation](screens/profile-deletion-confirmation.md) | | ● | | |
| [Device management](screens/device-management.md) | | ● | | |
| [Admin — profile name unlock](screens/admin-name-unlock.md) | | | | ● |
| [Admin — DOB correction](screens/admin-dob-correction.md) | | | | ● |
| [Admin — TOTP setup](screens/admin-totp-setup.md) | | | | ● |

Fifteen screens. No role management screen — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md) confirms role assignment is a database operation at launch, not a UI.

---

## Screens Deliberately Not Documented

**Ageing-up at 13** has no screen anywhere in this index. [3I-DEC-008](/3i/decisions/dec-008-ageing-up-at-13.md) is deferred pending a change request under §21.3. Documenting a screen for unapproved scope would make it look built when it is not authorised — the no-op (a profile simply stays a profile past 13) requires no new screen at all.

---

## Shared

| Document | Covers |
| :---- | :---- |
| [components.md](components.md) | The PIN pad, and elements reused across two or more screens |
| [validation-rules.md](validation-rules.md) | Field-level validation shared across registration and profile forms |

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| [OQ-10](/3i/open-questions.md#oq-10--pin-attempt-rate-limiting) | [Profile picker](screens/profile-picker.md) — lockout behaviour on repeated wrong PINs is not yet specified. The screen is documented with the gap named rather than guessed at |
