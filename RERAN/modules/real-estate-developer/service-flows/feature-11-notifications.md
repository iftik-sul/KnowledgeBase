---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/notifications.md"
tags:
  - real-estate-developer
  - shared-feature
  - notifications
---

# Feature #11 – Notifications

**Feature Category:** Shared Platform Features – General Platform

## 1. Feature Overview

**Notifications** surfaces every alert relevant to the organization — regulatory decisions, information requests, deadlines, escrow and bank events, document expiry, and system announcements — with the union of what were four separate, domain-specific notification-type vocabularies.

## 2. Purpose

Give any developer user a single feed of every organization notification, with the controls to read, act on, archive, and dismiss them, rather than being limited to whichever domain a prior role-based design happened to surface.

## 3. Description

Rebuilt 2026-08-15 from four role-specific designs into one, for the same underlying reason as Documents' category merge: the four prior notification-type vocabularies overlapped at the general end and diverged entirely at the domain end (regulatory, project/registration, sales/disclosure, escrow, documents/system) — unioned rather than chosen between. The card-list layout used by one prior variant is resolved to a table, matching every other list screen in the module; no field was lost in the mapping. Every user now sees every organization notification — previously each variant scoped the feed to its own domain, meaning a user simply never saw other domains' alerts.

## 4. Used By

Not tied to any single numbered service — cuts across every domain workspace and general-platform feature.

## 5. Prerequisites

* User is logged into a registered developer company account.

## 6. Required Information

Filter by: Notification Type, Priority (Critical/High/Medium/Low), Read Status (Unread/Read/Archived), Related Record type, date range.

## 7. Required Documents

None.

## 8. Service Fee

No fee.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Any of the developer's four Group B roles** — no role-based delivery restriction; every organization notification is visible to every user.

## 11. Expected Processing Time

Immediate on trigger.

## 12. Processing Workflow

Triggering Event (regulatory decision, information request, deadline approaching, escrow/bank event, document expiry, system announcement)
↓
Notification Raised, Typed, Prioritized
↓
Surfaced in Priority Notifications (if high-priority/action-required) and the Main List
↓
User Opens → Routes to the Concerned Record
↓
Mark as Read / Unread **or** Archive **or** Dismiss

## 13. Application Status Flow

Unread → Read → Archived. This is the one status vocabulary on this screen that was already consistent across all four prior variants, with no conflict to reconcile.

## 14. Possible Outcomes

* Notification Raised and Delivered
* Marked Read / Archived / Dismissed

## 15. Output

* Notification list entry: title, body, type, related record link, priority, received timestamp, status

## 16. Related Features

* Every other feature is a potential source: Applications, Projects, Property Registrations, Escrow Management, Fund Release Request, Sales & Disclosures, Documents, Company Profile.

## 17. UI Screens

* Notifications

## 18. API Requirements

* Retrieve Notifications / Filter
* Mark as Read / Unread / Archive / Dismiss
* Retrieve Priority Notifications, Upcoming Deadlines, Pinned Announcements
* Create Audit Log

## 19. Database Entities

* Developer Company, User
* Notification, Notification Type
* Audit Log

## 20. Acceptance Criteria

* Any of the developer's four Group B roles can view and act on every organization notification.
* All domain notification types remain available — no type dropped for belonging to one prior role's vocabulary.
* Summary card figures match the list's own filtered counts exactly.
* Opening a notification routes to the concerned record without marking any underlying work as actioned — only an explicit action on the destination screen does that.

## 21. Business Rules

1. Any of the developer's four Group B roles may receive and act on any notification — no per-domain visibility restriction.
2. Notification type filters are driven by subject, never by role.
3. Summary card figures must match the list's own filtered counts exactly.
4. Opening a notification does not mark related work as actioned.
5. All notification activity is permanently recorded in the audit trail.

## Open Questions

1. Same adoption question as Feature #1 — needs client confirmation.
