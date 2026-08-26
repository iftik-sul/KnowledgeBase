---
project: 3i
type: decision
status: current
updated: 2026-08-26
id: 3I-DEC-035
tags: [decision, navigation, ux, catalogue, materials]
---

# Course Detail's Enrolment CTA Has Three States, Not Two

## Context

[3I-DEC-034](dec-034-login-preserves-course-intent.md) documented two states for [Course Detail](/3i/modules/catalogue/ui/screens/course-detail.md)'s enrolment call-to-action: no session (route to Login, carrying course intent) and an active session with no qualifying enrolment (route directly to [Enrol & Waitlist](/3i/modules/learning-delivery/ui/screens/enrol-and-waitlist.md)). A third state — **already enrolled** — was never addressed, and a Figma mockup built against the two-state version showed "View enrolment options" for an enrolled Member, identical to the not-enrolled case. That's wrong: someone already in the course has no reason to see enrolment options at all.

Resolving this connects `catalogue` to `materials` for the first time — the actual destination for an enrolled viewer is [Course Materials List](/3i/modules/materials/ui/screens/course-materials-list.md), a screen this module never referenced before.

## Decision

**The CTA has three states:**

| State | Button reads | Destination |
| :---- | :---- | :---- |
| No session | (per DEC-034) | Login, carrying course reference |
| Session, no qualifying enrolment on this course | "View enrolment options" | [Enrol & Waitlist](/3i/modules/learning-delivery/ui/screens/enrol-and-waitlist.md) |
| Session, qualifying enrolment exists | "Go to course" | [Course Materials List](/3i/modules/materials/ui/screens/course-materials-list.md) |

**The enrolment check for this CTA (and for [Rate & Review](/3i/modules/catalogue/ui/screens/rate-and-review.md), which already does this) is at the Member level — across any of the Member's profiles — not tied to whichever profile happens to be active in the session.** This matters because [Course Materials List](/3i/modules/materials/ui/screens/course-materials-list.md)'s own access gate requires a specific **active** learner profile, a narrower condition than the Member-level check that decides whether "Go to course" appears at all. The two checks are related but not identical, and this decision is what reconciles them:

- **Exactly one of the Member's profiles has a qualifying enrolment on this course:** "Go to course" resolves that profile implicitly and opens [Course Materials List](/3i/modules/materials/ui/screens/course-materials-list.md) directly — same single-profile-skip principle as [3I-DEC-026](dec-026-single-profile-skips-picker.md), applied here rather than restated.
- **More than one profile qualifies** (e.g. two siblings both enrolled in the same course): "Go to course" first shows a "which profile" selection, the same pattern [Rate & Review](/3i/modules/catalogue/ui/screens/rate-and-review.md) already uses for its own profile-select step — not a new mechanism, the same one reused a second time.

## Consequences

- [`course-detail.md`](/3i/modules/catalogue/ui/screens/course-detail.md)'s CTA section rewritten to state all three cases, superseding the two-state version DEC-034 introduced (DEC-034 itself is unchanged and remains accurate for what it actually claimed — the Login/Registration distinction — this decision adds the third case DEC-034's scope never covered).
- [`course-materials-list.md`](/3i/modules/materials/ui/screens/course-materials-list.md) gains the "reached from" statement it was missing, plus the profile-resolution note above.
- The already-built "Enrolled Member" Course Detail Figma frame needs a repair pass: its sticky card button changes from "View enrolment options" to "Go to course," linking toward materials rather than back into enrolment.

## Cost

None beyond the frame correction above — this closes a real inconsistency rather than opening new scope, and reuses the existing profile-selection pattern rather than inventing a second one.
