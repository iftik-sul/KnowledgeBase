---
project: 3i
module: catalogue
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CAT-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - catalogue
---

# Screen: Catalogue Browse

Satisfies: FR-CRS-06, FR-CRS-07, FR-CRS-08, FR-CRS-09, FR-CRS-10

---

## Purpose

Search, filter, and browse published courses. The catalogue's front door.

## Access Gate

Public. Behaviour changes based on whether a learner profile is active in the session — see below — but no authentication is required to reach this screen at all.

## Contents

- Search bar (FR-CRS-07): title, summary, description, instructor name, fuzzy-matched.
- [Filter Panel](../components.md#filter-panel) (FR-CRS-08).
- Sort selector (FR-CRS-09): relevance, newest, most enrolled, highest rated, title A–Z.
- Grid of [Course Card](../components.md#course-card)s for matching, `published`-status courses only.

## The Age Gate (FR-CRS-10)

**No learner profile active (public browsing, or a Member who hasn't entered a profile context):** every published course is shown, unfiltered by age. The age band still displays on each card — it's informational here, not a filter.

**A learner profile active:** the grid is hard-filtered to courses whose age range includes that learner's current age. This is not a sort weight and not a "recommended" signal — a course outside the range is **absent**, not deprioritised. No banner or message explains the absence; a filtered-out course simply isn't part of the result set, the same way an under-13 profile's catalogue silently excludes 18+ content rather than showing it greyed out with an explanation (consistent with how [validation-rules.md](../../../identity-and-access/ui/validation-rules.md) treats other guardian-relevant absences as absent-not-disabled).

## Role Variations

None structurally — Public and Member see the same screen, differing only in whether the age gate is engaged, per above.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04): filter panel layout, card grid direction, and sort selector all mirror.