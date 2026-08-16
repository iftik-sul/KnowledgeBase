---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-16
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

> **Corrected 2026-08-15, twice, then again 2026-08-16.** This screen previously had a Settlement Expiry Warning category (an approved transaction inside its 30-day settlement window, B3) and a Low Balance category (the settlement account falling below a configured threshold). Both were correctly removed — B3's 30-day expiry and any standing-account balance genuinely don't apply anywhere in Group C. A second pass then added an Awaiting Counter Payment category, for Services #12 and #18, which then sourced RERA's decision *before* the customer's counter payment — leaving a genuine window where an approved application needed a payment-pending nudge. **The client has since reviewed that #12/#18 exception directly, confirmed it was an artefact of the source's original physical-counter process rather than intentional design, and normalized both services to pay before RERA's decision, the same as #13–#17.** With no Group C service reaching Approved while payment is still outstanding, the Awaiting Counter Payment category has no live scenario left to notify about, and is removed below — not merely relabelled, since the event it existed to flag no longer occurs.

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

A banner strip above the main list for the category that blocks work if missed: Approval Expiring/Expired. Shown only when it's active; the strip does not render empty.

**Corrected 2026-08-15, then 2026-08-16.** First pass: removed Settlement Expiring/Expired and Low Balance, both genuinely gone. A second pass added Awaiting Counter Payment; that addition is itself now removed (2026-08-16), following the #12/#18 payment-timing normalization — see the banner note above.

### Section 2 — Categories

| Category | Trigger | Typically relevant to |
| :---- | :---- | :---- |
| Approval Outcomes | RERAN approves, returns for correction, or rejects a submitted application | Filer, and institution-wide for the Institution Relationship Manager |
| Information Requested | RERAN raises a query on a submitted application | Filer, and institution-wide for the Institution Relationship Manager |
| Approval Expiry Warning | Institutional approval inside 60 / 14 days of expiry (answer B8, confirmed 2026-08-15) | Institution Relationship Manager |
| Escrow Routing | A new developer escrow request arrives, or one approaches its SLA | Account Trustee |
| Reporting Obligation | A compliance report or trust account statement approaches or passes its filing date | Auditing Bureau Officer |
| Certification Waiting | A record has waited in the internal certification queue past a configurable age | Any institution user |

**Removed 2026-08-15 (first pass, still correct):** Settlement Expiry Warning and Low Balance. Neither scenario can occur under the corrected payment model.

**Removed 2026-08-16:** Awaiting Counter Payment, added 2026-08-15 for Services #12/#18's then-sourced post-decision payment timing. That timing is retired — see the banner note above — and with it, the scenario this category existed to flag.

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

In-app toggle is always on for the Priority Alert category (approval expiry) and cannot be disabled — it blocks work. Every other category can be toggled off in-app and independently for email. **Proposed** — no source addresses notification preferences for any module; this section exists because Group C's deadline density makes "cannot be silenced" a deliberate design choice for the category that matters, not an oversight for the rest.

## Empty State

**Message**

> No notifications. You'll be alerted here about approval outcomes, information requests, expiry warnings, and — where applicable — escrow routing and reporting obligations.

**Corrected 2026-08-16** — "pending counter payments" removed from this message; that scenario no longer occurs anywhere in the module.

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
* **This screen's Awaiting Counter Payment history is worth recording in full, since it changed direction twice in two days.** Pass 1 (2026-08-15) removed Settlement Expiry Warning and Low Balance, correctly, since neither scenario survives the corrected payment model. Pass 2 (2026-08-15, later the same day) added Awaiting Counter Payment, after finding Services #12/#18 genuinely sourced a post-decision payment step the first pass's removal had missed. Pass 3 (2026-08-16) removes it again — this time not because the second pass misread the source, but because the client has since decided to build #12/#18 differently from what the source described, normalizing their payment timing to match #13–#17.
* The Certification Waiting age threshold is unset — no SLA is sourced for the internal certification step (see [internal-certification-queue.md](internal-certification-queue.md#notes)), so this category's trigger point remains a placeholder pending that figure.
