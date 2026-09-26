---
project: OstadLagbo
module: map-discovery
type: api
status: current
updated: 2026-09-25
id: OL-MAP-API-001
derived_from: /OstadLagbo/modules/map-discovery/requirements/map-discovery-requirements.md
owner: Iftikher
---

# Map Discovery — API

Endpoints for setting an Ostad's pin, browsing the map, filtering and searching, favorites, and share links. Conventions per [API Overview](/OstadLagbo/api-overview.md); query patterns and privacy rules per [MAP Data Model](/OstadLagbo/modules/map-discovery/data-model/map-discovery-data-model.md). This module owns almost no data — one entity, `favorite` — but it defines the platform's two hardest reads (spatial and fuzzy) and its strictest privacy rule: **no viewer's location is ever stored or logged.**

## The one rule that shapes every endpoint

Coordinates travel **into** the API only as ephemeral query parameters and only **out** of it for approved Ostads. A viewer's position is never a stored field, never an analytics property, and never a log line (MAP-10, NFR-06; Data Model Overview rule 4). The consequences, applied throughout:

- Discovery reads take a **map centre and bounds** the client chose — which may equal the device's GPS on first open, but the API cannot tell and does not care. It answers the query and forgets the centre.
- The API layer and Cloudflare are configured to **scrub coordinate parameters from request logs** (ADR-001 open item 5). This is infrastructure, not per-endpoint code, but it is a precondition of these endpoints being safe.
- Zero-result analytics carry a **coarsened area** (thana or grid cell), never the exact centre (MAP-DM query 7) — and, per the API Overview, they are **client-emitted to `POST /v1/events`**, where the server strips disallowed properties and coarsens; the discovery reads themselves emit nothing.

