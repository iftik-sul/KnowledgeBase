---
project: 3i
module: commerce
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-CMR-UI-000
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - matrix
---

# Commerce — UI Index

Role × screen matrix.

**Admin-only screens in this module are provisional — see [3I-DEC-033](/3i/decisions/dec-033-admin-instructor-surface-provisional.md).** [Waiver Admin Review](screens/waiver-admin-review.md) and [Refund Admin Action](screens/refund-admin-action.md) are built and confirmed against the current design system but will need revisiting once a separate admin/instructor portal design exists. This does not affect [Seat Management](screens/seat-management.md) or [Billing Portal Redirect](screens/billing-portal-redirect.md), which are primarily Member-facing screens Admin also uses for support.

| Screen | Member | Admin |
| :---- | :---: | :---: |
| [Pricing / Plan Selection](screens/pricing-plan-selection.md) | ● | |
| [Checkout](screens/checkout.md) | ● | |
| [Seat Management](screens/seat-management.md) | ● | ● |
| [Billing Portal Redirect](screens/billing-portal-redirect.md) | ● | ● |
| [Subscription Status (mobile)](screens/subscription-status-mobile.md) | ● | |
| [Waiver Request Form](screens/waiver-request-form.md) | ● | |
| [Waiver Admin Review](screens/waiver-admin-review.md) ⚠ provisional | | ● |
| [Refund Request](screens/refund-request.md) | ● | |
| [Refund Admin Action](screens/refund-admin-action.md) ⚠ provisional | | ● |

Nine screens. Web-only except Subscription Status — see [mobile-scope.md](/3i/mobile-scope.md#2-scope-by-module).
