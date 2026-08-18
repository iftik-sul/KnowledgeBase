---
project: 3i
type: decision
status: draft
updated: 2026-08-18
id: 3I-DEC-012
tags: [decision, chat, safeguarding, privacy]
---

# Profile Deletion Removes That Profile's Chat Messages

## Context

Deleting a profile removes progress, enrolments, and exam results, while issued certificates remain valid and publicly verifiable (FR-FAM-10). Chat is not mentioned.

A 13–17 learner may participate in chat directly under their own display name (FR-CHAT-08), so a deleted profile can have authored messages.

## Decision

**Messages authored by a deleted profile are removed.** Taken in review, 2026-08-18.

## Unresolved — two problems

Recorded in [OQ-06](../open-questions.md#oq-06--chat-history-on-profile-deletion).

**It contradicts the baseline.** FR-CHAT-14 retains messages on *account* deletion and anonymises authorship to "Deleted user". A 15-year-old may exist as an account or as a profile (see [3I-DEC-002](dec-002-under-13-family-accounts.md)), so identical conduct is preserved or erased depending on which shape they happen to have. Either FR-CHAT-14 changes or this does.

**It destroys safeguarding evidence.** FR-CHAT-09 requires moderation actions to be logged; FR-CHAT-10 gives reports a 24-hour SLA that is tracked and reportable; FR-CHAT-12 makes logs auditable by admin across all rooms. If a reported message is deleted with the profile, the report and the action taken lose their subject — and the deletion is available to the guardian of the profile that authored it, rate-limited only by FR-FAM-06's two changes per 30 days.

Proposed instead: **remove message content, retain the moderation record.** Not yet agreed.

## Cost

As decided, a guardian can erase a child's conduct record by deleting and recreating the profile. That is worth being deliberate about rather than arriving at by inheritance from the progress-deletion rule.
