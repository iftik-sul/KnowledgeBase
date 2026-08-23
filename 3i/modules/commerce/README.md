---
project: 3i
module: commerce
type: overview
status: current
updated: 2026-08-20
id: 3I-CMR-OVW-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - module
  - overview
---

# Commerce

The module that turns a family account into a paying subscription, and unwinds that relationship cleanly when a waiver, a refund, or a cancellation applies.

**Module status: complete.** README, data model, all three requirements documents, and the full nine-screen UI spec are written. The one cross-cutting dependency this module needed — [app-store-compliance.md](/3i/app-store-compliance.md) — now exists.

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| BILL | Subscriptions and billing | 8 |
| WAV | Waivers | 9 |
| REF | Refunds | 5 |

Twenty-two baseline requirements, plus four decisions that amend them ([3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md), [3I-DEC-010](/3i/decisions/dec-010-waiver-covers-all-seats.md), [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md), [3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md)) — all scope changes requiring §21.3 sign-off.

## Commercial Model

| Item | Value |
| :---- | :---- |
| Pricing | **Two tiers, by learner age** — see below. No flat subscription fee; every seat, including the first, is priced by its occupant's tier ([3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md)) |
| Maximum profiles | 6 per account — capped to **1** while a waiver is active ([3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md)) |
| Free trial | None |
| Payment rail | Stripe, **web checkout only** |
| Refunds | 14-day self-service on first payment; renewals at admin discretion |
| Waivers | Four fixed tiers — 25%, 50%, 75%, 100%, applied to the whole subscription across both seat tiers, capped to one profile for the duration |

### Seat Pricing

| Tier | Monthly | Annual |
| :---- | ----: | ----: |
| Adult (18+) | AUD $9.99 | AUD $99.99 |
| Under 18 | AUD $5.99 | AUD $49.99 |

Confirmed by the client 2026-08-20, resolving the last open pricing dependency. Total charge = (active adult seats × adult tier price) + (active minor seats × minor tier price), at one cadence chosen for the whole account. A family with 2 adult profiles and 2 children profiles pays $31.96/month or $299.96/year.

## The Seat Model

A seat is not a viewing slot — it is a **permanent, non-transferable enrolment grant to one profile** ([3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md)). Purchasing a seat activates a specific profile; cancelling deactivates it without deleting it, preserving all history. Reactivation is a fresh payment, since there is no free trial anywhere in the baseline.

This module owns the **Subscription** and its **two seat quantities** (adult tier, minor tier) as Stripe subscription line items — [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md). It does not own the **Learner** record or its activation state — that lives in `identity-and-access`, which this module reads and writes through the seat-purchase and seat-cancellation flows. See [data-model.md](data-model.md) for the split.

A learner's tier is read from their date of birth at the moment of activation. Turning 18 reprices the seat from minor to adult tier at the account's **next renewal**, never mid-cycle — the same no-proration principle already applied to waivers.

A waiver discounts the **whole subscription**, across both tiers ([3I-DEC-010](/3i/decisions/dec-010-waiver-covers-all-seats.md)) — but caps the account to the **one profile named in the waiver request**, auto-deactivating any others on approval ([3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md)). A 100% waiver on that one profile is a genuinely zero invoice; it no longer scales with household size the way an uncapped waiver would.

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-CMR-DM-001 | current |
| [requirements/bill-subscriptions-and-billing.md](requirements/bill-subscriptions-and-billing.md) | 3I-CMR-REQ-001 | current |
| [requirements/wav-waivers.md](requirements/wav-waivers.md) | 3I-CMR-REQ-002 | current |
| [requirements/ref-refunds.md](requirements/ref-refunds.md) | 3I-CMR-REQ-003 | current |
| [ui/README.md](ui/README.md) | 3I-CMR-UI-000 | current — full 9-screen role × screen matrix |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| The seat as an enrolment grant, and the four-state profile lifecycle | [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md), [3I-DEC-014](/3i/decisions/dec-014-cap-counts-active-profiles-only.md) |
| Two-tier age-based seat pricing and the ageing-up reprice rule | [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md) |
| Waiver single-profile cap, chosen at application | [3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md) |
| Every account is 18+; every minor is a guardian profile, never a billing party | [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) |
| Device allowance scaling with seats | [3I-DEC-015](/3i/decisions/dec-015-device-allowance-scales-with-seats.md) |
| No purchase surface in the mobile apps | [app-store-compliance.md](/3i/app-store-compliance.md) |

## Delivery

Phase 2, Commerce (§21.1) — Stripe, seats, subscriptions, waivers, refunds. Sits second deliberately: the app store submission strategy depends on it, and store review is the least predictable part of the schedule.

## Open Against This Module

| Item | Blocks | Note |
| :---- | :---- | :---- |
| GST treatment for overseas learners | Invoice line-item logic | From the client's accountant |
| Seat cancellation running to period-end vs. prorated refund | Backend spec for FR-BILL-04 | Assumed, not yet confirmed — see [3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md#cost--open-items-introduced-by-this-decision) |

Both resolved: **per-seat price** ([3I-DEC-024](/3i/decisions/dec-024-two-tier-age-based-seat-pricing.md)), **the waiver seat-stacking exposure** ([3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md)), and **`app-store-compliance.md`** (now written — see [ui/README.md](ui/README.md)). The two items above are the only things left, and both are external inputs — a client dependency and a one-line confirmation — not gaps in the specification itself.

## Change Requests Owed to the Client

Four decisions in this module change SRD v2.0 rather than interpret it — the seat-as-permanent-grant model, waiver-covers-all-seats, two-tier age-based pricing, and the waiver single-profile cap. All four are part of the consolidated change request under §21.3 — full list in [decisions/README.md](/3i/decisions/README.md#scope-changes-against-srd-v20).