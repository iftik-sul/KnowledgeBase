---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-020
tags: [decision, chat, safeguarding]
---

# Guardian-on-Behalf Chat Participation Is Retained

## Context

"No chat under 13" was reaffirmed in review. It is already the baseline: FR-FAM-08 makes under-13 chat permanently off, and FR-CHAT-06 gives the child no access.

The question raised was whether that also removes **guardian-on-behalf participation** (FR-CHAT-06) and **automatic guardian-only room mode** (FR-CHAT-07).

## Decision

**Both are retained.** Taken 2026-08-18. No change to FR-CHAT-06 or FR-CHAT-07.

The child has no chat access. The guardian participates for them, displayed as *"Fatima (guardian of Aisha)"*. Where a course's minimum age is under 13, the room is guardian-only, derived from the age tag and not configurable by the instructor.

## Reasoning

Removing guardian participation would leave an under-13 course with a room the learners cannot use and the guardians cannot use either — an instructor talking to nobody.

**The concrete reason is FR-BAT-02.** The instructor posts the meeting link to the batch group chat *and* by email. Remove guardian participation from under-13 rooms and link distribution for children's live classes rests on email alone, with no fallback and no visible record in the room.

The safeguarding requirement is that a child has no unsupervised channel to an adult (§3.3). Guardian-only mode satisfies that completely — every participant is an adult.

## The Alternative, If Revisited

If under-13 courses should genuinely have no room at all, the clean version is **not creating the room**, rather than creating one nobody can post in. That would require amending FR-BAT-02's link distribution to email-only for those batches, and it should be decided deliberately rather than arrived at by deleting FR-CHAT-06.

## Consequences

- Guardian-only mode remains structural, not policy. A room containing an under-13 course is safe by construction rather than by moderation.
- The display format matters and is specified: the guardian is never shown as the child.

## Known Gap

An under-13 learner enrolled into a 13+ course via the FR-ENR-04 override has **no route into the discussion at all** — their own access is off, and the room is not guardian-only because the course is tagged 13+. Confirmed as intended, recorded in [age-and-safeguarding.md](/3i/age-and-safeguarding.md#5-the-enrolment-override).
