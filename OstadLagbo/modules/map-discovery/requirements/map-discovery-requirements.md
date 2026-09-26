---
project: OstadLagbo
module: map-discovery
type: requirements
status: current
updated: 2026-09-26
id: OL-MAP-REQ-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.2.md
owner: Iftikher
---

# Map Discovery — Requirements

Derived from MVP Scope Baseline v1.2 §3. Governs Ostad location capture, the discovery map, filtering and search, and guest access. Profile content is governed by `ostad-profile`; the fuzzy matcher is shared with OSP-04; contact actions by `contact-and-offers`; analytics obligations by ADM-12/14.

## MAP-01 Ostad location capture

During onboarding stage 4 (REG-09) and afterward from profile editing, an Ostad sets their location by device GPS or by dropping/dragging a manual pin. Stored: latitude, longitude. The capture screen must state plainly: **the pin is publicly visible to everyone at exact precision**, and the Ostad may place it anywhere they teach or wish to be found — a coaching center, shop, or landmark — rather than their residence (baseline §3 rider; risk R-04). After saving, the Ostad can open a **self-preview**: their pin and preview card exactly as the public sees them. Location edits publish immediately (location is not a key field per ADM-06) and move the public pin in real time.

**Acceptance:** the consent statement appears on every location-setting surface; a manual pin can be placed with GPS denied; the self-preview matches the public rendering.

## MAP-02 The discovery map

The map shows every approved, non-suspended, **non-paused (OSP-11)** Ostad as a pin at exact stored coordinates — **pins only; no list view exists in the MVP**. The view centers on the user's live GPS position when permitted, else on a default city center (engineering default: Dhaka), supports free pan and zoom anywhere in Bangladesh, and provides a **recenter-to-me button** whenever GPS is available. Tapping a pin opens a preview card — profile photo, display name, verified badge, headline, average rating and review count, distance from map center — and tapping the card opens the full public profile.

**Map attribution is permanently visible** on the map surface: `© OpenStreetMap contributors` together with whatever credit the chosen tile provider requires (CL-035). It is not dismissible, and no card, sheet, or overlay may cover it. This is a licence obligation, not a design preference.

**Acceptance:** pending, rejected, suspended, and paused Ostads never render a pin; recenter returns to live position in one tap; denied GPS still yields a fully usable map; the attribution is legible at every zoom level and behind every overlay.

## MAP-03 Guest browsing

The map, search, filters, and full public Ostad profiles are available **without an account**. The Privacy Policy and Terms of Service are reachable from the guest map screen without registration (REG-13). Any contact action — sending an offer, favoriting, or anything requiring identity — routes a guest to registration/login and returns them to the same screen afterward. Guest sessions are instrumented as their own segment (guest→registration conversion feeds ADM-13). Scraping resistance — viewport query caps, request rate limits — is an engineering default obligation accompanying guest access.

**Acceptance:** a fresh install reaches a browsable map with zero registration steps; both legal documents open for a guest; no guest path reaches offer composition; the guest→register→same-screen flow survives the round trip.

## MAP-04 Radius and empty states

A user-adjustable radius slider (proposed default 5 km, range 1–30 km) filters which Ostads render, measured from the current map center — not the user's position — so any area can be explored. The radius is **one more filter on the single discovery read** that draws the pins (CL-033), so clustering and the viewport cap apply to it as to any other filter. The active radius is visibly indicated. When radius + filters + search produce **zero results**, the map shows a clear empty state ("No Ostads here yet") with a one-tap **widen radius** action; the zero-result event is logged per MAP-11.

**Acceptance:** changing radius updates results without re-search; the empty state and widen action appear on every zero-result combination.

## MAP-05 Filters

Two filters, combinable with search and radius under AND semantics:

- **Category** — single-select from the admin-managed list (ADM-11), entered via the OSP-04 fuzzy typeahead; deactivated categories never appear.
- **Gender** — Any (default) / Male / Female, filtering on the Ostad's public gender field (OSP-01). Included deliberately for the family-comfort dynamics of the Bangladesh tutoring market. The stored value set is Male / Female / **Other** (CL-031); there is **no "Other" filter option** — an Ostad whose gender is `other` is returned only under "Any", never under a Male or Female filter.

**Acceptance:** each filter works alone and combined; clearing filters restores the unfiltered map.

