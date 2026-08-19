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

**Per [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md):** the standalone 13–17 registration screen is removed. No learner under 18 has an independent login of any kind — every minor reaches the platform as a profile under a verified adult account.

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
| [Registration blocked — under 18](screens/registration-blocked-under-13.md) | ● | | | |
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

**Fourteen screens**, down from fifteen — the standalone-teen registration screen ([formerly 3I-IDA-UI-002](/3i/decisions/dec-023-no-standalone-accounts-under-18.md)) is removed, not merely deprecated, since it has no successor and no reason to exist under the current model. No role management screen — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md) confirms role assignment is a database operation at launch, not a UI.

---

## Screens Deliberately Not Documented

**Ageing-up at 13** has no screen anywhere in this index. [3I-DEC-008](/3i/decisions/dec-008-ageing-up-at-13.md) is deferred pending a change request under §21.3. **This item's relevance has changed since it was first raised** — it originally asked whether a 13-year-old *profile* should be offered a *standalone* account. Under [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md), standalone accounts under 18 no longer exist at all, so DEC-008 as originally framed cannot be built even if approved. It should be re-raised as a question about ageing up at 18, not 13, or retired outright — flagged in [open-questions.md](/3i/open-questions.md).

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
| None currently. | The last open item, PIN attempt rate limiting, was resolved by [3I-DEC-022](/3i/decisions/dec-022-pin-lockout-and-dob-correction-notification.md) |
