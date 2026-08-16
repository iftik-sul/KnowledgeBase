---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/property-registrations.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
tags:
  - real-estate-developer
  - shared-feature
  - domain-workspace
---

# Feature #3 – Property Registrations

**Feature Category:** Shared Platform Features – Domain Workspace

## 1. Feature Overview

**Property Registrations** is the domain workspace for registering individual unit sales, rent-to-own arrangements, usufruct, and related amendments within an already-registered project — the module's highest-volume domain workspace, covering seven of the module's 27 services.

## 2. Purpose

List the organization's property registrations and provide both the monitoring view and the operational controls to prepare, submit, correct, and track them.

## 3. Description

Like Projects, this screen merged two prior role-based variants into one, with row actions governed by registration status rather than viewer identity. Registration Insights (approval rate, average approval time, quarterly volume, distribution by property type) is carried forward from the monitoring variant. Confirmed directly against two services' own `derived_from`: Service #1 (Register Initial Sale) and Service #6 (Register Sale Associated with an Initial Mortgage) both cite this screen and its Details counterpart, not [sales-and-disclosures.md](../ui/screens/sales-and-disclosures.md) — resolving the ambiguity flagged in [shared-platform-features.md](../shared-platform-features.md)'s prior version.

**A worked correction found during this write-up, worth noting:** Service #6's own "Who Can Apply" section was found to attribute typical filing to the wrong role (Project Registration Officer) before this document was written; checked against `roles-and-responsibilities.md`'s worked examples and the master table's Responsible Role column, and corrected to Sales & Disclosure Officer. This has no access consequence — any of the four roles may file regardless — but is worth knowing before trusting other services' "typically filed by" language at face value.

## 4. Used By

Services #1–#7, confirmed via service-01 and service-06's `derived_from`:

* Register Initial Sale
* Register Initial Rent-to-Own
* Register Initial Usufruct
* Amend Initial Procedures Data
* Complete Initial Procedures Data
* Register Sale Associated with an Initial Mortgage
* Transfer Registration Fees Between Properties

## 5. Prerequisites

* User is logged into a registered developer company account.
* The relevant project is already registered (via Feature #2 – Projects) and the unit exists within that project's approved unit list.

## 6. Required Information

Varies by selected service — typically Project Reference Number, Unit/Property Identifier, purchaser or counterparty information, and (for Service #6) mortgage institution details. See each service's own Section 6. Search/filter on this screen: Property, project, property type, registration status, date range.

## 7. Required Documents

Varies by service; not itemized in source beyond "attach documents" for most — flagged Proposed on each service's own Section 7.

## 8. Service Fee

Set by the selected service.

## 9. Payment Required

**Yes for confirmed services (e.g. #1, #6) — before RERA's decision.** Both services checked directly place payment at submission, ahead of review. Not confirmed uniform across all seven; consult the selected service's own Section 9.

## 10. Processing Authority

**Compliance & Escrow Auditor.** Any of the developer's four Group B roles may file, though Service #6's typical-practice attribution (Sales & Disclosure Officer, corrected as above) suggests this cluster's practical pattern differs from Projects'.

## 11. Expected Processing Time

Set by the selected service — 6 business days for Service #6; see others' own Section 11.

## 12. Processing Workflow

Dashboard
↓
Open Property Registrations
↓
Register New Property *(select project unit, enter purchaser/mortgage information as required by the selected service)*
↓
Upload Required Documents
↓
Select Payment Method → Submit
↓
RERA Reviews
↓
Registration Certificate Issued *(and Electronic Map, for mortgage-linked sales)*

## 13. Application Status Flow

Draft → Submitted → Under Review → Information Requested / Returned → Approved → Registered

**Reconciled 2026-08-15** to a 7-state union (Draft, Submitted, Under Review, Information Requested, Returned, Approved, Rejected) — a clean subset resolution, unlike Projects' genuine conflict, since one prior variant's 6 states were a strict subset of the other's 7.

## 14. Possible Outcomes

* Registration Approved
* Information Requested
* Application Returned
* Application Rejected
* Payment Failed

## 15. Output

Registration Certificate; Mortgage Provisional Registration Certificate and Electronic Map for Service #6 specifically. Varies by service — see each service's own Section 15.

## 16. Related Features

* Applications *(Feature #1 — post-submission tracking, response, resubmission)*
* Escrow Management *(Feature #4/#5 — where a sale's escrow-related consequences are handled, distinct from the sale registration itself)*
* Financial & Trust Institutions Service #3 – Mortgage Registration *(cross-module, for Service #6 specifically)*

## 17. UI Screens

* Property Registrations
* Property Registration Details

## 18. API Requirements

* Retrieve Project Units / Validate Unit Availability
* Validate Purchaser / Mortgage Institution (where applicable)
* Upload Documents
* Calculate Service Fee / Initiate Payment / Verify Payment
* Submit Registration
* Generate Certificate(s)
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Developer Company, Project, Property Unit, User
* Purchaser, Mortgage Institution *(where applicable)*
* Property Sale, Mortgage, Application
* Document, Payment, Payment Transaction
* Notification, Audit Log

## 20. Acceptance Criteria

* Any of the developer's four Group B roles can register a property against an existing project.
* System validates the unit belongs to a registered project and is available.
* Row actions are governed by registration status, never by who is viewing.
* Registration Insights figures match the table's own filtered counts exactly.
* All registration activity is recorded in the audit log, including the acting user's role.

## 21. Business Rules

1. Only a unit belonging to a registered project (Feature #2) may be registered under this feature.
2. Any of the four Group B roles may file, regardless of typical practice.
3. Payment must be completed before regulatory review, for the services confirmed to require it.
4. Every registration receives a unique reference number.
5. All submissions, approvals, payments, and notifications are permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. Payment timing is confirmed for Services #1 and #6 specifically (before decision); not independently verified for #2–#5, #7 — consult each service's own file rather than assuming uniformity across the cluster.
2. Same adoption question as Feature #1 — needs client confirmation.
