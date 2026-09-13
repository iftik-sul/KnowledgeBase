---
project: OstadLagbo
module: ratings-and-trust
type: data-model
status: current
updated: 2026-09-13
id: OL-RNT-DM-001
derived_from: /OstadLagbo/modules/ratings-and-trust/requirements/ratings-and-trust-requirements.md
owner: Iftikher
---

# Ratings & Trust — Data Model

Entities owned: `rating`, `rating_reply`, `report`, `block`. Conventions per [Data Model Overview](/OstadLagbo/data-model-overview.md). Two of these entities carry obligations to other models: `block` is the record four models already query as a predicate input (OSP discoverability, SGP visibility, MAP favorites and discovery, OFR thread writability and contact reveal), and `rating` is the thing that keeps anonymized profiles and connections alive after their owners are gone (SGP-DM, OFR-DM). This model has to satisfy those callers exactly as they assumed it would.

## block — the record everyone checks

Defined once here; **never copied** (Overview rule 5). One row per block action.

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| blocker_account_id | uuid → user_account | The account that acted |
| blocked_account_id | uuid → user_account | The account acted upon |
| created_at | timestamp | |
| revoked_at | timestamp, nullable | Set on unblock by the blocker (RNT-08); null = active |

**Constraints:** unique on (`blocker_account_id`, `blocked_account_id`) where `revoked_at is null` — a pair has at most one active block in a given direction. Both directions may exist independently. `blocker ≠ blocked` enforced. Any registered account may block any other it can reach — including an Ostad blocking an Ostad from a profile view (RNT-08).

**The canonical block predicate**, as every other model assumed it:

```
block_exists(a, b)  iff
  EXISTS block WHERE revoked_at IS NULL
    AND ((blocker = a AND blocked = b) OR (blocker = b AND blocked = a))
```

**Direction-agnostic in effect, direction-specific in authorship** (RNT-08): a single active row in *either* direction makes the predicate true for the pair, so every effect — chat freeze (OFR-DM), visibility severance (SGP-DM), discovery and favorites hiding (MAP-DM), offer refusal (OFR-DM), contact-reveal withdrawal (OFR-DM) — lands on both parties. Only the `blocker` may revoke. The blocked party is never notified, and no read path exposes to them that a block exists — the effects present as absence (no pin, no profile, a frozen chat with no stated cause on their side).

Unblock stores nothing beyond `revoked_at`: the thread-writable predicate (OFR-DM) simply passes again; MAP-DM's hidden favorites reappear. Blocks are **not** `moderation_action` rows — they are user actions — but they are visible in ADM-09's block overview and ADM-10's account detail as reads over this entity.

## rating

One per (Shagred, Ostad) pair, ever (RNT-01, RNT-06).

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| connection_id | uuid → connection | **The eligibility proof.** A rating cannot exist without a connection (RNT-01); this references the connection through which it was submitted |
| shagred_account_id / ostad_account_id | uuid / uuid → user_account | **Copied from the connection at insert — denormalized deliberately**, because the pair-uniqueness invariant below cannot be expressed through `connection_id` alone (a pair may accumulate many connections; OFR-DM). Same justification as `connection`'s own denormalization |
| stars | int 1–5 | Required (RNT-02) |
| review_text | text | **Required**, proposed cap 600 chars (RNT-02 — star-only submissions are refused) |
| created_at / updated_at | timestamps | Editable by the author at any time (RNT-01); `updated_at` tracks edits |
| anonymized | boolean | Set when the author's account purges (RNT-05) |
| removed_at / removal_reason | timestamp, nullable / text, nullable | Set only by admin content removal (RNT-06, ADM-07); a removed rating is excluded from display and aggregate but the row persists — the pair's one slot is consumed |

**Constraints:**
- **One rating per pair, ever:** unique index on (`shagred_account_id`, `ostad_account_id`) — **including removed rows**, which is exactly what makes "removal consumes the slot" (RNT-06) structural rather than procedural.
- **Author-only edits:** `stars` and `review_text` are mutable only by the Shagred identified by `shagred_account_id`; there is no admin edit path — admin can only remove.

**Aggregate maintenance (RNT-03):** `ostad_profile.rating_avg` and `rating_count` (OSP-DM) are recomputed on every insert, edit, anonymization, or removal — over rows where `removed_at IS NULL`. Anonymized ratings **keep their aggregate weight** (RNT-05); removed ratings **lose it**. Zero counted rows → the profile renders "New."

**Reviewer display:** the reviewer's name is read live from `shagred_profile.display_name` while the author's account exists; once `anonymized`, the literal "Former Shagred" is rendered and no join to the profile is attempted.

## rating_reply

At most one per rating (RNT-04).

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| rating_id | uuid → rating | **Unique** — one reply per rating, structurally |
| reply_text | text | Proposed cap 600 chars |
| created_at / updated_at | timestamps | Editable by the Ostad |
| removed_at / removal_reason | timestamp, nullable / text, nullable | Admin content removal (RNT-06) |

The author is the Ostad identified by `rating.ostad_account_id`; not stored separately. **A reply is removed automatically when its rating is removed** — cascade on `rating.removed_at`, so an orphaned reply cannot render (RNT-04 acceptance). Replies carry no rating value.

