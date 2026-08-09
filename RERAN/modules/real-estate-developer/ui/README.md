---
project: RERAN
module: real-estate-developer
type: overview
status: draft
updated: 2026-08-09
derived_from:
  - "RERAN/modules/real-estate-developer/ui-design/RERAN_real_estate_developer_ui.md"
tags:
  - real-estate-developer
  - ui-spec
  - index
---

# Real Estate Developer UI Specifications

19 distinct screens across 4 roles. The source material documents 49 role-scoped screen instances; the same 7 screens are repeated for every role. Each screen is documented once here, with role differences captured inside the screen file under `## Role Variations`.

## Role × Screen Matrix

P = Developer Principal / Director · R = Project Registration Officer · S = Sales & Disclosure Officer · E = Escrow Liaison

| Screen | P | R | S | E |
| :---- | :---: | :---: | :---: | :---: |
| [dashboard.md](screens/dashboard.md) | ✓ | ✓ | ✓ | ✓ |
| [applications.md](screens/applications.md) | ✓ | ✓ | ✓ | ✓ |
| [application-details.md](screens/application-details.md) | ✓ | ✓ | ✓ | ✓ |
| [document-details.md](screens/document-details.md) | ✓ | ✓ | ✓ | ✓ |
| [reports.md](screens/reports.md) | ✓ | ✓ | ✓ | ✓ |
| [notifications.md](screens/notifications.md) | ✓ | ✓ | ✓ | ✓ |
| [help-and-support.md](screens/help-and-support.md) | ✓ | ✓ | ✓ | ✓ |
| [documents.md](screens/documents.md) | ✓ | ✓ | — | ✓ |
| [projects.md](screens/projects.md) | ✓ | ✓ | — | — |
| [project-details.md](screens/project-details.md) | ✓ | ✓ | — | — |
| [property-registrations.md](screens/property-registrations.md) | ✓ | ✓ | — | — |
| [property-registration-details.md](screens/property-registration-details.md) | — | ✓ | — | — |
| [sales-and-disclosures.md](screens/sales-and-disclosures.md) | ✓ | — | ✓ | — |
| [sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md) | ✓ | — | ✓ | — |
| [escrow-management.md](screens/escrow-management.md) | ✓ | — | — | ✓ |
| [escrow-details.md](screens/escrow-details.md) | ✓ | — | — | ✓ |
| [fund-release-request.md](screens/fund-release-request.md) | — | — | — | ✓ |
| [fund-release-request-details.md](screens/fund-release-request-details.md) | — | — | — | ✓ |
| [company-profile.md](screens/company-profile.md) | ✓ | — | — | — |
| **Screens per role** | **16** | **12** | **9** | **12** |

> **Open question:** the Role Permission Matrix grants the Sales & Disclosure Officer full access to Documents, but the source file documents no Documents list screen for that role — only Document Details. The dash above records the source as written, not a confirmed decision.

## Shared Documentation

These are documented once and linked from screen files, never repeated per screen.

* [components.md](components.md) — shared component library.
* [validation-rules.md](validation-rules.md) — validation patterns used by form screens.
* [status-badges.md](status-badges.md) — status vocabulary and colour coding.

## Screen File Template

Every screen file follows the same section order, matching the template used throughout the source material:

```
## Purpose
## Layout
## Sections
## Empty State
## Reused Components     — links into components.md
## Validation            — links into validation-rules.md (form screens only)
## Role Variations       — how the screen differs per role
## User Flow             — adjacent screens, in and out
## Notes
```
