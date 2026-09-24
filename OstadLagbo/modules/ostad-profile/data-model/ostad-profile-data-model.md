---
project: OstadLagbo
module: ostad-profile
type: data-model
status: current
updated: 2026-09-24
id: OL-OSP-DM-001
derived_from: /OstadLagbo/modules/ostad-profile/requirements/ostad-profile-requirements.md
owner: Iftikher
---

# Ostad Profile — Data Model

Entities owned: `ostad_profile`, `profile_revision`, `skill_entry`, `education_entry`, `experience_entry`, `portfolio_item`. Conventions per [Data Model Overview](/OstadLagbo/data-model-overview.md). This is the layer's largest model — it defines the profile that carries the platform's entire trust story, and the revision mechanism that makes "the public never sees an unapproved edit" (OSP-10) a property of the schema, not a UI convention. Revised 2026-09-13 after the cross-layer review: address-chain validity; identity-document references point at specific rows. Revised 2026-09-24 (CL-021, OSP api review): profile photo is a key field; the revision's submit, lock, discard, and 90-day abandonment rules.

## Two review paths — and which entity governs each

The platform reviews an Ostad twice over, and the model treats these differently:

- **Initial approval** (REG-11, ADM-02/03): the whole profile plus identity documents are reviewed before the Ostad is ever public. This path is governed by **`ostad_profile.approval_status`** — nothing is public until it reaches `approved`, so no revision machinery is needed. While `approval_status = pending`, **key fields are locked** (the review is deciding them); non-key fields remain editable (REG-11).
- **Post-approval key-field edits** (OSP-10, ADM-06): once a profile is live, changes to legal names, identity documents, skills, or the profile photo must not reach the public until approved. This path — and **only** this path — uses `profile_revision`.

A `profile_revision` row therefore never exists for an Ostad who has not yet been approved at least once.

## Design decision: what a revision snapshots

**Key-fields-only snapshots**, not whole-profile. A `profile_revision` captures exactly the fields OSP-10 designates as key — legal names, identity-document reference, the skill set, and the profile photo (CL-021) — because those are the only fields that ever require approval before publishing. Everything else (display name, gender, headline, about, address, education, experience, portfolio) writes directly to `ostad_profile` and is public the instant it saves, per OSP-10's explicit trade-off.

**Why not whole-profile snapshots:** a full-profile revision model would give *every* edit a diffable version when the requirement says only four field groups ever need one, storing far more than the review workflow uses and filling ADM-02's diff view with noise from fields never under review. Key-fields-only mirrors the requirement precisely: small, cheap, and the diff is naturally exactly what ADM-06 cares about.

## ostad_profile

One row per Ostad, one-to-one with `user_account` (`role = ostad`). Holds the **current public truth** for non-key fields; for key fields it holds the **last approved** state, with pending changes living in `profile_revision`.

| Field | Type | Visibility | Rules |
|---|---|---|---|
| id / account_id | uuid / uuid | — | 1:1 with `user_account` |
| legal_name_en / legal_name_bn | string | Public | **Key field.** Must match identity document (ADM-02) |
| display_name | string | Public | Not a key field; edits publish instantly |
| photo_ref | storage ref | Public | **Key field** (CL-021). After approval, a new photo arrives only through a revision |
| gender | enum | Public | |
| headline / about | string / text | Public | About nullable |
| occupation / years_experience / languages | string / int / string[] | Public | |
| street_address | string | Internal | Never served publicly (OSP-02) |
| division_id / district_id / thana_id / postal_code_id | uuid → `admin_area` (ADM) | Public | **Must form a valid parent chain in `admin_area`** (postal code under thana under district under division), enforced at write time — Overview: address chain validity |
| latitude / longitude | decimal | Public | **The system's only coordinate pair** (Overview rule 4) |
| approval_status | enum: `draft` \| `pending` \| `changes_requested` \| `rejected` \| `approved` | Public (as a trust signal) | **Canonical publishing gate.** Written only by ADM verdicts (ADM-04) and by submission (REG-11). Not mirrored from `review_case` — `review_case` records the *review*; this field records the *state of the profile* |
| paused_at | timestamp, nullable | System | OSP-11; null = not paused |
| completion_pct | int, computed | Public | Engineering-default formula (OSP-09) |
| rating_avg / rating_count | decimal / int | Public | Maintained by RNT on rating create/edit/remove |
| joined_at / last_active_at | timestamp / date | Public | last_active at day granularity only (OSP-08) |
| purge_at / legal_hold | per Overview conventions | — | Retention behavior below |

Identity-verification status is **not duplicated here** — it is owned by `identity_document.verification_status` on the account's **current** document row (REG-DM: `superseded_at IS NULL`) and read through it. The verified badge renders when that status is `passed` and `approval_status` is `approved` (ADM-03 guarantees the first whenever the second holds).

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

The single pending record of an approved Ostad's key-field changes. **At most one open row per profile** (open = `status = pending`).

| Field | Type | Rules |
|---|---|---|
| id / profile_id | uuid / uuid → ostad_profile | |
| proposed_legal_name_en / _bn | string, nullable | Set only if changed |
| proposed_photo_ref | storage ref, nullable | Set only if changed (CL-021); the object sits in a non-public bucket until approval |
| proposed_skill_entries | array of skill_entry-shaped values, nullable | A **copy** in `skill_entry` shape, not a reference to live rows (see below) |
| proposed_identity_document_id | uuid, nullable → identity_document | Set when identity documents are resubmitted — references the **new** `identity_document` row inserted for the resubmission (REG-DM: many rows per account; draft rows replaced in place until the revision is submitted) |
| status | enum: `pending` \| `approved` \| `rejected` | Drives ADM-02's queue and ADM-06's publish/discard |
| submitted_at / resolved_at | timestamps, nullable | `submitted_at` is the latest submission |
| last_activity_at | timestamp | Updated on every edit and submission; drives the 90-day abandonment rule |

