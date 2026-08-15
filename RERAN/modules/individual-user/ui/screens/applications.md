---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/service-flows/feature-02-track-application-status.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - applications
---

# Screen: Applications

**Access:** Any authenticated Individual User — own applications only.

## Purpose

Implements Feature #2 (Track Application Status) — a single place to search, filter, and monitor every application the account has submitted across all 41 field-collecting services (everything except #38/#39, which have their own [my-complaints.md](my-complaints.md) screen, since complaints are a distinct status vocabulary — see `status-badges.md`).

## Layout

```
Search / Filter Bar
↓
Status Summary Cards
↓
Applications Table
```

## Sections

### Section 1 — Search / Filter

By application reference number, service name, property address (where applicable), status, and date submitted — matching Feature #2's own Required Information search fields.

### Section 2 — Status Summary Cards

Counts by status group: Draft, Awaiting Action (Payment Pending, Information Requested, Awaiting Counterparty Confirmation), In Progress (Submitted, Under Review), Approved — Awaiting Payment (shown only if the account has any — see `status-badges.md`'s note that this status is genuinely conditional, not universal), Completed.

### Section 3 — Applications Table

One row per application: reference number, service name, date submitted, current status badge. Selecting a row opens [application-details.md](application-details.md).

## Empty State

**Message:**

> No applications yet. Browse the Services Catalog to get started.

## Reused Components

Status Badge, Search Bar, KPI/Summary Cards.

## Validation

Tracking is free — matches Feature #2's own explicit Section 9 ("No additional fee... Payment is not required to track an application that has already been submitted"). No payment gate of any kind belongs on this screen; that principle is exactly what `payments.md`'s Category 7 finding used to correct #39, and this screen must not reintroduce the same mistake for the 41 non-complaint services.

## Access

No role variation — every account sees only its own applications.

## User Flow

```
Sidebar → Applications → [search/filter] → [select row] → Application Details
```

## Notes

* This screen's status vocabulary is the Application Status list in `status-badges.md`, not the Complaint/Dispute or PoA lists — those have their own screens.
