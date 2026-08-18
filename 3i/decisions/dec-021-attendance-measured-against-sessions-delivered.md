---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-021
tags: [decision, certification, instructors]
---

# Attendance Is Measured Against Sessions Delivered

## Context

[3I-DEC-013](dec-013-instructor-removal-dismisses-course.md) established that losing an instructor mid-course dismisses the course. FR-CERT-02 requires ≥70% of sessions attended for an attendance certificate.

A course ending early makes 70% of the *scheduled* sessions unreachable. A learner with perfect attendance across every session actually held receives nothing.

## Decision

Taken 2026-08-18:

1. **Attendance is measured against sessions delivered, not sessions scheduled.** A learner present at all six of six held sessions has 100% attendance, whether or not ten were planned.
2. **The platform refuses to schedule sessions beyond an instructor's WWCC expiry date.**

## Reasoning

On (1): the threshold is meant to distinguish a learner who showed up from one who did not. Measuring against sessions that never happened measures the institute's disruption, not the learner's commitment.

On (2): FR-INST-03 already gives admin 60 days' notice before expiry, and FR-BAT-01 captures every session's date and time at batch creation. So the check is a date comparison at schedule time, and it converts a mid-course collapse into a scheduling error caught months earlier.

As things stand, the safeguarding control that protects children — blocking an expired-check instructor under FR-INST-04 — is also what destroys a cohort's certificates. Those should not be the same event.

## Scope

Both are changes requiring sign-off under §21.3. (1) reinterprets FR-CERT-02's denominator; (2) adds a constraint not in the baseline.

## Consequences

- A dismissed course still issues attendance certificates to learners who attended. Completion certificates remain unavailable if the final exam was never sat — consistent with [3I-DEC-011](dec-011-attendance-certificate-without-exam.md).
- Batch creation gains a validation: a session dated past the instructor's WWCC expiry is refused, naming the expiry date.
- The 60-day alert becomes actionable rather than informational — an instructor with sessions already scheduled near expiry has a concrete deadline.

## Cost

Measuring against delivered sessions means a course cancelled after one session of ten issues certificates to anyone who attended that one. The threshold is proportional, so 70% of one session is one session.

A floor — a minimum number of sessions before any certificate is issued — would fix that, and is not decided here. Worth raising if the client cares about what the certificate implies.
