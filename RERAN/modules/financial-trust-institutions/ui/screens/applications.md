---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-15
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

**Access:** Any of the institution's four Group C roles — unified access, not role-gated (`navigation.md`, confirmed 2026-08-14). Not used by way of a separate screen for the Account Trustee's inbound escrow work, which is Group B-originated, not one of the eighteen numbered services — see [escrow-request-queue.md](escrow-request-queue.md) instead.

Search, filter and act on service requests across the eighteen Group C services.

> **Corrected 2026-08-15.** This screen previously scoped visibility by role: Mortgage Officer saw only their own filings, Institution Relationship Manager saw the institution, Auditing Bureau Officer had institution-wide read only. Per the unified-access model, every user sees every application at the institution — role is attribution only, not a visibility filter. See Role Variations below, rewritten accordingly.

## Purpose

Give every institution user a single, institution-wide view of application activity across the eighteen services, with filters to narrow it to what they're working on — not a visibility boundary enforced by role.

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
| Completed This Month | Settled and issued |

Selecting a card filters the table. Cards reflect institution-wide totals — the same totals for every user, since the underlying data is not role-scoped.

**Corrected 2026-08-15** — the `Approved — Awaiting Payment` card is removed. Per `open-questions.md` B1 and B11, no Group C service is ever approved while payment is still pending: #1 and #3–#11 pay upfront before lodging, #2 carries no fee, and #12–#18 pay at the point of service. This status does not occur for any Group C application.

### Section 2 — Filters & Search

**Search by:** Application reference · Service · Property/instrument reference · Represented party

**Filters**

* **Service** — all eighteen, grouped as in the Service × Form Matrix
* **Status** — the Application Status vocabulary in [status-badges.md](../status-badges.md#application-status)
* **Gate** — Internal Certification · RERAN Review · Completed *(corrected 2026-08-15 — "Settlement" removed as a gate; see Section 3)*
* **Origination** — Direct · Assisted (Trustee Centre / Land Department)
* **Filed By** — dropdown of institution staff, added 2026-08-15 to preserve the "my filings" narrowing this screen used to provide by default, now available as an explicit filter instead of a role restriction
* **Date Range** — submitted date
* **SLA State** — All · Within window · Approaching · Breached
* **Sort By** — Most recent (default) · SLA urgency · Service

### Section 3 — Applications Table

| Column | Description |
| :---- | :---- |
| Application Reference | Links to [application-details.md](application-details.md) |
| Service | Which of the eighteen |
| Filed By | The institution user who filed it, whatever their role |
| Represented Party | Borrower, lessee, heir, purchaser, or the institution itself for #1/#2/#18 |
| Origination | Direct or Assisted, with operator identity where assisted |
| Gate | Internal Certification or RERAN Review, or Completed |
| Status | See [status-badges.md](../status-badges.md#application-status) |
| Submitted | Date, blank for drafts |
| SLA | Countdown against the service's sourced SLA, where one exists |
| Action | Open |

**Corrected 2026-08-15** — the Gate column's "Settlement" stage is removed, for the same reason the Status Summary Cards drop `Approved — Awaiting Payment`: payment happens before lodging (#1, #3–#11) or at the point of service (#12–#18), never as a stage between audit approval and completion.

**Row actions:** Open · Download Application Summary

**Bulk actions:** Export Selected. No bulk decision action exists on this screen — certify, return and approve all happen on their own screens, never as a list-level batch action here.

## Empty State

**Message**

> No applications match these filters. Adjust filters, or start a new service request.

**Primary Button:** New Service Request
**Secondary Button:** Clear Filters

**Corrected 2026-08-15** — the primary button is no longer conditional on role. Any of the four roles may file a service request (`open-questions.md` A4).

## Reused Components

See [components.md](../components.md). Uses Institution Operations Sidebar, Top Bar, Institution Context Header, KPI Summary Cards, Filter Bar, Data Table, Status Badge, Pagination, Empty State.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. **Corrected 2026-08-15** — row visibility is institution-wide for every role; there is no role-scoped visibility rule left to enforce here. The Filed By filter narrows the view by choice, not by access boundary.
2. Open is always available on any visible row. Any further action (certify, respond) is gated on the current status, not on who is viewing, and is offered on [application-details.md](application-details.md), not here.

## Role Variations

**Corrected 2026-08-15 — this section is removed.** Every role sees the same institution-wide table, the same summary cards, and has access to New Service Request. There is no per-role variation left to describe; see the banner note at the top of this document.

## User Flow

```
Applications
├─ Open → Application Details
├─ New Service Request → Service Request
└─ Export Selected → download
```

## Notes

* **The Account Trustee's inbound escrow work is a separate screen, not a role restriction on this one.** [escrow-request-queue.md](escrow-request-queue.md) exists because Group B-originated escrow requests are not one of the eighteen numbered Group C services and don't belong in this table structurally — any of the four roles can still open this Applications screen and act on any of the eighteen services here, same as anywhere else in the module.
* SLA figures shown are only as reliable as the source SLA for each service — several services (institutional approval, several title & ownership transactions) carry sourced SLAs; others remain proposed where the module's own service-flow documents flag them as such.
