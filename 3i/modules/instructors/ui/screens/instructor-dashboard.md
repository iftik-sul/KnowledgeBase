---
project: 3i
module: instructors
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-INS-UI-005
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - instructors
  - dashboard
---

# Screen: Instructor Dashboard

Not directly required by any single FR — the instructor-role counterpart to [Guardian Dashboard](/3i/modules/identity-and-access/ui/screens/guardian-dashboard.md) and [Learner Dashboard](/3i/modules/identity-and-access/ui/screens/learner-dashboard.md), per [3I-DEC-039](/3i/decisions/dec-039-instructor-self-service-unpaused.md).

---

## Purpose

An approved instructor's own hub — their courses, their upcoming batches, their credential status, all in one place. The landing point after login for an Account holding the Instructor role, the same way [Learner Dashboard](/3i/modules/identity-and-access/ui/screens/learner-dashboard.md) is the landing point for a learner profile.

## Access Gate

**Approved Instructor role only** — an `InstructorProfile` must exist. A Member with a `pending` `InstructorApplication` (per [3I-DEC-038](/3i/decisions/dec-038-instructor-registration-account-works-normally.md)) does **not** reach this screen — they remain an ordinary Member until approved, with their "application under review" state shown elsewhere (account settings), not as a locked or partial version of this dashboard.

## Contents

- **My Courses** — every course this instructor owns, each showing its status (`draft` / `pending_review` / `published` / `suspended` / `taken_down` — same status language as [Admin Course Management](/3i/modules/catalogue/ui/screens/admin-course-management.md), not a separate instructor-facing vocabulary for the same states). A prominent "Create new course" action leading to [Course Create / Edit](/3i/modules/catalogue/ui/screens/course-create-edit.md).
- **My Batches** — upcoming sessions across every batch this instructor teaches, similar in spirit to Learner Dashboard's Upcoming Sessions widget but instructor-scoped (their own teaching schedule, not a learner's enrolled classes). Links to [Batch Schedule / Manage](/3i/modules/learning-delivery/ui/screens/batch-schedule-manage.md) for the full management view.
- **Credential status** — the [WWCC Status Badge](../components.md#wwcc-status-badge) component instance, with a direct link to [WWCC Renewal](wwcc-renewal.md) when `Expiring Soon` or already expired. This should be hard to miss on the dashboard specifically, since a lapsed WWCC has real consequences ([data-model.md](../../data-model.md#fr-inst-04-enforcement--what-cannot-continue-teaching-actually-does) — automatic course suspension).
- **Storage usage** — the [Storage Usage Bar](../components.md#storage-usage-bar) component instance. Shown transparently despite there being no quota to stay under ([3I-DEC-029](/3i/decisions/dec-029-no-instructor-storage-quota.md)) — informational, not a limit warning.

## Behaviour

A suspended course (whether by admin action or automatic WWCC-expiry enforcement) is visually distinguishable in My Courses from an ordinary `published` one — same distinction [Admin Instructor Management](admin-instructor-management.md) already makes on the admin side, mirrored here so the instructor themselves understands their own status without needing to contact admin to find out why a course disappeared from the public catalogue.

## Role Variations

Instructor only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
