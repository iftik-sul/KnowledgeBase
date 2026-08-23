---
project: 3i
module: commerce
type: ui-spec
status: current
updated: 2026-08-20
id: 3I-CMR-UI-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - checkout
---

# Screen: Checkout

Satisfies: FR-BILL-01, FR-BILL-03, FR-BILL-07

---

## Purpose

Confirm the cart built on [Pricing / Plan Selection](pricing-plan-selection.md) and hand off to Stripe-hosted Checkout for payment.

## Access Gate

Web only (FR-BILL-01). Member session required. Not reachable directly — always arrives with a cart carried forward from Pricing / Plan Selection.

## Contents

- Final [Itemised Total](../components.md#itemised-total-by-tier), GST-inclusive, matching the stored integer-cent values exactly (FR-BILL-07).
- Billing contact fields, defaulting to the account holder's own name and email but editable (FR-BILL-05) — this is where a guardian confirms or changes who Stripe bills, separate from who's logged in.
- The [Stripe-Hosted Redirect Button](../components.md#stripe-hosted-redirect-button), which hands off to Stripe Checkout.

## On Return From Stripe

**Access is not granted here.** The return screen shows an optimistic "processing your subscription" state and waits for the webhook-driven state change (FR-BILL-03) — see [3I-CMR-DM-001](/3i/modules/commerce/data-model.md#webhookevent). If the webhook hasn't landed within a reasonable window, the screen shows a "this is taking longer than usual, check back shortly" message rather than a false confirmation or a false failure.

## Role Variations

Member only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04). The Stripe-hosted page itself is outside this module's control once redirected.