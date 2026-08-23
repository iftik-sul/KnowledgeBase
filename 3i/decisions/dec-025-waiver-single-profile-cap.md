---
project: 3i
type: decision
status: current
updated: 2026-08-20
id: 3I-DEC-025
tags: [decision, billing, waivers, scope-change]
---

# Waiver Single-Profile Cap, Chosen At Application

## Context

[3I-DEC-010](dec-010-waiver-covers-all-seats.md) left an exposure on record rather than resolving it: a waiver applies to the whole subscription, so a 100% waiver covers every seat on the account, and nothing in the baseline or in that decision caps how many profiles a waived account can add beyond the ordinary six-profile limit. A household approved for hardship could add five more profiles afterward, all riding the same free or discounted subscription with no further review.

Discussed and resolved 2026-08-20.

## Decision

1. **While a waiver is active, the account is capped at one profile — adult or minor, whichever it is.** This overrides the normal six-profile limit (FR-FAM-02 / [3I-DEC-014](dec-014-cap-counts-active-profiles-only.md)) for the duration.

2. **The covered profile is chosen at application time, not after approval.** The waiver request (FR-WAV-01) names which one profile the waiver is for, as part of the written submission — not a follow-up step, not something decided later.

3. **On approval, every other profile on the account is automatically deactivated by the system**, as a direct effect of approval, in the same action that activates the waiver. There is no pending-but-not-active state, no reminder or alert cadence, and no exception needed to the profile-change rate limit (FR-FAM-06) — the reduction is not the account holder making profile changes, so that limit was never in play.

4. **Deactivated profiles follow the standard deactivation pattern** — history preserved, reactivatable later at full price — the same as any ordinary seat cancellation. No special case.

5. **The cap blocks creating a second profile outright**, not just activating or paying for one, for as long as the waiver is active.

6. **On revocation or natural expiry, the cap reverts to the normal six-profile limit.** Adding profiles again afterward is the ordinary paid-seat-activation flow — no special re-review beyond what any new seat purchase already requires.

## Consequences

- **[3I-DEC-010](dec-010-waiver-covers-all-seats.md)'s open cost item is resolved.** That decision's "Cost" section flagged this exact exposure and deferred it as future scope; this decision is that future scope, arriving the same session the gap was named.
- **The waiver application form gains a field**: which profile the request covers. This is a small addition to FR-WAV-01's existing written-explanation-plus-evidence submission, not a new workflow.
- **No pending/alert state needs building.** The simpler shape — pick the profile up front, auto-deactivate on approval — was chosen specifically to avoid a three-part mechanism (pending status, reminder notifications, a rate-limit carve-out) that an after-the-fact reduction would have required.
- **Depends on profile tier being a real, queryable attribute**, not just derived live from date of birth — see the note below. The cap itself ("one profile, whichever tier") doesn't care about tier, but the surrounding commerce data model is being reworked to add explicit adult/minor typing on `LearnerProfile` alongside two-tier seat pricing ([3I-DEC-024](dec-024-two-tier-age-based-seat-pricing.md)), and this decision assumes that work lands.

## Cost / Open Items Introduced By This Decision

- **Auto-deactivation is a system action taken on the account holder's behalf, without a per-profile confirmation step.** This is a deliberate trade — it is what removes the pending/alert complexity — but it means the account holder does not get a "review before we deactivate these" moment. Worth confirming this reads as acceptable UX rather than surprising, once the Checkout/Waiver screens are actually designed.
- **No tie-breaking logic is needed** since the applicant names the surviving profile directly — but if that named profile is deleted or the account otherwise loses it between application and approval, there is no fallback rule yet for what happens to the waiver. Minor edge case, not yet addressed.

## Related

| | |
| :---- | :---- |
| Resolves the open cost item in | [3I-DEC-010](dec-010-waiver-covers-all-seats.md) |
| Depends on | [3I-DEC-024](dec-024-two-tier-age-based-seat-pricing.md) — profile tier as a stored attribute |
| Amends | FR-WAV-01 (submission gains a covered-profile field) |
| Requirements updated | [3I-CMR-REQ-002](/3i/modules/commerce/requirements/wav-waivers.md) |
| Data model updated | [3I-CMR-DM-001](/3i/modules/commerce/data-model.md) |