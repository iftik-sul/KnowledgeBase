---
project: 3i
module: commerce
type: ui-spec
status: current
updated: 2026-08-20
id: 3I-CMR-UI-004
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - billing
---

# Screen: Billing Portal Redirect

Satisfies: FR-BILL-01

---

## Purpose

Hand off to the Stripe Customer Portal for payment method changes and cancellation — functionality this module deliberately does not rebuild in-house (FR-BILL-01).

## Access Gate

Web only. Member (their own account) or Admin.

## Contents

This is a thin screen, not a form: a short explanation of what the Customer Portal handles (payment methods, invoice history, full cancellation) and the [Stripe-Hosted Redirect Button](../components.md#stripe-hosted-redirect-button).

**Cancelling the whole subscription here is different from cancelling one seat** on [Seat Management](seat-management.md) — this screen's cancellation ends the entire Subscription (all SubscriptionItems, both tiers) rather than one seat's quantity. The copy on this screen should make that distinction explicit, since the two actions look similar to a Member but have very different consequences for a multi-profile household.

## Role Variations

Member and Admin, same content.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04) for the explanatory copy; the Stripe-hosted portal itself is outside this module's control.
