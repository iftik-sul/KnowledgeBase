---
project: 3i
module: commerce
type: ui-spec
status: current
updated: 2026-08-20
id: 3I-CMR-UI-COMP
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - components
---

# Commerce — Shared Components

Documented once here. Screens link to this file rather than restating.

---

## Itemised Total (by tier)

Used on: [Checkout](screens/checkout.md), [Seat management](screens/seat-management.md).

Required by [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md): a live total broken out by tier as profiles are added or removed from the cart — never a single flat figure. Example rendering:

```
2 adult seats  × $9.99   = $19.98
2 child seats  × $5.99   = $11.98
                   Total   $31.96 / month
```

**Recomputes live as seats are added or removed**, before checkout is confirmed. A waived account (see [3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md)) shows the discount applied to the single covered seat, not a second breakdown — the component does not need a distinct waived-state layout, the numbers simply resolve to a smaller total.

**Prorated line items are visually distinguished from full-period renewal charges** on any invoice or billing-history view — a guardian looking at their first invoice after adding a seat mid-cycle should not mistake a one-off partial charge for the ongoing price ([3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md#consequences)).

## Tier Badge

Used on: [Seat management](screens/seat-management.md), [Waiver request form](screens/waiver-request-form.md), [Waiver admin review](screens/waiver-admin-review.md).

Displays `Adult` or `Minor` against a profile, read from the profile's stored `Tier` field ([3I-IDA-DM-001](/3i/modules/identity-and-access/data-model.md#tier--adult-or-minor-stored-not-derived)) — never recalculated live from date of birth in the UI layer either, for the same reason it isn't recalculated live in the data model.

## Stripe-Hosted Redirect Button

Used on: [Checkout](screens/checkout.md), [Billing portal redirect](screens/billing-portal-redirect.md).

A single button that hands off to a Stripe-hosted page (Checkout or Customer Portal) and returns to an in-app confirmation screen on completion. **The return screen never grants access itself** — access is granted only by the webhook, per FR-BILL-03. The return screen shows an optimistic "processing" state and polls or waits for the webhook-driven state to update; it does not flip any access flag on arrival.

**Web only.** This component does not exist on mobile — see [app-store-compliance.md](/3i/app-store-compliance.md).