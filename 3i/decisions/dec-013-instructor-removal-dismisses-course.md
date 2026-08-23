---
project: 3i
type: decision
status: current
updated: 2026-08-23
id: 3I-DEC-013
tags: [decision, instructors, batches]
---

# Losing an Instructor Mid-Course Dismisses the Course

> **Status corrected 2026-08-23** — this file's frontmatter read `status: draft` despite the decisions register having listed it as `current` since 2026-08-18, and despite [3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md) having resolved the "Unresolved" section below the same day it was written. Flagged and fixed while scaffolding `learning-delivery`, which depends on both. No content below is changed, only the status and this notice.

## Context

There is one instructor per course, and course ownership belongs to them (FR-INST-06). Multi-instructor and co-taught courses are out of scope (§23 item 4), so there is no one to hand over to.

Two events remove an instructor mid-delivery: admin suspension (FR-INST-07), and WWCC expiry, which blocks them from continuing to teach any course tagged under 18 (FR-INST-04).

## Decision

**The course is dismissed.** Taken in review, 2026-08-18.

FR-INST-07 already sets the surrounding behaviour: published courses become suspended, enrolled learners retain access to completed materials and may join a future batch. No refund is triggered, since access is subscription-based (FR-BAT-05).

## Resolved (was "Unresolved")

**Resolved by [3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md), 2026-08-18, the same day this decision was drafted.** The question below was live for only a few hours within the same review session:

~~FR-CERT-02 requires ≥70% of sessions attended. A course ending early makes 70% of the *scheduled* sessions unreachable, so a learner with perfect attendance across every session actually held receives nothing.~~

~~Proposed: measure against sessions **delivered**, not scheduled. Not yet agreed.~~

DEC-021 agreed exactly that proposal, and additionally implemented this decision's own "WWCC case should not arise" suggestion below as a real scheduling constraint, not just a recommendation.

## The WWCC Case — Implemented

FR-INST-03 gives admin 60 days' notice before expiry. [3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md) makes this actionable: **the platform refuses to schedule a session dated past an instructor's WWCC expiry.** A batch's sessions are all known at creation (FR-BAT-01), so this is a date comparison at schedule time — see [learning-delivery's data model](/3i/modules/learning-delivery/data-model.md#the-wwcc-scheduling-guard) for where this check actually lives.

## Cost

As it stood before DEC-021, the safeguarding control that protects children — blocking an expired-check instructor — was also what destroyed a cohort's certificates. DEC-021 is what stops those being the same event.