## report

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| reporter_account_id | uuid → user_account | Registered accounts only (RNT-07); guests cannot report |
| target_type | enum: `ostad_profile` \| `shagred_profile` \| `chat_message` \| `rating` \| `rating_reply` | The reportable surfaces, exactly (RNT-07 + CL-012) |
| target_id | uuid | Polymorphic reference to the reported entity. For `chat_message`, the **primary cited message** — it also appears in `cited_message_ids` |
| cited_message_ids | uuid[], nullable | `chat_message` reports only; **≥1**, includes `target_id`. This array is the **only** thing that unlocks the admin's chat-context read (OFR-DM: ±N neighbors, audit-logged); the thread is *derived* from these messages, never supplied — no admin surface ever accepts a thread id |
| reported_account_id | uuid → user_account | **Resolved at insert** from the target: the profile's owner, the message's sender, the rating's author, or the reply's Ostad. Stored so ADM-07's queue and ADM-10's "as reporter and reported" history are single-table reads, not four-way conditional joins |
| category | enum: `fake_profile` \| `inappropriate_content` \| `harassment` \| `scam_or_fraud` \| `safety_concern` \| `other` | RNT-07 proposed set (the list is an engineering default; the existence of a category is required) |
| detail | text, nullable | **Required when category = `other`** |
| status | enum: `open` \| `resolved` | |
| resolution | enum: `dismissed` \| `warned` \| `suspended` \| `content_removed`, nullable | ADM-07's actions; null while open |
| resolution_note | text, nullable | |
| resolved_by_admin_id | uuid, nullable → admin_account | |
| moderation_action_id | uuid, nullable → moderation_action | Set when resolution is `warned` or `suspended` (ADM-DM) |
| created_at / resolved_at | timestamps | |

**Constraints:**
- **One open report per (reporter, target):** partial unique index on (`reporter_account_id`, `target_type`, `target_id`) where `status = open`. A reporter cannot stack duplicate open reports on the same target; a new report on the same target is permitted once the prior one resolves. Anti-spam, structurally.
- **Reporter anonymity (RNT-07):** no read path returns `reporter_account_id` to any user, including the reported account — it is served only to admin surfaces (ADM-07, ADM-10).
- **Eligibility to report a `shagred_profile`** (CL-012): the reporter must be an Ostad who **holds or has held** an offer from that Shagred — a query-time check against `offer` (any status) at insert. Note the deliberate asymmetry with SGP-DM's *visibility* predicate: visibility lapses when an offer is declined or expires, but **reportability does not** — an Ostad may report a profile they can no longer see, on the basis of having seen it when they could. RNT-07 grants this explicitly; the model honors it rather than silently narrowing it.

**Every report reaches a resolution** (ADM-07): the only terminal write is `status = resolved` with a `resolution`; there is no delete.

## Effects that flow from admin resolution (not stored here)

`content_removed` on a `rating` or `rating_reply` sets that row's `removed_at` (above) and triggers aggregate recomputation. `warned` / `suspended` create a `moderation_action` (ADM-DM) referenced by `moderation_action_id`. `dismissed` writes nothing beyond this row. All four write an `admin_audit_entry` (`report_resolution`, plus `content_removal` where applicable).

## Retention behavior (OL-RET-001 mapping)

| Entity | Rule |
|---|---|
| block | **Persists through either party's 30-day deletion window** — a departing user's blocks keep protecting them while their account can still be recovered. **Purged when either party purges**: after a purge there is no profile, chat, or pin left to protect, and retaining the row would contradict clean deletion for honest users (OL-RET-001) |
| rating | **On the Shagred's purge:** `anonymized = true`; displayed as "Former Shagred"; stars, text, date, and aggregate weight retained (RNT-05); `shagred_account_id` remains a valid tombstone pointer (REG-DM). **On the Ostad's purge:** deleted with the profile — an Ostad's ratings leave with them (RNT-05). Removed ratings persist as slot-consumers until the Ostad purges |
| rating_reply | Follows its rating |
| report | **2 years after resolution** (OL-RET-001 moderation records), longer under legal hold. Account references (`reporter_account_id`, `reported_account_id`) remain valid tombstone pointers after purge. `cited_message_ids` may reference messages purged with their thread (OFR-DM: 90 days after both parties gone); the report survives on its category, resolution, and note — the same pattern as ADM-DM's `review_case` |
| Legal hold | A `legal_hold` on any account involved suspends purging of the related reports and, per the incident playbooks, the cited chat messages |

## Queries this model must serve

The block predicate (both directions, active only) — called by OSP-DM discoverability, SGP-DM visibility, MAP-DM discovery and favorites, OFR-DM thread writability and contact reveal, and offer creation; the blocker's own block list (settings); rating eligibility at submission (a `connection` exists for the pair ∧ no `rating` row exists for the pair, including removed — the unique index makes the second clause a constraint violation rather than a check); the Ostad profile's rating list (`removed_at IS NULL`, joined to reply where present, ordered `created_at desc`, reviewer name live or "Former Shagred"); aggregate recomputation per Ostad; the reports queue (`status = open`, oldest first, with reporter and `reported_account_id` context); report eligibility for `shagred_profile` targets (offer-history check, any status); duplicate-open-report refusal (partial unique index); ADM-09's block overview (most-blocked accounts, recent blocks — over active rows); report-outcome and block-rate metrics for ADM-15 (from analytics events, cross-checkable here).
