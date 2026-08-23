---
project: 3i
module: commerce
type: ui-spec
status: current
updated: 2026-08-20
id: 3I-CMR-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - checkout
---

# Screen: Pricing / Plan Selection

Satisfies: FR-BILL-01, FR-BILL-04

---

## Purpose

Let a Member choose which profiles to activate and at what cadence, before handing off to Stripe-hosted Checkout. This is the cart-building step, not the payment step.

## Access Gate

Web only (FR-BILL-01). Member session required. Reachable from the Guardian dashboard when adding or reactivating a seat.

## Contents

- A list of the account's profiles not currently on an active seat (never-activated or previously deactivated), each with its [Tier Badge](../components.md#tier-badge) and a checkbox to include it in this purchase.
- **Cadence selector — monthly or annual — shown once per account, not once per seat.** If the account already has an active subscription, this selector is hidden entirely; the existing cadence applies to every new seat automatically ([3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md)).
- The [Itemised Total](../components.md#itemised-total-by-tier) component, updating live as profiles are checked or unchecked.
- A note when a selected seat will be **prorated** rather than charged the full period rate, for accounts with an existing subscription mid-cycle.

## Continue

Proceeds to [Checkout](checkout.md) with the selected profiles and cadence carried forward. No charge occurs on this screen.

## Role Variations

Member only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04) — the itemised total's right-aligned figures in the LTR layout become left-aligned in RTL, not mirrored as a block.