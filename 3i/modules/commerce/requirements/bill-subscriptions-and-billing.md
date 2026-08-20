---
project: 3i
module: commerce
type: requirements
status: current
updated: 2026-08-20
id: 3I-CMR-REQ-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - billing
---

# Subscriptions and Billing

Baseline §14.1–14.2. Eight requirements, two amended by decision — [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) (seats as permanent grants) and [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md) (two-tier age-based pricing, replacing the baseline's flat per-seat price).

---

## Where Commerce Lives

| ID | Requirement |
| :---- | :---- |
| **FR-BILL-01** | All purchase, plan change, payment method, cancellation, and invoice functionality lives on the **web**. The Stripe Customer Portal handles payment methods and cancellation |
| **FR-BILL-02** | **The mobile apps contain no purchase surface.** No prices, no subscribe or upgrade buttons, no links to checkout, no text directing users to pay elsewhere |

**FR-BILL-02 is the requirement that makes the store-submission strategy work**, and it is enforced in three places at once — this module, `communication` (FR-NOT-06, no purchase prompts in push), and `platform` (NFR-15–21, the multiplatform-services model itself). It should not be treated as satisfied by simply omitting a "Subscribe" button; NFR-18 requires an account without an active subscription to see a neutral status message and a support email address only, with no URL, no price, and no call to action of any kind. This applies regardless of how many tiers or seats the underlying subscription has — the mobile status screen never breaks the itemised total down by tier either.

**This is exactly the requirement [`app-store-compliance.md`](/3i/open-questions.md#oq-09--app-store-compliancemd-not-yet-written) is meant to consolidate.** That document does not yet exist. Until it does, the mobile "subscription status" screen in this module's UI stage should be treated as provisional — written against FR-BILL-02 and NFR-18 directly, and revisited once the cross-cutting document lands.

---

## Access Grant

| ID | Requirement |
| :---- | :---- |
| **FR-BILL-03** | Access is granted from **Stripe webhooks only**, never from a client-side success redirect. Webhook handling is signature-verified and idempotent |

No exceptions. A checkout success page may show an optimistic "processing" state, but it must not itself flip any access flag — see [3I-CMR-DM-001](../data-model.md#webhookevent). This is the same discipline FR-BILL-06 depends on for failed-payment suspension: if access were ever granted client-side, there would be no single source of truth for when it should be revoked either.

---

## Seats and Pricing

| ID | Requirement |
| :---- | :---- |
| **FR-BILL-04** | Seat count is a **Stripe quantity**. Adding a profile beyond the purchased seats prompts a seat purchase |

**A seat is a permanent, non-transferable enrolment grant to one profile, not a viewing slot** — [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md). This resolves an internal conflict the baseline left unstated: FR-ENR-01 (enrolment needs a seat) and FR-AUTH-12 (concurrent streams capped by seats) cannot both be independently true readings of "seat" without one being a consequence of the other. Enrolment is the real event; the streaming cap follows automatically and must not be built as a second, independent check.

**FR-BILL-04's single "Stripe quantity" is now two quantities, one per age tier** — [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md). Confirmed pricing:

| Tier | Monthly | Annual |
| :---- | ----: | ----: |
| Adult (18+) | AUD $9.99 | AUD $99.99 |
| Under 18 | AUD $5.99 | AUD $49.99 |

A learner's tier is read from their date of birth at the moment of activation. Total charge is the sum across both tiers, at one cadence chosen for the whole subscription — Stripe does not support mixed intervals within one subscription. Turning 18 moves a seat from the minor item to the adult item at the account's **next renewal**, never mid-cycle.

The subscription flow this requirement drives: create account (free) → create profile (free) → **activate** a specific profile by paying for a seat at its tier's price → optionally cancel (deactivate, history preserved, access continues to period end) → optionally reactivate (pay again — there is no free trial, so reactivation is always a genuine second payment, re-evaluated against the learner's current age).

---

## Billing Identity

| ID | Requirement |
| :---- | :---- |
| **FR-BILL-05** | The **billing contact is separable from the account identity** — name and email on the Stripe customer may differ from the account holder's. For accounts with minor profiles, the billing contact defaults to the guardian |

**Since [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) removed standalone accounts under 18, every account holder is an adult by construction**, and every minor on the platform is a profile beneath one. The "defaults to guardian" language describes the ordinary case — the account holder billing themselves — rather than carving out an exception for a different kind of account holder. There is no scenario in this system where the billing contact is a minor.

---

## Failure Handling

| ID | Requirement |
| :---- | :---- |
| **FR-BILL-06** | Failed payments use **Stripe Smart Retries** plus a platform email sequence. Access is suspended at final failure |

Suspension is a `Subscription.status` transition triggered by a webhook (`invoice.payment_failed` reaching Stripe's final retry), not by a scheduled job independently polling for overdue invoices. Suspension applies to the whole subscription, not per tier — a family does not lose only its children's seats while adult seats stay active. See [3I-CMR-DM-001](../data-model.md#subscription).

---

## Pricing Storage

| ID | Requirement |
| :---- | :---- |
| **FR-BILL-07** | Prices are stored and displayed **GST-inclusive**, in **integer cents** |
| **FR-BILL-08** | Invoices record GST separately for reporting |

**Four stored price values now, not two** — one per tier × cadence combination, per [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md). Integer cents avoids floating-point rounding on money; GST is broken out only at the reporting layer (FR-REP-05, gross revenue with GST separated), not carried as a separate stored price per line item.

---

## Open Against This Requirement Set

**Per-seat price is resolved** — see [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md).

**GST treatment for overseas learners** remains outstanding, from the client's accountant, and affects FR-BILL-08's invoice line-item logic for non-Australian billing addresses.

**Seat cancellation running to period-end, rather than a prorated refund, is assumed rather than explicitly confirmed by the client** — flagged in [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md#cost--open-items-introduced-by-this-decision).

---

## Acceptance Criteria

1. No screen, string, or asset in either mobile app references price or purchase, at any tier.
2. A subscription created in Stripe grants access **only after the webhook is processed** — never on redirect.
3. A fourth device registration, a seat cancellation, a tier reprice at renewal, and a failed-payment suspension are each traceable to a specific webhook event or admin action in the audit log.
4. A checkout with 2 adult and 2 minor seats totals AUD $31.96/month or AUD $299.96/year exactly, matching the stored integer-cent values with GST included.
5. A minor-tier seat's Learner turning 18 does not change that period's invoice; the next renewal reflects the adult-tier price.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-CMR-DM-001](../data-model.md) |
| Seat as enrolment grant | [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) |
| Two-tier age-based pricing | [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md) |
| No standalone minors — billing contact is always an adult | [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) |
| App store compliance (not yet written) | [OQ-09](/3i/open-questions.md#oq-09--app-store-compliancemd-not-yet-written) |
| Waivers | [3I-CMR-REQ-002](wav-waivers.md) |
| Refunds | [3I-CMR-REQ-003](ref-refunds.md) |
