---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/navigation.md"
  - "RERAN/modules/individual-user/open-questions.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - leases
---

# Screen: My Leases

**Access:** Any authenticated Individual User — own leases only, shown as landlord and as tenant separately.

## Purpose

The account's registered leases. Because B1's resolution (`open-questions.md`) makes Tenant a genuine secondary applicant on Register/Renew Lease, this screen must support both a landlord's and a tenant's view of the same lease record, not just one — the exact requirement `navigation.md` flagged as settled by B1's resolution but not yet built.

## Layout

```
Tabs: As Landlord / As Tenant
↓
Lease List
↓
Per-Lease Actions
```

## Sections

### Section 1 — Tabs

Two tabs, since the same account can hold both roles across different properties. A lease where the account is landlord never appears under "As Tenant" and vice versa — no lease appears in both unless the account is, unusually, both parties to it (not prevented by source, but not a designed case either).

### Section 2 — Lease List

Each row: property address, counterparty name, lease dates, Lease Record Status badge (Active, Expiring Soon, Expired, Cancelled, In Dispute — `status-badges.md`).

### Section 3 — Per-Lease Actions

* **As Landlord:** Renew (#24), Manage (#25), Cancel (#27), Submit Dispute (#26).
* **As Tenant:** Manage (#25), Cancel (#27) — jointly with landlord per #27's Who Can Apply, Submit Dispute (#26), Request Rental Valuation (#28).

Register Lease (#23) itself doesn't appear as a per-lease action — it's reached from My Properties (as landlord, pre-filling the property) or directly from the Services Catalog (as tenant, the secondary path with no property of the tenant's own to pre-fill from).

## Empty State

**Message** (no leases in the selected tab):

> No leases registered yet [as landlord / as tenant]. Register a lease from My Properties, or from the Services Catalog if you're a tenant registering a lease you've signed.

## Reused Components

Lease Selector (this screen is its data source), Status Badge, Buttons.

## Validation

A lease must never disappear from one tab and silently reappear differently shaped in the other — the underlying record is the same regardless of which tab is viewing it; only the available actions differ by viewing role.

## Access

No role variation in the access-control sense — every account sees only its own leases in both tabs.

## User Flow

```
Sidebar → My Leases → [As Landlord / As Tenant] → [select lease] →
  Per-Lease Actions → Submit Application (lease pre-filled)
```

## Notes

* **#40 (Upload Building Details for Leasing) is documented here, not as its own screen** — per source, it's an off-platform, email-based process, not an in-app form. This screen can show a static note ("To list a new building for leasing, email building details to RERAN") but has no wizard entry point for it, matching `ui/README.md`'s Service × Form Matrix note.
* Expiring-Soon threshold (30 days) is **Proposed**, not sourced.
