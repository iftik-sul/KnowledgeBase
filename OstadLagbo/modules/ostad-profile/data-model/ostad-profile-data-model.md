---
project: OstadLagbo
module: ostad-profile
type: data-model
status: current
updated: 2026-09-12
id: OL-OSP-DM-001
derived_from: /OstadLagbo/modules/ostad-profile/requirements/ostad-profile-requirements.md
owner: Iftikher
---

# Ostad Profile — Data Model

Entities owned: `ostad_profile`, `profile_revision`, `skill_entry`, `education_entry`, `experience_entry`, `portfolio_item`. Conventions per [Data Model Overview](/OstadLagbo/data-model-overview.md). This is the layer's largest model — it defines the profile that carries the platform's entire trust story, and the revision mechanism that makes "the public never sees an unapproved edit" (OSP-10) a property of the schema, not a UI convention.

## Two review paths — and which entity governs each

The platform reviews an Ostad twice over, and the model treats these differently:

- **Initial approval** (REG-11, ADM-02/03): the whole profile plus identity documents are reviewed before the Ostad is ever public. This path is governed by **`ostad_profile.approval_status`** — nothing is public until it reaches `approved`, so no revision machinery is needed. There is no "last approved version" to protect, because there is no public version yet.
- **Post-approval key-field edits** (OSP-10, ADM-06): once a profile is live, edits to legal names, identity documents, or skills must not reach the public until approved. This path — and **only** this path — uses `profile_revision`.

A `profile_revision` row therefore never exists for an Ostad who has not yet been approved at least once.

## Design decision: what a revision snapshots

**Key-fields-only snapshots**, not whole-profile. A `profile_revision` captures exactly the fields OSP-10 designates as key — legal names, identity-document reference, and the skill set — because those are the only fields that ever require approval before publishing. Everything else (headline, about, education, experience, portfolio) writes directly to `ostad_profile` and is public the instant it saves, per OSP-10's explicit trade-off.

**Why not whole-profile snapshots:** a full-profile revision model would give *every* edit a diffable version when the requirement says only three field groups ever need one, storing far more than the review workflow uses and filling ADM-02's diff view with noise from fields never under review. Key-fields-only mirrors the requirement precisely: small, cheap, and the diff is naturally exactly what ADM-06 cares about.

## ostad_profile

One row per Ostad, one-to-one with `user_account` (`role = ostad`). Holds the **current public truth** for non-key fields; for key fields it holds the **last approved** state, with pending changes living in `profile_revision`.

| Field | Type | Visibility | Rules |
|---|---|---|---|
| id / account_id | uuid / uuid | — | 1:1 with `user_account` |
| legal_name_en / legal_name_bn | string | Public | **Key field.** Must match identity document (ADM-02) |
| display_name | string | Public | Not a key field; edits publish instantly |
| photo_ref | storage ref | Public | |
| gender | enum | Public | |
| headline / about | string / text | Public | About nullable |
| occupation / years_experience / languages | string / int / string[] | Public | |
| street_address | string | Internal | Never served publicly (OSP-02) |
| division_id / district_id / thana_id / postal_code_id | uuid → `admin_area` (ADM) | Public | See administrative-area dataset below |
| latitude / longitude | decimal | Public | **The system's only coordinate pair** (Overview rule 4) |
| approval_status | enum: `draft` \| `pending` \| `changes_requested` \| `rejected` \| `approved` | Public (as a trust signal) | **Canonical publishing gate.** Written only by ADM verdicts (ADM-04) and by submission (REG-11). Not mirrored from `review_case` — `review_case` records the *review*; this field records the *state of the profile* |
| paused_at | timestamp, nullable | System | OSP-11; null = not paused |
| completion_pct | int, computed | Public | Engineering-default formula (OSP-09) |
| rating_avg / rating_count | decimal / int | Public | Maintained by RNT on rating create/edit/remove |
| joined_at / last_active_at | timestamp / date | Public | last_active at day granularity only (OSP-08) |
| purge_at / legal_hold | per Overview conventions | — | Retention behavior below |

Identity-verification status is **not duplicated here** — it is owned by `identity_document.verification_status` (REG) and read through it. The verified badge renders when that status is `passed` and `approval_status` is `approved` (ADM-03 guarantees the first whenever the second holds).

### Discoverability — one predicate

An Ostad appears on the map, in search, and in category results **only when all four conditions hold**:

```
user_account.status        = active          (not suspended, not pending_deletion, not purged)
ostad_profile.approval_status = approved
ostad_profile.paused_at    IS NULL
no block exists between the viewer and this Ostad   (RNT-08)
```

This predicate is defined once here and referenced by MAP-02, MAP-05, MAP-06, and OFR-01; no module restates it in its own terms. Offer creation (OFR-01) checks the same predicate minus the viewer-specific block clause, which it evaluates separately.

## profile_revision

