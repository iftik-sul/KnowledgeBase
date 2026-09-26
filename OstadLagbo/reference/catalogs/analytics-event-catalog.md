---
project: OstadLagbo
type: catalog
status: current
updated: 2026-09-26
id: OL-CAT-EVT-001
derived_from: /OstadLagbo/api-overview.md
owner: Iftikher
---

# Analytics Event Catalog

Every analytics event the platform emits, in one place. The events themselves were already specified — scattered across MAP-11, OFR-08, RNT-10, OSP-12 and the ADM-12…15 requirements they feed. This collects them so the build has a single checklist and `POST /v1/events`' validator has something to validate *against* (the REG api requires the API to check each client event "against the **event catalog**" — this is that catalog).

**Naming convention:** flat `lower_snake_case`, matching what is already shipped in `packages/shared/src/events.ts` in the code repository. Names are stable contracts — an event may gain properties, **never be renamed**, because a rename silently breaks every historical series.

> **Reconciled 2026-09-26 (CL-048).** The first draft of this catalog proposed a `subject.verb_past` convention and a different name set, written without reading the code. Six client events were **already shipped**; by this catalog's own no-rename rule those names win. They are marked **shipped** below and must not change. The additions carry MAP-11's remaining instrumentation obligations in the same convention.

**Two streams, one store.** Client events are posted in batches to `POST /v1/events`; server events are written by the API at the moment of the action and are **never** accepted from a client. Both land in the ADR-002 analytics store.

**Privacy floor (NFR-06, MAP-10):** no event carries a phone, an email, a name, an identity-document reference, a chat message body, or a precise coordinate. Area is coarsened to thana/grid at ingestion. The API **strips disallowed properties rather than rejecting the batch**, so a client bug degrades data instead of losing it.

## Client events — `POST /v1/events`

Accepted from any session **or a guest** (pseudonymous `session_id`, no auth — analytics must work before login). Envelope: `{ name, ts, session_id, props }`.

| Event | Status | Fired when | Properties | Feeds |
|---|---|---|---|---|
| `map_session_start` | **shipped** | Discovery map becomes visible | `is_guest`, `area` (coarsened), `centre_source` (`gps` \| `default`) | ADM-12 demand funnel, ADM-13 |
| `map_viewport_search` | **shipped** | The map re-queries on pan or zoom | `result_count`, `area`, `zoom` | ADM-14, T-1 scraping watch |
| `category_search` | **shipped** | Keyword or category search returns | `query_script` (`latin` \| `bangla`), `result_count`, `category?`, `area` | ADM-14 |
| `zero_result_search` | **shipped** | A search/filter combination returns **0** | `category?`, `keyword_hash`, `query_script`, `gender_filter`, `area` | **ADM-14 — the recruitment compass** |
| `share_tap` | **shipped** | Share action on a profile or card | `ostad_id` | MAP-07 |
| `screen_view` | **shipped** | Any screen presented | `screen_name` | funnel diagnosis |
| `app_launch` | add | Cold start, after locale resolution | `locale`, `is_guest` | ADM-13 |
| `language_select` | add | First-launch choice or a later settings switch | `locale`, `at` (`first_launch` \| `settings`) | REG-14 adoption |
| `map_recenter` | add | Recenter-to-me tapped | — | MAP-02 usability |
| `radius_change` | add | Radius slider settles | `radius_km`, `result_count` | MAP-11, ADM-14 |
| `low_result_search` | add | Returns above zero but below the low-result threshold | as `zero_result_search`, plus `result_count` | ADM-14 |
| `filter_apply` | add | Category or gender filter set | `filter_type`, `value`, `result_count` | ADM-14 |
| `profile_view_from_pin` | add | Full profile opened from a preview card | `ostad_id`, `is_guest` | ADM-12, OSP-12 |
| `favorite_add` / `favorite_remove` | add | Favourite toggled | `ostad_id` | MAP-11 |
| `share_link_open` | add | App opened via a deep link | `ostad_id`, `had_app_installed` | MAP-07 |
| `guest_registration_prompt` | add | A guest hits an identity-gated action | `trigger` (`offer` \| `favorite` \| `other`) | ADM-12 guest→registration |

**Adding an event is a two-file change:** this catalog **and** `CLIENT_EVENT_NAMES` in `packages/shared/src/events.ts`. `POST /v1/events` drops any name absent from that constant (`events.service.ts` — *"drop unknown/server events"*), so an event added here alone is silently discarded.

