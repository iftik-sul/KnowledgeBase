---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/navigation.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - dashboard
---

# Screen: Dashboard

**Access:** Any authenticated Individual User — identical screen for every account, no role-based variant.

## Purpose

Give the user, on login, a single view of their own properties, leases, applications in progress, and anything requiring their action — matching `navigation.md`'s "Landing After Login" proposal directly. Unlike Group C's dashboard (one institution, many staff), this dashboard is single-account: everything shown belongs to the one person logged in, never an institution-wide view.

## Layout

```
Top Bar
↓
Quick Actions
↓
Requiring Action
↓
My Properties Summary / My Leases Summary
↓
Recent Activity
```

## Sections

### Section 1 — Quick Actions

* **Register Property Ownership (#4)**
* **Verify a Property/Developer/Project (#1–#3)**
* **Submit Complaint (#38)**

Same three actions for every user, per `navigation.md` — no per-role default, since the same person may need different actions on different days and there's no "role" to key a default off.

### Section 2 — Requiring Action

Applications with Information Requested or Returned status, PoA requests awaiting the account's confirmation (as a Pattern C/H counterparty), and services with Approved — Awaiting Payment or Audited — Awaiting Payment status (see `status-badges.md`'s two-status split) where payment hasn't been completed yet. Empty when there's nothing pending.

### Section 3 — My Properties / My Leases Summary

Count of registered properties and active leases (as landlord and as tenant, shown separately since B1 means the same account may hold both roles on different records), each linking to the full [my-properties](my-properties.md) / [my-leases](my-leases.md) screens.

**Empty state for a new account with neither:** shown as a prompt to register a property or verify one before purchasing, rather than a blank section.

### Section 4 — Recent Activity

Chronological feed of the account's own recent submissions, decisions, and payments — never another user's activity, since there is no institution-wide scope in this module.

## Empty State

**Message** (Section 2 only, when nothing needs action):

> Nothing needs your attention right now. Browse the Services Catalog to start something new.

The rest of the dashboard always renders — Quick Actions and the Properties/Leases summary remain meaningful even with an empty Requiring Action section.

## Reused Components

Sidebar, Top Bar, KPI/Summary Cards, Status Badge, Buttons.

## Validation

Every figure shown here must match its source screen exactly (My Properties, My Leases, Applications, Payment History) — this dashboard has no independent data source.

## Access

Identical for every account. No property owner, landlord, tenant, buyer, diaspora investor, or PoA holder sees a different dashboard shape — only different content, driven entirely by what's actually in their account.

## User Flow

```
Login
↓
Dashboard
├─ Quick Action → Services Catalog / Submit Application
├─ Requiring Action row → the relevant Application/PoA/Payment screen
├─ Properties/Leases Summary → My Properties / My Leases
└─ Activity Feed row → the record it concerns
```

## Notes

* No per-role landing default, matching `navigation.md`'s explicit reasoning: the account, not a declared role, is what's logged in.
* Diaspora Investor status doesn't change this dashboard's shape — `navigation.md` leaves open whether it should surface as a badge anywhere; this dashboard doesn't currently show one.
