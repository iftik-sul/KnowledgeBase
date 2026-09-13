---
project: OstadLagbo
module: admin-review
type: data-model
status: current
updated: 2026-09-13
id: OL-ADM-DM-001
derived_from: /OstadLagbo/modules/admin-review/requirements/admin-review-requirements.md
owner: Iftikher
---

# Admin Review & Dashboard — Data Model

Entities owned: `admin_account`, `admin_session`, `review_case`, `moderation_action`, `skill_category`, `admin_area`, `broadcast`, `admin_audit_entry`. Conventions per [Data Model Overview](/OstadLagbo/data-model-overview.md). `report` and `support_ticket` are owned by `ratings-and-trust` and `support` respectively; this document only defines how ADM queues and acts on them.

## review_case — the record, not the gate

`ostad_profile.approval_status` (OSP) remains the **canonical publishing gate**, exactly as OSP-DM declared, and `identity_document.verification_status` (REG) remains the **canonical identity state**. This model duplicates neither. `review_case` is the **workflow record**: one row per review episode, whether the Ostad's first submission or a later key-field re-review. What was decided about identity, and by whom, is recorded by the audit log (`identity_mark` entries, ADM-17), not by a second copy of the status here.

| Field | Type | Rules |
|---|---|---|
| id / ostad_profile_id | uuid / uuid, nullable after purge | See retention |
| kind | enum: `initial` \| `revision` | `initial` reviews the whole profile (REG-11); `revision` reviews a `profile_revision` (OSP-DM) |
| profile_revision_id | uuid, nullable → profile_revision | Set iff kind = `revision` |
| identity_document_id | uuid, nullable → identity_document | The document under review; nullable after purge (see retention) |
| identity_recheck_required | boolean | `true` for every `initial` case, and for `revision` cases whose revision changes legal names or identity documents; `false` for skills-only revisions, which carry the existing passed status forward without re-examination |
| verdict | enum: `approve` \| `request_changes` \| `reject`, nullable | Null while status = open |
| verdict_note | text, nullable | **Required** when verdict is request_changes or reject (ADM-04); delivered to the Ostad in-app (REG-11) |
| reviewer_admin_id | uuid → admin_account | |
| status | enum: `open` \| `resolved` | |
| opened_at / resolved_at | timestamps | |
| profile_display_name_snapshot | string | Captured at open so the case remains readable after the profile purges |

**Identity gate at verdict time (ADM-03):** the `approve` verdict is refused unless `identity_document.verification_status = passed` for the referenced document **and** the duplicate-ID check (queries section) returns no other active account. Both are evaluated at the moment of verdict, never cached on this row — so a duplicate resolved elsewhere (the other account deleted) unblocks automatically, and a document failed in a later episode blocks automatically.

**Verdict effects, by kind:**

