---
project: 3i
module: catalogue
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-CAT-UI-COMP
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - components
---

# Catalogue — Shared Components

Documented once here. Screens link to this file rather than restating.

---

## Course Card

Used on: [Catalogue browse](screens/catalogue-browse.md), and anywhere else in the platform a course is listed compactly (a `reporting` or `learning-delivery` screen may reuse this rather than inventing a second card).

Shows: thumbnail, title, [Age Band Badge](/3i/modules/identity-and-access/ui/components.md#age-band-badge) (derived from `minimumAge`, per [data-model.md](../data-model.md#course)), category, type badge (Regular / Online Class / Mixed), instructor name (read from `instructors`' `InstructorProfile`), and average rating from visible Reviews.

**A card never shows the full age range**, only the band — the full `minimumAge`–`maximumAge` range is a [Course Detail](screens/course-detail.md)-only disclosure, since a card's job is quick scanning, not precision.

### Enrolled Indicator

Not specified in the eleven FR-CRS requirements; added here as a reasonable default, not confirmed with the client. When the viewer is enrolled in the course, a second small badge — "ENROLLED," `green-600` fill, `navy-900` text — sits beside the type badge, same shape and weight, read as a matched pair.

**Deliberately simple: no progress bar, no percentage.** An earlier version of this card carried a progress indicator; it was removed in favour of a plain tag, on the direct instruction that the card stay simple. Do not reintroduce a progress element here without a new, explicit decision to do so.

**Scoped to the currently active learner profile, not the Member's account as a whole.** This matches how [Catalogue Browse](screens/catalogue-browse.md)'s own age gate is scoped (FR-CRS-10, active-profile-dependent), rather than the Member-level "any of my profiles" check [Course Detail](screens/course-detail.md) and [Rate \& Review](screens/rate-and-review.md) use — a compact grid of cards has no good way to show "enrolled, but only for one of your three children" at a glance, so the card answers a narrower, single-profile question instead.

### Wishlist Toggle

Not specified in the eleven FR-CRS requirements; added here as a new feature, not yet fully specified. A circular icon button overlaid on the top-right corner of the card's thumbnail image: an outline heart when not wishlisted, a filled `error-500` heart when wishlisted — see [design-system.md §1](/3i/design-system.md#semantic) for why this token, ordinarily reserved for error icons/borders, is deliberately reused here rather than introducing a new red.

**Available to both active and inactive subscribers** — a Member's wishlist is not gated on holding a currently-paid seat. **Present on every card regardless of enrollment state**, including already-enrolled courses, for now — whether wishlisting an already-enrolled course is meaningful, and whether the heart should hide once enrolled, is unresolved.

**Genuinely open, not yet decided:**
- Whether wishlisting requires any authenticated session at all, or is available to a fully public, unregistered visitor (in which case it would need to persist somewhere before an account exists).
- Whether a wishlist is scoped per learner profile (like the Enrolled indicator above) or per Member account.
- Where a saved wishlist is actually viewed — a dedicated "My Wishlist" screen does not exist yet anywhere in this module's screen list.

None of this blocks the component's visual design, which is confirmed — it blocks writing the actual behavior into this document with confidence, and should be resolved before [Catalogue Browse](screens/catalogue-browse.md) or any other screen documents wishlist *behavior*, not just the toggle's appearance.

## Filter Panel

Used on: [Catalogue browse](screens/catalogue-browse.md).

FR-CRS-08's seven filters: category, course type, level, age band, minimum rating, language, has upcoming batch — all live, checking directly against `learning-delivery`'s `Batch` data. Filters combine with **AND** logic; multiple selections within one filter (e.g. two categories) combine with **OR** — not specified in the baseline, a reasonable default matching common catalogue-filter conventions, not confirmed with the client.

**Filter state persists in the URL** (query parameters), not only in client state, so a filtered view is shareable and survives a page refresh — standard practice, not a baseline-specific requirement.
