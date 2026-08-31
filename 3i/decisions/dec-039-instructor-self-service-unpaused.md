---
project: 3i
type: decision
status: current
updated: 2026-08-26
id: 3I-DEC-039
tags: [decision, design-system, instructors, catalogue, learning-delivery, scope]
---

# Instructor Self-Service Tooling Is Unpaused — Only Admin-Facing Review/Management Stays Under DEC-033

## Context

[3I-DEC-033](dec-033-admin-instructor-surface-provisional.md) paused "the entire admin/instructor surface" as one undifferentiated category, on the reasoning that admin/instructor tooling would need a separate portal design. Revisiting this to resume instructor design work surfaced that the category was too broad: **an instructor applying, managing their own courses, scheduling their own batches, and viewing their own dashboard is genuinely different work from an admin reviewing other people's submissions or managing the platform at large.** The former is self-service, single-user-scoped, and structurally similar to every Member-facing screen already built (forms, lists of your own things, a personal dashboard). The latter is queue-based, cross-user, data-dense review tooling — the actual category DEC-033 was written to protect against building twice.

[3I-DEC-038](dec-038-instructor-registration-account-works-normally.md) already implicitly leaned this direction (documenting Instructor Application's behaviour in full despite the pause), but didn't formally narrow DEC-033's scope. This decision does.

## Decision

**DEC-033's pause now applies only to Admin-role screens, across every module.** Instructor-role self-service screens are unpaused, treated as ordinary design work using the same design system as everything else built so far — no separate portal, no different visual language.

**Unpaused (Instructor-role, self-service):**

| Module | Screen |
| :---- | :---- |
| `instructors` | [Instructor Application](/3i/modules/instructors/ui/screens/instructor-application.md) (per [3I-DEC-038](dec-038-instructor-registration-account-works-normally.md)) |
| `instructors` | [WWCC Renewal](/3i/modules/instructors/ui/screens/wwcc-renewal.md) |
| `instructors` | **Instructor Dashboard** (new — [`instructor-dashboard.md`](/3i/modules/instructors/ui/screens/instructor-dashboard.md), `3I-INS-UI-005`) |
| `catalogue` | [Course Create / Edit](/3i/modules/catalogue/ui/screens/course-create-edit.md) |
| `learning-delivery` | [Batch Schedule / Manage](/3i/modules/learning-delivery/ui/screens/batch-schedule-manage.md), [Batch Roster \& Attendance](/3i/modules/learning-delivery/ui/screens/batch-roster-attendance.md), [Batch Reschedule / Cancel](/3i/modules/learning-delivery/ui/screens/batch-reschedule-cancel.md) — never explicitly paused under the original DEC-033, now explicitly confirmed in scope rather than left ambiguous |

**Remains paused (Admin-role, review/management):**

| Module | Screen |
| :---- | :---- |
| `identity-and-access` | Admin — profile name unlock, DOB correction, TOTP setup |
| `commerce` | Waiver Admin Review, Refund Admin Action |
| `catalogue` | Admin Review Queue, Admin Course Management |
| `instructors` | Admin Application Review, Admin Instructor Management |

**The dividing line is role, not module.** A module can have screens on both sides — `catalogue` and `instructors` each do.

## Consequences

- [3I-DEC-033](dec-033-admin-instructor-surface-provisional.md) gets a partial-supersession notice (same pattern as [3I-DEC-002](dec-002-under-13-family-accounts.md)'s partial supersession by [3I-DEC-023](dec-023-no-standalone-accounts-under-18.md)) — its content is not rewritten, a notice is added pointing here.
- `instructors/ui/README.md`, `catalogue/ui/README.md`, and `learning-delivery/ui/README.md` all updated to reflect the narrowed pause accurately.
- A new screen, Instructor Dashboard, is specified for the first time — the instructor-role counterpart to [Guardian Dashboard](/3i/modules/identity-and-access/ui/screens/guardian-dashboard.md) and [Learner Dashboard](/3i/modules/identity-and-access/ui/screens/learner-dashboard.md), neither of which an approved instructor's own course/batch overview naturally belonged to.

## Cost

None — this is a scope narrowing, not an expansion of what needs to eventually be built. If anything it reduces total paused surface area, since roughly half of what DEC-033 swept in turns out not to need the deferred treatment at all.
