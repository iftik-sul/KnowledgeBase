---
project: 3i
module: certification
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CRT-UI-000
derived_from:
  - requirements/cert-certificates.md
tags:
  - ui
  - matrix
---

# Certification — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Public** | No session — the verification page requires none (FR-CERT-07) |
| **Member** | Viewing a profile's own issued certificates |
| **Admin** | |

---

## Matrix

| Screen | Public | Member | Admin |
| :---- | :---: | :---: | :---: |
| [Certificate detail / download](screens/certificate-detail-download.md) | | ● | |
| [Public verification page](screens/public-verification-page.md) | ● | | |
| [Admin certificate management](screens/admin-certificate-management.md) | | | ● |

Three screens. **No certificate-issuance screen exists** — issuance is automatic, triggered by eligibility being newly met (see [data-model.md](../data-model.md#when-eligibility-is-checked)); there is no learner-initiated "claim" action and no instructor-initiated "grant" action anywhere in the baseline.

---

## Shared

| Document | Covers |
| :---- | :---- |
| [components.md](components.md) | Certificate Card, Verification Status Badge |
| [validation-rules.md](validation-rules.md) | Revocation reason requirement, reissuance linkage |

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| Certificate design assets (template, seal, signature image) — §22.2 item 5, outstanding client dependency | The actual rendered PDF's visual layout. Does **not** block the verification page (a data lookup) or this module's own specification |