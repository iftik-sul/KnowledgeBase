---
project: OstadLagbo
module: admin-review
type: ui
status: current
updated: 2026-09-25
id: OL-ADM-UI-001
derived_from: /OstadLagbo/modules/admin-review/requirements/admin-review-requirements.md
owner: Iftikher
---

# Admin Review & Dashboard — UI

Every screen of the admin dashboard: overview, review, moderation, user management, taxonomy, analytics, communication, operations/compliance, settings, and support. Conventions per [UI Overview](/OstadLagbo/ui-overview.md) where they apply, plus this document's own (below); behaviour and endpoints per [ADM API](/OstadLagbo/modules/admin-review/api/admin-review-api.md). Report *creation* and blocking are the app's (RNT ui); this dashboard *handles* them.

## Dashboard conventions (its own)

The dashboard is a **separate web application** — desktop-oriented, **English-only**, the **only** interface holding these powers (none exist in the app). Its conventions differ from the app's:

- **Auth is email + password + TOTP** (ADM-20, CL-018): password alone never yields a session; a TOTP challenge follows. Sessions **expire after 24 hours of inactivity**. There is **no** admin registration, password reset, or self-service — a lost credential is an operations incident, not a screen. **All admins currently hold full permission** (role tiers are post-MVP).
- **The app's opacity rule does not apply here.** Admin moderation is the job; directories, detail views, and actions address **accounts** directly and show internal fields. Blocks and suspensions are visible to admin as data.
- **Sensitive reads are audit-logged as a side effect, always** (ADM-17): opening an **identity document**, viewing **report-cited chat context**, and viewing a **Shagred's Ostad history** each write an audit entry the reviewer cannot avoid or suppress. **Identity/selfie image reads are also rate-limited per session** with a spike flag (the vault-exfiltration tripwire) — a stolen token cannot silently pull every NID.
- **Every action is audit-logged** (ADM-17), and the audit log is **append-only** — no screen edits or deletes it.
- Error and state handling follow the overview's mapping (`unauthorized` → re-auth; `state_conflict` → the specific reason); charts use a standard library; tables paginate cursor-based.

## Admin sign-in
- **Structure:** email + password → a **TOTP** challenge screen → the dashboard.
- **Data:** `POST /v1/admin/auth/login` → `{challenge, challenge_id}` → `POST /v1/admin/auth/totp` → session; `locked_out` under REG-05 rules; `unauthorized` uniform on bad credentials.

## A — Overview (ADM-01)
- **Overview home:** KPI cards — pending reviews, open reports, open appeals, Ostads by status, total Shagreds, suspended, new registrations (today / 7 days), offers sent and **connections** (7 days), open tickets — each a **link to its filtered list**; counts exclude accounts mid-purge. A **recent-activity feed** (newest registrations, submissions, reports) with deep links.
- **Data:** `GET /v1/admin/overview`.

