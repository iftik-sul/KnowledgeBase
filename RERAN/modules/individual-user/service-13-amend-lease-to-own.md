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

# Service #13 – Amend Lease-to-Own

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Amend Lease-to-Own** service enables authorized parties to update or correct information contained in an existing registered lease-to-own agreement. The service ensures that amendments are officially reviewed, approved, and recorded in the RERAN property registry while preserving the integrity and history of the original agreement.

## 2. Purpose

Enable authorized parties to amend a registered lease-to-own agreement while maintaining accurate and up-to-date records within the official RERAN property registry.

## 3. Description

The service allows eligible applicants to submit amendments to an existing lease-to-own agreement. Amendments may include changes to contractual terms, participant information, payment schedules, or other permitted agreement details. Following verification and approval, the amended information is recorded in the official registry and updated registration documents are issued where applicable.

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
* A registered lease-to-own agreement exists.  
* Applicant is authorized to request amendments.  
* All parties required for the amendment have provided their consent where applicable.  
* Supporting documents are available.

## 6. Required Information

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Agreement Information

* Lease-to-Own Registration Number  
* Agreement Date

### Amendment Information

* Amendment Type  
* Existing Information  
* Updated Information  
* Reason for Amendment  
* Effective Date  
* Additional Remarks (Optional)

## 7. Required Documents

* Existing Lease-to-Own Registration Certificate  
* Existing Lease-to-Own Agreement  
* Amendment Agreement or Addendum  
* Government-issued Identification  
* Supporting Legal Documents (where applicable)  
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
Select "Amend Lease-to-Own"  
↓  
Select Registered Lease-to-Own Agreement  
↓  
Select Amendment Type  
↓  
Update Agreement Information  
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
Verify Existing Agreement  
↓  
Review Amendment Request  
↓  
Verify Supporting Documents  
↓  
Approve Amendment  
↓  
Update Lease-to-Own Registry  
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

* Lease-to-Own Agreement Successfully Amended  
* Registry Successfully Updated  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Updated Lease-to-Own Registration Certificate  
* Updated Electronic Certificate of Title (where applicable)  
* Updated Electronic Title Deed (where applicable)  
* Updated Property Registry Record  
* Amendment Confirmation  
* Payment Receipt

## 16. Related Services

* Service \#10 – Register Lease-to-Own  
* Service \#11 – Transfer Lease-to-Own  
* Service \#12 – Release Lease-to-Own  
* Service \#5 – Transfer Property Ownership  
* Service \#7 – Update Property Ownership Information

## 17. UI Screens

* Services  
* Amend Lease-to-Own  
* Select Registered Agreement  
* Select Amendment Type  
* Update Agreement Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Amendment Confirmation

## 18. API Requirements

* Retrieve Registered Lease-to-Own Agreements  
* Retrieve Agreement Details  
* Validate Agreement Status  
* Validate Applicant  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Amendment Application  
* Retrieve Application Status  
* Update Lease-to-Own Registry  
* Generate Updated Registration Documents  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Lease-to-Own Agreement  
* Lease-to-Own Amendment  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can submit an amendment request for an eligible lease-to-own agreement.  
* System validates that the agreement is active and eligible for amendment.  
* The requested amendment information is validated before submission.  
* Required supporting documents are uploaded successfully.  
* Payment is completed before regulatory review.  
* Application receives a unique application reference number.  
* Approved applications update the official lease-to-own registry.  
* Updated registration documents are generated after approval where applicable.  
* Applicant receives completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only authorized parties to a registered lease-to-own agreement or their authorized representatives may request an amendment.  
2. The lease-to-own agreement must be active and registered before an amendment can be submitted.  
3. Only information permitted under applicable regulations and the terms of the agreement may be amended.  
4. Payment must be completed before the application proceeds for review.  
5. Amendments become legally effective only after approval by RERAN.  
6. The official lease-to-own registry is updated only after the amendment has been approved.  
7. Updated registration documents are issued only when the approved amendment affects registered information.  
8. Every Amend Lease-to-Own application receives a unique application reference number.  
9. Previous versions of the agreement and amendment history must be permanently retained for audit and legal purposes.  
10. All applications, approvals, payments, registry updates, document submissions, amendment history, and notifications must be permanently recorded in the audit trail.
