---
project: OstadLagbo
module: map-discovery
type: requirements
status: current
updated: 2026-08-29
id: OL-MAP-REQ-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.0.md
owner: Iftikher
---

# Map Discovery — Requirements

Derived from MVP Scope Baseline v1.0 §3, extended by founder decision (2026-08-29) with gender filtering, shareable profile links, and favorites. Governs Ostad location capture, the discovery map, filtering and search, and guest access. Profile content is governed by `ostad-profile`; the fuzzy matcher is shared with OSP-04; contact actions by `contact-and-offers`; analytics obligations by ADM-12/14.

## MAP-01 Ostad location capture

During onboarding stage 4 (REG-09) and afterward from profile editing, an Ostad sets their location by device GPS or by dropping/dragging a manual pin. Stored: latitude, longitude. The capture screen must state plainly: **the pin is publicly visible to everyone at exact precision**, and the Ostad may place it anywhere they teach or wish to be found — a coaching center, shop, or landmark — rather than their residence (baseline §3 rider; risk R-04). After saving, the Ostad can open a **self-preview**: their pin and preview card exactly as the public sees them. Location edits publish immediately (location is not a key field per ADM-06) and move the public pin in real time.

**Acceptance:** the consent statement appears on every location-setting surface; a manual pin can be placed with GPS denied; the self-preview matches the public rendering.

## MAP-02 The discovery map

The map shows every approved, non-suspended Ostad as a pin at exact stored coordinates — **pins only; no list view exists in the MVP**. The view centers on the user's live GPS position when permitted, else on a default city center (engineering default: Dhaka), supports free pan and zoom anywhere in Bangladesh, and provides a **recenter-to-me button** whenever GPS is available. Tapping a pin opens a preview card — profile photo, display name, verified badge, headline, average rating and review count, distance from map center — and tapping the card opens the full public profile.

**Acceptance:** pending, rejected, and suspended Ostads never render a pin; recenter returns to live position in one tap; denied GPS still yields a fully usable map.

## MAP-03 Guest browsing

The map, search, filters, and full public Ostad profiles are available **without an account**. Any contact action — sending an offer, favoriting, or anything requiring identity — routes a guest to registration/login and returns them to the same screen afterward. Guest sessions are instrumented as their own segment (guest→registration conversion feeds ADM-13). Scraping resistance — viewport query caps, request rate limits — is an engineering default obligation accompanying guest access.

**Acceptance:** a fresh install reaches a browsable map with zero registration steps; no guest path reaches offer composition; the guest→register→same-screen flow survives the round trip.

## MAP-04 Radius and empty states

A user-adjustable radius slider (proposed default 5 km, range 1–30 km) filters which Ostads render, measured from the current map center — not the user's position — so any area can be explored. The active radius is visibly indicated. When radius + filters + search produce **zero results**, the map shows a clear empty state ("No Ostads here yet") with a one-tap **widen radius** action; the zero-result event is logged per MAP-11.

**Acceptance:** changing radius updates results without re-search; the empty state and widen action appear on every zero-result combination.

## MAP-05 Filters

Two filters, combinable with search and radius under AND semantics:

- **Category** — single-select from the admin-managed list (ADM-11), entered via the OSP-04 fuzzy typeahead; deactivated categories never appear.
- **Gender** — Any (default) / Male / Female, filtering on the Ostad's public gender field (OSP-01). Included deliberately for the family-comfort dynamics of the Bangladesh tutoring market.

**Acceptance:** each filter works alone and combined; clearing filters restores the unfiltered map.

## MAP-06 Keyword search

Keyword search matches **fixed category names and Ostads' free-text skill names only** — never headlines, about text, or personal names. Matching uses the same fuzzy algorithm as OSP-04, so "gitar" finds Guitar-category Ostads and misspelled skill names still hit. Search composes with radius and filters.

**Acceptance:** a term present only in an Ostad's about text yields no match; misspellings within edit-distance of a category or skill name do match.

## MAP-07 Shareable profile links

Every public Ostad profile has a **Share** action producing a deep link. Opening the link on a device with the app lands directly on that profile — including for guests, per MAP-03; without the app it resolves to the store listing (engineering default: deferred deep link so the profile still opens after install). Share events are instrumented per MAP-11.

**Acceptance:** link → installed app → correct profile, as guest and as registered user; link → no app → store.

## MAP-08 Favorites

Any registered user can favorite an Ostad from the preview card or profile, building a private **Favorites list** screen (name, photo, badge, rating, distance; tap-through to profile; unfavorite anywhere). Favorites are **strictly private**: the Ostad is never notified, and no count or indicator appears on any profile. Guests tapping favorite are routed to registration (MAP-03).

**Acceptance:** no API response or UI surface exposes who favorited an Ostad or how many did; the list survives logout/login.

## MAP-09 Result density and performance

At low zoom levels pins cluster with counts, expanding on zoom (engineering-standard clustering). Map data loads by viewport; the full Ostad table is never shipped to the client — performance and the technical half of scraping resistance.

## MAP-10 Privacy guarantees

No user's live position — Shagred or guest — is ever transmitted for storage; positioning is on-device only, per SGP-02. Only Ostads have stored coordinates, and only by their explicit act in MAP-01. Distance on preview cards is computed from map center. Favorites data belongs to the favoriting user alone.

**Acceptance:** network inspection during map use shows no user-position writes; the only coordinates in any API response belong to approved Ostads.

## MAP-11 Instrumentation obligations

This module emits the events ADM-12/13/14 require: map sessions (guest and registered separately), profile views from pins, searches and filter applications with result counts — **including zero and low-result events tagged with category/keyword, gender filter, and map area** — radius changes, share taps, share-link opens, and favorite adds/removes. These events exist from first release.

## Proposed technical defaults summary

Default center, radius default/range, cluster thresholds, rate limits, viewport caps, deep-link mechanics, and the map provider are engineering defaults — with one recorded constraint: provider choice must respect the bootstrap cost posture (free or free-tier-viable at MVP scale; e.g., OpenStreetMap-based rendering avoids per-load billing). Everything else — exact pins, the consent statement, guest access boundaries, pins-only presentation, the filter set, search scope, favorites privacy, and the no-stored-user-location rule — changes only with founder approval.
