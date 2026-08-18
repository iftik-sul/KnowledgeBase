---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-18
id: 3I-IDA-UI-013
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - admin
---

# Screen: Admin — Profile Name Unlock

Satisfies: FR-FAM-05

---

## Purpose

Admin-only override to unlock a profile's display name after a certificate has locked it.

## Content

Search or lookup for the target profile. Shows the current locked name, the certificate(s) that caused the lock, and a required free-text reason field.

## Behaviour

Unlocking does **not** retroactively change the name on already-issued certificates — those are snapshotted at issue ([3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md)) and are immutable regardless of what happens to the live profile afterward. This screen changes the *profile's* name going forward; it does not touch certificate records. Worth stating explicitly on screen, since the two could otherwise be assumed to move together.

The reason is recorded permanently (FR-FAM-05) and should appear in the admin audit log (NFR-09).

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Admin surfaces are lower priority for RTL polish than learner-facing ones but are not exempt from the requirement (FR-LOC-04).