## MAP-06 Keyword search

Keyword search matches **fixed category names — in English and via their Bangla aliases (ADM-11, CL-013) — and Ostads' free-text skill names, matched in whichever script they were entered** — never headlines, about text, or personal names. Matching uses the same fuzzy algorithm as OSP-04 per script, so "gitar" and "গিটার" both find Guitar-category Ostads, and misspelled skill names still hit. Search composes with radius and filters.

**Acceptance:** a term present only in an Ostad's about text yields no match; misspellings within edit-distance of a category, alias, or skill name do match; a Bangla-script query resolves to its aliased category.

## MAP-07 Shareable profile links

Every public Ostad profile has a **Share** action producing a deep link. Opening the link on a device with the app lands directly on that profile — including for guests, per MAP-03; without the app it resolves to the store listing (engineering default: deferred deep link so the profile still opens after install). A link to a paused profile opens it with the not-accepting notice per OSP-11. Share events are instrumented per MAP-11.

**Acceptance:** link → installed app → correct profile, as guest and as registered user; link → no app → store.

## MAP-08 Favorites

Any **Shagred** can favorite an Ostad from the preview card or profile (favourites are Shagred-only — CL-026), building a private **Favorites list** screen (name, photo, badge, rating, distance; tap-through to profile; unfavorite anywhere). Favorites are **strictly private**: the Ostad is never notified, and no count or indicator appears on any profile. Guests tapping favorite are routed to registration (MAP-03).

**Acceptance:** no API response or UI surface exposes who favorited an Ostad or how many did; the list survives logout/login.

## MAP-09 Result density and performance

At low zoom levels pins cluster with counts, expanding on zoom (engineering-standard clustering). Map data loads by viewport; the full Ostad table is never shipped to the client — performance and the technical half of scraping resistance.

## MAP-10 Privacy guarantees

No user's live position — Shagred or guest — is ever transmitted for storage; positioning is on-device only, per SGP-02. Only Ostads have stored coordinates, and only by their explicit act in MAP-01. Distance on preview cards is computed from map center. Favorites data belongs to the favoriting user alone.

**Acceptance:** network inspection during map use shows no user-position writes; the only coordinates in any API response belong to approved Ostads.

## MAP-11 Instrumentation obligations

This module emits the events ADM-12/13/14 require: map sessions (guest and registered separately), profile views from pins, searches and filter applications with result counts — **including zero and low-result events tagged with category/keyword, script, gender filter, and map area** — radius changes, share taps, share-link opens, and favorite adds/removes. These events exist from first release.

## Proposed technical defaults summary

Default center, radius default/range, cluster thresholds, rate limits, viewport caps, and deep-link mechanics are engineering defaults. **The map provider is a deliberately deferred decision carrying four recorded constraints (CL-035):**

- **Raster, not vector.** MapLibre — the renderer behind every vector basemap on mobile — cannot shape Bengali script, so Bangla place names render as broken, disconnected glyphs; Protomaps' own localization documentation lists Bengali under "no support", alongside Tamil, Telugu and Khmer. A Bangla-first product therefore ships **server-rendered raster tiles** (where the shaping happens on the provider's machine) or Google's own SDK, and **no vector basemap**. This rules out precisely the free options — OpenFreeMap, self-hosted Protomaps — whose price is what this constraint costs.
- **OpenStreetMap's public tiles are development-only.** Their usage policy forbids commercial products on community-funded servers, forbids any prefetching, and states plainly that "offline use is not permitted". Development use must send an app-identifying User-Agent rather than a library default. **They are never shipped.**
- **Cost posture (NFR-13) holds in development and changes at soft launch.** Free while building; then ≈ $20–30/month on a raster vendor, every credible free tier being non-commercial — or $0 on Google's mobile SDK, which costs `flutter_map` instead.
- **The choice is made in Slice 0, before any MAP screen exists** (OL-BLD-001), by rendering one launch-area viewport in each candidate — MapTiler, Stadia Maps, Google — and comparing Bangla label rendering and Dhaka data density directly. Deferred past that gate, the decision stops being a configuration line and becomes a rewrite of this module's screens.

Everything else — exact pins, the consent statement, guest access boundaries, pins-only presentation, the filter set, cross-script search scope, favorites privacy, and the no-stored-user-location rule — changes only with founder approval.
