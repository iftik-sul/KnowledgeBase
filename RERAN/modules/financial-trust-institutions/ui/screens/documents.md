---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - documents
---

# Screen: Documents

**Roles:** Mortgage Officer (own-linked) · Institution Relationship Manager (institution-wide) · Account Trustee (escrow-linked) · Auditing Bureau Officer (institution-wide, read)

The institution's document repository. Every file attached anywhere in the module — service requests, escrow assessments, compliance reports — lives here once, and is attached to further records by reference rather than re-uploaded.

## Purpose

Let a user find a document by what it's linked to, preview it without leaving the module, and — where their scope permits — attach an existing document to a new request instead of uploading a duplicate.

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
* **Linked To** — Service Request · Escrow Request · Compliance Report · Institution Profile (standing documents)
* **Status** — Uploaded · Referenced Elsewhere · Superseded (older version)
* **Uploaded By** — dropdown
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

Available only from within a service request, escrow assessment or compliance report at an editable stage — not as a standalone action on this screen. Documents.md is where uploaded files are *found* afterward, not where a new one is first added; see [components.md](../components.md#document-uploader) for the upload control itself, embedded in those other screens.

## Empty State

**Message**

> No documents match these filters. Documents are added from within a service request, escrow assessment or compliance report — this repository shows them afterward.

**Primary Button:** Clear Filters

## Reused Components

See [components.md](../components.md). Uses Institution Operations Sidebar, Top Bar, Institution Context Header, Filter Bar, Data Table, Status Badge, Pagination, Empty State.

## Validation

See [validation-rules.md](../validation-rules.md#documents). Specific to this screen:

1. Visibility follows the linked record's own visibility rules, not a separate document-level permission — see Role Variations. A user who cannot open an application cannot see its documents here either, even if the search matches.
2. Replace does not require re-confirmation from records that referenced the prior version; those records' filers see a **Newer Version Available** indicator on their own screen and choose whether to re-attach.
3. Preview and Download are available to any role that can see the row; only Replace requires the same scope that would let the user edit the linked record.

## Role Variations

### Mortgage Officer

Sees documents linked to applications they filed, plus anything they've uploaded that is not yet linked to a submitted record.

### Institution Relationship Manager

Sees every document at the institution, matching their institution-wide visibility elsewhere in the module.

### Account Trustee

Sees documents linked to escrow requests and trust account records they have worked, not the institution's Group C service-request documents — the same boundary [escrow-request-queue.md](escrow-request-queue.md) draws around this role's work.

### Auditing Bureau Officer

Institution-wide, read-only — consistent with the read access this role has to Applications and Trust Accounts for the same audit reason.

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

* **Visibility here is scoped, not uniform.** `navigation.md`'s sidebar matrix currently shows this row as full access (`●`) for all four roles with no required scope, which reads as institution-wide visibility for everyone. That's wrong once a document-linked view exists to compare it against — a Mortgage Officer should not browse another officer's mortgage documents, or the Account Trustee's escrow assessments, freely. `navigation.md` has been corrected in this pass; see the PR description.
* Document *types* are drawn from each service's own Required Documents section in `service-flows/`, and every one of those is itself marked Proposed at source — this screen inherits that status rather than asserting a document is definitely required.
* Redaction, watermarking or download restriction on sensitive documents (e.g. financial statements) is not addressed by any answer and is not proposed here.
