---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/services-overview.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - documents
---

# Screen: Documents

**Access:** Any authenticated Individual User — own documents only.

## Purpose

A single repository for every document the account has ever uploaded across any service, plus every output document RERAN has issued — implements the "Documents" general platform feature named in `shared-platform-features.md`.

## Layout

```
Search / Filter
↓
Document List (grouped by property/lease/application, or flat with filters)
```

## Sections

### Section 1 — Search / Filter

By document type, associated property/lease/application, and date.

### Section 2 — Document List

Every uploaded document (identification, agreements, certificates supplied as evidence) and every issued output document (Certificates of Title, judgments, reports, PoA registration confirmations), each linking back to the application or record it belongs to.

## Empty State

**Message:**

> No documents yet. Documents you upload or receive through any service will appear here.

## Reused Components

Search Bar, Document Upload.

## Validation

A document must never appear here without a traceable link back to the application, property, or lease it belongs to — this screen is a repository view, not an independent upload point.

## Access

No role variation.

## User Flow

```
Sidebar → Documents → [search/filter] → [select document] → the record it belongs to
```

## Notes

* This screen is read-heavy by design — new documents are uploaded through the wizard (`components.md`'s Document Upload component) or an Information Request response, not directly here.
