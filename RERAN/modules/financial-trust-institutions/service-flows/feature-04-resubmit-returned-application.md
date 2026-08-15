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
  - "RERAN/modules/individual-user/service-flows/feature-04-resubmit-returned-application.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - application-management
---

# Feature #4 – Resubmit Returned Application

**Feature Category:** Shared Platform Features – Application Management

> **Proposed** — named in [services-overview.md](../services-overview.md#shared-platform-features), not previously written as a standalone document. Needs client confirmation.

## 1. Feature Overview

The **Resubmit Returned Application** feature enables institution-account users to correct and resubmit applications that RERA's Compliance & Escrow Auditor has returned for revision. Instead of creating a new application, users can update the required information, upload corrected documents, and resubmit the existing application for further RERA-side review.

**Scope note:** this feature covers only RERA-side returns (application status `Returned for Correction`). It is distinct from the institution-internal certify-or-return loop (`Returned by Certifier`, Services #3–#11 only), which loops back to **Draft** and is handled by the Internal Certification Queue (Feature #5), not by this feature.

## 2. Purpose

Provide a standardized mechanism for institution-account users to correct RERA-returned applications and continue the process without starting a new application, across any of the 18 Group C services.

## 3. Description

If an application contains incomplete information, incorrect data, invalid documents, or other issues that prevent approval, RERA's Compliance & Escrow Auditor may return the application for correction — the `Returned for Correction` status appears in this module's core status vocabulary. The user is notified of the reason for the return and can access the application, make the necessary corrections, upload revised documents, and resubmit it for further RERA review. Any of the institution's four Group C roles may resubmit, not only the original filer.

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
* An application has previously been submitted and passed any applicable internal certification gate.
* RERA has returned the application for correction.
* The application status is **Returned for Correction**.

## 6. Required Information

Depending on the reason for return:

* Corrected Application Information
* Updated Borrower / Counterparty Information (where applicable)
* Response Comments
* Additional Remarks (Optional)

## 7. Required Documents

Depending on the return reason:

* Corrected Supporting Documents
* Updated Mortgage / Lease / Title Documents
* Other revised documents requested by RERA

## 8. Service Fee

No additional fee for resubmission.

The resubmission forms part of the original application unless otherwise specified by RERA policy.

## 9. Payment Required

**No**

No additional payment is required unless RERA specifically requires payment for a revised application. Where the original application's payment model places payment after RERA's decision (Services #12, #18), that timing is unaffected by resubmission.

## 10. Processing Authority

**RERA — Compliance & Escrow Auditor**

The corrected application is routed back to RERA's review queue — not to the institution's internal certification gate.

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
Application Returned to RERA Processing Queue
↓
Compliance & Escrow Auditor Continues Review

## 13. Application Status Flow

Returned for Correction
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
* Internal Certification Queue *(Feature #5 — a separate, institution-internal loop, not this feature)*
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

* Institution
* Institution Staff
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

* Any of the institution's four Group C roles can view all RERA-returned applications for the institution.
* User can review the reason the application was returned.
* User can update the required information.
* User can replace or upload revised supporting documents.
* The system validates the corrected application before resubmission.
* The original application reference number is retained.
* The application automatically returns to RERA's review process after resubmission, not to internal certification.
* The application timeline records the resubmission.
* The user receives a confirmation notification after successful resubmission.
* All resubmission activities are recorded in the audit log.

## 21. Business Rules

1. Only authenticated users of the institution account may resubmit its RERA-returned applications; any of the four Group C roles may do so, not only the original filer.
2. Applications may only be resubmitted through this feature when the application status is **Returned for Correction** — not **Returned by Certifier**, which uses the separate Internal Certification Queue.
3. Users must address all issues identified in the return comments before resubmission.
4. Revised documents replace or supplement the original documents while preserving document history.
5. Resubmission does not create a new application; the original application reference number is retained.
6. After successful resubmission, the application status automatically changes from **Returned for Correction** to **Under Review**.
7. RERA may return the application again if the identified issues have not been satisfactorily resolved.
8. Every resubmission receives a timestamp and is permanently linked to the original application.
9. The complete history of returns, corrections, and resubmissions must be preserved in the application timeline.
10. All updates, document uploads, resubmissions, notifications, and status changes must be permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. Same adoption question as Feature #1 — needs client confirmation.
