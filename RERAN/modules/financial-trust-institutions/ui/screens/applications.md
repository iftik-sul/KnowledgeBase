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

**Corrected 2026-08-15, twice.** This section previously claimed the `Approved — Awaiting Payment` card should be removed because the status "does not occur for any Group C application." A fuller per-service audit found that claim was wrong: **Services #12 and #18 genuinely source this status** — RERA decides before the customer pays at the counter, unlike every other service. No dedicated summary card is added for it here, since it applies to only two of eighteen services and a dedicated card would overstate its frequency — but the status itself is real and must render correctly wherever a #12 or #18 application actually reaches it, via the Status filter and the table's Status column below. Don't build against the earlier "never occurs" claim.

### Section 2 — Filters & Search

**Search by:** Application reference · Service · Property/instrument reference · Represented party

**Filters**

* **Service** — all eighteen, grouped as in the Service × Form Matrix
* **Status** — the Application Status vocabulary in [status-badges.md](../status-badges.md#application-status), which correctly includes `Approved — Awaiting Payment` scoped to Services #12/#18
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

**Corrected 2026-08-15** — the Gate column's "Settlement" stage is removed. This is a different concept from the `Approved — Awaiting Payment` status above: no Group C service ever passes through a distinct "Settlement" processing *gate* between audit approval and completion (that concept described the old settlement-account model), even though #12/#18 do carry a status describing payment as outstanding at that point. The Gate column tracks which processing stage a record is in; the Status column tracks its detailed state within that stage — #12/#18 sit in the "Completed" gate's neighborhood carrying an `Approved — Awaiting Payment` status until the counter payment clears.

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
├─ New Service Request → Submit Application
└─ Export Selected → download
```

**Corrected 2026-08-15** — "Submit Application" replaces "Service Request," matching the screen's actual current name in `ui/screens-unified/`; `service-request.md` was deleted after this file was originally corrected and this reference was never updated to match.

## Notes

* **The Account Trustee's inbound escrow work is a separate screen, not a role restriction on this one.** [escrow-request-queue.md](escrow-request-queue.md) exists because Group B-originated escrow requests are not one of the eighteen numbered Group C services and don't belong in this table structurally — any of the four roles can still open this Applications screen and act on any of the eighteen services here, same as anywhere else in the module.
* SLA figures shown are only as reliable as the source SLA for each service — several services (institutional approval, several title & ownership transactions) carry sourced SLAs; others remain proposed where the module's own service-flow documents flag them as such.
* **Approved — Awaiting Payment is real for #12/#18, but rare.** Don't design the Status Summary Cards or any dashboard rollup around it as if it were a common state — it applies to exactly two of eighteen services, both with short (15–30 minute) SLAs, so the window during which a record actually sits in this status is brief.
