---
project: OstadLagbo
module: map-discovery
type: data-model
status: current
updated: 2026-09-13
id: OL-MAP-DM-001
derived_from: /OstadLagbo/modules/map-discovery/requirements/map-discovery-requirements.md
owner: Iftikher
---

# Map Discovery — Data Model

Entity owned: `favorite`. Conventions per [Data Model Overview](/OstadLagbo/data-model-overview.md). This is the layer's smallest model by entity count and its largest by **query shape** — discovery owns almost no data of its own, but it defines the read patterns the whole map experience depends on, and those patterns are where a backend choice will be tested hardest.

## What this module does not own — and why

Discovery reads `ostad_profile` (OSP), `skill_category` and `admin_area` (ADM), and `block` (RNT). It owns none of them. The map pin is `ostad_profile.latitude/longitude`; the filterable category is `skill_entry.category_id`; the searchable text is `skill_category.name_en/name_bn` and `skill_entry.skill_name`. Nothing about discovery is duplicated into a discovery-specific store — the map is a **projection**, not a copy.

## Location write path (MAP-01)

The one write this module performs against another module's entity: the Ostad's pin. Setting or moving the pin — by device GPS or manual placement — writes `ostad_profile.latitude/longitude` directly (OSP-DM); location is not a key field, so no revision is involved and the public pin moves immediately (OSP-10). The consent statement is a UI obligation, not data. **Self-preview** is the discovery projection (below) of the Ostad's *own* row, served **regardless of discoverability** — a pending, paused, or unapproved Ostad must be able to see where their pin sits before anyone else can.

## favorite

The one entity discovery owns (MAP-08).

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| account_id | uuid → user_account | Any registered account — Shagred or Ostad (MAP-08: "any registered user") |
| ostad_profile_id | uuid → ostad_profile | |
| created_at | timestamp | |

**Constraints:** unique on (`account_id`, `ostad_profile_id`) — favoriting is idempotent. **No read path exists from the Ostad's side**: no query returns who favorited an Ostad or how many did (MAP-08 acceptance). The only reads are the owner's own list and admin account detail (ADM-10, audit-logged).

