---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-10
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
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

> **Conceptually close to Service #15 (Sub-division) — documented as distinct.** Service #15 sub-divides at the *project* level (splitting a project into sub-projects); this service acts at the *property* level (splitting or merging individual parcels within an already-registered property set). The source places them in different categories (Real Estate Development Services vs. Title Deed Data Services) and gives each its own row, which is treated here as evidence they are meant to be distinct rather than duplicates — but the distinction is not spelled out in the source beyond the category split, so it is flagged for client confirmation rather than asserted with full confidence.

## 2. Purpose

Keep a project's property/parcel-level records accurate where physical boundaries are split or merged after initial registration.

## 3. Description

The developer submits a separation or annexation request identifying the affected property/parcels and the requested change. RERA reviews and, on approval, issues an updated Electronic Certificate of Title / Title Deed and Electronic Map reflecting the new parcel boundaries.

## 4. Who Can Apply

* Project Registration Officer

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

Applicable according to the RERAN fee schedule.

## 9. Payment Required

Not specified in the source. **Proposed**: yes, consistent with other title-issuance services; needs client confirmation.

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

* Service #15 – Real Estate Project Sub-division *(the project-level equivalent — see the near-duplicate note in Section 1)*
* Service #24 – Registration/Amendment of Real Estate Project Details
* Service #25 – Issuing Map Application

## 17. UI Screens

* Property Registration Details
* Application Submitted

## 18. API Requirements

* Retrieve Property/Parcel Records
* Submit Separation/Annexation Application
* Retrieve Application Status
* Generate Electronic Certificate of Title
* Generate Electronic Map
* Send Notifications

## 19. Database Entities

* Developer Company
* Property Unit
* Parcel
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request separation or annexation of registered property parcels.
* System validates the affected properties are registered and, for annexation, adjoining.
* Approved requests generate an updated Certificate of Title and Map.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only registered properties may be separated or annexed under this service.
2. Annexation requires the affected properties to be adjoining — **proposed**, not stated explicitly in the source; needs client confirmation.
3. All submissions, reviews, and notifications must be permanently recorded in the audit trail.
4. **Distinction from Service #15 rests on the source's category split, not an explicit statement** — flagged for client confirmation.
