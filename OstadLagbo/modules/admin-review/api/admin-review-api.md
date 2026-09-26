---
project: OstadLagbo
module: admin-review
type: api
status: current
updated: 2026-09-26
id: OL-ADM-API-001
derived_from: /OstadLagbo/modules/admin-review/requirements/admin-review-requirements.md
owner: Iftikher
---

# Admin Review & Dashboard — API

Every endpoint the admin dashboard calls. Conventions per [API Overview](/OstadLagbo/api-overview.md); entities per [ADM Data Model](/OstadLagbo/modules/admin-review/data-model/admin-review-data-model.md). This is the largest api by surface, and the only one whose caller is the admin. Rules that govern the whole document:

1. **All endpoints are under `/v1/admin/`** and require an **admin token** (email + password + TOTP, ADM-20/CL-018). A user token here is `unauthorized`; the two families never cross (API Overview → authentication).
2. **The admin sees account ids.** This module is the stated exception to the identifier rule (API Overview → identifiers): account-level moderation is its job, so directories, detail views, and actions address accounts directly.
3. **Reads that touch sensitive data write an audit entry as a side effect.** Viewing an identity document, viewing report-cited chat context, viewing a Shagred's Ostad history (SGP-03), and every action write to `admin_audit_entry` (ADM-17). The audit is not an endpoint the admin calls; it is a consequence the API guarantees. There is **no way to read an identity document, a chat message, or a Shagred's history without the read being logged.**
4. **Vault reads are rate-limited per session.** Signed-URL issuance for identity documents and selfies is capped per admin session (ADM-DM); an unusual spike is flagged in the operations view. A single stolen admin token cannot silently exfiltrate every NID — mass reads are slow and visible.

## Admin authentication

| Endpoint | Request | Response | Errors |
|---|---|---|---|
| `POST /v1/admin/auth/login` | `email`, `password` | `{ challenge: "totp", challenge_id }` — password alone never returns a session | `unauthorized` (bad credentials, uniform message); `locked_out` (REG-05 lockout, per email) |
| `POST /v1/admin/auth/totp` | `challenge_id`, `code` | `{ session: { access_token, refresh_token, expires_at }, admin: { id, email } }` — the admin token (API Overview) | `unauthorized` (bad code); `locked_out` |
| `POST /v1/admin/auth/refresh` · `POST /v1/admin/auth/logout` | standard | `{ session }` / `204` | `unauthorized` |

Admin accounts are **provisioned out of band** (ADM-20): there is no admin registration, password-reset, or self-service endpoint in the MVP. A lost admin credential is an incident (OL-INC-001), recovered by direct database provisioning, not by an API.

## A. Overview

| Endpoint | Request | Response |
|---|---|---|
| `GET /v1/admin/overview` | — | The KPI cards (ADM-01): `{ pending_reviews, open_reports, open_appeals, ostads_by_status: {..}, shagreds_total, suspended, new_registrations: { today, week }, offers_sent_week, connections_week, open_tickets }` — counts exclude accounts mid-purge so the admin chases no ghosts (ADM-DM) — each a link to its filtered list, plus `recent_activity[]` (the newest registrations, submissions, reports, each with a deep link) |

## B. Review management

