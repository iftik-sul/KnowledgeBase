---
project: ERP
module: procurement
type: data-model
status: current
updated: 2026-08-14
derived_from:
  - reference/discovery/multi-tenancy-and-architecture.md
---

# Sourcing Order

Tracks the outsourced (buy) fulfillment path for an Order Line — the sibling to Production Order's make path. See [modules/sales-and-billing/order-model.md](/ERP/modules/sales-and-billing/order-model.md) for how an Order Line forks between the two.

## When a Sourcing Order is created

- The Order Line's Item is not flagged `is_manufacturable` on the Item Master — it's always sourced, no BOM exists for it.
- A manufacturable Order Line is partially or fully converted mid-course (see modules/manufacturing/production-model.md, "Mid-course conversion to sourcing").

## Relationship to Procurement

A Sourcing Order is a thin, order-linked layer over the existing Procurement Purchase Request flow (see [purchase-flow.md](purchase-flow.md)) — it creates/uses a Purchase Request with the same vendor-selection and approval/payment mechanics already defined there. It adds two things the generic Purchase Request doesn't otherwise carry:

1. A link back to the specific Order Line it's fulfilling.
2. A status lifecycle mirroring Production Order, so it can be tracked and reported on the same way.

This is a deliberate trade-off: a small amount of duplication (an order-linked wrapper) in exchange for reusing the approval/payment mechanics already designed in Procurement, rather than building a second purchasing system from scratch.

## Fields

| Field | Purpose |
|---|---|
| `order_line_id` | The Order Line being fulfilled |
| `item_id` | The item being sourced |
| `qty_to_source` | Qty committed to this Sourcing Order |
| `vendor_id` | Selected vendor |
| `purchase_request_id` | Linked Purchase Request in Procurement |
| `status` | Pending → Ordered from Vendor → Received |
| `received_qty`, `balance_qty` | Tracked the same way Production Order tracks produced/balance qty |

## Status parity with Production Order

An Order Line's Balance Qty is the Ordered Qty minus the sum of qty committed across every Production Order and Sourcing Order against it. This lets the In-Hand Report and Delivery Challan bundling logic treat a Sourcing Order's received qty the same way they treat a Production Order's produced qty — Delivery doesn't need to know which path supplied the stock.

## Open item

Whether stock received against a Sourcing Order is earmarked/reserved specifically for its Order Line, or enters general Finished Goods stock indistinguishable from other stock, is not yet decided. This matters if the same item is sourced for multiple orders concurrently — flagged for a future design pass, not resolved here.
