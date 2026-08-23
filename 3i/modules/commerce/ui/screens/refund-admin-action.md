---
project: 3i
module: commerce
type: ui-spec
status: current
updated: 2026-08-20
id: 3I-CMR-UI-009
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - refunds
  - admin
---

# Screen: Refund Admin Action

Satisfies: FR-REF-02, FR-REF-03

---

## Purpose

Process a discretionary refund on a renewal payment — outside the 14-day self-service window, admin judgement only (FR-REF-02).

## Access Gate

Web only. Admin only.

## Contents

- Search or lookup for the account and the specific payment to refund.
- **Reason field — required** for any admin-discretion refund, unlike the self-service flow which needs none. This is the audit distinction between the two refund types in [3I-CMR-DM-001](/3i/modules/commerce/data-model.md#refund).
- Amount, defaulting to the full payment but editable for a partial refund at admin discretion.
- Confirmation that access is **revoked immediately** on processing (FR-REF-03), same as the self-service path, and that any certificate already issued to the account's learners remains valid (FR-REF-04).

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
