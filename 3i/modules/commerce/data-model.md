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

**The seat/Learner split.** `identity-and-access` owns the `Learner` record and its four-state activation lifecycle (never-activated, active, inactive, deleted). This module owns the **Subscription** that funds activation and the **seat quantity** as a Stripe line item. Activating a profile is a write from this module into `identity-and-access`'s state machine, not a field this module duplicates. See [3I-IDA-DM-001](/3i/modules/identity-and-access/data-model.md#activation-state--introduced-by-decision-not-by-the-baseline).

---

## Subscription

| Field | Notes |
| :---- | :---- |
| Account | Owning account. One subscription per account |
| Stripe subscription ID | Source of truth lives in Stripe; this is a mirror for querying |
| Plan | Monthly or annual (FR-BILL-01 defaults; §14.1) |
| Seat quantity | Stripe quantity (FR-BILL-04). One seat included; additional seats are a per-seat charge |
| Status | Active, past due, suspended, cancelled — mirrors Stripe subscription status |
| Current period end | Renewal date |
| Waiver | Nullable reference to an active **Waiver** (below) |
| Price snapshot | GST-inclusive, stored in integer cents (FR-BILL-07) |

**Access is granted from Stripe webhooks only, never a client-side success redirect** (FR-BILL-03). Webhook handling is signature-verified and idempotent — see **WebhookEvent** below.

**Seat count changes are billing events, not profile events.** Adding a profile beyond purchased seats prompts a seat purchase (FR-BILL-04); the resulting Stripe quantity change is what activates the corresponding `Learner` in `identity-and-access`. Cancelling a seat is the same relationship in reverse: it deactivates the bound `Learner`, it does not touch this Subscription's plan.

Failed payments use Stripe Smart Retries plus a platform email sequence; access is suspended at final failure (FR-BILL-06) — this is a `status` transition on this record, driven by webhook, never by a scheduled job guessing at Stripe's retry state.

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
| Type | `checkout.session.completed`, `invoice.paid`, `invoice.payment_failed`, `customer.subscription.updated`, etc. |
| Signature verified | Boolean. Unverified events are rejected before processing |
| Processed at | Null until successfully applied |

**Every access-granting or access-revoking change to a Subscription or a Learner's activation state must trace back to a row here.** A support ticket that asks "why does this account have access" should always resolve to a specific webhook event, not to an assumption about what the client-side checkout flow returned.

---

## Waiver

| Field | Notes |
| :---- | :---- |
| Requester | Account (always the billing contact — an adult) |
| Written explanation | FR-WAV-01 |
| Evidence files | Optional. Private bucket, never CDN-cached, accessed only via short-lived signed URLs, every access logged (FR-WAV-07) |
| Tier | One of four fixed values: 25%, 50%, 75%, 100% (FR-WAV-02) |
| Status | Pending, approved, revoked, expired |
| Reviewer | Admin account |
| Decision date | |
| Effective date | Next renewal — no mid-cycle proration (FR-WAV-03) |
| Expiry date | 12 months from effective date (FR-WAV-04) |
| Revocation reason | Nullable. Set only on admin revocation (FR-WAV-05) |

**Applies to the whole subscription, additional seats included** — [3I-DEC-010](/3i/decisions/dec-010-waiver-covers-all-seats.md). Implemented as a Stripe coupon on the subscription, which discounts every line naturally rather than requiring bespoke seats-excluded logic. Seats added during a waived period inherit the discount for the remainder of that period.

**A 100% waiver is a live subscription with a 100% discount, not a flagged free account** (FR-WAV-06). Admin-created free accounts are a separate mechanism this data model does not cover.

**Evidence files are automatically deleted 12 months after the decision** (FR-WAV-08), independent of whether the waiver itself is later revoked early. The audit trail (requester, submission, reviewer, decision, tier, effective and expiry dates, revocation and reason — FR-WAV-09) persists after the evidence file is purged; only the file goes.

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
| `identity-and-access` | Subscription status — determines whether a Learner may be activated |
| `learning-delivery` | Subscription status, seat availability — gates enrolment (FR-ENR-01) |
| `communication` | Waiver/Subscription status is **not** read for chat access — chat is age-derived, never billing-derived |
| `platform` | Stripe integration contract; the Subscription and WebhookEvent records are the primary consumers of that contract |
| `reporting` | Subscription, Waiver, Refund — revenue, churn, and waivers-granted reports (FR-REP-01) |

## Referenced

| Entity | Owned by | Read here |
| :---- | :---- | :---- |
| Account | `identity-and-access` | Owner of Subscription; identity of BillingContact absent an override |
| Learner | `identity-and-access` | Target of seat activation/deactivation; never duplicated here |
