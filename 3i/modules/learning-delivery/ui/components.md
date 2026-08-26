---
project: 3i
module: learning-delivery
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-LDL-UI-COMP
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - components
---

# Learning Delivery — Shared Components

Documented once here. Screens link to this file rather than restating.

---

## Session Row

Used on: [Batch Schedule / Manage](screens/batch-schedule-manage.md), [Batch Roster \& Attendance](screens/batch-roster-attendance.md), [Batch Reschedule / Cancel](screens/batch-reschedule-cancel.md), and [Course Detail](/3i/modules/catalogue/ui/screens/course-detail.md)'s Class Schedule section (`catalogue`, cross-module reuse — added 2026-08-26).

One row per Session: date/time, status (`scheduled` / `delivered` / `cancelled`), and a context-appropriate action — mark attendance (roster view), reschedule (reschedule view), or **nothing** (read-only). **Course Detail uses the read-only variant** — no status badge, no action, since a pre-enrolment visitor has no attendance or reschedule concern; only date, time, and duration are shown. A `delivered` session's row is visually distinct from `scheduled` on the instructor-facing variants, since "has this already happened" is the single fact [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md)'s attendance denominator depends on and it should be legible at a glance, not inferred from the date alone — this distinction doesn't apply to the read-only Course Detail variant, where every session is necessarily still upcoming.

**Times are always displayed in the viewer's local time zone**, converted automatically from the stored UTC/server time — never a fixed timezone label the learner has to mentally convert. No timezone selector exists anywhere; this is handled transparently.

## Waitlist Position Badge

Used on: [Enrol \& Waitlist](screens/enrol-and-waitlist.md).

Shows the learner's current numeric position (FR-ENR-06) while `status = waitlisted`, or a distinct "offer expires in [countdown]" state while `status = offered` (FR-ENR-07) — these are visually different states, not the same badge with different text, since one is passive waiting and the other is a time-limited action the Member needs to actually take.