A queue of pending **post-approval** key-field changes. At most one open row per profile: a further key-field edit while one is pending **amends the same open revision** rather than creating a competing row (consistent with ADM-05's history-carrying resubmission).

| Field | Type | Rules |
|---|---|---|
| id / profile_id | uuid / uuid → ostad_profile | |
| proposed_legal_name_en / _bn | string, nullable | Set only if changed |
| proposed_skill_entries | array of skill_entry-shaped values, nullable | A **copy** in `skill_entry` shape, not a reference to live rows (see below) |
| proposed_identity_document_id | uuid, nullable → identity_document | Set when identity documents are resubmitted |
| status | enum: `pending` \| `approved` \| `rejected` | Drives ADM-02's queue and ADM-06's publish/discard |
| review_case_id | uuid → `review_case` (ADM) | The queue item carrying admin's verdict, notes, and diff |
| submitted_at / resolved_at | timestamps | |

**On approval:** proposed values overwrite the corresponding `ostad_profile` fields atomically; proposed skills **replace the live `skill_entry` rows wholesale** (skills are evaluated as a set, not field-by-field); `status → approved`. **On rejection:** `ostad_profile` and its live rows are untouched; `status → rejected`; the Ostad may edit and resubmit, opening a new revision (ADM-05, unlimited).

## skill_entry

Repeatable, 1–5 per Ostad (OSP-04). Live rows always belong to `ostad_profile` and are always the approved, public set. A pending change does not modify these rows — it holds a **copy** inside `proposed_skill_entries` until a verdict. The same conceptual skill therefore never exists as a live row and a pending row simultaneously; there is one live set and, at most, one proposed set.

| Field | Type | Rules |
|---|---|---|
| id / profile_id | uuid / uuid | |
| category_id | uuid → `skill_category` (ADM) | Constrained to the fixed list; never free text |
| skill_name | string | Free text (OSP-04) |
| level | enum: `beginner` \| `intermediate` \| `expert` | |
| years_experience | int | |

## education_entry

Repeatable, 0+ (OSP-05). Not a key field — publishes instantly.

| Field | Type | Rules |
|---|---|---|
| id / profile_id | uuid / uuid | |
| level | enum: `ssc` \| `hsc` \| `bachelor` \| `masters` \| `phd` \| `other_certification` | |
| credential_name / institution | string | |
| passing_year | int, 1950–current | |

## experience_entry

Repeatable, 0+, four groups (OSP-06). Not a key field.

| Field | Type | Rules |
|---|---|---|
| id / profile_id | uuid / uuid | |
| group | enum: `work` \| `teaching` \| `certification` \| `award` | |
| title / organization / period / description | string / string, nullable / string / string | description ≤300 chars |

## portfolio_item

Repeatable, typed (OSP-07). Not a key field.

| Field | Type | Rules |
|---|---|---|
| id / profile_id | uuid / uuid | |
| item_type | enum: `image` \| `intro_video` \| `document` \| `external_link` | |
| storage_ref / external_url | storage ref, nullable / url, nullable | Exactly one populated, matching item_type |
| duration_seconds | int, nullable | **`intro_video` only; ≤45 enforced by constraint; at most one `intro_video` row per profile_id** (OSP-07, encoded structurally) |

## Dependency: administrative-area dataset

Address fields reference `admin_area` — a **reference dataset owned by ADM** (alongside `skill_category`), holding Bangladesh's Division → District → Thana hierarchy with postal codes, each row carrying `name_en` and `name_bn` for the bilingual UI (CL-016). It is seeded data, not user-generated; OSP-02 and SGP-02 both read it. Its definition belongs to the ADM data model; this document only consumes it. *(Note for the ADM session: `admin_area` is a new entity not yet listed in the Overview's ownership map — it is added there when the ADM model is written.)*

## Retention behavior (OL-RET-001 mapping)

| Entity | On account deletion |
|---|---|
| ostad_profile | Purged at day 30 with the account. Ostads do not anonymize — profile and reviews leave together (RNT-05) |
| profile_revision | Purged with the profile; an open revision is discarded |
| skill_entry / education_entry / experience_entry / portfolio_item | Purged with the profile (child rows) |

**Storage objects:** deleting a row that holds a `storage_ref` (`photo_ref`, portfolio images, intro video, documents) must delete the underlying storage object in the same operation — row deletion alone would orphan media and defeat the policy. Orphaned objects are swept by the retention tooling (ADM-18), and all deleted media ages out of backups within 90 days (NFR-07).

## Queries this model must serve

Public profile read (join `ostad_profile` + children; key fields from the approved state only — an open `profile_revision` is **never** joined into a public read); admin review read (profile + open revision + `identity_document`, for ADM-02's diff); map/search read (a **narrow projection** — id, display_name, photo_ref, lat/long, rating_avg, badge — never the full row, per MAP-09's scraping resistance); the discoverability predicate above; category-filtered skill lookup (`skill_entry.category_id`); insights aggregation (OSP-12 — sourced from analytics events, not this model).
