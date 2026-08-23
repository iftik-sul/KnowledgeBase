---
project: 3i
module: platform
type: integration
status: current
updated: 2026-08-23
id: 3I-PLT-INT-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - integration
  - stripe
---

# Integration: Stripe

Contract with Stripe, the platform's sole payment rail (§14.1). Consumed entirely by `commerce`; documented here per [project-standards.md](/3i/project-standards.md#additional-document-types)'s `integration` document type, rather than inside `commerce` itself, since the contract is with the third party, not a `commerce`-owned behaviour.

---

## What 3i Uses

- **Checkout** — web-only hosted checkout ([3I-DEC-003](/3i/decisions/dec-003-web-only-stripe-checkout.md)), never embedded, never in the mobile apps.
- **Subscriptions with two line items per account** — adult-tier and minor-tier `SubscriptionItem`s on one `Subscription`, per [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md).
- **Customer Portal** — payment method changes and cancellation, not rebuilt in-house (FR-BILL-01).
- **Coupons** — the mechanism behind waiver discounts ([3I-DEC-010](/3i/decisions/dec-010-waiver-covers-all-seats.md)).
- **Webhooks** — the **only** path that grants or revokes access (FR-BILL-03). No client-side redirect ever flips an access flag.

## The One Rule That Matters Most

**Access is granted from webhooks only.** Every module that touches subscription state — `commerce` itself, and by extension anything gating on an active seat (`learning-delivery`'s enrolment check, `materials`' video access) — ultimately traces back to a `WebhookEvent` row (`commerce`'s own entity, not duplicated here). A support ticket asking "why does this account have access" should always resolve to a specific webhook event, never to an assumption about what a checkout success page returned.

## Failure Handling

Stripe Smart Retries plus a platform email sequence on payment failure; access suspends at final failure (FR-BILL-06). Reconciliation between Stripe's own record and the platform's mirrored `Subscription`/`SubscriptionItem` state should be periodically verifiable — not a baseline-specified requirement, standard practice for any payment integration where the third party is the actual source of truth.

## Related

| | |
| :---- | :---- |
| Owning module | `commerce` |
| Pricing model | [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md) |
| Web-only decision | [3I-DEC-003](/3i/decisions/dec-003-web-only-stripe-checkout.md) |
| No purchase surface in the apps (why checkout is web-only at all) | [app-store-compliance.md](/3i/app-store-compliance.md) |