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

# Service #15 – Amend Usufruct Right

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Amend Usufruct Right** service enables authorized parties to update or correct information contained in an existing registered usufruct right. The service ensures that approved amendments are officially recorded in the RERAN property registry while preserving the legal validity and historical record of the original registration.

## 2. Purpose

Enable authorized parties to amend registered usufruct rights while maintaining accurate and up-to-date records within the official property registry.

## 3. Description

The service allows eligible applicants to submit amendments to an existing registered usufruct right. Amendments may include changes to beneficiary information, usufruct duration, scope of rights, conditions, or other permitted details. Following verification and approval, the official property registry is updated and revised registration documents are issued where applicable.

## 4. Who Can Apply

### Property Owner

* Registered Property Owner  
* Joint Property Owner  
* Authorized Representative acting under a valid Power of Attorney

### Registered Usufruct Beneficiary

* Registered Individual User  
* Registered Legal Entity (where applicable)  
* Authorized Representative (where legally permitted)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* A registered usufruct right exists.  
* Applicant is authorized to request amendments.  
* Supporting documents are available.  
* Required approvals or consents have been obtained where applicable.

## 6. Required Information

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Existing Usufruct Information

* Usufruct Registration Number  
* Registration Date

### Amendment Information

* Amendment Type  
* Existing Information  
* Updated Information  
* Reason for Amendment  
* Effective Date  
* Additional Remarks (Optional)

## 7. Required Documents

* Existing Usufruct Registration Certificate  
* Existing Usufruct Agreement  
* Amendment Agreement or Supporting Legal Document  
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

**10–15 minutes.**

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Amend Usufruct Right"  
↓  
Select Registered Usufruct Right  
↓  
Select Amendment Type  
↓  
Update Usufruct Information  
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
Verify Existing Registration  
↓  
Review Amendment Request  
↓  
Verify Supporting Documents  
↓  
Approve Amendment  
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

* Usufruct Right Successfully Amended  
* Registry Successfully Updated  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Updated Electronic Usufruct Registration Certificate  
* Updated Electronic Usufruct Title Deed  
* Updated Property Registry Record  
* Amendment Confirmation  
* Payment Receipt

## 16. Related Services

* Service \#14 – Register Usufruct Right  
* Service \#16 – Terminate Usufruct Right  
* Service \#5 – Transfer Property Ownership  
* Service \#7 – Update Property Ownership Information

## 17. UI Screens

* Services  
* Amend Usufruct Right  
* Select Registered Usufruct Right  
* Select Amendment Type  
* Update Usufruct Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Amendment Confirmation

## 18. API Requirements

* Retrieve Registered Usufruct Rights  
* Retrieve Usufruct Details  
* Validate Registration Status  
* Validate Applicant  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Amendment Application  
* Retrieve Application Status  
* Update Property Registry  
* Generate Updated Registration Documents  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Usufruct Right  
* Usufruct Amendment  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can submit an amendment request for an eligible registered usufruct right.  
* System validates that the usufruct right is active and eligible for amendment.  
* The requested amendment information is validated before submission.  
* Required supporting documents are uploaded successfully.  
* Payment is completed before regulatory review.  
* Application receives a unique application reference number.  
* Approved applications update the official property registry.  
* Updated registration documents are generated where applicable.  
* Applicant receives completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only authorized parties to a registered usufruct right or their authorized representatives may request an amendment.  
2. The usufruct right must be active and registered before an amendment request can be submitted.  
3. Only information permitted under applicable regulations may be amended.  
4. Payment must be completed before the application proceeds for review.  
5. Amendments become legally effective only after approval by RERAN.  
6. The official property registry is updated only after the amendment has been approved.  
7. Updated registration documents are issued only when the approved amendment affects registered information.  
8. Every Amend Usufruct Right application receives a unique application reference number.  
9. Previous registration details and amendment history must be permanently retained for legal and audit purposes.  
10. All applications, approvals, payments, registry updates, document submissions, amendment history, and notifications must be permanently recorded in the audit trail.
