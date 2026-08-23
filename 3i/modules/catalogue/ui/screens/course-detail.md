---
project: 3i
module: catalogue
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CAT-UI-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - catalogue
---

# Screen: Course Detail

Satisfies: FR-CRS-01, FR-CRS-06, FR-CRS-11

---

## Purpose

Full course information — the page a learner reads before enrolling, and the page a public visitor reads before creating an account.

## Access Gate

Public, for any `published` course. A `draft`, `pending_review`, `suspended`, or `taken_down` course returns a not-found response to anyone other than its owning instructor or an admin — same treatment as any other absent-not-disabled content on this platform.

## Contents

- Title, summary, description, learning outcomes, category, type, level, language (FR-CRS-01).
- **Full numeric age range** (`minimumAge`–`maximumAge`), not just the band — the one place on the platform this precision is shown, since [Course Card](../components.md#course-card) only shows the band.
- Instructor name and bio (forward-referenced to `instructors`; shows a placeholder until that module exists).
- Average rating and the list of `visible`-status Reviews, each showing the reviewer's display name — self-submitted reviews show the learner's own name; guardian-submitted reviews show the guardian-attribution format per [3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md).
- Enrolment call-to-action — the actual enrolment flow lives in `learning-delivery` (not yet built); this screen links out to it rather than duplicating it.

## Role Variations

None for viewing — identical for Public and Member. An enrolled Member additionally sees a **Rate \& review** entry point once their enrolment qualifies (see [Rate \& Review](rate-and-review.md)); a non-enrolled visitor does not see that entry point at all, rather than seeing it disabled.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).