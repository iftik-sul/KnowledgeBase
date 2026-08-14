---
project: ERP
module: manufacturing
type: data-model
status: current
updated: 2026-08-14
derived_from:
  - reference/discovery/multi-tenancy-and-architecture.md
---

# Production Model

Generic, make-to-order.

- A Production Order is one fulfillment path for an Order Line (see [modules/sales-and-billing/order-model.md](/ERP/modules/sales-and-billing/order-model.md)) — the in-house manufacturing path. An Order Line can have zero, one, or more Production Orders, alongside zero or more Sourcing Orders, together covering its ordered qty.
- Each Production Order has independent status, produced qty, balance qty, and priority.
- Material Requisition is created per Production Order.
- Inventory: Raw Material master + a single Stock Ledger (IN = purchase, OUT = requisition issue) — full detail in modules/inventory/README.md.
- Finished Goods & Waste tracked per Production Order (Waste includes QC rejects and trimming/material waste).
- BOM Master is fixed, predefined, and reusable — selected (not auto-generated) when creating a Requisition.
- **Only items flagged `is_manufacturable` on the Item Master can have a BOM or a Production Order at all.** Items not flagged this way are always fulfilled via Sourcing Order — see [modules/procurement/sourcing-order.md](/ERP/modules/procurement/sourcing-order.md).

## Mid-course conversion to sourcing

If a Production Order can't complete its committed qty (capacity issue, equipment failure, etc.), its remaining Balance Qty can be closed out and reassigned to a new Sourcing Order against the same Order Line, rather than cancelling or recreating the Order Line itself. The Order Line's overall Balance Qty accounts for this automatically once qty is summed across both fulfillment types.

## In-Hand Report

Daily production-planning view listing Production Orders with Balance Qty > 0, groupable by a configurable dimension (e.g., color/category). Production Manager generates it each morning; Admin/MD sets a numeric Priority field per Production Order (1 = goes first) to decide production sequence. This report only concerns the manufacturing fulfillment path — the sourced portion of a split Order Line is tracked separately via Sourcing Order status.

---

## Industry Variations

### Woven Label

- Material Requisition is called the "Yarn Requisition Slip."
- Artwork File# and Sample Card are shared at the Order Line level (not duplicated per Production Order, in the case of a split line).
- In-Hand Report groups by color (White/Black in the reference deployment's paper form) — the grouping dimension itself is configurable per company, not fixed to color for every Woven Label company.

### Packaging

- Manufactured vs. traded item distinction is now handled generically at the platform level via `is_manufacturable` on the Item Master — no category-specific work needed here.
