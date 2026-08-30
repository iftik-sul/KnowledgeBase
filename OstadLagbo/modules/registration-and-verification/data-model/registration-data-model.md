---
project: OstadLagbo
module: registration-and-verification
type: data-model
status: current
updated: 2026-08-30
id: OL-REG-DM-001
derived_from: /OstadLagbo/modules/registration-and-verification/requirements/registration-requirements.md
owner: Iftikher
---

# Registration & Verification — Data Model

Entities owned: `user_account`, `otp_request`, `auth_session`, `consent_record`, `identity_document`, `onboarding_progress`. Conventions per [Data Model Overview](/OstadLagbo/data-model-overview.md).

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
| status | enum: `active` \| `pending_deletion` \| `suspended` \| `purged` | State machine below |
| suspended_at / suspension_reason_ref | timestamp / uuid → moderation_action | Set only by ADM-08 |
| deleted_at | timestamp, nullable | Deletion request moment; starts the 30-day window |
| purge_at | timestamp, nullable | deleted_at + 30d; executed by retention tooling (ADM-18) |
| legal_hold | boolean, default false | Suspends purge (OL-RET-001) |
| created_at / updated_at | timestamps | |

**Status machine:** `active → pending_deletion` (self-service deletion; REG-12) · `pending_deletion → active` (login within 30d recovers; REG-02/CL-015) · `pending_deletion → purged` (day 30, unless legal_hold) · `active ↔ suspended` (ADM-08 only). `purged` rows retain only: id, role, `purged_at`, and — for 12 months — `id_number_retained` (below); everything else is erased. A banned-at-deletion account additionally retains phone, legal-name copy, and ID-number hash per the banned-account exception.

## otp_request

| Field | Type | Rules |
|---|---|---|
| id / phone / purpose | uuid / string / enum: `signup` \| `password_reset` \| `phone_change` | |
| code_hash | string | Never the code itself |
| expires_at / attempts / consumed_at | timestamp / int / timestamp | 5-min expiry, 5 attempts, single consumption (REG-02 defaults) |
| created_at | timestamp | Rate limits computed over this (5/number/24h) |

Retention: rows purge at 90 days (OTP request logs, OL-RET-001).

## auth_session

| Field | Type | Rules |
|---|---|---|
| id / account_id | uuid / uuid | Multi-device permitted (REG-05) |
| device_label / created_at / last_seen_at | string / timestamps | |
| revoked_at | timestamp, nullable | Set by logout, password change (REG-06), suspension, deletion |

Engineering note: a managed auth provider may subsume this entity; the *behaviors* (multi-device, revoke-on-password-change, revoke-on-suspension) are the requirement, not the table itself.

## consent_record

Append-only (REG-13). One row per acceptance event.

| Field | Type | Rules |
|---|---|---|
| id / account_id | uuid / uuid | |
| tos_version / privacy_version | string / string | Document versions accepted |
| method | enum: `registration` \| `re_acceptance` | |
| accepted_at | timestamp | |

An account must have ≥1 registration-method row; material policy changes create re_acceptance rows. Never edited or deleted; survives to purge like the account's minimal record where legally required.

## identity_document

The vault. Encrypted at rest; internal visibility; every read audit-logged (ADM-17).

| Field | Type | Rules |
|---|---|---|
| id / account_id | uuid / uuid | Ostad accounts only |
| doc_type | enum: `nid` \| `passport` \| `driving_licence` | CL-017 |
| id_number | string, encrypted | **Flagged on match with any active account's id_number** (REG-10/ADM-03 duplicate gate) |
| front_image_ref / back_image_ref / selfie_ref | storage refs | Per-type image rule: nid and driving_licence require front + back; passport requires photo page (front) only. Selfie is **live in-app capture only, holding the document** (REG-10/CL-017). All encrypted objects |
| submitted_at | timestamp | |
| verification_status | enum: `pending` \| `passed` \| `failed` | Set only by ADM-03; `passed` is a precondition of approval |
| purge_at | timestamp, nullable | account purge day: images + refs erased |
| id_number_retained_until | timestamp, nullable | purge + 12 months; the number alone survives for abuse tracing (OL-RET-001), then erased |
| legal_hold | boolean | |

## onboarding_progress

| Field | Type | Rules |
|---|---|---|
| account_id | uuid, PK | Ostads only |
| current_stage | int 1–6 | Fixed wizard order (REG-09); stage N requires 1…N-1 complete |
| stages_completed | per-stage timestamps | Resume point = first incomplete |
| last_activity_at | timestamp | Drives 90-day abandoned-draft purge with prior notice (OL-RET-001) |
| submitted_at | timestamp, nullable | Sets account into review (REG-11); creates ADM `review_case` |

## Retention behavior (OL-RET-001 mapping)

| Entity | On account deletion | Schedule |
|---|---|---|
| user_account | pending_deletion → purge at day 30; minimal banned-exception retention where applicable | 30d window |
| identity_document | images/refs purged at day 30; id_number retained 12 months then erased | 30d + 12mo |
| otp_request | independent of account | 90d rolling |
| auth_session | revoked immediately at deletion request | purged with account |
| consent_record | retained as long as any account record lawfully persists | legal basis |
| onboarding_progress | purged with account; abandoned drafts purged at 90d inactivity | 30d / 90d |

## Queries this model must serve

Login by phone (unique index); OTP rate-limit windows per phone; duplicate-ID check at submission (active accounts only); recovery-window detection at registration (phone → pending_deletion account); purge-due scans for retention tooling; consent version lookup per account (ADM-10 detail); supply-funnel stage counts from onboarding_progress (ADM-12).
