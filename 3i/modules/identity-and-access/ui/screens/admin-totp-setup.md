---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-18
id: 3I-IDA-UI-015
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - admin
---

# Screen: Admin — TOTP Setup

Satisfies: FR-RBAC-05

---

## Purpose

Optional two-factor authentication setup for admin accounts. Standard TOTP enrolment: QR code, manual entry fallback, confirmation code, recovery codes.

## Behaviour

Optional, per FR-RBAC-05 — not enforced at launch. Once enabled, [Login](login.md) requires the TOTP step after password success, as noted there.

Recovery codes are single-use and shown once at setup, with an explicit "save these now" step before proceeding — standard practice, not a baseline-specific requirement, included because omitting it is a common and costly oversight.

## Role Variations

Admin only — the baseline restricts TOTP to admin accounts specifically (FR-RBAC-05), not offered to Instructor or Member.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).
