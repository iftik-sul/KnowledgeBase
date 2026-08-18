---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-016
tags: [decision, chat, safeguarding, privacy]
supersedes: dec-012-chat-history-on-profile-deletion.md
---

# Profile Deletion Removes Message Content, Retains the Moderation Record

## Context

[3I-DEC-012](dec-012-chat-history-on-profile-deletion.md) recorded that deleting a profile removes its chat messages outright. Two problems were raised against it: it contradicts FR-CHAT-14, and it destroys safeguarding evidence.

## Decision

**Message content is removed. The record is retained.** Taken 2026-08-18, superseding 3I-DEC-012.

On profile deletion:

| Element | Treatment |
| :---- | :---- |
| Message body | Replaced with a tombstone |
| Author display name | Anonymised to "Deleted learner" |
| Message ID, room, timestamp | Retained |
| Reports against the message (FR-CHAT-10) | Retained |
| Moderation actions taken (FR-CHAT-09) | Retained |

## Reasoning

**It resolves the contradiction.** FR-CHAT-14 already does exactly this for *account* deletion — messages retained, authorship anonymised to "Deleted user". A 15-year-old may exist as either an account or a profile ([3I-DEC-002](dec-002-under-13-family-accounts.md)), and identical conduct should not be preserved or erased depending on which shape they happen to have.

**It is what privacy law actually requires.** The Australian Privacy Principles and GDPR require erasure of personal data, not destruction of child-safety records. Retaining a moderation log has a clear lawful basis. Deleting the evidence that a report was raised and acted upon protects nobody — least of all the child who raised it.

**The abuse case matters.** Without this, a guardian could erase a child's conduct record by deleting the profile, rate-limited only by FR-FAM-06.

## Consequences

- The deletion confirmation screen must state plainly what is destroyed and what is kept. A parent should not discover afterwards that a moderation record survived.
- Admin chat audit across all rooms (FR-CHAT-12) continues to function over deleted profiles' history, which is the point.
- Tombstoned messages remain visible in the room's read-only archive (FR-CHAT-13), preserving conversational context for other participants.

## Cost

A room's history will accumulate tombstones. Accepted — a gap where a message was is more honest than silently reflowing the conversation as though nothing was said.
