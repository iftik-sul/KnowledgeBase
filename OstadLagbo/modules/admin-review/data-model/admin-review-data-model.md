---
project: OstadLagbo
module: admin-review
type: data-model
status: current
updated: 2026-09-24
id: OL-ADM-DM-001
derived_from: /OstadLagbo/modules/admin-review/requirements/admin-review-requirements.md
owner: Iftikher
---

# Admin Review & Dashboard — Data Model

Entities owned: `admin_account`, `admin_session`, `review_case`, `moderation_action`, `skill_category`, `admin_area`, `broadcast`, `admin_audit_entry`. Conventions per [Data Model Overview](/OstadLagbo/data-model-overview.md). `report` and `support_ticket` are owned by `ratings-and-trust` and `support` respectively; this document only defines how ADM queues and acts on them. Revised 2026-09-13 after the cross-layer review: `terminate` action (CL-019); active-suspension derivation; duplicate check against current documents. Revised 2026-09-24 after the ADM api review: appeal-linked reinstatement; selfie shown for photo-only revisions; identity-view rate limiting.

## review_case — the record, not the gate

`ostad_profile.approval_status` (OSP) remains the **canonical publishing gate**, exactly as OSP-DM declared, and `identity_document.verification_status` (REG) remains the **canonical identity state**. This model duplicates neither. `review_case` is the **workflow record**: one row per review episode, whether the Ostad's first submission or a later key-field re-review. What was decided about identity, and by whom, is recorded by the audit log (`identity_mark` entries, ADM-17), not by a second copy of the status here.

| Field | Type | Rules |
|---|---|---|
| id / ostad_profile_id | uuid / uuid, nullable after purge | See retention |
| kind | enum: `initial` \| `revision` | `initial` reviews the whole profile (REG-11); `revision` reviews a `profile_revision` (OSP-DM) |
| profile_revision_id | uuid, nullable → profile_revision | Set iff kind = `revision` |
| identity_document_id | uuid, nullable → identity_document | The specific document row under review (REG-DM: many rows per account); nullable after purge (see retention) |
| identity_recheck_required | boolean | `true` for every `initial` case, and for `revision` cases whose revision changes legal names or identity documents; `false` for skills-only revisions, which carry the existing passed status forward without re-examination |
| photo_recheck_required | boolean | `true` when the revision changes the profile photo (CL-021). A photo change is an **identity-grade** judgment — the reviewer compares the proposed photo against the account's current identity selfie — so **the review screen always surfaces the current selfie when this is true**, even for a photo-only revision that needs no document recheck |
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

**Identity-view rate limiting (NFR-05, ADM api review).** Issuing a signed URL to a vault object (identity document or selfie) is rate-limited **per admin session** — a small number per minute (engineering default) — and every issuance is an `identity_document_viewed` audit entry. This is the structural guard against a single compromised admin token paging through every NID: the audit log records a breach, but the rate limit and the operations-view spike alert (ADM-15/19) make mass exfiltration slow and visible rather than silent. It bounds the blast radius of the one credential the whole vault trusts.

## moderation_action

The single record behind every warn, suspend, reinstate, and terminate (ADM-08, CL-019) — `user_account.suspension_reason_ref` (REG-DM) points here.

| Field | Type | Rules |
|---|---|---|
| id / target_account_id | uuid / uuid → user_account | |
| action_type | enum: `warn` \| `suspend` \| `reinstate` \| `terminate` | |
| reason | text | **Internal** — the admin's record of why; required; never shown to the user |
| user_message | text, nullable | **User-facing** — the text delivered to the account; **required for `warn` and `terminate`** (the user must be told they are banned and may appeal), optional for suspend (the suspension-notice screen shows it if present) |
| related_report_id | uuid, nullable → report (RNT) | Set when the action resolves a report |
| resolves_appeal_ticket_id | uuid, nullable → support_ticket | **Reinstate only:** set when the reinstatement resolves an appeal (ADM api). The API closes that appeal ticket in the same transaction and tags this record as appeal-driven, so quality analytics (ADM-15) can distinguish a successful appeal from a suspension lifted for another reason |
| actor_admin_id | uuid → admin_account | |
| created_at | timestamp | |

**Effects, in the same transaction as the row insert:**

| Action | Effect on `user_account` (REG-DM) | Other effects |
|---|---|---|
| `warn` | none | Delivers `user_message`; audit `warn` |
| `suspend` | `status → suspended`, `suspended_at`, `suspension_reason_ref` | Sessions and push tokens revoked; pending offers frozen (OFR-DM); audit `suspend` |
| `reinstate` | `status → active`; clears `suspended_at`, `suspension_reason_ref`, **and** `banned_at` / `deleted_at` / `purge_at` if a termination was pending | Resolves `resolves_appeal_ticket_id` if present; audit `reinstate`. Reinstating a terminated account is the outcome of a successful appeal |
| `terminate` | If not already suspended, suspends first (same effects as `suspend`); then sets `banned_at`, `deleted_at = now`, `purge_at = now + 30d` — status **remains `suspended`** through the appeal window (Overview rule 7) | Pending offers resolved with `resolution_source = deletion` (OFR-DM); at `purge_at`, the retention job purges under the banned-account exception (OL-RET-001); audit `terminate` |

**Active suspension is derived, not stored** (Overview: predicates over flags): an account is under an active suspension iff its latest `suspend` or `terminate` action has no later `reinstate`. `user_account.status = suspended` is the canonical state (rule 6); this derivation exists so SUP-DM's appeal linkage (`related_moderation_action_id`) resolves to *which* action is being contested — the latest `suspend`/`terminate` without a subsequent `reinstate`.

