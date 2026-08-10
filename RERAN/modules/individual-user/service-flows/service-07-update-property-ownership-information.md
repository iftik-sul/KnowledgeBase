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

# Service #7 – Update Property Ownership Information

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Update Property Ownership Information** service enables registered property owners to update ownership-related information maintained within the RERAN property registry. The service supports amendments to owner information as well as property information while preserving the legal ownership of the property.

## 2. Purpose

Enable property owners to maintain accurate ownership and property records by submitting amendments to registered owner information or registered property information.

## 3. Description

The service allows a registered property owner to submit a request to amend information recorded in the official property registry. Depending on the requested amendment, the applicant may update personal information, entity information, or property details by submitting the required supporting documents. Following review and approval, the official registry is updated and, where applicable, revised title documents are issued.

## 4. Who Can Apply

* Registered Property Owner  
* Joint Property Owner  
* Authorized Representative acting under a valid Power of Attorney  
* Court-appointed Representative (where legally applicable)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is registered with RERAN.  
* Applicant has legal authority over the property.  
* Supporting documents are available for the requested amendment.

## 6. Required Information

### Amendment Type

* Amendment of Owner / Entity Information  
* Amendment of Property Information

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Current Information

* Existing Registered Information

### Updated Information

* New Owner Details (where applicable)  
* New Entity Details (where applicable)  
* Updated Property Details (where applicable)

### Additional Information

* Reason for Amendment  
* Effective Date  
* Additional Remarks (Optional)

## 7. Required Documents

Depending on the amendment type:

* Government-issued Identification  
* Existing Certificate of Title  
* Supporting Legal Documents  
* Proof of Ownership  
* Court Order (where applicable)  
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

* **Owner / Entity Information Amendment:** **20 minutes**  
* **Property Information Amendment:** **Maximum 3 business hours**

## 12. Processing Workflow

Option 1 – Owner / Entity Information Amendment

Visit Real Estate Services Trustee Center  
↓  
Submit Required Documents  
↓  
Officer Reviews Documents  
↓  
Owner / Entity Information Updated  
↓  
Application Approved  
↓  
Registry Updated

──────────────────────────

Option 2 – Property Information Amendment

Login  
↓  
Open Services  
↓  
Select "Update Property Ownership Information"  
↓  
Select Registered Property  
↓  
Select Amendment Type  
↓  
Update Property Information  
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
Receive Updated Electronic Certificate of Title

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

* Information Successfully Updated  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Depending on the amendment type:

* Updated Registry Information  
* Updated Electronic Certificate of Title (where applicable)  
* Updated Electronic Title Deed (where applicable)

## 16. Related Services

* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership  
* Service \#6 – Register Property Sale  
* Service \#3 – Verify Property

## 17. UI Screens

* Services  
* Update Property Ownership Information  
* Select Property  
* Select Amendment Type  
* Update Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Updated Certificate of Title

## 18. API Requirements

* Retrieve User Properties  
* Retrieve Property Details  
* Retrieve Registered Owner Information  
* Validate Ownership  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Amendment Application  
* Retrieve Application Status  
* Update Registry Information  
* Generate Updated Title Documents  
* Download Updated Documents

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Property Amendment  
* Owner Information  
* Property Information  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Audit Log  
* Notification

## 20. Acceptance Criteria

* User can submit either an owner information amendment or a property information amendment.  
* System validates ownership before submission.  
* Required information is successfully validated.  
* Supporting documents are uploaded successfully.  
* Payment is completed before submission.  
* Application receives a unique reference number.  
* User can monitor the application status.  
* Approved applications update the official property registry.  
* Updated title documents are generated where applicable.  
* Payment receipt is generated after successful payment.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the registered property owner or an authorized representative may submit an amendment request.  
2. The property must already be registered with RERAN.  
3. Payment must be completed before the application is submitted.  
4. This service updates registry information only and does **not** transfer legal ownership.  
5. Ownership transfers must be completed through the **Transfer Property Ownership** service.  
6. All mandatory supporting documents must be submitted before the application proceeds for review.  
7. Approved amendments update the official property registry.  
8. Updated title documents are issued only when the approved amendment affects title information.  
9. Every amendment request receives a unique application reference number.  
10. All submissions, approvals, registry updates, payments, and document uploads must be permanently recorded in the audit trail.
