---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-IDA-UI-019
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - dashboard
figma: null
---

# Screen: Learner Dashboard

Not directly required by any single FR — a navigation gap-fill per [3I-DEC-036](/3i/decisions/dec-036-learner-dashboard.md), same category as [Account Settings](account-settings.md) and [Account Menu](../components.md#account-menu) before it.

---

## Purpose

The screen a learner profile lands on immediately after successful PIN entry — the "study context" [Profile Picker](profile-picker.md) and [Login](login.md) both reference but never previously defined. The profile-level counterpart to [Guardian Dashboard](guardian-dashboard.md): Guardian Dashboard manages every profile from the Member's account-level view; this screen is what one specific profile sees once inside its own session.

## Access Gate

A specific learner profile must be active in the session — reached only via successful PIN entry on [Profile Picker](profile-picker.md), or the single-profile skip on [Login](login.md) ([3I-DEC-026](/3i/decisions/dec-026-single-profile-skips-picker.md)). Never reached directly.

## Contents

- **Continue Learning** — in-progress courses with materials, each linking to [Course Materials List](/3i/modules/materials/ui/screens/course-materials-list.md).
- **Enrolled Courses** — the full list of courses this profile is enrolled in, Regular and Online Class alike. For an Online-Class enrolment specifically, this is the natural landing area, though the actual schedule/session-join detail screen this would ideally link to does not exist yet anywhere in the platform — a related, still-open gap (see [3I-DEC-036](/3i/decisions/dec-036-learner-dashboard.md)'s consequences), not resolved by this screen alone.
- **Wishlist** — this profile's saved courses, via [Course Card](/3i/modules/catalogue/ui/components.md#wishlist-toggle)'s wishlist toggle. Scoped per profile, matching the Course Card's own Enrolled-indicator scoping — the two indicators and this screen's Wishlist section are deliberately consistent about which "account level" they operate at.
- **Certificates** — this profile's own certificates. Distinct from the same certificates shown on [Guardian Dashboard](guardian-dashboard.md), which is the guardian's view of the same data, not a duplicate screen.

## Behaviour

Every profile lands here after PIN entry, regardless of age band — this is the universal per-profile landing point, not varied by age. Content sections may be empty (no enrolled courses yet, no wishlist items yet) without any of this screen's sections requiring dedicated empty-state design beyond what [design-system.md §9](/3i/design-system.md#9-known-gaps--not-yet-designed) already flags as a general open item.

## Role Variations

None — profile-level screen, not role-gated beyond the access gate above.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
