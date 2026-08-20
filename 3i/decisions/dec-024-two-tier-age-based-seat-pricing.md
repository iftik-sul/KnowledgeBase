---
project: 3i
type: decision
status: current
updated: 2026-08-20
id: 3I-DEC-024
tags: [decision, billing, pricing, scope-change]
---

# Two-Tier, Age-Based Seat Pricing

## Context

Client confirmed per-seat pricing 2026-08-20, resolving §22.2 dependency #1 and [OQ-07](../open-questions.md). Two tiers, not the single flat "additional seat" price the baseline describes:

| Tier | Monthly | Annual |
| :---- | ----: | ----: |
| Adult (18+) | AUD $9.99 | AUD $99.99 |
| Under 18 | AUD $5.99 | AUD $49.99 |

The adult tier matches the SRD's existing base plan price exactly. That is the tell: the base price was always describing the cost of one adult seat, not a separate flat subscription fee with a free first seat bundled in. The "included seat" language in §14.1 is reinterpreted accordingly — there is no bundled free seat. Every seat, including the first, is priced by its occupant's tier.

Alongside the price, the client asked the real operating question: how is payment calculated and maintained across a mixed cart — for example, 2 adult profiles and 2 children profiles under one account.

## Decision

1. **No flat subscription fee.** Total charge = (active adult seats × adult tier price) + (active minor seats × minor tier price), at the account's chosen cadence.

2. **Modelled as two Stripe subscription items on one Stripe Subscription per account** — an adult-tier item and a minor-tier item, each with its own quantity — rather than two separate subscriptions. One subscription keeps one invoice, one payment method, and one renewal date, which two subscriptions would not.
   - `price_seat_adult_monthly` / `price_seat_adult_annual` — $9.99 / $99.99
   - `price_seat_minor_monthly` / `price_seat_minor_annual` — $5.99 / $49.99

3. **Billing cadence is chosen once, for the whole subscription**, at first seat activation. Stripe does not support mixing intervals within one subscription. Changing cadence later is an account-wide plan change, not a per-seat one.

4. **A learner's tier is set by age at the moment of activation**, read from the profile's date of birth (FR-FAM-07, not user-editable). Activating a profile increments the matching item's quantity, creating that item on the subscription if it is the first seat of that tier. Deactivating decrements it; if both items reach zero, the subscription is cancelled.

5. **Ageing from minor to adult reprices at the next renewal, not immediately.** A learner turning 18 does not trigger a mid-cycle charge. A scheduled job moves that seat's quantity from the minor item to the adult item effective at the account's next renewal — mirroring the no-mid-cycle-proration principle already established for waivers (FR-WAV-03) rather than inventing a new billing behaviour.

6. **Seat activation prorates immediately** — adding a profile mid-cycle charges the prorated difference right away, Stripe's standard behaviour. **Seat cancellation runs to the end of the current paid period** — the profile stays active until then rather than losing access instantly, consistent with the no-refund-on-cancellation pattern used elsewhere in the baseline (FR-BAT-05).

7. **A waiver coupon still applies to the whole subscription** ([3I-DEC-010](dec-010-waiver-covers-all-seats.md)) — Stripe percentage-off coupons discount every line item automatically, so the two-tier split needs no additional waiver logic.

## Consequences

- **FR-BILL-04 and FR-BILL-07 are amended.** "Seat count is a Stripe quantity" (singular) becomes two quantities, one per tier, on one subscription.
- **[3I-CMR-DM-001](/3i/modules/commerce/data-model.md)'s Subscription entity changes** from a single `seatQuantity` field to two tier-scoped quantities. Updated in the same change as this decision.
- **The client's own example checks out cleanly:** 2 adult + 2 minor seats → monthly $9.99×2 + $5.99×2 = $31.96; annual $99.99×2 + $49.99×2 = $299.96.
- **Checkout must show a live itemised total**, split by tier, as profiles are added to the cart — not a single flat figure. Noted against the Checkout screen in [ui/README.md](/3i/modules/commerce/ui/README.md).
- Revenue reporting (FR-REP-01) now has two seat-price dimensions to break out instead of one flat per-seat figure.

## Cost / Open Items Introduced By This Decision

- **The ageing-up reprice job is new infrastructure.** Nothing in the baseline anticipated a scheduled age-crossing check. It is well-defined (scan active minor-tier seats, compare DOB to today, move quantity at the next renewal boundary) but did not exist as a requirement before this decision, and should be scoped explicitly into the commerce backend spec.
- **Seat cancellation running to period-end, rather than refunding the unused portion, is assumed rather than confirmed.** It matches the existing no-refund pattern (FR-BAT-05), but this is the first time that pattern applies to commerce directly rather than a live-session batch. Worth a one-line confirmation from the client, not a blocker to proceeding.
- **Bundled base-price language throughout the SRD and project documentation needs correcting** wherever it currently reads "$9.99/mo includes one seat" — see Related for the files updated alongside this decision.

## Related

| | |
| :---- | :---- |
| Client dependency this resolves | §22.2 item 1 / [OQ-07](/3i/open-questions.md) |
| Amends | FR-BILL-04, FR-BILL-07 |
| Interacts with | [3I-DEC-009](dec-009-seats-as-account-pool.md) — seat as permanent grant; [3I-DEC-010](dec-010-waiver-covers-all-seats.md) — waiver covers all seats |
| Data model updated | [3I-CMR-DM-001](/3i/modules/commerce/data-model.md) |
| Requirements updated | [3I-CMR-REQ-001](/3i/modules/commerce/requirements/bill-subscriptions-and-billing.md) |
