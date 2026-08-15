---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: extrapolated
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/navigation.md"
  - "RERAN/modules/individual-user/service-flows/feature-03-respond-to-information-request.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - application-management
---

# Feature #3 – Respond to Information Request

**Feature Category:** Shared Platform Features – Application Management

> **Proposed** — named in [services-overview.md](../services-overview.md#shared-platform-features), not previously written as a standalone document. Needs client confirmation.

## 1. Feature Overview

The **Respond to Information Request** feature enables institution-account users to provide additional information, upload missing documents, correct application details, or respond to requests issued by RERA's Compliance & Escrow Auditor during the review of an application. This feature allows an application to continue through the approval process without requiring a new application.

**Scope note:** this feature covers only RERA-side information requests (application status `Information Requested`). It is distinct from the institution-internal certify-or-return loop (`Returned by Certifier`, Services #3–#11 only), which is handled by the separate Internal Certification Queue (Feature #5).

## 2. Purpose

Provide a standardized mechanism for institution-account users to respond to RERA's requests for additional information during application processing, across any of the 18 Group C services.

## 3. Description

During RERA's review of an application, the Compliance & Escrow Auditor may request additional information, supporting documents, clarifications, or corrections — the `Information Requested` status appears in this module's platform-wide core status vocabulary. The user receives a notification and can access the information request directly from the application. After completing the requested updates, the response is submitted for further review, allowing the application to continue through its normal RERA-side processing workflow. Any of the institution's four Group C roles may respond, not only the original filer.

This feature is shared by all business services that support RERA-side application review.

## 4. Used By

The feature is shared by all 18 Group C business services, including:

* Mortgage Registration
* Mortgage Amendment
* Mortgage Transfer
* Mortgage Release
* Grant Property Mortgage
* Finance Lease Registration
* Registration of Real Estate Fund Companies
* Updating Title Deed Information
* Split Ownership
* Issuance of Title Deed

## 5. Prerequisites

* User is logged into a verified institution account.
* An application has been submitted and has passed any applicable internal certification gate.
* RERA has issued an Information Request.
* The application status is **Information Requested**.

## 6. Required Information

Depending on the request:

* Response Comments
* Updated Application Information
* Corrected Information
* Additional Remarks (Optional)

## 7. Required Documents

Depending on the request:

* Missing Supporting Documents
* Corrected Documents
* Updated Mortgage / Lease / Title Documents
* Other documents requested by RERA

## 8. Service Fee

No additional fee.

The response forms part of the original application.

## 9. Payment Required

**No**

No additional payment is required when responding to an information request.

## 10. Processing Authority

**RERA — Compliance & Escrow Auditor**

The submitted response is routed back to the RERA queue currently processing the application. It does not re-enter the institution's internal certification gate.

## 11. Expected Processing Time

Response submission is immediate.

Subsequent review depends on the processing timeline of the original application.

## 12. Processing Workflow

User Receives Information Request
↓
Notification Received
↓
Open Applications
↓
Open Requested Application
↓
Review Information Request
↓
Update Requested Information
↓
Upload Additional Documents
↓
Review Response
↓
Submit Response
↓
System Validates Response
↓
Application Returned to RERA Processing Queue
↓
Compliance & Escrow Auditor Continues Review

## 13. Application Status Flow

Information Requested
↓
User Preparing Response
↓
Response Submitted
↓
Under Review
↓
Approved / Rejected / Information Requested Again

Possible additional statuses

* Validation Failed
* Response Incomplete
* Cancelled

## 14. Possible Outcomes

* Response Successfully Submitted
* Application Returned to Review
* Additional Information Requested Again
* Validation Failed
* Response Incomplete

## 15. Output

Upon successful submission, the system generates:

* Response Confirmation
* Response Submission Timestamp
* Updated Application Timeline
* Notification Confirmation

## 16. Related Features

* Submit Application
* Track Application Status
* Resubmit Returned Application
* Internal Certification Queue *(Feature #5 — a separate, institution-internal loop, not this feature)*
* Documents
* Notifications

## 17. UI Screens

* Applications
* Application Details
* Information Request Details
* Update Information
* Document Upload
* Review Response
* Response Submitted

## 18. API Requirements

* Retrieve Information Request
* Retrieve Application Details
* Upload Documents
* Update Application Information
* Validate Response
* Submit Response
* Update Application Status
* Send Notifications
* Retrieve Updated Timeline

## 19. Database Entities

* Institution
* Institution Staff
* User
* Application
* Information Request
* Response
* Document
* Application Timeline
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can view all outstanding RERA information requests for the institution.
* User can review the details of each request.
* User can update the requested information.
* User can upload additional supporting documents.
* The system validates the response before submission.
* The response is linked to the original application.
* The application automatically returns to RERA's review process after submission, not to internal certification.
* The application timeline records the response.
* Notifications are sent confirming successful submission.
* All response activities are recorded in the audit log.

## 21. Business Rules

1. Only authenticated users of the institution account may respond to RERA information requests on its applications; any of the four Group C roles may do so, not only the original filer.
2. Responses can only be submitted when the application status is **Information Requested**.
3. The response must address the specific items requested by RERA.
4. Supporting documents may be uploaded only for the requested application.
5. Submission of a response does not create a new application.
6. After submission, the application status automatically changes from **Information Requested** to **Under Review**.
7. RERA may issue additional information requests if the submitted response is insufficient.
8. A response never re-enters the internal certification gate (Services #3–#11); it is routed directly back to RERA.
9. Every response receives a submission timestamp and is permanently linked to the original application.
10. All user actions, document uploads, submissions, and status changes must be permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. Same adoption question as Feature #1 — needs client confirmation.
