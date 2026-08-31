---
project: 3i
module: instructors
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-INS-UI-007
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - instructors
---

# Screen: Instructor Application Status

Not directly required by any single FR — per [3I-DEC-041](/3i/decisions/dec-041-role-context-switch.md), resolving the persistent-status gap [3I-DEC-040](/3i/decisions/dec-040-instructor-registration-confirmation-screen.md) explicitly left open.

---

## Purpose

Where an Account with a `pending` `InstructorApplication` lands on **every** login, for as long as the application remains pending — distinct from [Instructor Application Confirmation](instructor-application-confirmation.md), which is shown exactly once, immediately after email verification, and never again.

## Access Gate

Any authenticated Account with a `pending` `InstructorApplication` and no approved `InstructorProfile`. Reached automatically as the default login destination per [3I-DEC-041](/3i/decisions/dec-041-role-context-switch.md)'s routing priority — not a screen someone navigates to deliberately.

## Contents

- A status indicator, plainly stated: application under review, with the date it was submitted.
- No promised timeline (none is specified in the baseline) — a general "we'll email you once a decision is made" statement, not a fabricated estimate.
- If this Account also holds learner profiles (is also a parent/guardian on the platform), the [Account Menu](/3i/modules/identity-and-access/ui/components.md#account-menu)'s role-context switch is available, letting them move to the ordinary Member view — this screen does not trap them in an instructor-only context if they have other reasons to use the platform in the meantime.

## Behaviour

This screen is re-evaluated on every login, not cached — the moment the application resolves (`approved` or `rejected`), the next login routing falls through to a different case entirely ([Instructor Dashboard](instructor-dashboard.md) on approval, the ordinary Member flow on rejection), and this screen is no longer reached.

## Role Variations

None — same content regardless of what the Member's other roles or profiles look like; only the presence of the role-context switch varies.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
