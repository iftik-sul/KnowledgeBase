---
project: OstadLagbo
module: registration-and-verification
type: data-model
status: current
updated: 2026-09-13
id: OL-REG-DM-001
derived_from: /OstadLagbo/modules/registration-and-verification/requirements/registration-requirements.md
owner: Iftikher
---

# Registration & Verification — Data Model

Entities owned: `user_account`, `otp_request`, `auth_session`, `device_push_token`, `consent_record`, `identity_document`, `onboarding_progress`. Conventions per [Data Model Overview](/OstadLagbo/data-model-overview.md). Revised 2026-09-13 after the cross-layer review: termination path (CL-019), locale, push tokens, identity-document cardinality, consent retention.

## user_account

The identity spine. One row per person; role-specific profiles hang off it one-to-one.

| Field | Type | Rules |
|---|---|---|
| id | uuid | PK |
| role | enum: `ostad` \| `shagred` | Immutable after creation (REG-01) |
| phone | string (BD mobile, normalized) | **Unique among non-purged accounts**; login identifier (REG-02) |
| phone_verified_at | timestamp | Set by OTP success; account cannot exist without it |
| password_hash | string | Hashed only, never plaintext (REG-03) |
| date_of_birth | date | 18+ enforced at creation, server-side; internal visibility |
| email | string, nullable | Unique among verified; see email_verified_at |
| email_verified_at | timestamp, nullable | Null = unverified; unverified emails excluded from uniqueness, reveal (OFR-04), and recovery (REG-04) |
| preferred_locale | enum: `en` \| `bn` | Chosen at first launch, switchable in settings (CL-016). **Every push notification and broadcast is rendered in this locale** — the reason it must be stored, not just held on-device |
| status | enum: `active` \| `pending_deletion` \| `suspended` \| `purged` | State machine below |
| suspended_at / suspension_reason_ref | timestamp / uuid → moderation_action | Set only by ADM-08 |
| banned_at | timestamp, nullable | Set only by the `terminate` moderation action (CL-019, ADM-DM). Non-null on a tombstone triggers the banned-account retention exception |
| deleted_at | timestamp, nullable | Deletion-request moment (self-service) **or** termination moment; starts the 30-day window either way |
| purge_at | timestamp, nullable | deleted_at + 30d; executed by retention tooling (ADM-18) |
| legal_hold | boolean, default false | Suspends purge (OL-RET-001) |
| created_at / updated_at | timestamps | |

**Status machine:**

```
active ──(self-service deletion, REG-12)──► pending_deletion ──(login within 30d)──► active
                                                    └──(day 30, no legal_hold)──► purged
active ◄──(suspend / reinstate, ADM-08)──► suspended
suspended ──(terminate, CL-019: sets banned_at, deleted_at, purge_at)──► suspended [30-day appeal window] ──(day 30)──► purged
```

Termination does not change `status` — the account remains `suspended` (so rule 7's appeal path stays open and nothing else does) while `purge_at` runs. A successful appeal is `reinstate`, which clears `banned_at`, `deleted_at`, and `purge_at`. A suspended account **cannot** self-delete (settings are unreachable; SUP-DM's exception permits only appeals) — termination is the only route from `suspended` to `purged`.

**Tombstones:** a `purged` row retains only `id`, `role`, `purged_at`, `banned_at`, and `preferred_locale` (harmless, and it lets any post-purge notice render correctly). Everything else is erased. Foreign references from persisting records (connections, ratings, reports, tickets) stay valid against the tombstone (Overview: tombstone references). A tombstone with `banned_at` set additionally retains `phone` and a legal-name copy (from the profile, captured at purge) per the banned-account exception; the retained ID number lives on `identity_document`, below — not here.

## otp_request

| Field | Type | Rules |
|---|---|---|
| id / phone / purpose | uuid / string / enum: `signup` \| `password_reset` \| `phone_change` | |
| code_hash | string | Never the code itself |
| expires_at / attempts / consumed_at | timestamp / int / timestamp | 5-min expiry, 5 attempts, single consumption (REG-02 defaults) |
| created_at | timestamp | Rate limits computed over this (5/number/24h) |

Retention: rows purge at 90 days (OL-RET-001).

## auth_session

| Field | Type | Rules |
|---|---|---|
| id / account_id | uuid / uuid | Multi-device permitted (REG-05) |
| device_label / created_at / last_seen_at | string / timestamps | |
| revoked_at | timestamp, nullable | Set by logout, password change (REG-06), suspension, deletion request, termination |

Engineering note: a managed auth provider may subsume this entity; the *behaviors* (multi-device, revoke-on-password-change, revoke-on-suspension) are the requirement, not the table itself.

## device_push_token

The delivery address for every push notification (OFR-03, REG-11 status pushes, SUP-03 replies) and broadcast (ADM-16). Without this entity the platform has nothing to send to.

