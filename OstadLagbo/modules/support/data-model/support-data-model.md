---
project: OstadLagbo
module: support
type: data-model
status: current
updated: 2026-09-13
id: OL-SUP-DM-001
derived_from: /OstadLagbo/modules/support/requirements/support-requirements.md
owner: Iftikher
---

# Support — Data Model

Entities owned: `support_ticket`, `ticket_message`. Conventions per [Data Model Overview](/OstadLagbo/data-model-overview.md). The smallest model in the layer, with two rules that matter more than its size suggests: the **suspension-appeal exception** (the one case where a locked-out account may still write to the platform) and the **14-day reopen window** as a state rule rather than a UI convention.

## support_ticket

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| account_id | uuid → user_account | The user who opened it; any registered account, any status except `purged` (see appeal exception) |
| category | enum: `account_login` \| `verification_review` \| `technical` \| `appeal` \| `other` | SUP-02's five categories, exactly |
| description | text | Proposed cap 1,000 chars (SUP-02) |
| attachment_ref | storage ref, nullable | **At most one** image (SUP-02); OSP image rules; **visible only to the owner and admin** — no other user read path exists |
| status | enum: `open` \| `resolved` | |
| resolved_at | timestamp, nullable | Set on resolve; the reopen window is computed from it, not stored |
| reopened_count | int, default 0 | Incremented on each reopen; informational for ADM-15's reopen rate |
| related_moderation_action_id | uuid, nullable → moderation_action | **Required for an `appeal` created from the suspension-notice screen** — the active `suspend` action being contested (ADM-DM). Nullable otherwise: an appeal of a warning may reference the `warn` action; an appeal of a **content removal carries no link**, because removals are not `moderation_action` rows (they live on the rating/reply row and the audit log) — the user describes it in text |
| last_activity_at | timestamp | Updated on every message insert and status change; drives inactivity auto-resolution and the owner's list ordering |
| created_at / updated_at | timestamps | |

**Constraints:**
- **Open-ticket cap:** proposed 5 open tickets per account (SUP-02) — a count-check at creation, not a constraint, same limitation as OFR-DM's offer cap. **The cap does not apply to `appeal` tickets**: an appeal is a right the ToS promises (§7), never a convenience the cap may refuse.
- **One open appeal per contested action:** partial unique index on (`account_id`, `related_moderation_action_id`) where `category = appeal and status = open`. A suspended user cannot stack duplicate appeals of the same suspension; a new appeal is permitted once the prior one resolves — the same anti-spam pattern as RNT-DM's reports.

### The suspension-appeal exception (SUP-04, ADM-08)

`user_account.status = suspended` locks the account out of the app except the suspension-notice screen. **That screen may create exactly one kind of write: an `appeal` ticket** — and may read that ticket's thread to follow the appeal. The policy layer permits, for a suspended account: `INSERT support_ticket WHERE category = appeal`, `INSERT ticket_message` on tickets that account owns, and `SELECT` on those same tickets. **Nothing else.** This is stated here because every other model treats `suspended` as fully read-only for the user; this is the single documented exception, and it exists so the ToS §7 appeal promise has a working door.

`pending_deletion` accounts may also create and follow tickets (they can log in to recover; support is part of that). `purged` accounts cannot — there is no account to act.

### Reopen window — a state rule (SUP-03)

```
ticket accepts a new user message  iff
  status = open
  OR (status = resolved AND now ≤ resolved_at + 14 days)
```

A user message on a `resolved` ticket inside the window **reopens** it: `status → open`, `resolved_at → null`, `reopened_count + 1`. Outside the window the insert is refused and the client offers a new ticket. **Admin and system messages never reopen a ticket** — an admin adding to a resolved ticket is a follow-up note, not a reopening. The window is computed from `resolved_at`; there is no stored deadline (Overview: predicates over flags).

### Inactivity auto-resolution

