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

# Service #27 – Cancel Tenancy Contract

**Service Category:** Tenancy Services

## 1. Service Overview

The **Cancel Tenancy Contract** service enables landlords and tenants to formally terminate a registered tenancy contract before or upon the expiration of its agreed term. The service records the cancellation in the official RERAN tenancy registry, updates the tenancy records, and issues a cancellation confirmation upon successful approval.

## 2. Purpose

Enable the lawful cancellation of registered tenancy contracts while maintaining accurate tenancy records within the official RERAN registry.

## 3. Description

The service allows an eligible landlord, tenant, or authorized representative to submit a tenancy contract cancellation request. The applicant provides the tenancy details, cancellation reason, supporting documents, and completes the applicable service fee. Following verification and approval, the tenancy contract is cancelled, the tenancy registry is updated, and an official cancellation record is generated.

## 4. Who Can Apply

### Landlord

* Registered Property Owner  
* Registered Lessor  
* Authorized Representative acting under a valid Power of Attorney

### Tenant

* Registered Individual User  
* Authorized Representative (where legally permitted)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* A registered tenancy contract exists.  
* Applicant is a party to the tenancy agreement or an authorized representative.  
* Required supporting documents are available.

## 6. Required Information

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Landlord Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Tenant Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Cancellation Information

* Tenancy Registration Number  
* Cancellation Date  
* Reason for Cancellation  
* Vacate Date  
* Mutual Agreement Status  
* Additional Remarks (Optional)

## 7. Required Documents

* Registered Tenancy Agreement  
* Government-issued Identification of Applicant  
* Mutual Termination Agreement (where applicable)  
* Court Order (where applicable)  
* Proof of Property Ownership (for Landlord)  
* Proof of Payment  
* Power of Attorney (where applicable)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before the application is submitted.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**Approximately 20–30 minutes.**

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Cancel Tenancy Contract"  
↓  
Select Registered Tenancy Contract  
↓  
Review Contract Details  
↓  
Provide Cancellation Information  
↓  
Upload Required Documents  
↓  
Review Application  
↓  
Complete Payment  
↓  
Submit Application

↓

RERAN

Review Application  
↓  
Verify Tenancy Registration  
↓  
Verify Supporting Documents  
↓  
Review Cancellation Request  
↓  
Approve Contract Cancellation  
↓  
Update Tenancy Registry  
↓  
Generate Cancellation Confirmation  
↓  
Notify Landlord & Tenant

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted  
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
* Cancelled  
* Withdrawn

## 14. Possible Outcomes

* Tenancy Contract Successfully Cancelled  
* Tenancy Registry Successfully Updated  
* Cancellation Successfully Recorded  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Tenancy Contract Cancellation Certificate  
* Updated Tenancy Registration Record  
* Cancellation Confirmation  
* Payment Receipt

## 16. Related Services

* Service \#23 – Register Lease  
* Service \#24 – Renew Lease  
* Service \#25 – Manage Lease  
* Service \#26 – Submit Tenancy Dispute

## 17. UI Screens

* Services  
* Cancel Tenancy Contract  
* Select Registered Tenancy Contract  
* Cancellation Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Cancellation Confirmation

## 18. API Requirements

* Retrieve Registered Tenancy Contracts  
* Retrieve Contract Details  
* Validate Tenancy Registration  
* Validate Applicant  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Cancellation Application  
* Retrieve Application Status  
* Update Tenancy Registry  
* Generate Cancellation Certificate  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Tenancy Agreement  
* Tenancy Registration  
* Tenancy Cancellation  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can submit a tenancy contract cancellation request.  
* System validates that the tenancy contract is active and eligible for cancellation.  
* Required information is validated before submission.  
* Required supporting documents are uploaded successfully.  
* Payment is completed before regulatory review.  
* Application receives a unique application reference number.  
* Approved applications update the official tenancy registry.  
* A cancellation certificate is generated upon approval.  
* Landlord and tenant receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the landlord, tenant, or an authorized representative may submit a tenancy contract cancellation request.  
2. The tenancy contract must be registered and active before it can be cancelled.  
3. Where required by law or the tenancy agreement, the consent of both landlord and tenant shall be obtained before cancellation.  
4. A court order or regulatory decision may be required in cases involving disputes or unilateral termination.  
5. Payment must be completed before the application proceeds for review.  
6. The tenancy contract is considered cancelled only after approval by RERAN.  
7. The official tenancy registry is updated only after the cancellation has been approved.  
8. Every Cancel Tenancy Contract application receives a unique application reference number.  
9. The cancelled tenancy contract shall remain permanently available as part of the property's tenancy history.  
10. All applications, approvals, payments, registry updates, document submissions, cancellation records, and notifications must be permanently recorded in the audit trail.
