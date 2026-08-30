---
project: OstadLagbo
module: ratings-and-trust
type: requirements
status: current
updated: 2026-08-30
id: OL-RNT-REQ-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.0.md
owner: Iftikher
---

# Ratings & Trust — Requirements

Derived from MVP Scope Baseline v1.0 §6. Governs ratings and reviews, review replies, reporting, and blocking. Aggregates render per OSP-08; reports are handled per ADM-07; block effects on chat and visibility execute per OFR-06 and SGP-05.

## RNT-01 Rating eligibility

Only a Shagred holding a **connection** (accepted offer, OFR-04) with an Ostad may rate that Ostad — **one rating per Shagred–Ostad pair**, regardless of how many connections the pair accumulates. Rating unlocks **immediately on connection**. The rating is editable by its author at any time; edits recompute the aggregate. Declined, expired, and withdrawn offers grant no rating rights (baseline §6; risk R-09 mitigation).

**Acceptance:** no rating path exists without an accepted offer; a second rating for the same pair is impossible; edits update the profile aggregate.

## RNT-02 Rating content

A rating is **1–5 stars (required) plus a written review (required**, proposed cap 600 characters). Star-only submissions are refused — the written component is what makes a review useful to the next Shagred. The review displays on the Ostad's profile with the reviewer's display name and the rating date.

## RNT-03 Aggregation

The profile shows average rating (one decimal) and review count (OSP-08), recomputed on every create, edit, anonymization, or removal. An Ostad with no reviews shows "New" rather than a zero.

## RNT-04 Ostad reply

An Ostad may post **one public reply per review** (proposed cap 600 characters), shown beneath it, editable by the Ostad. A reply is removed automatically if its review is removed. Replies carry no rating value.

**Acceptance:** a second reply to the same review is impossible; orphaned replies never render.

## RNT-05 Persistence

Reviews **persist through blocks** — blocking someone does not erase what they experienced. When a reviewer deletes their account, the review persists **anonymized** ("Former Shagred") with stars, text, and date intact, still counted in the aggregate. When an Ostad deletes their account, their profile and its reviews leave the platform together. Only admin action (RNT-06) removes a living review.

**Acceptance:** account-cycling cannot remove a review; anonymized reviews keep their aggregate weight.

## RNT-06 Review and reply moderation

Reviews and replies are reportable by any registered viewer. Report resolution for review/reply reports includes a **remove content** action (extending ADM-07's action set): removal deletes the review (and its reply) from the profile and aggregate, is recorded with a reason, and is audit-logged. Removed reviews do not restore the pair's ability to submit a fresh rating — the pair's one slot is consumed.

## RNT-07 Reporting

Any registered user can report an **Ostad profile**; chat participants can report **messages** (cited messages flow to admin per OFR-07); registered viewers can report **reviews and replies**. Guests cannot report (registration routes per MAP-03). A report carries a category — proposed set: *Fake profile / Inappropriate content / Harassment / Scam or fraud / Safety concern / Other* — and free-text detail (required for Other). Reports enter ADM-07's queue; the reporter's identity is never revealed to the reported account.

**Acceptance:** every reportable surface has a report action; reporter anonymity holds in every user-facing response.

## RNT-08 Blocking

Either party of any offer or connection can block the other; additionally, any registered user can block any Ostad from their profile, and an Ostad can block any Shagred whose offer they received. Effects, immediate and per OFR-06/SGP-05: chats freeze read-only, profile visibility severs, new offers between the pair are impossible in either direction, and each party disappears from the other's discovery surfaces (map pins, search results, favorites). Blocks are one-directional in authorship but mutual in effect, reversible only by the blocker, and managed from a private block list in settings. The blocked party is never notified.

**Acceptance:** every effect lands within one request cycle; unblocking restores discovery but not frozen chats (a new connection requires a new offer); no notification or indicator reaches the blocked account.

## RNT-09 Trust signals (cross-reference)

The verified badge is granted solely per ADM-03; profile completion per OSP-09. This module adds no further badges in MVP.

## RNT-10 Instrumentation obligations

Emitted for ADM-13/15 and ADM-09: ratings created/edited with star values, review participation among connections, reports by category and surface, report outcomes, blocks created/reversed. These events exist from first release.

## Proposed technical defaults summary

Character caps, the report category list, and "New" display mechanics are engineering defaults, changeable without founder re-approval. Eligibility (accepted offers only, immediate unlock), one-rating-per-pair, required written review, one-reply-per-review, persistence and anonymization rules, removal consuming the pair's slot, and all block effects change only with founder approval.
