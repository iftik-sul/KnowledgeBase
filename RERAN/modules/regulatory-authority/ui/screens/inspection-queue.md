---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-18
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a7-conduct-site-inspection.md"
  - "RERAN/modules/regulatory-authority/ui/screen-archetypes.md"
tags: [regulatory-authority, ui-spec, inspection, queue]
---

# Screen: Inspection Queue

**Archetype:** 1 — Queue. Desktop back-office (like every other Regulatory Authority screen).
**Access (RBAC-gated):** Inspection & Enforcement Officer. MFA required. Navigation is governed by [role-screen-matrix.md](../role-screen-matrix.md).

The field officer's worklist (A-7): inspections requested (as a sub-step of an A-1 decision, e.g.
RED #27, or proactively) and scheduled. Follows the standard desktop Queue archetype. Row click opens
the [Inspection Capture](inspection-capture.md) screen for a scheduled visit, or a schedule action for
a requested one.

## Purpose

Give the officer one prioritised list of their requested and scheduled inspections, ordered so they
can plan and conduct visits.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (role-scoped)
* **Top Bar Title:** Inspections
* **Search Bar:** Search by site, project, or reference...

```
Top Bar → Summary Cards → Filters & Search → Inspection Table → Pagination
```

## Sections

### Section 1 — Summary Cards

Requested · Scheduled today · Completed this month · Overdue.

### Section 2 — Filters & Search

**Filter by:** status (Requested / Scheduled / Completed / Cancelled — A-7 §13) · scheduled date ·
matter type. **Search by:** site / project / reference.

### Section 3 — Inspection Table

| Column | Notes |
| :-- | :-- |
| Site / project | With its reference |
| Matter type | What triggered it — e.g. RED #27 field visit |
| Location | Short address |
| Status | Inspection lifecycle (status-badges §4): Requested / Scheduled / Completed / Cancelled |
| Scheduled | Date/time, if scheduled — otherwise a **Schedule** action |

Row click → [Inspection Capture](inspection-capture.md) (scheduled) or the schedule flow (requested).

## Role Variations / Permissions

- Inspection & Enforcement Officer only. No decision is taken here — inspections feed A-1 decisions,
  they don't make them.

## Notes

- Desktop back-office, same 1440×927 shell as every other Regulatory Authority screen.
- Statuses use the inspection lifecycle vocabulary (status-badges §4), not the shared four-state
  decision vocabulary.
