---
project: 3i
module: communication
type: requirements
status: current
updated: 2026-08-23
id: 3I-CMN-REQ-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - notifications
---

# Notifications

Baseline §16. Eight requirements. FR-NOT-03's "per-category" opt-out is interpreted, not baseline-defined — see [README.md](../README.md#notification-categories--confirmed-grouping) for the confirmed four-category grouping this document assumes throughout.

---

## Channels

| ID | Requirement |
| :---- | :---- |
| **FR-NOT-01** | Channels: **push and email**. No SMS |
| **FR-NOT-02** | An **in-app notification centre** retains history with read/unread state |

No SMS anywhere in this module's data model or screens — not merely unused, structurally absent, consistent with §23 item 12's explicit exclusion.

---

## Opt-Out

| ID | Requirement |
| :---- | :---- |
| **FR-NOT-03** | **Per-category opt-out**, at account level |

Four categories — Learning Updates, Billing, Chat \& Moderation, Instructor — confirmed 2026-08-23, folding §16.2's fifteen individual triggers down from what would otherwise be fifteen separate toggles. **Chat \& Moderation carries no safety exemption**: a guardian may opt out of chat-mention and moderation-action notifications exactly as freely as billing ones, confirmed explicitly rather than left to a default either way. **Account verification is not part of this category system at all** — always sent, never toggleable, for the functional reason (not a safety one) that opting out of your own verification email would mean never being able to verify. See [README.md](../README.md#notification-categories--confirmed-grouping) for the full trigger-to-category mapping and the now-defunct "guardian notification" trigger.

---

## Addressing and Language

| ID | Requirement |
| :---- | :---- |
| **FR-NOT-04** | Notifications route to the **account holder**. Where a notification concerns a learner profile, the profile is named in the body — *"Aisha has completed Level 2 Tajweed"* |
| **FR-NOT-05** | Notification language follows the account's locale preference |

A notification is never sent to a learner profile directly — profiles have no credentials and no independent contact channel (FR-FAM-03), so this was never really a choice, but it's worth stating plainly since "notify the learner" is an easy phrase to reach for when writing a trigger and it's never actually correct in this system.

---

## App Store Compliance

| ID | Requirement |
| :---- | :---- |
| **FR-NOT-06** | **Push notifications must not contain purchase prompts or links to checkout.** Expiry notices state that access has ended and that the account can be managed on the website, without a link |

Full detail in [app-store-compliance.md](/3i/app-store-compliance.md), which this requirement is one of three enforcement points for — not restated here.

---

## Delivery Infrastructure

| ID | Requirement |
| :---- | :---- |
| **FR-NOT-07** | Email is sent via **AWS SES (Sydney)** with SPF, DKIM, and DMARC configured on the institute's domain |
| **FR-NOT-08** | Delivery, bounce, and complaint events are logged |

FR-NOT-08 is what `NotificationDeliveryLog` exists for — see [data-model.md](../data-model.md#notificationdeliverylog). A `Notification` row tracks whether sending was *attempted*; the delivery log tracks what actually *happened* to it, and the two are deliberately separate records.

---

## Triggers (§16.2)

Account verification (always-on, outside the category system), enrolment confirmation, batch scheduling and rescheduling, meeting link distribution, waitlist promotion, exam availability, grading completion, certificate issue, payment success and failure, subscription expiry, waiver decision and revocation, chat mention, moderation action, instructor approval or rejection.

**"Guardian notification" is omitted from this list — it is defunct**, per [README.md](../README.md#notification-categories--confirmed-grouping): [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) removed the FR-AUTH-05 registration path that used to produce it. Fourteen live triggers remain, mapped to the four categories above.

---

## Acceptance Criteria

1. Opting out of a category stops both push and email for that category only — other categories, and account verification, are unaffected.
2. A subscription expiry push contains no URL and no price.
3. Bounces are visible in the admin email log.
4. Opting out of Chat \& Moderation successfully stops a chat-mention notification, with no override or exemption applied.
5. A notification concerning a specific profile names that profile in the body, and is still routed to the account holder, never to the profile.
6. Switching account locale changes the language of subsequently sent notifications; already-sent ones are unaffected.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-CMN-DM-001](../data-model.md) |
| Category grouping, defunct trigger | [README.md](../README.md#notification-categories--confirmed-grouping) |
| App store compliance | [app-store-compliance.md](/3i/app-store-compliance.md) |
| Group chat and moderation | [3I-CMN-REQ-001](chat-group-chat-and-moderation.md) |