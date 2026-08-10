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
  - property-info-certificates
---

# Service #33 – Request Property Survey

**Service Category:** Property Information & Certificate Services

## 1. Service Overview

The **Request Property Survey** service enables eligible applicants to request an official property survey for a registered property. The service facilitates the verification, measurement, mapping, and confirmation of property boundaries, dimensions, and location. Upon completion, RERAN issues an official Property Survey Report and updated survey documents where applicable.

## 2. Purpose

Provide an official property survey to establish or verify the physical characteristics, boundaries, and location of a property for legal, regulatory, financial, or development purposes.

## 3. Description

The service allows an eligible applicant to request a property survey by submitting the required property information, supporting documents, and applicable service fee. Following verification, RERAN schedules the survey where necessary, conducts the survey, prepares the official survey report, and makes the completed documents available electronically.

## 4. Who Can Apply

### Eligible Applicants

* Registered Property Owner  
* Joint Property Owner  
* Authorized Representative acting under a valid Power of Attorney  
* Individual User with legal authority or a legitimate interest, where permitted by RERAN regulations

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property information is available.  
* Applicant is authorized to request the survey.  
* Applicable service fee is paid.

## 6. Required Information

### Applicant Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Property Information

* Property Registration Number (if available)  
* Property Address  
* Plot Number  
* Property Type  
* Land Area (if known)

### Survey Information

* Purpose of Survey  
* Preferred Survey Date (Optional)  
* Additional Remarks (Optional)

## 7. Required Documents

* Government-issued Identification  
* Proof of Property Ownership (where applicable)  
* Existing Survey Plan (if available)  
* Site Plan or Property Map (if available)  
* Authorization Letter or Power of Attorney (where applicable)  
* Proof of Payment  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before the survey request is processed.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**Approximately 3–10 working days**, depending on property location, survey complexity, and whether an on-site inspection is required.

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Request Property Survey"  
↓  
Search & Select Property  
↓  
Enter Survey Information  
↓  
Upload Required Documents  
↓  
Review Application  
↓  
Complete Payment  
↓  
Submit Request

↓

RERAN

Review Application  
↓  
Verify Property Information  
↓  
Schedule Survey (if required)  
↓  
Conduct Property Survey  
↓  
Prepare Survey Report  
↓  
Approve Survey Report  
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
Survey Scheduled  
↓  
Survey in Progress  
↓  
Report Preparation  
↓  
Approved  
↓  
Completed

### Additional Statuses

* Information Requested  
* Survey Rescheduled  
* Returned  
* Rejected  
* Cancelled

## 14. Possible Outcomes

* Property Survey Successfully Completed  
* Property Survey Report Issued  
* Survey Rescheduled  
* Additional Information Requested  
* Property Not Found  
* Payment Failed  
* Request Cancelled

## 15. Output

Upon successful completion, the system generates:

* Official Property Survey Report  
* Survey Plan  
* Property Boundary Information  
* Property Coordinates  
* Updated Property Map (where applicable)  
* Payment Receipt

## 16. Related Services

* Service \#31 – Request Detailed Real Estate Statement  
* Service \#32 – Request To Whom It May Concern Certificate  
* Service \#34 – Request Property Valuation  
* Service \#35 – Request Full / Partial Indemnity  
* Service \#4 – Register Property Ownership

## 17. UI Screens

* Services  
* Request Property Survey  
* Property Search  
* Survey Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Request Submitted  
* Survey Status  
* Survey Report  
* Download Survey Report

## 18. API Requirements

* Search Registered Property  
* Retrieve Property Details  
* Validate Applicant Authorization  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Survey Request  
* Schedule Survey  
* Update Survey Status  
* Generate Survey Report  
* Retrieve Request Status  
* Download Survey Report  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Property Survey  
* Survey Schedule  
* Survey Report  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can submit a property survey request.  
* System validates the applicant's authorization before processing.  
* Required property information is validated successfully.  
* Required supporting documents are uploaded successfully.  
* Payment is completed before processing begins.  
* Survey is scheduled where required.  
* Survey status is visible throughout the process.  
* Official survey report is generated after approval.  
* Applicant can download the completed survey report.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only eligible applicants with appropriate authorization may request a property survey.  
2. Payment must be completed before survey activities commence.  
3. An on-site survey may be required depending on the property type, existing records, or regulatory requirements.  
4. Survey appointments may be rescheduled due to operational, weather, or access constraints.  
5. The survey report becomes official only after approval by RERAN.  
6. Every Property Survey request receives a unique request reference number.  
7. Completed survey reports and survey plans become part of the property's official record.  
8. A property survey does not change ownership or legal rights unless processed through the appropriate registration service.  
9. Survey reports are issued electronically with digital authentication.  
10. All requests, survey schedules, field activities, approvals, reports, payments, downloads, and notifications must be permanently recorded in the audit trail.
