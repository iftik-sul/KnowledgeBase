---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-023
tags: [decision, identity, safeguarding, scope-change]
supersedes: FR-AUTH-05's standalone teen registration path
---

# No Standalone Accounts Under 18 — Every Minor Is a Guardian Profile

## Context

The baseline (FR-AUTH-05) let a 13–17 year old register a **standalone account** of their own — their own email, password, and login — with a guardian's name and email captured alongside it, and a single notification email sent to that address.

Reviewing that flow surfaced a real gap: **nothing verified the guardian was actually 18+, or even a real person.** The guardian fields were free text typed in by the teenager. Compare that to every other guardian relationship on the platform, which only ever exists between a verified adult account (already passed the real date-of-birth check on registration) and a profile beneath it. The standalone-teen path was the one place "guardian" didn't mean what it meant everywhere else.

## Decision

**Every learner under 18 exists only as a profile under a verified adult account.** No independent login exists for anyone under 18, regardless of age. Taken 2026-08-18.

Registration collapses to two outcomes, not three:

| Date of birth | Outcome |
| :---- | :---- |
| **18+** | Account created normally |
| **Under 18 — any age** | Registration is refused. Redirected toward creating a family account instead |

The 13–17-specific redirect screen (formerly [Screen 2 / 3I-IDA-UI-002](modules/identity-and-access/ui/screens/registration-standalone-teen.md)) is **removed entirely** — it no longer has a reason to exist, since 13–17 now follows exactly the same path as under-13: redirect to family registration.

**What is unaffected:** the 13–17 chat toggle (FR-FAM-08) stays exactly as it was. A 13–17 profile still gets a guardian-controlled toggle; a younger profile still doesn't. That distinction was never about account type — it was always about age, and it still is.

## Reasoning

This closes the verification gap completely rather than patching it. Under this model, "guardian" always resolves to a real account that passed the same 18+ date-of-birth check every adult account passes. There is no longer a code path where a guardian relationship exists without that check having happened.

It also removes an inconsistency the review surfaced independently: a standalone 13–17 account's guardian got one notification email and nothing else — no dashboard, no ongoing say, no chat control — while a 13–17 *profile*'s guardian got continuous oversight including the chat toggle. Two teenagers of the same age had very different safety postures depending purely on who filled out the form first. Collapsing to one path removes that inconsistency along with the verification gap.

## Scope

**This reverses FR-AUTH-05, not merely amends it.** Every other decision in this register adjusted baseline behaviour; this one removes an entire account type the baseline specifies. It is the largest scope change in the project so far and should be flagged to the client distinctly from the earlier seven-item batch, not folded into it silently.

The real cost, stated plainly: a 17-year-old six months from turning 18 has **no account of their own** under this model — same as a 6-year-old. Whether that's the right trade-off for an international, subscription-based platform serving independent-minded older teens as well as young children is a product question, not just a safeguarding one. Recorded here as approved per [3I-DEC-README's operating assumption](README.md), consistent with how the prior seven items were handled.

## Consequences

- **`Account` no longer needs `guardianName` / `guardianEmail` fields.** Those existed solely to support FR-AUTH-05. Removing them is a schema simplification, not a loss — no other feature reads them.
- **Registration branches on one threshold (18), not two (13 and 18).** Screen 1 and the redirect screen (formerly under-13-only) now share identical logic for anyone under 18.
- **The guardian-notification-on-registration behaviour is gone.** There is no longer any point where an unverified guardian email receives an automated email from a teen's own registration attempt — because that registration attempt never reaches account creation.
- Everywhere in this repository that says "13–17 may register standalone" is now wrong and needs correcting: [age-and-safeguarding.md](../age-and-safeguarding.md), the module README, [3I-IDA-DM-001](modules/identity-and-access/data-model.md), [3I-IDA-REQ-001](modules/identity-and-access/requirements/auth-registration-and-authentication.md), the UI index and screens, and [backend-spec.md](modules/identity-and-access/backend-spec.md).

## Cost

Losing standalone teen accounts is a real product cost, not a free safety win. An institute serving learners internationally, some of whom may not have an engaged guardian managing an account on their behalf, loses a path that served exactly that learner. If that turns out to matter in practice, the fix is not reintroducing FR-AUTH-05 as originally written — it would need real guardian verification (matching against an existing adult account, or a confirmed accept/decline link) rather than the unverified text field the baseline had.
