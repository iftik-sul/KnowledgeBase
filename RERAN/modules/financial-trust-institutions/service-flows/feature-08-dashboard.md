---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/screens/dashboard.md"
  - "RERAN/modules/financial-trust-institutions/navigation.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - dashboard
---

# Feature #8 – Dashboard

**Feature Category:** Shared Platform Features – General Platform

## 1. Feature Overview

The **Dashboard** is the single landing screen every institution user reaches on login: institution-wide KPIs, a prioritized list of applications needing action, quick actions, and condensed Focus Area summaries for Applications, Escrow & Trust Accounts, Compliance, and Institution Standing — each linking to its own full feature rather than duplicating it.

## 2. Purpose

Give any institution user one view of the institution's work in flight across every Group C function — service requests, internal certification, escrow assessment, trust account maintenance, compliance reporting — with quick access to start something new.

## 3. Description

The screen is identical for all four roles; nothing is gated or reshaped by who's looking at it. KPI cards (Draft Applications, Pending Internal Certification, With RERA, Completed This Month, Escrow Requests Awaiting Assessment, Approval Expiry) are institution-wide totals, each navigating to the relevant filtered list on selection. Applications Requiring Action is a short, prioritized list of records with something waiting on a user — pending certification, an information request, or a return — not a duplicate of the full Applications table. Focus Areas condense each of Features #2–#7's own summary cards without re-deriving them independently — every figure here must match its source screen exactly. An Institution-Wide Activity feed closes the screen, showing recent activity across the institution with acting user and role attribution, not filtered to the viewer's own actions.

## 4. Used By

Not tied to any single numbered service or feature — an aggregation layer over Features #1–#7.

## 5. Prerequisites

* User is logged into a verified institution account.

## 6. Required Information

None to view — the dashboard renders on login with no input required.

## 7. Required Documents

None.

## 8. Service Fee

No fee.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Any of the institution's four Group C roles** — identical screen, no role-based variant. **Reworked 2026-08-15**: previously four structurally different dashboards, one per role, plus a `certify`-scope overlay; replaced entirely by one unified screen.

## 11. Expected Processing Time

Immediate — real-time aggregation of Features #2–#7's own data.

## 12. Processing Workflow

Login
↓
Dashboard Renders (KPIs, Quick Actions, Applications Requiring Action, Focus Areas, Activity Feed)
↓
User Selects a KPI Card, Quick Action, Focus Area Link, or Activity Feed Row
↓
Navigates to the Relevant Feature, Filtered Where Applicable

## 13. Application Status Flow

Not applicable — this feature has no status of its own; it displays statuses owned by Features #2–#7.

## 14. Possible Outcomes

* Dashboard Renders with Items Requiring Action
* Dashboard Renders with Nothing Requiring Action *(Applications Requiring Action section empty; rest of screen still renders — Focus Areas and Activity Feed remain meaningful regardless)*

## 15. Output

No document or record is produced by this feature — it is a read-only aggregation and navigation layer.

## 16. Related Features

* Service Requests, Applications, Internal Certification Queue, Escrow Request Queue, Trust Accounts, Compliance Reports, Institution Profile — every Focus Area links to one of these; this feature has no independent data source.

## 17. UI Screens

* Dashboard

## 18. API Requirements

* Retrieve Institution-Wide KPIs
* Retrieve Applications Requiring Action
* Retrieve Focus Area Summaries (Applications, Escrow & Trust Accounts, Compliance, Institution Standing)
* Retrieve Institution-Wide Activity Feed

## 19. Database Entities

None of its own — reads from Application, Escrow Request, Trust Account, Compliance Report, Finding, and Institution entities owned by other features.

## 20. Acceptance Criteria

* Every institution user sees an identical dashboard, regardless of role.
* No card, action, or Focus Area is gated by role.
* Every Focus Area figure matches its source feature's own figures exactly — no independent aggregation logic that could drift.
* Applications Requiring Action shows only records with something genuinely waiting on a user; empty when there's nothing to act on, without rendering a placeholder card.
* The Activity Feed is institution-wide, not filtered to the viewer, with acting-user and role attribution on every row.

## 21. Business Rules

1. This screen is identical for all four Group C roles — no per-role variant.
2. Every Focus Area figure must match its source screen exactly; this feature has no independent data source.
3. Approval Expiry uses the same neutral/warning/error thresholds (60/14 days) as Institution Profile, defined once and read from the same setting.
4. Applications Requiring Action renders only when something is genuinely waiting — empty state applies to that section specifically, not the whole screen.

## Open Questions

1. Exact thresholds for what counts as "nearest" or "oldest" in Focus Area summaries, and how many rows a summary shows before linking out, are reasonable defaults, not sourced.
2. `services-overview.md` To Confirm item 2 remains open and covers this feature too.
