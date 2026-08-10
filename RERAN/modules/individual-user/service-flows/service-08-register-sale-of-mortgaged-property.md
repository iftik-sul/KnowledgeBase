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

# Service #8 – Register Sale of Mortgaged Property

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Register Sale of Mortgaged Property** service enables a property owner to legally sell a property that is currently under mortgage. The service coordinates the transaction between the seller, purchaser, mortgage lender, and RERAN to ensure that the mortgage obligations are fulfilled before ownership is transferred and the property registration is completed.

## 2. Purpose

Enable the lawful sale of a mortgaged property while protecting the interests of the purchaser, seller, mortgage lender, and RERAN through a regulated registration process.

## 3. Description

The service allows the seller and purchaser to jointly initiate the sale of a mortgaged property. The transaction is registered with RERAN, the required documents are submitted, fees are paid, and the application is reviewed by the Compliance & Escrow Auditor. Once the mortgage lender issues a Mortgage Release Letter confirming settlement or release of the mortgage, RERAN completes the property registration and finalizes the ownership transfer.

## 4. Who Can Apply

### Seller

* Registered Property Owner  
* Joint Property Owner  
* Authorized Representative acting under a valid Power of Attorney

### Purchaser

* Registered Individual User  
* Eligible Property Buyer  
* Authorized Representative (where legally permitted)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* Seller and purchaser are identified.  
* Property is registered with RERAN.  
* Property is currently under a registered mortgage.  
* Mortgage lender has been identified.  
* Required supporting documents are available.

## 6. Required Information

### Seller Information

* Full Name  
* National Identification Number (NIN)  
* Contact Information

### Purchaser Information

* Full Name  
* National Identification Number (NIN)  
* Contact Information

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Mortgage Information

* Mortgage Institution  
* Mortgage Account / Reference Number  
* Outstanding Mortgage Status

### Sale Information

* Sale Value  
* Agreed Sale Date  
* Additional Remarks (Optional)

## 7. Required Documents

* Existing Certificate of Title  
* Mortgage Agreement  
* Sale Agreement  
* Government-issued Identification (Seller)  
* Government-issued Identification (Purchaser)  
* Mortgage Release Letter *(required before completion of registration)*  
* Proof of Payment  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before the application proceeds for regulatory review.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**15–20 minutes** (registration process), excluding any time required by the mortgage lender to issue the Mortgage Release Letter.

## 12. Processing Workflow

Seller

Login  
↓  
Open Services  
↓  
Select "Register Sale of Mortgaged Property"  
↓  
Select Registered Property  
↓  
Enter Purchaser Information  
↓  
Enter Mortgage Information  
↓  
Upload Required Documents  
↓  
Review Application  
↓  
Complete Payment  
↓  
Submit Application

↓

Purchaser

Receive Transaction Notification  
↓  
Login  
↓  
Review Property Information  
↓  
Review Mortgage Information  
↓  
Accept Transaction  
↓  
Upload Required Documents  
↓  
Confirm Participation

↓

Mortgage Institution

Review Settlement  
↓  
Issue Mortgage Release Letter

↓

RERAN

Review Application  
↓  
Verify Mortgage Release  
↓  
Approve Registration  
↓  
Update Property Registry  
↓  
Generate Electronic Title Documents  
↓  
Notify Seller & Purchaser

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted  
↓  
Purchaser Confirmation Pending  
↓  
Mortgage Release Pending  
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
* Mortgage Release Rejected

## 14. Possible Outcomes

* Sale Successfully Registered  
* Mortgage Successfully Released  
* Ownership Successfully Transferred  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Mortgage Release Not Received  
* Transaction Cancelled

## 15. Output

Upon successful completion, the system generates:

* Electronic Certificate of Title  
* Electronic Title Deed  
* Updated Property Ownership Record  
* Mortgage Release Confirmation  
* Property Map  
* Payment Receipt

## 16. Related Services

* Service \#5 – Transfer Property Ownership  
* Service \#6 – Register Property Sale  
* Service \#7 – Update Property Ownership Information  
* Service \#1 – Verify Developer  
* Service \#2 – Verify Development Project  
* Service \#3 – Verify Property
* Financial & Trust Institutions Service \#6 – Mortgage Release *(cross-module: this is the source of the Mortgage Release Letter required at Section 7 above — the mortgage lender discharges the encumbrance through that service before this one can complete ownership transfer)*
* Financial & Trust Institutions Service \#3 – Mortgage Registration *(cross-module: the service that originally registered the mortgage this service's sale must clear)*

## 17. UI Screens

* Services  
* Register Sale of Mortgaged Property  
* Select Property  
* Purchaser Information  
* Mortgage Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Mortgage Status  
* Registration Confirmation

## 18. API Requirements

* Retrieve User Properties  
* Retrieve Property Details  
* Retrieve Mortgage Information  
* Validate Property Ownership  
* Validate Mortgage Status  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Sale Registration Application  
* Retrieve Application Status  
* Verify Mortgage Release  
* Update Property Ownership  
* Generate Electronic Certificate of Title  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Mortgage  
* Mortgage Institution  
* Property Sale  
* Title Transfer  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Seller can initiate the sale of a mortgaged property.  
* System validates that the property is under an active mortgage.  
* Purchaser successfully confirms participation.  
* Required information is validated before submission.  
* Required documents are uploaded successfully.  
* Payment is completed before regulatory review.  
* Application receives a unique application reference number.  
* Mortgage Release Letter is received before ownership transfer is completed.  
* Approved applications update the official property registry.  
* Electronic title documents are generated upon successful completion.  
* Seller and purchaser receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the registered property owner or an authorized representative may initiate the sale of a mortgaged property.  
2. The property must be registered in the official RERAN property registry.  
3. The property must have an active registered mortgage.  
4. Both the seller and purchaser must participate in the transaction.  
5. Payment must be completed before the application proceeds for review.  
6. The mortgage lender must issue a valid Mortgage Release Letter before ownership can be transferred.  
7. Ownership transfer becomes legally effective only after RERAN approves the application and updates the property registry.  
8. A new Electronic Certificate of Title is issued after successful registration.  
9. Every application receives a unique application reference number.  
10. All applications, approvals, mortgage verifications, payments, ownership transfers, document uploads, and notifications must be permanently recorded in the audit trail.
