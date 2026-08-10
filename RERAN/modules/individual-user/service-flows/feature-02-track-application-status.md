---
project: RERAN
module: individual-user
type: service-flow
status: current
source_type: sourced
updated: 2026-08-09
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - individual-user
  - shared-feature
  - application-management
---

# Feature #2 – Track Application Status

**Feature Category:** Shared Platform Features – Application Management

## 1. Feature Overview

The **Track Application Status** feature enables users to monitor the progress of all applications submitted through the RERAN platform. It provides real-time visibility into the application's current status, processing history, assigned department, outstanding actions, and final decision.

## 2. Purpose

Provide users with a centralized location to track the progress and current status of all submitted applications throughout their lifecycle.

## 3. Description

The feature allows users to view all submitted applications, search for specific applications, monitor status changes, review processing history, view comments or requests from RERAN, and download approved documents once processing is complete.

This feature is shared by every business service that submits an application to RERAN.

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
* At least one application has been submitted.  
* User is authorized to access the application.

## 6. Required Information

The user may search using one or more of the following:

* Application Reference Number  
* Service Type  
* Property Registration Number (where applicable)  
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

**RERAN**

Application status information is retrieved directly from the official application management system.

## 11. Expected Processing Time

Immediate (real-time retrieval).

## 12. Processing Workflow

Login  
↓  
Open My Applications  
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
Completed

Possible additional statuses

* Payment Pending  
* Validation Failed  
* Returned  
* Cancelled  
* Withdrawn

## 14. Possible Outcomes

* Application Found  
* Application Not Found  
* Application Under Review  
* Information Requested  
* Application Approved  
* Application Rejected  
* Application Completed

## 15. Output

The system displays:

* Application Reference Number  
* Service Name  
* Submission Date  
* Current Status  
* Processing Timeline  
* Assigned Department (where applicable)  
* Status History  
* Comments from RERAN (where applicable)  
* Available Certificates or Documents  
* Payment Information

## 16. Related Features

* Submit Application  
* Respond to Information Request  
* Resubmit Returned Application  
* Documents  
* Notifications

## 17. UI Screens

* My Applications  
* Application List  
* Application Search  
* Application Details  
* Application Timeline  
* Status History  
* Download Documents

## 18. API Requirements

* Retrieve User Applications  
* Search Applications  
* Retrieve Application Details  
* Retrieve Application Timeline  
* Retrieve Status History  
* Retrieve Comments  
* Retrieve Available Documents  
* Download Documents

## 19. Database Entities

* User  
* Application  
* Application Status  
* Application Timeline  
* Service Request  
* Document  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* User can view all submitted applications.  
* User can search applications using supported search criteria.  
* Current application status is displayed correctly.  
* Complete status history is available.  
* Processing timeline is displayed in chronological order.  
* Users can view requests for additional information.  
* Approved documents are available for download when applicable.  
* Users can only access their own authorized applications.  
* All application access activities are recorded in the audit log.

## 21. Business Rules

1. Only authenticated users may access application status information.  
2. Users may only view applications they own or are authorized to access.  
3. Application status is updated automatically as processing progresses.  
4. Status history cannot be modified by users.  
5. Approved certificates and documents become available for download only after the application reaches the appropriate status.  
6. If RERAN requests additional information, the application status changes to **Information Requested**, and the user must use the **Respond to Information Request** feature.  
7. If an application is returned for correction, the user must use the **Resubmit Returned Application** feature.  
8. Every status change is recorded with a timestamp in the application timeline.  
9. All application viewing activities must be permanently recorded in the audit trail.  
10. The feature provides a unified tracking experience regardless of the underlying RERAN service.
