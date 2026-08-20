---
project: 3i
module: commerce
type: ui-index
status: draft
updated: 2026-08-20
id: 3I-CMR-UI-000
derived_from:
  - requirements/bill-subscriptions-and-billing.md
  - requirements/wav-waivers.md
  - requirements/ref-refunds.md
tags:
  - ui
  - commerce
---

# Commerce — UI Index

**Status: stub.** Screens are not yet individually specified — this records the role × screen matrix so a missing screen is visible, ahead of Figma work. Follows the shape in [project-standards.md](/3i/project-standards.md#the-ui-stage).

## Role × Screen Matrix

| Screen | Member | Admin | Mobile (Flutter) |
| :---- | :---: | :---: | :---: |
| Pricing / plan selection | ✅ web only | — | ❌ no purchase surface (FR-BILL-02) |
| Checkout | ✅ web only, Stripe-hosted | — | ❌ |
| Seat management | ✅ | ✅ (all accounts) | ❌ |
| Billing portal (payment method, cancellation) | ✅ via Stripe Customer Portal | ✅ (all accounts) | ❌ |
| Subscription status (neutral, no CTA) | — | — | ✅ NFR-18 — status + support email only |
| Waiver request form | ✅ | — | ❌ |
| Waiver admin review | — | ✅ | — |
| Refund request (self-service, ≤14 days) | ✅ web | — | ❌ |
| Refund admin action (renewal, discretionary) | — | ✅ | — |

**The mobile column is the one to get wrong carefully.** Every ❌ in that column is FR-BILL-02 and NFR-18 in effect, not an oversight — a mobile screen in this module should never grow a price, a button, or a link back to any of the web screens above. See [OQ-09](/3i/open-questions.md#oq-09--app-store-compliancemd-not-yet-written).

## Pending

Individual screen files (`ui/screens/<screen-name>.md`), `components.md`, and `validation-rules.md` are not yet written. Each screen file, once created, must state its WCAG 2.2 AA contrast pairs (NFR-12) and its RTL behaviour (FR-LOC-04) per the repository standard — Checkout and Billing Portal in particular involve dense tabular pricing data, which is exactly the kind of layout the standard's contrast warning is aimed at.

## Related

| | |
| :---- | :---- |
| Module overview | [README.md](../README.md) |
| Requirements | [bill](../requirements/bill-subscriptions-and-billing.md), [wav](../requirements/wav-waivers.md), [ref](../requirements/ref-refunds.md) |
| UI stage rules | [project-standards.md](/3i/project-standards.md#the-ui-stage) |
