---
project: OstadLagbo
type: decision
status: current
updated: 2026-09-24
id: OL-DEC-002
derived_from: /OstadLagbo/decisions/adr-001-platform-architecture.md
owner: Iftikher
decision_status: accepted
accepted: 2026-09-24
---

# ADR-002 — Analytics Event Store

## Status

**Accepted** — founder approval 2026-09-24. This decision is revisited only by a superseding ADR, never edited in place. It **adds to** ADR-001 (which it does not supersede): ADR-001 fixed the platform but never named where analytics events are stored.

## Context

The admin panel's business-intelligence suite (ADM-12 funnels and connections, ADM-13 growth and retention, ADM-14 demand intelligence, ADM-15 quality) renders charts and time-series from **analytics events**. The data-model layer deliberately keeps events out of the product model (Data Model Overview → instrumentation convention), and the API receives them at `POST /v1/events` (OL-API-001) — but no document said where they go. The REG api review surfaced the gap.

Constraints: free or free-tier-viable (NFR-13); no personal data in analytics payloads — pseudonymous ids, no phone, name, or precise coordinates (NFR-06, MAP-DM coarsening); the retention schedule's analytics rows — user-linked events 24 months then aggregate-only, de-linked at account purge (OL-RET-001); the charts must live **inside the admin panel** (ADM-12…15), not in a separate vendor's UI; and every new vendor is a new data-residency question while the PDPA ruling on ADR-001's Singapore location is still pending.

## Options considered

| | A · Supabase table (chosen) | B · Product-analytics SaaS (e.g., PostHog) | C · Firebase / Google Analytics |
|---|---|---|---|
| Marginal cost | $0 within the Pro plan | Free tier, then usage-based | Free |
| New vendor / residency question | **None** — same database, same region | Yes — events leave to the vendor's region | Yes — Google-controlled |
| Charts inside the admin panel | Yes — queried directly | Only by re-exporting; its native dashboards live outside the panel | Only via BigQuery export |
| Joins with product data (e.g., connections by category) | Native SQL | Not without syncing product data out | Not without export |
| Server-side events (offers, verdicts) | Written by the API directly | Via its SDK | Awkward |
| Build effort | Rollup queries must be written | Funnels and retention come prebuilt | Prebuilt, limited |

Option B is genuinely good software and would save chart-building effort; it loses on the residency question, on keeping charts in the panel, and on joining events to product data. Option C loses on data control and on server-side events.

## Decision

**Store analytics events in a dedicated `analytics` schema in the same Supabase database (ADR-001), separate from the product schema.**

**`analytics.event`** — append-only, enforced by database permissions (the same mechanism as the admin audit log, ADM-DM):

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| event_name | string | From the analytics event catalog (a planned document; until then, each module's instrumentation requirement) |
| occurred_at / received_at | timestamps | Client time and server time; charts use `received_at` for ordering |
| actor_kind | enum: `guest` \| `user` \| `system` | |
| account_id | uuid, nullable | For `user` events only; **nulled at the account's purge** (OL-RET-001 de-linking), after which the event keeps its aggregate weight anonymously |
| session_id | string | A pseudonymous id generated on the device (guests) or per session (users); never derived from phone, device hardware ids, or advertising ids |
| role | enum, nullable | `ostad` \| `shagred` for user events — enables role-split charts without a join |
| properties | json | Event-specific fields. **Never** phone, name, email, free text a user typed, or coordinates — locations only as a coarsened area (thana or grid cell, MAP-DM) |
| app_version / locale / platform | strings | For segmenting and for debugging a bad release |

**Rollups.** A nightly scheduled job (pg_cron, ADR-001) aggregates events into **daily rollup tables** keyed by date, event, role, and the dimensions each chart needs (category, district, script). The admin panel's charts read the rollups, never the raw table, so dashboards stay fast regardless of event volume.

**Retention.** Raw user-linked events: **24 months**, then deleted — their information survives only in the rollups (OL-RET-001's "then aggregate-only"). Raw guest events: 24 months likewise. Rollups: retained indefinitely (no personal data). De-linking at purge (above) is part of the retention job.

**Write paths.** Clients batch events to `POST /v1/events` (OL-API-001); the API validates each against the catalog, strips anything outside the allowed property set, and writes. The API writes server-side events (offer created, connection made, verdict issued) directly in the same transaction as the product change where a funnel depends on exact counts.

## Consequences

**Positive:** zero marginal cost; no new vendor; no new residency question — analytics data lives wherever ADR-001's data lives and inherits whatever the PDPA ruling decides for it; charts are native to the admin panel; funnels can join events to product data in plain SQL.

**Costs and obligations:**
- The funnel, retention, and cohort queries that a SaaS tool provides prebuilt must be written — part of Slice 5's ADM-12…15 build (OL-BLD-001).
- **Storage growth is the watch item.** At MVP scale (NFR-08) raw events are expected in the low millions per year — a few GB over the 24-month window, inside Supabase Pro's included database size alongside product data. If raw volume approaches the plan's limit, the mitigation is to export raw events older than 90 days to compressed files in Storage (cheaper per GB) while rollups stay in the database. The admin panel's operations view should surface analytics table size so this is seen early.
- Events are only as good as their catalog: an **analytics event catalog** document (already planned) becomes the contract for every event name and its allowed properties.

## Open items created by this decision

1. **Documentation:** the analytics event catalog — every event name, its trigger, and its allowed properties; the API's validation list.
2. **Engineering (Slice 0):** create the `analytics` schema with append-only permissions; the events pipeline is part of Slice 0's gate ("an analytics event lands").
3. **Engineering (Slice 5):** the nightly rollup job and the chart queries.
4. **Operations:** a storage-size indicator for the analytics schema in the admin panel's operations area.

## Superseded by

None.
