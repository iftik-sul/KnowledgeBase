---
project: OstadLagbo
type: api
status: current
updated: 2026-09-24
id: OL-API-001
derived_from: /OstadLagbo/decisions/adr-001-platform-architecture.md
owner: Iftikher
---

# API — Overview & Conventions

The rulebook for the api layer: how the mobile app and the admin dashboard talk to the **Render API** (ADR-001), what every endpoint has in common, and the template each module's api document follows. Module documents define the endpoints; this document defines the rules they all obey. Where this document and a module document disagree, this one wins — raise the conflict as a documentation fix.

## What talks to what

| Client | Goes through the API for | Talks to Supabase directly for |
|---|---|---|
| Flutter app (guest, Shagred, Ostad) | **Everything that reads or writes product data**, including all authentication flows | **Realtime subscriptions** for chat delivery (OFR) and **signed-URL media transfer** (uploads and downloads), both scoped by row-level security |
| Admin dashboard (Vercel) | Everything | **Nothing** — the dashboard never holds a Supabase credential or token of any kind |

**The API is the single write path.** No client writes to the database except through it. Registration and login are API endpoints, not direct Supabase Auth calls, so the 18+ gate, consent capture, deletion-window recovery, and rate limits are enforced in one place before an account ever exists.

## Authentication

There are **two token families, and they never cross.**

**User tokens** are Supabase-issued JWTs, obtained only through the API's auth endpoints (the API creates the Supabase Auth user and session server-side). They are accepted by the API and, for the direct channels, by Supabase Realtime and Storage. `Authorization: Bearer <token>`; **no header = guest.**

**Admin tokens** are issued by the **API itself** after email + password + TOTP verification against `admin_account` (ADM-DM, ADM-20, CL-018). Admins are **not** Supabase Auth users. Admin tokens are signed by the API with a separate key and audience, accepted only by `/v1/admin/*` endpoints, and never by Supabase. A user token presented to an admin endpoint — or an admin token to a user endpoint — is `unauthorized`. The 24-hour inactivity expiry is enforced against `admin_session` (ADM-DM).

Every authenticated user request resolves the caller's `user_account` and its `status` before the handler runs:

| `status` | What the API allows |
|---|---|
| `active` | Everything the role permits |
| `pending_deletion` | **No session exists** — the deletion request revoked them all. A login recovers the account (REG-02), after which it is `active` |
| `suspended` (incl. terminated) | A **restricted session** (REG-DM `auth_session.restricted`) permitting only: the suspension-notice read, `appeal` ticket create/read/message (SUP), a `ticket_attachment` upload ticket, push-token registration, locale change, and logout (Data Model Overview rule 7). Everything else is `suspended` (403) |
| `purged` | Token invalid |

**Direct channels enforce account status.** A suspended user's token is still a valid Supabase JWT, so the API's refusal alone is not enough: **every row-level-security policy on a table or bucket the app reaches directly (Realtime chat subscriptions, Storage objects) additionally requires the caller's account status to be `active`.** A suspended account therefore receives no chat delivery and can fetch no media directly; its appeal attachments and ticket thread come through the API. Suspension also revokes the account's Supabase refresh tokens, and the RLS status check closes the window before the last access token expires.

**The policy layer.** Every handler calls the centralized policy module (Data Model Overview → authorization model) before touching data. Module api documents state, per endpoint, **who may call it and which rule the policy layer checks.** No handler evaluates access on its own.

## Account existence

Whether a phone number has an account is sensitive (it identifies who uses the platform). The API's stance, stated once so every module applies it consistently:

- **Registration necessarily reveals it.** `register/start` must say "this number is in use" or "this number is recoverable" — a registration flow cannot hide it and still work. This is accepted industry practice; it is mitigated by per-IP and per-phone rate limits (REG-02).
- **Everything else hides it.** Password reset responds identically for known and unknown numbers; login failures give one message whether the phone or the password is wrong; **login lockout is keyed on the submitted phone string**, so a lockout occurs (and is reported) identically whether or not an account exists; phone-change collisions are reported only to the authenticated account attempting the change.

## Conventions

**Base and versioning.** All endpoints live under `/v1/`. Breaking changes ship as `/v2/` alongside `/v1/` for a deprecation window; additive changes (new optional fields, new endpoints) do not bump the version. The app sends `X-App-Version` on every request so the API can refuse builds below a minimum (engineering default).

**Localization.** Authenticated requests are answered in `user_account.preferred_locale` (REG-14); guests send `Accept-Language: en` or `bn` (default `en`). Every user-facing string in a response — error messages, notification text, status labels — is localized server-side; the client never translates API text. Phone numbers, OTP codes, and IDs are always Latin digits (NFR-11). The admin dashboard is English-only.

**Errors.** One shape, always:

