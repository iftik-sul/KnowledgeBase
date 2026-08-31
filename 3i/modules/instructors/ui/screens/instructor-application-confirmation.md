---
project: 3i
module: instructors
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-INS-UI-006
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - instructors
  - registration
---

# Screen: Instructor Application Confirmation

Not directly required by any single FR — a one-time UX addition per [3I-DEC-040](/3i/decisions/dec-040-instructor-registration-confirmation-screen.md).

---

## Purpose

Shown exactly once, immediately after the [Email Verification](/3i/modules/identity-and-access/ui/screens/email-verification.md) link is clicked — but **only** when that verification completes the combined instructor-registration path ([Instructor Application](instructor-application.md), Path 1). An ordinary Member's registration never reaches this screen.

## Access Gate

Reached only as the direct next step after successful email verification for an Account whose registration also created a `pending` `InstructorApplication` in the same action. Not reachable by navigating here directly, and not shown again on any later login — [Instructor Application Status](instructor-application-status.md) is the screen for every login after this first one, per [3I-DEC-041](/3i/decisions/dec-041-role-context-switch.md).

## Contents

Confirms two things at once, since both happened in the same moment for this path:

- Email verified — the account is now fully active, same as any other Member's.
- Teaching application received and under review — stating plainly that this is a separate, ongoing process from the account itself, with no promised timeline (none is specified in the baseline).

A single acknowledgement action ("Continue") proceeds to **[Instructor Application Status](instructor-application-status.md)** — updated per [3I-DEC-041](/3i/decisions/dec-041-role-context-switch.md); the original version of this spec routed to Guardian Dashboard, which read as a mismatch for someone who just registered specifically to teach.

## Behaviour

This screen introduces no persistent state of its own — it is not repeated. Ongoing visibility into the pending application is now handled by [Instructor Application Status](instructor-application-status.md), reached on every subsequent login rather than being absent, per [3I-DEC-041](/3i/decisions/dec-041-role-context-switch.md).

## Role Variations

None — this is a one-time, path-specific screen, not role-gated beyond the access condition above.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
