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
  - service-flow
  - property-ownership-transaction
---

# Service #6 – Register Property Sale

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Register Property Sale** service enables an Individual User to officially register the sale of a property with RERAN. The service records the property sale transaction, validates the transaction details and supporting documents, and maintains an official regulatory record of the sale. The registered sale becomes part of the property's transaction history and supports subsequent ownership transfer where applicable.

## 2. Purpose

Enable property owners to officially register a property sale with RERAN and create a regulatory record of the transaction.

## 3. Description

The service allows a property owner or an authorized representative to submit the details of a property sale, including seller information, purchaser information, property details, transaction details, and supporting documents. After review and approval by RERAN, the sale transaction is officially recorded within the property registry.

## 4. Who Can Apply

* Registered Property Owner  
* Joint Property Owner  
* Authorized Power of Attorney Holder  
* Court-Appointed Representative (where legally permitted)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is already registered with RERAN.  
* Applicant is authorized to sell the property.  
* Purchaser information is available.  
* Required supporting documents are available.

## 6. Required Information

### Seller Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Purchaser Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Property Information

* Property Registration Number  
* Property Address  
* Property Type  
* Development Project (if applicable)

### Sale Information

* Sale Agreement Number  
* Sale Date  
* Sale Price  
* Payment Method  
* Transaction Reference Number  
* Booking Reference Number  
* Remarks (Optional)

## 7. Required Documents

* Sale Agreement  
* Purchase Agreement  
* Existing Ownership Certificate  
* Government-issued Identification  
* Proof of Payment  
* Power of Attorney (where applicable)  
* Tax Clearance (where applicable)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before the property sale registration application is submitted.

## 10. Processing Authority

**RERAN**

The sale registration application is reviewed by the appropriate RERAN department before the sale transaction is officially recorded.

## 11. Expected Processing Time

**25–35 minutes**

## 12. Processing Workflow

Seller

Login  
↓  
Open Services  
↓  
Select "Register Property Sale"  
↓  
Select Property  
↓  
Enter Property Sale Information  
↓  
Upload Property Photos  
↓  
Enter Bank Details  
↓  
Send Sale Request to Purchaser  
↓  
Receive Booking Reference Number  
↓  
Review Service Fee  
↓  
Complete Payment  
↓  
Submit Application

↓

Purchaser Receives Booking Reference

↓

Login  
↓  
Select "Register Property Sale"  
↓  
Enter Booking Reference Number  
↓  
Verify OTP  
↓  
Review Property Details  
↓  
Accept Property Details  
↓  
Enter Purchaser Information  
↓  
Upload Required Documents  
↓  
Review Service Fee  
↓  
Complete Payment  
↓  
Submit Response

↓

RERAN Review  
↓  
Approval  
↓  
Property Sale Registered  
↓  
Download Sale Registration Documents

## 13. Application Status Flow

Draft  
↓  
Booking Pending  
↓  
Purchaser Response Pending  
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
* Withdrawn  
* Cancelled

## 14. Possible Outcomes

* Property Sale Successfully Registered  
* Purchaser Accepted Sale  
* Purchaser Declined Sale  
* Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful approval, the system generates:

* E-Certificate of Title  
* Title Deed  
* Usufruct Right e-Certificate (where applicable)  
* Provisional Sale Contract  
* Provisional Registration Contract  
* Updated Property Transaction Record  
* Fee Balance Information  
* Property Map  
* Payment Receipt

## 16. Related Services

* Service \#3 – Verify Property  
* Service \#5 – Transfer Property Ownership  
* Service \#4 – Register Property Ownership  
* Service \#7 – Update Property Ownership Information

## 17. UI Screens

* Services  
* Register Property Sale  
* Select Property  
* Sale Information  
* Property Photos  
* Bank Details  
* Booking Reference  
* Purchaser Verification  
* OTP Verification  
* Purchaser Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Sale Registration Confirmation

## 18. API Requirements

* Retrieve User Properties  
* Retrieve Property Details  
* Generate Booking Reference  
* Send Sale Invitation  
* Verify OTP  
* Validate Purchaser  
* Upload Documents  
* Upload Property Photos  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Sale Registration Application  
* Retrieve Application Status  
* Generate Sale Registration Documents  
* Download Documents

## 19. Database Entities

* User  
* Property  
* Property Sale  
* Seller  
* Purchaser  
* Booking Reference  
* OTP Verification  
* Application  
* Service Request  
* Document  
* Property Images  
* Payment  
* Payment Transaction  
* Audit Log  
* Notification

## 20. Acceptance Criteria

* Seller can initiate a property sale for an eligible property.  
* System generates a unique booking reference number.  
* Purchaser can access the transaction using the booking reference number.  
* OTP verification is completed before purchaser participation.  
* Purchaser reviews and accepts the property information.  
* Required documents are uploaded successfully.  
* Payment is completed before submission.  
* Application receives a unique reference number.  
* RERAN reviews and processes the application.  
* Approved applications create an official property sale record.  
* Sale documents are generated upon approval.  
* Payment receipt is generated after successful payment.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the registered property owner or a legally authorized representative may initiate a property sale.  
2. The property must already be registered within the RERAN property registry.  
3. A unique booking reference number must be generated for every sale transaction.  
4. The purchaser must verify their identity using OTP before participating in the transaction.  
5. Both seller and purchaser must complete their respective parts of the workflow before the application proceeds for review.  
6. Payment must be completed before the application is submitted.  
7. Registering a property sale records the sale transaction but does not automatically transfer legal ownership.  
8. Ownership transfer must be completed through the **Transfer Property Ownership** service after the sale registration is approved.  
9. Properties with multiple owners must obtain all required owner approvals before the sale can be approved.  
10. All activities, approvals, payments, and document submissions must be permanently recorded in the audit trail.
