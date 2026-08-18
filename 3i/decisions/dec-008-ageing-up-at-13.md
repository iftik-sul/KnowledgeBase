---
project: 3i
type: decision
status: draft
updated: 2026-08-18
id: 3I-DEC-008
tags: [decision, identity, scope-change]
---

# A Profile Reaching 13 Is Offered Its Own Account

## Context

A profile's date of birth is set at creation and cannot be edited (FR-FAM-07), so the system knows precisely when a learner turns 13. At that point they become eligible for a standalone account under FR-AUTH-05.

The baseline does not say what happens. A learner could remain a profile until 18 with nobody ever deciding otherwise.

## Decision

**On reaching 13, the learner is offered their own account.** Taken in review, 2026-08-18.

## Scope

**This is not in SRD v2.0 and is therefore new scope requiring a change request under §21.3.** It is recorded here as a decision because it has been taken, not because it is authorised to build.

## Unresolved

Recorded in [OQ-05](../open-questions.md#oq-05--ageing-up-at-13):

- Does the new account consume a family seat, or free one? Depends on [3I-DEC-009](dec-009-seats-as-account-pool.md).
- Who holds the chat toggle afterwards? FR-FAM-08 gives it to the guardian for a 13–17 *profile*; FR-AUTH-05 captures only a guardian email for a standalone 13–17 *account*. The permission has no defined handover.
- What if the learner declines? A profile that stays a profile until 18 must remain fully supported.
- What migrates — progress, enrolments, certificates — and what does FR-FAM-05's permanent name lock mean once the learner controls their own account?

## Cost

This creates a transition between the two shapes described in [3I-DEC-002](dec-002-under-13-family-accounts.md), and transitions are where safeguarding rules are most often dropped. The chat permission is the one to watch: a guardian-controlled toggle becoming self-controlled is a real change in a child's exposure, and it must be deliberate rather than incidental to the account migration.
