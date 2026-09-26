---
project: OstadLagbo
module: map-discovery
type: ui
status: current
updated: 2026-09-26
id: OL-MAP-UI-001
derived_from: /OstadLagbo/modules/map-discovery/requirements/map-discovery-requirements.md
owner: Iftikher
---

# Map Discovery — UI

Screens for the discovery map, search and filters, favourites, share links, and the Ostad's pin capture. Conventions per [UI Overview](/OstadLagbo/ui-overview.md); behaviour and endpoints per [MAP API](/OstadLagbo/modules/map-discovery/api/map-discovery-api.md); the public profile a pin opens is OSP ui; offer and contact actions are OFR ui.

**The map is the guest and Shagred home.** It is reachable with **zero registration** (MAP-03) and is the Shagred shell's first tab; an Ostad has no discovery map tab (they are found, not finding — UI overview). **The governing rule on every screen here: no viewer's position is ever sent to be stored.** Live GPS only centres the map on-device; distances are computed on-device from the map centre; the discovery reads take the *map centre/bounds the user chose*, which the API answers and forgets (MAP-10).

## Group A — The discovery map

### Discovery map
- **Purpose:** browse nearby Ostads as pins; the home surface for guests and Shagreds.
- **Shell(s):** guest, Shagred (home tab).
- **Entry:** app open (guest lands here after language choice; Shagred's Map tab); a "view on map" from a profile's pin.
- **Structure:** a full-screen map — **pins only, no list view** (MAP-02) — over Bangladesh, free pan and zoom; a **search bar**; a **filter control** (category, gender) and a **radius slider**; a **recenter-to-me** button when GPS is available; and, in the guest shell, **Log in / Create account** and the **Terms / Privacy** links in the chrome (MAP-03, REG-13). **Map attribution** — `© OpenStreetMap contributors` plus the tile provider's required credit — sits permanently on the map surface and is never covered by the preview card, filter sheet, or empty state (MAP-02, CL-035).
- **Centring:** opens on the user's live GPS position when permitted, else a default city centre (Dhaka). GPS is used **only on-device**; it is never transmitted.
- **Pins & clustering:** each approved, non-suspended, **non-paused** Ostad is a pin at exact coordinates; at low zoom or above the viewport cap the map shows **cluster counts** that expand on zoom (MAP-09, also the anti-scraping guard) — no individual pins are enumerated beyond the cap.
- **Preview card (component):** tapping a pin opens the card — photo, display name, verified badge, headline, rating average + review count (or **"New"**), and **distance from the map centre** (computed on-device). The card carries quick **Favourite** and **Share** actions (MAP-08/07; a guest tapping favourite routes to registration). Tapping the card opens the full public profile (OSP ui).
- **States:** **loading** → first pins ≤2 s on 4G, progressively (NFR-02); **empty / zero-result** → "No Ostads here yet" with a one-tap **widen radius** (MAP-04); **GPS denied** → a fully usable map centred on the default, recenter hidden.
- **Data & actions:** `GET /v1/discovery/map?bounds=&zoom=&category=&gender=&q=` on pan/zoom/filter; the client posts a guest-or-registered **map-session** analytics event to `POST /v1/events` (never carrying coordinates — REG shared endpoint, MAP-11). Any identity action a guest attempts routes to registration and returns here (MAP-03).
- **Never shows:** it sends no viewer position for storage; the only coordinates in any response belong to approved Ostads (MAP-10).

## Group B — Search, filters, and radius

### Search & filters
- **Purpose:** narrow the pins; all compose with each other and the radius under **AND** semantics (MAP-05/06).
- **Where:** the search bar and filter control on the discovery map — **there is no separate search-results screen**; search filters the same pins (pins-only, MAP-02).
- **Structure:**
  - **Keyword search** — a query (≥2 chars) matched **fuzzily and cross-script over skills only** (category names, their Bangla aliases, and free-text skill names) — never headline, about, or names (MAP-06). "gitar" and "গিটার" both find Guitar Ostads.
  - **Category filter** — single-select via the **fuzzy category picker** (shared component; deactivated categories never appear).
  - **Gender filter** — Any (default) / Male / Female (MAP-05). Profiles stored as **Other** (CL-031) appear only under "Any"; there is no "Other" filter chip.
  - **Radius slider** — 1–30 km (default 5), measured **from the map centre**, not the viewer; the active radius is visibly indicated. It rides the **same** `GET /v1/discovery/map` read as `centre` + `radius_km`, exactly like the other filters (MAP-04, CL-033).
- **States:** changing radius or a filter updates results without a fresh text search; **clear filters** restores the unfiltered map; a zero-result combination shows the empty state and widen action.
- **Data & actions:** all params ride the single `discovery/map` read (CL-033); `q` carries a **tighter rate limit** (fuzzy is the most expensive query). Searches, filter applications with result counts, **zero/low-result events** (tagged category, keyword, script, gender, coarsened area — never the exact centre), and radius changes are posted to `POST /v1/events` (MAP-11).
- **Never shows:** the exact map centre in any analytics — area is coarsened before it leaves the device/at ingestion (MAP-10, REG events endpoint).

## Group C — Favourites (MAP-08)

### Favourites list
- **Purpose:** a private shortlist of Ostads to compare and return to.
- **Shell:** Shagred shell → **Favourites** tab. (The favourite *toggle* appears on any card/profile for a registered viewer; the API permits any registered account, but the MVP surfaces the *list* only in the Shagred shell — the Ostad shell has no discovery loop.)
- **Structure:** each entry the preview projection **plus an accepting-offers indicator**, with **distance computed on-device**; tap-through to the profile; unfavourite anywhere.
- **States:** a **paused** Ostad shows "not accepting"; a **suspended, unapproved, purged, or now-blocked** Ostad is **omitted** while that holds and **reappears** if it clears (hidden, not deleted); the list **survives logout/login**.
- **Data & actions:** `POST /v1/favorites {ostad_id}` (idempotent), `DELETE /v1/favorites/{ostad_id}`, `GET /v1/favorites`. A **guest** tapping favourite routes to registration (MAP-03).
- **Never shows:** who favourited an Ostad or how many did — no such surface exists anywhere, for anyone, ever (MAP-08). Distance is computed on-device; the client's position is never sent.

## Group D — Share (MAP-07)

### Share a profile
- **Purpose:** send someone a link to an Ostad.
- **Where:** the Share action on any public profile (OSP ui) and preview card.
- **States:** **loading** → the share action shows brief progress while the link is fetched; the OS share sheet opens only once a link exists, never with a placeholder. **Empty** → not applicable. **Error** → a failed fetch keeps the user on the profile with a retry and **no share sheet**, rather than sharing a broken link; offline says the link cannot be created right now. On the **receiving** side a link that cannot resolve — paused, blocked, deleted, or purged — opens the profile's own state per MAP-07, and the blocked case stays the neutral **"not available"**, never distinguishable from a deleted one.
- **Data & actions:** `GET /v1/ostads/{id}/share` returns a deep link. Opening it in the app lands on the profile — for guests too (MAP-03); without the app it resolves to the store listing (deferred deep link, so the profile opens after install). A link to a **paused** profile opens it with the not-accepting notice; a link the viewer is **blocked** from resolves to "not available" (opacity). Share taps and link opens are instrumented (MAP-11).
- **Never shows:** a shared link grants no special access — it resolves under the profile's own public rules.

## Group E — Ostad location capture & self-preview (MAP-01)

### Set / move the teaching pin
- **Purpose:** the Ostad places the single public pin others discover them by.
- **Shell:** Ostad shell — reached in **onboarding stage 4** (REG ui) and afterward from **profile editing** (OSP ui); not a discovery-map surface.
- **Structure:** a map to **drop or drag a manual pin**, or a **use-my-GPS** action to place it at the current position; the **public-pin consent statement** — plainly, *the pin is publicly visible to everyone at exact precision; place it where you teach or wish to be found (a coaching centre, shop, or landmark), not necessarily your home* (MAP-01, risk R-04); and a **self-preview** — the pin and preview card exactly as the public will see them.
- **States:** works with **GPS denied** (manual pin); location edits **publish immediately** (location is not a key field) and move the public pin in real time; the self-preview is available **regardless of approval state**, so a pending Ostad can still check their card.
- **Data & actions:** `PUT /v1/profile/location {lat, lng}` (onboarding stage 4 delegates here); self-preview via `GET /v1/profile/location/preview`.
- **Consent surface:** the public-pin statement must appear on this screen every time it is shown (overview → consent surfaces).
- **Never shows:** this is the *only* place a coordinate is ever stored on the platform, and only for an Ostad, by their explicit act — never for a Shagred or guest (MAP-10, SGP-02).

## Flows

**Guest discovers and is nudged to register.** Language → the map (map-first) → search "গিটার" → pins narrow to Guitar Ostads → tap a pin → preview card → tap → the full public profile → tap "contact" → routed to registration → after signing up, returned to the same profile (MAP-03).

**Shagred shortlists.** Favourite several Ostads from cards → open the **Favourites** tab → compare with on-device distances and accepting-offers state → one has since paused (shown "not accepting"); another was suspended (silently absent) → send an offer to a chosen one (OFR ui).

**Ostad sets their pin.** Onboarding stage 4 (or later, profile editing) → drag the pin to their coaching centre → read the public-pin consent statement → save (publishes immediately) → open the self-preview to confirm the card looks right.

## What this module's screens never show

No screen sends a viewer's position to be stored, or shows a coordinate that is not an approved Ostad's; no analytics event carries the exact map centre (area is coarsened); no screen enumerates more Ostads than the viewport cap (clusters above it); no screen reveals who or how many favourited an Ostad; no discovery surface lists or maps Shagreds; and no map distinguishes a paused Ostad's deep link (explicit notice) from a blocked viewer's (neutral "not available").