`review_case` references the revision (ADM-DM: `review_case.profile_revision_id`); the revision carries no back-reference, and a revision may be referenced by several cases over its life (each resubmission opens a new one).

**Review state — derived, never stored** (Overview: predicates over flags):

| State | Condition |
|---|---|
| `editing` | `status = pending` and no `review_case` references it |
| `under_review` | `status = pending` and an **open** `review_case` references it |
| `changes_requested` | `status = pending` and its latest `review_case` resolved with `request_changes` |

**Lifecycle rules:**
- **Amend in place, but never under review.** An edit in `editing` or `changes_requested` updates the same open row; there is never a second. In `under_review` the row is **locked** — the admin is reviewing a fixed target.
- **Submit** opens a new `review_case` of kind `revision` (ADM-DM), setting `identity_recheck_required` when legal names or identity change; a photo change is reviewed against the Ostad's current identity selfie.
- **Discard** is permitted only in `editing` (never submitted): the row is deleted, and any draft identity row and proposed photo object it carries are deleted in the same operation. Once any `review_case` references the row it is evidence and cannot be discarded.
- **Abandonment.** A revision in `editing` or `changes_requested` with `last_activity_at` older than **90 days** is discarded by a scheduled job after a prior notice to the Ostad (engineering default: notice at day 76), deleting its proposed photo object and any draft identity row with its images. A revision in `changes_requested` is referenced by a case and therefore evidence: on abandonment its `status` becomes `rejected` (with a `system` reason recorded in the audit log) rather than being deleted, and its uploads are deleted.

**On approval:** proposed values overwrite the corresponding `ostad_profile` fields atomically; proposed skills **replace the live `skill_entry` rows wholesale** (skills are evaluated as a set, not field-by-field); a proposed photo replaces `photo_ref` (the previous photo object is deleted in the same operation); a proposed identity document becomes the account's current one (its predecessor's `superseded_at` is set); `status → approved`. **On rejection:** `ostad_profile` and its live rows are untouched; a proposed photo object is deleted; a proposed identity document is superseded without ever having been current; `status → rejected`; the Ostad may start a new revision (ADM-05, unlimited).

## skill_entry

Repeatable, 1–5 per Ostad (OSP-04). Live rows always belong to `ostad_profile` and are always the approved, public set. A pending change does not modify these rows — it holds a **copy** inside `proposed_skill_entries` until a verdict. The same conceptual skill therefore never exists as a live row and a pending row simultaneously; there is one live set and, at most, one proposed set.

| Field | Type | Rules |
|---|---|---|
| id / profile_id | uuid / uuid | |
| category_id | uuid → `skill_category` (ADM) | Constrained to the fixed list; never free text. A **new** skill set may use active categories only; a deactivated category stays on live rows until the next skill edit (ADM-11) |
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

Address fields reference `admin_area` — a **reference dataset owned by ADM** (alongside `skill_category`), holding Bangladesh's Division → District → Thana hierarchy with postal codes, each row carrying `name_en` and `name_bn` for the bilingual UI (CL-016). It is seeded data, not user-generated; OSP-02 and SGP-02 both read it. Its definition is in `OL-ADM-DM-001`; this document only consumes it.

## Retention behavior (OL-RET-001 mapping)

| Entity | On account deletion |
|---|---|
| ostad_profile | Purged at day 30 with the account (self-service or termination path). Ostads do not anonymize — profile and reviews leave together (RNT-05); `connection.ostad_profile_id` and `ostad_history_entry.ostad_profile_id` are nulled, their snapshots carry the display |
| profile_revision | Purged with the profile; an open revision is discarded. **Independently of deletion,** an unsubmitted or returned revision inactive for 90 days is discarded with prior notice, its uploads deleted (OSP-10, OL-RET-001) |
| skill_entry / education_entry / experience_entry / portfolio_item | Purged with the profile (child rows) |

**Storage objects:** deleting a row or field that holds a `storage_ref` (`photo_ref`, `proposed_photo_ref`, portfolio images, intro video, documents) must delete the underlying storage object in the same operation — row deletion alone would orphan media and defeat the policy. Orphaned objects are swept by the retention tooling (ADM-18), and all deleted media ages out of backups within 90 days (NFR-07).

## Queries this model must serve

Public profile read (join `ostad_profile` + children; key fields from the approved state only — an open `profile_revision` is **never** joined into a public read); admin review read (profile + open revision + the referenced `identity_document` rows + the current selfie for photo comparison, for ADM-02's diff); the revision's derived review state (latest referencing `review_case`); the abandonment sweep (`status = pending and review state ≠ under_review and last_activity_at ≤ now − 90d`, with the day-76 notice); map/search read (a **narrow projection** — id, display_name, photo_ref, lat/long, rating_avg, badge — never the full row, per MAP-09's scraping resistance); the discoverability predicate above; address-chain validation at write; category-filtered skill lookup (`skill_entry.category_id`); insights aggregation (OSP-12 — sourced from analytics events, not this model).
