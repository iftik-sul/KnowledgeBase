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

Baseline §14.3. Nine requirements, one amended by decision.

A needs-based discount scheme with four fixed tiers, evidence-backed, admin-reviewed, and time-bounded.

---

## Request

| ID | Requirement |
| :---- | :---- |
| **FR-WAV-01** | An account holder submits a waiver request with a **written explanation** and **optional file uploads** as supporting evidence |

Evidence is optional by requirement — a written explanation alone is a valid submission. The upload, when present, is what carries the storage and access controls below.

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

**The cost, recorded and accepted rather than resolved:** there is no cap on seats a waived account can add beyond the six-profile limit. If that turns out to matter commercially, the fix is a seat limit on waived accounts specifically — new scope, not a variation of this decision. Admin revocation (FR-WAV-05, below) is the existing safety valve.

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

---

## Acceptance Criteria

1. A 100% waiver produces an active subscription visible in Stripe with a zero invoice, including any additional seats on the account.
2. Waiver evidence files are unreachable without a signed URL and are purged 12 months after the decision date, independent of the waiver's own expiry.
3. Revoking a waiver mid-term produces both an email and a push notification, and full price resumes at the account's next billing date — not immediately.
4. A waiver's audit record remains complete and queryable after its evidence file has been auto-deleted.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-CMR-DM-001](../data-model.md) |
| Waiver applies to all seats | [3I-DEC-010](/3i/decisions/dec-010-waiver-covers-all-seats.md) |
| Sensitive upload handling precedent (WWCC) | Baseline NFR-10 |
| Subscriptions and billing | [3I-CMR-REQ-001](bill-subscriptions-and-billing.md) |
| Refunds | [3I-CMR-REQ-003](ref-refunds.md) |
