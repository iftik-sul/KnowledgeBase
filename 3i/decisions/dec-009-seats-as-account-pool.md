---
project: 3i
type: decision
status: draft
updated: 2026-08-18
id: 3I-DEC-009
tags: [decision, billing, enrolment]
---

# Seats Are an Account-Level Pool

## Context

One seat is included in the subscription; additional seats carry a per-seat monthly charge, to a maximum of six profiles (§14.1). Seat count is a Stripe quantity (FR-BILL-04).

The baseline does not say whether a seat belongs to a named profile or floats.

## Decision

**Seats are a pool held at account level, not assigned to a named profile.** Taken in review, 2026-08-18.

## Unresolved — this is the blocking question

Recorded in [OQ-02](../open-questions.md#oq-02--what-a-seat-actually-is). "Pool" resolves two ways, and the baseline supports both:

| Reading | Effect | Family of four buys |
| :---- | :---- | :---- |
| **Study slot** | Only *n* profiles may be enrolled at all | 4 seats |
| **Viewing slot** | All 6 may enrol; only *n* may watch at once | 1–2 seats |

FR-ENR-01 requires an available seat *for that learner* to enrol — study slot. FR-AUTH-12 caps concurrent video streams by purchased seats — viewing slot. Both are in the document.

The revenue difference across a family customer base is roughly fourfold. The per-seat price the client still owes (§22.2 item 1) cannot be set until this is answered.

Also undefined: whether a seat may be reassigned between profiles, and any cooldown. §22.3 risk 5 already names seat sharing as a risk, mitigated by the profile cap, the certificate name lock, and profile change rate limits — all of which assume seats are somewhat sticky.

## Cost

Until this is settled, enrolment and billing cannot be specified, and phase 2 is Commerce.
