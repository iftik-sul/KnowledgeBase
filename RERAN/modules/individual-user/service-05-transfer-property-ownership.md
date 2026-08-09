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
  - property-ownership-transaction
---

# Service #5 – Transfer Property Ownership

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Transfer Property Ownership** service enables the legal transfer of ownership of a registered property from the current owner to a new owner. The service records the ownership transfer within the official RERAN property registry after validating the transaction, supporting documents, and regulatory requirements. Upon successful approval, the title records are updated and a new electronic Certificate of Title is issued.

## 2. Purpose

Enable the legal transfer of ownership of a registered property while maintaining accurate ownership records within the official RERAN property registry.

## 3. Description

The service allows the current property owner to transfer ownership of a registered property to another eligible individual or entity. The applicant submits the required property information, transferee information, supporting documents, and completes the applicable service fee. Following review and approval by RERAN, the ownership record is updated and the new title documents are issued electronically.

## 4. Who Can Apply

* Registered Property Owner  
* Joint Property Owner  
* Authorized Representative acting under a valid Power of Attorney  
* Court-appointed Representative (where legally applicable)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is registered with RERAN.  
* Applicant has legal authority to transfer ownership.  
* Required supporting documents are available.  
* Transferee information is available.

## 6. Required Information

### Current Owner Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### New Owner Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Property Information

* Property Registration Number  
* Property Address  
* Property Type  
* Plot Number (where applicable)

### Transfer Information

* Transfer Reason  
* Transfer Date  
* Transfer Value  
* Ownership Type  
* Additional Remarks (Optional)

## 7. Required Documents

* Existing Certificate of Title  
* Transfer Agreement  
* Government-issued Identification (Transferor)  
* Government-issued Identification (Transferee)  
* Proof of Payment  
* Power of Attorney (where applicable)  
* Court Order (where applicable)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before the application is submitted.

## 10. Processing Authority

Compliance & Escrow Auditor

## 11. Expected Processing Time

25 minutes.

## 12. Processing Workflow

Option 1 – Customer Center

Visit Customer Center at Land Department  
↓  
Submit Required Documents  
↓  
Officer Reviews Documents  
↓  
Property Transfer Information Entered into System  
↓  
Transaction Audited  
↓  
Pay Service Fee  
↓  
Application Approved  
↓  
Electronic Certificate of Title and Property Map Sent via Email

──────────────────────────

Option 2 – Online

Login  
↓  
Open Services  
↓  
Select "Transfer Property Ownership"  
↓  
Select Registered Property  
↓  
Enter New Owner Information  
↓  
Upload Required Documents  
↓  
Review Application  
↓  
Complete Payment  
↓  
Submit Application  
↓  
RERAN Review  
↓  
Application Approved  
↓  
Receive Electronic Certificate of Title and Property Map

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

* Ownership Successfully Transferred  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Electronic Certificate of Title  
* Electronic Title Deed  
* Electronic Property Map

## 16. Related Services

* Service \#4 – Register Property Ownership  
* Service \#6 – Register Property Sale  
* Service \#7 – Update Property Ownership Information  
* Service \#3 – Verify Property

## 17. UI Screens

* Services  
* Transfer Property Ownership  
* Select Property  
* New Owner Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Certificate of Title

## 18. API Requirements

* Retrieve User Properties  
* Retrieve Property Details  
* Validate Property Ownership  
* Validate New Owner  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Title Transfer Application  
* Retrieve Application Status  
* Generate Electronic Certificate of Title  
* Download Title Documents

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Ownership History  
* Title Transfer  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Audit Log  
* Notification

## 20. Acceptance Criteria

* User can submit a title transfer application for an eligible property.  
* System validates ownership before submission.  
* Required information is validated successfully.  
* Supporting documents are uploaded successfully.  
* Payment is completed before submission.  
* Application receives a unique reference number.  
* User can monitor the application status.  
* Approved applications update the official ownership registry.  
* Electronic Certificate of Title and Property Map are generated after approval.  
* Payment receipt is generated after successful payment.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the registered property owner or an authorized representative may initiate a title transfer.  
2. The property must already be registered in the RERAN property registry.  
3. Payment must be completed before the application is submitted.  
4. Ownership transfer becomes legally effective only after approval by RERAN.  
5. All mandatory supporting documents must be submitted before the application proceeds for review.  
6. The official ownership registry is updated only after successful approval.  
7. A new Electronic Certificate of Title is issued upon successful ownership transfer.  
8. The previous ownership record must remain permanently available in the ownership history.  
9. Every title transfer application receives a unique application reference number.  
10. All submissions, approvals, payments, ownership changes, and document uploads must be permanently recorded in the audit trail.
