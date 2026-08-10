---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
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

**Scope:** `certify` to act — held by any delegated staff member, regardless of role · Institution Relationship Manager has institution-wide read without holding the scope

The institution's own maker-checker gate, worked here before a record ever reaches RERAN. This screen belongs to a **permission scope**, not a job title (answer A1). A Mortgage Officer holding `certify` sees this queue and can act in it; a Mortgage Officer without it does not see it at all; the Institution Relationship Manager sees it read-only by virtue of their oversight role even without holding `certify` themselves, and separately configures who does hold it.

## Purpose

Give every `certify`-scoped user, whatever their role, a single queue of records awaiting internal certification — filtered so that a record they filed themselves never appears in their own queue — and give the Institution Relationship Manager a read view of the same queue for backlog oversight, without granting the certification action itself.

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
| Awaiting My Certification | Submitted for certification, not filed by this user |
| Certified This Month | Actioned by this user |
| Returned This Month | Sent back by this user |
| Oldest Waiting | Age of the longest-waiting record in the queue |

Selecting a card filters the table.

### Section 2 — Filters & Search

**Search by:** Application reference · Service · Filed by · Represented party

**Filters**

* **Service** — all services with certification configured (see the Service × Form Matrix in [README.md](../README.md#service--form-matrix); several are marked "Yes when configured" rather than unconditionally certified)
* **Filed By** — dropdown of institution staff, excluding the current viewer
* **Age** — All · Under 24 hours · 24–72 hours · Over 72 hours
* **Sort By** — Oldest first (default) · Filed by · Service

Default sort is oldest-first. Nothing in the source sets an SLA for this internal step specifically — the queue's ordering is a design choice against that gap, not a sourced figure.

### Section 3 — Certification Queue Table

| Column | Description |
| :---- | :---- |
| Application Reference | Links to [application-details.md](application-details.md) |
| Service | Which of the eighteen |
| Filed By | The Mortgage Officer or IRM who submitted it |
| Represented Party | Borrower, lessee, or other counterparty |
| Submitted | Date entered this queue |
| Age | Time waiting |
| Status | Pending Internal Certification |
| Action | Review |

**Row actions:** Review · Download Request Pack

**Bulk actions:** none. Certification is a per-record decision made on [application-details.md](application-details.md)'s Decision Panel — this queue routes to it and never certifies inline, for the same reason [escrow-request-queue.md](escrow-request-queue.md) has no bulk certify: a control that certifies several records in one action defeats the reasoning a maker-checker gate exists to capture.

## Empty State

**Message**

> No records are awaiting your certification. Records filed by other staff at this institution will appear here once submitted.

**Primary Button:** View Applications

The Institution Relationship Manager's read-only Queue Overview shows the institution-wide equivalent: *"No records are awaiting certification institution-wide."*

## Reused Components

See [components.md](../components.md). Uses Institution Operations Sidebar, Top Bar, Institution Context Header, KPI Summary Cards, Filter Bar, Data Table, Status Badge, Pagination, Empty State.

## Validation

See [validation-rules.md](../validation-rules.md#permission-scope). Specific to this screen:

1. **The query itself excludes the viewer's own filings**, not just the certify button on them — a self-filed record does not appear in this list at all, rather than appearing greyed. This is enforced at the data layer, not the UI layer, because a visible-but-disabled row would leak information about a filing this user should not be reviewing.
2. Only users holding `certify` can reach this screen; it is not rendered in the sidebar for anyone else, per [navigation.md](../../navigation.md#access-rules) rule 1.
3. Certify and Return both happen on [application-details.md](application-details.md), where the return reason is mandatory — this screen has no decision controls of its own.

## Role Variations

### Any user holding `certify`

No variation by role — a Mortgage Officer, an Institution Relationship Manager, or any other delegated staff member holding the scope sees the same queue, filtered the same way. The only variation is which records are excluded (their own filings), and that follows from who they are, not from their role.

### Institution Relationship Manager, without `certify`

**Institution-wide read.** `navigation.md` and `README.md`'s Role × Screen Matrix both grant this role "Configure" access to this screen, which is really two separate things this rewrite now distinguishes:

* **Configuring** who holds `certify` happens on [institution-profile.md](institution-profile.md#section-2--staff--scopes-tab), not here.
* **Seeing the queue itself**, institution-wide and read-only, happens here — a Queue Overview view with the same summary cards and table as the acting view, minus the Review action and the Awaiting My Certification framing (it becomes Awaiting Certification, institution-wide, not filtered to any one certifier). This gives the IRM visibility into certification backlog and turnaround without granting the action itself, matching the oversight-without-participation pattern already used on [escrow-request-queue.md](escrow-request-queue.md#institution-relationship-manager) and [compliance-reports.md](compliance-reports.md#institution-relationship-manager).

An Institution Relationship Manager who also personally holds `certify` gets the acting view above, not this read-only one — holding the scope always grants the fuller access.

## User Flow

```
Dashboard (certification count badge, any role holding certify)
↓
Internal Certification Queue
├─ Review → Application Details → Certify → back to queue (record removed)
├─ Review → Application Details → Return → back to queue (record removed, filer notified)
└─ Download Request Pack → Documents
```

## Notes

* **This queue is scope-filtered, not role-filtered**, throughout — the Role Variations section above says so explicitly rather than listing four near-identical role blocks, which was the previous version's defect.
* **No SLA is sourced for the internal certification step itself.** Answer A6 addresses the Group B escrow SLA split, not this gate. The Age column and sort order are working assumptions pending a client figure.
* Certification's structure — free-form sign-off versus a defined checklist — is not resolved by any answer for the Mortgage Officer's filings specifically. Answer A3 resolves this for Account Trustee milestone certification ([escrow-request-details.md](escrow-request-details.md)), which is a different certification act on a different object; it should not be assumed to transfer here without confirmation.
