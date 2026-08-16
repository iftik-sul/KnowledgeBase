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

## Layout

```
Top Bar
↓
Priority Alerts
↓
Category Filters
↓
Notification List
```

## Sections

### Section 1 — Priority Alerts

A banner strip for the category that blocks work if missed: **Payment Due** — Services #12–#15 only, once RERA accepts an application and payment becomes the next required action. This category cannot be muted, matching the reasoning Financial & Trust Institutions applies to its own un-mutable Approval Expiry Warning — a real, sourced scenario where inaction has a consequence, not a generic "stay informed" nudge.

### Section 2 — Categories

| Category | Trigger | Typically relevant to |
| :---- | :---- | :---- |
| Application Outcomes | RERA approves, returns, or rejects | Filer |
| Information Requested | RERA raises a query | Filer |
| **Payment Due** | Services #12–#15 accepted, payment now required | Brokerage Principal |
| JOP Activity | A property's supervision, association, or escrow-adjacent status changes | Owners'-Association Manager |
| Licence Expiry | Company licence (Service #12) approaching expiry — **proposed**, pending confirmation of whether Group D licences expire the way institutional approvals do elsewhere in the project | Brokerage Principal |

### Section 3 — Notification List

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

> No notifications. You'll be alerted here about application outcomes, information requests, payments due, and JOP activity.

## Reused Components

Company Operations Sidebar, Top Bar, Status Badge, Buttons.

## Validation

1. Any company user can receive any category.
2. The Payment Due Priority Alert cannot be muted.
3. Every other category is independently toggleable, in-app and by email.

## Access

Identical for all four roles.

## User Flow

```
Dashboard (unread count)
↓
Notifications
├─ Open (Application Outcome / Info Request) → Application Details
├─ Open (Payment Due) → Application Details, Complete Payment action
├─ Open (JOP Activity) → Jointly Owned Property
└─ Mark All Read → list refreshed
```

## Notes

* **Payment Due is a genuinely sourced category, checked directly against Services #12–#15's own workflow text** — not built by analogy to Financial & Trust Institutions' now-retired Awaiting Counter Payment category (see that module's own three-pass correction history for why that comparison should be treated with caution rather than copied uncritically). This module's version rests on a different, still-current sourced fact: #12–#15 genuinely pay after acceptance, and that timing has not been normalized away the way Financial & Trust Institutions' #12/#18 was.
* If `open-questions.md` B4 resolves toward normalizing #12–#15 to pay-before-lodging, this category becomes moot the same way Financial & Trust Institutions' equivalent did — flagged for whoever revisits this screen if that happens.
