---
project: OstadLagbo
module: shagred-profile
type: api
status: current
updated: 2026-09-24
id: OL-SGP-API-001
derived_from: /OstadLagbo/modules/shagred-profile/requirements/shagred-profile-requirements.md
owner: Iftikher
---

# Shagred Profile — API

Endpoints for the Shagred's own profile, the one narrow read an Ostad may make of it, and the Shagred's private Ostad history. Conventions per [API Overview](/OstadLagbo/api-overview.md); entities per [SGP Data Model](/OstadLagbo/modules/shagred-profile/data-model/shagred-profile-data-model.md). The module's design principle carries straight into the API: **Ostads exist to be found; Shagreds must never be findable.** This api therefore has no list, no search, no browse, and no map endpoint of any kind for Shagreds.

## Endpoints — the Shagred's own profile

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `GET /v1/shagred-profile` | The Shagred themself (active) | — | **Own profile**: `{ id, display_name, photo_url? (signed), gender?, address: { street_address, division, district, thana, postal_code }, joined_at, profile_complete }` — the full address, including the parts no Ostad ever sees | `forbidden` (Ostad); `suspended` |
| `PUT /v1/shagred-profile` | The Shagred themself (active), **only while `profile_complete` is false** — first-time setup | `display_name` (required), `address: { street_address, division_id, district_id, thana_id, postal_code_id }` (required, REG-08), `photo_upload_id?` (purpose `profile_photo`), `gender?` | own profile | `validation_failed` (`details.address = "invalid_chain"`; required fields missing); `state_conflict` (`details.use = "patch"` — the profile is already complete) |
| `PATCH /v1/shagred-profile` | The Shagred themself (active) | Any subset of the fields above; **anything omitted stays unchanged**. `photo_upload_id: null` removes the photo; `gender: null` clears it | own profile | `validation_failed` |

**Why setup is a separate `PUT`.** `PUT` replaces the whole profile, so a Shagred who reopened the setup form and saved without re-attaching a photo would lose it. Restricting `PUT` to the first, empty setup — and routing every later edit through `PATCH`, where omission means "unchanged" — makes that loss impossible.

**Setup and REG-08.** REG-08 has the Shagred complete setup right after registration, before reaching the map. That ordering is a **client flow rule**: the API cannot gate the map itself, because guests browse it without any account (MAP-03). The API instead enforces completeness at the one point it matters — **sending an offer**: OFR-01 refuses an offer from an incomplete profile with `state_conflict`, `details.reason = "profile_incomplete"`, because an Ostad deciding on an offer must see at least a name and a Thana and District. `profile_complete` is **derived** — true when a display name and a complete, valid address exist — and is what REG's account summary reports as `shagred.profile_complete`.

**Edits publish instantly** (SGP-06): no review, no revision. A removed photo's storage object is deleted in the same operation (SGP-DM). No coordinates are accepted by any endpoint in this module — a request carrying `lat`/`lng` is rejected with `validation_failed`, not silently ignored, so a client bug that tried to store a location is caught immediately (SGP-02, Data Model Overview rule 4).

## Endpoints — the Ostad's view of a Shagred

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `GET /v1/shagreds/{id}` | **An Ostad only**, and only when the **permitted-Ostad predicate** holds (below). `{id}` is the Shagred's **profile** id — the only Shagred identifier any client ever holds (API Overview → identifiers) | — | **The fixed projection** (SGP-DM): `{ id, display_name, photo_url? (signed), gender?, area: { district, thana }, joined_at }` — area names localized to the Ostad | `not_found` for **every** refusal (below) |

**The permitted-Ostad predicate** (SGP-05, SGP-DM), evaluated by the policy layer on every read:

```
caller is an Ostad
AND ( an offer from this Shagred to the caller is pending
      OR a connection exists between them )
AND no block exists between them                      (RNT-08)
AND the Shagred's account status is active or suspended
AND the Shagred's `deleted_at` is null                 (departing or terminated — CL-032)
```

