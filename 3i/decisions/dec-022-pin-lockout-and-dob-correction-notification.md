---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-022
tags: [decision, identity, safeguarding]
---

# PIN Lockout Matches FR-AUTH-09 Exactly; DOB Corrections That Change Chat Eligibility Notify the Guardian

## Context

Two gaps remained open against `identity-and-access` after the module was otherwise complete.

**PIN lockout.** [3I-DEC-018](dec-018-profile-pin-mandatory-guardian-controlled.md) made the profile PIN mandatory. A 4-digit PIN is ten thousand combinations — trivially brute-forced by a sibling on a shared device without a lockout. FR-AUTH-09 already defines a pattern for password attempts; nothing required the picker to use it.

**DOB correction notification.** [Admin — DOB Correction](../modules/identity-and-access/ui/screens/admin-dob-correction.md) is the one surface where a value every other screen treats as immutable can actually change. A correction can silently alter chat eligibility (FR-FAM-08), catalogue visibility (FR-CRS-10), and enrolment eligibility (FR-ENR-03) at once. Whether the guardian should be told was a judgement call written into the spec, not yet a decision.

## Decision

Taken 2026-08-18:

1. **PIN attempts follow FR-AUTH-09 exactly:** five failed attempts trigger a 15-minute lockout, with progressive delay and per-IP rate limiting — the same shape, not merely a similar one.
2. **A guardian is notified whenever an admin DOB correction changes a profile's chat eligibility.** Not for corrections that leave eligibility unchanged (e.g. an under-13 correction that stays under 13). The notification follows the standard channel rules in FR-NOT-01–08: push and email, routed to the account holder, the profile named in the body.

## Reasoning

**On (1):** reusing FR-AUTH-09 rather than inventing a separate pattern keeps the two lockout mechanisms behaviourally identical, which matters for both implementation consistency and for anyone auditing the two later — two different lockout shapes for two credential-adjacent controls invites divergence over time for no reason.

**On (2):** a DOB correction that flips chat eligibility is a real, consequential change to a child's exposure, and it currently happens with no visible trace to the person responsible for that child. Silence here is the failure mode the age-and-safeguarding rules exist to prevent everywhere else — a stored value changing a safeguarding boundary without the guardian knowing.

## Scope

Neither is in the baseline as written. (1) is a natural extension of FR-AUTH-09's existing pattern rather than new policy, and is unlikely to need separate client sign-off. (2) adds a new notification trigger to FR-NOT-01's list and should be named explicitly in any change request alongside the other identity-and-access items, since it is new behaviour rather than an interpretation.

## Consequences

- [Profile picker](../modules/identity-and-access/ui/screens/profile-picker.md) is now fully specified — no remaining gap.
- [Admin — DOB Correction](../modules/identity-and-access/ui/screens/admin-dob-correction.md) gains a concrete behaviour rather than a "should be visible" note.
- FR-NOT-02's in-app notification centre should surface this event distinctly from routine progress notifications, given its safeguarding weight.

## Cost

None significant. Both reuse existing patterns rather than introducing new mechanisms.
