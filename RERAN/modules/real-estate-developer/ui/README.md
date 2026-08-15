---
project: RERAN
module: real-estate-developer
type: overview
status: draft
updated: 2026-08-15
derived_from:
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - real-estate-developer
  - ui-spec
  - index
---

# Real Estate Developer UI Specifications

19 distinct screens. The source material documents 49 role-scoped screen instances; the same 7 screens are repeated for every role. Each screen is documented once here, with the source's per-role differences captured inside the screen file under `## Role Variations`.

> **Corrected 2026-08-15 (issue #58).** Reconciled against two client decisions: the unified-access model (no role or permission-scope gating; role is audit-trail attribution only) and the corrected payment model (RERA service fees are paid per transaction through the shared platform payment gateway; no standing or pre-funded fee account). The Role × Screen Matrix is removed, the role-filtered sidebars inside every screen file are replaced by the one shared sidebar, and each `## Role Variations` section is reframed as content variants rather than access restrictions.

## Screen Access

**Every screen in this package is reachable and actionable by all four Group B roles** — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison. There is no permission-scope gating, no role-filtered sidebar, and no read-only variant assigned to a role.

The **Role × Screen Matrix** this document previously carried is removed rather than rewritten to all-✓. Under the unified model it would be four identical `✓` columns on every row, which says nothing the screen list below doesn't. It previously read 16 / 12 / 9 / 12 screens per role, barring the Sales & Disclosure Officer from Documents, Projects, Property Registrations and all four escrow screens; the Registration Officer from every escrow and sales screen; and every role but the Principal from Company Profile. All of that is retired.

| Screen | |
| :---- | :---- |
| [dashboard.md](screens/dashboard.md) | [applications.md](screens/applications.md) |
| [application-details.md](screens/application-details.md) | [document-details.md](screens/document-details.md) |
| [documents.md](screens/documents.md) | [document-details.md](screens/document-details.md) | 1245 | 1188 | 4 |
| [reports.md](screens/reports.md) | 1245 | 1189 | 4 |
| [application-details.md](screens/application-details.md) | 1170 | 1107 | 4 |
| [help-and-support.md](screens/help-and-support.md) | 1132 | 1076 | 4 |
| [documents.md](screens/documents.md) | 1022 | 964 | 4 |
| [applications.md](screens/applications.md) | 1018 | 962 | 4 |
| [dashboard.md](screens/dashboard.md) | 997 | 943 | 4 |
| [notifications.md](screens/notifications.md) | 984 | 928 | 4 |
| [escrow-details.md](screens/escrow-details.md) | 601 | 545 | 2 |
| [sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md) | 597 | 539 | 2 |
| [project-details.md](screens/project-details.md) | 529 | 471 | 2 |
| [sales-and-disclosures.md](screens/sales-and-disclosures.md) | 460 | 404 | 2 |
| [property-registrations.md](screens/property-registrations.md) | 451 | 395 | 2 |
| [escrow-management.md](screens/escrow-management.md) | 446 | 386 | 2 |
| [projects.md](screens/projects.md) | 372 | 318 | 2 |

Each block is a **complete screen definition**, not a note about who may see what: different KPI card sets, different filter lists, different table columns, different row actions, different empty-state messages and buttons, different analytics sections. `reports.md` defines four entirely different report catalogues. `help-and-support.md`'s Escrow Liaison variant has Training Resources and Quick Help Categories sections that no other variant has, while the other three have System Status and Feedback sections it lacks.

**These are genuinely structural differences, not visibility differences.** Removing the access gating does not tell us which variant is now *the* screen. Merging them means deciding, per screen, whether the correct result is one variant, the union of all of them, or a new consolidated design — a product decision with real consequences for what users see.

Following the same caution Group C's UI pass used, this pass **did not merge them**. What it did:

* Removed every access assertion — the `**Roles:**` gate line at the top of all 19 files, the 49 role-filtered sidebar menus, and the role-based read-only claims.
* Reframed each `## Role Variations` section so the role headings read as *"the variant the source defined under this heading"* rather than *"what this role may see."*
* Left the variant content itself verbatim, pending the decision above.

Status-based read-only rules ("fields become read-only after submission", "approved fund releases cannot be modified") are untouched — those are lifecycle rules, not permissions.

The four screens with no Role Variations section — [company-profile.md](screens/company-profile.md), [fund-release-request.md](screens/fund-release-request.md), [fund-release-request-details.md](screens/fund-release-request-details.md), [property-registration-details.md](screens/property-registration-details.md) — need no decision; the source defined a single variant for each, and they are now reachable by everyone.

## Escrow Content Is Out Of Scope For The Payment Correction

The escrow screens show balances, milestone schedules and fund-release amounts. Those belong to the developer's **project escrow account** — a regulated holding account, and a real product feature — not to any RERA-fee account. The move to per-transaction gateway payment for RERA's service fees does not touch them. See the note at the top of [escrow-management.md](screens/escrow-management.md).

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
## Role Variations       — content variants the source defined per role heading (not access)
## User Flow             — adjacent screens, in and out
## Notes
```
