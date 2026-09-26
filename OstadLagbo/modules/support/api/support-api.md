---
project: OstadLagbo
module: support
type: api
status: current
updated: 2026-09-26
id: OL-SUP-API-001
derived_from: /OstadLagbo/modules/support/requirements/support-requirements.md
owner: Iftikher
---

# Support — API

Endpoints for in-app help tickets, their threads, and the suspension appeal. Conventions per [API Overview](/OstadLagbo/api-overview.md); entities, the reopen predicate, and the appeal exception per [SUP Data Model](/OstadLagbo/modules/support/data-model/support-data-model.md). The smallest api in the layer, and the one that makes the **restricted-session whitelist** — cited throughout REG and OFR — concrete: the appeal ticket is the single new write a suspended account can perform anywhere in the system.

## Two rules that shape these endpoints

- **A ticket is private to its owner and admin.** No other user reaches a ticket, its thread, or its attachment by any id (SUP-DM read rules). Admin access is the ADM-22 queue, defined in the ADM api, not here.
- **Ticket threads are not chat threads** (SUP-05): no delivery states, no voice notes, no realtime channel. They are operational records — simpler than `chat_message`, never joined to it, and immutable (no edit or delete).

## Endpoints — tickets

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `POST /v1/support/tickets` | Any **registered** account (both roles, including a pending Ostad, SUP-01); accepts `Idempotency-Key`. A **suspended** account may call this **only** for `category = appeal` (the restricted-session exception, below) | `{ category, description, attachment_upload_id?, related_moderation_action_id? }` — `category` ∈ `account_login`/`verification_review`/`technical`/`appeal`/`other`; `description` ≤1,000 chars; **at most one** image via the upload-ticket flow (`POST /v1/uploads`, purpose `ticket_attachment`), which the API re-validates at consumption (OSP image rules) | The created `support_ticket` (`status: open`); appears in "my tickets" and reaches ADM-22's queue | `validation_failed` (description empty/oversized; unknown category; more than one attachment; a suspension or termination appeal missing `related_moderation_action_id`, or one naming an action that is not the latest active `suspend`/`terminate`); `conflict` (`reason: "open_ticket_limit"` — the 5-open cap, **which never applies to `appeal`**; or `reason: "duplicate_open_appeal"` — one open appeal per contested action); `forbidden` (a suspended account creating any non-`appeal` category) |
| `GET /v1/support/tickets` | The owner | `?limit=&cursor=` | The owner's tickets, `last_activity_at desc`, each with `category`, `status`, and an **unread indicator** = any `admin`/`system` message with `read_by_user_at` null (SUP-03) | — |
| `GET /v1/support/tickets/{id}` | The **owner** only (a suspended owner may read any ticket they own — the exception below) | — | The ticket and its thread: each `ticket_message` with `author_kind` (`user`/`admin`/`system`), `body`, `is_resolution`, `created_at`; the first message is the ticket's `description` rendered inline (not a row). The attachment, if any, as a **short-lived signed URL** served only to the owner (SUP-DM) | `not_found` (not the owner, or no such ticket — opacity) |
| `POST /v1/support/tickets/{id}/messages` | The **owner** (a suspended owner may message any ticket they own — the exception below); accepts `Idempotency-Key` | `{ body }` | The created `ticket_message` (`author_kind: user`); a message on a **resolved** ticket within 14 days **reopens** it (`status → open`, `resolved_at → null`, `reopened_count + 1`) per the reopen predicate | `not_found` (not the owner); `state_conflict` (`reason: "reopen_window_closed"` — the ticket resolved more than 14 days ago; the client offers a new ticket) |
| `POST /v1/support/tickets/{id}/read` | The owner | — | `204` — sets `read_by_user_at` on the ticket's unread `admin`/`system` messages, clearing the unread indicator (SUP-03) | `not_found` (not the owner) |

**No user resolve action exists.** A ticket is resolved only by an admin, with a closing reply (`is_resolution`, ADM-22), or by a scheduled job — inactivity auto-resolution after ~90 days of silence (appeals excluded), and the purge job closing a departed owner's open tickets. Both write a `system` message; **neither an admin follow-up nor a system note ever reopens a ticket** (SUP-DM). The 14-day reopen window belongs to the user's message alone. A reopen is **not** subject to the 5-open cap — the cap is checked only at creation (SUP-DM), so continuing a resolved thread never counts as a new ticket.

