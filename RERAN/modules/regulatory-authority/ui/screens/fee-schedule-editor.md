---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-17
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a4-configure-fee-schedule.md"
  - "RERAN/modules/regulatory-authority/ui/screen-archetypes.md"
tags: [regulatory-authority, ui-spec, back-office, finance, config]
---

# Screen: Fee Schedule Editor

**Archetype:** 3 — Editor / Config.
**Access (RBAC-gated):** Revenue & Finance Officer only. MFA required. Navigation (which roles reach this screen) is governed by [role-screen-matrix.md](../role-screen-matrix.md); the roles named here identify who acts on this screen.

Where the platform's fee and levy schedule is maintained (A-4). Every fee-bearing
service reads what is published here — the widest-blast-radius config surface in the
Regulatory Authority.

## Purpose

Let the Revenue & Finance Officer maintain fees and levies in one authoritative, versioned
place, so pricing changes are made once and applied everywhere.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (Revenue & Finance scope)
* **Top Bar Title:** Fee Schedule
* **Search Bar:** Search by service or levy...

```
Top Bar → Fee Entry List → Fee Entry Editor → Publish → Version History
```

## Sections

### Section 1 — Fee Entry List

| Column | Notes |
| :-- | :-- |
| Service / levy | The service or levy the fee applies to |
| Amount | Current published amount |
| Effective from | |
| Status | Draft / Published / Archived (status-badges §3) |

### Section 2 — Fee Entry Editor

Create/edit a fee or levy entry (`M-FIN-01`): mapped service/levy, amount, effective dates.
Validation per validation-rules (must map to a real service/levy; valid amount and dates; no
fee-bearing service left without an entry).

### Section 3 — Publish & Version History

Publish (`M-FIN-02`) makes the entry live for all fee-bearing services — that modal must
state the blast radius, and **step-up re-authentication is required**. Superseded amounts are
archived (`M-FIN-04`) with their effective dates; a prior version can be restored
(`M-FIN-03`). History shows every version and who published it. Modal wording and fields are
owned by [modals.md](../modals.md) §5.

## Role Variations / Permissions

- **Revenue & Finance Officer only.** Actions: create/edit entries, publish, revert to a
  prior published version. All logged to the Audit Trail.

## Notes

- This is the sole source of truth for platform fees (A-4 §21). No other screen sets fees.
- Feeds A-5 Reconciliation (the "owed" side).
