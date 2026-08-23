---
project: 3i
module: communication
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CMN-UI-004
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - chat
  - instructor
---

# Screen: Instructor Room Management

Satisfies: FR-CHAT-09, FR-CHAT-13

---

## Purpose

An instructor moderates their own course/batch's room — delete a message, mute or remove a participant, or close the room entirely.

## Access Gate

Instructor, for rooms belonging to courses/batches they own.

## Contents

Participant list with mute/remove actions per person, and delete available directly on any [Message Bubble](../components.md#message-bubble) in the room view. A **Close Room** action, styled and confirmed as the most consequential of the four — it ends the room's writable life entirely, not just one participant's.

## Behaviour

**Every action here writes a `ModerationAction` row** (FR-CHAT-09) — there is no quiet-delete path; a removed message leaves the same tombstone-style gap marker a profile-deletion tombstone does, so participants see something was taken down rather than the conversation silently reflowing.

**Closing a room** flips it to `closed` — read-only archive, not hidden (FR-CHAT-13). This is not reversible from this screen; reopening, if ever needed, is not specified in the baseline and isn't offered here.

## Role Variations

Instructor only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the instructor panel supports it (FR-LOC-04).