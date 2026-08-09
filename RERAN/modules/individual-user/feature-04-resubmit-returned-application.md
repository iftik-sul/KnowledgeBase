---
project: RERAN
module: individual-user
type: service-flow
status: current
updated: 2026-08-09
derived_from:
  - "RERAN/modules/individual-user/RERAN_ individual user_service_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - individual-user
  - shared-feature
  - application-management
---

# Feature #4 – Resubmit Returned Application

**Feature Category:** Shared Platform Features – Application Management

## 1. Feature Overview

The **Resubmit Returned Application** feature enables users to correct and resubmit applications that have been returned by RERAN for revision. Instead of creating a new application, users can update the required information, upload corrected documents, and resubmit the existing application for further review.

## 2. Purpose

Provide a standardized mechanism for applicants to correct returned applications and continue the application process without starting a new application.

## 3. Description

If an application contains incomplete information, incorrect data, invalid documents, or other issues that prevent approval, RERAN may return the application for correction. The user is notified of the reason for the return and can access the application, make the necessary corrections, upload revised documents, and resubmit it for further review.

This feature is shared by all business services that support application review.

## 4. Used By

The feature is shared by all applicable Individual User business services, including:

* Register Property Ownership  
* Transfer Property Ownership  
* Register Property Sale  
* Update Property Ownership Information  
* Register Lease  
* Renew Lease  
* Register Power of Attorney  
* Remote Identity Verification  
* Remote Property Transactions  
* Submit Complaint  
* Submit Tenancy Dispute

## 5. Prerequisites

* User is logged into the platform.  
* An application has previously been submitted.  
* RERAN has returned the application for correction.  
* The application status is **Returned**.

## 6. Required Information

Depending on the reason for return:

* Corrected Application Information  
* Updated Property Information (where applicable)  
* Corrected Applicant Information  
* Response Comments  
* Additional Remarks (Optional)

## 7. Required Documents

Depending on the return reason:

* Corrected Supporting Documents  
* Updated Agreements  
* Government-issued Identification  
* Property Documents  
* Proof of Payment (where requested)  
* Other revised documents requested by RERAN

## 8. Service Fee

No additional fee for resubmission.

The resubmission forms part of the original application unless otherwise specified by RERAN policy.

## 9. Payment Required

**No**

No additional payment is required unless RERAN specifically requires payment for a revised application.

## 10. Processing Authority

**RERAN**

The corrected application is routed back to the department responsible for processing the original application.

## 11. Expected Processing Time

Application resubmission is immediate.

Subsequent review follows the normal processing timeline of the original service.

## 12. Processing Workflow

User Receives Returned Application Notification  
↓  
Open My Applications  
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
RERAN Continues Review

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

* My Applications  
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

* User can view all returned applications.  
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

1. Only authenticated users may resubmit their own returned applications.  
2. Applications may only be resubmitted when the application status is **Returned**.  
3. Users must address all issues identified in the return comments before resubmission.  
4. Revised documents replace or supplement the original documents while preserving document history.  
5. Resubmission does not create a new application; the original application reference number is retained.  
6. After successful resubmission, the application status automatically changes from **Returned** to **Under Review**.  
7. RERAN may return the application again if the identified issues have not been satisfactorily resolved.  
8. Every resubmission receives a timestamp and is permanently linked to the original application.  
9. The complete history of returns, corrections, and resubmissions must be preserved in the application timeline.  
10. All updates, document uploads, resubmissions, notifications, and status changes must be permanently recorded in the audit trail.
