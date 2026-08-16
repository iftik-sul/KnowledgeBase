---
project: 3i
type: decision
status: current
updated: 2026-08-16
id: 3I-DEC-001
tags: [decision, data-model]
---

# Learner Is the Universal Unit of Study

## Context

The obvious modelling choice in an LMS is to hang enrolment, progress, submissions, and certificates off `User`. That works only while every studying party is also an account holder.

3i breaks that assumption immediately. A guardian holds one account and may carry several children as learner profiles beneath it. Those children study, submit, and earn certificates, but they are not users — they do not authenticate, and under the age gate they must not.

## Decision

**`Learner` is the entity that studies.** Every record describing study — enrolment, progress, attempt, submission, grade, certificate — references `Learner`, never `User`.

`User` models an authenticating party. An independent adult learner has both a `User` and a `Learner`; a child has a `Learner` with no `User`; a guardian may have a `User` with no `Learner` of their own.

## Consequences

- Every query in the study path filters on learner, not on the authenticated user. Authorisation becomes a separate question: *may this user act for this learner?*
- Guardians switching between children is a change of learner context, not a change of session. This must not be modelled as impersonation.
- An independent adult and a supervised child are the same shape downstream. No feature needs to branch on which it is.
- Migrating an ageing-out child to their own `User` attaches an account to an existing `Learner`. Study history is untouched, because it never referenced the account.

## Cost

Any code written against `User` in the study path is wrong even when it happens to work for adult learners in testing, because the adult case is the one where the two entities coincide. This is the failure mode to watch for in review.
