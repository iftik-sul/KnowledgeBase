---
project: RERAN
module: individual-user
type: feature
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

# Feature #3 – Respond to Information Request

**Feature Category:** Shared Platform Features – Application Management

## 1. Feature Overview

The **Respond to Information Request** feature enables users to provide additional information, upload missing documents, correct application details, or respond to requests issued by RERAN during the review of an application. This feature allows an application to continue through the approval process without requiring a new application.

## 2. Purpose

Provide a standardized mechanism for applicants to respond to requests for additional information during application processing.

## 3. Description

During the review of an application, RERAN may request additional information, supporting documents, clarifications, or corrections. The user receives a notification and can access the information request directly from the application. After completing the requested updates, the response is submitted for further review, allowing the application to continue through its normal processing workflow.

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
* An application has been submitted.  
* RERAN has issued an Information Request.  
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
* Updated Agreements  
* Government-issued Identification  
* Property Documents  
* Proof of Payment  
* Other documents requested by RERAN

## 8. Service Fee

No additional fee.

The response forms part of the original application.

## 9. Payment Required

**No**

No additional payment is required when responding to an information request.

## 10. Processing Authority

**RERAN**

The submitted response is routed back to the department currently processing the application.

## 11. Expected Processing Time

Response submission is immediate.

Subsequent review depends on the processing timeline of the original application.

## 12. Processing Workflow

User Receives Information Request  
↓  
Notification Received  
↓  
Open My Applications  
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
Application Returned to Processing Queue  
↓  
RERAN Continues Review

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
* Documents  
* Notifications

## 17. UI Screens

* My Applications  
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

* User  
* Application  
* Information Request  
* Response  
* Document  
* Application Timeline  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* User can view all outstanding information requests.  
* User can review the details of each request.  
* User can update the requested information.  
* User can upload additional supporting documents.  
* The system validates the response before submission.  
* The response is linked to the original application.  
* The application automatically returns to the review process after submission.  
* The application timeline records the response.  
* Notifications are sent confirming successful submission.  
* All response activities are recorded in the audit log.

## 21. Business Rules

1. Only authenticated users may respond to information requests for their own applications.  
2. Responses can only be submitted when the application status is **Information Requested**.  
3. The response must address the specific items requested by RERAN.  
4. Supporting documents may be uploaded only for the requested application.  
5. Submission of a response does not create a new application.  
6. After submission, the application status automatically changes from **Information Requested** to **Under Review**.  
7. RERAN may issue additional information requests if the submitted response is insufficient.  
8. Every response receives a submission timestamp and is permanently linked to the original application.  
9. The complete history of all information requests and responses must be preserved in the application timeline.  
10. All user actions, document uploads, submissions, and status changes must be permanently recorded in the audit trail.
