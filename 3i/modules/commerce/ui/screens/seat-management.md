---
project: 3i
module: commerce
type: ui-spec
status: current
updated: 2026-08-20
id: 3I-CMR-UI-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - seats
---

# Screen: Seat Management

Satisfies: FR-BILL-04, FR-BILL-06

---

## Purpose

View and manage which profiles currently hold a seat, add new seats, and cancel existing ones.

## Access Gate

Web only. Member (their own account) or Admin (any account, for support purposes).

## Contents

- Every profile on the account with its [Tier Badge](../components.md#tier-badge) and seat state — Active, Never activated, Inactive (Cancelled) — per [3I-IDA-DM-001](/3i/modules/identity-and-access/data-model.md#activation-state--introduced-by-decision-not-by-the-baseline).
- **"Add seat"** for a never-activated or inactive profile → [Pricing / Plan Selection](pricing-plan-selection.md).
- **"Cancel seat"** for an active profile — a confirmation step states plainly that the profile stays active until the end of the current paid period, then deactivates (not immediately), and that history is preserved and reactivation later is a fresh payment ([3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md)).
- The account's current [Itemised Total](../components.md#itemised-total-by-tier) and billing anchor date, so a Member can see when the next renewal charges and at what amount.
- **If the account has an active waiver** ([3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md)), the "Add seat" action is **absent, not disabled**, for every profile except the one covered by the waiver — consistent with how this module treats gated actions elsewhere (absent, matching the identity-and-access convention for the guardian age gate).
- A banner explaining the suspended state if `Subscription.status` is `past_due` or `suspended` (FR-BILL-06), with no purchase action offered until payment is resolved through the Stripe Customer Portal (see [Billing Portal Redirect](billing-portal-redirect.md)).

## Role Variations

**Member:** sees and acts on their own account only.
**Admin:** same view, any account, for support. Every admin action here is logged the same way as any other webhook-driven or admin-driven Subscription change ([3I-CMR-DM-001](/3i/modules/commerce/data-model.md#webhookevent)).

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04) — dense tabular pricing data, flagged in [ui/README.md](../README.md#checkout--two-tier-itemisation-requirement) as a layout worth extra contrast-review attention.
