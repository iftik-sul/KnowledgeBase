---
project: OstadLagbo
type: meeting-note
status: current
updated: 2026-08-28
owner: Iftikher
tags:
  - shagred-profile
  - decisions
---

# Discovery Note — Shagred Profile Decisions (2026-08-28)

Decisions made by the founder in the planning discussion of 2026-08-28, recorded here so they carry standing until the `shagred-profile` (SGP) requirements document is written. That requirements document supersedes this note when it exists.

## Decided

1. **A dedicated `shagred-profile` module exists** (declared in [project standards](/OstadLagbo/project-standards.md)). Shagred account creation remains in `registration-and-verification`; the profile itself is documented in SGP.
2. **Profile contents:**
   - Account basics: display name, profile photo (optional), date of birth (for 18+ enforcement only, never public), gender (optional). Verified phone and optional verified email exist on the account and are never shown publicly.
   - Coarse location only: District and Area. No map pin, no latitude/longitude. A Shagred's GPS is used live to center their own map view and is never stored.
   - Ostad history: an automatically derived record of Ostads whose offers connected with this Shagred (accepted offers, with dates). Not editable by the Shagred.
   - Statistics: joined date only.
3. **No learning-context / "about me" section.** Explicitly rejected by the founder.
4. **Ostad history is private.** Only the Shagred sees their own history. It is never visible to Ostads — not as a list, not as a count.
5. **Visibility rule:** a Shagred profile is never browsable, searchable, or shown on the map. It is visible to exactly one audience: an Ostad who has received that Shagred's offer, and only while the offer or the resulting relationship exists.
6. **No baseline revision.** The founder ruled these elaborations do not require an `mvp-scope-v1.1`; the baseline never enumerated Shagred profile fields.

## Not yet decided

- Whether a Shagred can hide or remove entries from their own private Ostad history view.
- What an Ostad sees of a Shagred profile after a relationship ends or an offer expires (current working assumption: visibility lapses).
