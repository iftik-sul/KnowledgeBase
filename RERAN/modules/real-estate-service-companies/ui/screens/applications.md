---
project: RERAN
module: real-estate-service-companies
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/services-overview.md"
  - "RERAN/modules/real-estate-service-companies/navigation.md"
tags:
  - real-estate-service-companies
  - ui-spec
  - applications
---

# Screen: Applications

**Access:** Any of the company's four Group D roles — identical screen for every user.

## Purpose

Give every company user a single, company-wide view of application activity across the module's services, with filters to narrow it to what they're working on.

## Layout

```
Top Bar
↓
Company Context Header
↓
Status Summary Cards
↓
Filters & Search
↓
Applications Table
↓
Pagination
```

## Sections

### Section 1 — Status Summary Cards

| KPI | Description |
| :---- | :---- |
| Draft | Started, not submitted |
| Submitted / Under Review | With RERA |
| Information Requested | RERA has raised a query |
| Awaiting Payment | Approved, payment outstanding — Services #12–#15 only, see Notes |
| Completed This Month | Settled and issued |

**Awaiting Payment is a genuinely real state for this module**, unlike Financial & Trust Institutions' now-retired equivalent (see that module's `status-badges.md` for the full three-pass history of getting this wrong and then right). Services #12–#15 source payment happening after acceptance, not before — confirmed directly against each service's own file, not assumed from a filter list. This status card exists because the underlying scenario is sourced, not because a UI screen implied it.

### Section 2 — Filters & Search

**Search by:** Application reference · Service · Property/agent/instrument reference

**Filters**

* **Category** — Jointly Owned Property · Licensing · Rental · Transaction · Dispute
* **Status** — the Application Status vocabulary in `ui/status-badges.md` (Phase 5)
* **Payment State** — No Fee · Pending · Paid · Awaiting Payment (post-decision)
* **Filed By** — dropdown of company staff, attribution-only, not an access filter
* **Date Range** — submitted date

### Section 3 — Applications Table

| Column | Description |
| :---- | :---- |
| Application Reference | Links to Application Details |
| Service | Which of the 25 |
| Category | JOP · Licensing · Rental · Transaction · Dispute |
| Filed By | The company user who filed it, whatever their role |
| Status | See `ui/status-badges.md` |
| Payment State | No Fee · Pending · Paid · Awaiting Payment |
| Submitted | Date, blank for drafts |
| Action | Open |

**Row actions:** Open · Download Application Summary

**Bulk actions:** Export Selected. No bulk decision action exists here — there is no internal certification gate anywhere in this module (`open-questions.md` A5) for a bulk certify action to apply to in the first place.

## Empty State

**Message**

> No applications match these filters. Adjust filters, or start a new service request.

**Primary Button:** New Service Request
**Secondary Button:** Clear Filters

## Reused Components

Company Operations Sidebar, Top Bar, Company Context Header, KPI Summary Cards, Filter Bar, Data Table, Status Badge, Pagination, Empty State.

## Validation

1. Row visibility is company-wide for every role; the Filed By filter narrows the view by choice, not access.
2. Open is always available on any visible row. Further action (respond to query, complete post-decision payment) is gated on the current status, not on who is viewing.

## User Flow

```
Applications
├─ Open → Application Details
├─ New Service Request → Submit Application
└─ Export Selected → download
```

## Notes

* **This table shows all 25 selectable-service applications, including Jointly Owned Property services.** Even though JOP also has its own dedicated register (`jointly-owned-property.md`), JOP applications still appear here — the register shows JOP *properties* as standing entities; this table shows every individual *application* filed against the module's services, JOP included. The two screens serve different questions, not competing ones.
* Service #18 does not appear anywhere in this table, consistent with `navigation.md`'s provenance exclusion.
