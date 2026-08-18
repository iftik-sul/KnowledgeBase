---
project: 3i
type: decision
status: draft
updated: 2026-08-18
id: 3I-DEC-013
tags: [decision, instructors, batches]
---

# Losing an Instructor Mid-Course Dismisses the Course

## Context

There is one instructor per course, and course ownership belongs to them (FR-INST-06). Multi-instructor and co-taught courses are out of scope (§23 item 4), so there is no one to hand over to.

Two events remove an instructor mid-delivery: admin suspension (FR-INST-07), and WWCC expiry, which blocks them from continuing to teach any course tagged under 18 (FR-INST-04).

## Decision

**The course is dismissed.** Taken in review, 2026-08-18.

FR-INST-07 already sets the surrounding behaviour: published courses become suspended, enrolled learners retain access to completed materials and may join a future batch. No refund is triggered, since access is subscription-based (FR-BAT-05).

## Unresolved

Recorded in [OQ-04](../open-questions.md#oq-04--attendance-threshold-after-a-dismissed-course).

FR-CERT-02 requires ≥70% of sessions attended. A course ending early makes 70% of the *scheduled* sessions unreachable, so a learner with perfect attendance across every session actually held receives nothing.

Proposed: measure against sessions **delivered**, not scheduled. Not yet agreed.

## The WWCC case should not arise

FR-INST-03 gives admin 60 days' notice before expiry. The platform should refuse to schedule sessions beyond an instructor's WWCC expiry date, which turns a mid-course collapse into a scheduling error caught months earlier.

That is not in the baseline and would be a change request. It is the cheaper fix by a wide margin: a batch's sessions are all known at creation (FR-BAT-01), so the check is a date comparison at schedule time.

## Cost

As it stands, the safeguarding control that protects children — blocking an expired-check instructor — is also what destroys a cohort's certificates. Those should not be the same event.
