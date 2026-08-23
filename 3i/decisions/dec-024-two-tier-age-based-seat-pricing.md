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

Alongside the price, the client asked the real operating question: how is payment calculated and maintained across a mixed cart — for example, 2 adult profiles and 2 children profiles under one account, and, in a follow-up, four profiles joining on four different dates.

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

8. **The subscription has one renewal anchor, set by whichever seat activates first on that account.** Every seat added afterward — any tier, any date — is prorated for the remainder of the current period and then folds into that same shared renewal date. There is no per-seat billing anniversary.

### Worked example — four profiles, four join dates, one anchor

An account with adult A activating 13 Jan, adult B activating 21 Feb, minor D activating 3 Mar, and minor C activating 28 Mar, all monthly:

| Date | Event | Effect |
| :---- | :---- | :---- |
| 13 Jan | A (adult) activates | Subscription created. **Anchor = 13th of every month.** Full charge $9.99 |
| 13 Feb | Renewal | Adult qty 1 → $9.99 |
| 21 Feb | B (adult) activates | Mid-cycle (13 Feb–13 Mar period). Adult qty → 2. **Prorated charge** for the 20 remaining days — not a new subscription, not a new anchor |
| 3 Mar | D (minor) activates | Still inside the 13 Feb–13 Mar period. Minor item created, qty 1. **Prorated charge** for the 10 remaining days |
| 13 Mar | Renewal | Adult qty 2 × $9.99 + minor qty 1 × $5.99 = $25.97 |
| 28 Mar | C (minor) activates | Mid-cycle (13 Mar–13 Apr period). Minor qty → 2. **Prorated charge** for the 16 remaining days |
| 13 Apr onward | Steady state | Adult qty 2 × $9.99 + minor qty 2 × $5.99 = **$31.96/month**, every seat renewing together regardless of original join date |

This converges to the same $31.96 monthly figure as the earlier 2-adult/2-minor example — join order and join date only affect the one-time prorated amount charged at activation; the ongoing steady-state charge depends only on final tier composition.

**If an account's seats are ever all cancelled to zero, the Stripe subscription is cancelled** (item 4 above), and the next seat activated after that starts an entirely new anchor date — it does not inherit the old one.

## Consequences

- **FR-BILL-04 and FR-BILL-07 are amended.** "Seat count is a Stripe quantity" (singular) becomes two quantities, one per tier, on one subscription, sharing one renewal anchor.
- **[3I-CMR-DM-001](/3i/modules/commerce/data-model.md)'s Subscription entity changes** from a single `seatQuantity` field to two tier-scoped quantities plus an explicit anchor date. Updated in the same change as this decision.
- **The client's own examples check out cleanly:** 2 adult + 2 minor seats joining together → monthly $9.99×2 + $5.99×2 = $31.96; the same household joining on four staggered dates converges to the identical $31.96 steady state, differing only in the one-off prorated charges along the way.
- **Checkout must show a live itemised total**, split by tier, as profiles are added to the cart — not a single flat figure. Noted against the Checkout screen in [ui/README.md](/3i/modules/commerce/ui/README.md).
- **Billing history / invoices must clearly label prorated line items as partial-period charges**, distinct from full-period renewal charges — a guardian looking at their first few invoices after adding seats mid-cycle should not mistake a prorated amount for the ongoing price.
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