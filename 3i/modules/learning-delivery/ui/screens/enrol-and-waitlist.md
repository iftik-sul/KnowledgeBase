---
project: 3i
module: learning-delivery
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-LDL-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - enrolment
---

# Screen: Enrol & Waitlist

Satisfies: FR-ENR-01, FR-ENR-02, FR-ENR-03, FR-ENR-04, FR-ENR-05, FR-ENR-06, FR-ENR-07

---

## Purpose

Enrol a profile into a course (and, for batch-based courses, a specific batch), including the age-gate check and override, and manage the resulting waitlist state if the batch is full.

## Access Gate

Member. Reached two ways — see [3I-DEC-034](/3i/decisions/dec-034-login-preserves-course-intent.md):

1. **Directly** from [Course Detail](/3i/modules/catalogue/ui/screens/course-detail.md)'s enrolment call-to-action, when the visitor already has an active session.
2. **Via [Login](/3i/modules/identity-and-access/ui/screens/login.md)'s return-to redirect**, when the visitor clicked the same CTA with no session — they land here immediately after authenticating (and completing profile selection), rather than at a generic post-login destination.

Not reachable at all from Registration — a newly-registered Member lands on Guardian Dashboard with zero profiles, and returns to a course's Enrol & Waitlist screen on their own once a profile and seat exist.

## Contents

- Which profile is enrolling (implicit if only one qualifies, same single-profile-skip principle as [3I-DEC-026](/3i/decisions/dec-026-single-profile-skips-picker.md), applied here rather than restated as a new decision).
- For `Online Class`/`Mixed` courses: batch selection, if more than one is open.
- If the profile's age doesn't meet the course's `minimumAge` but is within 2 years: the override option, requiring **explicit separate confirmation** (see [validation-rules.md](../validation-rules.md#age-gate-and-override)) — absent entirely if the gap exceeds 2 years or the course is `18+`.
- If the target batch is at capacity: waitlist join instead of direct enrolment, with the [Waitlist Position Badge](../components.md#waitlist-position-badge).

## Behaviour

**No seat purchase happens here** if the profile already has an active seat — enrolling in a second course consumes nothing further (FR-ENR-01, see [README.md](../../README.md#one-seat-many-courses)). If the profile has **no** active seat, this screen routes to [Pricing / Plan Selection](/3i/modules/commerce/ui/screens/pricing-plan-selection.md) instead of enrolling directly — enrolment cannot proceed without an active profile.

**On successful confirmation** — per [3I-DEC-037](/3i/decisions/dec-037-online-class-post-enrolment-routing.md), the same destination "Go to course" would later use on [Course Detail](/3i/modules/catalogue/ui/screens/course-detail.md):

| Course type | Lands on |
| :---- | :---- |
| Regular | [Course Materials List](/3i/modules/materials/ui/screens/course-materials-list.md) |
| Online Class / Mixed (batch-based) | The enrolled batch's [Chat Room](/3i/modules/communication/ui/screens/chat-room.md) |

No separate confirmation or "success" screen sits between this one and that destination — confirming enrolment takes the Member straight there.

**Once waitlisted**, this screen (or a notification linking back to it) is where a promoted `offered`-status learner accepts within the 48-hour window — see [validation-rules.md](../validation-rules.md#waitlist-promotion-window).

## Role Variations

Member only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
