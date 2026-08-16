---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/screens/documents.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - documents
---

# Feature #9 – Documents

**Feature Category:** Shared Platform Features – General Platform

## 1. Feature Overview

**Documents** is the institution's document repository: every file attached anywhere in the module — service requests, escrow assessments, compliance reports — lives here once and is attached to further records by reference rather than re-uploaded.

## 2. Purpose

Let any institution user find a document by what it's linked to, preview it without leaving the module, and reuse an existing document on a new request instead of uploading a duplicate.

## 3. Description

Upload itself happens only from within Service Requests, an escrow assessment, or a compliance report at an editable stage — this feature is where uploaded files are *found* afterward, not where a new one is first added. Selecting a row opens a preview panel alongside the table, not a separate screen, so a user can check a document and return without losing filters. Replacing a document creates a new version; records that attached the prior version by reference keep pointing at it until their own filer re-attaches the new one — a version-pinning rule, not automatic propagation.

## 4. Used By

All 18 Group C services, plus escrow assessments and compliance reports — anywhere a document is attached anywhere in the module.

## 5. Prerequisites

* User is logged into a verified institution account.
* At least one document has been uploaded, from within one of the originating features.

## 6. Required Information

Search/filter by: Document name · Linked application reference · Linked service · Uploaded by · Document type · Linked To (Submit Application / Escrow Request / Compliance Report / Institution Profile) · Status (Uploaded / Referenced Elsewhere / Superseded).

## 7. Required Documents

Not applicable — this feature displays documents; it does not itself require any.

## 8. Service Fee

No fee.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Any of the institution's four Group C roles.** **Corrected 2026-08-15**: previously scoped visibility by role, since the underlying records (Applications, Escrow Requests, Compliance Reports) were themselves role-scoped; both are retired.

## 11. Expected Processing Time

Retrieval and preview are immediate.

## 12. Processing Workflow

Dashboard / Applications / Escrow Request Details / Compliance Reports
↓
Open Documents
↓
Search / Filter
↓
Preview (inline panel) **or** Download **or** View Linked Records **or** Replace
↓
*(on Replace)* New Version Uploaded, Linked Records Flagged "Newer Version Available"

## 13. Application Status Flow

Uploaded → Referenced Elsewhere *(attached to one or more records)* → Superseded *(a newer version exists; the record referencing the old version keeps pointing at it until re-attached)*

## 14. Possible Outcomes

* Document Found and Previewed
* Document Downloaded
* New Version Uploaded, Linked Records Notified

## 15. Output

* Preview panel (read-only, audit-safe)
* Version History (every version, upload date, uploader, which records reference which version)

## 16. Related Features

* Service Requests, Escrow Request Queue, Compliance Reports — the only places documents are uploaded from.

## 17. UI Screens

* Documents

## 18. API Requirements

* Retrieve Institution Documents / Search / Filter
* Retrieve Document Preview
* Retrieve Version History
* Upload New Version (Replace)
* Retrieve Linked Records
* Send Notifications *(Newer Version Available)*
* Create Audit Log

## 19. Database Entities

* Institution, Institution Staff, User
* Document, Document Version
* Linked Record *(cross-reference to Application, Escrow Request, Compliance Report, Institution Profile)*
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can view, preview, download, and replace any document at the institution.
* Upload happens only from within an originating feature, never as a standalone action here.
* Replacing a document does not retroactively alter records that referenced the prior version — they see a "Newer Version Available" indicator instead.
* All access and replacement activity is recorded in the audit log.

## 21. Business Rules

1. Documents are uploaded only from within Service Requests, an escrow assessment, or a compliance report — not from this feature directly.
2. Any of the institution's four Group C roles may preview, download, or replace any document; there is no role-based visibility restriction.
3. Replacing a document creates a new version; existing references are not automatically updated — the referencing record's filer chooses whether to re-attach.
4. Document types are drawn from each service's own Required Documents section, which is itself marked Proposed at source — this feature inherits that status.
5. All document access, upload, and replacement activity is permanently recorded in the audit trail.

## Open Questions

1. Redaction, watermarking, or download restriction on sensitive documents (e.g. financial statements) is not addressed by any answer and is not proposed here.
2. `services-overview.md` To Confirm item 2 remains open and covers this feature too.
