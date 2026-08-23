---
project: 3i
module: instructors
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-INS-UI-004
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - instructors
  - safeguarding
---

# Screen: WWCC Renewal

Satisfies: FR-INST-03, FR-INST-04

---

## Purpose

An approved instructor updates their own WWCC details when it renews — the mechanism that clears an expiring or expired status.

## Access Gate

Instructor only (their own `InstructorProfile`).

## Contents

Current WWCC number, issuing state, expiry date (read-only display, with the [WWCC Status Badge](../components.md#wwcc-status-badge)), and an update form using the same validation as initial application (see [validation-rules.md](../validation-rules.md#wwcc-field-validation)).

## Behaviour

Saving a renewed WWCC updates `InstructorProfile` directly — no new [InstructorApplication](../../data-model.md#instructorapplication) is created, and no admin approval step gates it, since this is credential upkeep on an already-approved instructor, not a new bid for the role ([data-model.md](../../data-model.md#wwcc-renewal)). The pending 60-day alert state clears automatically once the new expiry date is far enough out.

**Renewing does not automatically republish any course suspended by an earlier expiry** — the instructor sees this stated plainly ("your WWCC is now current; suspended courses need admin review before they can republish") rather than assuming renewal alone fixes everything downstream.

## Role Variations

Instructor only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the instructor panel supports it (FR-LOC-04).