---
project: 3i
module: reporting
type: overview
status: current
updated: 2026-08-23
id: 3I-RPT-OVW-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - module
  - overview
---

# Reporting

The module that reads across almost every other module to produce eleven fixed report types, exports them in three formats, and delivers a subset of them on a recurring schedule — without ever blocking the admin UI while a large export runs.

**Module status: complete.** README, data model, requirements, and the full UI stage are written.

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| REP | Reports and exports | 5 |

Five baseline requirements. No existing decisions touch REP — a clean scaffold, like `catalogue` and `public-site` before it. This is the **broadest reader in the project**: eleven report types, each pulling from a different combination of already-built modules, and every single one of those modules already exists. Nothing here is forward-referenced.

## Admin-Only, Not a Member-Facing Module

Every report type in FR-REP-01 — revenue, subscription churn, moderation actions, instructor activity — is administrative and sensitive by nature. This module has no Member or Instructor-facing screens at all; access is Admin only, throughout.

## Eleven Fixed Report Types, Not a Report Builder

Same shape as `catalogue`'s Category list and `public-site`'s fixed Page set: FR-REP-01 names exactly eleven report types — learner activity, course performance, enrolment, attendance, exam results, certificates issued, revenue (gross), subscription and churn, waivers granted, moderation and reports handled, instructor activity — and this module has no "create a new report type" action. An admin picks one of the eleven, applies filters (date range, course, etc.), and exports; there is no ad-hoc query builder.

## On-Demand Exports and Scheduled Reports Are Different Delivery Paths

Easy to conflate, worth stating precisely: an **on-demand export** (FR-REP-02, FR-REP-04) is admin-requested, runs as a background job, and the admin downloads it from the UI once ready. A **scheduled report** (FR-REP-03) is a recurring job that emails the finished file directly to nominated recipients — who may not even hold a platform Account at all (an external accountant, for instance). Scheduled delivery **does not route through `communication`'s Notification/category-preference system** — there's no account to check an opt-out preference against for a recipient who isn't one, so this module sends that email directly, reusing the same AWS SES infrastructure `communication` already established (FR-NOT-07) without going through its category-based routing.

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-RPT-DM-001 | current |
| [requirements/rep-reports-and-exports.md](requirements/rep-reports-and-exports.md) | 3I-RPT-REQ-001 | current |
| [ui/README.md](ui/README.md) | 3I-RPT-UI-000 | current — 2 screens, matrix, components, validation rules |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| GST recorded separately on invoices, specifically so revenue reporting can read it | `commerce` (FR-BILL-08) |
| Email delivery infrastructure this module's scheduled-report path reuses | `communication` (FR-NOT-07) |

## Delivery

Phase 7, Surface (§21.1) — CMS, blog, SEO, reports, exports, admin panel. This module is the reports/exports two-thirds of that phase; `public-site` (already built) is the CMS/blog/SEO third.

## Forward References

None. Every module this module reads from — `identity-and-access`, `catalogue`, `materials`, `learning-delivery`, `assessment`, `certification`, `commerce`, `communication`, `instructors` — already exists.

## Open Against This Module

None.

## Change Requests Owed to the Client

None. Nothing in this module amends or reverses the baseline.