## B — Review management (ADM-02…06)
- **Review queue:** all Ostad submissions — first submissions and key-field re-reviews — in **one queue, oldest first**; each row flags `identity_recheck_required`, `photo_recheck_required`, and an `id_duplicate_flag`. Nothing bypasses it. `GET /v1/admin/reviews`.
- **Review screen:** the **complete profile** including internal fields; the **identity documents and selfie beside the claimed legal names and DOB** (documents as short-lived vault URLs — each issuance rate-limited and audited; the selfie shown whenever an identity/photo re-check is required, CL-021); for a **re-review**, a field-level **diff** against the last approved version; a **duplicate match** (the other account's id and status) when flagged.
  - **Identity gate (ADM-03):** the reviewer marks identity **passed / failed** (`POST …/identity`). **Approve is unavailable** — in this UI and the API — while identity is not `passed` or a duplicate is unresolved; the button is disabled with the reason shown.
  - **Verdicts (ADM-04):** **Approve** (→ discoverable + badge), **Request changes** (**mandatory note**), **Reject** (**mandatory reason**) — an empty note/reason cannot submit. Each notifies the Ostad by push and in-app status. `POST …/verdict`. Verdict history is retained and shown.
  - **Re-review (ADM-06):** approving publishes the pending key-field change; rejecting discards it — the public profile never shows unapproved content at any point.
- **Resubmission (ADM-05):** unlimited; each re-enters the queue carrying full verdict history.
- **Data:** `GET /v1/admin/reviews/{case_id}`, `POST …/identity`, `POST …/verdict`.

## C — Moderation (ADM-07…09)
- **Reports queue:** reporter, reported account, category, created-at, and whether messages are cited; filter by state / target type / category; a `via_offer` marker where a hidden-Shagred report carries its offer evidence. `GET /v1/admin/reports`.
- **Report detail:** the report and the **reported content inline** — profile, review, reply, or (via `via_offer_id`) **the offer's message as evidence**; for a message report, the **cited messages with ±10 context** as signed reads — **this view audits `chat_context_viewed`** and shows only the cited window, never a browsable chat. Resolutions: **dismiss** (optional note) / **warn** (message delivered) / **suspend** / **remove content** (reviews/replies) — each requires an internal reason. `GET …/{report_id}`, `POST …/resolve`.
- **Block overview (ADM-09):** read-only — most-blocked accounts and recent blocks; a moderation signal only, action goes through account detail. `GET /v1/admin/blocks`.

## D — User management (ADM-10)
- **Ostad list:** every Ostad, filter by status (draft / pending / changes-requested / rejected / approved / suspended / terminated), search by **name, phone, or ID number**, filter by District and category, sort by registration/submission date. `GET /v1/admin/ostads`.
- **Shagred list:** filter by status, search by name or phone. `GET /v1/admin/shagreds`.
- **Account detail:** the **full profile including every internal field** (street address, DOB, contact, identity **metadata**; identity **images** only via the audited, rate-limited vault path); **verdict history**; **report history as reporter and reported**; **audit entries touching this account**; the **Shagred's Ostad history** if a Shagred (this read audits `shagred_history_viewed`); and the applicable **actions** — verdicts where a review is open, and **warn / suspend / reinstate / terminate** always. `GET /v1/admin/accounts/{account_id}`.
  - **Warn / Suspend / Reinstate / Terminate (ADM-08, CL-019):** warn (internal reason + user message) · suspend (internal reason, optional message; revokes sessions, freezes chats, freezes pending offers — expiry clocks keep running) · reinstate (restores prior state incl. approval; if resolving an appeal, takes the `appeal_ticket_id` and closes it in one step) · **terminate** (internal reason + **mandatory ban-and-appeal message**; opens the 30-day appeal window, after which the account purges under the banned-account retention exception). Every one is audit-logged. `POST …/warn|suspend|reinstate|terminate`.

## E — Content & taxonomy (ADM-11)
- **Skill categories:** create, rename (either script), deactivate; each carries an English name and an admin-managed **Bangla name/alias** (for cross-script matching); **per-category usage counts**. In-use categories **cannot be deleted, only deactivated** (hidden from new selection; existing profiles keep them until their next skill edit); renames propagate immediately; no operation strands a profile. `GET /v1/admin/skill-categories`, `POST`, `PATCH`.
- **Admin areas:** maintenance of the Division→District→Thana→postal dataset (`GET/POST/PATCH /v1/admin/admin-areas`).

## F — Analytics (ADM-12…15)
Five boards, each full charts and time-series with **7 / 30 / 90-day** ranges, reading pre-aggregated rollups (never raw events):
- **Connections & funnels (ADM-12):** contacts made (offers sent, accepted = connections, unique pairs, active chats, messages, phone reveals) as totals and series; supply funnel (registration→onboarding→submission→approval) and demand funnel (map sessions→profile views→offers→connections) with stage conversions; offer-health distribution. `GET /v1/admin/analytics/connections`.
- **Growth & retention (ADM-13):** registrations by role, approvals, connections as series; activation, retention, dormancy (**paused distinguished from inactive**). `GET …/growth`.
- **Demand intelligence (ADM-14):** zero/low-result searches by category, script, and area; top searched vs. coverage by District and category; concentration — the recruitment compass. `GET …/demand`.
- **Quality & operations (ADM-15):** ratings distribution, review-submission rate, reports per 100 WAU, review turnaround vs. 48 h, resolution time, suspension/termination/reinstatement counts (appeal-driven reinstatements distinguished), appeals pending beyond 7 days, ticket volume/resolution/reopen. `GET …/quality`; the operations feed (OTP volume, spend, rate-limit hits, the identity-view spike flag, analytics-store size) `GET …/operations`.

## G — Communication (ADM-16)
- **Broadcasts:** compose a push to a **segment** (all / Ostads / Shagreds) with title and body **required in both English and Bangla** (each recipient gets their locale's version); a **preview** resolves the recipient count **without sending**; sending is **irreversible** and the client confirms against the preview first; past broadcasts are listed. Recorded and audit-logged. `POST /v1/admin/broadcasts?preview=true`, `POST …/broadcasts`, `GET …/broadcasts`.

## H — Operations & compliance (ADM-17…19)
- **Audit log (ADM-17):** a searchable, filterable viewer (actor, action type, target, date range) over the **append-only** log — **read-only; no edit or delete endpoint exists**. `GET /v1/admin/audit`.
- **Retention tools (ADM-18):** identity-document storage status per account; the **pending-abandonment list** (revisions/onboarding drafts due for 90-day discard); execute a scheduled purge early where policy allows (audit-logged). `GET /v1/admin/retention`, `POST …/retention/purge/{account_id}`.
- **SMS/OTP monitor (ADM-19):** OTP volume by day, per-number rate-limit hits, estimated spend — read-only (folded into the operations analytics feed).

## I — Settings (ADM-21, read-only)
- **Platform configuration:** a read-only page displaying current platform values — offer expiry days, radius limits, portfolio limits, OTP parameters, login-lockout thresholds, and the review-turnaround target — from `GET /v1/admin/config`. Changing any is an engineering deployment in the MVP; there is **no edit action** (editable config is post-MVP, ADM-21).

## J — Support (ADM-22)
- **Support queue:** tickets by state (open / resolved) and category, **Appeal tickets flagged and sorted first**, each with the awaiting-admin signal and a **reopened marker** where a resolved ticket was reopened (ADM-22). `GET /v1/admin/tickets`.
- **Ticket detail:** the thread, the owner's **account context** (linking to account detail), the attachment if present, and for an appeal the **contested moderation action**. Actions: **reply** (push-notifies the user) and **resolve** (**requires a closing reply**). Resolving an appeal does **not** itself reinstate — reinstatement is the account action with the `appeal_ticket_id`; resolving alone **denies** the appeal (suspension stands). `GET …/{id}`, `POST …/reply`, `POST …/resolve`.

## Flows

**Review an Ostad.** Review queue → open a case → the identity documents and selfie load (each audited, rate-limited) → compare against the claimed names → mark identity **passed** → **Approve** (now available) → the Ostad is notified and becomes discoverable with the badge. A duplicate-ID flag or an unpassed identity keeps Approve disabled.

**Handle a report on a hidden Shagred.** Reports queue → open the report (it carries `via_offer_id`) → read the offer's message as evidence → **Suspend** with an internal reason → the Shagred is suspended; the reporting Ostad never re-saw the profile.

**Terminate, then an appeal.** Account detail → **Terminate** with the ban-and-appeal message → the account can now only appeal → the appeal arrives in the support queue flagged first → open it, review the contested action → to grant: **Reinstate** with the `appeal_ticket_id` (restores the account, closes the ticket); to deny: **Resolve** the ticket with a reason (the ban stands to the end of the window).

**Broadcast.** Compose (both languages) → **Preview** ("reaches N people") → confirm → send.

## What this dashboard never allows

No approval while identity is unpassed or a duplicate is unresolved; no verdict, warning, termination, or ticket resolution without its mandatory note/reason/reply; no identity-document, chat-context, or Shagred-history read without an audit entry (and identity reads spend the per-session vault budget); no edit or deletion of the audit log; no browsing of a chat absent a report citing specific messages; no admin registration, password reset, or self-provisioning; no broadcast in a single language; and no admin token accepted by any app endpoint or Supabase channel.