## Endpoints — the Ostad's pin (MAP-01)

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `PUT /v1/profile/location` | The Ostad themself, `active` (which includes setting the pin during onboarding stage 4, REG-09). A suspended Ostad is refused by the global restricted-session rule (API Overview); a Shagred by role | `{ lat, lng }` — set by device GPS or a manual drag; the client shows the public-pin consent statement (a UI obligation, MAP-01) | `{ lat, lng }` — written straight to `ostad_profile` (not a key field, so it publishes immediately, OSP-10) | `validation_failed` (coordinates outside Bangladesh's bounds — an engineering-default sanity box, not a precision claim); `forbidden` (Shagred) |
| `GET /v1/profile/location/preview` | The Ostad themself | — | The Ostad's **own** discovery projection and pin exactly as the public sees it (MAP-01 self-preview) — served **regardless of discoverability**, so a pending, paused, or unapproved Ostad can check their pin first. Here alone `verified` reflects the Ostad's real `approval_status` (it is `false` while pending), because this is the one projection a non-approved Ostad ever receives | `forbidden` (Shagred) |

This pin is stage 4 of onboarding (`PUT /v1/onboarding/stages/4` in the REG wizard delegates here) and is editable any time after.

## Endpoints — discovery

Both discovery reads share one response element, the **map pin projection** (MAP-DM's narrow projection — never the full profile row, MAP-09):

```
{ id, display_name, photo_url (signed), lat, lng,
  rating_avg | null, rating_count, headline, verified: true,
  distance_km? }        // present only on the radius read, computed from the query centre
```

`verified` is always true here because only approved Ostads appear (the discoverability predicate, OSP-DM). "New" is **not** a field — the client renders it when `rating_count == 0` (MAP-DM). Tapping a pin opens the full public profile through `GET /v1/ostads/{id}` (OSP api), which is itself guest-readable and which records the profile view (server-side, MAP-11).

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `GET /v1/discovery/map` | **Anyone, incl. guests** (MAP-03). Returns only Ostads satisfying the discoverability predicate (OSP-DM) with no block against the viewer. Per-IP viewport rate limit (MAP-09) | `?bounds=<sw_lat,sw_lng,ne_lat,ne_lng>&zoom=&category=<category_id>&gender=&q=&centre=<lat,lng>&radius_km=` | **The single discovery read — it draws every pin on the map** (CL-033). At high zoom: pins (the projection) inside `bounds`. **At low zoom or above the viewport cap: aggregated `clusters[]` of `{ lat, lng, count }` only — no individual pins** (MAP-09, scraping resistance). `centre` + `radius_km` are the **radius slider**, applied as one more AND filter alongside category/gender/`q` (MAP-04/05/06) — the viewport cap and clustering apply to it exactly as to any other filter, so no request can ever enumerate more Ostads than the cap. No `distance_km` — the client computes distance from its own map centre on-device (MAP-02, mirroring the favorites-distance rule) | `validation_failed` (malformed bounds; radius outside 1–30 km); `rate_limited` |

**Filter and search parameters** (compose with the spatial read under AND semantics, MAP-05/06):

- `category` — a single `category_id` the user selected from the admin-managed list via the OSP-04 typeahead (MAP-05); deactivated categories are never offered as inputs.
- `gender` — `any` (default) / `male` / `female`, on the Ostad's public gender field (MAP-05).
- `q` — the **cross-script fuzzy keyword** (≥2 chars). Matches skill fields **only** — category `name_en`, category `name_bn`/aliases, and free-text `skill_name`, in whichever script — **never** headline, about, or any name (MAP-06). One matcher, shared with OSP-04. **Because fuzzy matching is the most expensive public query, any request carrying `q` is held to a tighter rate limit** (API Overview). There is no separate search endpoint: search filters the same pins, it does not produce a ranked list (MAP-DM query 5, pins-only per MAP-02).

**Analytics.** Per the API Overview, the client emits map sessions, searches and filter applications with result counts, zero-result events (with keyword, script, filters, and the coarsened area), radius changes, and share taps to `POST /v1/events` — tagged guest or registered, never carrying the viewer's coordinates. The discovery reads perform no analytics writes of their own.

**The block clause, for guests.** A guest has no identity, so no block can apply — the predicate's block check is vacuously satisfied (MAP-DM). For a signed-in viewer, an Ostad who blocked them (or whom they blocked) simply does not appear, indistinguishable from being out of the area (opacity rule).

## Endpoints — favorites (MAP-08)

Favorites are keyed by `ostad_id` throughout — the handle the client already holds on the card or profile it is favoriting from ("unfavorite anywhere", MAP-08). The `favorite` row's own id and its `account_id` never leave the API (identifier rule).

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `POST /v1/favorites` | Any **registered** user (guests are routed to registration by the client, MAP-03); accepts `Idempotency-Key` | `{ ostad_id }` | `{ ostad_id, favorited: true }` — creates the `favorite` row, or returns the same success if it already existed (favoriting is **naturally idempotent**, MAP-DM unique constraint — no `conflict`). **The Ostad is never notified and no count is ever exposed** (MAP-08). Emits a favorite-add analytics event server-side (MAP-11) | `not_found` (no such approved Ostad, **or a block exists** — opacity rule) |
| `DELETE /v1/favorites/{ostad_id}` | Owner | — | `204`; idempotent (deleting a non-favorite succeeds). Emits a favorite-remove event server-side (MAP-11) | — |
| `GET /v1/favorites` | Owner | `?limit=&cursor=` | The private list: each entry is the map pin projection **plus `accepting_offers`**, with **distance computed on-device** from the client's own position (never sent — MAP-DM). Entries for paused Ostads show `accepting_offers: false` (OSP-11 keeps favorites reachable); entries for suspended, unapproved, or purged Ostads, or where a block now exists, are **omitted** while that holds and reappear if it clears (favorites are hidden, not deleted — MAP-DM) | — |

**Favorites are strictly one-directional and private.** No endpoint returns who favorited an Ostad, or how many did, to anyone — not the Ostad, not admin as a browsable surface (MAP-08).

## Endpoints — share links (MAP-07)

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `GET /v1/ostads/{id}/share` | Anyone | — | `{ url }` — a deep link to the public profile. Opening it in the app lands on `GET /v1/ostads/{id}` (guest-readable); without the app it resolves to the store listing (deferred deep link, an engineering default) | `not_found` (unapproved/suspended, or blocked — opacity rule) |

A shared link grants no special access: it resolves under the public profile's own rules, so a **paused** Ostad opens with the not-accepting notice (OSP-11), and a **blocked** viewer gets `not_found`, exactly as any other read (OSP api). Share-link opens land on the Ostad profile read, which records the view server-side; the share tap itself is a client event (MAP-11).

## Reference lookups

The category dropdown and its typeahead reuse `GET /v1/skill-categories` from the OSP api unchanged (active categories only). Discovery has **no** area filter — location is spatial (bounds/radius), not address-based — so no admin-areas lookup is used here.

## What the backend must do here (for the engineers, from MAP-DM)

Two indexes carry this module: a **spatial index** on approved-Ostad coordinates for bounds and radius, and a **fuzzy cross-script text index** on category names, aliases, and skill names. Both were named as hard requirements in the Data Model Overview and resolved to Supabase PostgreSQL (PostGIS + trigram) by ADR-001. The viewport cap, cluster grid, radius range (1–30 km), and rate limits are engineering defaults surfaced to ADM-19/21.

## Flows

**Guest opens the app.** Device GPS centres the map on-device → `GET /v1/discovery/map?bounds=…` → pins render, distances shown from the map centre computed on-device → the guest searches "গিটার" → `GET /v1/discovery/map?bounds=…&q=গিটার` resolves to the Guitar category (tighter rate limit) and narrows the pins → the guest taps a pin → `GET /v1/ostads/{id}` (full profile, view recorded) → taps "contact" → the client routes to registration (MAP-03). No coordinate the guest's device produced was ever stored, and the client posts a guest map-session event to `POST /v1/events`.

**Registered Shagred saves and compares.** `POST /v1/favorites {ostad_id}` on several Ostads (each emits a favorite-add event) → `GET /v1/favorites` shows them with on-device distances and `accepting_offers` → one Ostad has since paused, shown as not accepting; another was suspended and is simply absent from the list until reinstated.

## What this module does not expose

No endpoint stores, logs, or returns a viewer's position; no discovery read emits analytics or carries a `distance_km` except the radius read; no endpoint returns pins for an Ostad who is unapproved, suspended, paused-from-discovery, or blocking the viewer; no endpoint reveals who or how many favorited an Ostad, or exposes the `favorite` row id or account id; no endpoint lists or maps Shagreds (there is no such thing in this module); and no search matches an Ostad's name, headline, or about text (MAP-06).
