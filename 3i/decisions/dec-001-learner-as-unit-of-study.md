---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-001
tags: [decision, data-model]
---

# Learner Is the Unit of Study

## Context

The obvious modelling choice is to hang enrolment, progress, submissions, and certificates off the account. That works only while every studying party is also an account holder.

3i breaks that immediately. An account may carry up to six learner profiles (FR-FAM-02). A profile has no email address and no credentials (FR-FAM-03) — it studies, submits, and earns certificates without ever authenticating. Under-13 learners cannot hold an account by any route (FR-AUTH-03).

## Decision

**The learner profile is the entity that studies.** Every record describing study — enrolment, progress, attempt, submission, grade, certificate, attendance — references the profile, never the account.

The account is the authenticating and billing party. Profile selection happens after account login, via a picker (FR-FAM-04).

## Consequences

- Every query in the study path filters on profile, not on the authenticated account. Authorisation becomes a separate question: may this account act for this profile?
- Switching between children is a change of profile context, not of session. It must not be modelled as impersonation.
- The billing contact is separable from the account identity, and defaults to the guardian where minor profiles exist (FR-BILL-05). Three parties — payer, account holder, learner — may be three different people.
- An adult studying alone and a supervised child are the same shape downstream. No feature branches on which it is.

## Cost

Every account has at least one profile, including an adult studying alone. That case is the one where account and profile coincide, so code written against the account will pass testing and fail for families. This is the specific regression to watch for in review.
