---
project: 3i
module: platform
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-PLT-UI-000
derived_from:
  - requirements/plt-non-functional-requirements.md
tags:
  - ui
  - matrix
---

# Platform — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Admin** | The only role touching this module's one screen |

---

## Matrix

| Screen | Admin |
| :---- | :---: |
| [Admin audit log](screens/admin-audit-log.md) | ● |

One screen. **This module is deliberately UI-thin** — most NFRs are system properties (uptime, encryption, response times), not screens. There is no "system health dashboard" or similar invented here, since nothing in the baseline calls for one; NFR-05's monitoring and alerting (Sentry, uptime checks) are operational tooling outside the application itself, not an in-app screen this module documents.

---

## Shared

| Document | Covers |
| :---- | :---- |
| [validation-rules.md](validation-rules.md) | Audit log immutability |

No `components.md` — one screen has nothing to share with.

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| None. | |