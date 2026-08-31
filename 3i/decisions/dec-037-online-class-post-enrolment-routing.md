---
project: 3i
type: decision
status: current
updated: 2026-08-26
id: 3I-DEC-037
tags: [decision, navigation, ux, learning-delivery, communication, catalogue]
---

# Enrolment Success and "Go to Course" for Online Class Both Route to the Batch's Chat Room

## Context

[3I-DEC-035](dec-035-course-detail-cta-three-states.md) resolved "Go to course" for a **Regular** course (routes to [Course Materials List](/3i/modules/materials/ui/screens/course-materials-list.md)) but explicitly left the **Online Class** case open, since Online Class courses carry no materials at all ([catalogue/data-model.md](/3i/modules/catalogue/data-model.md#course)). Separately, [`enrol-and-waitlist.md`](/3i/modules/learning-delivery/ui/screens/enrol-and-waitlist.md) never specified what happens immediately after "Confirm enrolment" succeeds, for either course type.

Investigating the Online Class case surfaced that the real mechanism already exists: [`learning-delivery/data-model.md`](/3i/modules/learning-delivery/data-model.md#session) states plainly that meeting-link distribution **"is a `communication`-module action... `communication` owns actually sending the link out"** — and `communication`'s own module notes confirm **one chat room per batch** for Online Class/Mixed courses. The missing piece wasn't a screen; it was a routing decision plus one small addition to a screen that already existed.

## Decision

**One rule, not two — the same destination applies to both "just confirmed enrolment" and every later "Go to course" click:**

| Course type | Destination |
| :---- | :---- |
| Regular | [Course Materials List](/3i/modules/materials/ui/screens/course-materials-list.md) — unchanged, already correct per [3I-DEC-035](dec-035-course-detail-cta-three-states.md) |
| Online Class (or the Online-Class-delivered portion of Mixed) | The enrolled batch's **Chat Room** (`communication`) — directly, no intermediate landing screen |

**No separate "first landing" screen for either case.** Confirming enrolment on [Enrol \& Waitlist](/3i/modules/learning-delivery/ui/screens/enrol-and-waitlist.md) and clicking "Go to course" on a later visit to [Course Detail](/3i/modules/catalogue/ui/screens/course-detail.md) land in exactly the same place — consistent with how the Regular path already works, where there's no special first-time detour either.

**[Chat Room](/3i/modules/communication/ui/screens/chat-room.md) gains one addition to support this:** a persistent info bar showing the batch's next scheduled session — "Next session: [date, time]," pulled from the next upcoming `Session` record, shown in the viewer's local time zone (same silent-conversion principle already established for [Session Row](/3i/modules/learning-delivery/ui/components.md#session-row)). This bar only appears on rooms scoped to a `Batch` with upcoming sessions — a course-level room with no batch scoping shows no such bar, since there's nothing to schedule.

**[Learner Dashboard](/3i/modules/identity-and-access/ui/screens/learner-dashboard.md) remains an independent path to the same room** via its Enrolled Courses section — it is not a required intermediate stop between enrolling and reaching the room, just an additional way to find it later.

## Consequences

- [`enrol-and-waitlist.md`](/3i/modules/learning-delivery/ui/screens/enrol-and-waitlist.md) gains an explicit "on successful confirmation" statement covering both course types.
- [`chat-room.md`](/3i/modules/communication/ui/screens/chat-room.md) gains the next-session info bar, conditional on batch scoping.
- No new screen anywhere — this decision is entirely routing plus one additive UI element on an existing, already-specified screen.

## Cost

None beyond the one info-bar addition. This was deliberately chosen over building a separate "batch details" or "my schedule" screen, since the real mechanism already existed and needed a destination decision more than it needed new surface area.
