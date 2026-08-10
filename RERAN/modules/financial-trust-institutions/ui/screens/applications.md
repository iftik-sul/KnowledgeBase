---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/modules/financial-trust-institutions/navigation.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - applications
---

# Screen: Applications

**Roles:** Mortgage Officer (own) · Institution Relationship Manager (institution-wide) · Auditing Bureau Officer (institution-wide, read)

Search, filter and act on service requests across the eighteen Group C services. Not used by the Account Trustee, whose inbound work is Group B escrow requests, not one of the eighteen — see [escrow-request-queue.md](escrow-request-queue.md) instead.

## Purpose

Give each role the slice of application activity relevant to their job: the Mortgage Officer their own filings, the Institution Relationship Manager everything at the institution, the Auditing Bureau Officer a read-only view sufficient to support an audit without granting action.

## Layout

```
Top Bar
↓
Institution Context Header
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
| Pending Internal Certification | At the institution's own gate, where configured |
| Submitted / Under Review | With RERAN |
| Information Requested | RERAN has raised a query |
| Approved — Awaiting Payment | Passed audit, not yet settled |
| Completed This Month | Settled and issued |

Selecting a card filters the table. Cards reflect only what the current scope shows — see Role Variations.

### Section 2 — Filters & Search

**Search by:** Application reference · Service · Property/instrument reference · Represented party

**Filters**

* **Service** — all eighteen, grouped as in the Service × Form Matrix
* **Status** — the Application Status vocabulary in [status-badges.md](../status-badges.md#application-status)
* **Gate** — Internal Certification · RERAN Review · Settlement · Completed
* **Origination** — Direct · Assisted (Trustee Centre / Land Department)
* **Date Range** — submitted date
* **SLA State** — All · Within window · Approaching · Breached
* **Sort By** — Most recent (default) · SLA urgency · Service

### Section 3 — Applications Table

| Column | Description |
| :---- | :---- |
| Application Reference | Links to [application-details.md](application-details.md) |
| Service | Which of the eighteen |
| Filed By | Mortgage Officer or IRM of record |
| Represented Party | Borrower, lessee, heir, purchaser, or the institution itself for #1/#2/#18 |
| Origination | Direct or Assisted, with operator identity where assisted |
| Gate | Internal Certification, RERAN Review, Settlement or Completed — mirrors [application-details.md](application-details.md#progress) |
| Status | See [status-badges.md](../status-badges.md#application-status) |
| Submitted | Date, blank for drafts |
| SLA | Countdown against the service's sourced SLA, where one exists |
| Action | Open |

**Row actions:** Open · Download Application Summary

**Bulk actions:** Export Selected. No bulk decision action exists on this screen — certify, return, approve and settle all happen on their own screens, never as a list-level batch action here.

## Empty State

**Message**

> No applications match these filters. Adjust filters, or start a new service request.

**Primary Button:** New Service Request *(Mortgage Officer, Institution Relationship Manager only — see Role Variations)*
**Secondary Button:** Clear Filters

## Reused Components

See [components.md](../components.md). Uses Institution Operations Sidebar, Top Bar, Institution Context Header, KPI Summary Cards, Filter Bar, Data Table, Status Badge, Pagination, Empty State.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. Row visibility is scoped per role before any filter is applied — see Role Variations. A user cannot widen visibility with a filter; filters narrow what their scope already shows.
2. Open is always available within a role's visible rows. Any further action (certify, respond, settle) is gated on the current status and scope, and is offered on [application-details.md](application-details.md), not here.

## Role Variations

### Mortgage Officer

Sees **only applications they filed**, direct or assisted, across the services they can initiate (#3–#12, and #13–#17 where bank-originated). Status Summary Cards count their own filings only. New Service Request is the primary action.

### Institution Relationship Manager

Sees **every application at the institution**, across every Mortgage Officer and every service, including #1/#2/#18 filed under their own name. Status Summary Cards reflect institution-wide totals — the same totals the Dashboard's Institution-Wide Volume section pulls from. New Service Request is available, scoped to #1/#2/#18.

### Auditing Bureau Officer

**Read-only, institution-wide.** Sees every application, for the same reason the role needs institution-wide visibility for compliance reporting, but has no Open→action path beyond viewing: no Open button leads to a Certify, Return, Respond or Settle control on [application-details.md](application-details.md) for this role. No New Service Request action — this role does not file.

## User Flow

```
Applications
├─ Open → Application Details
├─ New Service Request → Service Request (Mortgage Officer, IRM only)
└─ Export Selected → download
```

## Notes

* **Account Trustee has no variation here because the screen does not apply.** This is not an omission — the role owns none of the eighteen services (services-overview.md), and its equivalent work surface is [escrow-request-queue.md](escrow-request-queue.md). Listing a non-variation would misstate that as an access gap rather than a structural fact.
* Holding the `certify` scope does not add a further filtered view on this screen. The certification-specific queue is [internal-certification-queue.md](internal-certification-queue.md); Applications remains scoped by the user's underlying role regardless of scopes held.
* SLA figures shown are only as reliable as the source SLA for each service — several services (institutional approval, several title & ownership transactions) carry sourced SLAs; others remain proposed where the module's own service-flow documents flag them as such.
