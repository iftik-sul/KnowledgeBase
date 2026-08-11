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
  - real-estate-development-services
---

# Service #4 – Amend Initial Procedures Data

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Amend Initial Procedures Data** service allows a developer to correct or update the data submitted under any of the initial (provisional) registration services — sale, rent-to-own, or usufruct — before the registration is finalized.

## 2. Purpose

Allow developers to fix errors or reflect changes in provisional registration data without restarting the underlying registration from scratch.

## 3. Description

The developer opens the provisional registration record from Property Registration Details, submits the amended data with supporting justification, attaches any updated documents, and submits for review. RERA re-reviews and issues an updated Provisional Registration e-Certificate.

## 4. Who Can Apply

* Project Registration Officer *(see Service #1 §4 for the source/UI role-assignment note — applies identically here)*

## 5. Prerequisites

* An existing provisional registration (Service #1, #2, or #3) in a status that permits amendment.
* Amended data and justification available.
* Required supporting documents available, where the amendment affects them.

## 6. Required Information

* Original Provisional Registration Reference Number
* Field(s) Being Amended
* Amended Value(s)
* Reason for Amendment

## 7. Required Documents

> **Proposed** — not itemized in the source beyond the general "amend" description. Needs client confirmation.

* Supporting Evidence for the Amendment (where applicable)
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**6 business days**

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Open Provisional Registration Record
↓
Select "Amend Initial Procedures Data"
↓
Edit Field(s) and Provide Reason
↓
Attach Updated Documents (if applicable)
↓
Select Payment Method
↓
Submit Amendment Application
↓
RERA Reviews Amendment
↓
Updated Provisional Registration e-Certificate Issued

## 13. Application Status Flow

Draft
↓
Payment Pending
↓
Payment Successful
↓
Submitted
↓
Under Review
↓
Approved
↓
Amended

### Additional Statuses

* Information Requested
* Returned
* Rejected
* Cancelled

## 14. Possible Outcomes

* Amendment Successfully Registered
* Additional Information Requested
* Application Returned
* Application Rejected
* Payment Failed

## 15. Output

* Updated Provisional Registration e-Certificate

## 16. Related Services

* Service #1 – Register Initial Sale
* Service #2 – Register Initial Rent-to-Own
* Service #3 – Register Initial Usufruct
* Service #5 – Complete Initial Procedures Data

## 17. UI Screens

* Property Registration Details
* Document Upload
* Payment
* Application Submitted

## 18. API Requirements

* Retrieve Provisional Registration
* Validate Amendment Eligibility
* Upload Documents
* Calculate Service Fee
* Initiate Payment
* Verify Payment
* Submit Amendment Application
* Retrieve Application Status
* Generate Updated Provisional Registration e-Certificate
* Send Notifications

## 19. Database Entities

* Developer Company
* Provisional Registration
* Amendment Record
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can submit an amendment against an existing provisional registration.
* System validates the target registration is in an amendable status.
* A reason for the amendment is required.
* Payment is completed before the amendment proceeds for review.
* Approved amendments generate an updated Provisional Registration e-Certificate.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a provisional registration in an amendable status may be amended under this service.
2. Payment must be completed before the amendment proceeds for regulatory review.
3. A reason for the amendment is required for every submission.
4. All submissions, approvals, payments, and notifications must be permanently recorded in the audit trail.
