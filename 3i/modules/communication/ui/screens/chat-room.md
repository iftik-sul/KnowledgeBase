---
project: 3i
module: communication
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CMN-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - chat
  - safeguarding
---

# Screen: Chat Room

Satisfies: FR-CHAT-01, FR-CHAT-02, FR-CHAT-03, FR-CHAT-04, FR-CHAT-05, FR-CHAT-06, FR-CHAT-07, FR-CHAT-08, FR-CHAT-13

---

## Purpose

The room itself — real-time group chat scoped to a course or batch, with guardian-only mode engaging automatically where the course's age tag calls for it.

## Access Gate

Member with a qualifying enrolment on the room's course/batch. **Under-13 profiles have no access of their own** (FR-CHAT-06) — the guardian's own Member session participates instead, with every message they send on the child's behalf carrying the [Guardian Attribution Tag](../components.md#guardian-attribution-tag). 13–17 profiles participate directly, subject to the guardian toggle (FR-CHAT-08). Instructor sees the same room for any course/batch they own, with moderation actions available (see [Instructor Room Management](instructor-room-management.md)).

## Contents

Real-time [Message Bubble](../components.md#message-bubble) stream over WebSocket (FR-CHAT-01), a text-only composer (no attachment button exists, FR-CHAT-02), and search across the room's history (FR-CHAT-05). **Flat structure** — no pinned/announcement section, no thread nesting (FR-CHAT-04).

**Guardian-only mode is visually stated on the room**, not just enforced silently — a guardian entering a room derived from an under-13 course tag should see plainly that every other visible participant is also an adult, since that's the actual safety property FR-CHAT-07 provides.

A **closed** room ([Instructor Room Management](instructor-room-management.md)) renders identically except the composer is replaced with a "this room is closed" notice — history remains fully visible (FR-CHAT-13).

## Behaviour

Every send passes through the server-side filter before reaching anyone else (FR-CHAT-11) — a filtered message never appears in the shared stream; only the sender sees it was withheld, inline. A **report** action is available on every message (see [Report Message](report-message.md)).

## Role Variations

**Member:** participates directly or on a child's behalf, per age.
**Instructor:** same room view, plus moderation entry points — see [Instructor Room Management](instructor-room-management.md).

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04): message alignment, composer layout, and timestamp positioning all mirror.