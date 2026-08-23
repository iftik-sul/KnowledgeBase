---
project: 3i
module: communication
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CMN-UI-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - chat
  - safeguarding
---

# Screen: Report Message

Satisfies: FR-CHAT-10

---

## Purpose

Any participant flags a message for admin review.

## Access Gate

Any Member or Instructor participant in the room the message belongs to.

## Contents

The message being reported (shown for context), a required reason field (see [validation-rules.md](../validation-rules.md#report-reason-required)), and a submit action. Copy on this screen is in the exempt safeguarding-string set — [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) — and requires named human sign-off per language before launch.

## Behaviour

Submitting creates a `ChatMessageReport` with `status = open`, entering the [Admin Moderation Queue](admin-moderation-queue.md) with the 24-hour SLA clock starting immediately (FR-CHAT-10). **The reported message is not automatically hidden or removed on report alone** — reporting flags it for review; only an admin or instructor moderation action (delete, mute, remove) actually changes what other participants see.

## Role Variations

Identical for Member and Instructor.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).