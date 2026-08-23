---
project: 3i
module: commerce
type: ui-spec
status: current
updated: 2026-08-20
id: 3I-CMR-UI-008
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - refunds
---

# Screen: Refund Request

Satisfies: FR-REF-01, FR-REF-05

---

## Purpose

Self-service refund on a first subscription payment, within the 14-day window.

## Access Gate

Web only. Member session required. Only shown when the account's first payment falls within the last 14 days — see [validation-rules.md](../validation-rules.md#refund-window-check). Outside that window, this screen is not reachable; the entry point instead routes to a support-contact message that feeds [Refund Admin Action](refund-admin-action.md).

## Contents

- A summary of the payment being refunded — amount, date, plan.
- A short confirmation stating access will be **revoked immediately** on refund, not at the end of the current paid period (FR-REF-03) — this is the one place in commerce where "immediately" genuinely means immediately, unlike ordinary cancellation, and the copy should make that distinction clear rather than implying the same grace period.
- A note that any certificate already issued remains valid regardless (FR-REF-04).
- A link to the full refund policy page, which carries the Australian Consumer Law disclaimer (FR-REF-05) — this screen does not restate that copy, it links to the CMS page that owns it.
- **Confirm refund** — an irreversible action, styled and worded accordingly.

## Role Variations

Member only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
