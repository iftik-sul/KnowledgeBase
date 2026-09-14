---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a1-audit-and-decide.md"
  - "RERAN/modules/regulatory-authority/service-flows/service-a2-vet-and-decide-licensing.md"
  - "RERAN/modules/regulatory-authority/ui/role-screen-matrix.md"
tags:
  - regulatory-authority
  - ui-spec
  - back-office
  - queue
---

# Screen: Work Queue

**Access (RBAC-gated):** Compliance & Escrow Auditor (transaction + escrow views);
Licensing & Registration Officer (licensing view). Reachable only by the role that owns
the queue type — see [role-screen-matrix.md](../role-screen-matrix.md). MFA required.

The single worklist a reviewer works from. Submitted, paid applications land here awaiting
a decision; the reviewer triages and opens them into [Application Review](application-review.md).
It is **one screen with queue-type views**, not separate screens — the columns and filters
change per queue type, the layout does not.

## Purpose

Give a reviewer one prioritised list of everything awaiting their decision, with enough
per-row context to triage without opening each item, and a clear view of what is breaching
its SLA.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (role-scoped per the matrix)
* **Active Menu:** the relevant queue (carries a count badge)
* **Top Bar Title:** Work Queue — {queue type}
* **Subtitle:** Review and decide submitted applications.
* **Search Bar:** Search by reference, applicant, or subject...

```
Top Bar
↓
Queue Summary Cards
↓
Filters & Search
↓
Queue Table
↓
Pagination
```

## Queue-type views

One screen renders the view for the queue the role opened:

| View | Owner role | Sourced from |
| :-- | :-- | :-- |
| Transaction | Compliance & Escrow Auditor | A-1 (79 services) |
| Escrow / Trust | Compliance & Escrow Auditor | A-1 (13 services) — adds trustee-assessment context |
| Licensing | Licensing & Registration Officer | A-2 (9 services) |

*(Case, inspection, enforcement, and sign-off queues follow the same pattern but are
separate screens/latent — see their own specs.)*

## Sections

### Section 1 — Queue Summary Cards

KPI cards; selecting one filters the table.

| KPI | Description |
| :-- | :-- |
| Awaiting Review | Received, not yet opened |
| Under Review | Opened by a reviewer |
| Information Requested | Queried back to the applicant |
| Decided This Month | Approved / returned / rejected |
| Breaching SLA | Past the originating service's processing window |

### Section 2 — Filters & Search

**Filter by:** originating service · status · age / SLA state · channel (transaction vs
escrow, on the C&E Auditor's queues).
**Search by:** application reference · applicant · subject (project / property / title /
practitioner).

### Section 3 — Queue Table

| Column | Notes |
| :-- | :-- |
| Reference | Application reference number |
| Originating service | e.g. "RED #1 Register Initial Sale" |
| Applicant | Person / company that filed |
| Subject | Project / property / title / practitioner |
| Status | Shared status vocabulary (see status-badges) |
| Age / SLA | Time in queue vs the originating service's SLA; breaching rows flagged |
| Escrow flag | *(escrow view)* trustee-assessment received indicator |

Row click → [Application Review](application-review.md). No decision is taken from the
queue itself; the queue triages, the review screen decides.

## Role Variations / Permissions

- **Compliance & Escrow Auditor** — reaches the transaction and escrow views; the escrow
  view adds the trustee-assessment column and only shows items past the FTI trustee gate.
- **Licensing & Registration Officer** — reaches the licensing view only; sees credential
  type instead of the escrow column.
- No role can take a decision from this screen; it only opens items. Decision permissions
  live on [Application Review](application-review.md).
- Read access to a queue does not imply decide access on its items (per the matrix).

## Notes

- **Breaching SLA** is computed against each item's *originating* service SLA, not a
  single queue-wide time (A-1 §11 / A-2 §11).
- Auto-approval licensing items (A-2 §15b) do **not** appear here — they raise no manual
  queue item.

> **Proposed** — the exact KPI set and default sort (by SLA urgency vs age) need
> confirmation.
