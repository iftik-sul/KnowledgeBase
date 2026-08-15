---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens-unified/README.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - dashboard
---

# Screen: Dashboard

**Access:** Any of the institution's four Group C roles — identical screen for every user, no role-based variant.

> **Reworked 2026-08-15.** This screen previously described four structurally different dashboards, one per role, plus a `certify`-scope overlay — the explicit defect an earlier pass (issue #27) had corrected everywhere else in the module except here. It is replaced entirely by the unified dashboard drafted in `ui/screens-unified/dashboard.md` (issue #50), reworked here to absorb the institution-wide summary content the four role dashboards used to split apart: application volume, escrow/trust account state, compliance obligations, and staff/institution standing. This is now the single canonical dashboard — `ui/screens-unified/dashboard.md` is retired, its content merged in below.

## Purpose

Give any institution user, on login, a single view of the institution's work in flight across every function Group C performs — service requests, internal certification, escrow assessment, trust account maintenance, and compliance reporting — with quick access to start something new. No section is gated or reshaped by which of the four roles is looking at it; what a user actually focuses on is a matter of their role in practice, not what the screen shows them.

## Layout

```
Top Bar
↓
Institution Context Header
↓
KPI Summary Cards
↓
Quick Actions
↓
Applications Requiring Action
↓
Focus Areas (Applications · Escrow & Trust Accounts · Compliance · Institution Standing)
↓
Institution-Wide Activity
```

## Sections

### Section 1 — KPI Summary Cards

Institution-wide totals, identical for every user.

| KPI | Description |
| :---- | :---- |
| Draft Applications | Started, not submitted, institution-wide |
| Pending Internal Certification | Awaiting certify-or-return, any of the four users may act |
| With RERA | Submitted, under review, or information requested |
| Completed This Month | Settled and issued |
| Escrow Requests Awaiting Assessment | Developer-originated, routed from Group B |
| Approval Expiry | Days remaining on the institution's own trustee/auditor standing (B8, confirmed 2026-08-15) |

Selecting a card navigates to the relevant list screen, filtered accordingly.

### Section 2 — Quick Actions

* **New Service Request** — opens [Services Catalog](../screens-unified/services-catalog.md)
* **View Applications** — institution-wide list
* **Internal Certification Queue** — if anything is waiting
* **Escrow Requests** — if anything is waiting

All four actions are available to every user. None is conditional on role.

### Section 3 — Applications Requiring Action

A short, prioritized list — not the full Applications table — of records where something is waiting on an institution user: pending internal certification, an information request from RERA, or a returned application needing correction. Each row shows the application reference, service, what's waiting, and how long it's been waiting. Empty when there's nothing to act on, and doesn't render a placeholder card in that case.

### Section 4 — Focus Areas

**Absorbed 2026-08-15** from the four retired role dashboards' most load-bearing sections — condensed summary cards for each function, each linking out to its own full screen rather than duplicating that screen's detail here.

**Applications**

* Institution-wide volume by status (Draft, Pending Certification, With RERA, Completed This Month) — the same figures as the KPI cards above, shown here as a small breakdown rather than repeated as separate cards.
* Links to [applications.md](applications.md).

**Escrow & Trust Accounts**

* Condensed escrow queue counts: Awaiting Assessment, Under Assessment, Breaching SLA — the three of [escrow-request-queue.md](escrow-request-queue.md#section-1--queue-summary-cards)'s six KPI cards that indicate outstanding work.
* **Oldest Awaiting Assessment** — the single request that has waited longest, as a call-to-action card, since the queue's failure mode is a request aging quietly, not a request being hard to find.
* Trust accounts summary: count under management, count with an overdue statement, count Flagged.
* Links to [escrow-request-queue.md](escrow-request-queue.md) and [trust-accounts.md](trust-accounts.md).

**Compliance**

* Reporting Obligations — the same banded card set as [compliance-reports.md](compliance-reports.md#section-1--reporting-obligations): Reports Due, Overdue, Accounts Statement Overdue.
* Open Findings — count and nearest-severity summary of unresolved findings against trust accounts.
* Links to [compliance-reports.md](compliance-reports.md).

**Institution Standing**

* Approval status and expiry countdown — the same figure as the KPI card above, shown here alongside staff roster size and count of staff invited but not yet active.
* Links to [institution-profile.md](institution-profile.md).

Every Focus Area is visible to every user, regardless of role. In practice, a given user will likely check the areas relevant to what they typically do — but nothing on this screen enforces that as a restriction, and there is no per-role variant of which Focus Areas render.

### Section 5 — Institution-Wide Activity

A compact activity feed: recent submissions, RERA decisions, certifications, escrow actions, and compliance filings across the institution, most recent first. Not filtered to the viewer's own actions — institution-wide, matching the audit-trail-attribution model (`navigation.md#audit-trail-principle`), where every row shows who did it and what role they held at the time.

## Empty State

**Message**

> Nothing needs your attention right now. Start a new service request, or check institution-wide activity below.

Applies to Section 3 only — the rest of the dashboard always renders, since Focus Area summaries and the activity feed remain meaningful even with nothing urgently pending.

## Reused Components

Institution Operations Sidebar, Top Bar, Institution Context Header, KPI Summary Cards, Status Badge, Buttons.

## Validation

1. No card, action, list item, or Focus Area on this screen is role-gated. What each user sees differs only by what work exists at the institution, never by who they are.
2. Approval Expiry follows the same neutral/warning/error thresholds (60 / 14 days) used on Institution Profile and the Institution Context Header — defined once, read from the same setting everywhere.
3. Every Focus Area figure must match its source screen's own figures exactly — this dashboard has no independent data source and must not drift from [applications.md](applications.md), [escrow-request-queue.md](escrow-request-queue.md), [trust-accounts.md](trust-accounts.md), or [compliance-reports.md](compliance-reports.md).

## Access

Identical for Mortgage Officer, Institution Relationship Manager, Account Trustee, and Auditing Bureau Officer. This is not four dashboards collapsed into shared sections — it is one screen, reachable and fully readable by any institution user regardless of role, matching the unified-access model this whole module now follows.

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

* **This absorbs, rather than references, the four retired role dashboards' content.** The old Mortgage Officer, Institution Relationship Manager, Account Trustee, and Auditing Bureau Officer sections are gone as separate variants; their most load-bearing pieces (work summary, institution volume, escrow/trust state, reporting obligations, staff/standing) are now Focus Area cards on one screen, visible to everyone.
* **The `certify`-scope Certification Queue overlay is retired along with the scope itself.** Internal Certification's KPI card and Quick Action serve the same purpose — visible to every user, not an overlay conditional on holding a scope that no longer exists.
* **The old Institution Relationship Manager section's "whichever is more urgent: renewal or settlement shortfall" landing-action logic is retired, not replaced with an equivalent.** There is no settlement shortfall concept left (`open-questions.md` B1, B11) — approval renewal urgency (the Approval Expiry KPI card) is what remains, and it applies to every user's view of this screen equally, not as a role-specific landing action.
* Exact thresholds for what counts as "nearest" or "oldest," and how many rows a Focus Area summary shows before linking out, remain **Proposed** — reasonable defaults, not sourced.
* This screen does not redesign escrow assessment, trust account maintenance, or compliance reporting themselves — those remain [escrow-request-queue.md](escrow-request-queue.md), [escrow-request-details.md](escrow-request-details.md), [trust-accounts.md](trust-accounts.md), and [compliance-reports.md](compliance-reports.md), unchanged by this rework. This screen only summarizes and links to them.
