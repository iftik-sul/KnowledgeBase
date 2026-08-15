---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: extrapolated
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/shared-platform-features.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/individual-user/service-flows/feature-02-track-application-status.md"
tags:
  - real-estate-developer
  - shared-feature
  - application-management
---

# Feature #2 – Track Application Status

**Feature Category:** Shared Platform Features – Application Management

> **Proposed** — not sourced as a standalone feature; see [shared-platform-features.md](../shared-platform-features.md). Needs client confirmation.

## 1. Feature Overview

The **Track Application Status** feature enables developer-account users to monitor the progress of every application submitted through the Real Estate Developers Portal, via the **Applications** sidebar item. It provides visibility into the application's current status, processing history, assigned authority, outstanding actions, and final decision.

## 2. Purpose

Provide a centralized location to track the progress and current status of all submitted applications throughout their lifecycle, for any of the four Group B roles.

## 3. Description

The feature allows users to view all submitted applications, search for specific applications, monitor status changes, review processing history, view comments or requests from RERA, and download approved documents once processing is complete. Because Group B is not gated by role ([navigation.md](../navigation.md)), any of the four roles can view and act on any application filed under the developer account, including ones they did not personally submit.

This feature is shared by every business service that submits an application to RERA.

## 4. Used By

The feature is shared by all applicable Group B business services, including:

* Register Initial Sale
* Register Initial Rent-to-Own
* Registration of Real Estate Project
* Amend Initial Procedures Data
* Escrow Account Activation
* Escrow Account Transfer
* Real Estate Licensing Application
* Real Estate Project Sub-division
* Requesting a Technical Report for the Project

## 5. Prerequisites

* User is logged into a registered developer company account.
* At least one application has been submitted under the developer account.

## 6. Required Information

The user may search using one or more of the following:

* Application Reference Number
* Service Type
* Project Reference Number (where applicable)
* Unit / Property Identifier (where applicable)
* Application Date
* Current Status

## 7. Required Documents

No document upload is required.

Approved documents and certificates become available for download when applicable.

## 8. Service Fee

No additional fee.

Application tracking is included as part of the submitted service.

## 9. Payment Required

**No**

Payment is not required to track an application that has already been submitted.

## 10. Processing Authority

**RERA**

Application status information is retrieved directly from the official application management system.

## 11. Expected Processing Time

Immediate (real-time retrieval).

## 12. Processing Workflow

Login
↓
Open Applications
↓
Search or Select Application
↓
Retrieve Application Details
↓
View Current Status
↓
View Timeline
↓
View Processing History
↓
Download Documents (when available)

## 13. Application Status Flow

Submitted
↓
Under Review
↓
Information Requested (if applicable)
↓
Resubmitted (if applicable)
↓
Approved / Rejected
↓
Registered / Completed

Possible additional statuses

* Payment Pending (where the service requires payment)
* Validation Failed
* Returned
* Cancelled

**Not every service uses this exact vocabulary.** Service #13 (Register Real Estate Project) sources a longer, service-specific status chain (Licensed → Draft → Submitted → Under Review → Accepted → Units Uploaded → Registrar Account Requested → Payment Pending → Payment Successful → Registered). This feature displays whatever status vocabulary the underlying service defines; it does not impose its own.

## 14. Possible Outcomes

* Application Found
* Application Not Found
* Application Under Review
* Information Requested
* Application Approved
* Application Rejected
* Application Registered / Completed

## 15. Output

The system displays:

* Application Reference Number
* Service Name
* Submission Date
* Current Status
* Processing Timeline
* Assigned Authority (where applicable)
* Status History
* Comments from RERA (where applicable)
* Available Certificates or Documents
* Payment Information (where the service requires payment)

## 16. Related Features

* Submit Application
* Respond to Information Request
* Resubmit Returned Application
* Documents
* Notifications

## 17. UI Screens

* Applications
* Application Details
* Application Timeline (where present)
* Status History
* Download Documents

## 18. API Requirements

* Retrieve Developer Applications
* Search Applications
* Retrieve Application Details
* Retrieve Application Timeline
* Retrieve Status History
* Retrieve Comments
* Retrieve Available Documents
* Download Documents

## 19. Database Entities

* Developer Company
* User
* Application
* Application Status
* Application Timeline
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the four Group B roles can view all applications submitted under the developer account.
* Users can search applications using supported search criteria.
* Current application status is displayed correctly, using the vocabulary defined by the underlying service.
* Complete status history is available.
* Processing timeline is displayed in chronological order.
* Users can view requests for additional information.
* Approved documents are available for download when applicable.
* All application access activities are recorded in the audit log.

## 21. Business Rules

1. Only authenticated users of the developer company account may access its application status information.
2. Any of the four Group B roles may view or act on any application under the account — there is no per-role restriction (per [navigation.md](../navigation.md)).
3. Application status is updated automatically as processing progresses.
4. Status history cannot be modified by users.
5. Approved certificates and documents become available for download only after the application reaches the appropriate status.
6. If RERA requests additional information, the application status changes to **Information Requested**, and the user must use the **Respond to Information Request** feature.
7. If an application is returned for correction, the user must use the **Resubmit Returned Application** feature.
8. Every status change is recorded with a timestamp in the application timeline, including the acting user's role.
9. All application viewing activities must be permanently recorded in the audit trail.
10. The feature displays whatever status vocabulary the underlying service defines — it does not standardize a single vocabulary across all 27 services.

## Open Questions

1. Same adoption question as Feature #1 — needs client confirmation.
2. Whether a single unified status vocabulary should eventually be adopted for Group B (as financial-trust-institutions has proposed for Group C, per its `open-questions.md` D1) is out of scope for this document and left for a separate discussion.
