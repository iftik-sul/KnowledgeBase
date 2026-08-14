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

## Sourced qty is independent of the Order Line's need

`qty_to_source` is **not** capped at the Order Line's remaining balance — a Sourcing Order can order more than the line currently needs (vendor minimum order quantities, bulk pricing, or intentional buffer). The system does not require these to match.

## Fields

| Field | Purpose |
|---|---|
| `order_line_id` | The Order Line being fulfilled |
| `item_id` | The item being sourced |
| `qty_to_source` | Qty being purchased — may exceed the Order Line's remaining need |
| `vendor_id` | Selected vendor |
| `purchase_request_id` | Linked Purchase Request in Procurement |
| `status` | Pending → Ordered from Vendor → Received |
| `received_qty` | Total qty received against this Sourcing Order |
| `qty_reserved_to_line` | `min(received_qty, order_line_remaining_need_at_receipt)` — the portion counted toward this Order Line's fulfillment |
| `qty_surplus` | `received_qty − qty_reserved_to_line` — the portion that exceeded what this line needed |

## Reservation and surplus

Received stock is reserved to its Order Line, but only up to what the line actually needs at the time of receipt. Reservation is what makes a Sourcing Order meaningfully different from a generic raw-material Purchase Request: it guarantees `qty_reserved_to_line` isn't consumed by a different order — a Sourcing Order exists specifically to fulfill one Order Line, and if its output weren't reserved to that line there would be nothing distinguishing it from ordinary restocking.

Any qty sourced beyond that need (`qty_surplus`) enters general Finished Goods stock automatically on receipt, unreserved and available to any future order — no manual step, since it was never committed to a specific Order Line in the first place.

**Contrast with cancellation:** if an Order (or Order Line) is cancelled or reduced after stock was already reserved against it, that previously-reserved stock becomes orphaned — releasing it back to general stock is an **explicit, manual action**, not automatic, since it's a real inventory-value decision that shouldn't happen silently the moment an order is amended.

## Status parity with Production Order

An Order Line's Balance Qty is the Ordered Qty minus the sum of `qty_reserved_to_line` committed across every Production Order and Sourcing Order against it. This lets the In-Hand Report and Delivery Challan bundling logic treat a Sourcing Order's reserved qty the same way they treat a Production Order's produced qty — Delivery doesn't need to know which path supplied the stock.
