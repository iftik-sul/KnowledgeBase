---
project: RERAN
module: real-estate-service-companies
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/service-flows/"
tags:
  - real-estate-service-companies
  - ui-spec
  - documents
---

# Screen: Documents

**Access:** Any of the company's four Group D roles — identical screen for every user.

## Purpose

The company's document repository — every file attached anywhere in the module, findable by what it's linked to, previewable without leaving the module.

## Layout

```
Top Bar
↓
Document Summary Cards
↓
Filters & Search
↓
Documents Table
↓
Pagination
```

## Sections

### Section 1 — Document Summary Cards

| KPI | Description |
| :---- | :---- |
| Total Documents | Company-wide |
| Pending Verification | Awaiting RERA review |
| Linked to JOP Properties | Documents attached to a Section-1-registered property |
| Linked to Practice Cards | Documents attached to an agent's card record |

### Section 2 — Filters & Search

**Search by:** Document name · Linked application reference

**Filters:** Category · Linked Record Type (Application · JOP Property · Practice Card · Management Contract) · Verification Status · Uploaded By

### Section 3 — Document Categories

Grouped by what the document attaches to, following the pattern established in Real Estate Developer and Financial & Trust Institutions' equivalent screens:

**Company / Licensing**

* Certificate of Incorporation · Company Licence · Permit Documents · Practice Card Evidence

**Jointly Owned Property**

* JOP Registration Documents · Owners' Association Records · Escrow Account Documents · Auditor Appointment Records

**Rental**

* Management Contracts · Tenancy System User Records

**Transaction**

* Auction Permits · Auction Sale Records

**Dispute**

* Dispute Filings · Judgment Documents

**Other**

* Supporting Documents · Other

### Section 4 — Documents Table

| Column | Description |
| :---- | :---- |
| Document Name | Uploaded document |
| Category | Document category |
| Linked Record | Application · JOP Property · Practice Card · Management Contract |
| Uploaded By | Company user, and the role they held at the time |
| Upload Date | |
| Verification Status | |
| Action | View · Download · Replace |

**Row actions** depend on document status, never on who is viewing.

## Empty State

**Message**

> No documents uploaded yet. Upload the documents required to support your JOP registrations, licensing applications, and other filings.

**Primary Button:** Upload Documents

## Reused Components

Company Operations Sidebar, Top Bar, KPI Summary Cards, Filter Bar, Data Table, Status Badge, Pagination, Empty State.

## Validation

1. No card, column, filter, category, or action on this screen is role-gated.
2. Summary card figures must match the table's own filtered counts exactly.

## Access

Identical for all four roles.

## User Flow

```
Dashboard / Applications / JOP Register
↓
Documents
├─ Upload Documents → upload flow
├─ Row → preview / download
└─ Linked Record → that record's own detail screen
```

## Notes

* **This module's document lists are notably shorter, per service, than Financial & Trust Institutions' or Real Estate Developer's** — most Group D service-flow files mark their entire Required Documents section as Proposed rather than sourced, since the source table rarely itemizes documents beyond "attach documents." The category taxonomy above is built from what's plausible, not from a rich sourced list the way Financial & Trust Institutions' escrow document categories were.
