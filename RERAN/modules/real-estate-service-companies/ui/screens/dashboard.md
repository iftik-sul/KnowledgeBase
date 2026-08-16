---
project: RERAN
module: real-estate-service-companies
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/services-overview.md"
  - "RERAN/modules/real-estate-service-companies/roles-and-responsibilities.md"
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
tags:
  - real-estate-service-companies
  - ui-spec
  - dashboard
---

# Screen: Dashboard

**Access:** Any of the company's four Group D roles — identical screen for every user, no role-based variant. Built this way from the start, matching where Groups B and C ended up after correcting an earlier role-scoped design — not repeated here.

## Purpose

Give any company user, on login, a single view of work in flight across every function Group D performs — JOP administration, licensing, rental, transaction, and dispute — with quick access to start something new.

## Layout

```
Top Bar
↓
Company Context Header
↓
KPI Summary Cards
↓
Quick Actions
↓
Applications Requiring Action
↓
Focus Areas (JOP · Licensing · Rental · Transaction · Dispute)
↓
Company-Wide Activity
```

## Sections

### Section 1 — Company Context Header

Company licence status badge and expiry countdown (mirroring Financial & Trust Institutions' Institution Context Header pattern, since Service #12 plays the same institutional-standing role that module's Service #1 does). **Proposed** — the specific renewal/expiry mechanics for Group D's licence are not sourced beyond the licence application itself; see `service-flows/service-12-real-estate-licensing-application.md`'s own Open Questions.

### Section 2 — KPI Summary Cards

| KPI | Description |
| :---- | :---- |
| Draft Applications | Started, not submitted, company-wide |
| With RERA | Submitted, under review, or information requested |
| Completed This Month | Settled and issued |
| JOP Properties Under Supervision | Count of properties with an active Service #1 registration |
| Practice Cards Active | Count of agents holding a current card |

Selecting a card navigates to the relevant filtered list.

### Section 3 — Quick Actions

* **New Service Request** — opens [Services Catalog](services-catalog.md)
* **View Applications** — company-wide list
* **Register JOP Property** — shortcut into Service #1
* **View JOP Register** — opens [Jointly Owned Property](jointly-owned-property.md)

All four actions are available to every user. None is conditional on role.

### Section 4 — Applications Requiring Action

A short, prioritized list — not the full Applications table — of records where something is waiting on a company user: an information request from RERA, or a return needing correction. Empty when there's nothing to act on, and doesn't render a placeholder card in that case.

**No "pending internal certification" row type exists here**, unlike Financial & Trust Institutions' equivalent section — Group D has no internal certification gate anywhere (`open-questions.md` A5).

### Section 5 — Focus Areas

**Jointly Owned Property**

* Properties under supervision, escrow-adjacent requests in flight, pending auditor appointments.
* Links to [Jointly Owned Property](jointly-owned-property.md).

**Licensing**

* Company licence status, active permits, practice cards by status (active / expiring / cancelled).
* Links to [Applications](applications.md), filtered to Licensing services.

**Rental**

* Active management contracts, tenancy-system users registered.
* Links to [Applications](applications.md), filtered to Rental services.

**Transaction**

* Active auction permits, registered auction sales.
* Links to [Applications](applications.md), filtered to Transaction services.

**Dispute**

* Open primary suits, pending execution cases.
* Links to [Applications](applications.md), filtered to Dispute services.

Every Focus Area is visible to every user, regardless of role. Nothing enforces a role-specific view.

### Section 6 — Company-Wide Activity

A compact activity feed: submissions, RERA decisions, JOP registrations, card issuances, and dispute filings across the company, most recent first, latest 10. Organization-wide, not filtered to the viewer's own actions, matching the audit-trail-attribution model. Every row shows who performed the action and what role they held at the time.

## Empty State

**Message**

> Welcome to the RERA Real Estate Service Companies Portal. Your company is ready to begin managing jointly-owned property, licensing, rental, and dispute activities.

**Primary Button** — Register JOP Property
**Secondary Button** — View Company Profile

## Reused Components

See `ui/components.md` (Phase 5) for definitions of every component used on this screen — Company Operations Sidebar, Top Bar, Company Context Header, KPI Summary Cards, Quick Action Cards, Status Badge, Buttons.

## Validation

1. No card, action, or Focus Area on this screen is role-gated.
2. Every Focus Area figure must match its source screen's own figures exactly — this dashboard has no independent data source.
3. Status vocabulary comes from `ui/status-badges.md` (Phase 5); this screen defines no status of its own.

## User Flow

```
Login
↓
Dashboard
├─ New Service Request → Services Catalog
├─ KPI Card / Focus Area link → filtered list screen
├─ Applications Requiring Action row → Application Details
└─ Activity Feed row → the record it concerns
```

## Notes

* **Service #18 does not appear anywhere on this dashboard**, consistent with `navigation.md`'s provenance note — no Evaluation Certificate KPI, Focus Area, or Quick Action exists here pending resolution of whether the service belongs to this module at all.
* JOP's own Focus Area intentionally links out to a dedicated screen rather than the generic Applications list, matching `navigation.md`'s reasoning for giving JOP its own sidebar item.
