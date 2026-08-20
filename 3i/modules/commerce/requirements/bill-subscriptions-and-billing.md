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

Baseline §14.1–14.2. Eight requirements, none amended by decision — the two commerce decisions ([3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md), [3I-DEC-010](/3i/decisions/dec-010-waiver-covers-all-seats.md)) sharpen how seats and waivers behave but do not change the BILL requirements themselves.

---

## Where Commerce Lives

| ID | Requirement |
| :---- | :---- |
| **FR-BILL-01** | All purchase, plan change, payment method, cancellation, and invoice functionality lives on the **web**. The Stripe Customer Portal handles payment methods and cancellation |
| **FR-BILL-02** | **The mobile apps contain no purchase surface.** No prices, no subscribe or upgrade buttons, no links to checkout, no text directing users to pay elsewhere |

**FR-BILL-02 is the requirement that makes the store-submission strategy work**, and it is enforced in three places at once — this module, `communication` (FR-NOT-06, no purchase prompts in push), and `platform` (NFR-15–21, the multiplatform-services model itself). It should not be treated as satisfied by simply omitting a "Subscribe" button; NFR-18 requires an account without an active subscription to see a neutral status message and a support email address only, with no URL, no price, and no call to action of any kind.

**This is exactly the requirement [`app-store-compliance.md`](/3i/open-questions.md#oq-09--app-store-compliancemd-not-yet-written) is meant to consolidate.** That document does not yet exist. Until it does, the mobile "subscription status" screen in this module's UI stage should be treated as provisional — written against FR-BILL-02 and NFR-18 directly, and revisited once the cross-cutting document lands.

---

## Access Grant

| ID | Requirement |
| :---- | :---- |
| **FR-BILL-03** | Access is granted from **Stripe webhooks only**, never from a client-side success redirect. Webhook handling is signature-verified and idempotent |

No exceptions. A checkout success page may show an optimistic "processing" state, but it must not itself flip any access flag — see [3I-CMR-DM-001](../data-model.md#webhookevent). This is the same discipline FR-BILL-06 depends on for failed-payment suspension: if access were ever granted client-side, there would be no single source of truth for when it should be revoked either.

---

## Seats

| ID | Requirement |
| :---- | :---- |
| **FR-BILL-04** | Seat count is a **Stripe quantity**. Adding a profile beyond the purchased seats prompts a seat purchase |

**A seat is a permanent, non-transferable enrolment grant to one profile, not a viewing slot** — [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md). This resolves an internal conflict the baseline left unstated: FR-ENR-01 (enrolment needs a seat) and FR-AUTH-12 (concurrent streams capped by seats) cannot both be independently true readings of "seat" without one being a consequence of the other. Enrolment is the real event; the streaming cap follows automatically and must not be built as a second, independent check.

The subscription flow this requirement drives: create account (free) → create profile (free) → **activate** a specific profile by paying for a seat → optionally cancel (deactivate, history preserved) → optionally reactivate (pay again — there is no free trial, so reactivation is always a genuine second payment).

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

Suspension is a `Subscription.status` transition triggered by a webhook (`invoice.payment_failed` reaching Stripe's final retry), not by a scheduled job independently polling for overdue invoices. See [3I-CMR-DM-001](../data-model.md#subscription).

---

## Pricing Storage

| ID | Requirement |
| :---- | :---- |
| **FR-BILL-07** | Prices are stored and displayed **GST-inclusive**, in **integer cents** |
| **FR-BILL-08** | Invoices record GST separately for reporting |

Integer cents avoids floating-point rounding on money; GST is broken out only at the reporting layer (FR-REP-05, gross revenue with GST separated), not carried as a separate stored price.

---

## Open Against This Requirement Set

**Per-seat price is not yet confirmed by the client** — §22.2 dependency #1, needed before this module's checkout flow can be built against a real Stripe price object. The base plan prices ($9.99/$99.99 GST-inclusive) are confirmed; only the additional-seat charge is outstanding.

**GST treatment for overseas learners** is also outstanding, from the client's accountant, and affects FR-BILL-08's invoice line-item logic for non-Australian billing addresses.

---

## Acceptance Criteria

1. No screen, string, or asset in either mobile app references price or purchase.
2. A subscription created in Stripe grants access **only after the webhook is processed** — never on redirect.
3. A fourth device registration, a seat cancellation, and a failed-payment suspension are each traceable to a specific webhook event or admin action in the audit log.
4. Prices displayed anywhere in the web app match the stored integer-cent value exactly, with GST included.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-CMR-DM-001](../data-model.md) |
| Seat as enrolment grant | [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) |
| No standalone minors — billing contact is always an adult | [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) |
| App store compliance (not yet written) | [OQ-09](/3i/open-questions.md#oq-09--app-store-compliancemd-not-yet-written) |
| Waivers | [3I-CMR-REQ-002](wav-waivers.md) |
| Refunds | [3I-CMR-REQ-003](ref-refunds.md) |
