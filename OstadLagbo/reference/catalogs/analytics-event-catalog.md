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

**Naming convention:** `subject.verb_past`, lower snake case. Names are stable contracts — an event may gain properties, never be renamed, because a rename silently breaks every historical series.

**Two streams, one store.** Client events are posted in batches to `POST /v1/events`; server events are written by the API at the moment of the action and are **never** accepted from a client. Both land in the ADR-002 analytics store.

**Privacy floor (NFR-06, MAP-10):** no event carries a phone, an email, a name, an identity-document reference, a chat message body, or a precise coordinate. Area is coarsened to thana/grid at ingestion. The API **strips disallowed properties rather than rejecting the batch**, so a client bug degrades data instead of losing it.

## Client events — `POST /v1/events`

Accepted from any session **or a guest** (pseudonymous `session_id`, no auth — analytics must work before login). Envelope: `{ name, ts, session_id, props }`.

| Event | Fired when | Properties | Feeds |
|---|---|---|---|
| `app.launched` | Cold start, after locale resolution | `locale`, `is_guest` | ADM-13 |
| `language.selected` | First-launch choice or a later settings switch | `locale`, `at` (`first_launch` \| `settings`) | REG-14 adoption |
| `map.session_started` | Discovery map becomes visible | `is_guest`, `area` (coarsened), `centre_source` (`gps` \| `default`) | ADM-12 demand funnel, ADM-13 |
| `map.recentred` | Recenter-to-me tapped | — | MAP-02 usability |
| `map.radius_changed` | Radius slider settles | `radius_km`, `result_count` | MAP-11, ADM-14 |
| `search.performed` | Keyword search returns | `query_script` (`latin` \| `bangla`), `result_count`, `area` | ADM-14 |
| `search.zero_result` | A search/filter combination returns **0** | `category?`, `keyword_hash`, `query_script`, `gender_filter`, `area` | **ADM-14 — the recruitment compass** |
| `search.low_result` | Returns above zero but below the low-result threshold | as above, plus `result_count` | ADM-14 |
| `filter.applied` | Category or gender filter set | `filter_type`, `value`, `result_count` | ADM-14 |
| `profile.viewed_from_pin` | Full profile opened from a preview card | `ostad_id`, `is_guest` | ADM-12, OSP-12 |
| `favorite.added` / `favorite.removed` | Favourite toggled | `ostad_id` | MAP-11 |
| `share.tapped` | Share action on a profile or card | `ostad_id` | MAP-07 |
| `share_link.opened` | App opened via a deep link | `ostad_id`, `had_app_installed` | MAP-07 |
| `guest.registration_prompted` | A guest hits an identity-gated action | `trigger` (`offer` \| `favorite` \| `other`) | ADM-12 guest→registration |
| `screen.viewed` | Any screen presented | `screen_name` | funnel diagnosis |

**Never a client event:** anything the server can observe itself. A client-reported connection or approval is unverifiable and forgeable.

## Server events — written by the API

No client can post these. Each is written in the same transaction as the action it records, so the count cannot drift from the truth.

### Registration and supply funnel

| Event | Fired when | Properties | Feeds |
|---|---|---|---|
| `otp.requested` / `otp.verified` / `otp.failed` | OTP lifecycle | `purpose`, `attempt_no` | ADM-19, R-08 |
| `account.registered` | `register/verify` commits | `role`, `locale` | ADM-12, ADM-13 |
| `onboarding.stage_completed` | Each Ostad wizard stage | `stage` (1–6) | **ADM-12 supply funnel** |
| `onboarding.submitted` | Stage 6 submit | `elapsed_since_registration` | ADM-12, ADM-13 |
| `review_case.verdict` | Admin approves / requests changes / rejects | `verdict`, `turnaround_hours`, `resubmission_no` | ADM-12, ADM-15 (48h target) |
| `account.deleted_requested` / `account.purged` | Deletion path | `role`, `days_to_purge?` | ADM-18 |

### Offers, connections, chat — the success unit

| Event | Fired when | Properties | Feeds |
|---|---|---|---|
| `offer.sent` | Offer created | `ostad_id`, `shagred_id`, `category` | ADM-12 |
| `offer.accepted` | **The connection.** Acceptance transaction commits | `response_hours`, `is_first_pair_connection` | **ADM-12 success unit**, OSP-12 |
| `offer.declined` / `offer.expired` / `offer.withdrawn` | Terminal states | `response_hours?` | ADM-12 offer health |
| `offer.reminder_sent` | Day-5 pending reminder | — | OFR-03 efficacy |
| `connection.contact_revealed` | Phone/email revealed on acceptance | `had_email` | ADM-12 |
| `message.sent` | Chat message committed | `kind` (`text` \| `voice`) | ADM-12 |
| `thread.frozen` | Block, suspension, or deletion freezes a thread | `cause` (`block` \| `suspension` \| `deletion`) | ADM-15 |

### Trust, safety and support

| Event | Fired when | Properties | Feeds |
|---|---|---|---|
| `rating.created` / `rating.edited` | Review submitted or edited | `stars`, `has_text` | ADM-15 |
| `rating.replied` | Ostad posts their one public reply | — | RNT-04 |
| `report.created` | Report filed | `category`, `surface` | ADM-15 |
| `report.resolved` | Admin resolves | `resolution`, `hours_open` | ADM-15 |
| `block.created` / `block.reversed` | Block toggled | — | ADM-09, ADM-15 |
| `moderation.action` | Warning, suspension, termination, reinstatement | `action`, `role` | ADM-15 |
| `ticket.created` / `ticket.replied` / `ticket.resolved` / `ticket.reopened` | Support lifecycle | `category`, `is_appeal`, `hours_open?` | ADM-15, SUP-06 |
| `broadcast.sent` | Admin broadcast dispatched | `segment`, `recipient_count` | ADM-16 |

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