## skill_category

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| name_en / name_bn | string | Bilingual (CL-013); both required |
| active | boolean | Deactivated categories excluded from selection (ADM-11) but remain on existing `skill_entry` rows until next edit |
| created_at / updated_at | timestamps | Renames propagate by reference — `skill_entry.category_id` is a live foreign key; no denormalized copies exist |

Usage counts (ADM-11) are computed from `skill_entry` at read time, not stored. **Categories are never deleted, only deactivated** (ADM-11); deactivation is always safe because it leaves the category on existing profiles until their owners next edit skills, so no Ostad is ever stripped of a category out from under them. There is therefore no delete endpoint and no last-category hazard to guard against.

## admin_area

The shared administrative-geography dataset OSP-02 and SGP-02 both reference — **owned here**. Seed data, not user-generated.

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| level | enum: `division` \| `district` \| `thana` \| `postal_code` | |
| parent_id | uuid, nullable, self-referencing | Division → District → Thana cascade; postal codes attach to a Thana |
| name_en / name_bn | string | Bilingual (CL-016); both required |

**Labeled assumption:** attaching each postal code to a single Thana is a seed-dataset simplification. Bangladesh Post's codes follow post offices, and some straddle thana boundaries; the seed dataset assigns each code to its predominant Thana. This affects dropdown filtering only, never correctness of the stored address. Profiles storing the four ids must form a valid chain (Overview: address chain validity).

## broadcast

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| segment | enum: `all` \| `ostads` \| `shagreds` | |
| title_en / title_bn / body_en / body_bn | string / string / text / text | **Bilingual, both required** — each recipient receives the version matching `user_account.preferred_locale` (REG-DM, CL-016) |
| sender_admin_id | uuid → admin_account | |
| sent_at | timestamp | |
| recipient_count | int | Snapshot at send time: the count of **accounts** in the segment with at least one active push token, not the count of tokens |

Delivery resolves segment → active accounts (status = active) → `device_push_token` rows (REG-DM). Suspended and pending-deletion accounts are excluded from broadcasts. **A broadcast is irreversible once sent**, so the API offers a preview that returns `recipient_count` before sending (ADM api), the one confirmation step on a mass action.

## admin_audit_entry

Append-only at the storage level (NFR-05) — no update or delete path exists in any interface, dashboard or API.

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| actor_admin_id | uuid → admin_account | |
| action_type | enum | Every ADM-17 category: `verdict`, `identity_mark`, `warn`, `suspend`, `reinstate`, `terminate`, `category_change`, `report_resolution`, `content_removal`, `support_reply`, `support_resolution`, `broadcast_sent`, `identity_document_viewed`, `chat_context_viewed`, `retention_purge` |
| target_type / target_id | string / uuid | Polymorphic reference to the affected entity |
| metadata | json | Whatever makes the action reconstructable — the verdict and note, the identity mark value, the category diff, the purge scope |
| created_at | timestamp | The only timestamp; no updated_at, by design |

## Retention behavior (OL-RET-001 mapping)

| Entity | Retention |
|---|---|
| review_case | **2 years after resolution** (moderation evidence). When the referenced profile or identity document purges at day 30, `ostad_profile_id` and `identity_document_id` are **nulled**; the row survives on `profile_display_name_snapshot` and the verdict fields. The two promises — 30-day purge and 2-year evidence — coexist because the case keeps only the verdict record, never the identity data |
| moderation_action | **Retained while the related suspension or ban stands** (a `terminate` row is the banned-account exception's anchor and persists as long as the tombstone's `banned_at` does); otherwise 2 years, aligned with reports. `target_account_id` remains a valid tombstone pointer |
| admin_audit_entry | **3-year rolling retention**, independent of any account's deletion — the accountability record survives the account it describes |
| skill_category / admin_area | Not user data; no purge schedule — managed by admin lifecycle (deactivation, not deletion) |
| broadcast | Retained indefinitely as a low-volume operational record; no PII beyond the admin author |
| admin_account / admin_session | Retained while active; sessions purge on revocation + 90 days |

## Queries this model must serve

The review queue (`review_case where status = open`, oldest first, ADM-02), **excluding cases whose subject account is mid-purge** (no ghost work); the **identity-duplicate check** — `identity_document.id_number` matched across the **current** document (`superseded_at IS NULL`) of every other account where `user_account.status = active`, plus the ID-number hash of banned tombstones (REG-DM) — run at case open (to flag) and again at verdict time (to enforce); the reports queue (RNT's `report` joined to reporter/reported context), likewise excluding mid-purge subjects; the active-suspension derivation for appeals; the appeal-ticket-to-moderation-action link for reinstatement; category typeahead source for OSP-04/MAP-06 (`skill_category where active`, both scripts); administrative-area cascades and chain validation for OSP-02/SGP-02; broadcast segment resolution to active accounts and tokens, with a pre-send recipient count; the pending-abandonment list (revisions and drafts due for 90-day discard, REG-DM/OSP-DM) for the retention view; identity-view rate-limit state per admin session; the audit-log viewer's filters (actor, action_type, target, date range); dormancy analytics distinguishing paused (OSP) from suspended (`user_account.status`) from genuinely inactive; the reconciliation check that the latest resolved `initial` or identity-changing case for a profile agrees with the current document's `verification_status`.
