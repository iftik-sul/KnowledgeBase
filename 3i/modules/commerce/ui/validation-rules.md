---
project: 3i
module: commerce
type: ui-spec
status: current
updated: 2026-08-20
id: 3I-CMR-UI-VAL
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - validation
---

# Commerce — Validation Rules

Field-level validation shared across two or more commerce screens.

---

## Waiver Covered-Profile Selection

On [Waiver request form](screens/waiver-request-form.md): the covered-profile field is **required**, single-select, limited to the requester's own active or never-activated profiles. Cannot be left blank and cannot name a profile that is already inactive or deleted — per [3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md), this selection is what the whole cap mechanism is built on, so the form must not allow submission without it.

## Refund Window Check

On [Refund request](screens/refund-request.md): the self-service path is only offered when the subscription's first payment was **within the last 14 days** (FR-REF-01). Outside that window, the self-service form is not shown at all — replaced by a message directing the Member to contact support, which routes to the admin-discretion flow ([Refund admin action](screens/refund-admin-action.md)) rather than presenting a form the backend would reject anyway.

## Money Formatting

All prices, everywhere in this module: GST-inclusive, formatted to two decimal places, currency symbol per locale (FR-BILL-07). No screen performs its own rounding — the displayed figure is always the stored integer-cent value divided by 100, never a client-side recalculation from a per-seat rate.