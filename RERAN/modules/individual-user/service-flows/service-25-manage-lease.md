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
  - service-flow
  - tenancy
---

# Service #25 – Manage Lease

**Service Category:** Tenancy Services

## 1. Service Overview

The **Manage Lease** service enables landlords and tenants to manage an active registered lease throughout its lifecycle. The service provides a centralized workspace for viewing lease details, monitoring lease status, requesting amendments, recording lease events, managing supporting documents, and tracking all lease-related activities until the lease expires or is terminated.

## 2. Purpose

Enable property owners and tenants to efficiently manage an active registered lease while maintaining accurate tenancy records within the RERAN platform.

## 3. Description

The service provides a complete lease management workspace where authorized users can access lease information, monitor lease status, update permissible lease information, upload supporting documents, manage lease-related requests, and review the complete history of the tenancy. All approved updates become part of the official lease record.

## 4. Who Can Apply

* Registered Property Owner  
* Landlord  
* Registered Tenant  
* Authorized Property Representative  
* Property Management Company (where authorized)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is registered with RERAN.  
* Lease is already registered.  
* Applicant is authorized to access the lease.

## 6. Required Information

### Lease Information

* Lease Registration Number  
* Property Information  
* Landlord Information  
* Tenant Information  
* Lease Status

### Lease Management Information

* Requested Action  
* Reason for Request  
* Effective Date  
* Remarks (Optional)

## 7. Required Documents

Depending on the requested action:

* Updated Lease Agreement  
* Supporting Legal Documents  
* Government-issued Identification  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule for chargeable lease management requests.

## 9. Payment Required

**Yes**

Payment is required for lease management requests that attract a regulatory service fee.

## 10. Processing Authority

**RERAN**

Where regulatory approval is required, the application is reviewed by the appropriate RERAN department before the lease record is updated.

## 11. Expected Processing Time

Subject to the type of lease management request and RERAN's regulatory service standards.

## 12. Processing Workflow

Login  
↓  
Open Services  
↓  
Select "Manage Lease"  
↓  
Select Registered Lease  
↓  
View Lease Details  
↓  
Select Required Action  
↓  
Update Lease Information (if applicable)  
↓  
Upload Supporting Documents  
↓  
Review Service Fee  
↓  
Complete Payment  
↓  
Submit Request  
↓  
Application Validation  
↓  
RERAN Review (if required)  
↓  
Application Approved  
↓  
Lease Record Updated  
↓  
View Updated Lease Information

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted  
↓  
Validation  
↓  
Under Review  
↓  
Information Requested  
↓  
Resubmitted  
↓  
Approved  
↓  
Completed

### Additional Statuses

* Returned  
* Rejected  
* Withdrawn  
* Cancelled

## 14. Possible Outcomes

* Lease Successfully Updated  
* Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Updated Lease Record  
* Lease Management Confirmation  
* Updated Lease Information  
* Request Reference Number  
* Payment Receipt

## 16. Related Services

* Service \#23 – Register Lease  
* Service \#24 – Renew Lease  
* Service \#26 – Submit Tenancy Dispute  
* Service \#3 – Verify Property

## 17. UI Screens

* Services  
* Manage Lease  
* Lease List  
* Lease Details  
* Lease Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Lease Management Confirmation

## 18. API Requirements

* Retrieve User Leases  
* Retrieve Lease Details  
* Validate Lease  
* Update Lease Information  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Lease Management Request  
* Retrieve Application Status  
* Update Lease Record  
* Retrieve Updated Lease Information

## 19. Database Entities

* User  
* Property  
* Lease  
* Lease Management Request  
* Landlord  
* Tenant  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Audit Log  
* Notification

## 20. Acceptance Criteria

* User can access authorized registered leases.  
* System validates user authorization before allowing lease management actions.  
* Required information is validated before submission.  
* Supporting documents are uploaded successfully.  
* Payment is completed where applicable.  
* Application receives a unique reference number.  
* User can monitor the application status.  
* Approved requests update the official lease record.  
* Updated lease information is immediately available after approval.  
* Payment receipt is generated after successful payment.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only authorized users may access and manage a registered lease.  
2. Payment is required only for lease management requests that attract a regulatory fee.  
3. Lease management does not transfer property ownership or tenancy rights.  
4. Requests requiring regulatory approval become effective only after RERAN approval.  
5. All updates must preserve the complete history of the lease.  
6. The original lease record remains permanently available for audit purposes.  
7. Every lease management request receives a unique application reference number.  
8. All lease updates, approvals, payments, document submissions, and user activities must be permanently recorded in the audit trail.  
9. Any change affecting the legal rights or obligations of either party must comply with applicable RERAN regulations before approval.
