---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-15
derived_from:
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - real-estate-developer
  - ui-spec
---

# Screen: Notifications

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described four designs — one per role — differing in their notification type vocabularies, their summary cards and whether they carried a Priority Notifications section or Pinned Announcements. All four are **retired**; this is one screen absorbing the load-bearing content of each, including the **union of the four notification type vocabularies**.

## Purpose

Show every alert and system message relevant to the organization — regulatory decisions, information requests, deadlines, escrow and bank events, document expiry and system announcements — with the controls to read, act on, and dismiss them.

## Layout

```
Top Bar
↓
Notification Summary Cards
↓
Filters & Search
↓
Priority Notifications
↓
Notifications List
↓
Upcoming Deadlines
↓
Pinned Announcements
↓
Pagination
```

## Sections

### Section 1 — Notification Summary Cards

| KPI | Description |
| :---- | :---- |
| Total Notifications | All notifications, organization-wide |
| Unread | Not yet read |
| High Priority | Requiring prompt attention |
| Action Required | Carrying an action the organization must take |
| Due This Week | Tied to a deadline within seven days |
| Read | Already read |
| Archived | Dismissed to archive |

**Absorbed 2026-08-15:** the union of all four variants' cards. Each defined a similar set scoped to its own notification domain.

### Section 2 — Filters

* Search Notifications
* **Notification Type Filter** — see Section 3
* Priority Filter — Critical · High · Medium · Low
* Read Status Filter — Unread · Read · Archived
* Related Record Filter — project · property · application · sale · escrow account
* Date Range Filter
* Reset Filters

### Section 3 — Notification Types

**Absorbed 2026-08-15 — the union of all four vocabularies**, grouped by subject. As with [documents.md](documents.md)'s categories, the four lists overlapped on the general types and diverged entirely on the domain ones; picking any single list would have deleted whole classes of notification.

**Regulatory**

* Application approved · Application rejected · Application returned for correction
* Additional information requested
* Inspection scheduled
* Technical clarification requested
* Compliance deadline approaching

**Project & Registration**

* Project registration approved · Property registration approved
* Registration returned for correction
* Survey or technical review update

**Sales & Disclosure**

* Disclosure submitted · Disclosure approved · Disclosure returned
* Buyer document required or expiring

**Escrow**

* Fund release approved · Fund release returned · Funds released
* Milestone verification required · Milestone overdue
* Bank action pending · Account Trustee response received
* Escrow agreement expiring

**Documents & System**

* Document verified · Document rejected · Document expiring · Document expired
* System announcement · Scheduled maintenance
* Payment confirmation *(per-transaction gateway payment — see the relevant [service flow](../../service-flows/) for that service's payment timing)*

### Section 4 — Priority Notifications

High-priority and action-required notifications surfaced above the main list, with a primary and secondary action per item.

**Absorbed 2026-08-15** from the three operational variants. The Principal / Director variant had no equivalent — it opened directly on the full list. Kept, since surfacing urgent items is real function.

### Section 5 — Notifications List

| Column | Description |
| :---- | :---- |
| Notification | Title and body |
| Type | Notification type |
| Related Record | The record it concerns |
| Priority | Critical / High / Medium / Low |
| Received | Timestamp |
| Status | Unread / Read / Archived |
| Action | Available actions |

**Notification Actions:** Open Related Record · Mark as Read · Mark as Unread · Archive · Dismiss.

**Reconciled 2026-08-15:** the Principal / Director variant rendered this as a card list with header/body/footer rather than a table; the three operational variants used a table with columns. Kept as the **table**, which carries more per row and matches every other list screen in the module. The card layout's header/body/footer content maps onto the columns without loss.

### Section 6 — Upcoming Deadlines

Deadline-bearing notifications with due dates, sorted nearest first.

**Absorbed** from the three operational variants, each of which scoped it to its own domain. Now one list across all deadline types — the same consolidation applied on [dashboard.md](dashboard.md).

### Section 7 — Pinned Announcements

System and regulatory announcements pinned above the feed.

**Absorbed 2026-08-15** from the Principal / Director variant's *Pinned Announcements* and the operational variants' *Recent System Announcements* — the same content, pinned in one and listed in the others. Kept pinned, which is the stronger treatment.

### Read Status

Unread · Read · Archived. See [status-badges.md](../status-badges.md) — this vocabulary was already consistent across all four variants, the one legend in this screen with no conflict.

## Empty State

> No notifications. Alerts about applications, registrations, disclosures, escrow activity and documents will appear here.

## Pagination

Rows per page · Previous · Next · Page Number · Total Records

## Reused Components

See [components.md](../components.md). **Reconciled naming:** three variants listed "Notification Cards" while the Escrow Liaison's listed "Notification List" plus a separate "Priority Alert Cards" entry. With one screen and a table layout, the resolved components are **Data Table**, **Status Badges** and **Priority Alert Cards** for Section 4; `components.md` is updated.

## Validation

1. No card, column, filter, notification type or action on this screen is role-gated. Every user sees every organization notification.
2. Notification type filters are driven by subject, never by role.
3. Summary card figures must match the list's own filtered counts exactly.

## User Flow

```
Dashboard
↓
Notifications
├─ Priority item → the record it concerns
├─ List row → the record it concerns
├─ Upcoming Deadline → the record it concerns
└─ Mark Read / Archive → stays on screen
```

## Notes

* **This absorbs, rather than references, all four retired variants.**

* **The notification type vocabularies were the substantive merge**, for the same reason as [documents.md](documents.md)'s categories: four domain-specific lists with no overlap at the domain end. Unioned and grouped by subject.

* **Reconciliation — card list vs table.** The Principal / Director variant was the only one to render notifications as cards. Resolved to the table, matching every other list screen; no field was lost in the mapping.

* **Reconciliation — Pinned Announcements vs Recent System Announcements.** Same content, different prominence. Kept pinned.

* **Every user now sees every organization notification.** Previously each variant scoped the feed to its own domain, which under role-gating meant a user simply never saw other domains' alerts. There is no longer a basis for that filtering — the Notification Type and Related Record filters let anyone narrow the feed themselves.

* **What was dropped, and why.** Only the per-domain scoping of the feed and its summary cards, and the card-list layout. Nothing representing distinct work was discarded — the Principal variant's Pinned Announcements and Recent Activities are carried forward, as are the operational variants' Priority Notifications and Upcoming Deadlines.
