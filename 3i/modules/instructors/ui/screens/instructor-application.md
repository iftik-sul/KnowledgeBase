---
project: 3i
module: instructors
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-INS-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - instructors
---

# Screen: Instructor Application

Satisfies: FR-INST-01, FR-INST-03

---

## Purpose

A Member applies to become an instructor — bio, expertise, CV, and WWCC details.

## Access Gate

Member (any Account not already holding the Instructor role). Reachable from account settings or a general "become an instructor" entry point — not gated behind anything else, since applying itself has no prerequisite beyond having an account at all.

## Fields

Bio (free text), area of expertise, CV upload, WWCC number, issuing state, WWCC expiry date — see [validation-rules.md](../validation-rules.md#wwcc-field-validation) for the all-or-nothing WWCC requirement and the not-already-expired check.

## Behaviour

Submission creates an [InstructorApplication](../../data-model.md#instructorapplication) with `status = pending` and notifies admin (see [Admin Application Review](admin-application-review.md)). **No immediate role change** — the Member remains whatever they were until admin approves.

If this Account has a prior `rejected` application, submitting a new one is simply another row — no special "reapplying" framing is needed structurally, though the screen may reasonably show the applicant their own prior rejection reason as context.

## Role Variations

Member only.

## Contrast and RTL

Standard form contrast, 4.5:1 minimum (NFR-12). Full RTL mirroring (FR-LOC-04).