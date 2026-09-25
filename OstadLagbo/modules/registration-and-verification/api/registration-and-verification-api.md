---
project: OstadLagbo
module: registration-and-verification
type: api
status: current
updated: 2026-09-25
id: OL-REG-API-001
derived_from: /OstadLagbo/modules/registration-and-verification/requirements/registration-and-verification-requirements.md
owner: Iftikher
---

# Registration & Verification — API

Endpoints for accounts, authentication, onboarding, identity capture, consent, uploads, analytics ingestion, health, and device registration. Conventions per [API Overview](/OstadLagbo/api-overview.md); entities per [REG Data Model](/OstadLagbo/modules/registration-and-verification/data-model/registration-and-verification-data-model.md). Stage payloads for onboarding stages 1, 3, and 5 (profile fields) are defined in the OSP api; stage 4 (location) in the MAP api; this document owns the wizard itself, stage 2 (identity), and the cross-cutting shared endpoints (uploads, analytics events, health).

## Endpoints — authentication

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `POST /v1/auth/register/start` | Guest. Rate-limited per IP and per phone (REG-02) | `role` (ostad\|shagred), `phone` (BD mobile, normalized server-side), `password` (REG-03 rules), `date_of_birth`, `preferred_locale` (en\|bn, REG-14), `consent: { tos_version, privacy_version }` (REG-13, must equal the current versions) | `{ registration_id, otp_expires_at, resend_available_at }`. Creates a `pending_registration` (REG-DM: password hashed immediately, 15-minute expiry) and sends the signup OTP. **No account exists yet** | `validation_failed` (under 18 → `details.date_of_birth = "under_18"`; stale consent → `details.consent = "outdated"`); `conflict` (phone in use by a live account); `account_recoverable` (phone inside a deletion window — the client routes to login); `rate_limited`. Revealing account existence here is deliberate and unavoidable (API Overview → account existence) |
| `POST /v1/auth/register/resend` | Guest | `registration_id` | `{ otp_expires_at, resend_available_at }` | `rate_limited` (5 per number per 24 h); `state_conflict` (pending registration expired — start again) |
| `POST /v1/auth/register/verify` | Guest | `registration_id`, `otp` | `{ session: { access_token, refresh_token, expires_at }, account: <account summary> }` — **the account is created here**, in one transaction: Supabase Auth user, `user_account`, the first `consent_record` (method `registration`), and, for Ostads, `onboarding_progress` at stage 1; the `pending_registration` row is deleted in the same transaction | `validation_failed` (wrong code; `details.attempts_remaining`); `locked_out` (5 wrong attempts invalidates the code); `state_conflict` (expired code or pending registration — resend or start again) |
| `POST /v1/auth/login` | Guest. Lockout keyed on the submitted phone string | `phone`, `password` | `{ session, account }`. **If the account was `pending_deletion`, login recovers it** (REG-02): status → active, `account.recovered = true`. **If suspended**, login succeeds into a **restricted session** with `account.status = "suspended"` and `account.suspension_notice` — the client shows only the notice screen and the appeal path | `unauthorized` (one message whether phone or password is wrong); `locked_out` (5 failures / 15 min per phone string, whether or not an account exists — REG-05) |
| `POST /v1/auth/refresh` | Any session | `refresh_token` | `{ session }` (a restricted session refreshes as restricted) | `unauthorized` (revoked or expired) |
| `POST /v1/auth/logout` | Any session, incl. restricted | — (optionally `all_devices: true`) | `204` — revokes this `auth_session` (or all) and its `device_push_token` rows | — |
| `POST /v1/auth/password/reset/start` | Guest | `phone` | `{ otp_expires_at, resend_available_at }` — **always 200**, identical for known and unknown numbers; an OTP is sent only if an active account exists | `rate_limited` |
| `POST /v1/auth/password/reset/verify` | Guest | `phone`, `otp`, `new_password` | `204` — old password invalid immediately; all sessions revoked (REG-06) | `validation_failed`; `locked_out`; `state_conflict` |

**Account summary** (returned by register/verify, login, refresh, and `GET /v1/me`):

```
{ id, role, status, preferred_locale,
  phone,                                   // full number — it is the owner's own data
  email, email_verified,
  consent_current,                         // false → client shows the re-acceptance notice (REG-13)
  banned_at?, suspension_notice?, recovered?,
  ostad?:   { approval_status, onboarding: { current_stage, submitted } },
  shagred?: { profile_complete } }
```

Never in the summary: date of birth, password hash, identity data. For a restricted session, only `id`, `role`, `status`, `preferred_locale`, `banned_at`, and `suspension_notice` are returned.

