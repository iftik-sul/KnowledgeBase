---
project: 3i
module: catalogue
type: overview
status: current
updated: 2026-08-23
id: 3I-CAT-OVW-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - module
  - overview
---

# Catalogue

The module that turns an instructor's course into something a learner can find, filter to their own age, and rate after taking it.

**Module status: complete.** README, data model, requirements, and the full UI stage are written.

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| CRS | Course catalogue and management | 11 |

**Correction against project-standards.md:** that document's module table lists CRS at 12 FRs. Counting FR-CRS-01 through FR-CRS-11 directly against §8.2 of the baseline gives 11. Flagged here rather than silently followed either way — project-standards.md should be corrected to 11 in a small follow-up edit.

No decisions existed against CRS before this module was scaffolded. One new decision accompanies it: [3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md) (guardian submits ratings/reviews for under-13 profiles).

## Course Types

| Type | Structure |
| :---- | :---- |
| **Regular** | Self-paced materials only. No batches |
| **Online Class** | Live sessions only, delivered in batches |
| **Mixed** | Materials plus live batch sessions |

This module owns the **Course** record itself — its metadata, age tagging, publication state, search, and filtering. It does **not** own the materials attached to a course (`materials`, not yet built) or the batches scheduling its live sessions (`learning-delivery`, not yet built). A course can exist and be catalogued before either of those modules is built against it; the publish gate (FR-CRS-03) is the one place this module has to ask a question of a module that doesn't exist yet — see [data-model.md](data-model.md#forward-references) for how that's handled.

## The Age Gate

**FR-CRS-10 is the module's safeguarding-relevant core requirement:** when a learner profile is active, the catalogue shows only courses whose age range includes that learner's age. This is the same age-band system already defined for learner profiles in `identity-and-access` — [Age Band Badge](/3i/modules/identity-and-access/ui/components.md#age-band-badge) — reused here rather than redefined, since a course's age range and a learner's age band need to compare against the same six bands (FR-CRS-06) to mean anything.

A course's age range is two fields — `minimumAge` (mandatory, no default, FR-CRS-02) and `maximumAge` (optional) — not a single band value. The **band shown on a course card** is derived from `minimumAge` for a compact display; the **full range** is shown on the course detail page. See [data-model.md](data-model.md#course).

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-CAT-DM-001 | current |
| [requirements/crs-course-catalogue-and-management.md](requirements/crs-course-catalogue-and-management.md) | 3I-CAT-REQ-001 | current |
| [ui/README.md](ui/README.md) | 3I-CAT-UI-000 | current — 6 screens, matrix, components, validation rules |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| Age bands and their derivation from date of birth | [Age Band Badge](/3i/modules/identity-and-access/ui/components.md#age-band-badge), FR-CRS-06 |
| Guardian-on-behalf attribution pattern | [3I-DEC-020](/3i/decisions/dec-020-guardian-on-behalf-chat-retained.md), extended here by [3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md) |
| Every account is 18+; every minor is a guardian profile | [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) |

## Delivery

Phase 3, Catalogue (§21.1) — courses, materials, Bunny integration, catalogue, age filtering. The baseline's phase table groups `catalogue` and `materials` into one delivery phase even though they are separate modules in this repository's partition — see [project-standards.md](/3i/project-standards.md#modules) for why the split exists.

## Open Against This Module

| Item | Note |
| :---- | :---- |
| Course `level` field has no defined value set in the baseline | Defaulted to Beginner / Intermediate / Advanced — a reasonable placeholder, not confirmed with the client |
| Course `language` field — unclear whether limited to the platform's 5 UI locales | Modelled as free text for now, since a course could reasonably be taught in a language the platform UI doesn't otherwise support (e.g. Qur'anic Arabic recitation delivered to an English-locale account). Flagged, not decided |
| Category taxonomy | Simple flat, admin-managed list — confirmed direction, no fixed values yet |
| `instructorId` on Course | Forward-references the `instructors` module (INST), not yet built. See [data-model.md](data-model.md#forward-references) |
| Publish gate's material/batch check | Forward-references `materials` and `learning-delivery`, neither yet built. See [data-model.md](data-model.md#forward-references) |

None of the above block this module's own specification — they are dependencies on modules still to come, flagged plainly rather than assumed silently, per the same treatment `commerce` gave its dependency on `identity-and-access`.

## Change Requests Owed to the Client

None. [3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md) is a safeguarding/UX interpretation of a baseline silence, not a scope change — same treatment as [3I-DEC-020](/3i/decisions/dec-020-guardian-on-behalf-chat-retained.md).