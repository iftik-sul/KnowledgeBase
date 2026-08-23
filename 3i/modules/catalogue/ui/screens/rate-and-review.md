---
project: 3i
module: catalogue
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CAT-UI-006
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - catalogue
  - safeguarding
---

# Screen: Rate & Review

Satisfies: FR-CRS-11

---

## Purpose

Submit a 1–5 rating and optional written review for a course, once per enrolled learner profile.

## Access Gate

Member only, and only reachable for a profile with a qualifying enrolment on this course (forward-referenced to `learning-delivery`, not yet built — until it exists, this entry point cannot actually be gated and should be treated as **absent**, fail-closed, per [validation-rules.md](../validation-rules.md#publish-gate)'s same fail-closed principle). Not reachable a second time for a profile that has already reviewed this course — the entry point becomes "edit your review" instead, not a second submission form.

## Fields

- **Which profile** this review is for — required select, from the Member's profiles with a qualifying enrolment on this course. For an account with only one such profile, this step is skipped and the profile is implicit, the same UX principle as [3I-DEC-026](/3i/decisions/dec-026-single-profile-skips-picker.md)'s single-profile skip, applied here rather than restated as a new decision.
- **Rating** — 1–5, required.
- **Review text** — optional, free text.

## Behaviour

**If the selected profile is under 13**, the form's framing shifts to make the authorship explicit — e.g. a label reading "Submitting as [Guardian name] on behalf of [Learner name]" — rather than presenting the form identically and only changing the stored attribution silently. The Member should see, at the point of submission, that this is exactly the same guardian-on-behalf pattern already familiar from chat ([3I-DEC-020](/3i/decisions/dec-020-guardian-on-behalf-chat-retained.md), [3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md)), not a new or different mechanism.

**If the selected profile is 13 or older**, the review is submitted and displayed under that profile's own display name directly — no guardian framing.

On submission, the review is immediately `visible` — no pending-moderation state before publication (admin's hide action, FR-CRS-11, is a post-hoc moderation tool, not a pre-publication gate).

## Role Variations

Member only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).