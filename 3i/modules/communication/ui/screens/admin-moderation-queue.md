---
project: 3i
module: communication
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CMN-UI-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - chat
  - admin
  - safeguarding
---

# Screen: Admin Moderation Queue

Satisfies: FR-CHAT-10, FR-CHAT-12

---

## Purpose

Admin reviews and resolves reported messages, and can audit chat across every room — not only the reported ones.

## Access Gate

Admin only.

## Contents

**Reports tab:** every `open`-status `ChatMessageReport`, sorted by SLA urgency (closest to the 24-hour target first), each showing the reported message in its [Message Bubble](../components.md#message-bubble) context, the report reason, and resolve/dismiss actions leading into the same moderation actions [Instructor Room Management](instructor-room-management.md) exposes (delete message, mute, remove participant).

**An overdue-reports count is visible on the admin dashboard** (FR-CHAT-10's own acceptance criterion), not just on this screen.

**Audit tab:** search across **every room on the platform**, not scoped to any one instructor's courses (FR-CHAT-12) — this is the one place chat history is browsable outside its own room context.

## Behaviour

Resolving a report sets `respondedAt` and records the action taken — which may be "no action, message was appropriate" as legitimately as any moderation action, since not every report is upheld.

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).