**The favorites list applies a modified discoverability predicate:** entries for **paused** Ostads are shown with the not-accepting state (OSP-11 explicitly keeps favorites reachable); entries for **suspended or unapproved** Ostads are hidden while that state holds; entries with a **block** in either direction are hidden (not deleted — a block is reversible, and deleting would lose the user's intent); entries for **purged** Ostads are deleted with the profile (retention, below). **Distance** in the list is computed **on-device** from the client's own live position against the returned coordinates — the user's position is never sent to compute it.

## The discovery projection

Every map, search, filter, and favorites read returns the **same narrow projection** of an Ostad — never the full profile row (MAP-09 scraping resistance, made structural):

```
ostad_profile.id, display_name, photo_ref, latitude, longitude,
rating_avg, rating_count, headline,
verified = (approval_status = approved)
```

The badge is `approval_status = approved` alone — ADM-03 guarantees a passed identity check whenever a profile is approved, so the map's hottest query path does **not** join `identity_document`; the invariant that the two agree lives in ADM-DM's reconciliation check, not here. `rating_count` is carried so the client can render "New" when it is zero (RNT-03). Skill categories for the card are joined only for the *selected* category context, not the full skill list. The full profile is a separate read (OSP-DM's public profile read) triggered by tap-through, itself guest-readable (MAP-03).

## Query patterns this module must serve

These are the read shapes the backend must support efficiently at NFR-08 scale (1,000 approved Ostads, 500 concurrent) and NFR-02 latency (first pins ≤2 s on 4G).

### 1. Viewport query (MAP-02, MAP-09)

Input: a bounding box (the visible map area) + zoom level. Output: the discovery projection for every Ostad satisfying the **discoverability predicate** (OSP-DM) with coordinates inside the box, **and** with no block between viewer and Ostad. **Above a viewport cap (engineering default), the server returns aggregated cluster counts per grid cell only — no individual projections** — until the client zooms in. This is both the low-zoom clustering behavior and a scraping-resistance mechanism: no single request ever enumerates more Ostads than the cap.

**Index requirement:** a spatial index on `ostad_profile(latitude, longitude)` restricted to discoverable rows. This is the single most important performance requirement in the platform.

### 2. Radius query (MAP-04)

Input: a center point + radius in km. Output: the discovery projection for discoverable, non-blocked Ostads within the radius, with `distance_km` computed from the center. Combines with query 1 as an additional filter.

**The center is a query parameter, not a datum.** It is the map's current center — which, until the user pans, may equal the device's GPS-initialized position. It is transmitted to serve the query, **never persisted, and scrubbed from request logs** (NFR-06). No table, event, or log line receives it. See "Privacy guarantees" below.

### 3. Category filter (MAP-05)

Adds `EXISTS skill_entry WHERE category_id = :selected` to queries 1–2. Single-select in MVP. Deactivated categories (`skill_category.active = false`) never appear as selectable inputs; an Ostad still holding one remains discoverable by other means.

### 4. Gender filter (MAP-05)

Adds `ostad_profile.gender = :selected` when not "Any." Trivial; listed for completeness of the AND-composition.

### 5. Keyword search (MAP-06, CL-013)

The **cross-script fuzzy match**. Input: free text in either script. Output: the pin set narrowed to discoverable, non-blocked Ostads whose skills match. **Search filters; it does not rank** — presentation is pins-only (MAP-02), so there is no ordered result list to score. Ranking exists only inside the typeahead suggestions (OSP-04), which is the same matcher serving a different surface.

**Match scope, exactly:** `skill_category.name_en`, `skill_category.name_bn`, and `skill_entry.skill_name` (in whatever script it was entered). **Never** `headline`, `about`, `display_name`, or legal names (MAP-06 acceptance).

**Match method:** fuzzy — edit-distance or equivalent per script — so "gitar" and "গিটার" both resolve to the Guitar category, and a misspelled skill name still hits. One matcher implementation, shared with OSP-04's typeahead. Query-time normalization (case, Bangla vowel-sign variants, common transliteration equivalents) is an engineering default the matcher owns.

**Index requirement:** a trigram or equivalent fuzzy index on the three matched fields, both scripts — with the spatial index, the second requirement the backend architecture decision must satisfy.

### 6. Composition rule

Queries 1–5 compose under **AND semantics** (MAP-05, MAP-06): viewport ∧ radius ∧ category ∧ gender ∧ keyword ∧ discoverability ∧ no-block. The discoverability predicate and the block check apply to **every** discovery read without exception — there is no "unfiltered" map read.

### 7. Zero-result detection (MAP-04, MAP-11)

When a composed query returns nothing, the app renders the empty state *and* emits a zero-result analytics event carrying the filters, keyword, script, and a **coarsened map area** — the containing thana or a rounded grid cell (engineering default), **never the exact center or bounding box** — as the raw material for ADM-14's demand intelligence. Analytics emission, not a stored entity.

### 8. Deep-link resolution (MAP-07)

Input: an `ostad_profile.id` from a share link. Output: the full public profile (OSP-DM read) — for a paused Ostad, with the not-accepting notice (OSP-11); for a suspended, purged, or unapproved one, a "not available" state. Deep links bypass discovery filters but **not** the block check for authenticated viewers.

## Guest access — the read-path rule (MAP-03)

Queries 1–5 and 8 are served to **unauthenticated** requests with one difference: the block check is vacuously satisfied (no viewer identity, no blocks). Everything else — the discoverability predicate, the narrow projection, the viewport cap, rate limiting (NFR-05) — applies identically. Guest reads emit analytics under a guest-session pseudonym (NFR-06), never a device fingerprint stored as data.

## Privacy guarantees, restated structurally (MAP-10, NFR-06)

No query in this module **persists or logs** a viewer's position. Coordinates the client sends — the viewport box (query 1), the radius center (query 2) — are consumed to answer the request and discarded: excluded from request logs, never written to any table, and reduced to a coarsened area before reaching analytics (query 7). The device's GPS may initialize the map on-device and may compute favorites-list distances on-device; that value is transmitted only as an ephemeral query parameter, and only when the user has not yet panned away from it. The only coordinates any discovery query **returns** belong to discoverable Ostads.

## Retention behavior (OL-RET-001 mapping)

| Entity | On account deletion |
|---|---|
| favorite | Purged at day 30 with the owning account (`account_id`); rows pointing at a purged Ostad (`ostad_profile_id`) are deleted when that profile purges — favorites have no reason to outlive either party |

Discovery holds no other data; nothing else to retain or purge.

## What the backend decision must satisfy (for the architecture decision record)

Two hard requirements surface here that no other module produces: **(a)** an efficient spatial index with bounding-box and radius queries over ~1,000–10,000 points, with server-side cluster aggregation above a cap; and **(b)** fuzzy text matching across Latin and Bangla scripts with per-script normalization. A backend that supports both natively is strongly preferred over one requiring a separate search service at MVP scale (NFR-13 cost posture). A third, softer requirement: request-log scrubbing of coordinate parameters must be achievable at the infrastructure layer, not left to application discipline.
