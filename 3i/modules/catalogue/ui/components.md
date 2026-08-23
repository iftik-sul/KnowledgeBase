---
project: 3i
module: catalogue
type: ui-spec
status: current
updated: 2026-08-23
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

Used on: [Catalogue browse](screens/catalogue-browse.md), and anywhere else in the platform a course is listed compactly (e.g. a future `reporting` or `learning-delivery` screen may reuse this rather than inventing a second card).

Shows: thumbnail, title, [Age Band Badge](/3i/modules/identity-and-access/ui/components.md#age-band-badge) (derived from `minimumAge`, per [data-model.md](../data-model.md#course)), category, type badge (Regular / Online Class / Mixed), instructor name (forward-referenced, shows a placeholder until `instructors` exists), and average rating from visible Reviews.

**A card never shows the full age range**, only the band — the full `minimumAge`–`maximumAge` range is a [Course Detail](screens/course-detail.md)-only disclosure, since a card's job is quick scanning, not precision.

## Filter Panel

Used on: [Catalogue browse](screens/catalogue-browse.md).

FR-CRS-08's seven filters: category, course type, level, age band, minimum rating, language, has upcoming batch. The last one is inert (shown but produces no results change) until `learning-delivery` exists — see [ui/README.md](README.md#blocked). Filters combine with **AND** logic; multiple selections within one filter (e.g. two categories) combine with **OR** — not specified in the baseline, a reasonable default matching common catalogue-filter conventions, not confirmed with the client.

**Filter state persists in the URL** (query parameters), not only in client state, so a filtered view is shareable and survives a page refresh — standard practice, not a baseline-specific requirement.