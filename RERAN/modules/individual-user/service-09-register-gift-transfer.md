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
  - service-flow
  - property-ownership-transaction
---

# Service #9 – Register Gift Transfer

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Register Gift Transfer** service enables a registered property owner to legally transfer ownership of a property to another individual without monetary consideration. The service records the gift transaction in the official RERAN property registry and issues updated ownership documents after regulatory approval.

## 2. Purpose

Enable property owners to legally transfer ownership of a property as a gift while maintaining accurate ownership records within the official RERAN property registry.

## 3. Description

The service allows the donor (current property owner) to transfer ownership of a registered property to a recipient without a sale transaction. The donor submits the required application, supporting documents, and applicable fees. Following review and approval by RERAN, the ownership records are updated and new title documents are issued to the recipient.

## 4. Who Can Apply

### Donor

* Registered Property Owner  
* Joint Property Owner  
* Authorized Representative acting under a valid Power of Attorney

### Recipient

* Registered Individual User  
* Eligible Property Recipient

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is registered with RERAN.  
* Donor has legal authority to transfer the property.  
* Recipient information is available.  
* Required supporting documents are available.

## 6. Required Information

### Donor Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Recipient Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Gift Transfer Information

* Gift Transfer Date  
* Relationship Between Donor and Recipient (where applicable)  
* Reason for Gift Transfer (Optional)  
* Additional Remarks (Optional)

## 7. Required Documents

* Existing Certificate of Title  
* Gift Transfer Declaration  
* Government-issued Identification (Donor)  
* Government-issued Identification (Recipient)  
* Proof of Property Ownership  
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

**25–30 minutes**.

## 12. Processing Workflow

Donor

Login  
↓  
Open Services  
↓  
Select "Register Gift Transfer"  
↓  
Select Registered Property  
↓  
Enter Recipient Information  
↓  
Upload Required Documents  
↓  
Review Application  
↓  
Complete Payment  
↓  
Submit Application

↓

Recipient

Receive Notification  
↓  
Login  
↓  
Review Gift Transfer Details  
↓  
Accept Gift Transfer  
↓  
Confirm Identity  
↓  
Confirm Participation

↓

RERAN

Review Application  
↓  
Verify Documents  
↓  
Approve Gift Transfer  
↓  
Update Property Registry  
↓  
Generate Electronic Title Documents  
↓  
Notify Donor & Recipient

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted  
↓  
Recipient Confirmation Pending  
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
* Recipient Declined

## 14. Possible Outcomes

* Gift Transfer Successfully Registered  
* Ownership Successfully Transferred  
* Recipient Accepted Gift  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Recipient Declined Gift

## 15. Output

Upon successful completion, the system generates:

* Electronic Certificate of Title  
* Electronic Title Deed  
* Updated Property Ownership Record  
* Property Map  
* Payment Receipt

## 16. Related Services

* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership  
* Service \#6 – Register Property Sale  
* Service \#7 – Update Property Ownership Information  
* Service \#3 – Verify Property

## 17. UI Screens

* Services  
* Register Gift Transfer  
* Select Property  
* Recipient Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Gift Transfer Confirmation

## 18. API Requirements

* Retrieve User Properties  
* Retrieve Property Details  
* Validate Property Ownership  
* Validate Recipient  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Gift Transfer Application  
* Retrieve Application Status  
* Update Property Ownership  
* Generate Electronic Certificate of Title  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Gift Transfer  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Donor can initiate a gift transfer for an eligible property.  
* System validates that the donor is authorized to transfer the property.  
* Recipient successfully confirms participation.  
* Required information is validated before submission.  
* Required documents are uploaded successfully.  
* Payment is completed before regulatory review.  
* Application receives a unique application reference number.  
* Approved applications update the official property registry.  
* Electronic title documents are generated upon successful completion.  
* Donor and recipient receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the registered property owner or an authorized representative may initiate a gift transfer.  
2. The property must be registered in the official RERAN property registry.  
3. Gift transfers do not involve the exchange of a purchase price between the donor and recipient.  
4. Payment of the applicable service fee must be completed before the application proceeds for review.  
5. The recipient must confirm acceptance of the gift transfer before ownership is transferred.  
6. Ownership transfer becomes legally effective only after approval by RERAN and the official property registry is updated.  
7. A new Electronic Certificate of Title is issued to the recipient upon successful registration.  
8. Every gift transfer application receives a unique application reference number.  
9. Previous ownership records must be retained for historical and audit purposes.  
10. All applications, approvals, ownership transfers, document submissions, payments, notifications, and registry updates must be permanently recorded in the audit trail.
