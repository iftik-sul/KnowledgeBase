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

> **Corrected 2026-08-16, by client decision (`open-questions.md` B4).** The Awaiting Payment status card and Payment State value, both built specifically for Services #12–#15's now-retired post-decision payment timing, are removed.

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
| Completed This Month | Settled and issued |

**Corrected 2026-08-16 — Awaiting Payment card removed.** This card previously tracked Services #12–#15's approved-but-unpaid state. With those four services normalized to pay before lodging (`open-questions.md` B4, `payments.md` Model 2), no Group D service is ever approved while payment is still pending — the scenario this card existed to surface no longer occurs.

### Section 2 — Filters & Search

**Search by:** Application reference · Service · Property/agent/instrument reference

**Filters**

* **Category** — Jointly Owned Property · Licensing · Rental · Transaction · Dispute
* **Status** — the Application Status vocabulary in `ui/status-badges.md`
* **Payment State** — No Fee · Pending · Paid *(Corrected 2026-08-16 — "Awaiting Payment (post-decision)" value removed; no longer applies to any service)*
* **Filed By** — dropdown of company staff, attribution-only, not an access filter
* **Date Range** — submitted date

### Section 3 — Applications Table

| Column | Description |
| :---- | :---- |
| Application Reference | Links to Application Details |
| Service | Which of the module's services |
| Category | JOP · Licensing · Rental · Transaction · Dispute |
| Filed By | The company user who filed it, whatever their role |
| Status | See `ui/status-badges.md` |
| Payment State | No Fee · Pending · Paid |
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
2. Open is always available on any visible row. Further action (respond to query) is gated on the current status, not on who is viewing.

## User Flow

```
Applications
├─ Open → Application Details
├─ New Service Request → Submit Application
└─ Export Selected → download
```

## Notes

* **This table shows applications for every wizard-eligible and email-only service, including Jointly Owned Property services.** Even though JOP also has its own dedicated register (`jointly-owned-property.md`), JOP applications still appear here.
* **Service #18 now appears in this table, per `open-questions.md` A2's 2026-08-16 decision to keep it in Group D** — previously excluded entirely. Its own atypical shape (evaluation-company-decides, not a standard RERA application) may need a distinct row treatment or status vocabulary; flagged for follow-up once Service #18's own dedicated screen is designed, not resolved here.
