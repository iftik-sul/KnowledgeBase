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
tags:
  - real-estate-developer
  - service-flow
  - real-estate-licensing-service
---

# Service #22 – Real Estate Licensing Application

**Service Category:** Real Estate Licensing Service

## 1. Service Overview

The **Real Estate Licensing Application** service allows a developer entity to apply for the real estate license required before it can register any project with RERA. This is the precondition Service #13 (Registration of Real Estate Project) assumes is already in place.

> **UI gap — flagged, not resolved.** No screen in the 19-screen UI set represents this service. `company-profile.md` maintains an already-licensed company's profile; it does not expose a licensing application. Nothing else in the UI addresses entity licensing. The UI Screens list below is a **proposed** minimum surface, not a documented existing one.

## 2. Purpose

Establish a developer entity's regulatory standing to operate on the platform, before any project-level activity is possible.

## 3. Description

The developer entity submits a licensing application with the required company information. The Licensing & Registration Officer reviews and approves or rejects the application.

## 4. Who Can Apply

* Project Registration Officer

## 5. Prerequisites

* Registered developer company account (pre-licensing status).
* Required company information and supporting documents available.

## 6. Required Information

* Company Name and Registration Number
* Company Address
* Principal Contact Information

## 7. Required Documents

> **Proposed** — not itemized in the source beyond the service's existence. Needs client confirmation.

* Certificate of Incorporation
* Company Ownership/Directorship Details
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

Not specified in the source. **Proposed**: yes, consistent with other licensing-type services; needs client confirmation.

## 10. Processing Authority

**Licensing & Registration Officer**

## 11. Expected Processing Time

**5 minutes**

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Select "Real Estate Licensing Application"
↓
Enter Company Information
↓
Attach Supporting Documents
↓
Submit Application Online
↓
Licensing & Registration Officer Reviews Application
↓
License Issued, Developer Self Registration Username Designated

## 13. Application Status Flow

Draft
↓
Submitted
↓
Under Review
↓
Approved
↓
Licensed

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* License Successfully Issued
* Additional Information Requested
* Application Rejected

## 15. Output

Not specified in the source ("no doc" against this row). **Proposed**: a Real Estate License record and a Developer Self Registration username, consistent with Service #13's dependency on both; needs client confirmation.

## 16. Related Services

* Service #13 – Registration of Real Estate Project *(this license is a stated prerequisite for that service)*
* Service #23 – Accreditation of Training Entities

## 17. UI Screens

Not currently represented in the 19-screen UI set. **Proposed** minimum surface: a "Licensing Application" flow, distinct from `company-profile.md`'s ongoing profile management.

## 18. API Requirements

* Submit Licensing Application
* Upload Documents
* Retrieve Application Status
* Issue Real Estate License
* Designate Developer Self Registration Username
* Send Notifications

## 19. Database Entities

* Developer Company
* Real Estate License
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* A developer entity can apply for a real estate license.
* System validates required company information and documents.
* Approved applications issue a license and a Developer Self Registration username.
* All activities are recorded in the audit log.

## 21. Business Rules

1. A developer entity must hold a valid real estate license before registering a project under Service #13.
2. All submissions, reviews, and notifications must be permanently recorded in the audit trail.
3. **No UI screen currently exists for this service** — flagged for the client rather than force-fit to an existing screen.
