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

> **Corrected 2026-08-15, twice.** This screen previously had a Settlement Expiry Warning category (an approved transaction inside its 30-day settlement window, B3) and a Low Balance category (the settlement account falling below a configured threshold). Both were correctly removed — B3's 30-day expiry and any standing-account balance genuinely don't apply anywhere in Group C. **What the first pass got wrong was generalizing that removal into "no Group C service is ever approved while payment is pending."** Services #12 and #18 are the exception, found later the same day — approved, then waiting on a counter payment, same as `payments.md`, `payment-history.md`, and `assisted-service-terminal.md` needed correcting for. A new category is added below for exactly this case, distinct from the correctly-removed Settlement Expiry Warning: no expiry window, no balance — just a pending counter payment.

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

A banner strip above the main list for the categories that block work if missed: Approval Expiring/Expired, **Awaiting Counter Payment** (added — see Section 2). Shown only when at least one is active; the strip does not render empty.

**Corrected 2026-08-15, twice.** First pass: removed Settlement Expiring/Expired and Low Balance, both genuinely gone. Second pass: added Awaiting Counter Payment — #12/#18's approved-but-unpaid state is exactly the kind of thing this screen exists to surface (see the screen's own Purpose statement), and it had no category at all until now.

### Section 2 — Categories

| Category | Trigger | Typically relevant to |
| :---- | :---- | :---- |
| Approval Outcomes | RERAN approves, returns for correction, or rejects a submitted application | Filer, and institution-wide for the Institution Relationship Manager |
| Information Requested | RERAN raises a query on a submitted application | Filer, and institution-wide for the Institution Relationship Manager |
| Approval Expiry Warning | Institutional approval inside 60 / 14 days of expiry (answer B8, confirmed 2026-08-15) | Institution Relationship Manager |
| **Awaiting Counter Payment** | A #12 or #18 application is approved and waiting on the customer's counter payment (see [payment-history.md](payment-history.md), [assisted-service-terminal.md](assisted-service-terminal.md#section-3a--payment-at-counter)) | Whoever filed it, and the operator or institution user handling the counter transaction |
| Escrow Routing | A new developer escrow request arrives, or one approaches its SLA | Account Trustee |
| Reporting Obligation | A compliance report or trust account statement approaches or passes its filing date | Auditing Bureau Officer |
| Certification Waiting | A record has waited in the internal certification queue past a configurable age | Any institution user |

**Removed 2026-08-15 (first pass, still correct):** Settlement Expiry Warning and Low Balance. Neither scenario can occur under the corrected payment model.

**Added 2026-08-15 (second pass): Awaiting Counter Payment.** Trigger threshold (how long before this fires, whether it escalates) is not addressed by any source document or client decision — the same open item flagged in `payments.md`'s and `validation-rules.md`'s To Confirm sections. This category exists so the gap is at least visible, not so it's resolved.

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

In-app toggle is always on for the Priority Alert categories (approval expiry, awaiting counter payment) and cannot be disabled — both block work. Every other category can be toggled off in-app and independently for email. **Proposed** — no source addresses notification preferences for any module; this section exists because Group C's deadline density makes "cannot be silenced" a deliberate design choice for the categories that matter, not an oversight for the rest.

## Empty State

**Message**

> No notifications. You'll be alerted here about approval outcomes, information requests, expiry warnings, pending counter payments and — where applicable — escrow routing and reporting obligations.

**Corrected 2026-08-15** — "pending counter payments" added to match the new category.

## Reused Components

See [components.md](../components.md). Uses Institution Operations Sidebar, Top Bar, Status Badge, Buttons.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. A notification links to the record it concerns; opening it does not mark related work as actioned — only the explicit action on the destination screen does that.
2. The Approval Expiry Warning and Awaiting Counter Payment Priority Alert categories cannot be muted, per Section 4.
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
├─ Open (Awaiting Counter Payment) → Application Details / Payment History
├─ Open (Escrow Routing) → Escrow Request Queue
├─ Open (Reporting Obligation) → Compliance Reports
├─ Open (Certification Waiting) → Internal Certification Queue
└─ Mark All Read → list refreshed
```

## Notes

* **Categories are now typical-relevance defaults, not an access-restricted list.** The previous "additive per role" framing implied a role determined what a user *could* receive; under the unified model it only describes what's practically useful to route to whom by default.
* **Settlement Expiry Warning and Low Balance are gone, not weakened — Awaiting Counter Payment is a genuinely new category, not a renamed old one.** The two removals were correct: B3's 30-day expiry and any standing-account balance don't exist anywhere in Group C. The addition responds to a different, real fact found later the same day: #12/#18 can sit approved-but-unpaid, and this screen had nothing to say about it until now.
* The Certification Waiting age threshold is unset — no SLA is sourced for the internal certification step (see [internal-certification-queue.md](internal-certification-queue.md#notes)), so this category's trigger point is a placeholder pending that figure. **The Awaiting Counter Payment threshold has the same problem, for the same underlying reason** — no source addresses how long is too long for a customer not to return and pay.