## Endpoints — the authenticated account (`/v1/me`)

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `GET /v1/me` | Any session (restricted sessions get the reduced summary) | — | account summary | — |
| `PATCH /v1/me/password` | Active user | `current_password`, `new_password` | `204` — other sessions revoked (REG-06) | `unauthorized` (current password wrong); `validation_failed` |
| `PATCH /v1/me/locale` | Any session, incl. restricted | `preferred_locale` | `204` — applies to all subsequent responses and notifications (REG-14) | `validation_failed` |
| `POST /v1/me/phone/change/start` | Active user | `new_phone` | `{ otp_expires_at, resend_available_at }` — OTP goes to the **new** number (REG-07) | `conflict` (number belongs to another live or recoverable account — reported only to this authenticated caller); `rate_limited` |
| `POST /v1/me/phone/change/verify` | Active user | `otp` | account summary with the new phone; old number released | `validation_failed`; `locked_out` |
| `POST /v1/me/email` | Active user | `email` | `{ verification_sent: true }` — stored unverified (REG-04) | `conflict` (email verified on another account); `validation_failed` |
| `POST /v1/me/email/verify` | Active user | `code` | account summary with `email_verified = true` | `validation_failed`; `state_conflict` (expired) |
| `DELETE /v1/me/email` | Active user | — | `204` | — |
| `POST /v1/me/consent` | Active user | `tos_version`, `privacy_version` | `204` — appends a `consent_record` (method `re_acceptance`, REG-13); `consent_current` becomes true | `validation_failed` (not the current versions) |
| `DELETE /v1/me` | Active user (a suspended user cannot self-delete; REG-DM) | `password` (re-confirmation) | `204` — status → `pending_deletion`, `purge_at` set; every session and push token revoked; pending offers resolved (OFR-DM); threads freeze via predicate. Logging in within 30 days recovers | `unauthorized` (password wrong); `suspended` |
| `POST /v1/me/push-tokens` | Active user, **or a restricted session** (so appeal replies reach a suspended user — REG-DM) | `platform` (android\|ios), `token` | `{ id }` — upsert: the same token refreshes in place; bound to the calling session | `validation_failed` |
| `DELETE /v1/me/push-tokens/{id}` | Owner | — | `204` | `not_found` |

## Endpoints — Ostad onboarding wizard (REG-09)

All require an Ostad whose `approval_status` is `draft`, `changes_requested`, or `rejected` — not currently in review and not approved. Approved Ostads edit through the OSP api, which routes key fields to a revision. Stage order is enforced server-side: writing stage *n* requires stages 1…*n−1* complete; completed stages may be re-written before submission (REG-09).

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `GET /v1/onboarding` | Ostad (draft states) | — | `{ current_stage, stages: [ { n, complete_at } ], resume_stage, submitted_at, last_verdict: { verdict, note, at }? }` — `last_verdict` carries the admin's note after `changes_requested`/`rejected` (REG-11) | `forbidden` (Shagred, or Ostad in review/approved) |
| `PUT /v1/onboarding/stages/1` | Ostad | Personal-information payload — **fields per OSP api** | `{ current_stage }` | `validation_failed` |
| `PUT /v1/onboarding/stages/2` | Ostad; stage 1 complete | Identity capture (below) | `{ current_stage }` | see below |
| `PUT /v1/onboarding/stages/3` | Ostad; stages 1–2 complete | Address payload — **fields per OSP api** (chain validity enforced) | `{ current_stage }` | `validation_failed` (`details.address = "invalid_chain"`) |
| `PUT /v1/onboarding/stages/4` | Ostad; stages 1–3 complete | Location payload — **fields per MAP api** | `{ current_stage }` | `validation_failed` |
| `PUT /v1/onboarding/stages/5` | Ostad; stages 1–4 complete | Professional payload — **fields per OSP api** (skills 1–5, education, experience, portfolio via upload ids) | `{ current_stage }` | `validation_failed` |
| `POST /v1/onboarding/submit` | Ostad; stages 1–5 complete | — | `{ approval_status: "pending", submitted_at }` — sets `approval_status = pending` and `onboarding_progress.submitted_at`, opens an ADM `review_case` of kind `initial` referencing the draft identity row (which freezes it — REG-DM), emits the funnel event | `state_conflict` (a stage incomplete — `details.incomplete_stages`) |

Every stage write saves immediately (REG-09). After `changes_requested` or `rejected`, the stages re-open for editing and `submit` opens a new review case (ADM-05, unlimited).

### Stage 2 — identity capture (REG-10, CL-017)

`PUT /v1/onboarding/stages/2` body:

```
{ doc_type: "nid" | "passport" | "driving_licence",
  id_number,
  front_upload_id, back_upload_id?,        // back required for nid and driving_licence; must be absent for passport
  selfie_upload_id }                        // must be an upload ticket issued with purpose "identity_selfie"
```

**Server validation:** image requirements per type; every `upload_id` must exist, be unconsumed, and carry the matching purpose. The selfie ticket's purpose is `identity_selfie`, which the app requests **only from its in-app live-capture flow** — the client closes the gallery path, and that is the primary guard. Server-side, an image is an image: the API additionally rejects a selfie whose file metadata indicates a gallery origin where the platform exposes it, as a **backstop only**, and the live-capture rule's real enforcement at review time is the three-way face ↔ document photo ↔ document-in-hand check (ADM-03).

**Draft replacement (REG-DM):** if the account already has a **draft** identity row (one no `review_case` references yet), this write **replaces it in place and deletes its image objects in the same operation** — retaking a blurry photo never leaves the old one in the vault. If the account's latest row is frozen (already reviewed), this write creates a new draft row. On every write the duplicate-ID check runs; a match flags the row for review (REG-10) — the Ostad is **not** told (a duplicate is either their own mistake or fraud; either way the admin decides).