| Field | Type | Rules |
|---|---|---|
| id / account_id | uuid / uuid → user_account | |
| session_id | uuid, nullable → auth_session | The session that registered it; revoking the session revokes the token |
| platform | enum: `android` \| `ios` | |
| token | string | The platform push token; **treated as a secret** — never logged, never served to any user |
| created_at / last_refreshed_at | timestamps | Platforms rotate tokens; refresh updates in place |
| revoked_at | timestamp, nullable | Set by logout, session revocation, suspension, deletion request, termination |

**Delivery rule:** a notification is sent to every non-revoked token of the recipient account, rendered in `user_account.preferred_locale`. Broadcasts (ADM-16) resolve a segment to accounts, then accounts to active tokens; `recipient_count` on the broadcast is the count of accounts, not tokens. Suspended accounts receive **only** appeal-ticket notifications (rule 7); pending-deletion accounts receive none.

## consent_record

Append-only (REG-13). One row per acceptance event.

| Field | Type | Rules |
|---|---|---|
| id / account_id | uuid / uuid | |
| tos_version / privacy_version | string / string | Document versions accepted |
| method | enum: `registration` \| `re_acceptance` | |
| accepted_at | timestamp | |

An account must have ≥1 registration-method row; material policy changes create re_acceptance rows. Never edited or deleted by any interface. **Retention: 3 years after the account purges** (OL-RET-001) — proof of lawful basis under the PDPA, referencing the tombstone.

## identity_document

The vault. Encrypted at rest; internal visibility; every read audit-logged (ADM-17).

**Cardinality: many rows per account over time.** Each submission or resubmission (initial onboarding, or a key-field revision that resubmits documents — OSP-DM) inserts a **new** row; rows are never edited after submission. Exactly one row per account is **current** (`superseded_at IS NULL`); submitting a new document sets `superseded_at` on the previous current row. ADM-DM's `review_case.identity_document_id` and OSP-DM's `profile_revision.proposed_identity_document_id` reference specific rows.

| Field | Type | Rules |
|---|---|---|
| id / account_id | uuid / uuid | Ostad accounts only |
| doc_type | enum: `nid` \| `passport` \| `driving_licence` | CL-017 |
| id_number | string, encrypted | **Flagged on match with another active account's current document** (REG-10/ADM-03 duplicate gate, evaluated at case open and verdict — ADM-DM) |
| front_image_ref / back_image_ref / selfie_ref | storage refs | Per-type image rule: nid and driving_licence require front + back; passport requires photo page (front) only. Selfie is **live in-app capture only, holding the document** (REG-10/CL-017). All encrypted objects |
| submitted_at | timestamp | |
| superseded_at | timestamp, nullable | Null = the account's current document |
| verification_status | enum: `pending` \| `passed` \| `failed` | **Canonical identity state** (Overview rule 6). Set only by ADM-03's reviewer action; `passed` on the current row is a precondition of approval |
| purge_at | timestamp, nullable | Account purge day: images + refs erased on **every** row for the account |
| id_number_retained_until | timestamp, nullable | **Set on the current row only** at purge: purge + 12 months. The number alone survives on that one row for abuse tracing (OL-RET-001), then is erased; superseded rows lose their number at purge. A tombstone with `banned_at` keeps a **hash** of the number on the same row for as long as the ban stands |
| legal_hold | boolean | |

## onboarding_progress

| Field | Type | Rules |
|---|---|---|
| account_id | uuid, PK | Ostads only |
| current_stage | int 1–6 | Fixed wizard order (REG-09); stage N requires 1…N-1 complete |
| stages_completed | per-stage timestamps | Resume point = first incomplete |
| last_activity_at | timestamp | Drives 90-day abandoned-draft purge with prior notice (OL-RET-001) |
| submitted_at | timestamp, nullable | Sets `ostad_profile.approval_status = pending` (OSP-DM) and opens an ADM `review_case` of kind `initial` |

## Retention behavior (OL-RET-001 mapping)

| Entity | On account deletion / termination | Schedule |
|---|---|---|
| user_account | `pending_deletion` (or terminated-suspended) → tombstone at day 30; banned tombstones retain phone + legal-name copy while the ban stands | 30d window |
| identity_document | Images/refs purged on all rows at day 30; the current row's `id_number` retained 12 months then erased (hash retained on banned tombstones) | 30d + 12mo |
| device_push_token | Revoked at deletion request or termination; purged with the account | 30d |
| auth_session | Revoked at deletion request or termination; purged with the account | 30d |
| otp_request | Independent of account | 90d rolling |
| consent_record | Retained 3 years after purge, then erased | 3y |
| onboarding_progress | Purged with account; abandoned drafts purged at 90d inactivity | 30d / 90d |

## Queries this model must serve

Login by phone (unique index); OTP rate-limit windows per phone; the current identity document per account (`superseded_at IS NULL`); duplicate-ID check across current documents of active accounts; recovery-window detection at registration (phone → pending_deletion account); purge-due scans (both deletion paths) for retention tooling; active push tokens per account for notification delivery, and segment → accounts → tokens for broadcasts; locale lookup per account for every outbound notification; consent version lookup per account (ADM-10); supply-funnel stage counts from onboarding_progress (ADM-12); banned-tombstone re-registration check (phone and ID-number hash against `banned_at IS NOT NULL` tombstones, at registration and at identity submission).
