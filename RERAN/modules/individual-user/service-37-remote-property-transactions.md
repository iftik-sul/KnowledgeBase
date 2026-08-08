---
project: RERAN
module: individual-user
type: service-flow
status: current
updated: 2026-08-09
derived_from:
  - "RERAN/modules/individual-user/RERAN_ individual user_service_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
tags:
  - individual-user
  - service-flow
  - diaspora
---

# Service #37 – Remote Property Transactions

**Service Category:** Diaspora Services

## 1. Service Overview

The **Remote Property Transactions** service enables eligible users to complete property-related transactions through the RERAN platform without being physically present in Nigeria. The service supports secure digital processing of property transactions, allowing verified users to submit applications, upload documents, complete payments, and receive regulatory approvals remotely.

## 2. Purpose

Enable eligible users to securely complete property-related transactions remotely while ensuring compliance with RERAN regulations.

## 3. Description

The service allows users who have successfully completed identity verification to initiate and manage eligible property transactions through the RERAN platform. Depending on the selected transaction, users may submit applications, upload supporting documents, complete regulatory payments, monitor application progress, and receive digital approvals and certificates without visiting a RERAN office.

## 4. Who Can Apply

* Diaspora Investor  
* Nigerian Citizen Living Abroad  
* Property Owner Living Abroad  
* Property Buyer Living Abroad  
* Authorized Representative acting on behalf of a verified user

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Remote Identity Verification has been successfully completed.  
* User is eligible for the selected property transaction.  
* Required supporting documents are available.

## 6. Required Information

### Applicant Information

* Full Name  
* National Identification Number (NIN)  
* Contact Information  
* Country of Residence

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Transaction Information

* Transaction Type  
* Transaction Details  
* Property Owner Information (where applicable)  
* Purchaser Information (where applicable)  
* Additional Remarks (Optional)

## 7. Required Documents

Depending on the selected transaction:

* Verified Identity Documents  
* Property Ownership Documents  
* Sale Agreement  
* Lease Agreement  
* Power of Attorney (where applicable)  
* Proof of Payment  
* Other supporting documents required for the selected service

## 8. Service Fee

Applicable according to the RERAN fee schedule for the selected transaction.

## 9. Payment Required

**Yes**

Payment must be completed before the transaction application is submitted.

## 10. Processing Authority

**RERAN**

The application is processed by the appropriate RERAN department based on the selected transaction.

## 11. Expected Processing Time

Subject to the selected service and RERAN's regulatory service standards.

## 12. Processing Workflow

Login  
↓  
Open Services  
↓  
Select "Remote Property Transactions"  
↓  
Complete Identity Verification Check  
↓  
Select Transaction Type  
↓  
Select Property  
↓  
Enter Transaction Information  
↓  
Upload Supporting Documents  
↓  
Review Application  
↓  
Review Service Fee  
↓  
Complete Payment  
↓  
Submit Application  
↓  
Application Validation  
↓  
RERAN Review  
↓  
Additional Information Requested (if required)  
↓  
Applicant Responds  
↓  
Final Review  
↓  
Application Approved  
↓  
Transaction Completed  
↓  
Download Transaction Documents

## 13. Application Status Flow

Draft  
↓  
Identity Verification Pending  
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

* Identity Verification Failed  
* Returned  
* Rejected  
* Withdrawn  
* Cancelled

## 14. Possible Outcomes

* Transaction Successfully Completed  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Identity Verification Failed  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Transaction Confirmation  
* Transaction Reference Number  
* Updated Property Record (where applicable)  
* Digital Certificate or Approval Document (where applicable)  
* Payment Receipt

## 16. Related Services

* Service \#36 – Remote Identity Verification  
* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership  
* Service \#6 – Register Property Sale  
* Service \#23 – Register Lease  
* Service \#29 – Register Power of Attorney

## 17. UI Screens

* Services  
* Remote Property Transactions  
* Transaction Type Selection  
* Select Property  
* Transaction Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Transaction Confirmation

## 18. API Requirements

* Validate Identity Verification Status  
* Retrieve Eligible Properties  
* Retrieve Available Transaction Types  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Transaction Application  
* Retrieve Application Status  
* Generate Transaction Confirmation  
* Download Transaction Documents

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Transaction  
* Application  
* Service Request  
* Document  
* Identity Verification  
* Payment  
* Payment Transaction  
* Audit Log  
* Notification

## 20. Acceptance Criteria

* User has a verified identity before initiating a remote transaction.  
* User can select an eligible property transaction.  
* Required information is validated before submission.  
* Supporting documents are uploaded successfully.  
* Payment is completed before submission.  
* Application receives a unique reference number.  
* User can monitor the application throughout the review process.  
* Approved applications complete the requested transaction.  
* Relevant transaction documents are generated after approval.  
* Payment receipt is generated after successful payment.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only users with a successfully verified identity may access remote property transaction services.  
2. The requested transaction must comply with all applicable RERAN regulations.  
3. Payment must be completed before the application is submitted.  
4. Each transaction is processed according to the business rules governing the selected service.  
5. Supporting documents must be submitted and validated before review.  
6. Additional information may be requested during the review process.  
7. Approved transactions update the relevant property records where applicable.  
8. Every remote transaction is assigned a unique transaction reference number.  
9. All applications, approvals, payments, document submissions, and completed transactions must be permanently recorded in the audit trail.