Errors: `validation_failed` (`details.images = "back_required" | "back_not_allowed"`, `details.selfie = "invalid_ticket"`); `state_conflict` (stage 1 incomplete).

## Endpoints — uploads (shared by all modules)

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `POST /v1/uploads` | Active user; purposes are role-checked (identity and portfolio purposes Ostad-only). **A restricted session may request `ticket_attachment` only** (appeal screenshots, rule 7) | `purpose` (profile_photo \| identity_front \| identity_back \| identity_selfie \| portfolio_image \| portfolio_video \| portfolio_document \| voice_note \| ticket_attachment), `content_type`, `size_bytes`, `duration_seconds?` (video/voice) | `{ upload_id, url, method: "PUT", headers, expires_at }` — a signed URL to Supabase Storage, valid minutes, single-use | `validation_failed` (type/size/duration outside NFR-04 / OSP-07 / OFR-05 limits — refused **before** any bytes move); `forbidden` (purpose not permitted for the caller); `suspended` (restricted session asking for any other purpose); `rate_limited` |

An upload ticket is consumed exactly once by the endpoint that references its `upload_id`; unconsumed tickets expire and their objects are swept (ADM-18). The API re-validates the stored object at consumption.

## Endpoints — analytics events & health (shared)

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `POST /v1/events` | Any session or **guest** (a pseudonymous `session_id`; no auth required — client analytics must work before login, NFR-06); rate-limited per IP and per account | `{ events: [ { name, ts, session_id, props } ] }` — a batch of **client-side events only** (map sessions, searches, zero-result searches, share taps, screen views; API Overview → analytics). The API validates each against the **event catalog**, **strips any disallowed property** and coarsens area to thana/grid (never phone, name, or precise coordinates — NFR-06, MAP-DM), then writes accepted events to the analytics store (ADR-002) | `204` — the batch is accepted; an individually invalid event is dropped, not failed, so one bad event never loses the batch | `validation_failed` (malformed envelope); `rate_limited` |
| `GET /v1/health` | Anyone, unauthenticated | — | `{ status: "ok" }` — for uptime monitoring (NFR-09); no auth, no body | — |

**Server-side events are never posted here.** Ostad profile views (OSP), offer/connection/message/phone-reveal events (OFR), rating/report/block events (RNT), verdicts and moderation (ADM), and ticket events (SUP) are written by the API itself at the moment of the action — `POST /v1/events` carries only what the client observes (API Overview → analytics events). Both streams land in the same ADR-002 store and feed ADM-12…15.

## Endpoints — legal documents (guest-reachable)

| Endpoint | Caller & policy check | Request | Response |
|---|---|---|---|
| `GET /v1/legal/versions` | Anyone | — | `{ tos_version, privacy_version, effective_at }` — what `register/start` and `/me/consent` must send |
| `GET /v1/legal/terms` · `GET /v1/legal/privacy` | Anyone; `Accept-Language` | — | The document text in the requested language (REG-13, MAP-03; the same content the public website serves, CL-020) |

## Flows

**Registration.** `register/start` — validates 18+, consent versions, and the phone; stores a `pending_registration`; sends the OTP through the SMS gateway (ADR-001) → `register/verify` — one transaction: Supabase Auth user created with the server's credential, `user_account` with `preferred_locale`, `consent_record`, `onboarding_progress` for Ostads, pending registration deleted → session returned. The 18+ gate and consent are checked **before** the OTP is sent, so no SMS is spent on a registration that cannot complete and no partial account ever exists (REG-03 acceptance).

**Ostad onboarding.** `GET /v1/onboarding` on every app open → resume at `resume_stage` → `PUT` stages in order (re-writes replace, never accumulate) → `submit`. After a verdict, `GET /v1/onboarding` shows `last_verdict` and the stages re-open.

**Deletion and recovery.** `DELETE /v1/me` → `pending_deletion`, no sessions → any `POST /v1/auth/login` within 30 days recovers (REG-02, CL-015); `register/start` with that phone during the window returns `account_recoverable` and the client offers the login screen.

**Suspension.** `login` succeeds into a restricted session → the client renders `suspension_notice`, registers a push token, and offers the appeal → the only calls that succeed are the SUP api's ticket endpoints (create an appeal, and read or reply to any ticket the account owns), a `ticket_attachment` upload, `PATCH /v1/me/locale`, push-token registration, and `logout` (Data Model Overview rule 7). Direct Realtime and Storage access is refused by RLS.

## What this module does not expose

No endpoint returns a date of birth, a password hash, an OTP code, another user's phone or email (OFR's contact reveal is the only path, in the OFR api), an identity document or selfie to any user (admin-only, ADM api, audit-logged), a pending registration's contents, whether a given phone number has an account outside registration itself (API Overview → account existence), or whether a duplicate-ID flag was raised. `POST /v1/events` accepts only client-observable events and never a viewer's precise coordinates, phone, or name (NFR-06).
