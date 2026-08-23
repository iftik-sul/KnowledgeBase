---
project: 3i
module: communication
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CMN-UI-VAL
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - validation
---

# Communication — Validation Rules

Field-level validation shared across two or more communication screens.

---

## Message Content

On [Chat Room](screens/chat-room.md): text only, non-empty, no attachment field exists to validate against (FR-CHAT-02) — there is nothing to reject here beyond emptiness, since the type system itself prevents anything but text from ever reaching this validation point. Every message runs through the server-side profanity/link filter on send (FR-CHAT-11); a filtered message never reaches the room, and the sender sees this immediately, not as a later removal.

## Report Reason Required

On [Report Message](screens/report-message.md): a reason is required, free text, non-empty — not baseline-mandated in so many words, but consistent with every other consequential-action-needs-a-reason pattern already established across this project (waiver rejection, instructor rejection, certificate revocation).