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

# Service #21 – Register Partners Division

**Service Category:** Title & Land Registration Services

## 1. Service Overview

The **Register Partners Division** service enables co-owners or legal partners of a jointly owned property to formally divide their ownership interests and register the resulting ownership structure with RERAN. Upon successful approval, the official property registry is updated and revised ownership documents are issued.

## 2. Purpose

Enable joint property owners to legally divide jointly owned property while maintaining accurate ownership records within the official RERAN property registry.

## 3. Description

The service allows eligible co-owners or their authorized representatives to submit a property division application. The applicant provides the ownership details, proposed division information, supporting legal documents, and completes the applicable service fee. Following verification and approval, the property registry is updated to reflect the approved ownership division and revised registration documents are issued.

## 4. Who Can Apply

### Property Owners

* Registered Joint Property Owners  
* Legal Partners in Property Ownership  
* Authorized Representative acting under a valid Power of Attorney

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is jointly owned and registered with RERAN.  
* All owners are legally identified.  
* Required supporting documents are available.  
* Required approvals or consents have been obtained from all parties where applicable.

## 6. Required Information

### Property Information

* Property Registration Number  
* Property Address  
* Property Type  
* Plot Number

### Existing Ownership Information

* Existing Owners  
* Current Ownership Shares

### Division Information

* Proposed Ownership Division  
* New Ownership Shares  
* Division Agreement Date  
* Division Reason  
* Additional Remarks (Optional)

## 7. Required Documents

* Existing Certificate of Title  
* Property Division Agreement  
* Government-issued Identification of All Owners  
* Proof of Property Ownership  
* Survey Plan (where applicable)  
* Court Order (where applicable)  
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

**Approximately 30 minutes.**

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Register Partners Division"  
↓  
Select Jointly Owned Property  
↓  
Review Existing Ownership Details  
↓  
Enter Proposed Division Information  
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
Verify Division Agreement  
↓  
Review Supporting Documents  
↓  
Approve Partners Division  
↓  
Update Property Registry  
↓  
Generate Updated Registration Documents  
↓  
Notify Property Owners

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

* Partners Division Successfully Registered  
* Ownership Shares Successfully Updated  
* Property Registry Successfully Updated  
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
* Service \#19 – Register Heirs Ownership  
* Service \#20 – Register Community Land  
* Service \#22 – Register Industrial & Commercial Land Ownership

## 17. UI Screens

* Services  
* Register Partners Division  
* Select Property  
* Existing Ownership Details  
* Division Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Registration Confirmation

## 18. API Requirements

* Retrieve Jointly Owned Properties  
* Retrieve Property Details  
* Retrieve Ownership Information  
* Validate Property Ownership  
* Validate Division Agreement  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Partners Division Application  
* Retrieve Application Status  
* Update Property Registry  
* Generate Updated Registration Documents  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Joint Ownership  
* Ownership Share  
* Partners Division  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can submit a partners division registration request.  
* System validates that the property is jointly owned.  
* Existing ownership information is successfully retrieved and validated.  
* Proposed ownership shares are validated before submission.  
* Required supporting documents are uploaded successfully.  
* Payment is completed before regulatory review.  
* Application receives a unique application reference number.  
* Approved applications update the official property registry.  
* Updated ownership documents are generated after approval.  
* All property owners receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only registered joint property owners or their authorized representatives may submit a Register Partners Division application.  
2. The property must be jointly owned and registered in the official RERAN property registry.  
3. The proposed ownership division must comply with applicable laws and regulations.  
4. Where required, all joint owners must consent to the proposed division before approval.  
5. Payment must be completed before the application proceeds for review.  
6. The ownership division becomes legally effective only after approval by RERAN.  
7. The official property registry is updated only after the application has been approved.  
8. Updated title documents are issued reflecting the revised ownership structure.  
9. Every Register Partners Division application receives a unique application reference number.  
10. All applications, approvals, payments, ownership changes, registry updates, document submissions, and notifications must be permanently recorded in the audit trail.
