---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-009
tags: [decision, billing, enrolment, scope-change]
supersedes: N/A — first current version; superseded a draft of the same file
---

# A Seat Is a Permanent, Non-Transferable Grant to One Profile

## Context

One seat is included in the subscription; additional seats carry a per-seat monthly charge (§14.1). Seat count is a Stripe quantity (FR-BILL-04). The baseline left two things unstated: whether a seat is consumed by enrolling a learner or by concurrent viewing, and whether it can move between profiles.

Two conflicting requirements pointed at different readings. FR-ENR-01 requires an available seat *for that learner* to enrol, which implies enrolling spends a seat. FR-AUTH-12 caps concurrent video streams by seats purchased, which implies watching spends a seat. Both cannot be independently true.

## Decision

Settled in review, 2026-08-18, across several rounds:

1. **A seat is an enrolment grant, not a viewing slot.** One seat purchased makes exactly one profile active — able to enrol and study. FR-AUTH-12's concurrency cap is a *consequence* of this, not a separate mechanism: a profile with no seat cannot enrol, so it cannot stream either. With two seats, at most two profiles can ever be active, so at most two can ever be streaming simultaneously — the cap is automatically satisfied and needs no independent enforcement.

2. **A seat is permanently bound to the profile it activates.** It is never reassigned or switched to a different profile while both exist. If a guardian wants a different child studying under the same money, the running seat is cancelled and a new one is purchased for the other profile.

3. **Cancelling a seat deactivates the profile; it does not delete it.** The profile becomes inactive — unenrolled, unable to study — but its history (progress, certificates, exam results) is fully preserved, same protection FR-FAM-10 already gives on deletion, without deletion occurring.

4. **An inactive profile can be reactivated later** by purchasing a new seat for it. This is a genuine second payment, not a toggle — there is no free trial anywhere in the baseline (§14.1), so reactivation always costs money. That absence of a free tier is what keeps this safe from abuse: there is no incentive to cycle seats across profiles, because every activation is paid regardless.

5. **The account holder's subscription flow is: create account (free) → create profile (free, unlimited) → activate a specific profile by paying for a seat → optionally cancel (deactivate, preserve history) → optionally reactivate (pay again).** Profile creation carries no charge and touches no seat; only activation and cancellation are billing events.

6. **The six-profile cap in FR-FAM-02 is removed.** Since a seat is what makes a profile capable of studying, and profiles are now free and unlimited to create, there is no reason to cap the *number of profiles that can exist* — only the number that can be simultaneously active is billed and therefore self-limiting.

## Scope

**Item 6 is a genuine scope change against SRD v2.0** and requires a change request under §21.3. FR-FAM-02 is explicit — "Maximum 6 learner profiles per account" — and several other parts of the baseline implicitly assume a small, bounded family: the guardian dashboard (FR-FAM-09), course-card age filtering, and the profile picker (FR-FAM-04) were all specified against a family of up to six, not an account that could accumulate an unbounded number of inactive profiles over years.

## Consequences

- **A new profile state exists that the baseline does not describe.** Currently FR-FAM only distinguishes an active profile from a deleted one (FR-FAM-10). This decision introduces a third: inactive-but-preserved. The guardian dashboard needs to represent this distinctly from both, and any UI or data-model document for the FAM area must specify it explicitly rather than inheriting the two-state assumption from the baseline text.
- **FR-FAM-06's 2-changes-per-30-days rate limit now applies to activation and cancellation, not to profile creation.** Creating a profile is free and untracked against this limit; only the paid, seat-consequential actions are throttled. This is a redefinition of what FR-FAM-06 counts as a "change" and should be stated explicitly wherever that requirement is implemented, since the baseline's own wording ("profile creation and deletion") no longer matches what is actually rate-limited.
- **FR-AUTH-12 is satisfied automatically** and should not be implemented as an independent concurrency check. Documenting it as a consequence of the seat model, not a second control, avoids a redundant and possibly conflicting enforcement path being built later.
- Ageing up at 13 ([3I-DEC-008](dec-008-ageing-up-at-13.md)) now has a concrete mechanism: the guardian cancels the 13-year-old's seat on the family account, freeing budget, while the teenager's own standalone account is activated separately. The profile's history stays attached to the (now inactive) family profile, snapshotted certificates remain valid per [3I-DEC-005](dec-005-denormalised-certificates.md).

## Cost

An account can now hold an unbounded number of inactive profiles — every child ever considered, every seat ever cancelled, sitting in history forever with no cap. This is accepted as the trade-off for removing the six-profile limit; if it becomes an operational problem (support load, storage, guardian dashboard clutter), the fix is a cap on *created* profiles specifically, separate from the seat mechanism, and would be a new decision rather than a reversal of this one.
