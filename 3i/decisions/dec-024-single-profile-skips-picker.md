---
project: 3i
type: decision
status: current
updated: 2026-08-23
id: 3I-DEC-024
tags: [decision, identity, ux]
---

# A Member With Exactly One Profile Skips the Profile Picker's Tile Selection

## Context

[Login](../modules/identity-and-access/ui/screens/login.md) and [Profile Picker](../modules/identity-and-access/ui/screens/profile-picker.md) both carried the same unresolved note: a Member with exactly one profile (themself, if they study, or their sole child) might reasonably skip the picker screen entirely, since there is nothing to pick between. Flagged in both files as "not specified in the baseline; a reasonable default, confirm with client" — never actually confirmed, and no decision recorded it.

FR-FAM-04 requires the picker to exist for accounts with multiple profiles. It says nothing about the single-profile case, so this is genuinely undecided rather than baseline-contradicting.

## Decision

Taken 2026-08-23: **a Member whose account has exactly one profile — active or never-activated — skips the picker's tile-selection step** and is taken directly to that profile's [PIN Pad](../modules/identity-and-access/ui/components.md#pin-pad) after login.

This changes only which screen appears first. It does **not** change anything about the PIN itself — [3I-DEC-018](dec-018-profile-pin-mandatory-guardian-controlled.md)'s mandatory, guardian-controlled PIN still applies, including to the Member's own profile if they study. A Member is never signed straight into a study context without entering the PIN.

The never-activated-profile-with-no-seat redirect to seat purchase, described in [Profile Picker](../modules/identity-and-access/ui/screens/profile-picker.md), still applies identically in the single-profile case — it simply triggers on login rather than on a tile tap.

## Reasoning

The picker's only job is letting a Member choose between profiles. With one profile there is no choice to make, so showing it anyway is a tap that teaches nothing and confirms nothing — the PIN entry that follows is where the actual security check happens, and that step is preserved unchanged. This is the same reasoning that already governs the picker's tile filtering (active and never-activated only): the picker exists to serve a real decision, not to exist for its own sake.

## Scope

UX interpretation, not a baseline scope change — FR-FAM-04 is silent on the single-profile case, so nothing is being reversed or amended. No client sign-off required beyond the existing operating assumption that Saitama holds decision authority for this class of call.

## Consequences

- [Login](../modules/identity-and-access/ui/screens/login.md) and [Profile Picker](../modules/identity-and-access/ui/screens/profile-picker.md) are now fully specified on this point — no remaining inline hedge in either file.
- Implementation note for `backend-spec.md` / the frontend routing layer: the post-login redirect logic needs a profile-count check (1 vs. many), not just an authentication check.

## Cost

None. Removes a screen from the common case rather than adding one.