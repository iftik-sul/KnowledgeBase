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

# Service #34 – Request Property Valuation

**Service Category:** Property Information & Certificate Services

## 1. Service Overview

The **Request Property Valuation** service enables eligible applicants to obtain an official valuation of a registered property. The service provides an independent assessment of the property's market value based on approved valuation standards and methodologies. The valuation may be used for property transactions, financing, taxation, insurance, investment, legal proceedings, regulatory compliance, and other official purposes.

## 2. Purpose

Provide an official property valuation that reflects the assessed market value of a property based on approved valuation standards and regulatory requirements.

## 3. Description

The service allows an eligible applicant to request a property valuation by submitting the required property information, supporting documents, and applicable service fee. Following verification, RERAN conducts the valuation, prepares an official Property Valuation Report, and makes the completed report available electronically.

## 4. Who Can Apply

### Eligible Applicants

* Registered Property Owner  
* Joint Property Owner  
* Authorized Representative acting under a valid Power of Attorney  
* Financial Institution (where legally authorized)  
* Individual User with legal authority or a legitimate interest, where permitted by RERAN regulations

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property information is available.  
* Applicant is authorized to request the valuation.  
* Applicable service fee is paid.

## 6. Required Information

### Applicant Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Property Information

* Property Registration Number  
* Property Address  
* Plot Number  
* Property Type  
* Property Usage  
* Land Area  
* Building Area (where applicable)

### Valuation Information

* Purpose of Valuation  
* Preferred Inspection Date (Optional)  
* Additional Remarks (Optional)

## 7. Required Documents

* Government-issued Identification  
* Proof of Property Ownership (where applicable)  
* Existing Survey Plan (if available)  
* Site Plan or Property Map (if available)  
* Previous Valuation Report (Optional)  
* Authorization Letter or Power of Attorney (where applicable)  
* Proof of Payment  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before the valuation request is processed.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**Approximately 3–10 working days**, depending on the property type, complexity of the valuation, and whether a physical inspection is required.

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Request Property Valuation"  
↓  
Search & Select Property  
↓  
Enter Valuation Information  
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
Schedule Property Inspection (if required)  
↓  
Conduct Property Valuation  
↓  
Prepare Valuation Report  
↓  
Approve Valuation Report  
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
Inspection Scheduled  
↓  
Valuation in Progress  
↓  
Report Preparation  
↓  
Approved  
↓  
Completed

### Additional Statuses

* Information Requested  
* Inspection Rescheduled  
* Returned  
* Rejected  
* Cancelled

## 14. Possible Outcomes

* Property Successfully Valued  
* Property Valuation Report Issued  
* Property Inspection Required  
* Additional Information Requested  
* Property Not Found  
* Payment Failed  
* Request Cancelled

## 15. Output

Upon successful completion, the system generates:

* Official Property Valuation Report  
* Assessed Market Value  
* Valuation Summary  
* Property Information Summary  
* Payment Receipt

## 16. Related Services

* Service \#31 – Request Detailed Real Estate Statement  
* Service \#32 – Request To Whom It May Concern Certificate  
* Service \#33 – Request Property Survey  
* Service \#35 – Request Full / Partial Indemnity  
* Service \#4 – Register Property Ownership

## 17. UI Screens

* Services  
* Request Property Valuation  
* Property Search  
* Valuation Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Request Submitted  
* Valuation Status  
* Valuation Report  
* Download Valuation Report

## 18. API Requirements

* Search Registered Property  
* Retrieve Property Details  
* Validate Applicant Authorization  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Property Valuation Request  
* Schedule Property Inspection  
* Update Valuation Status  
* Generate Property Valuation Report  
* Retrieve Request Status  
* Download Valuation Report  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Property Valuation  
* Property Inspection  
* Valuation Report  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can submit a property valuation request.  
* System validates the applicant's authorization before processing.  
* Required property information is validated successfully.  
* Required supporting documents are uploaded successfully.  
* Payment is completed before processing begins.  
* Property inspection is scheduled where required.  
* Valuation status is visible throughout the process.  
* Official Property Valuation Report is generated after approval.  
* Applicant can download the completed valuation report.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only eligible applicants with appropriate authorization may request a property valuation.  
2. Payment must be completed before valuation activities commence.  
3. A physical property inspection may be required depending on the property type, valuation purpose, or regulatory requirements.  
4. Inspection appointments may be rescheduled due to operational, weather, or access constraints.  
5. The valuation report becomes official only after approval by RERAN.  
6. Every Property Valuation request receives a unique request reference number.  
7. The valuation reflects the property's assessed market value as of the valuation date and should not be interpreted as a guaranteed sale price.  
8. Completed valuation reports become part of the property's historical records.  
9. Property valuation does not modify ownership, title, or other legal rights associated with the property.  
10. All requests, inspections, valuation activities, approvals, reports, payments, downloads, and notifications must be permanently recorded in the audit trail.
