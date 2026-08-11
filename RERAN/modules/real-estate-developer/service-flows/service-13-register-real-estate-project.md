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
  - "RERAN/modules/real-estate-developer/ui/screens/projects.md"
  - "RERAN/modules/real-estate-developer/ui/screens/project-details.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-development-services
---

# Service #13 – Registration of Real Estate Project

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Registration of Real Estate Project** service is the foundational service through which a developer registers a new real estate project with RERA, before any unit within it can be sold, leased, or otherwise transacted. Most other Group B services (property registrations, escrow activation) depend on a project already being registered under this service.

## 2. Purpose

Establish a regulated project record — the project's units, survey data, and registrar account — before any property-level transaction under it can proceed.

## 3. Description

RERA first issues the developer a real estate license and designates a username in the Developer Self Registration system. The developer applies through that system, attaching the project's requirements. RERA audits and reviews, accepting or rejecting. If accepted, the developer uploads the project's units through an approved survey company, then submits an application to the Registrar to open a project account. After the registration fee is paid, the project approval certificate is issued via the online system.

## 4. Who Can Apply

* Project Registration Officer

## 5. Prerequisites

* Registered developer company account with a valid real estate license.
* Designated Developer Self Registration username.
* Project requirements and unit survey data available from an approved survey company.

## 6. Required Information

### Project Information

* Project Name
* Project Location
* Project Type
* Number of Units

### Survey Information

* Approved Survey Company
* Survey Reference

## 7. Required Documents

> **Proposed** — not itemized field-by-field beyond "attach requirements." Following the general project-registration document pattern. Needs client confirmation.

* Real Estate License
* Land Title Documents
* Survey Report from Approved Survey Company
* Project Master Plan
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule; paid before certificate issuance.

## 9. Payment Required

**Yes**

## 10. Processing Authority

**Compliance & Escrow Auditor** (audit/review step); **Registrar** (account-opening step).

## 11. Expected Processing Time

**Project registration: 3 business days.**

## 12. Processing Workflow

RERA Issues Real Estate License, Designates Developer Self Registration Username
↓
Developer Applies via Developer Self Registration System, Attaches Requirements
↓
RERA Audits and Reviews: Accept or Reject
↓
If Accepted: Developer Uploads Units through Approved Survey Company
↓
Developer Submits Application to Registrar to Open Account
↓
Pay Registration Fee
↓
Real Estate Project Approval Certificate Issued via Online System

## 13. Application Status Flow

Licensed
↓
Draft
↓
Submitted
↓
Under Review
↓
Accepted
↓
Units Uploaded
↓
Registrar Account Requested
↓
Payment Pending
↓
Payment Successful
↓
Registered

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Project Successfully Registered
* Additional Information Requested
* Application Rejected
* Payment Failed

## 15. Output

* Real Estate Project Approval Certificate (e-certificate)

## 16. Related Services

* Service #14 – Real Estate Project Cancellation
* Service #16 – Changing the Name of a Real Estate Project
* Service #17 – Project Re-registration
* Service #24 – Register/Amend Real Estate Project Details
* Service #22 – Real Estate Licensing Application *(cross-reference: the license issued as the precondition for this service)*

## 17. UI Screens

* Projects
* Project Details
* Document Upload
* Payment
* Application Submitted

## 18. API Requirements

* Validate Real Estate License
* Submit Project Registration Application
* Retrieve Application Status
* Validate Survey Company Approval
* Upload Project Units
* Submit Registrar Account Request
* Calculate Registration Fee
* Initiate Payment
* Verify Payment
* Generate Real Estate Project Approval Certificate
* Send Notifications

## 19. Database Entities

* Developer Company
* Real Estate License
* Project
* Property Unit
* Survey Company
* Survey Report
* Registrar Account
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can apply to register a new real estate project once licensed.
* System validates the developer's license and Developer Self Registration credentials.
* Units can only be uploaded through an approved survey company.
* A Registrar account is opened before the registration fee is collected.
* Payment is completed before the certificate is issued.
* Approved registrations generate a Real Estate Project Approval Certificate.
* All activities are recorded in the audit log.

## 21. Business Rules

1. A developer must hold a valid real estate license (Service #22) before registering a project.
2. Project units must be uploaded through an approved survey company; self-reported unit data is not accepted.
3. Registration fee must be paid before the approval certificate is issued.
4. Every project receives a unique project reference number, referenced by all downstream property-level services.
5. All submissions, reviews, uploads, payments, and notifications must be permanently recorded in the audit trail.