## The restricted-session exception (SUP-04, ADM-08)

A `suspended` account is locked out of the whole app except the suspension-notice screen, and that screen holds the **only** new writes such an account can perform anywhere — the working door behind the ToS §7 appeal promise. Exactly:

- **Create** — `POST /v1/support/tickets` with `category = appeal` only, `related_moderation_action_id` set to the latest active `suspend` **or** `terminate` action being contested (CL-041);
- **Continue** — `POST /v1/support/tickets/{id}/messages` and `GET` on **any ticket that account owns** (not only the appeal), so a support thread opened before the suspension is not frozen mid-conversation;
- the three supporting operations named in REG/ADM: request a `ticket_attachment` upload, register a push token from the restricted session (so the admin's reply arrives), and change locale or log out.

Everything else returns `suspended`. The appeal path is exempt from the open-ticket cap, and the one-open-appeal-per-action index prevents stacking duplicate appeals of the same suspension.

**`pending_deletion` accounts never use support as such** — the deletion request revoked every session; logging in recovers the account (REG-02), after which support is used as an ordinary active user. `purged` accounts cannot act at all.

## `related_moderation_action_id`, by what is being appealed

- **A suspension or a termination** (from the notice screen) — **required**, references the **latest active `suspend` or `terminate`** action (ADM-DM, CL-041). Where the account is terminated this is the `terminate` row: the termination is what is being contested, and a user who already appealed the underlying suspension must still be able to appeal the ban.
- **A warning** — optional, may reference the `warn` action.
- **A content removal** — **null**: removals are not `moderation_action` rows (they live on the rating/reply row and the audit log, RNT-DM), so the user describes it in `description`.

## Instrumentation (SUP-06)

Written **server-side by the API**, under the overview's analytics rules, for ADM-15: **tickets created** (by `category`), **resolution time** (`resolved_at − created_at`, emitted on the resolution event the ADM api owns), and **reopen rate** (a reopen event on each user message that flips a resolved ticket back to open). In-app state (the list, the unread indicator) derives from these rows, not from delivery, so a notifications-denied user misses nothing (SUP-03, OFR-03).

## Handled in the ADM api (named for completeness)

Ticket *handling* is ADM-22: the admin queue (open tickets, appeals first, then oldest `last_activity_at`, with the awaiting-admin signal), the admin reply, and the resolve action (an `admin` message with `is_resolution = true`, `status → resolved`, `resolved_at` — one transaction), all audit-logged (`support_reply`, `support_resolution`). This module owns only the user-facing side.

## Flows

**Ordinary ticket.** A Shagred opens Help & Support → `POST /v1/support/tickets {category: "technical", description, attachment_upload_id}` → it appears in `GET /v1/support/tickets` as open → an admin replies (ADM) → the user is pushed, opens the thread via `GET …/{id}`, and `POST …/read` clears the indicator → the user replies with `POST …/messages` → the admin resolves with a closing reply → 20 days later the user has a follow-up: outside the 14-day window, `POST …/messages` returns `state_conflict: reopen_window_closed`, and the client starts a new ticket.

**Appeal from suspension.** A suspended Ostad reaches the notice screen → `POST /v1/support/tickets {category: "appeal", related_moderation_action_id, description}` → the ticket reaches ADM-22 flagged as an appeal → the Ostad follows it with `GET` and `POST …/messages`, and can attach a screenshot via an upload ticket — and, beyond reading and replying to tickets they already own, can do nothing else in the app until the appeal resolves.

## What this module does not expose

No ticket, thread, or attachment is readable by anyone but its owner and admin; no endpoint lets a user resolve, edit, or delete a ticket or message; no admin follow-up or system note reopens a ticket, and no user message reopens one past 14 days; a suspended account can create nothing but an appeal, and act on nothing but tickets it already owns; tickets never carry voice notes, delivery states, or a realtime channel, and never mix with offer chat; and tickets are never the abuse-reporting channel — that is RNT-07, which the client steers users toward when they try to file abuse in a ticket (SUP-05).
