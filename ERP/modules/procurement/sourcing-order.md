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

`qty_to_source` is **not** capped at the Order Line's remaining need — a Sourcing Order can order more than the line currently needs (vendor minimum order quantities, bulk pricing, or intentional buffer), or, in practice, end up receiving less (partial vendor shipment, short supply). The system does not require these to match.

## Fields

| Field | Purpose |
|---|---|
| `order_line_id` | The Order Line being fulfilled |
| `item_id` | The item being sourced |
| `qty_required` | The Order Line's qty needed from this Sourcing Order at the time it was created |
| `qty_to_source` | Qty being purchased — may be more or less than `qty_required` |
| `vendor_id` | Selected vendor |
| `purchase_request_id` | Linked Purchase Request in Procurement |
| `status` | Pending → Ordered from Vendor → Received |
| `received_qty` | Total qty received against this Sourcing Order, fully linked to the Order Line — no split between "reserved" and "surplus" |
| `sourcing_status` | Derived: **Complete** if `received_qty ≥ qty_required`; **Not Completed** if `received_qty < qty_required` |

## Received stock is fully linked to the order, whatever the quantity

All stock received against a Sourcing Order enters inventory linked to that Order Line — including any amount beyond `qty_required`. There is no automatic split into a "reserved" portion and an unreserved "surplus" portion; the entire received qty stays associated with the order. This is what makes `sourcing_status` a simple comparison rather than a computed reservation.

**If it's ever useful to release excess linked stock back to general inventory** (e.g., the order is later reduced or cancelled, or the business decides the extra qty should be available to other orders), that's an **explicit, manual action** — not automatic. Moving stock away from an order it's currently linked to is a real inventory-value decision that shouldn't happen silently.

## Status parity with Production Order

An Order Line's fulfillment is tracked across both Production Orders (produced qty) and Sourcing Orders (received qty). `sourcing_status` on a Sourcing Order plays the same role as a Production Order's produced-vs-balance tracking, so the In-Hand Report and Delivery Challan bundling logic can treat both fulfillment paths the same way — Delivery doesn't need to know which path supplied the stock, only whether it's complete.
