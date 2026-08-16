---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/screens/notifications.md"
  - "RERAN/modules/financial-trust-institutions/payments.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - notifications
---

# Feature #11 – Notifications

**Feature Category:** Shared Platform Features – General Platform

## 1. Feature Overview

**Notifications** surfaces the module's deadline- and gate-driven alerts in one place, so nothing that requires action ages quietly: approval outcomes, information requests, approval expiry, escrow routing, reporting obligations, and certification waiting.

## 2. Purpose

Give any institution user a single place to see what needs attention across every Group C function, with the category that blocks work (approval expiry) surfaced as a Priority Alert that cannot be muted.

## 3. Description

Six categories exist: Approval Outcomes, Information Requested, Approval Expiry Warning, Escrow Routing, Reporting Obligation, Certification Waiting. Each has a "typically relevant to" role, but this is routing convention, not an access restriction — any institution user can receive any category. One category (Approval Expiry Warning) sits in a Priority Alerts strip above the main list and cannot be disabled; every other category can be toggled off in-app and independently for email.

**Corrected 2026-08-16.** This feature previously carried a seventh category, "Awaiting Counter Payment," as a second un-mutable Priority Alert — built for Services #12 and #18, which then sourced a payment step falling *after* RERA's decision, leaving a window where an approved application genuinely needed a payment-pending nudge. The client has since reviewed that #12/#18 exception directly, confirmed it was an artefact of the source's original physical-counter process rather than intentional design, and normalized both services to pay before RERA's decision, the same as #13–#17. With no Group C service reaching Approved while payment is still outstanding, there is no longer a scenario for this category to notify about — it is removed below, not merely relabelled, since the underlying event it existed to flag no longer occurs.

## 4. Used By

Cuts across every Group C service and feature — not tied to any single one.

## 5. Prerequisites

* User is logged into a verified institution account.

## 6. Required Information

Filter by: Category · Priority (Info / Warning / Error) · Read/Unread · Date range.

## 7. Required Documents

None.

## 8. Service Fee

No fee.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Any of the institution's four Group C roles** — no role-based delivery restriction; the "typically relevant to" table describes practical routing defaults only.

## 11. Expected Processing Time

Immediate on trigger.

## 12. Processing Workflow

Triggering Event (approval decision, info request, expiry threshold crossed, escrow request arrives, reporting deadline approaches, certification ages)
↓
Notification Raised, Categorized, Prioritized
↓
Delivered In-App (and Email, where enabled)
↓
User Opens → Routes to the Concerned Record (Application Details / Institution Profile / Escrow Request Queue / Compliance Reports / Internal Certification Queue)

## 13. Application Status Flow

Unread → Read *(opening the notification; the underlying record's own status is unaffected — only the destination screen's own action changes that)*

## 14. Possible Outcomes

* Notification Raised and Delivered
* Marked Read (individually or via Mark All Read)

## 15. Output

* Notification list entry: category, message, related record link, date, priority, read state

## 16. Related Features

* Every other feature is a potential source: Service Requests, Applications, Internal Certification Queue, Escrow Request Queue, Trust Accounts, Compliance Reports, Institution Profile, Payment History.

## 17. UI Screens

* Notifications

## 18. API Requirements

* Retrieve Notifications / Filter
* Mark Read / Mark All Read
* Update Notification Preferences (per-category in-app/email toggle, except the one un-mutable Priority Alert category)
* Create Audit Log

## 19. Database Entities

* Institution, Institution Staff, User
* Notification, Notification Preference
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can receive and act on any notification category.
* Approval Expiry Warning cannot be muted, in-app or by email.
* Every other category can be independently toggled off in-app and by email.
* Opening a notification navigates to the concerned record without marking any underlying work as actioned — only an explicit action on the destination screen does that.
* All notification activity is recorded in the audit log.

## 21. Business Rules

1. Category delivery is not role-restricted — the "typically relevant to" table is a routing default, not an access rule.
2. Approval Expiry Warning is a Priority Alert and cannot be muted.
3. Every other category is independently toggleable, in-app and by email.
4. Opening a notification does not mark related work as actioned.
5. All notifications and preference changes are permanently recorded in the audit trail.

## Open Questions

1. What trigger threshold should Certification Waiting use — how long before it fires, and does it escalate? Not addressed by any source or client decision; a placeholder pending a client figure, same underlying gap as the SLA question on Internal Certification Queue.
2. `services-overview.md` To Confirm item 2 remains open and covers this feature too.
