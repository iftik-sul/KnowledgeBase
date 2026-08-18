---
project: 3i
type: decision
status: current
updated: 2026-08-18
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

The exposure is a family on 100% adding five seats at no cost. There is no cap on this beyond the six-profile limit. If that matters commercially, the control is a seat limit on waived accounts — which would be new scope, not a variation of this decision.

Admin may revoke a waiver at any time, with the account holder notified and full price resuming at the next billing date (FR-WAV-05). That is the existing safety valve.
