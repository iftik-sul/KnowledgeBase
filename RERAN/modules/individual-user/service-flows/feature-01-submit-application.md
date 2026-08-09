---
project: RERAN
module: individual-user
type: service-flow
status: current
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

# Feature #1 – Submit Application

**Feature Category:** Shared Platform Features – Application Management

## 1. Feature Overview

The **Submit Application** feature provides a standardized mechanism for Individual Users to submit requests for any RERAN service. It serves as the final submission stage of every service workflow, validating the application, confirming payment, generating a unique application reference number, and routing the application to the appropriate RERAN department for processing.

## 2. Purpose

Provide a common application submission process that is shared across all RERAN business services, ensuring consistency, traceability, and regulatory compliance.

## 3. Description

After completing the required service-specific information, uploading supporting documents, and paying the applicable service fee, the user submits the application. The platform validates the application, assigns a unique reference number, records the submission, and forwards it to the responsible RERAN department.

This feature is reused by every business service that requires an official application.

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
* User has selected a RERAN service.  
* All mandatory information has been completed.  
* Required documents have been uploaded.  
* Payment has been successfully completed (where applicable).

## 6. Required Information

The feature receives information from the selected business service.

Typical information includes:

* Service Type  
* Applicant Information  
* Property Information (where applicable)  
* Service-specific Data  
* Uploaded Documents  
* Payment Confirmation  
* Additional Remarks (Optional)

## 7. Required Documents

Documents depend on the selected service.

Examples include:

* Identification Documents  
* Property Documents  
* Lease Agreements  
* Sale Agreements  
* Power of Attorney  
* Supporting Evidence  
* Other service-specific documents

## 8. Service Fee

No separate fee.

The feature uses the fee defined by the selected business service.

## 9. Payment Required

**Yes (where applicable)**

If the selected service requires payment, successful payment must be confirmed before submission.

## 10. Processing Authority

**RERAN**

The submitted application is automatically routed to the department responsible for the selected service.

## 11. Expected Processing Time

Application submission is immediate.

Subsequent processing depends on the selected business service.

## 12. Processing Workflow

User Completes Service Form  
↓  
Upload Required Documents  
↓  
Review Application  
↓  
Complete Payment (if applicable)  
↓  
Submit Application  
↓  
System Validates Application  
↓  
Generate Application Reference Number  
↓  
Record Audit Log  
↓  
Route Application to Appropriate RERAN Department  
↓  
Application Successfully Submitted

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted

Possible exception statuses

* Validation Failed  
* Payment Failed  
* Submission Failed  
* Cancelled

## 14. Possible Outcomes

* Application Successfully Submitted  
* Validation Failed  
* Missing Information  
* Missing Documents  
* Payment Failed  
* Submission Failed

## 15. Output

Upon successful submission, the system generates:

* Application Reference Number  
* Submission Confirmation  
* Submission Timestamp  
* Digital Acknowledgement Receipt  
* Payment Receipt (where applicable)

## 16. Related Features

* Track Application Status  
* Respond to Information Request  
* Resubmit Returned Application  
* Payments  
* Documents  
* Notifications

## 17. UI Screens

* Application Review  
* Payment  
* Payment Successful  
* Submit Application Confirmation  
* Application Submitted  
* Application Details

## 18. API Requirements

* Validate Application  
* Validate Required Documents  
* Validate Payment  
* Generate Application Reference Number  
* Submit Application  
* Assign Processing Department  
* Send Notifications  
* Create Audit Log  
* Retrieve Application Details

## 19. Database Entities

* User  
* Service Request  
* Application  
* Application Status  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* User can submit a completed application.  
* All mandatory information is validated before submission.  
* Required documents are successfully uploaded.  
* Payment is verified before submission when required.  
* The system generates a unique application reference number.  
* The application is routed to the correct RERAN department.  
* The user receives a submission confirmation.  
* A digital acknowledgement receipt is generated.  
* The application becomes available in **My Applications**.  
* Notifications are sent to the user.  
* All submission activities are recorded in the audit log.

## 21. Business Rules

1. Only authenticated users may submit applications.  
2. All mandatory information must be completed before submission.  
3. All required supporting documents must be uploaded before submission.  
4. Payment must be successfully completed for services that require payment.  
5. Every submitted application receives a unique application reference number.  
6. Applications cannot be modified after submission unless additional information is requested or the application is returned.  
7. Every application is automatically routed to the appropriate RERAN department based on the selected service.  
8. Submission generates an acknowledgement receipt and user notification.  
9. Every submission event must be permanently recorded in the audit trail.  
10. The submitted application becomes available immediately under **My Applications** for status tracking.