| Endpoint | Request | Response | Errors |
|---|---|---|---|
| `GET /v1/admin/reviews` | `?state=open&kind=initial\|revision&limit=&cursor=` | The queue (ADM-02), oldest first: `[ { case_id, kind, ostad: { account_id, display_name }, submitted_at, identity_recheck_required, photo_recheck_required, id_duplicate_flag } ]` | — |
| `GET /v1/admin/reviews/{case_id}` | — | The full review screen: the complete profile including internal fields; the identity documents for this case as **short-lived signed URLs to the vault** (each issuance rate-limited and writing an `identity_document_viewed` audit entry — ADM-DM, ADM-17); **the current identity selfie whenever `identity_recheck_required` or `photo_recheck_required`** (so a photo-only revision still shows the face to compare, CL-021); for a `revision` case, the field-level **diff** against the approved values; the duplicate match if any (the other account's id and status) | `not_found` |
| `POST /v1/admin/reviews/{case_id}/identity` | `verification: "passed" \| "failed"` | `204` — records the identity mark on the current `identity_document` (REG-DM, canonical state); audits `identity_mark`. May be set before the verdict | `state_conflict` (resolved) |
| `POST /v1/admin/reviews/{case_id}/verdict` | `verdict: "approve" \| "request_changes" \| "reject"`, `note` (**required** for request_changes and reject, ADM-04) | `204` — runs the verdict transaction (ADM-DM): initial sets `ostad_profile.approval_status`; revision publishes / returns / discards per OSP-DM; notifies the Ostad by push in their locale; audits `verdict` | `validation_failed` (missing note); `state_conflict` (already resolved, or **`approve` while identity is not `passed` or a duplicate is unresolved** — ADM-03: `details.reason = "identity_not_passed" \| "duplicate_unresolved"`) |

## C. Moderation

| Endpoint | Request | Response | Errors |
|---|---|---|---|
| `GET /v1/admin/reports` | `?state=open&target_type=&category=&limit=&cursor=` | The reports queue (ADM-07), oldest first: `[ { report_id, target_type, category, reporter: { account_id }, reported: { account_id, display_name }, created_at, has_cited_messages, via_offer } ]` — reporter identity is admin-only (RNT-07); mid-purge subjects excluded | — |
| `GET /v1/admin/reports/{report_id}` | — | Report detail: the report, the **reported content** inline (profile, review, reply, or — when the report carries a `via_offer_id` (a hidden-Shagred report filed through a lapsed offer, RNT/SGP) — **that offer's message as the evidence**), and for a message report the cited messages **with ±N context** (OFR-07) as signed reads — **this read audits `chat_context_viewed`** and returns only the cited window, never a browsable chat | `not_found` |
| `POST /v1/admin/reports/{report_id}/resolve` | `resolution: "dismiss" \| "warn" \| "suspend" \| "terminate" \| "remove_content"`, `internal_reason` (**required**), `user_message?` (required for `warn`) | `204` — `remove_content` sets `removed_at` and recomputes the Ostad's aggregate (RNT-DM); `warn`/`suspend`/`terminate` create a `moderation_action` (`terminate` bans the account, ADM-10/CL-019); all audit `report_resolution` (+ `content_removal`) | `validation_failed`; `state_conflict` |
| `GET /v1/admin/blocks` | `?limit=&cursor=` | The block overview (ADM-09), read-only: most-blocked accounts and recent blocks over **active** blocks (RNT-DM) | — |

## D. User management

| Endpoint | Request | Response | Errors |
|---|---|---|---|
| `GET /v1/admin/ostads` | `?status=&q=&district=&category=&sort=&limit=&cursor=` — `q` matches name, phone, or ID number (ADM-10) | `[ { account_id, display_name, approval_status, account_status, district, submitted_at } ]` | — |
| `GET /v1/admin/shagreds` | `?status=&q=&limit=&cursor=` — `q` matches name or phone | `[ { account_id, display_name, account_status, joined_at } ]` | — |
| `GET /v1/admin/accounts/{account_id}` | — | The account detail view (ADM-10): full profile **including every internal field** (street address, DOB, contact, identity metadata; identity images only via the audited, rate-limited signed-URL path); verdict history; **report history as both reporter and reported**; audit entries touching this account; **the Shagred's Ostad history if a Shagred (SGP-03, admin path — this read writes a `shagred_history_viewed` audit entry, honoring SGP's audit guarantee)**; the applicable actions | `not_found` |
| `POST /v1/admin/accounts/{account_id}/warn` | `internal_reason`, `user_message` (required) | `204` — a `moderation_action` (warn); delivers the message; audits `warn` | `state_conflict` (purged) |
| `POST /v1/admin/accounts/{account_id}/suspend` | `internal_reason`, `user_message?` | `204` — status → suspended; revokes sessions and push tokens; freezes chats; pending offers frozen; audits `suspend` | `state_conflict` (already suspended or purged) |
| `POST /v1/admin/accounts/{account_id}/reinstate` | `internal_reason`, `appeal_ticket_id?` | `204` — status → active; clears a pending termination (REG-DM); **if `appeal_ticket_id` is present, resolves that appeal ticket in the same transaction and tags the action appeal-driven** (ADM-DM); audits `reinstate` | `state_conflict` (not suspended) |
| `POST /v1/admin/accounts/{account_id}/terminate` | `internal_reason`, `user_message` (**required** — the ban notice and appeal right, ADM-08/CL-019) | `204` — the termination transaction (REG-DM/ADM-DM): suspends if not already, sets `banned_at`/`deleted_at`/`purge_at`, resolves pending offers, audits `terminate`. The account keeps the 30-day appeal window | `state_conflict` (purged) |

## E. Content and taxonomy

| Endpoint | Request | Response | Errors |
|---|---|---|---|
| `GET /v1/admin/skill-categories` | `?include_inactive=true` | Every category with `usage_count` (ADM-11) | — |
| `POST /v1/admin/skill-categories` | `name_en`, `name_bn` | `{ id }` | `validation_failed`; `conflict` (name exists) |
| `PATCH /v1/admin/skill-categories/{id}` | `name_en?`, `name_bn?`, `active?` | `204` — a rename propagates by reference; `active:false` deactivates (hidden from new selection, kept on existing profiles until their next skill edit — always safe, ADM-DM). **Deletion is not offered** (ADM-11) | `state_conflict` |
| `GET /v1/admin/admin-areas` · `POST` · `PATCH` | the `admin_area` dataset (ADM-DM) | seed-data maintenance for the Division→District→Thana→postal hierarchy | — |

## F. Analytics

Charts read the **rollup tables** (ADR-002), never raw events — every response is a pre-aggregated series. All accept `?range=7d\|30d\|90d`.

| Endpoint | Response |
|---|---|
| `GET /v1/admin/analytics/connections` | ADM-12: offers sent, accepted (= connections), unique pairs, active chats, messages, phone reveals — totals and series; supply and demand funnels with stage conversions; offer-health distribution |
| `GET /v1/admin/analytics/growth` | ADM-13: registrations by role, approvals, connections as series; activation, retention, dormancy (paused distinguished from inactive — OSP-11) |
| `GET /v1/admin/analytics/demand` | ADM-14: zero/low-result searches grouped by category, script, and area; top searched vs. coverage by district and category; concentration |
| `GET /v1/admin/analytics/quality` | ADM-15: ratings distribution, review-submission rate, reports per 100 WAU, review turnaround vs. 48 h, resolution time, suspension/termination/reinstatement counts (appeal-driven reinstatements distinguished — ADM-DM), appeals pending beyond 7 days, ticket volume/resolution/reopen |
| `GET /v1/admin/analytics/operations` | OTP volume, spend estimate, rate-limit hits (ADM-19); **identity-view rate per session with a spike flag** (the vault-exfiltration tripwire, ADM-DM); the **analytics-store size indicator** (ADR-002) |

## G. Communication

| Endpoint | Request | Response | Errors |
|---|---|---|---|
| `POST /v1/admin/broadcasts?preview=true` | `segment` | `{ recipient_count }` — the resolved reach, **sending nothing** | — |
| `POST /v1/admin/broadcasts` | `segment: "all" \| "ostads" \| "shagreds"`, `title_en`, `title_bn`, `body_en`, `body_bn` (**both languages required**, CL-016/ADM-16) | `{ id, recipient_count }` — resolves the segment to active accounts, then tokens (REG-DM), delivering each recipient their locale's version; records the broadcast; audits `broadcast_sent`. Irreversible — the client is expected to confirm against the preview count first | `validation_failed` (a language missing) |
| `GET /v1/admin/broadcasts` | `?limit=&cursor=` | Past broadcasts with segment, sender, timestamp, recipient count | — |

## H. Operations and compliance

| Endpoint | Request | Response |
|---|---|---|
| `GET /v1/admin/audit` | `?actor=&action_type=&target=&from=&to=&limit=&cursor=` | The append-only audit log viewer (ADM-17): actor, action, target, timestamp, metadata. **Read-only — no write, edit, or delete endpoint exists for the audit log**, by design (append-only at storage, NFR-05) |
| `GET /v1/admin/retention` | — | Identity-document storage status per account; purge-due items; **the pending-abandonment list** — revisions and onboarding drafts due for 90-day discard (REG-DM/OSP-DM), so nothing is auto-discarded unseen |
| `POST /v1/admin/accounts/{account_id}/legal-hold` | `internal_reason` (required) | `204` — sets `user_account.legal_hold = true`, suspending every purge touching the account (REG-DM, CL-041); audits `legal_hold_set`. Idempotent — holding a held account succeeds and re-audits | `state_conflict` (purged — nothing left to hold) |
| `DELETE /v1/admin/accounts/{account_id}/legal-hold` | `internal_reason` (required) | `204` — clears the flag; audits `legal_hold_released`. Purges due while the hold stood run at the next sweep | `state_conflict` (no hold in place) |
| `POST /v1/admin/retention/purge/{account_id}` | — | Executes a scheduled purge early where policy allows; audits `retention_purge`. Routine purges run on schedule (pg_cron); this is the manual control |

## I. Support

| Endpoint | Request | Response | Errors |
|---|---|---|---|
| `GET /v1/admin/tickets` | `?state=open&category=&limit=&cursor=` | The support queue (ADM-22, SUP-DM): `appeal` first, then oldest by `last_activity_at`, each with the awaiting-admin signal | — |
| `GET /v1/admin/tickets/{id}` | — | The thread, the owner's account context (linking to the detail view), the attachment if present, and for an appeal the contested `moderation_action` | `not_found` |
| `POST /v1/admin/tickets/{id}/reply` | `body` | `204` — an admin `ticket_message`; push-notifies the owner (SUP-03); audits `support_reply` | `state_conflict` |
| `POST /v1/admin/tickets/{id}/resolve` | `body` (**required** — the closing reply, ADM-22) | `204` — resolves with the closing message; audits `support_resolution` | `validation_failed` (no closing message) |

Resolving an appeal ticket does **not** itself reinstate the account; the admin reinstates through `POST /v1/admin/accounts/{id}/reinstate` with the `appeal_ticket_id`, which resolves the ticket and reinstates in one transaction (ADM-DM). Resolving the ticket alone is how an appeal is *denied* (with a closing reason), leaving the suspension in place.

## K. Settings — platform configuration (ADM-21)

| Endpoint | Request | Response |
|---|---|---|
| `GET /v1/admin/config` | — | The current platform values the **read-only** Settings page shows (ADM-21): offer expiry days; radius min/max; portfolio limits (image/video/document/link counts and sizes, the 45-s video); OTP parameters (length, expiry, resend window, per-number daily cap); login-lockout thresholds; and the review-turnaround target. These are **deployment configuration** in the MVP — there is **no write endpoint**; changing a value is an engineering deploy (editable config is post-MVP, ADM-21). |

The values are read from the same engineering-default constants the rest of the API enforces (offer expiry OFR-DM, radius/portfolio MAP/OSP, OTP REG-DM), surfaced here so the founder can see the live configuration in one place without reading code.

## Flows

**Reviewing an Ostad.** `GET /v1/admin/reviews` → open a case → `GET …/{case_id}` (identity URLs issued, rate-limited, each audited; selfie shown for a photo change) → compare selfie, documents, and claimed names → `POST …/identity {passed}` → `POST …/verdict {approve}`. The approve is refused until identity is passed and any duplicate is resolved.

**Handling a harassment report against a hidden Shagred.** The report was filed through a lapsed **offer** and carries `via_offer_id` (RNT/SGP) → `GET …/{report_id}` shows that offer's message (the evidence) and the reported Shagred resolved server-side → `POST …/resolve {suspend}`. The reporting Ostad never regained sight of the Shagred's profile.

**Appeal.** A terminated account appeals → the ticket arrives flagged first → `GET …/{ticket_id}` shows the contested action → to grant: `POST …/accounts/{id}/reinstate {appeal_ticket_id}` (reinstates and closes the ticket together); to deny: `POST …/tickets/{id}/resolve {reason}` (suspension stands).

**Broadcast.** `POST …/broadcasts?preview=true` → the client shows "this reaches N people" → the admin confirms → `POST …/broadcasts` sends.

## What this module does not expose

No endpoint returns an identity document image, a chat message, or a Shagred's Ostad history without writing an audit entry for the read (and, for identity documents, consuming the per-session vault-read budget); no endpoint lets the admin browse chats absent a report citing specific messages (OFR-07); no endpoint edits or deletes the audit log; no admin registration, password-reset, or self-provisioning endpoint exists (ADM-20); and the admin token is accepted by no Supabase channel and no user endpoint (API Overview).