```
{ "error": { "code": "<stable_snake_case>", "message": "<localized, user-safe>", "details": { ... optional, field-level ... } } }
```

`code` is a closed enum the client switches on; `message` is shown to the user as-is. Standard codes and their HTTP statuses:

| code | HTTP | Meaning |
|---|---|---|
| `validation_failed` | 400 | Input rejected; `details` names fields |
| `unauthorized` | 401 | Missing, invalid, or wrong-family token |
| `forbidden` | 403 | Policy layer refused — the caller's role or state may not do this |
| `suspended` | 403 | Caller's session is restricted; `details` carries the notice payload and whether an appeal is open |
| `not_found` | 404 | The resource does not exist **or the caller may not know it exists** (opacity rule) |
| `conflict` | 409 | Uniqueness violated (phone in use, second pending offer, second rating) |
| `state_conflict` | 409 | The action is valid but the target is in the wrong state (accepting an expired offer) |
| `account_recoverable` | 409 | Registration hit a phone inside its deletion window — log in to recover (REG-02) |
| `locked_out` | 423 | Login or OTP lockout; `details.retry_after_seconds` |
| `app_update_required` | 426 | Build below minimum |
| `rate_limited` | 429 | `Retry-After` header set |

**The opacity rule.** A refusal must never reveal a **block** (RNT-08: the blocked party is never told). Any read or write that fails only because a block exists returns `not_found`, identical to the resource not existing. A refusal because an Ostad is **paused** is explicit (`state_conflict`, `details.reason = "ostad_not_accepting"`) — pause is public state (OSP-11). Module documents mark every endpoint where the opacity rule applies.

**Pagination.** Cursor-based on every list: `?limit=` (max 50, default 20) and `?cursor=` (opaque). Responses carry `next_cursor` (null at the end). Never offset-based — lists change under the reader.

**Idempotency.** Every `POST` that creates something a user would notice twice — offers, ratings, replies, tickets, ticket messages, chat messages, reports, favorites — accepts an `Idempotency-Key` header (client-generated UUID). A retry with the same key within **24 hours** returns the original result and creates nothing. Keys are scoped to the caller (account, or guest session) and held as **infrastructure state for 24 hours** — not product data, not modeled, not backed up beyond that window. This is NFR-03's "never silently lost, never duplicated" made concrete.

**Rate limits.** Per IP for guests, per account for users, per admin for the dashboard, and **per phone string** for OTP and login attempts; the map's viewport queries carry their own cap (MAP-DM, scraping resistance). Limits are engineering defaults surfaced to ADM-19 and ADM-21; `429` always carries `Retry-After`.

**Media.** Uploads never pass through the API body. The client asks the API for an **upload ticket** (`POST /v1/uploads`, stating the purpose), receives a short-lived signed URL and an `upload_id`, `PUT`s the bytes to Supabase Storage, then references the `upload_id` in the endpoint that consumes it. The API re-validates the stored object at consumption (real content type, size, duration — NFR-04, OSP-07, OFR-05) and moves it to its permanent, purpose-appropriate bucket. Identity documents and selfies go to the **encrypted vault bucket** and are never URL-addressable outside admin review (ADM-17 audit on every view). Downloads are likewise short-lived signed URLs issued per read.

**Realtime.** Chat message *delivery* is a Supabase Realtime subscription on the participant's own threads (RLS-scoped, status-checked). Chat message *sending* is an API call (OFR api). The API is the only writer; Realtime is a read channel.

**Analytics events.** Client-side events (map sessions, searches, zero-result searches, profile views, share taps, screen views) are batched to `POST /v1/events` under a pseudonymous session id — never phone, name, or precise coordinates (NFR-06; MAP-DM coarsening). The API validates each against the event catalog, strips disallowed properties, and writes to the **analytics store defined by ADR-002** (a separate append-only schema in the same database). Server-side events (offers, connections, verdicts, tickets) are written by the API itself. Both feed ADM-12…15.

**Timestamps and IDs.** ISO-8601 UTC timestamps; UUID identifiers; money never appears (out of scope).

**Health and admin.** `GET /v1/health` (unauthenticated, for uptime monitoring, NFR-09). Admin endpoints live under `/v1/admin/` and appear only in the ADM api document.

## Endpoint document template

Each module's api document lists endpoints in a fixed table:

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `VERB /v1/path` | who may call; the rule the policy layer enforces | body / query fields with rules | shape returned | codes beyond the standard set, and whether the opacity rule applies |

followed by **flows** (multi-step sequences, showing which endpoints fire in which order and what transaction the API runs), and **what this module does not expose** (data the models hold that no endpoint returns — the privacy guarantees made explicit at the API boundary).

## Document sequence

REG → OSP → SGP → ADM → MAP → OFR → RNT → SUP, each at `modules/<module>/api/`, deriving from its requirements document and citing its data model. Each drafted, adversarially reviewed, then approved.
