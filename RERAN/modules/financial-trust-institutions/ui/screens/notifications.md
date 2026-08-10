---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
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

**Roles:** all Group C roles — categories received differ; see [Role Variations](#role-variations)

## Purpose

Surface the module's deadline- and gate-driven alerts in one place. Group C has more of these than a typical module — two expiry windows (institutional approval, settlement) and an internal gate that can silently wait for someone — so this screen exists to make sure nothing that requires action ages quietly.

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

A banner strip above the main list for the categories that block work if missed: Approval Expiring/Expired, Settlement Expiring/Expired, Low Balance. Shown only when at least one is active; the strip does not render empty.

### Section 2 — Categories

| Category | Trigger | Roles who receive it |
| :---- | :---- | :---- |
| Approval Outcomes | RERAN approves, returns for correction, or rejects a submitted application | Mortgage Officer (own), Institution Relationship Manager (institution-wide) |
| Information Requested | RERAN raises a query on a submitted application | Mortgage Officer (own), Institution Relationship Manager (institution-wide) |
| Approval Expiry Warning | Institutional approval inside 60 / 14 days of expiry (answer B8) | Institution Relationship Manager |
| Settlement Expiry Warning | An approved transaction is inside 7 days / 24 hours of the 30-day settlement window (answer B3) | Mortgage Officer (own transaction), Institution Relationship Manager (institution-wide) |
| Low Balance | Settlement account falls below the configured threshold (see [institution-profile.md](institution-profile.md#section-3--settlement-preferences-tab)) | Institution Relationship Manager |
| Escrow Routing | A new developer escrow request arrives, or one approaches its SLA | Account Trustee |
| Reporting Obligation | A compliance report or trust account statement approaches or passes its filing date | Auditing Bureau Officer |
| Certification Waiting | A record has waited in the internal certification queue past a configurable age | Any user holding `certify` |

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

In-app toggle is always on for Priority Alert categories (approval, settlement, low balance) and cannot be disabled — these block work. Every other category can be toggled off in-app and independently for email. **Proposed** — no source addresses notification preferences for any module; this section exists because Group C's deadline density makes "cannot be silenced" a deliberate design choice for the three that matter, not an oversight for the rest.

## Empty State

**Message**

> No notifications. You'll be alerted here about approval outcomes, information requests, expiry warnings and — where applicable — escrow routing and reporting obligations.

The message lists only the categories the signed-in role actually receives — see Role Variations.

## Reused Components

See [components.md](../components.md). Uses Institution Operations Sidebar, Top Bar, Status Badge, Buttons.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. A notification links to the record it concerns; opening it does not mark related work as actioned — only the explicit action on the destination screen does that.
2. Priority Alert categories cannot be muted, per Section 4.
3. Escrow Routing and Reporting Obligation notifications are never shown to a role that cannot act on them (Mortgage Officer never sees escrow routing; Account Trustee never sees reporting obligations) — categories are additive per role, not a shared list with irrelevant rows filtered client-side.

## Role Variations

### Mortgage Officer

Receives Approval Outcomes, Information Requested and Settlement Expiry Warning, all scoped to their own filings. No institution-wide, approval-standing, or escrow categories.

### Institution Relationship Manager

Receives every category except Escrow Routing, Reporting Obligation and Certification Waiting (unless they personally hold `certify`) — institution-wide. This is the largest set of any role, matching the role being the one whose journey `role-workflows.md` describes as "driven by deadlines rather than inbound work."

### Account Trustee

Receives only Escrow Routing. No approval, settlement or reporting categories — this role owns none of the eighteen services and has no institutional-standing responsibility.

### Auditing Bureau Officer

Receives only Reporting Obligation. Does not receive Approval Outcomes or Information Requested even institution-wide, since those concern work the role has no action on — the role's read access to Applications does not extend to being notified about them.

### Any role holding `certify`

Additionally receives Certification Waiting, on top of whatever their base role's categories are.

## User Flow

```
Dashboard (unread count)
↓
Notifications
├─ Open (Approval Outcome / Info Request) → Application Details
├─ Open (Expiry Warning) → Institution Profile / Settlement Account
├─ Open (Escrow Routing) → Escrow Request Queue
├─ Open (Reporting Obligation) → Compliance Reports
├─ Open (Certification Waiting) → Internal Certification Queue
└─ Mark All Read → list refreshed
```

## Notes

* **Categories are additive per role**, not one list with client-side filtering — see Validation point 3. This keeps a role's notification set aligned with what role-workflows.md says that role's journey actually contains.
* Settlement Expiry Warning reaching the Mortgage Officer (not just the IRM) reflects answer B1's point that the officer "sees whether their own approved transaction can clear" — the notification is where that visibility becomes proactive rather than something the officer has to go looking for on Settlement Account.
* The Certification Waiting age threshold is unset — no SLA is sourced for the internal certification step (see [internal-certification-queue.md](internal-certification-queue.md#notes)), so this category's trigger point is a placeholder pending that figure.
