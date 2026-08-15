---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/service-flows/feature-03-respond-to-information-request.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - notifications
---

# Screen: Notifications

**Access:** Any authenticated Individual User — own notifications only.

## Purpose

Every alert the account needs to see: RERAN information requests, returned applications, decisions, PoA/counterparty confirmation requests, and payment reminders where payment falls after some or all of a decision.

## Layout

```
Filter (All / Unread)
↓
Notification List
```

## Sections

### Section 1 — Notification List

Each notification: type icon, short description, timestamp, and a link to the relevant screen — Application Details (information requests, decisions, returns), Application Details' Pay Now action (Approved — Awaiting Payment or Audited — Awaiting Payment, per `status-badges.md`'s two-status split), Power of Attorney or Application Details (Pattern C/H confirmation requests), or My Complaints (complaint resolution).

## Empty State

**Message:**

> No notifications.

## Reused Components

Status Badge (via linked records).

## Validation

Every notification must link to a real, currently-actionable state on its target screen — a notification for an already-resolved information request should not still show as actionable.

## Access

No role variation.

## User Flow

```
Top Bar (bell) or Sidebar → Notifications → [select] → the relevant screen
```

## Notes

* Counterparty confirmation notifications (Pattern C, H) are the one notification type that opens a *different* action area than the primary applicant would see on the same Application Details screen — see that screen's own notes.