| Verdict | kind = `initial` | kind = `revision` |
|---|---|---|
| `approve` | `ostad_profile.approval_status → approved` | `profile_revision.status → approved` (OSP-DM publish path) |
| `request_changes` | `approval_status → changes_requested`; Ostad amends and resubmits | **`profile_revision` stays `pending` and editable** — the Ostad amends the *same* revision (OSP-DM's amend-in-place rule); resubmission opens a **new** `review_case` pointing at the same revision row |
| `reject` | `approval_status → rejected` | `profile_revision.status → rejected`; the pending change is discarded and `ostad_profile` is untouched |

Every verdict resolves the case (`status → resolved`). A resubmission always opens a new case (ADM-05), never reopens one, so verdict history is the plain list of cases per profile.

## admin_account and admin_session

| admin_account field | Type | Rules |
|---|---|---|
| id / email | uuid / string | Provisioned manually — no registration path (ADM-20) |
| password_hash | string | Argon2id/bcrypt (NFR-05) |
| totp_secret_ref | encrypted ref | **Required for login** (CL-018, NFR-05) |
| active | boolean | Deprovisioning is a manual admin action; deactivated admins cannot authenticate |
| created_at / last_login_at | timestamps | |

`admin_session` follows REG-DM's `auth_session` pattern (id, admin_account_id, device_label, created_at, last_seen_at, revoked_at) with `admin_account` as the principal. The 24-hour inactivity expiry (ADM-20) is enforced by comparing `last_seen_at` at session-check time. Single permission tier in MVP — no role/permission fields, per the Overview's authorization model (static roles; RBAC deferred to post-MVP admin tiers).

## moderation_action

The single record behind every warn, suspend, and reinstate (ADM-08) — `user_account.suspension_reason_ref` (REG-DM) points here.

| Field | Type | Rules |
|---|---|---|
| id / target_account_id | uuid / uuid → user_account | |
| action_type | enum: `warn` \| `suspend` \| `reinstate` | |
| reason | text | **Internal** — the admin's record of why; required; never shown to the user |
| user_message | text, nullable | **User-facing** — the text delivered to the account; **required for `warn`**, optional for suspend (the suspension-notice screen shows it if present) |
| related_report_id | uuid, nullable → report (RNT) | Set when the action resolves a report |
| actor_admin_id | uuid → admin_account | |
| created_at | timestamp | |

Suspend/reinstate additionally toggle `user_account.status` (REG-DM) in the same transaction; warn does not change account status.

## skill_category

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| name_en / name_bn | string | Bilingual (CL-013); both required |
| active | boolean | Deactivated categories excluded from selection (ADM-11) but remain on existing `skill_entry` rows until next edit |
| created_at / updated_at | timestamps | Renames propagate by reference — `skill_entry.category_id` is a live foreign key; no denormalized copies exist |

Usage counts (ADM-11) are computed from `skill_entry` at read time, not stored.

## admin_area

The shared administrative-geography dataset OSP-02 and SGP-02 both reference — **owned here**, closing the dependency noted in `OL-OSP-DM-001`. Seed data, not user-generated.

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| level | enum: `division` \| `district` \| `thana` \| `postal_code` | |
| parent_id | uuid, nullable, self-referencing | Division → District → Thana cascade; postal codes attach to a Thana |
| name_en / name_bn | string | Bilingual (CL-016); both required |

**Labeled assumption:** attaching each postal code to a single Thana is a seed-dataset simplification. Bangladesh Post's codes follow post offices, and some straddle thana boundaries; the seed dataset assigns each code to its predominant Thana. This affects dropdown filtering only, never correctness of the stored address.

**Update to the Data Model Overview:** `admin_area` is added to the entity ownership map (owner: ADM; referenced by: OSP, SGP) in the same push as this document.

## broadcast

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| segment | enum: `all` \| `ostads` \| `shagreds` | |
| title / body | string / text | |
| sender_admin_id | uuid → admin_account | |
| sent_at | timestamp | |
| recipient_count | int | Snapshot at send time |

## admin_audit_entry

Append-only at the storage level (NFR-05) — no update or delete path exists in any interface, dashboard or API.

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| actor_admin_id | uuid → admin_account | |
| action_type | enum | Every ADM-17 category: `verdict`, `identity_mark`, `warn`, `suspend`, `reinstate`, `category_change`, `report_resolution`, `content_removal`, `support_reply`, `support_resolution`, `broadcast_sent`, `identity_document_viewed`, `chat_context_viewed`, `retention_purge` |
| target_type / target_id | string / uuid | Polymorphic reference to the affected entity |
| metadata | json | Whatever makes the action reconstructable — the verdict and note, the identity mark value, the category diff, the purge scope |
| created_at | timestamp | The only timestamp; no updated_at, by design |

## Retention behavior (OL-RET-001 mapping)

| Entity | Retention |
|---|---|
| review_case | **2 years after resolution** (moderation evidence). When the referenced profile or identity document purges at day 30, `ostad_profile_id` and `identity_document_id` are **nulled**; the row survives on `profile_display_name_snapshot` and the verdict fields. The two promises — 30-day purge and 2-year evidence — coexist because the case keeps only the verdict record, never the identity data |
| moderation_action | Retained while the related suspension/ban stands; otherwise 2 years, aligned with reports. `target_account_id` retained (it is the banned-account exception's anchor) |
| admin_audit_entry | **3-year rolling retention**, independent of any account's deletion — the accountability record survives the account it describes |
| skill_category / admin_area | Not user data; no purge schedule — managed by admin lifecycle (deactivation, not deletion) |
| broadcast | Retained indefinitely as a low-volume operational record; no PII beyond the admin author |
| admin_account / admin_session | Retained while active; sessions purge on revocation + 90 days |

## Queries this model must serve

The review queue (`review_case where status = open`, oldest first, ADM-02); the **identity-duplicate check** — `identity_document.id_number` matched across accounts where `user_account.status = active`, excluding the case's own account — run at case open (to flag on the review screen) and again at verdict time (to enforce); the reports queue (RNT's `report` joined to reporter/reported context); category typeahead source for OSP-04/MAP-06 (`skill_category where active`, both scripts); administrative-area cascades for OSP-02/SGP-02 (`admin_area` by level + parent); the audit-log viewer's filters (actor, action_type, target, date range); dormancy analytics distinguishing paused (OSP) from suspended (`user_account.status`) from genuinely inactive; the reconciliation check that the latest resolved `initial` or identity-changing case for a profile agrees with `identity_document.verification_status`.
