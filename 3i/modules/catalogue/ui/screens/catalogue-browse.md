---
project: 3i
module: catalogue
type: ui-spec
status: current
updated: 2026-08-26
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
- **Pagination — numbered, not infinite scroll.** Not specified anywhere in the eleven FR-CRS requirements; added here as a reasonable default, not confirmed with the client, matching how the Filter Panel's AND/OR combination logic is already flagged the same way in `components.md`. 24 results per page (matches the original design exploration's "Showing 24 of 140 courses" pattern). Numbered page controls, not "load more" — chosen for consistency with that same reference, and because numbered pages keep a specific result set linkable/shareable in the same way filter state already is (see Filter Panel's URL-persistence note).
- **The result count and pagination controls must both reflect the age-gated result set**, not the platform-wide total, whenever a learner profile is active — e.g. "52 courses" and page controls sized to 52 results, not 140, if the active profile's age band excludes 88 of them. Getting this wrong would leak the total catalogue size to someone whose actual browsable set is smaller, which is a minor but real information mismatch given how strict FR-CRS-10's filtering is meant to be everywhere else on this screen.

## The Age Gate (FR-CRS-10)

**No learner profile active (public browsing, or a Member who hasn't entered a profile context):** every published course is shown, unfiltered by age. The age band still displays on each card — it's informational here, not a filter.

**A learner profile active:** the grid is hard-filtered to courses whose age range includes that learner's current age. This is not a sort weight and not a "recommended" signal — a course outside the range is **absent**, not deprioritised. No banner or message explains the absence; a filtered-out course simply isn't part of the result set, the same way an under-13 profile's catalogue silently excludes 18+ content rather than showing it greyed out with an explanation (consistent with how [validation-rules.md](../../../identity-and-access/ui/validation-rules.md) treats other guardian-relevant absences as absent-not-disabled).

**This silent profile-based gate is a completely different mechanism from the Filter Panel's own Age Band filter** (one of the seven FR-CRS-08 filters, user-toggled and visible). The two must never be visually conflated — the profile gate has no on-screen control of any kind, while the Age Band filter is an ordinary checkbox/pill a visitor can select or clear themselves. A mockup showing the age-gated result set should **not** show the Age Band filter pill in a checked state, since that would imply the gate works by pre-selecting a filter, which is not how it works and would mislead whoever builds this screen from the mockup.

## Role Variations

None structurally — Public and Member see the same screen, differing only in whether the age gate is engaged, per above.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04): filter panel layout, card grid direction, sort selector, and pagination controls all mirror.
