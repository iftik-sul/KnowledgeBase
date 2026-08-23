---
project: 3i
module: commerce
type: data-model
status: current
updated: 2026-08-20
id: 3I-CMR-DM-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - data-model
  - commerce
---

# Commerce — Data Model

Entities owned by this module. Other modules reference these; they do not restate them.

**The seat/Learner split.** `identity-and-access` owns the `Learner` record and its four-state activation lifecycle (never-activated, active, inactive, deleted). This module owns the **Subscription** that funds activation and the **seat quantities** as Stripe subscription line items. Activating a profile is a write from this module into `identity-and-access`'s state machine, not a field this module duplicates. See [3I-IDA-DM-001](/3i/modules/identity-and-access/data-model.md#activation-state--introduced-by-decision-not-by-the-baseline).

---

## Subscription

| Field | Notes |
| :---- | :---- |
| Account | Owning account. One subscription per account |
| Stripe subscription ID | Source of truth lives in Stripe; this is a mirror for querying |
| Cadence | Monthly or annual. Chosen once at first seat activation, shared by both subscription items — Stripe does not support mixed intervals within one subscription |
| Billing anchor date | **Set once, by whichever seat activates first on this account.** Every subsequent seat, at any tier, prorates in against this same anchor rather than starting its own cycle — [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md#worked-example--four-profiles-four-join-dates-one-anchor). Reset only if the subscription is fully cancelled (both items reach zero) and later restarted |
| Status | Active, past due, suspended, cancelled — mirrors Stripe subscription status |
| Current period end | Renewal date, derived from the anchor |
| Waiver | Nullable reference to an active **Waiver** (below) |

**Access is granted from Stripe webhooks only, never a client-side success redirect** (FR-BILL-03). Webhook handling is signature-verified and idempotent — see **WebhookEvent** below.

**There is one renewal date per account, not one per seat.** A profile activated mid-cycle is charged a one-time prorated amount for the remainder of the current period, then folds into the same renewal date as every other seat on the account — regardless of tier or join date. See the worked four-profile example in [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md#worked-example--four-profiles-four-join-dates-one-anchor).

Failed payments use Stripe Smart Retries plus a platform email sequence; access is suspended at final failure (FR-BILL-06) — this is a `status` transition on this record, driven by webhook, never by a scheduled job guessing at Stripe's retry state.

### SubscriptionItem — two-tier seat pricing

**Introduced by [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md), replacing a single flat `seatQuantity` field.** A Subscription has up to two SubscriptionItems, one per tier:

| Field | Notes |
| :---- | :---- |
| Subscription | Owning subscription |
| Tier | `adult` or `minor` |
| Stripe price ID | One of four Stripe Price objects — `price_seat_adult_monthly`, `price_seat_adult_annual`, `price_seat_minor_monthly`, `price_seat_minor_annual` |
| Quantity | Stripe quantity for this item. Zero-quantity items are removed, not retained |
| Price snapshot | GST-inclusive, stored in integer cents (FR-BILL-07). Four possible values, one per tier × cadence combination |

**A learner's tier is set by age at the moment of activation**, read from the Learner's date of birth (FR-FAM-07, not user-editable). Activating a profile increments the matching item's quantity, creating that item if the account has no seat of that tier yet. Deactivating decrements it; if both items reach zero, the Subscription is cancelled entirely.

**Seat activation prorates immediately** — Stripe's standard mid-cycle proration. **Seat cancellation runs to the end of the current paid period**, matching the no-refund-on-cancellation pattern elsewhere in the baseline (FR-BAT-05) — the Learner stays active until the period ends rather than losing access instantly.

**Ageing from minor to adult reprices at the next renewal, not mid-cycle.** A scheduled process compares each active minor-tier seat's Learner DOB against today and, where it now indicates 18+, moves that unit of quantity from the minor item to the adult item effective at the Subscription's next renewal — mirroring FR-WAV-03's no-mid-cycle-proration principle for waivers rather than inventing a new billing behaviour. This process is new infrastructure with no baseline precedent; see the decision's cost section.

---

## BillingContact

| Field | Notes |
| :---- | :---- |
| Subscription | Owning subscription |
| Name, email | May differ from the account holder's identity (FR-BILL-05) |
| Defaults to guardian | For accounts with minor profiles — which, per [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md), is every account with any learner under 18, since no minor holds their own account |

**Since every account is 18+ ([3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md)), the billing contact is always an adult by construction** — the "defaults to guardian" language in FR-BILL-05 describes the common case (the account holder billing themselves) rather than a special exception, because there is no other kind of account holder.

---

## WebhookEvent

| Field | Notes |
| :---- | :---- |
| Stripe event ID | Unique. The idempotency key (FR-BILL-03) |
| Type | `checkout.session.completed`, `invoice.paid`, `invoice.payment_failed`, `customer.subscription.updated`, `subscription_schedule.updated` (ageing-up reprice), etc. |
| Signature verified | Boolean. Unverified events are rejected before processing |
| Processed at | Null until successfully applied |

**Every access-granting or access-revoking change to a Subscription, a SubscriptionItem quantity, or a Learner's activation state must trace back to a row here.** A support ticket that asks "why does this account have access, and at which tier" should always resolve to a specific webhook event, not to an assumption about what the client-side checkout flow returned.

---

## Waiver

| Field | Notes |
| :---- | :---- |
| Requester | Account (always the billing contact — an adult) |
| Written explanation | FR-WAV-01 |
| Covered profile | **The one Learner this waiver is for**, named in the request itself — [3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md). Not editable after submission short of a fresh request |
| Evidence files | Optional. Private bucket, never CDN-cached, accessed only via short-lived signed URLs, every access logged (FR-WAV-07) |
| Tier | One of four fixed discount values: 25%, 50%, 75%, 100% (FR-WAV-02) — **not** the same "tier" as a SubscriptionItem's adult/minor tier; this field is the discount percentage |
| Status | Pending, approved, revoked, expired |
| Reviewer | Admin account |
| Decision date | |
| Effective date | Next renewal — no mid-cycle proration (FR-WAV-03) |
| Expiry date | 12 months from effective date (FR-WAV-04) |
| Revocation reason | Nullable. Set only on admin revocation (FR-WAV-05) |

**Applies to the whole subscription, across both seat tiers** — [3I-DEC-010](/3i/decisions/dec-010-waiver-covers-all-seats.md). Implemented as a Stripe coupon on the subscription, which discounts every line item naturally — including both the adult and minor SubscriptionItems — rather than requiring bespoke per-tier logic. Seats added during a waived period, of either tier, inherit the discount for the remainder of that period.

**While a waiver is active, its account is capped at the one covered profile** — [3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md). On approval, every other profile on the account is automatically deactivated in the same action that activates the waiver — not a separate step, not a pending state. Deactivated profiles follow the standard deactivation pattern (history preserved, reactivatable later at full price). Creating a second profile is blocked outright for the duration. On revocation or expiry, the cap lifts and the account reverts to the normal six-profile limit.

**A 100% waiver is a live subscription with a 100% discount, not a flagged free account** (FR-WAV-06). Admin-created free accounts are a separate mechanism this data model does not cover.

**Evidence files are automatically deleted 12 months after the decision** (FR-WAV-08), independent of whether the waiver itself is later revoked early. The audit trail (requester, submission, reviewer, decision, tier, effective and expiry dates, revocation and reason — FR-WAV-09) persists after the evidence file is purged; only the file goes. **The covered profile and any auto-deactivated profiles are part of this same audit trail.**

---

## Refund

| Field | Notes |
| :---- | :---- |
| Subscription | Owning subscription |
| Type | Self-service first-payment (FR-REF-01) or admin-discretion renewal (FR-REF-02) |
| Requested by | Account |
| Processed by | Nullable — null for self-service, an admin account for discretionary refunds |
| Amount | |
| Reason | Required for admin-discretion refunds |
| Access revoked at | Set immediately on refund (FR-REF-03) |

**Certificates already issued remain valid after a refund** (FR-REF-04) — the same snapshotting protection that survives profile deletion ([3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md)) applies here without any special-casing, because certificate validity was never conditional on subscription status in the first place.

The published refund policy states that Australian Consumer Law guarantees apply regardless of policy terms (FR-REF-05) — this is copy on the CMS refund-policy page, not a field on this record.

---

## Referenced By

| Module | Reads |
| :---- | :---- |
| `identity-and-access` | Subscription status — determines whether a Learner may be activated, and at which tier |
| `learning-delivery` | Subscription status, seat availability — gates enrolment (FR-ENR-01) |
| `communication` | Waiver/Subscription status is **not** read for chat access — chat is age-derived, never billing-derived |
| `platform` | Stripe integration contract; the Subscription, SubscriptionItem, and WebhookEvent records are the primary consumers of that contract |
| `reporting` | Subscription, SubscriptionItem, Waiver, Refund — revenue, churn, and waivers-granted reports, now broken out by seat tier (FR-REP-01) |

## Referenced

| Entity | Owned by | Read here |
| :---- | :---- | :---- |
| Account | `identity-and-access` | Owner of Subscription; identity of BillingContact absent an override |
| Learner | `identity-and-access` | Target of seat activation/deactivation and the tier read from its date of birth; never duplicated here |
