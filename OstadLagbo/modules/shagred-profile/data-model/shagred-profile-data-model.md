---
project: OstadLagbo
module: shagred-profile
type: data-model
status: current
updated: 2026-09-13
id: OL-SGP-DM-001
derived_from: /OstadLagbo/modules/shagred-profile/requirements/shagred-profile-requirements.md
owner: Iftikher
---

# Shagred Profile — Data Model

Entities owned: `shagred_profile`, `ostad_history_entry`. Conventions per [Data Model Overview](/OstadLagbo/data-model-overview.md). This model is deliberately small — it exists to hold the little a Shagred is, and to make the Shagred-invisibility principle (SGP design principle; Overview rule 4) structurally impossible to violate. Revised 2026-09-13 after the cross-layer review: profile anonymization removed (it was a phantom state — nothing references the profile after purge); address-chain validity added.

## What this model deliberately does not contain

- **No coordinates, in any form** — no lat/long, no geohash, no "approximate location." The `admin_area` references below are the only locational data (SGP-02).
- **No rating fields** — rating is one-directional (baseline §6); Shagreds are never rated.
- **No counters** — no offers-sent, acceptance-rate, or activity fields that could leak a Shagred's behavior to any viewer (SGP-04).
- **No revision machinery** — Shagreds undergo no review (SGP-06); every edit publishes to the permitted audience instantly.
- **No anonymized state** — the profile purges outright at day 30. "Former Shagred" is rendered from `rating.anonymized` and `connection.anonymized` with their display-name snapshots (RNT-DM, OFR-DM); nothing reads this profile after purge, so there is nothing to anonymize here (Overview: tombstone references).

## shagred_profile

One row per Shagred, one-to-one with `user_account` (`role = shagred`).

| Field | Type | Visibility | Rules |
|---|---|---|---|
| id / account_id | uuid / uuid | — | 1:1 with `user_account` |
| display_name | string | Permitted Ostads (SGP-05) | Required (REG-08) |
| photo_ref | storage ref, nullable | Permitted Ostads | Optional |
| gender | enum, nullable | Permitted Ostads | Optional |
| street_address | string | **Private** — Shagred and admin only | Never served to any Ostad (SGP-01) |
| division_id / district_id / thana_id | uuid → `admin_area` (ADM) | Thana + District to permitted Ostads; Division implied | The only locational data (SGP-02). **The four `admin_area` references must form a valid parent chain** (postal code under thana under district under division), enforced at write time (Overview: address chain validity) |
| postal_code_id | uuid → `admin_area` (ADM) | **Private** — Shagred and admin only | Collected per CL-008; never served to Ostads (SGP-01) |
| joined_at | timestamp | Permitted Ostads | The only statistic (SGP-04) |
| purge_at / legal_hold | per Overview conventions | — | Retention behavior below |

Date of birth, phone, and email are **not** on this entity — they live on `user_account` (REG) and are never served through any profile read (SGP-01 acceptance).

### Visibility — the permitted-Ostad predicate

A Shagred profile row is returned to an Ostad **only when all of these hold**:

```
an `offer` exists from this Shagred to this Ostad with status = pending
   OR a `connection` exists between them            (SGP-05 lifecycle)
no block exists between the two accounts             (RNT-08)
shagred user_account.status ≠ purged
```

No other read path exists: a Shagred profile is never listable, searchable, mappable, or reachable by ID without satisfying this predicate. The predicate is evaluated by the centralized policy layer (Overview → Authorization model), not by individual endpoints. Declined, expired, and withdrawn offers satisfy neither clause — visibility lapses the moment the offer leaves `pending` without becoming a connection.

The **projection** served to a permitted Ostad is fixed: `display_name`, `photo_ref`, `gender`, `district_id`, `thana_id`, `joined_at`. Never `street_address`, `postal_code_id`, or anything from `user_account`.

## ostad_history_entry

A system-derived, **immutable, owner-only** record: one row per connection this Shagred has ever made (SGP-03).

| Field | Type | Rules |
|---|---|---|
| id / shagred_profile_id | uuid / uuid | |
| connection_id | uuid → `connection` (OFR) | The source of truth; this row is a projection of it, created on connection |
| ostad_display_name_snapshot | string | Captured at connection time so the entry survives the Ostad's later deletion |
| ostad_profile_id | uuid, nullable → ostad_profile | Nulled when the Ostad's profile row is deleted at purge; the entry remains, displayed as "deleted account" |
| connected_at | timestamp | The connection's acceptance timestamp |

**No mutation path.** No endpoint updates, hides, or deletes an `ostad_history_entry` — not for the Shagred, not for admin. The only write is the insert at connection time. This is the structural form of the founder's "history is a fixed record" ruling.

**No external read path.** Only the owning Shagred's account can read these rows; not the listed Ostads, not other users, not as a count. Admin sees them only through ADM-10's account detail (audit-logged), never as a browsable surface.

## Retention behavior (OL-RET-001 mapping)

| Entity | On the Shagred's deletion | On a listed Ostad's deletion |
|---|---|---|
| shagred_profile | **Purged outright at day 30** with the account (tombstone remains on `user_account`). Persisting records that involved this Shagred — ratings, connections, reports, tickets — keep their tombstone references and their own display-name snapshots; none reads this row afterward | — |
| ostad_history_entry | Purged with the owning Shagred at day 30 — no one else can see them, so nothing is lost | `ostad_profile_id` nulled; `ostad_display_name_snapshot` and `connected_at` retained; row persists |

**Storage objects:** `photo_ref` deletion follows the same-operation rule as OSP (object deleted with the field; swept by ADM-18; out of backups within 90 days).

## Queries this model must serve

Permitted-Ostad profile read (the predicate above, then the fixed projection); the owning Shagred's own profile read (full row); the owning Shagred's history list (`ostad_history_entry` ordered by `connected_at desc`, joined to `ostad_profile` where not null); admin account-detail read (ADM-10, full row + history, audit-logged); address-chain validation at write; existence checks by `account_id` for OFR's offer creation.
