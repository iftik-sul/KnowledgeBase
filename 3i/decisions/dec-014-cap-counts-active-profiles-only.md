---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-014
tags: [decision, identity, billing]
---

# The Six-Profile Cap Counts Active and Never-Activated Profiles Only

## Context

[3I-DEC-009](dec-009-seats-as-account-pool.md) introduced a profile state the baseline does not describe: inactive but preserved. FR-FAM-02 caps profiles at six. Whether an inactive profile occupies a cap slot was unresolved.

If it did, a guardian who had cycled through six children's profiles over several years would have a full account and no way to add a seventh without **deleting** one — destroying that child's progress and exam results (FR-FAM-10). Forcing a parent to erase one child's learning history to enrol another is a bad outcome to reach by accident.

## Decision

**The cap counts active and never-activated profiles. Cancelled-with-history profiles sit outside the cap, as archive.** Taken 2026-08-18.

There are four states, not three:

| State | Counts against cap | Notes |
| :---- | :---: | :---- |
| Active | Yes | A seat is bound to it |
| Never activated | Yes | Created, free, no seat ever purchased |
| Cancelled (inactive) | **No** | Archive. History preserved |
| Deleted | No | FR-FAM-10. History destroyed |

## Reasoning

The cap limits how many learners one subscription serves — a commercial constraint on people currently studying, not on archived history. An inactive profile consumes nothing.

**Never-activated profiles are the real abuse vector, not cancelled ones.** Profile creation is free, so an account could otherwise accumulate unlimited profiles at no cost. A cancelled profile was paid for at some point, and that payment is a natural brake. Capping active-plus-never-activated closes the free path while letting genuine history accumulate.

## Scope

This reinterprets what "maximum 6 learner profiles per account" means. It is a narrow change — the baseline never contemplated an inactive state — but it needs client sign-off under §21.3.

## Consequences

- The guardian dashboard (FR-FAM-09) shows four states and must make **cancelled** and **deleted** visibly distinct, since one preserves history and one destroys it.
- The seat purchase prompt (FR-BILL-04) fires against the active-plus-never-activated count, not the total profile count.
- Reactivating a cancelled profile brings it back inside the cap. If the account is already at six active, reactivation is refused until a seat is cancelled — the refusal message must say so, rather than reading as a generic failure.

## Cost

An account's total profile list grows without bound over years. This is accepted: it is archive, it is cheap, and the alternative destroys learning records.
