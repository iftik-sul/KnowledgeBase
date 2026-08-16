---
project: RERAN
module: real-estate-service-companies
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/service-flows/"
  - "RERAN/modules/real-estate-service-companies/payments.md"
tags:
  - real-estate-service-companies
  - ui-spec
  - notifications
---

# Screen: Notifications

**Access:** Any of the company's four Group D roles — identical screen for every user.

## Purpose

Surface the module's deadline- and decision-driven alerts in one place.

> **Corrected 2026-08-16, by client decision (`open-questions.md` B4).** The Payment Due Priority Alert category, built specifically for Services #12–#15's now-retired post-decision payment timing, is removed — not merely relabelled, since the scenario it existed to flag no longer occurs.

## Layout

```
Top Bar
↓
Category Filters
↓
Notification List
```

**Corrected 2026-08-16** — the Priority Alerts banner strip is removed from the layout entirely. With Payment Due retired and no other category in this module ever having needed an un-mutable treatment, there is no remaining category that blocks work if missed — unlike Financial & Trust Institutions, which retains its own Approval Expiry Warning as a genuine Priority Alert.

## Sections

### Section 1 — Categories

| Category | Trigger | Typically relevant to |
| :---- | :---- | :---- |
| Application Outcomes | RERA approves, returns, or rejects | Filer |
| Information Requested | RERA raises a query | Filer |
| JOP Activity | A property's supervision, association, or escrow-adjacent status changes | Owners'-Association Manager |
| Licence Expiry | Company licence (Service #12) approaching expiry — **proposed**, pending confirmation of whether Group D licences expire the way institutional approvals do elsewhere in the project | Brokerage Principal |

**Corrected 2026-08-16 — Payment Due removed.** This category was checked directly against Services #12–#15's own sourced workflow text at the time it was built, not built by analogy to any other module's category — that checking was correct when done. The category is now removed because the underlying fact it was built on has since changed by client decision (`open-questions.md` B4), not because the original check was wrong.

### Section 2 — Notification List

| Column | Description |
| :---- | :---- |
| Category | See table above |
| Message | Short description |
| Related Record | Application, JOP property, or company profile — links out |
| Date | Raised |
| Priority | Info · Warning · Error |
| Read State | Unread bolded |

**Filters:** Category · Priority · Read/Unread · Date range

**Bulk actions:** Mark All Read

## Empty State

**Message**

> No notifications. You'll be alerted here about application outcomes, information requests, and JOP activity.

**Corrected 2026-08-16** — "payments due" removed from this message.

## Reused Components

Company Operations Sidebar, Top Bar, Status Badge, Buttons.

## Validation

1. Any company user can receive any category.
2. Every category is independently toggleable, in-app and by email — with the Priority Alert un-mutable exception retired along with the category it applied to.

## Access

Identical for all four roles.

## User Flow

```
Dashboard (unread count)
↓
Notifications
├─ Open (Application Outcome / Info Request) → Application Details
├─ Open (JOP Activity) → Jointly Owned Property
└─ Mark All Read → list refreshed
```

## Notes

* **This screen's Payment Due history is worth recording, since it directly mirrors a pattern Financial & Trust Institutions went through at larger scale.** That module added, then removed, an equivalent category for its own #12/#18 after their payment timing was normalized on 2026-08-16 — the same day, coincidentally, this module's own #12–#15 were normalized. Both modules ended up in the same place (no post-decision payment category) via the same mechanism (a client decision changing the underlying sourced timing), even though the two modules' services are otherwise unrelated.
