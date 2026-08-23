---
project: 3i
type: decision
status: current
updated: 2026-08-20
id: 3I-DEC-010
tags: [decision, billing, waivers]
---

# A Waiver Applies to the Whole Subscription

## Context

Waivers are approved at four fixed tiers — 25%, 50%, 75%, 100% (FR-WAV-02). A subscription may carry additional paid seats beyond the included one. The baseline does not say whether the discount reaches those seats.

## Decision

**The waiver applies to the full subscription, additional seats included.** Taken in review, 2026-08-18.

## Consequences

- A 100% waiver produces a genuinely zero invoice for a family of six, not a zero base with five seats still charged.
- Implementation stays simple: a Stripe coupon on the subscription discounts the whole line, which is what fixed-tier coupons do naturally. A seats-excluded rule would need bespoke logic.
- This is the reading a waiver applicant would assume, so it avoids a dispute at the first invoice.
- Waivers run 12 months and take effect at the next renewal, with no mid-cycle proration (FR-WAV-03, FR-WAV-04). Seats added *during* a waived period inherit the discount for the remainder.

## Cost

**Resolved by [3I-DEC-025](dec-025-waiver-single-profile-cap.md), 2026-08-20.** The exposure originally recorded here — a family on 100% adding five more seats at no cost, with only the six-profile limit as a ceiling — is closed by capping any waived account to one profile, chosen at application time, for the duration of the waiver.

Admin may revoke a waiver at any time, with the account holder notified and full price resuming at the next billing date (FR-WAV-05). That remains the safety valve for the waiver itself; the profile cap is what removes the seat-stacking exposure specifically.