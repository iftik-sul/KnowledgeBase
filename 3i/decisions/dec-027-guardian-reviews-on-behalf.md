---
project: 3i
type: decision
status: current
updated: 2026-08-23
id: 3I-DEC-027
tags: [decision, catalogue, safeguarding]
---

# Guardian Submits Ratings/Reviews on Behalf of Under-13 Profiles

## Context

FR-CRS-11 lets a learner rate a course 1–5 with an optional written review, once per course, after enrolment. The baseline does not say who submits this for a profile with no independent voice anywhere else on the platform — an under-13 profile has no login, no chat access of its own (FR-FAM-08, FR-CHAT-06), and no other authored content channel.

## Decision

Taken 2026-08-23: **for an under-13 profile, the guardian submits the rating and review on the profile's behalf.** Displayed with the same attribution format already used in chat — *"Fatima (guardian of Aisha)"* — per [3I-DEC-020](dec-020-guardian-on-behalf-chat-retained.md). One review per **profile** per course still applies (FR-CRS-11); the guardian is the author of record, not a co-author alongside the child.

**13–17 and adult profiles submit directly**, under their own name — no change from a literal reading of FR-CRS-11 for those bands.

## Reasoning

This is the same shape as guardian-on-behalf chat, for the same underlying reason: a child with no independent channel needs an adult to speak for them rather than being silently excluded from a feature the baseline otherwise grants every learner. Reusing the existing attribution convention rather than inventing a new one keeps "who is actually speaking" consistent and recognisable everywhere it appears on the platform, not just in chat.

## Consequences

- **`Review`** (see [3I-CAT-DM-001](/3i/modules/catalogue/data-model.md)) needs both the learner the review is *about* and the account that *submitted* it — these differ for a guardian-submitted review and are identical for a self-submitted one.
- Admin's review-hiding action (FR-CRS-11) applies identically regardless of who submitted — no special case for guardian-submitted reviews.
- The one-review-per-course limit is keyed to the **profile**, not the submitting account — a guardian with three enrolled under-13 children can submit three separate reviews for the same course, one per child's experience of it.

## Cost

None significant. Extends an existing, already-accepted pattern rather than introducing a new mechanism.

## Related

| | |
| :---- | :---- |
| Mirrors | [3I-DEC-020](dec-020-guardian-on-behalf-chat-retained.md) — guardian-on-behalf chat participation |
| Amends | FR-CRS-11 (author of record for under-13 profiles) |
| Data model | [3I-CAT-DM-001](/3i/modules/catalogue/data-model.md) |