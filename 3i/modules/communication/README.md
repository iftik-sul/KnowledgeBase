---
project: 3i
module: communication
type: overview
status: current
updated: 2026-08-23
id: 3I-CMN-OVW-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - module
  - overview
---

# Communication

The module that runs every group chat room, moderates what's said in them, and decides who gets told what — push, email, and the in-app notification centre.

**Module status: complete.** README, data model, both requirements documents, and the full UI stage are written.

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| CHAT | Group chat and moderation | 15 |
| NOT | Notifications | 8 |

Twenty-three baseline requirements — the second-largest module after `identity-and-access`. Four existing decisions apply directly: [3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md) (profile deletion tombstones content, retains the record), [3I-DEC-020](/3i/decisions/dec-020-guardian-on-behalf-chat-retained.md) (guardian-on-behalf participation), [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) (several of this module's own strings are in the exempt set), and [3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md) (the same guardian-attribution pattern, extended to reviews — this module is where that pattern originates).

## Two Deletion Rules That Look Similar and Aren't

Easy to conflate, worth stating precisely once:

| Event | Content | Authorship |
| :---- | :---- | :---- |
| **Profile deletion** ([3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md)) | Tombstoned | "Deleted learner" |
| **Account deletion** (FR-CHAT-14, baseline as written) | Retained | "Deleted user" |

A profile losing its content but an account keeping its content is not an inconsistency — they're different events with different reasoning. Profile deletion is the guardian acting on the child's data; the tombstone is what DEC-016 decided privacy law actually calls for there. Account deletion is the adult's own data under their own authority, and FR-CHAT-14 as written never called for tombstoning it, only anonymising who said it. This module implements both, distinctly, not one rule applied twice with different labels.

## Room Scoping Resolves a Forward Reference

One room per `Regular`-type course; one room per `Batch` for `Online Class`/`Mixed` courses (§15.1). This is `learning-delivery`'s last standing forward reference — FR-BAT-02's meeting-link distribution ("posts to the batch's chat room, and by email") now has a real room to post into. A learner re-joining a later batch of the same course (FR-BAT-06) gets that batch's own room, not the earlier one — rooms are scoped to the batch instance, not the course-level relationship.

## Notification Categories — Confirmed Grouping

FR-NOT-03's "per-category opt-out" doesn't define what a category is; §16.2 lists fifteen individual trigger events. Grouped into four opt-out-able categories, confirmed 2026-08-23:

| Category | Triggers |
| :---- | :---- |
| **Learning Updates** | Enrolment confirmation, batch scheduling/rescheduling, meeting link distribution, waitlist promotion, exam availability, grading completion, certificate issue |
| **Billing** | Payment success/failure, subscription expiry, waiver decision/revocation |
| **Chat \& Moderation** | Chat mention, moderation action — **opt-out-able, confirmed, no safety exemption.** A guardian may turn these off like any other category |
| **Instructor** | Instructor approval/rejection — only ever relevant to an account that has applied |

**Account verification sits outside the category system entirely** — not a safety exemption, a functional one: opting out of your own verification email would mean never being able to verify at all, which isn't a preference, it's the platform's core registration mechanic (FR-AUTH-06). It is always sent, never toggleable, and this is a different rationale from the Chat & Moderation decision above — the two shouldn't be read as the same kind of exception.

**"Guardian notification" in §16.2's trigger list is defunct.** It originates from FR-AUTH-05's standalone-teen guardian email, which [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) removed entirely — there is no longer a registration path that produces this notification. Flagged here rather than silently dropped or silently kept as a phantom trigger with nothing behind it.

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-CMN-DM-001 | current |
| [requirements/chat-group-chat-and-moderation.md](requirements/chat-group-chat-and-moderation.md) | 3I-CMN-REQ-001 | current |
| [requirements/not-notifications.md](requirements/not-notifications.md) | 3I-CMN-REQ-002 | current |
| [ui/README.md](ui/README.md) | 3I-CMN-UI-000 | current — 7 screens, matrix, components, validation rules |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| Every chat and safeguarding age rule | [age-and-safeguarding.md §6](/3i/age-and-safeguarding.md#6-chat) |
| Guardian-on-behalf attribution | [3I-DEC-020](/3i/decisions/dec-020-guardian-on-behalf-chat-retained.md), [3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md) |
| Profile-deletion tombstoning | [3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md) |
| Exempt safeguarding strings (several are this module's own) | [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) |
| No purchase surface in push notifications | [app-store-compliance.md](/3i/app-store-compliance.md) |

## Delivery

Phase 6, Communication (§21.1) — chat, moderation, notifications.

## Forward References Resolved

| Consumer | Reference | Now resolved by |
| :---- | :---- | :---- |
| `learning-delivery` | FR-BAT-02's meeting-link chat-room distribution | ChatRoom (batch-scoped) |

## Open Against This Module

| Item | Note |
| :---- | :---- |
| Multilingual profanity filter false positives on religious vocabulary | §22.3 risk 2 — tuning time budgeted, admin override provided. Not a spec gap, a known operational risk carried forward from the baseline's own risk register |

## Change Requests Owed to the Client

None directly. The notification-category grouping is an interpretation of a baseline silence (FR-NOT-03 doesn't define "category"), not a scope change.