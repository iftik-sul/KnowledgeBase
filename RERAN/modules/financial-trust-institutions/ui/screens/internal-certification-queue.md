---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/modules/financial-trust-institutions/navigation.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - certification
---

# Screen: Internal Certification Queue

**Access:** Any of the institution's four Group C roles — unified access, not scope-gated (`navigation.md`, confirmed 2026-08-14).

The institution's own maker-checker gate, worked here before a record ever reaches RERAN.

> **Corrected 2026-08-15.** This screen previously belonged to a `certify` permission scope, held only by delegated staff the Institution Relationship Manager provisioned, and excluded a user's own filings from their queue at the data layer to enforce maker ≠ checker. Both are retired. Certification is now an unrestricted action any of the institution's four users may perform on any pending record — **including one they filed themselves** (`open-questions.md` A1; `navigation.md#access-rules` rule 2). This is the single largest correction on this screen; every section below reflects it.

## Purpose

Give every institution user a single queue of every record at the institution awaiting internal certification, so any of the four roles can pick up and act on any pending item — including one they filed themselves.

## Layout

```
Top Bar
↓
Institution Context Header
↓
Queue Summary Cards
↓
Filters & Search
↓
Certification Queue Table
↓
Pagination
```

## Sections

### Section 1 — Queue Summary Cards

| KPI | Description |
| :---- | :---- |
| Awaiting Certification | Submitted for certification, institution-wide |
| Certified This Month | Actioned by this user |
| Returned This Month | Sent back by this user |
| Oldest Waiting | Age of the longest-waiting record in the queue |

Selecting a card filters the table. **Corrected 2026-08-15** — "Awaiting My Certification" is renamed "Awaiting Certification": the queue is institution-wide, not filtered to records the viewer didn't file.

### Section 2 — Filters & Search

**Search by:** Application reference · Service · Filed by · Represented party

**Filters**

* **Service** — all services with certification configured (see the Service × Form Matrix in [README.md](../README.md#service--form-matrix); several are marked "Yes when configured" rather than unconditionally certified)
* **Filed By** — dropdown of institution staff, **now including the current viewer** *(corrected 2026-08-15 — previously excluded the viewer by default, since self-filed records didn't appear in the queue at all)*
* **Age** — All · Under 24 hours · 24–72 hours · Over 72 hours
* **Sort By** — Oldest first (default) · Filed by · Service

Default sort is oldest-first. Nothing in the source sets an SLA for this internal step specifically — the queue's ordering is a design choice against that gap, not a sourced figure.

### Section 3 — Certification Queue Table

| Column | Description |
| :---- | :---- |
| Application Reference | Links to [application-details.md](application-details.md) |
| Service | Which of the eighteen |
| Filed By | The institution user who submitted it — may be the viewer themselves |
| Represented Party | Borrower, lessee, or other counterparty |
| Submitted | Date entered this queue |
| Age | Time waiting |
| Status | Pending Internal Certification |
| Action | Review |

**Row actions:** Review · Download Request Pack

**Bulk actions:** none. Certification is a per-record decision made on [application-details.md](application-details.md)'s Decision Panel — this queue routes to it and never certifies inline, for the same reason [escrow-request-queue.md](escrow-request-queue.md) has no bulk certify: a control that certifies several records in one action defeats the reasoning a maker-checker gate exists to capture, even where maker and checker are no longer required to be different people.

## Empty State

**Message**

> No records are awaiting internal certification institution-wide.

**Primary Button:** View Applications

**Corrected 2026-08-15** — removed the previous two-tier empty state (an acting user's personal message plus a separate IRM read-only message). There is now one queue and one empty state for everyone.

## Reused Components

See [components.md](../components.md). Uses Institution Operations Sidebar, Top Bar, Institution Context Header, KPI Summary Cards, Filter Bar, Data Table, Status Badge, Pagination, Empty State.

## Validation

See [validation-rules.md](../validation-rules.md#audit-trail). Specific to this screen:

1. **Removed 2026-08-15** — the query previously excluded the viewer's own filings at the data layer. It no longer does; a self-filed record appears in this queue like any other, and its Review action leads to the same Decision Panel.
2. **Corrected 2026-08-15** — previously restricted to users holding `certify`, rendered in the sidebar only for them. Now visible to every institution user, per `navigation.md#access-rules` rule 1.
3. Certify and Return both happen on [application-details.md](application-details.md), where the return reason is mandatory — this screen has no decision controls of its own.

## Role Variations

**Corrected 2026-08-15 — this section is removed.** Every institution user sees the same institution-wide queue and can act on any record in it, including their own filings. There is no per-role or per-scope variation left to describe.

## User Flow

```
Dashboard (certification count badge)
↓
Internal Certification Queue
├─ Review → Application Details → Certify → back to queue (record removed)
├─ Review → Application Details → Return → back to queue (record removed, filer notified)
└─ Download Request Pack → Documents
```

## Notes

* **This queue is now unrestricted, not scope-filtered.** The previous version's core design point — "scope-filtered, not role-filtered" — is itself superseded: there is no filtering by role or scope left at all, only ordinary search/filter narrowing available to anyone.
* **No SLA is sourced for the internal certification step itself.** Answer A6 addresses the Group B escrow SLA split, not this gate. The Age column and sort order are working assumptions pending a client figure.
* Certification's structure — free-form sign-off versus a defined checklist — is not resolved by any answer for these filings specifically. Answer A3 (confirmed 2026-08-15) resolves this for Account Trustee milestone certification ([escrow-request-details.md](escrow-request-details.md)), which is a different certification act on a different object; it should not be assumed to transfer here without confirmation.