**Never a client event:** anything the server can observe itself. A client-reported connection or approval is unverifiable and forgeable.

## Server events — written by the API

No client can post these. Each is written in the same transaction as the action it records, so the count cannot drift from the truth. **None is implemented yet** — Slice 0 has no offers, ratings or reports — so unlike the client names above, these are still free to change. They follow the same flat `lower_snake_case` as the client names.

### Registration and supply funnel

| Event | Fired when | Properties | Feeds |
|---|---|---|---|
| `otp_request` / `otp_verify` / `otp_fail` | OTP lifecycle | `purpose`, `attempt_no` | ADM-19, R-08 |
| `account_register` | `register/verify` commits | `role`, `locale` | ADM-12, ADM-13 |
| `onboarding_stage_complete` | Each Ostad wizard stage | `stage` (1–6) | **ADM-12 supply funnel** |
| `onboarding_submit` | Stage 6 submit | `elapsed_since_registration` | ADM-12, ADM-13 |
| `review_verdict` | Admin approves / requests changes / rejects | `verdict`, `turnaround_hours`, `resubmission_no` | ADM-12, ADM-15 (48h target) |
| `account_delete_request` / `account_purge` | Deletion path | `role`, `days_to_purge?` | ADM-18 |

### Offers, connections, chat — the success unit

| Event | Fired when | Properties | Feeds |
|---|---|---|---|
| `offer_sent` | Offer created | `ostad_id`, `shagred_id`, `category` | ADM-12 |
| `offer_accept` | **The connection.** Acceptance transaction commits | `response_hours`, `is_first_pair_connection` | **ADM-12 success unit**, OSP-12 |
| `offer_decline` / `offer_expire` / `offer_withdraw` | Terminal states | `response_hours?` | ADM-12 offer health |
| `offer_reminder_sent` | Day-5 pending reminder | — | OFR-03 efficacy |
| `contact_reveal` | Phone/email revealed on acceptance | `had_email` | ADM-12 |
| `message_sent` | Chat message committed | `kind` (`text` \| `voice`) | ADM-12 |
| `thread_freeze` | Block, suspension, or deletion freezes a thread | `cause` (`block` \| `suspension` \| `deletion`) | ADM-15 |

### Trust, safety and support

| Event | Fired when | Properties | Feeds |
|---|---|---|---|
| `rating_create` / `rating_edit` | Review submitted or edited | `stars`, `has_text` | ADM-15 |
| `rating_reply` | Ostad posts their one public reply | — | RNT-04 |
| `report_create` | Report filed | `category`, `surface` | ADM-15 |
| `report_resolve` | Admin resolves | `resolution`, `hours_open` | ADM-15 |
| `block_create` / `block_reverse` | Block toggled | — | ADM-09, ADM-15 |
| `moderation_action` | Warning, suspension, termination, reinstatement | `action`, `role` | ADM-15 |
| `ticket_create` / `ticket_reply` / `ticket_resolve` / `ticket_reopen` | Support lifecycle | `category`, `is_appeal`, `hours_open?` | ADM-15, SUP-06 |
| `broadcast_sent` | Admin broadcast dispatched | `segment`, `recipient_count` | ADM-16 |

## Derived, not emitted

These are **computed from the events above** and must not become their own events — a second write path is how two numbers that should agree stop agreeing:

- Conversion rates at every funnel stage (ADM-12)
- Activation, retention, dormancy cohorts (ADM-13)
- Coverage gaps: searched categories vs. approved-Ostad supply by area (ADM-14)
- The Ostad's private insight counts (OSP-12) — the **same** events as ADM-12, filtered to one account and stripped of identities. OSP-12's acceptance criterion ("insight counts match admin analytics for the same account and period") holds only because there is one source.
- Every target in OL-MET-001.

## Obligations

1. **Instrumented from first release.** MAP-11, OFR-08 and RNT-10 all say "these events exist from first release", and the build sequence puts the pipeline in Slice 0 — analytics are never retrofitted, because a funnel cannot be measured backwards.
2. **A new event is a catalog change first.** Adding an event without adding it here means `POST /v1/events` drops it — the validator rejects what the catalog does not list.
3. **Events are not the product state.** Inbox contents, badge counts and profile figures read from their own tables; analytics are for measurement only (OFR-DM).
