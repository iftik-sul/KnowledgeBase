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

- One Production Order per product within a parent Order.
- Each Production Order has independent status, produced qty, balance qty, and priority.
- Material Requisition is created per Production Order (not per whole parent Order).
- Inventory: Raw Material master + a single Stock Ledger (IN = purchase, OUT = requisition issue) — full detail in modules/inventory/README.md.
- Finished Goods & Waste tracked per Production Order (Waste includes QC rejects and trimming/material waste).
- BOM Master is fixed, predefined, and reusable — selected (not auto-generated) when creating a Requisition.

## In-Hand Report

Daily production-planning view listing Orders with Balance Qty > 0 (Order Qty minus cumulative Produced Qty), groupable by a configurable dimension (e.g., color/category). Production Manager generates it each morning; Admin/MD sets a numeric Priority field per Order (1 = goes first) to decide production sequence.

---

## Industry Variations

### Woven Label Manufacturing

- Material Requisition is called the "Yarn Requisition Slip."
- Artwork File# and Sample Card are shared at the Order level (not per Production Order/product).
- In-Hand Report groups by color (White/Black in the original paper form).

### Circle Packaging

- Manufactured vs. traded item distinction (production vs. procurement) is currently out of scope for this template — all 17 products are treated uniformly for now.
