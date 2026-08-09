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

# Service #12 – Release Lease-to-Own

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Release Lease-to-Own** service enables the termination and release of a registered lease-to-own agreement after the contractual obligations have been fulfilled or the agreement has otherwise been concluded. Upon approval, the lease-to-own registration is closed, the property records are updated, and the appropriate ownership status is reflected in the official property registry.

## 2. Purpose

Enable the lawful release of a registered lease-to-own agreement while ensuring that the official property records accurately reflect the final ownership status of the property.

## 3. Description

The service allows eligible applicants to request the release of an existing lease-to-own agreement. The applicant submits the required information, supporting documents, and applicable service fee. Following verification and approval, the lease-to-own agreement is released, the property registry is updated, and the appropriate registration documents are issued.

## 4. Who Can Apply

### Property Owner

* Registered Property Owner  
* Joint Property Owner  
* Authorized Representative acting under a valid Power of Attorney

### Lease-to-Own Purchaser

* Registered Lease-to-Own Purchaser  
* Authorized Representative (where legally permitted)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* A valid lease-to-own agreement exists.  
* The applicant is authorized to request the release.  
* All contractual obligations required for the release have been satisfied.  
* Required supporting documents are available.

## 6. Required Information

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Property Owner Information

* Full Name  
* National Identification Number (NIN)  
* Contact Information

### Lease-to-Own Purchaser Information

* Full Name  
* National Identification Number (NIN)  
* Contact Information

### Release Information

* Lease-to-Own Registration Number  
* Release Date  
* Release Reason  
* Final Settlement Status  
* Additional Remarks (Optional)

## 7. Required Documents

* Existing Lease-to-Own Registration Certificate  
* Lease-to-Own Agreement  
* Evidence of Completion or Settlement  
* Government-issued Identification  
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

**Approximately 25 minutes.**

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Release Lease-to-Own"  
↓  
Select Registered Lease-to-Own Agreement  
↓  
Review Agreement Details  
↓  
Provide Release Information  
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
Verify Agreement Status  
↓  
Verify Supporting Documents  
↓  
Confirm Contract Completion  
↓  
Approve Release  
↓  
Update Property Registry  
↓  
Generate Updated Registration Documents  
↓  
Notify Applicant

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

* Lease-to-Own Successfully Released  
* Agreement Successfully Closed  
* Property Registry Updated  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Release Confirmation Certificate  
* Updated Electronic Certificate of Title (where applicable)  
* Updated Electronic Title Deed (where applicable)  
* Updated Property Registry Record  
* Payment Receipt

## 16. Related Services

* Service \#10 – Register Lease-to-Own  
* Service \#11 – Transfer Lease-to-Own  
* Service \#13 – Amend Lease-to-Own  
* Service \#5 – Transfer Property Ownership

## 17. UI Screens

* Services  
* Release Lease-to-Own  
* Select Registered Agreement  
* Release Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Release Confirmation

## 18. API Requirements

* Retrieve Registered Lease-to-Own Agreements  
* Retrieve Agreement Details  
* Validate Agreement Status  
* Validate Applicant  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Release Application  
* Retrieve Application Status  
* Update Property Registry  
* Generate Release Documents  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Lease-to-Own Agreement  
* Lease-to-Own Release  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can request the release of an eligible lease-to-own agreement.  
* System validates that the agreement is active and eligible for release.  
* Required information is validated before submission.  
* Required supporting documents are uploaded successfully.  
* Payment is completed before regulatory review.  
* Application receives a unique application reference number.  
* Approved applications update the official property registry.  
* Release documents are generated after successful approval.  
* Applicant receives completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only an authorized party to the lease-to-own agreement or an authorized representative may request its release.  
2. The lease-to-own agreement must be registered and active before a release request can be submitted.  
3. All contractual obligations required for the release must be fulfilled before approval.  
4. Payment must be completed before the application proceeds for review.  
5. The property registry is updated only after the release application has been approved.  
6. Where applicable, updated ownership documents are issued following the release.  
7. Every Release Lease-to-Own application receives a unique application reference number.  
8. The release permanently closes the existing lease-to-own registration while preserving its historical record.  
9. Any future ownership transaction must be initiated through the appropriate RERAN service.  
10. All applications, approvals, payments, registry updates, document submissions, and notifications must be permanently recorded in the audit trail.
