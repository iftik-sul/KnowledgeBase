---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - documents
---

# Screen: Documents

**Access:** Any of the institution's four Group C roles — unified access, not role-gated (`navigation.md`, confirmed 2026-08-14).

The institution's document repository. Every file attached anywhere in the module — service requests, escrow assessments, compliance reports — lives here once, and is attached to further records by reference rather than re-uploaded.

> **Corrected 2026-08-15, twice.** First pass: this screen previously scoped visibility by role. Per the unified-access model, every user sees every document at the institution. Second pass: the "Linked To" filter still named "Service Request" as a value, matching the screen deleted in favour of Submit Application — fixed below.

## Purpose

Let any institution user find a document by what it's linked to, preview it without leaving the module, and attach an existing document to a new request instead of uploading a duplicate.

## Layout

```
Top Bar
↓
Institution Context Header
↓
Filters & Search
↓
Document Table
↓
Pagination
```

Selecting a row opens a preview panel alongside the table rather than navigating away, so a user can check a document and return to the list without losing their filters.

## Sections

### Section 1 — Filters & Search

**Search by:** Document name · Linked application reference · Linked service · Uploaded by

**Filters**

* **Document Type** — Certificate of Title, Mortgage/Lease Agreement, Valuation Report, Identification, Board Resolution, Trust Account Statement, and the other types named across the eighteen services' Required Documents sections
* **Linked To** — Submit Application · Escrow Request · Compliance Report · Institution Profile (standing documents) *(corrected 2026-08-15, second pass — previously "Service Request," the deleted screen's name)*
* **Status** — Uploaded · Referenced Elsewhere · Superseded (older version)
* **Uploaded By** — dropdown, added 2026-08-15 to preserve the "my documents" narrowing role-scoping used to provide, now available as an explicit filter rather than a visibility boundary
* **Date Range** — upload date
* **Sort By** — Most recent (default) · Name · Linked application

### Section 2 — Document Table

| Column | Description |
| :---- | :---- |
| Document Name | File name or, where renamed on upload, the assigned label |
| Type | See Document Type filter above |
| Linked To | Every record this document is attached to, by reference — may be more than one |
| Version | Current version number |
| Uploaded By | Original uploader |
| Uploaded | Date |
| Status | Uploaded · Referenced Elsewhere · Superseded |
| Action | Preview |

**Row actions:** Preview · Download · View Linked Records · Replace (uploads a new version; does not alter any record that pinned the prior version — see Validation)

**Bulk actions:** Export Selected (metadata list, not the files themselves)

### Section 3 — Preview & Version History

Read-only, audit-safe preview — no redistribution controls beyond what the platform provides for any downloaded file. Version History lists every version of the document with its upload date, uploader, and which records reference which version. This is where the version-pinning rule in [validation-rules.md](../validation-rules.md#documents) becomes visible: replacing a document creates a new version; records that attached the prior version by reference keep pointing at it until their own filer re-attaches the new one.

### Section 4 — Upload

Available only from within Submit Application, an escrow assessment, or a compliance report at an editable stage — not as a standalone action on this screen. Documents.md is where uploaded files are *found* afterward, not where a new one is first added; see [components.md](../components.md#document-uploader) for the upload control itself, embedded in those other screens. *(Corrected 2026-08-15, second pass — previously "a service request," the deleted screen's name.)*

## Empty State

**Message**

> No documents match these filters. Documents are added from within Submit Application, an escrow assessment or a compliance report — this repository shows them afterward.

**Primary Button:** Clear Filters

## Reused Components

See [components.md](../components.md). Uses Institution Operations Sidebar, Top Bar, Institution Context Header, Filter Bar, Data Table, Status Badge, Pagination, Empty State.

## Validation

See [validation-rules.md](../validation-rules.md#documents). Specific to this screen:

1. **Corrected 2026-08-15** — previously scoped visibility to the linked record's own role-based visibility rule. Every document at the institution is visible to every user, since the underlying records (Applications, Escrow Requests, Compliance Reports) are themselves institution-wide now, not role-scoped.
2. Replace does not require re-confirmation from records that referenced the prior version; those records' filers see a **Newer Version Available** indicator on their own screen and choose whether to re-attach.
3. Preview, Download and Replace are available to any institution user on any visible row. **Corrected 2026-08-15** — Replace previously required the same scope that would let the user edit the linked record; that scope no longer exists.

## Role Variations

**Corrected 2026-08-15 — this section is removed.** Every institution user sees every document at the institution, institution-wide, with no role-based partitioning left to describe.

## User Flow

```
Dashboard / Applications / Escrow Request Details / Compliance Reports
↓
Documents
├─ Preview → inline panel
├─ View Linked Records → Application Details / Escrow Request Details / Compliance Report
└─ Replace → new version uploaded, linked records flagged Newer Version Available
```

## Notes

* **Visibility here now matches every other list screen in the module** — institution-wide, not role-partitioned. The previous version's role-scoped visibility model is superseded by the same 2026-08-14 unified-access decision that corrected `applications.md`.
* Document *types* are drawn from each service's own Required Documents section in `service-flows/`, and every one of those is itself marked Proposed at source — this screen inherits that status rather than asserting a document is definitely required.
* Redaction, watermarking or download restriction on sensitive documents (e.g. financial statements) is not addressed by any answer and is not proposed here.
