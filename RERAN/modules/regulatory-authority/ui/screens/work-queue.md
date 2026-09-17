---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-17
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

**Archetype:** 1 — Queue.
**Access (RBAC-gated):** Compliance & Escrow Auditor (transaction + escrow views); Licensing & Registration Officer (licensing view). Reachable only by the role that owns the queue type — MFA required. Navigation (which roles reach this screen) is governed by [role-screen-matrix.md](../role-screen-matrix.md); the roles named here identify who acts on this screen.

The single worklist a reviewer works from. Submitted, paid applications land here awaiting
a decision; the reviewer triages and opens them into [Application Review](application-review.md).
It is **one screen with queue-type views**, not separate screens — the columns and filters
change per queue type, the layout does not. **Transaction and Escrow are two separate
sidebar entries with distinct routes** that render this one screen (resolves flow gap G2):
escrow work has a different entry gate and a heavier checklist, so it warrants its own
entry point even though the layout is shared.

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
separate screens — see their own specs.)*

## Sections

### Section 1 — Queue Summary Cards

Four cards; selecting one filters the table. Chosen as **triage signals** — each answers
"what should I work on next" (open-questions A7).

| Card | Description |
| :-- | :-- |
| Breaching deadline | Past the originating service's processing window — act now |
| Due soon | Approaching the deadline; next in line |
| Waiting to be picked up | Unclaimed items in the pool — the main queue |
| My open items | Claimed by this officer, so nothing is left half-reviewed |

**Default sort: most urgent deadline first, not oldest.** The 92 services carry very
different SLAs (25 minutes to 6 business days), so a 2-day-old item can be far more urgent
than a 5-day-old one — sorting by age would quietly bury genuinely urgent work.

*Deliberately excluded:* "Decided this month" (a performance statistic, not a triage
signal), "Information requested" (sitting with the applicant, so not actionable — available
as a filter instead), and "Under review" (vague, and overlaps My open items).

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
| Status | Shared status vocabulary (see [status-badges.md](../status-badges.md) §1) |
| Resubmission | Flags an item returning after Information Requested / Returned, with the original query available (resolves flow gap G9) |
| Age / SLA | Time against the **current** SLA window vs the originating service's SLA; breaching rows flagged. Resets on resubmission (see below) |
| Total elapsed | Time since **first** submission, across all query rounds. Does not reset — kept visible so repeated queries cannot hide overall delay |
| Escrow flag | *(escrow view)* trustee-assessment received indicator |
| Claimed by | Who currently holds the item, and since when. Blank = available to claim |

Row click → [Application Review](application-review.md), which **claims** the item to the
opening officer. No decision is taken from the queue itself; the queue triages, the review
screen decides.

### Section 4 — Work allocation *(resolves flow gap G4)*

This queue is a **shared pool**, not an assigned worklist. Any Compliance & Escrow Auditor
may claim any available item; there is no supervisor allocation step and no "assigned to
me" concept.

This deliberately differs from A-3, where dispute cases *are* assigned to a named officer.
The reason is the nature of the work: a dispute is a long-running relationship worked over
multiple sessions, so continuity matters; a transaction audit is a discrete task, so
throughput matters. Pool suits high, uneven arrival volume across 92 services.

Claiming is governed by claim-on-open with timed release (modals.md §9): opening claims,
inactivity lapses the claim (`M-QUE-02`), and an officer may release deliberately
(`M-QUE-01`). Opening an item another officer holds raises `M-QUE-03` and offers read-only.

### Section 5 — Empty state *(resolves flow gap G3)*

An empty table must say which of three things it means:
- **You are clear** — nothing awaiting review in this queue.
- **Filters hide everything** — offer to clear filters.
- **Nothing has arrived yet** — first-run / new queue.

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

**Returning items (G9).** An item the applicant has responded to re-enters this queue
routed **back to the officer who queried it** where that officer is available, otherwise to
the pool. It is flagged as a resubmission and shows the original query.

**SLA clock — resets on resubmission (confirmed).** When an item is returned to the
applicant (Request Additional Information / Return) and the applicant resubmits, the SLA
clock **restarts from zero** — the item gets a fresh full window from the originating
service's published processing time. It does not pause-and-resume, and it does not run
continuously.

Consequences the UI must handle:
- **Breaching SLA** is computed against the *current* window only, so a resubmitted item is
  never carried in breaching on arrival.
- Because the clock resets, an item queried repeatedly could accumulate long real-world
  elapsed time while always showing green. The **Total elapsed** column (time since first
  submission, never reset) is therefore shown alongside, so overall delay stays visible for
  oversight and audit even though it does not drive the SLA badge.

**Claim lapse (confirmed).** A claim lapses after **30 minutes of inactivity**; the item
returns to the pool and may be claimed by another officer (`M-QUE-02`).
