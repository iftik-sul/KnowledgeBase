---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-009
tags: [decision, billing, enrolment]
---

# A Seat Is a Permanent, Non-Transferable Grant to One Profile

## Context

One seat is included in the subscription; additional seats carry a per-seat monthly charge, to a maximum of six profiles (§14.1, FR-FAM-02). Seat count is a Stripe quantity (FR-BILL-04). The baseline left two things unstated: whether a seat is consumed by enrolling a learner or by concurrent viewing, and whether it can move between profiles.

Two conflicting requirements pointed at different readings. FR-ENR-01 requires an available seat *for that learner* to enrol, which implies enrolling spends a seat. FR-AUTH-12 caps concurrent video streams by seats purchased, which implies watching spends a seat. Both cannot be independently true.

## Decision

Settled in review, 2026-08-18:

1. **A seat is an enrolment grant, not a viewing slot.** One seat purchased makes exactly one profile active — able to enrol and study. FR-AUTH-12's concurrency cap is a *consequence* of this, not a separate mechanism: a profile with no seat cannot enrol, so it cannot stream either. With two seats, at most two profiles can ever be active, so at most two can ever be streaming simultaneously — the cap is automatically satisfied and needs no independent enforcement.

2. **A seat is permanently bound to the profile it activates.** It is never reassigned or switched to a different profile while both exist. If a guardian wants a different child studying under the same money, the running seat is cancelled and a new one is purchased for the other profile.

3. **Cancelling a seat deactivates the profile; it does not delete it.** The profile becomes inactive — unenrolled, unable to study — but its history (progress, certificates, exam results) is fully preserved: the same protection FR-FAM-10 gives on deletion, without deletion occurring.

4. **An inactive profile can be reactivated later** by purchasing a new seat for it. This is a genuine second payment, not a toggle — there is no free trial anywhere in the baseline (§14.1), so reactivation always costs money. That absence of a free tier is what keeps this safe from abuse: there is no incentive to cycle seats across profiles, because every activation is paid regardless.

5. **The subscription flow is: create account (free) → create profile (free) → activate a specific profile by paying for a seat → optionally cancel (deactivate, preserve history) → optionally reactivate (pay again).** Profile creation carries no charge and touches no seat; only activation and cancellation are billing events.

6. **FR-FAM-02's six-profile cap stands.** Removing it was considered in the same review and rejected. The cap is retained.

## Consequences

- **A new profile state exists that the baseline does not describe.** FR-FAM only distinguishes an active profile from a deleted one (FR-FAM-10). This decision introduces a third: inactive-but-preserved. The guardian dashboard (FR-FAM-09) needs to represent this distinctly from both, and any UI or data-model document for the FAM area must specify it explicitly rather than inheriting the two-state assumption from the baseline text.

- **FR-FAM-06's rate limit applies to activation and cancellation, not to profile creation.** Creating a profile is free and untracked against the 2-changes-per-30-days limit; only the paid, seat-consequential actions are throttled. This is a redefinition of what FR-FAM-06 counts as a "change" — the baseline's own wording is "profile creation and deletion" — and should be stated explicitly wherever that requirement is implemented. With the six-profile cap retained, the cap now does most of the work the creation limit was doing.

- **FR-AUTH-12 is satisfied automatically** and should not be implemented as an independent concurrency check. Documenting it as a consequence of the seat model, not a second control, avoids a redundant and possibly conflicting enforcement path being built later.

- **Ageing up at 13** ([3I-DEC-008](dec-008-ageing-up-at-13.md)) has a concrete mechanism: the guardian cancels the 13-year-old's seat on the family account, and the teenager's standalone account is activated separately. The family profile's history stays attached to the now-inactive profile; snapshotted certificates remain valid per [3I-DEC-005](dec-005-denormalised-certificates.md).

## Cost — the cap and the inactive state interact badly

Retaining the six-profile cap alongside the new inactive state creates a squeeze the baseline never had to consider.

An inactive profile still exists, so it presumably still counts against the six. A guardian who has cycled through six children's profiles over several years — each cancelled but preserved — has a full account and **no way to add a seventh child without deleting one of the six**. Deletion is the harsh action: it destroys progress and exam results (FR-FAM-10), and only snapshotted certificates survive.

So the guardian's only route to a new profile is to destroy an old child's learning history. That is a bad position to put a parent in, and it is a direct product of combining a hard cap with a preserve-forever inactive state.

Three ways out, none yet chosen: count only *active* profiles against the cap; raise the cap; or accept it and make the deletion consequence very explicit in the UI. Recorded in [OQ-08](../open-questions.md#resolved).
