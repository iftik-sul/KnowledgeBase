---
project: 3i
module: instructors
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-INS-UI-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - instructors
  - admin
---

# Screen: Admin Instructor Management

Satisfies: FR-INST-03, FR-INST-04, FR-INST-07

---

## Purpose

Admin oversight of every approved instructor — WWCC status and suspension.

## Access Gate

Admin only.

## Contents

A searchable list of every `InstructorProfile`, each showing the [WWCC Status Badge](../components.md#wwcc-status-badge). Selecting an instructor opens detail with: WWCC number/state/expiry (view-only here — renewal is instructor-initiated, see [WWCC Renewal](wwcc-renewal.md)), and a **Suspend** / **Reinstate** action.

**No storage quota control exists on this screen** — [3I-DEC-029](/3i/decisions/dec-029-no-instructor-storage-quota.md) removed the per-instructor quota this screen originally would have let admin adjust.

**Instructors flagged `Expiring Soon`** (within the 60-day window, FR-INST-03) are surfaced prominently — not buried in an alphabetical list — since this is the screen the alert is actually actionable from.

## Behaviour

**Suspend** (FR-INST-07) triggers the same course-suspension consequence [data-model.md](../data-model.md#fr-inst-04-enforcement--what-cannot-continue-teaching-actually-does) describes for automatic WWCC-expiry suspension — both write to the same `Course.status = suspended` transition in `catalogue`, distinguished by `suspensionReason`. This screen shows both kinds distinctly, not as one undifferentiated "suspended" list, so an admin can tell at a glance whether a suspension was their own action or an automatic consequence of an expired WWCC.

**Reinstate** clears `suspendedAt`/`suspensionReason` on the `InstructorProfile` but does **not** automatically republish any of the instructor's suspended courses (see [data-model.md](../data-model.md#re-approval-after-suspension)) — each needs separate review from [Admin Course Management](/3i/modules/catalogue/ui/screens/admin-course-management.md).

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).