The last two clauses end visibility **the moment the Shagred is leaving** — self-requested deletion (`pending_deletion`) **or admin termination** (status stays `suspended` with `deleted_at` set, CL-019) — not at purge. A **plain** suspension (no `deleted_at`) still leaves the Shagred visible to an Ostad already holding their offer or connection, so the Ostad keeps the context needed to understand a frozen chat or to report; a reinstated account clears `deleted_at` and reappears.

**Every refusal is `not_found`.** Whether the caller is a guest or another Shagred, the offer lapsed, no relationship ever existed, the Shagred is deleting, or a block exists, the response is identical. If a lapsed offer returned `forbidden` while a block returned `not_found`, the difference would reveal the block; making all refusals the same keeps the opacity rule intact (API Overview).

**The same projection travels with offers.** The OFR api embeds this projection in pending-offer and connection payloads rather than making the Ostad fetch it; wherever it is embedded, the same predicate governs it.

**After an offer lapses (binding on the OFR and RNT apis).** Once an offer is declined, expires, or is withdrawn, the Ostad's offer history shows **no Shagred projection** for it — no name, no photo, no area — but it **keeps the offer's own content**: the message text the Ostad received, and its dates. That offer remains a valid handle for **reporting** the Shagred (RNT-07's reportability survives lapse) and for **blocking** them (RNT-08, the anti-pestering tool behind OFR-02's immediate re-offers). The RNT api accepts the **offer id** as the target for both and resolves the Shagred server-side; the Ostad never regains sight of the profile. The message stays because it is what the Ostad actually received — and is often the evidence a report needs.

**No view tracking.** Unlike Ostad profiles, reads of a Shagred profile emit **no** analytics event. Recording which Ostads looked at which Shagreds would build exactly the observation record the invisibility principle exists to prevent.

## Endpoints — Ostad history (private)

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `GET /v1/shagred-profile/history` | The Shagred themself only (SGP-03) | `?limit=&cursor=` | `{ items: [ { connected_at, ostad_name, ostad_id \| null, deleted } ], next_cursor }` — ordered `connected_at` descending. `ostad_name` is **always the name captured at connection time**; `ostad_id` is the link to the Ostad's public profile, null with `deleted: true` once the Ostad's account is gone (shown as "deleted account") | `forbidden` (Ostad); `suspended` |

**Snapshot only, never live data.** History entries show no live name or photo of the Ostad. The link resolves under the public profile's own rules (OSP api): an Ostad who later blocked the Shagred, was suspended, or stopped being available all resolve identically, so no entry reveals by its appearance what happened afterward (SGP-DM display rule).

**There is no write endpoint for history — none.** No `POST`, `PATCH`, or `DELETE` exists under `/v1/shagred-profile/history`; entries are created only by the API's offer-acceptance transaction (OFR-DM). This is SGP-03's "fixed record" made structural at the API boundary: the Shagred cannot hide or remove an entry, and no Ostad can read the list, count it, or learn that it exists. Admin sees it only through the ADM api's account detail, audit-logged.

## Reference lookups

The address dropdowns use `GET /v1/admin-areas` from the OSP api, unchanged. Skill categories are not used by this module.

## Flows

**First-time setup.** `register/verify` (REG api) → the account summary shows `shagred.profile_complete = false` → the client opens the setup form (REG-08) → `PUT /v1/shagred-profile` → `profile_complete = true` → the map. Later edits are `PATCH`. If setup is somehow incomplete, the offer check (OFR-01) sends the Shagred back to it.

**An Ostad deciding on an offer.** The offer arrives (OFR api) carrying the Shagred projection → the Ostad may refresh it with `GET /v1/shagreds/{id}` while the offer is pending → the Ostad accepts: the projection stays visible for the life of the connection; or declines: the next read is `not_found`, and the offer history keeps the message and dates — with report and block actions — but no name, photo, or area.

## What this module does not expose

No endpoint lists, searches, maps, or counts Shagreds; no endpoint returns a Shagred's street address, postal code, date of birth, phone, email, or account id to any Ostad (contact reveal on acceptance is OFR's, and returns phone and email only); no endpoint returns a Shagred's Ostad history to anyone but its owner, in any form; no endpoint records or reveals which Ostads viewed a Shagred; and no endpoint accepts or returns coordinates for a Shagred.
