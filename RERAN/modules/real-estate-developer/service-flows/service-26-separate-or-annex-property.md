---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-15
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registration-details.md"
tags:
  - real-estate-developer
  - service-flow
  - title-deed-data-services
---

# Service #26 – Separation or Annexing a Property

**Service Category:** Title Deed Data Services

## 1. Service Overview

The **Separation or Annexing a Property** service allows a developer to either split a registered property into separate parcels or merge separate parcels into one, at the property level.

> **Distinction from Service #15 (Sub-division) — resolved 2026-08-15 (issue #37).** Checked against both files' own sourced workflows rather than the category split alone: **Service #15 operates on the project** — "indicating number of phases," followed by re-uploading units through a survey company and opening a new Registrar account, the same pattern as initial project registration (Service #13). **This service operates on an already-registered property/parcel** — splitting or merging individual titled units after registration, with no Registrar-account-opening step and no phase count. These are different objects at different points in the property/project lifecycle, not the same action described twice. The source's category split (Real Estate Development Services vs. Title Deed Data Services) tracks this same distinction rather than being an arbitrary filing artifact. No client input needed on this point.

## 2. Purpose

Keep a project's property/parcel-level records accurate where physical boundaries are split or merged after initial registration.

## 3. Description

The developer submits a separation or annexation request identifying the affected property/parcels and the requested change. RERA reviews and, on approval, issues an updated Electronic Certificate of Title / Title Deed and Electronic Map reflecting the new parcel boundaries.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Project Registration Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* An existing registered property (Service #1–#6) within a registered project.
* For annexation: two or more adjoining registered properties to merge.
* For separation: a single registered property to split, with a proposed parcel plan.

## 6. Required Information

* Property Reference Number(s)
* Requested Action (Separation or Annexation)
* Proposed New Parcel Boundaries

## 7. Required Documents

> **Proposed** — not itemized in the source. Needs client confirmation.

* Proposed Parcel Plan
* Updated Survey Data
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule. Paid through the shared platform payment gateway, per transaction. There is no standing or pre-funded RERA-fee account for developers; each application is paid for on its own.

## 9. Payment Required

**Yes — after RERA's decision.** The source workflow places the audit/accept-or-reject step *before* the fee is paid; payment is what releases the output, not what admits the application to review. Paid per transaction through the shared platform payment gateway. This is a genuine payment-timing exception, verified against this service's own source row rather than inferred from neighbouring services.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**One business day**

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Open Property Registration Record
↓
Select "Separation or Annexing a Property"
↓
Provide Proposed Parcel Plan
↓
Submit Application Online
↓
RERA Reviews Application
↓
Pay Fees via Payment Gateway
↓
Electronic Certificate of Title / Title Deed Issued
↓
Electronic Map Issued

## 13. Application Status Flow

Draft
↓
Submitted
↓
Under Review
↓
Approved
↓
Payment Pending
↓
Payment Successful
↓
Updated

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Property Successfully Separated/Annexed
* Additional Information Requested
* Application Rejected

## 15. Output

* Electronic Certificate of Title / Title Deed
* Electronic Map

## 16. Related Services

* Service #15 – Real Estate Project Sub-division *(the project-level equivalent — see Section 1)*
* Service #24 – Registration/Amendment of Real Estate Project Details
* Service #25 – Issuing Map Application

## 17. UI Screens

* Property Registration Details
* Payment
* Application Submitted

## 18. API Requirements

* Retrieve Property/Parcel Records
* Submit Separation/Annexation Application
* Retrieve Application Status
* Calculate Service Fee
* Initiate Payment
* Verify Payment
* Generate Electronic Certificate of Title
* Generate Electronic Map
* Send Notifications

## 19. Database Entities

* Developer Company
* Property Unit
* Parcel
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request separation or annexation of registered property parcels.
* System validates the affected properties are registered and, for annexation, adjoining.
* Approved requests generate an updated Certificate of Title and Map.
* All activities are recorded in the audit log.
* Payment is completed after approval and before the title deed and map are issued.

## 21. Business Rules

1. Only registered properties may be separated or annexed under this service.
2. Annexation requires the affected properties to be adjoining — **proposed**, not stated explicitly in the source; needs client confirmation.
3. All submissions, reviews, and notifications must be permanently recorded in the audit trail.
4. **Distinction from Service #15 is resolved** — see Section 1. Project-level (phases, #15) vs. property-level (parcels, #26), not a duplicate.
