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
  - title-land-registration
---

# Service #20 – Register Community Land

**Service Category:** Title & Land Registration Services

## 1. Service Overview

The **Register Community Land** service enables eligible communities, community representatives, or legally authorized bodies to register community-owned land with RERAN. The service establishes official recognition of community land ownership, records the land in the property registry, and issues the appropriate registration documents upon successful approval.

## 2. Purpose

Enable the legal registration and recognition of community-owned land while maintaining accurate ownership records within the official RERAN property registry.

## 3. Description

The service allows an authorized community representative to apply for the registration of community-owned land by submitting community information, property details, supporting legal documents, and the applicable service fee. Following verification and approval, the community land is officially registered, and the corresponding ownership documents are issued.

## 4. Who Can Apply

### Authorized Community Representative

* Registered Individual User acting on behalf of the community  
* Community Leader  
* Authorized Community Committee Member  
* Legally Authorized Representative acting under a valid authorization

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Applicant is authorized to represent the community.  
* Community ownership has been legally established.  
* Required supporting documents are available.

## 6. Required Information

### Community Information

* Community Name  
* Community Registration Number (where applicable)  
* Community Address  
* Contact Information

### Representative Information

* Full Name  
* National Identification Number (NIN)  
* Position within the Community  
* Contact Number  
* Email Address

### Property Information

* Property or Land Reference Number (where applicable)  
* Property Address  
* Land Area  
* Plot Number  
* Property Type  
* Geographic Location

### Registration Information

* Community Ownership Type  
* Land Use  
* Additional Remarks (Optional)

## 7. Required Documents

* Community Ownership Documents  
* Community Resolution or Authorization Letter  
* Government-issued Identification of the Representative  
* Survey Plan  
* Site Plan or Property Map  
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

**Approximately 30–40 minutes.**

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Register Community Land"  
↓  
Enter Community Information  
↓  
Enter Property Information  
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
Verify Community Authorization  
↓  
Verify Land Ownership Documents  
↓  
Review Survey Information  
↓  
Approve Community Land Registration  
↓  
Update Property Registry  
↓  
Generate Registration Documents  
↓  
Notify Community Representative

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

* Community Land Successfully Registered  
* Community Ownership Successfully Recorded  
* Property Registry Successfully Updated  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Community Land Registration Certificate  
* Electronic Certificate of Title  
* Electronic Title Deed  
* Updated Property Registry Record  
* Property Map  
* Payment Receipt

## 16. Related Services

* Service \#17 – Grant Registration  
* Service \#18 – Grant Completion  
* Service \#19 – Register Heirs Ownership  
* Service \#21 – Register Partners Division  
* Service \#22 – Register Industrial & Commercial Land Ownership

## 17. UI Screens

* Services  
* Register Community Land  
* Community Information  
* Representative Information  
* Property Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Registration Confirmation

## 18. API Requirements

* Validate Community Information  
* Validate Community Authorization  
* Validate Property Information  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Community Land Registration Application  
* Retrieve Application Status  
* Update Property Registry  
* Generate Registration Documents  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Community  
* Community Representative  
* Property  
* Property Ownership  
* Community Land  
* Survey Record  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Authorized community representative can submit a community land registration request.  
* System validates the applicant's authority to represent the community.  
* Community ownership information is successfully validated.  
* Required property information is validated before submission.  
* Required supporting documents are uploaded successfully.  
* Payment is completed before regulatory review.  
* Application receives a unique application reference number.  
* Approved applications register the community land in the official property registry.  
* Registration documents are generated upon successful approval.  
* Community representative receives completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only an authorized community representative or legally authorized representative may submit a Register Community Land application.  
2. The applicant must provide evidence of authority to act on behalf of the community.  
3. Community ownership must be supported by valid legal or customary documentation recognized by RERAN.  
4. Payment must be completed before the application proceeds for review.  
5. Community land registration becomes legally effective only after approval by RERAN.  
6. The official property registry is updated only after the registration has been approved.  
7. Registration documents are issued upon successful completion of the registration process.  
8. Every Register Community Land application receives a unique application reference number.  
9. The registered community land forms part of the permanent property ownership records maintained by RERAN.  
10. All applications, approvals, payments, registry updates, survey records, document submissions, and notifications must be permanently recorded in the audit trail.
