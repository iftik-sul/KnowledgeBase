---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/modules/financial-trust-institutions/payments.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - notifications
---

# Screen: Notifications

**Access:** Any of the institution's four Group C roles — unified access, not role-gated (`navigation.md`, confirmed 2026-08-14). Categories differ by typical relevance, not by access restriction — see [Categories](#section-2--categories).

## Purpose

Surface the module's deadline- and gate-driven alerts in one place. This screen exists so nothing that requires action ages quietly.

> **Corrected 2026-08-15.** This screen previously had a Settlement Expiry Warning category (an approved transaction inside its 30-day settlement window) and a Low Balance category (the settlement account falling below a configured threshold). Neither applies any more: no Group C transaction is ever approved while still awaiting payment (`open-questions.md` B1, B11), and there is no standing account to run low. Both categories are removed. The Certification Waiting category's `certify`-scope restriction is also removed — every institution user can now receive it.

## Layout

```
Top Bar
↓
Priority Alerts
↓
Category Filters
↓
Notification List
↓
Preferences
```

## Sections

### Section 1 — Priority Alerts

A banner strip above the main list for the categories that block work if missed: Approval Expiring/Expired. Shown only when at least one is active; the strip does not render empty.

**Corrected 2026-08-15** — previously also included Settlement Expiring/Expired and Low Balance. Both are removed; Approval Expiring/Expired (institutional approval, B8) is the only remaining category that blocks work.

### Section 2 — Categories

| Category | Trigger | Typically relevant to |
| :---- | :---- | :---- |
| Approval Outcomes | RERAN approves, returns for correction, or rejects a submitted application | Filer, and institution-wide for the Institution Relationship Manager |
| Information Requested | RERAN raises a query on a submitted application | Filer, and institution-wide for the Institution Relationship Manager |
| Approval Expiry Warning | Institutional approval inside 60 / 14 days of expiry (answer B8, confirmed 2026-08-15) | Institution Relationship Manager |
| Escrow Routing | A new developer escrow request arrives, or one approaches its SLA | Account Trustee |
| Reporting Obligation | A compliance report or trust account statement approaches or passes its filing date | Auditing Bureau Officer |
| Certification Waiting | A record has waited in the internal certification queue past a configurable age | Any institution user |

**Removed 2026-08-15:** Settlement Expiry Warning and Low Balance. Neither scenario can occur under the corrected payment model — see the banner note above.

**Corrected 2026-08-15** — the "Roles who receive it" column is renamed "Typically relevant to" and no longer describes an access restriction. Any institution user can receive any category; the table describes practical routing, not a permission boundary.

### Section 3 — Notification List

| Column | Description |
| :---- | :---- |
| Category | See table above |
| Message | Short description |
| Related Record | Application, escrow request, trust account or institution profile — links out |
| Date | Raised |
| Priority | Info · Warning · Error, matching the underlying status treatment in [status-badges.md](../status-badges.md) |
| Read State | Unread bolded |

**Filters:** Category · Priority · Read/Unread · Date range

**Bulk actions:** Mark All Read

### Section 4 — Preferences

In-app toggle is always on for the Priority Alert category (approval expiry) and cannot be disabled — it blocks work. Every other category can be toggled off in-app and independently for email. **Proposed** — no source addresses notification preferences for any module; this section exists because Group C's deadline density makes "cannot be silenced" a deliberate design choice for the one category that matters, not an oversight for the rest.

## Empty State

**Message**

> No notifications. You'll be alerted here about approval outcomes, information requests, expiry warnings and — where applicable — escrow routing and reporting obligations.

## Reused Components

See [components.md](../components.md). Uses Institution Operations Sidebar, Top Bar, Status Badge, Buttons.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. A notification links to the record it concerns; opening it does not mark related work as actioned — only the explicit action on the destination screen does that.
2. The Approval Expiry Warning Priority Alert category cannot be muted, per Section 4.
3. **Corrected 2026-08-15** — category delivery is no longer role-restricted; every institution user can receive every category. The typical-relevance table in Section 2 describes practical defaults, which an institution may configure, not an access rule this screen enforces.

## Role Variations

**Corrected 2026-08-15 — this section is removed.** Category relevance by role is described once, in Section 2's table, rather than repeated as four separate access-restricted blocks. Every institution user can, in principle, receive every category.

## User Flow

```
Dashboard (unread count)
↓
Notifications
├─ Open (Approval Outcome / Info Request) → Application Details
├─ Open (Expiry Warning) → Institution Profile
├─ Open (Escrow Routing) → Escrow Request Queue
├─ Open (Reporting Obligation) → Compliance Reports
├─ Open (Certification Waiting) → Internal Certification Queue
└─ Mark All Read → list refreshed
```

## Notes

* **Categories are now typical-relevance defaults, not an access-restricted list.** The previous "additive per role" framing implied a role determined what a user *could* receive; under the unified model it only describes what's practically useful to route to whom by default.
* **Settlement Expiry Warning and Low Balance are gone, not weakened.** Both described scenarios that cannot occur under the corrected payment model (`open-questions.md` B1, B11) — no Group C service is ever approved while payment is pending, and there is no standing account to run low.
* The Certification Waiting age threshold is unset — no SLA is sourced for the internal certification step (see [internal-certification-queue.md](internal-certification-queue.md#notes)), so this category's trigger point is a placeholder pending that figure.
