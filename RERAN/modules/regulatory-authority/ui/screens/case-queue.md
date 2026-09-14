---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a3-adjudicate-dispute.md"
  - "RERAN/modules/regulatory-authority/ui/screen-archetypes.md"
tags: [regulatory-authority, ui-spec, back-office, tribunal, queue]
---

# Screen: Case Queue

**Archetype:** 1 — Queue.
**Access (RBAC-gated):** Dispute Adjudication Officer. MFA required.

The worklist of dispute cases (A-3): suits, execution cases, tenancy disputes, complaints.
Follows the Queue archetype; row click opens the [Case Workspace](case-workspace.md). Unlike
the Work Queue, the "decision" is not taken here or even on a single screen — it happens
across sessions in the workspace.

## Purpose

Give the Dispute Adjudication Officer one prioritised list of cases across their lifecycle
stages, with enough context to pick up the right case next.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (role-scoped)
* **Top Bar Title:** Cases
* **Search Bar:** Search by case ref, party, or matter...

```
Top Bar → Summary Cards → Filters & Search → Case Table → Pagination
```

## Sections

### Section 1 — Summary Cards

Open cases · Scheduled this week · Awaiting judgment · Closed this month.

### Section 2 — Filters & Search

**Filter by:** matter type (suit / execution / tenancy / complaint) · case-lifecycle status
(status-badges §2) · next-session date. **Search by:** case reference · party.

### Section 3 — Case Table

| Column | Notes |
| :-- | :-- |
| Case ref | |
| Matter type | Suit / execution / tenancy dispute / complaint |
| Parties | |
| Status | Case lifecycle (status-badges §2) |
| Next session | Scheduled date, if any |

Row click → [Case Workspace](case-workspace.md).

## Role Variations / Permissions

- Dispute Adjudication Officer only reaches this screen; no decision is taken here.

## Notes

- Statuses use the case lifecycle vocabulary (status-badges §2), not the shared four-state
  decision vocabulary.
