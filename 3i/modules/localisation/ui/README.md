---
project: 3i
module: localisation
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-LCL-UI-000
derived_from:
  - requirements/loc-localisation.md
tags:
  - ui
  - matrix
---

# Localisation — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Admin** | The platform's single Admin role — all translation management and sign-off happens here |

---

## Matrix

| Screen | Admin |
| :---- | :---: |
| [Admin translation management](screens/admin-translation-management.md) | ● |
| [Exempt string sign-off](screens/exempt-string-signoff.md) | ● |

Two screens — the smallest UI stage in the project. **No public-facing screen exists here** — the locale switcher visitors actually use is a small, shared piece of global chrome (see [components.md](components.md#locale-switcher)), not a dedicated screen this module documents on its own.

---

## Shared

| Document | Covers |
| :---- | :---- |
| [components.md](components.md) | Locale Switcher, Translation Status Indicator |
| [validation-rules.md](validation-rules.md) | Sign-off requirement gating an exempt string's visibility |

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| Human sign-off for the five exempt strings, per language — §22.2 dependency 9, outstanding | Actual visibility of those five strings in each language until sign-off lands. Does not block this module's own specification or tooling |