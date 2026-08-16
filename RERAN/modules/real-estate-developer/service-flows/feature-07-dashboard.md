---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/dashboard.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
tags:
  - real-estate-developer
  - shared-feature
  - dashboard
---

# Feature #7 – Dashboard

**Feature Category:** Shared Platform Features – General Platform

## 1. Feature Overview

The **Dashboard** is the single landing screen every developer user reaches on login: organization-wide KPIs spanning every Group B function, a prioritized cross-function "Requiring Action" list, Quick Actions, and condensed Focus Area summaries for Projects & Registrations, Sales & Disclosures, Escrow & Fund Releases, and Compliance & Standing — each linking to its own domain workspace rather than duplicating it.

## 2. Purpose

Give any developer user one view of the organization's work in flight across every function — project registration, property registration, sales and disclosures, escrow and fund releases, and regulatory compliance — with quick access to start something new.

## 3. Description

Rebuilt 2026-08-15 from four structurally different role dashboards into one, absorbing rather than choosing between them — KPIs are a deliberate superset, since every metric that represented real distinct work in any prior variant survives. The "Requiring Action" section replaces four separate work queues ("Projects Requiring Attention," "Sales Requiring Action," "Escrow Accounts Requiring Action," "Compliance & Alerts") with one cross-function list sorted by urgency. Three near-identical "RERA Requests" sections that appeared separately in three prior variants are consolidated into the Compliance & Standing Focus Area. Every Focus Area figure must match its source feature's own figures exactly — this feature has no independent data source.

## 4. Used By

Not tied to any single numbered service or feature — an aggregation layer over Features #1–#6.

## 5. Prerequisites

* User is logged into a registered developer company account.

## 6. Required Information

None to view — renders on login.

## 7. Required Documents

None.

## 8. Service Fee

No fee.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Any of the developer's four Group B roles** — identical screen, no role-based variant. Rebuilt 2026-08-15 from four role-specific designs into one, reorganized by function rather than by role.

## 11. Expected Processing Time

Immediate — real-time aggregation of Features #1–#6's own data.

## 12. Processing Workflow

Login
↓
Dashboard Renders (Welcome Banner, KPIs, Quick Actions, Requiring Action, Focus Areas, Upcoming Deadlines, Organization Activity)
↓
User Selects a Quick Action, KPI Card, Focus Area Link, Requiring Action Row, Deadline, or Activity Row
↓
Navigates to the Relevant Feature, Filtered Where Applicable

## 13. Application Status Flow

Not applicable — this feature has no status of its own; it displays statuses owned by Features #1–#6.

## 14. Possible Outcomes

* Dashboard Renders with Items Requiring Action
* Dashboard Renders with Nothing Requiring Action *(Requiring Action section empty; rest of screen still renders)*

## 15. Output

No document or record is produced — a read-only aggregation and navigation layer.

## 16. Related Features

* Applications, Projects, Property Registrations, Escrow Management, Fund Release Request, Sales & Disclosures — every Focus Area links to one of these; this feature has no independent data source.

## 17. UI Screens

* Dashboard

## 18. API Requirements

* Retrieve Organization-Wide KPIs
* Retrieve Requiring-Action List
* Retrieve Focus Area Summaries (Projects & Registrations, Sales & Disclosures, Escrow & Fund Releases, Compliance & Standing)
* Retrieve Upcoming Deadlines
* Retrieve Organization Activity Feed

## 19. Database Entities

None of its own — reads from Project, Property Registration, Property Sale, Sales Disclosure, Escrow Account, Fund Release, Application, and Document entities owned by other features.

## 20. Acceptance Criteria

* Every developer user sees an identical dashboard, regardless of role.
* No card, action, or Focus Area is gated by role.
* Every Focus Area figure matches its source feature's own figures exactly.
* Requiring Action shows only records with something genuinely waiting; empty when there's nothing to act on, without a placeholder card.
* Organization Activity is organization-wide, not filtered to the viewer, with acting-user and role attribution on every row.

## 21. Business Rules

1. This screen is identical for all four Group B roles — no per-role variant.
2. KPIs are a deliberate superset — nothing dropped for having originated in one prior role's dashboard, since all four roles now perform all four kinds of work.
3. Every Focus Area figure must match its source feature exactly; no independent aggregation logic.
4. Requiring Action renders only when something is genuinely waiting.

## Open Questions

1. The "Oldest Pending Release" card, the Create/Respond/Review grouping of Quick Actions, and how many rows a Focus Area summary shows before linking out are reasonable defaults, not sourced.
2. Same adoption question as Feature #1 — needs client confirmation.
