---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-17
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a5-reconcile-settlements.md"
  - "RERAN/modules/regulatory-authority/ui/screen-archetypes.md"
tags: [regulatory-authority, ui-spec, back-office, finance]
---

# Screen: Reconciliation Dashboard

**Archetype:** 4 — Dashboard / Monitor (with a remittance sub-view).
**Access (RBAC-gated):** Revenue & Finance Officer only. MFA required. Navigation (which roles reach this screen) is governed by [role-screen-matrix.md](../role-screen-matrix.md); the roles named here identify who acts on this screen.

Where gateway receipts are matched to fees owed, discrepancies surfaced, and remittances
managed (A-5). It closes the money loop the Fee Schedule Editor opens.

## Purpose

Give the Revenue & Finance Officer a clear picture of whether collected equals owed for a
period, a way to investigate discrepancies, and the remittances due to each account.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (Revenue & Finance scope)
* **Top Bar Title:** Reconciliation
* **Tabs:** Reconciliation · Remittances

```
Top Bar → Period selector → Summary tiles → Matched vs Discrepant table → [Remittances tab]
```

## Sections

### Section 1 — Period & Summary tiles

Select a period and run reconciliation (`M-FIN-05`); tiles show Collected · Owed · Matched ·
Discrepant · run status (Open / Balanced / Discrepant, status-badges §3).

### Section 2 — Matched vs Discrepant table

| Column | Notes |
| :-- | :-- |
| Receipt / transaction | Gateway settlement record |
| Service | The transacted service |
| Owed | Per the published fee schedule (A-4) |
| Collected | Per the gateway |
| State | Matched / Discrepant (flagged) |

Discrepant rows drill into an investigation view; resolving one raises `M-FIN-06`, which
**requires a recorded reason** — discrepancies cannot be auto-cleared (validation-rules).

### Section 3 — Remittances (tab)

Computed remittances per destination account, each Pending or Remitted (status-badges §3).
Recording a remittance raises `M-FIN-07`. Modal wording and fields are owned by
[modals.md](../modals.md) §5.

## Role Variations / Permissions

- **Revenue & Finance Officer only.** Actions: run reconciliation, flag/resolve
  discrepancies (with reason), record remittances. All logged to the Audit Trail.

## Notes

- Depends on A-4 (the "owed" amounts) and the Remita gateway (the "collected" side).
- No standing balances; per-transaction receipts only (A-5 §21).
