---
project: RERAN
module: individual-user
type: service-flow
status: current
source_type: sourced
updated: 2026-08-15
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

# Service #17 – Grant Registration

**Service Category:** Title & Land Registration Services

## 1. Service Overview

The **Grant Registration** service enables eligible applicants to register a government land grant or allocation with RERAN. The service records the grant in the official property registry, establishes the legal ownership record, and issues the corresponding registration documents upon successful approval.

## 2. Purpose

Enable the legal registration of granted land or property rights while establishing an official ownership record within the RERAN property registry.

## 3. Description

The service allows an eligible applicant to register a government-issued land grant or allocation by submitting the required property information and supporting documents. Following verification and approval, the grant is recorded in the official registry and the corresponding title documents are generated.

## 4. Who Can Apply

### Grant Recipient

* Registered Individual User  
* Registered Legal Entity (where applicable)  
* Authorized Representative acting under a valid Power of Attorney

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* A valid government grant or land allocation has been issued.  
* Applicant is the lawful grant recipient or an authorized representative.  
* Required supporting documents are available.

## 6. Required Information

### Applicant Information

* Full Name / Organization Name  
* National Identification Number (NIN) or Registration Number  
* Contact Number  
* Email Address

### Grant Information

* Grant Reference Number  
* Grant Date  
* Issuing Authority  
* Grant Type

### Property Information

* Plot Number  
* Property Address  
* Property Type  
* Land Area  
* Survey Reference (where applicable)

### Additional Information

* Intended Land Use  
* Additional Remarks (Optional)

## 7. Required Documents

* Government Grant Letter  
* Allocation Letter (where applicable)  
* Government-issued Identification  
* Survey Plan  
* Site Plan or Property Map (where applicable)  
* Power of Attorney (where applicable)  
* Other supporting documents required by RERAN

## 8. Service Fee

**No fee.** Source row 98 documents no payment step anywhere in its workflow — submit, enter data, audit and approve, notify. This is a genuine no-fee case, not an omission: rows 98 and 99 (Grant Completion) sit directly beside fee-bearing siblings #19–#22 in the same Title & Land Registration cluster, which is the same contrast-with-neighbours evidence Group C used to confirm its own Service #2's fee-free status. See `payments.md` Category 4.

## 9. Payment Required

**No**

*(Corrected 2026-08-15 — this file previously stated payment was required before submission. Source row 98 has no payment step. See `payments.md` Category 4.)*

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**Approximately 25–30 minutes.**

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Grant Registration"  
↓  
Enter Grant Information  
↓  
Enter Property Information  
↓  
Upload Required Documents  
↓  
Review Application  
↓  
Submit Application

↓

RERAN

Review Application  
↓  
Verify Grant Documents  
↓  
Verify Property Information  
↓  
Review Supporting Documents  
↓  
Approve Grant Registration  
↓  
Register Property  
↓  
Generate Registration Documents  
↓  
Notify Applicant

## 13. Application Status Flow

Draft  
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

* Grant Successfully Registered  
* Property Successfully Registered  
* Ownership Successfully Recorded  
* Additional Information Requested  
* Application Returned  
* Application Rejected

## 15. Output

Upon successful completion, the system generates:

* Electronic Certificate of Title  
* Electronic Title Deed  
* Property Registration Certificate  
* Property Map

## 16. Related Services

* Service \#18 – Grant Completion  
* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership  
* Service \#7 – Update Property Ownership Information

## 17. UI Screens

* Services  
* Grant Registration  
* Grant Information  
* Property Information  
* Document Upload  
* Application Review  
* Application Submitted  
* Application Details  
* Registration Confirmation

## 18. API Requirements

* Validate Applicant  
* Validate Grant Information  
* Validate Property Information  
* Upload Documents  
* Submit Grant Registration Application  
* Retrieve Application Status  
* Register Property  
* Generate Registration Documents  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Land Grant  
* Property Registration  
* Application  
* Service Request  
* Document  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can submit a grant registration request.  
* System validates the grant information before submission.  
* Required property information is successfully validated.  
* Required supporting documents are uploaded successfully.  
* No payment step applies to this service.  
* Application receives a unique application reference number.  
* Approved applications register the property in the official property registry.  
* Registration documents are generated upon successful approval.  
* Applicant receives completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the lawful grant recipient or an authorized representative may submit a grant registration application.  
2. The grant must be issued by a competent authority and be valid at the time of application.  
3. **No fee applies to this service.** *(Corrected 2026-08-15 — see Section 8/9.)*  
4. All mandatory supporting documents must be submitted before the application can be processed.  
5. Grant registration becomes legally effective only after approval by RERAN.  
6. The property is recorded in the official property registry only after the application has been approved.  
7. An Electronic Certificate of Title and related registration documents are issued upon successful registration.  
8. Every Grant Registration application receives a unique application reference number.  
9. The registered grant forms part of the permanent ownership history of the property.  
10. All applications, approvals, registry updates, document submissions, and notifications must be permanently recorded in the audit trail.
