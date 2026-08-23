---
project: 3i
module: commerce
type: requirements
status: current
updated: 2026-08-20
id: 3I-CMR-REQ-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - waivers
---

# Waivers

Baseline §14.3. Nine requirements, two amended by decision.

A needs-based discount scheme with four fixed tiers, evidence-backed, admin-reviewed, and time-bounded — now also capped to a single profile per waived account.

---

## Request

| ID | Requirement |
| :---- | :---- |
| **FR-WAV-01** | An account holder submits a waiver request with a **written explanation** and **optional file uploads** as supporting evidence |

Evidence is optional by requirement — a written explanation alone is a valid submission. The upload, when present, is what carries the storage and access controls below.

**Amended by [3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md): the request also names which one profile the waiver covers.** Chosen at application time, not decided later — this is what lets approval be a single, immediate action rather than a multi-step reduction process.

---

## Decision

| ID | Requirement |
| :---- | :---- |
| **FR-WAV-02** | Admin approves at one of **four fixed tiers: 25%, 50%, 75%, 100%** |
| **FR-WAV-03** | An approved waiver takes effect **at the next renewal**. No mid-cycle proration |
| **FR-WAV-04** | A waiver runs **12 months**, after which the account holder may re-apply |

No custom or partial percentages outside the four tiers — this keeps the Stripe coupon implementation simple, since fixed-tier coupons map directly to Stripe's discount model without bespoke calculation. See [3I-CMR-DM-001](../data-model.md#waiver).

---

## Scope of the Discount

| ID | Requirement |
| :---- | :---- |
| — | **Applies to the whole subscription, including additional seats** |

Not a baseline requirement number — the baseline left this unstated, and [3I-DEC-010](/3i/decisions/dec-010-waiver-covers-all-seats.md) settles it. A 100% waiver produces a genuinely zero invoice for a family of six, not a zero base plan with five seats still charged. The reasoning: this is the reading a waiver applicant would assume, and a seats-excluded rule would need bespoke logic a fixed-tier Stripe coupon doesn't naturally provide.

Given the single-profile cap below, "the whole subscription" while waived means, in practice, exactly one seat — but the discount mechanism itself (a Stripe coupon on the subscription) is unchanged, and would still apply correctly to every seat if the cap were ever lifted for a different reason.

---

## Single-Profile Cap

| ID | Requirement |
| :---- | :---- |
| — | **While active, a waiver caps the account at one profile — adult or minor** |

Not a baseline requirement number — [3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md) closes an exposure [3I-DEC-010](/3i/decisions/dec-010-waiver-covers-all-seats.md) left open: an account-level waiver with no per-profile limit meant a household could stack profiles onto a free or discounted subscription with no additional review.

**Mechanics:**
- The one profile is named in the waiver **request itself** (see FR-WAV-01 above), not chosen after the fact.
- **On approval, every other profile on the account is automatically deactivated** by the system, as part of the same action that activates the waiver — not a pending state, not a reminder, not something the account holder does manually afterward.
- Deactivated profiles follow the ordinary deactivation pattern: history preserved, reactivatable later at full price.
- The cap **blocks creating** a second profile outright while the waiver is active, not just activating or paying for one.
- **On revocation or expiry, the cap lifts** and the account reverts to the normal six-profile limit (FR-FAM-02 / [3I-DEC-014](/3i/decisions/dec-014-cap-counts-active-profiles-only.md)); adding profiles afterward is the ordinary paid-seat-activation flow.

This shape — pick the profile up front, auto-deactivate on approval — was chosen specifically to avoid a more complex alternative (approve first, give the account holder a pending status and a reminder to reduce down, carve out an exception to the profile-change rate limit for the reduction). Naming the profile at application time removes all three of those pieces.

---

## Revocation

| ID | Requirement |
| :---- | :---- |
| **FR-WAV-05** | Admin may **revoke** an active waiver. The account holder is notified by email and push, and full price resumes at the **next billing date** |
| **FR-WAV-06** | A 100% waiver produces a **live subscription with a 100% discount** — not a flagged free account. Admin-created free accounts are a separate mechanism |

FR-WAV-06 matters for reporting integrity: a 100% waiver still appears in subscriber counts and revenue reports as a zero-dollar active subscription, not as an out-of-band exception the numbers have to account for separately.

---

## Evidence Handling

| ID | Requirement |
| :---- | :---- |
| **FR-WAV-07** | Waiver evidence files are stored in a **private bucket**, never CDN-cached, accessed only via **short-lived signed URLs**, with every access logged |
| **FR-WAV-08** | Waiver evidence is **automatically deleted 12 months after the decision** |

This is the same evidence-handling discipline the baseline applies to WWCC data and other sensitive uploads (NFR-10). The 12-month deletion is tied to the **decision date**, not the request date and not the waiver's own 12-month run (FR-WAV-04) — those two clocks happen to be the same length but start from different events and should not be implemented as a single timer.

---

## Audit Trail

| ID | Requirement |
| :---- | :---- |
| **FR-WAV-09** | Full audit trail: **requester, submission, reviewer, decision, tier, effective and expiry dates, revocation and reason** |

This trail outlives the evidence file. FR-WAV-08 deletes the upload; FR-WAV-09's record — who asked, who decided, what tier, when it started and ended — persists regardless, since it is what a later dispute or a re-application review needs, and none of it is personally sensitive in the way the evidence itself is.

**Also worth recording per [3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md):** which profile the waiver covers, and which profiles were auto-deactivated on approval as a consequence — not a separate requirement number, but the same audit discipline FR-WAV-09 already establishes, extended to the new mechanic.

---

## Acceptance Criteria

1. A 100% waiver produces an active subscription visible in Stripe with a zero invoice, including any additional seats on the account.
2. Waiver evidence files are unreachable without a signed URL and are purged 12 months after the decision date, independent of the waiver's own expiry.
3. Revoking a waiver mid-term produces both an email and a push notification, and full price resumes at the account's next billing date — not immediately.
4. A waiver's audit record remains complete and queryable after its evidence file has been auto-deleted.
5. Approving a waiver request on an account with three profiles immediately deactivates the two not named in the request, in the same action, with no pending or reminder state in between.
6. Attempting to create a second profile on an account with an active waiver is blocked outright, regardless of the tier of either profile.
7. Revoking or letting a waiver expire restores the account's normal six-profile limit with no special re-review required to add profiles again.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-CMR-DM-001](../data-model.md) |
| Waiver applies to all seats | [3I-DEC-010](/3i/decisions/dec-010-waiver-covers-all-seats.md) |
| Single-profile cap, chosen at application | [3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md) |
| Sensitive upload handling precedent (WWCC) | Baseline NFR-10 |
| Subscriptions and billing | [3I-CMR-REQ-001](bill-subscriptions-and-billing.md) |
| Refunds | [3I-CMR-REQ-003](ref-refunds.md) |