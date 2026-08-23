---
project: 3i
type: decision
status: deprecated
updated: 2026-08-18
id: 3I-DEC-008
tags: [decision, identity, scope-change, deprecated]
---

> **Retired 2026-08-18.** [3I-DEC-023](dec-023-no-standalone-accounts-under-18.md) removed the standalone account this decision proposed granting. The idea of offering an ageing-up path at any age has been dropped, not re-framed. This file is kept for history, per the repository's rule that a dropped feature is marked `deprecated` rather than deleted. Nothing below is active or should be built against.

# A Profile Reaching 13 Is Offered Its Own Account

## Context

A profile's date of birth is set at creation and cannot be edited (FR-FAM-07), so the system knows precisely when a learner turns 13. At that point they become eligible for a standalone account under FR-AUTH-05.

The baseline does not say what happens. A learner could remain a profile until 18 with nobody ever deciding otherwise.

## Decision

**On reaching 13, the learner is offered their own account.** Taken in review, 2026-08-18.

## Scope

**This is not in SRD v2.0 and is therefore new scope requiring a change request under §21.3.** It is recorded here as a decision because it has been taken, not because it is authorised to build.

## Seat Mechanism — Resolved by 3I-DEC-009

The seat question below is answered now that [3I-DEC-009](dec-009-seats-as-account-pool.md) is settled. The 13-year-old's family profile is deactivated by cancelling its seat, which preserves its history without deleting it (per DEC-009 point 3). The guardian's family subscription frees that seat's cost. The teenager's new standalone account is a separate subscription entirely — not paid for out of the family plan — activated the same way any new account is: no free trial, they pay for their own access from day one.

This does not resolve *whether* the family should stop paying and the teenager start paying, only that the mechanism for a guardian to release the family seat exists cleanly. Whether ageing up should default to "guardian cancels, teenager pays independently" versus "guardian keeps paying for the teenager's new account" is still open and is a commercial question, not a technical one.

## Unresolved

Recorded in [OQ-05](../open-questions.md#resolved):

- Who pays for the new standalone account — the teenager, or does the guardian's payment method carry over? Not yet decided.
- Who holds the chat toggle afterwards? FR-FAM-08 gives it to the guardian for a 13–17 *profile*; FR-AUTH-05 captures only a guardian email for a standalone 13–17 *account*. The permission has no defined handover.
- What if the learner declines? A profile that stays a profile until 18 must remain fully supported — and now clearly remains active-with-a-seat rather than being forced through any transition.
- What migrates — progress, enrolments, certificates — and what does FR-FAM-05's permanent name lock mean once the learner controls their own account? The old profile keeps its history regardless (DEC-009), so this is really about whether the *new* account should show that history or start blank.

## Cost

This creates a transition between the two shapes described in [3I-DEC-002](dec-002-under-13-family-accounts.md), and transitions are where safeguarding rules are most often dropped. The chat permission is the one to watch: a guardian-controlled toggle becoming self-controlled is a real change in a child's exposure, and it must be deliberate rather than incidental to the account migration.