A ticket that is `open` with no message from any author for **N days** (engineering default, proposed 90, measured from `last_activity_at`) is resolved by a scheduled job with a `system` closing note. This exists so every ticket eventually reaches `resolved_at` and its retention clock starts — without it, an abandoned ticket would never purge. Appeal tickets are **excluded** from auto-resolution: an unanswered appeal is an admin failure to surface in ADM-15, not a ticket to close silently.

## ticket_message

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| ticket_id | uuid → support_ticket | |
| author_kind | enum: `user` \| `admin` \| `system` | `system` for platform-authored notes: inactivity auto-resolution, purge-job closure, and nothing else |
| author_account_id | uuid, nullable → user_account | Set iff `author_kind = user`; **must equal `support_ticket.account_id`** — enforced as a constraint: only the ticket's owner writes as `user` |
| author_admin_id | uuid, nullable → admin_account | Set iff `author_kind = admin` |
| body | text | |
| is_resolution | boolean, default false | `true` on the message that resolves the ticket — the "closing reply" ADM-22 requires; permitted for `admin` and `system` authors; a resolve action without a message is refused |
| read_by_user_at | timestamp, nullable | For `admin` and `system` messages: set when the user opens it; drives the owner's unread indicator (SUP-03). Not tracked for `user` messages |
| created_at | timestamp | |

Both author ids are null for `system`; exactly one is set otherwise — a check constraint, not a convention.

**Ticket threads are not chat threads.** No delivery states, no voice notes (SUP-05) — a deliberately simpler entity than `chat_message`, and never joined to it. A ticket's first message is the `description` rendered inline, not a `ticket_message` row.

**Immutability:** `ticket_message` rows are never edited or deleted from any user-facing interface; support threads are operational records. Admin replies and resolutions are audit-logged (`support_reply`, `support_resolution` — ADM-DM).

## Read rules the policy layer enforces

- A ticket and its messages are readable **only** by the owning account (`support_ticket.account_id`) and admin. No other user can reach a ticket by id.
- Attachments follow the same rule — the storage object is served only to the owner and admin, never linkable elsewhere.
- Admin reads are through ADM-22's queue and ADM-10's account detail; admin support actions are audit-logged.
- The suspension-appeal exception above is the **only** write path a suspended account holds anywhere in the system.

## Retention behavior (OL-RET-001 mapping)

| Entity | Rule |
|---|---|
| support_ticket + ticket_message | **2 years after resolution** — the reports-and-moderation schedule (SUP-03 explicitly aligns tickets to it). On the owner's purge, `account_id` remains a valid tombstone pointer (REG-DM); the thread survives on its content and category. Open tickets belonging to a purged account are resolved by the purge job with a `system` closing note, so no ticket is orphaned open. Inactivity auto-resolution (above) guarantees every non-appeal ticket eventually reaches this clock |
| attachment_ref | The storage object deletes with the ticket at the end of its retention, in the same operation (the OSP/OFR pattern); swept by ADM-18; out of backups within 90 days (NFR-07) |
| Legal hold | A `legal_hold` on the owning account suspends purging of its tickets — an appeal thread is evidence in any dispute about the suspension it contests |

## Queries this model must serve

Open-ticket count per account (the cap, excluding appeals); the owner's ticket list (`account_id = :me`, ordered `last_activity_at desc`, with state and an unread indicator = any `admin`/`system` message with `read_by_user_at is null`); ticket thread read (owner or admin only); the reopen predicate on every user message insert; the resolve action (an `admin` `ticket_message` with `is_resolution = true` + `status → resolved` + `resolved_at`, one transaction); **ADM-22's queue** — `status = open`, `category = appeal` first, then oldest `last_activity_at` first — with each ticket's **awaiting-admin signal** derived as *latest message has `author_kind = user`* (or no message yet), so tickets the user has answered surface ahead of ones waiting on the user; the linked `moderation_action` context for appeals; the suspension-screen read (a suspended account's own `appeal` tickets); the inactivity auto-resolve job (`status = open and category ≠ appeal and last_activity_at ≤ now − N days`); ticket volume by category, resolution time (`resolved_at − created_at`, per resolution event), and reopen rate for ADM-15 (from analytics events, cross-checkable here).
