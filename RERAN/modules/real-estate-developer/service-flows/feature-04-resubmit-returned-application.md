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
  - "RERAN/modules/individual-user/service-flows/feature-04-resubmit-returned-application.md"
tags:
  - real-estate-developer
  - shared-feature
  - application-management
---

# Feature #4 – Resubmit Returned Application

**Feature Category:** Shared Platform Features – Application Management

> **Proposed** — not sourced as a standalone feature; see [shared-platform-features.md](../shared-platform-features.md). Needs client confirmation.

## 1. Feature Overview

The **Resubmit Returned Application** feature enables developer-account users to correct and resubmit applications that have been returned by RERA for revision. Instead of creating a new application, users can update the required information, upload corrected documents, and resubmit the existing application for further review.

## 2. Purpose

Provide a standardized mechanism for developer-account users to correct returned applications and continue the process without starting a new application, across any of the 27 Group B services.

## 3. Description

If an application contains incomplete information, incorrect data, invalid documents, or other issues that prevent approval, RERA may return the application for correction — the `Returned` additional status appears across the module's service-flow files. The user is notified of the reason for the return and can access the application, make the necessary corrections, upload revised documents, and resubmit it for further review. Any of the four Group B roles may resubmit, not only the original filer.

This feature is shared by all business services that support application review.

## 4. Used By

The feature is shared by all applicable Group B business services, including:

* Register Initial Sale
* Register Initial Rent-to-Own
* Registration of Real Estate Project
* Amend Initial Procedures Data
* Escrow Account Activation
* Real Estate Licensing Application
* Real Estate Project Sub-division
* Requesting a Technical Report for the Project

## 5. Prerequisites

* User is logged into a registered developer company account.
* An application has previously been submitted.
* RERA has returned the application for correction.
* The application status is **Returned**.

## 6. Required Information

Depending on the reason for return:

* Corrected Application Information
* Updated Project / Unit Information (where applicable)
* Response Comments
* Additional Remarks (Optional)

## 7. Required Documents

Depending on the return reason:

* Corrected Supporting Documents
* Updated Agreements
* Revised Survey Reports
* Other revised documents requested by RERA

## 8. Service Fee

No additional fee for resubmission.

The resubmission forms part of the original application unless otherwise specified by RERA policy.

## 9. Payment Required

**No**

No additional payment is required unless RERA specifically requires payment for a revised application.

## 10. Processing Authority

**RERA**

The corrected application is routed back to the authority responsible for processing the original application.

## 11. Expected Processing Time

Application resubmission is immediate.

Subsequent review follows the normal processing timeline of the original service.

## 12. Processing Workflow

User Receives Returned Application Notification
↓
Open Applications
↓
Open Returned Application
↓
Review Return Comments
↓
Correct Application Information
↓
Upload Revised Documents
↓
Review Updated Application
↓
Resubmit Application
↓
System Validates Updates
↓
Application Returned to Processing Queue
↓
RERA Continues Review

## 13. Application Status Flow

Returned
↓
User Updating Application
↓
Resubmitted
↓
Under Review
↓
Approved / Rejected / Returned Again

Possible additional statuses

* Validation Failed
* Resubmission Failed
* Cancelled

## 14. Possible Outcomes

* Application Successfully Resubmitted
* Returned to Review
* Returned Again
* Validation Failed
* Application Rejected

## 15. Output

Upon successful resubmission, the system generates:

* Resubmission Confirmation
* Updated Application Timeline
* Resubmission Timestamp
* User Notification

## 16. Related Features

* Submit Application
* Track Application Status
* Respond to Information Request
* Documents
* Notifications

## 17. UI Screens

* Applications
* Returned Applications
* Application Details
* Return Comments
* Update Application
* Document Upload
* Review Changes
* Resubmission Successful

## 18. API Requirements

* Retrieve Returned Applications
* Retrieve Return Comments
* Retrieve Application Details
* Update Application Information
* Upload Revised Documents
* Validate Updated Application
* Resubmit Application
* Update Application Status
* Send Notifications
* Retrieve Updated Timeline

## 19. Database Entities

* Developer Company
* User
* Application
* Application Status
* Return Reason
* Application Revision
* Document
* Application Timeline
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the four Group B roles can view all returned applications for the developer account.
* User can review the reason the application was returned.
* User can update the required information.
* User can replace or upload revised supporting documents.
* The system validates the corrected application before resubmission.
* The original application reference number is retained.
* The application automatically returns to the review process after resubmission.
* The application timeline records the resubmission.
* The user receives a confirmation notification after successful resubmission.
* All resubmission activities are recorded in the audit log.

## 21. Business Rules

1. Only authenticated users of the developer company account may resubmit its returned applications; any of the four Group B roles may do so, not only the original filer.
2. Applications may only be resubmitted when the application status is **Returned**.
3. Users must address all issues identified in the return comments before resubmission.
4. Revised documents replace or supplement the original documents while preserving document history.
5. Resubmission does not create a new application; the original application reference number is retained.
6. After successful resubmission, the application status automatically changes from **Returned** to **Under Review**.
7. RERA may return the application again if the identified issues have not been satisfactorily resolved.
8. Every resubmission receives a timestamp and is permanently linked to the original application.
9. The complete history of returns, corrections, and resubmissions must be preserved in the application timeline.
10. All updates, document uploads, resubmissions, notifications, and status changes must be permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. Same adoption question as Feature #1 — needs client confirmation.
