---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/documents.md"
tags:
  - real-estate-developer
  - shared-feature
  - documents
---

# Feature #8 – Documents

**Feature Category:** Shared Platform Features – General Platform

## 1. Feature Overview

**Documents** is the organization-wide document repository spanning every domain workspace — projects, property registrations, sales disclosures, escrow accounts, and regulatory applications — with a category taxonomy that is the union of what each domain actually needs, not a single generic list.

## 2. Purpose

Let any developer user upload, find, preview, replace, and track verification of any document, across any domain, from one place.

## 3. Description

Rebuilt 2026-08-15 from four domain-specific designs into one, with the category taxonomy as the substantive merge: the four prior variants shared general categories (Company Documents, Compliance Documents, Supporting Documents) but had **zero overlap** at the domain end — sales agreements and buyer identification existed only in the sales variant; engineer certificates and quantity surveyor reports only in escrow; survey and technical documents only in registration. Picking one list would have deleted two entire domains' vocabulary; all are kept, grouped by what the document attaches to (Organization, Project & Registration, Sales & Disclosure, Escrow, Other). Two sections that looked mutually exclusive across variants — Pending Verification and Document Analytics — are both kept; the either/or was a consequence of one prior variant having no actions to offer, not a real choice.

## 4. Used By

All 27 numbered services, plus Sales & Disclosures — anywhere a document is attached anywhere in the module.

## 5. Prerequisites

* User is logged into a registered developer company account.
* At least one document has been uploaded, from within an originating feature or directly via Upload Documents.

## 6. Required Information

Search/filter by: Category, Project, Property, Application/Application Type, Buyer, Disclosure, Escrow Account, Fund Release, Financial Institution, Verification Status, Expiry Status, Uploaded By, upload date range.

## 7. Required Documents

Not applicable — this feature displays and manages documents; it does not itself require any to be used.

## 8. Service Fee

No fee.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Any of the developer's four Group B roles.** Rebuilt 2026-08-15 from four role-specific designs (one repository view, three operational workspaces) into one; the repository variant's prior view-only restriction is retired.

## 11. Expected Processing Time

Retrieval, preview, and upload are immediate.

## 12. Processing Workflow

Dashboard / any domain workspace
↓
Open Documents
↓
Search / Filter / Select Category
↓
Upload **or** Preview **or** Replace **or** Resubmit (per document status)
↓
*(on Replace/Resubmit)* Document Status Updated, Linked Record's Filer Notified

## 13. Application Status Flow

Draft → Pending Verification → Verified, or → Information Requested / Returned → Replace/Resubmit → Pending Verification, or → Rejected

**Document status vocabulary is a pre-existing, unreconciled source conflict**, flagged in `status-badges.md` and not caused by or resolved through this feature's own 2026-08-15 rebuild — carried forward as a known gap, not silently resolved.

## 14. Possible Outcomes

* Document Uploaded / Verified
* Verification Returned, Replacement Requested
* Document Rejected

## 15. Output

* Verified document, available for download and linked-record reference
* Recent Document Activity entry (uploaded, replaced, verification started, verified, rejected), attributed to acting user and role

## 16. Related Features

* Projects, Property Registrations, Escrow Management, Fund Release Request, Sales & Disclosures — the domain workspaces documents are typically uploaded from and linked to.

## 17. UI Screens

* Documents

## 18. API Requirements

* Retrieve Organization Documents / Search / Filter
* Upload / Replace / Resubmit Document
* Retrieve Document Preview, Category Taxonomy
* Retrieve Pending Verification Queue, Document Analytics
* Retrieve Recent Document Activity
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Developer Company, User
* Document, Document Category, Document Version
* Linked Record *(cross-reference to Project, Property Registration, Sale, Disclosure, Escrow Account, Fund Release, Application)*
* Audit Log

## 20. Acceptance Criteria

* Any of the developer's four Group B roles can view, upload, preview, and replace any document.
* All domain category taxonomies remain available — no category dropped for belonging to one prior role's variant.
* Summary card figures match the table's own filtered counts exactly.
* All document activity is recorded in the audit log, including the acting user's role.

## 21. Business Rules

1. Any of the developer's four Group B roles may act on any document — no per-domain or per-role visibility restriction.
2. Row actions depend on document status, never on who is viewing.
3. Domain filters (Buyer, Escrow Account, etc.) apply only where the document category carries that value — never role-conditional.
4. Summary figures must match the table's own filtered counts exactly.
5. All document activity is permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. The source's own document-status vocabulary conflict (three unreconciled lists, per `status-badges.md`) is pre-existing and not resolved by this document — needs source clarification, not a merge decision.
2. Same adoption question as Feature #1 — needs client confirmation.
