---
project: 3i
module: commerce
type: ui-spec
status: current
updated: 2026-08-20
id: 3I-CMR-UI-000
derived_from:
  - requirements/bill-subscriptions-and-billing.md
  - requirements/wav-waivers.md
  - requirements/ref-refunds.md
tags:
  - ui
  - matrix
---

# Commerce — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Member** | The renamed Account holder role — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md) |
| **Admin** | |
| **Mobile (Flutter)** | Not a role — a platform column, since this module's mobile behaviour is a single deliberate exception rather than a per-role variation |

---

## Matrix

| Screen | Member | Admin | Mobile |
| :---- | :---: | :---: | :---: |
| [Pricing / plan selection](screens/pricing-plan-selection.md) | ● (web) | | ❌ |
| [Checkout](screens/checkout.md) | ● (web) | | ❌ |
| [Seat management](screens/seat-management.md) | ● (web) | ● | ❌ |
| [Billing portal redirect](screens/billing-portal-redirect.md) | ● (web) | ● | ❌ |
| [Subscription status (mobile)](screens/subscription-status-mobile.md) | | | ● |
| [Waiver request form](screens/waiver-request-form.md) | ● (web) | | ❌ |
| [Waiver admin review](screens/waiver-admin-review.md) | | ● | |
| [Refund request](screens/refund-request.md) | ● (web) | | ❌ |
| [Refund admin action](screens/refund-admin-action.md) | | ● | |

Nine screens. **The ❌ column is FR-BILL-02 and NFR-18 in effect, not an oversight** — every screen in this module except Subscription Status is deliberately absent from mobile. See [app-store-compliance.md](/3i/app-store-compliance.md).

---

## Shared

| Document | Covers |
| :---- | :---- |
| [components.md](components.md) | Itemised total by tier, tier badge, Stripe-hosted redirect button |
| [validation-rules.md](validation-rules.md) | Waiver covered-profile selection, refund window check, money formatting |

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| None. | |

Resolved since the previous stub version of this document: [app-store-compliance.md](/3i/app-store-compliance.md) now exists, so the mobile Subscription Status screen above is written against a settled cross-cutting rule rather than a provisional one.
