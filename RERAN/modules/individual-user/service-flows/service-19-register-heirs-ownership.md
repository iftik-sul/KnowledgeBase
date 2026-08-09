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
  - title-land-registration
---

# Service #19 – Register Heirs Ownership

**Service Category:** Title & Land Registration Services

## 1. Service Overview

The **Register Heirs Ownership** service enables the lawful registration of property ownership in the names of legal heirs following the death of a property owner. The service verifies inheritance documentation, records the new ownership structure in the official property registry, and issues updated ownership documents upon successful approval.

## 2. Purpose

Enable the legal transfer and registration of property ownership to eligible heirs while maintaining accurate ownership records within the official RERAN property registry.

## 3. Description

The service allows eligible heirs or their authorized representative to apply for the registration of inherited property ownership. The applicant submits inheritance documents, identifies all legal heirs, uploads the required supporting documents, and completes the applicable service fee. Following verification and approval, the ownership records are updated and new title documents are issued.

## 4. Who Can Apply

### Eligible Heir

* Registered Individual User  
* Legal Heir recognized under applicable law  
* Court-appointed Administrator or Executor  
* Authorized Representative acting under a valid Power of Attorney

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is registered with RERAN.  
* Legal ownership succession has been established.  
* Required inheritance documents are available.  
* Where there are multiple heirs, all legally required approvals or consents have been obtained.

## 6. Required Information

### Deceased Owner Information

* Full Name  
* National Identification Number (NIN)  
* Date of Death

### Heir Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address  
* Relationship to the Deceased  
* Ownership Share (where applicable)

### Property Information

* Property Registration Number  
* Property Address  
* Property Type  
* Plot Number

### Registration Information

* Succession Type  
* Court Reference (where applicable)  
* Additional Remarks (Optional)

## 7. Required Documents

* Death Certificate  
* Probate or Letter of Administration (where applicable)  
* Court Order (where applicable)  
* Existing Certificate of Title  
* Government-issued Identification of Heirs  
* Proof of Relationship (where applicable)  
* Proof of Payment  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before the application is submitted.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**30–40 minutes.**

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Register Heirs Ownership"  
↓  
Select Registered Property  
↓  
Enter Deceased Owner Information  
↓  
Enter Heir Information  
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
Verify Property Ownership  
↓  
Verify Succession Documents  
↓  
Verify Legal Heirs  
↓  
Review Supporting Documents  
↓  
Approve Heirs Registration  
↓  
Update Property Registry  
↓  
Generate Updated Title Documents  
↓  
Notify Applicant(s)

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

* Heirs Successfully Registered  
* Property Ownership Successfully Updated  
* Joint Ownership Successfully Created (where applicable)  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Updated Electronic Certificate of Title  
* Updated Electronic Title Deed  
* Updated Property Ownership Record  
* Property Map  
* Payment Receipt

## 16. Related Services

* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership  
* Service \#7 – Update Property Ownership Information  
* Service \#17 – Grant Registration

## 17. UI Screens

* Services  
* Register Heirs Ownership  
* Select Property  
* Deceased Owner Information  
* Heir Information  
* Ownership Allocation  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Registration Confirmation

## 18. API Requirements

* Retrieve Property Details  
* Validate Property Ownership  
* Validate Succession Documents  
* Validate Heir Information  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Heirs Registration Application  
* Retrieve Application Status  
* Update Property Registry  
* Generate Updated Title Documents  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Heir  
* Ownership Share  
* Succession Record  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can submit a heirs ownership registration request.  
* System validates that the property exists and is eligible for succession registration.  
* All required heir information is successfully validated.  
* Required succession documents are uploaded successfully.  
* Payment is completed before regulatory review.  
* Application receives a unique application reference number.  
* Approved applications update the official property registry.  
* Ownership shares are correctly recorded where multiple heirs exist.  
* Updated title documents are generated upon approval.  
* All applicants receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a lawful heir, court-appointed administrator, executor, or authorized representative may submit a Register Heirs Ownership application.  
2. The property must already be registered in the official RERAN property registry.  
3. Legal succession must be established before ownership can be registered.  
4. Where multiple heirs exist, ownership shares shall be recorded according to the supporting legal documents or applicable law.  
5. Payment must be completed before the application proceeds for review.  
6. Ownership registration becomes legally effective only after approval by RERAN.  
7. Updated title documents are issued after the official property registry has been updated.  
8. Every Register Heirs Ownership application receives a unique application reference number.  
9. Previous ownership records shall remain permanently preserved as part of the property's ownership history.  
10. All applications, approvals, payments, succession records, registry updates, ownership allocations, document submissions, and notifications must be permanently recorded in the audit trail.
