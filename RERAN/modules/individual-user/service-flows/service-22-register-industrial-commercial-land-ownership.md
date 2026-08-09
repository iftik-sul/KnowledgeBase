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

# Service #22 – Register Industrial & Commercial Land Ownership

**Service Category:** Title & Land Registration Services

## 1. Service Overview

The **Register Industrial & Commercial Land Ownership** service enables eligible individuals or organizations to register ownership of industrial or commercial land with RERAN. The service records the ownership in the official property registry and issues the corresponding title documents upon successful approval.

## 2. Purpose

Enable the legal registration of industrial and commercial land ownership while maintaining accurate ownership records within the official RERAN property registry.

## 3. Description

The service allows eligible applicants to register ownership of industrial or commercial land by submitting ownership information, property details, supporting documents, and the applicable service fee. Following verification and approval, the property ownership is officially recorded in the registry and the corresponding registration documents are issued.

## 4. Who Can Apply

### Property Owner

* Registered Individual User  
* Registered Business Entity  
* Authorized Representative acting under a valid Power of Attorney

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* The industrial or commercial land is eligible for registration.  
* Applicant has legal ownership or allocation rights.  
* Required supporting documents are available.

## 6. Required Information

### Applicant Information

* Full Name / Organization Name  
* National Identification Number (NIN) or Business Registration Number  
* Contact Number  
* Email Address

### Property Information

* Property Registration Number (if available)  
* Plot Number  
* Property Address  
* Property Type (Industrial / Commercial)  
* Land Area  
* Survey Reference Number

### Ownership Information

* Acquisition Method  
* Ownership Date  
* Intended Land Use  
* Additional Remarks (Optional)

## 7. Required Documents

* Government Allocation or Ownership Document  
* Existing Certificate of Title (where applicable)  
* Government-issued Identification  
* Business Registration Certificate (for organizations)  
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

**Approximately 30 minutes.**

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Register Industrial & Commercial Land Ownership"  
↓  
Enter Applicant Information  
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
Verify Ownership Documents  
↓  
Verify Property Information  
↓  
Review Supporting Documents  
↓  
Approve Registration  
↓  
Update Property Registry  
↓  
Generate Registration Documents  
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

* Industrial or Commercial Land Successfully Registered  
* Ownership Successfully Recorded  
* Property Registry Successfully Updated  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Electronic Certificate of Title  
* Electronic Title Deed  
* Industrial / Commercial Land Registration Certificate  
* Updated Property Registry Record  
* Property Map  
* Payment Receipt

## 16. Related Services

* Service \#17 – Grant Registration  
* Service \#18 – Grant Completion  
* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership  
* Service \#7 – Update Property Ownership Information

## 17. UI Screens

* Services  
* Register Industrial & Commercial Land Ownership  
* Applicant Information  
* Property Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Registration Confirmation

## 18. API Requirements

* Validate Applicant  
* Validate Ownership Documents  
* Validate Property Information  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Industrial & Commercial Land Registration Application  
* Retrieve Application Status  
* Update Property Registry  
* Generate Registration Documents  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Organization  
* Property  
* Property Ownership  
* Industrial Property  
* Commercial Property  
* Land Registration  
* Survey Record  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can submit an industrial or commercial land ownership registration request.  
* System validates the applicant's ownership rights.  
* Property information is validated before submission.  
* Required supporting documents are uploaded successfully.  
* Payment is completed before regulatory review.  
* Application receives a unique application reference number.  
* Approved applications update the official property registry.  
* Registration documents are generated upon successful approval.  
* Applicant receives completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the lawful owner of the industrial or commercial land, or an authorized representative, may submit a registration application.  
2. The land must be eligible for registration under applicable laws and RERAN regulations.  
3. Industrial and commercial land registrations require valid ownership or allocation documents.  
4. Payment must be completed before the application proceeds for review.  
5. Registration becomes legally effective only after approval by RERAN.  
6. The official property registry is updated only after the application has been approved.  
7. Electronic title and registration documents are issued upon successful registration.  
8. Every Register Industrial & Commercial Land Ownership application receives a unique application reference number.  
9. The registered ownership becomes part of the permanent property ownership history maintained by RERAN.  
10. All applications, approvals, payments, registry updates, document submissions, ownership records, and notifications must be permanently recorded in the audit trail.
