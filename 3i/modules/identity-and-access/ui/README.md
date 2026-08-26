---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-26
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

**The three admin-only screens in this module are paused — see [3I-DEC-033](/3i/decisions/dec-033-admin-instructor-surface-provisional.md).** No Figma design work should be produced against them until the admin/instructor portal's own design direction is set.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Public** | No session |
| **Member** | The renamed Account holder role — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md) |
| **Instructor** | |
| **Admin** | |
| **Mobile (Flutter)** | Not a role — a platform column marking which screens are in scope for the native app. See [mobile-scope.md](/3i/mobile-scope.md) |

---

## Matrix

| Screen | Public | Member | Instructor | Admin | Mobile |
| :---- | :---: | :---: | :---: | :---: | :---: |
| [Account type selector](screens/account-type-selector.md) | ● | | | | ● |
| [Registration — adult](screens/registration-adult.md) | ● | | | | ● |
| [Registration blocked — under 18](screens/registration-blocked-under-18.md) | ● | | | | ● |
| [Email verification](screens/email-verification.md) | ● | ● | ● | ● | ● |
| [Login](screens/login.md) | ● | | | | ● |
| [Social login — DOB capture](screens/social-login-dob-capture.md) | ● | | | | ● |
| [Password reset](screens/password-reset.md) | ● | | | | ● |
| [Profile picker](screens/profile-picker.md) | | ● | | | ● |
| [Account settings](screens/account-settings.md) | | ● | ● | ● | ● |
| [Login \& security](screens/login-security.md) | | ● | ● | ● | ● |
| [Profile create / edit](screens/profile-create-edit.md) | | ● | | | ● |
| [Guardian dashboard](screens/guardian-dashboard.md) | | ● | | | ● |
| [Profile deletion confirmation](screens/profile-deletion-confirmation.md) | | ● | | | ● |
| [Device management](screens/device-management.md) | | ● | ● | ● | ● |
| [Admin — profile name unlock](screens/admin-name-unlock.md) ⚠ paused | | | | ● | |
| [Admin — DOB correction](screens/admin-dob-correction.md) ⚠ paused | | | | ● | |
| [Admin — TOTP setup](screens/admin-totp-setup.md) ⚠ paused | | | | ● | |

Seventeen screens, fourteen in scope for mobile — see [mobile-scope.md](/3i/mobile-scope.md#2-scope-by-module) for the reasoning. No role management screen — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md) confirms role assignment is a database operation at launch, not a UI.

---

## Shared

| Document | Covers |
| :---- | :---- |
| [components.md](components.md) | The PIN pad, Account Menu, and elements reused across two or more screens |
| [validation-rules.md](validation-rules.md) | Field-level validation shared across registration and profile forms |

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| [3I-DEC-033](/3i/decisions/dec-033-admin-instructor-surface-provisional.md) | Figma design work on the three ⚠-marked admin screens above |
