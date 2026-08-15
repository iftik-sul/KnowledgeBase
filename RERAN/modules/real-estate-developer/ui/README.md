---
project: RERAN
module: real-estate-developer
type: overview
status: current
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

19 distinct screens, each documented once and identical for every user. The source material documented 49 role-scoped screen instances — the same 7 screens repeated for every role. Those per-role designs have been retired and rebuilt into 19 unified screens.

> **Corrected and rebuilt 2026-08-15 (issue #58).** Reconciled against two client decisions: the unified-access model (no role or permission-scope gating; role is audit-trail attribution only) and the corrected payment model (RERA service fees are paid per transaction through the shared platform payment gateway; no standing or pre-funded fee account). The Role × Screen Matrix is removed and the role-filtered sidebars replaced by one shared sidebar. **The 15 multi-variant screens have since been rebuilt as unified screens** — the per-role designs are retired, not merged in place. See [Per-Role Content Variants — Resolved](#per-role-content-variants--resolved).

## Screen Access

**Every screen in this package is reachable and actionable by all four Group B roles** — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison. There is no permission-scope gating, no role-filtered sidebar, and no read-only variant assigned to a role.

The **Role × Screen Matrix** this document previously carried is removed rather than rewritten to all-✓. Under the unified model it would be four identical `✓` columns on every row, which says nothing the screen list below doesn't. It previously read 16 / 12 / 9 / 12 screens per role, barring the Sales & Disclosure Officer from Documents, Projects, Property Registrations and all four escrow screens; the Registration Officer from every escrow and sales screen; and every role but the Principal from Company Profile. All of that is retired.

### Screen Index

| Screen | Screen |
| :---- | :---- |
| [dashboard.md](screens/dashboard.md) | [applications.md](screens/applications.md) |
| [application-details.md](screens/application-details.md) | [documents.md](screens/documents.md) |
| [document-details.md](screens/document-details.md) | [reports.md](screens/reports.md) |
| [notifications.md](screens/notifications.md) | [help-and-support.md](screens/help-and-support.md) |
| [projects.md](screens/projects.md) | [project-details.md](screens/project-details.md) |
| [property-registrations.md](screens/property-registrations.md) | [property-registration-details.md](screens/property-registration-details.md) |
| [sales-and-disclosures.md](screens/sales-and-disclosures.md) | [sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md) |
| [escrow-management.md](screens/escrow-management.md) | [escrow-details.md](screens/escrow-details.md) |
| [fund-release-request.md](screens/fund-release-request.md) | [fund-release-request-details.md](screens/fund-release-request-details.md) |
| [company-profile.md](screens/company-profile.md) | |

**Resolved:** the open question this section used to carry — the Role Permission Matrix granting the Sales & Disclosure Officer Documents access that no Documents list screen provided — is answered by the unified model. The misplaced source fragment was merged into [documents.md](screens/documents.md); see [../README.md](../README.md#open-questions).

## Per-Role Content Variants — Resolved

**Resolved 2026-08-15 by client decision: the variants are retired and the screens rebuilt as unified screens.**

This section previously flagged an open question. Measured across the 19 files, the `## Role Variations` sections occupied ~95% of every screen that had one, and each block was a complete screen definition — different KPI sets, filters, columns, row actions, empty states and, on `reports.md`, four entirely separate report catalogues. Those were genuinely structural differences, so the earlier pass removed the access gating but deliberately left the variant content untouched rather than deciding unilaterally which variant was correct.

The client has since decided. **All 15 multi-variant screens have been rebuilt**, following the technique used for Group C's [`dashboard.md`](../../financial-trust-institutions/ui/screens/dashboard.md) rework: identify what is genuinely load-bearing in each variant, fold it into one screen organized **by function rather than by role**, and reconcile explicitly wherever two variants defined the same thing differently.

| Screen | Variants | Lines before | Lines after |
| :---- | :---: | :---: | :---: |
| [reports.md](screens/reports.md) | 4 | 1245 | 184 |
| [document-details.md](screens/document-details.md) | 4 | 1245 | 149 |
| [application-details.md](screens/application-details.md) | 4 | 1170 | 155 |
| [help-and-support.md](screens/help-and-support.md) | 4 | 1132 | 164 |
| [documents.md](screens/documents.md) | 4 | 1022 | 258 |
| [applications.md](screens/applications.md) | 4 | 1018 | 191 |
| [dashboard.md](screens/dashboard.md) | 4 | 997 | 238 |
| [notifications.md](screens/notifications.md) | 4 | 984 | 188 |
| [escrow-details.md](screens/escrow-details.md) | 2 | 601 | 165 |
| [sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md) | 2 | 597 | 168 |
| [project-details.md](screens/project-details.md) | 2 | 529 | 162 |
| [sales-and-disclosures.md](screens/sales-and-disclosures.md) | 2 | 460 | 192 |
| [property-registrations.md](screens/property-registrations.md) | 2 | 451 | 191 |
| [escrow-management.md](screens/escrow-management.md) | 2 | 446 | 209 |
| [projects.md](screens/projects.md) | 2 | 372 | 186 |

The four screens that never had variants — [company-profile.md](screens/company-profile.md), [fund-release-request.md](screens/fund-release-request.md), [fund-release-request-details.md](screens/fund-release-request-details.md), [property-registration-details.md](screens/property-registration-details.md) — needed no rebuild.

### The technique

Not "pick one variant," and not "paste all variants together." For each screen:

1. **Identify what is load-bearing in each variant.** A KPI, section or action representing real distinct work is kept, whichever variant it came from and even when only one variant had it.
2. **Fold it into one screen, organized by function.** Focus Areas on the Dashboard; grouped taxonomies on Documents and Notifications; report categories by subject on Reports. Never a section per role.
3. **Reconcile conflicts explicitly, in each screen's `## Notes`.** Where two variants defined the same thing differently, the resolution and its reasoning are recorded rather than silently applied.

### What this preserved that a naive merge would have lost

The executive variants were the only source of most analytics — Portfolio Insights, Registration Insights, Sales Analytics, Escrow Analytics, Document Analytics, Application Analytics, Executive Insights, Fund Release Overview. The operational variants explicitly framed themselves as emphasizing "actionable work rather than analytics," so basing each merge on an operational variant would have deleted all of it. Conversely the operational variants were the only source of status-driven row actions, bulk actions, validation summaries, required-document checklists and detailed filtering.

Three taxonomies were **unioned rather than chosen between**, because the variants overlapped on general entries and diverged completely on domain ones: **document categories** (sales agreements and buyer identification existed only in the sales variant; engineer certificates and quantity surveyor reports only in the escrow variant), **notification types**, and **report catalogues**.

### Conflicts resolved, and where

| Conflict | Resolution | Recorded in |
| :---- | :---- | :---- |
| Project Status — 6-state vs 8-state, not subsettable | 9-state union; "Pending Review" merged into "Under Review"; "Suspended" kept though single-sourced | [status-badges.md](status-badges.md#project-status) |
| Property Registration Status — 6 vs 7 states | 7-state union (clean subset) | [status-badges.md](status-badges.md#property-registration-status) |
| Document upload checks — 5 vs 6, differing wording | 6 checks; wording variants merged; "Required document linked" kept and scoped, with one flag | [validation-rules.md](validation-rules.md#document-upload-rules) |
| `escrow-details.md` — linear 10-section page vs 5-tab workspace | Tabs, with reasoning recorded and the decision flagged as reversible | [escrow-details.md](screens/escrow-details.md#notes) |
| "Active Projects" — all ongoing vs assigned to you | Organization-wide | [dashboard.md](screens/dashboard.md#notes) |
| "Escrow Balance" vs "Available Balance" | Escrow Balance, **flagged** if "available" is meant net of pending releases | [escrow-management.md](screens/escrow-management.md#notes) |
| Notifications — card list vs table | Table, matching every other list screen | [notifications.md](screens/notifications.md#notes) |
| Component names — Document Viewer, Version History, Analytics, Notification, File Upload | Resolved to the majority or more descriptive name | [components.md](components.md) |

Two questions are deliberately **still open**: whether "Task Cards" and "Task List" were meant as distinct visual patterns ([components.md](components.md)), and the three unreconciled document-status vocabularies in [status-badges.md](status-badges.md#document-status) — the latter predates the role variants and is a source-clarification question, not a merge decision.

## Escrow Content Is Out Of Scope For The Payment Correction

The escrow screens show balances, milestone schedules and fund-release amounts. Those belong to the developer's **project escrow account** — a regulated holding account, and a real product feature — not to any RERA-fee account. The move to per-transaction gateway payment for RERA's service fees does not touch them. See the note at the top of [escrow-management.md](screens/escrow-management.md).

## Shared Documentation

These are documented once and linked from screen files, never repeated per screen.

* [components.md](components.md) — shared component library.
* [validation-rules.md](validation-rules.md) — validation patterns used by form screens.
* [status-badges.md](status-badges.md) — status vocabulary and colour coding.

## Screen File Template

Every screen file follows the same section order:

```
## Purpose
## Layout
## Sections
## Empty State
## Reused Components     — links into components.md
## Validation            — links into validation-rules.md (form screens only)
## User Flow             — adjacent screens, in and out
## Notes                 — reconciliations, what was retired, what stays open
```

**Changed 2026-08-15:** `## Role Variations` is gone from the template. It described per-role screen designs, which no longer exist. Where a rebuilt screen absorbed content from a retired variant, that is recorded inline against the section and summarized in `## Notes`.
