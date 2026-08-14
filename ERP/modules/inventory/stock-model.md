---
project: ERP
module: inventory
type: data-model
status: current
updated: 2026-08-14
derived_from:
  - reference/discovery/multi-tenancy-and-architecture.md
---

# Stock Model

- Raw Material master + a single Stock Ledger table for both IN (purchase) and OUT (requisition issue) transactions.
- Reorder level field exists on the Raw Material record; automated reorder-point triggering is not designed.
- Finished Goods & Waste are tracked per Production Order (see modules/manufacturing/production-model.md), not per whole parent Order. Waste includes QC rejects and trimming/material waste.

## Out of scope

Multi-location/multi-warehouse inventory, lot/batch/serial tracking, cycle counts.
