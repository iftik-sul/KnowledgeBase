---
project: 3i
module: instructors
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-INS-UI-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - instructors
  - admin
---

# Screen: Admin Application Review

Satisfies: FR-INST-02

---

## Purpose

Admin reviews pending instructor applications — bio, expertise, CV, WWCC — and approves or rejects.

## Access Gate

Admin only.

## Contents

A queue of `pending`-status [InstructorApplication](../data-model.md#instructorapplication)s, each showing every submitted field including the CV (accessed via signed URL per NFR-10's sensitive-upload discipline, same pattern as waiver evidence). **Approve** and **Reject** actions, the latter requiring a reason (see [validation-rules.md](../validation-rules.md#rejection-reason-required)).

## Behaviour

**Approve** grants the Instructor role and creates (or reactivates, per [data-model.md](../data-model.md#re-approval-after-suspension)) the Account's `InstructorProfile`, seeded from this application's WWCC fields and the default 50 GB quota (FR-INST-05).

**Reject** notifies the applicant with the recorded reason (FR-INST-02) and leaves the Account's role unchanged — they may submit a new application at any time, with no cooldown specified in the baseline.

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).