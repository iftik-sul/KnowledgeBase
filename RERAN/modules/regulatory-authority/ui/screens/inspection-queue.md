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
tags: [regulatory-authority, ui-spec, inspection, queue, mobile]
---

# Screen: Inspection Queue

**Archetype:** 1 — Queue. **Form factor: mobile / tablet** (field use, not desk-based) — the only
Regulatory Authority screens that are not desktop back-office (per A-7 service flow).
**Access (RBAC-gated):** Inspection & Enforcement Officer. MFA required. Navigation is governed by [role-screen-matrix.md](../role-screen-matrix.md).

The field officer's worklist (A-7): inspections requested (as a sub-step of an A-1 decision, e.g.
RED #27, or proactively) and scheduled. Follows the Queue archetype adapted to a phone/tablet — a
single-column stacked list rather than a wide desktop table. Row tap opens the
[Inspection Capture](inspection-capture.md) screen for a scheduled visit, or a schedule action for a
requested one.

## Purpose

Give the on-site officer a mobile list of their requested and scheduled inspections, ordered so they
can plan and conduct visits in the field.

## Layout (mobile / tablet)

* **Visible Sidebar:** none on mobile — a top app bar + bottom nav or hamburger menu (role-scoped),
  not the 240-wide desktop sidebar.
* **Top Bar Title:** Inspections
* **Search Bar:** Search by site, project, or reference...

```
Mobile Top Bar → Summary chips → Filters → Inspection list (stacked cards) → (infinite scroll / paged)
```

## Sections

### Section 1 — Summary chips

Requested · Scheduled today · Overdue. (Compact chips, not the desktop KPI card row.)

### Section 2 — Filters

**Filter by:** status (Requested / Scheduled / Completed / Cancelled — A-7 §13) · scheduled date ·
matter type. **Search by:** site / project / reference.

### Section 3 — Inspection list (stacked cards, mobile)

Each inspection is a tappable card (not a table row), showing:

- Site / project name + reference
- Matter type (what triggered it — e.g. RED #27 field visit)
- Status (status-badges — inspection lifecycle: Requested / Scheduled / Completed / Cancelled)
- Scheduled date/time (if scheduled), or a **Schedule** action (if only requested)
- Location (short address) with a map affordance

Tap → [Inspection Capture](inspection-capture.md) (scheduled) or the schedule flow (requested).

## Role Variations / Permissions

- Inspection & Enforcement Officer only. No decision is taken here — inspections feed A-1 decisions,
  they don't make them.

## Notes

- **Mobile/tablet form factor** — do not reuse the desktop shell (240 sidebar, 1440×927). Design for a
  phone/tablet viewport with touch targets and on-the-go use.
- Inspection status vocabulary is A-7's own (Requested/Scheduled/Completed/Cancelled); confirm/record
  its Badge colours in status-badges when built.
