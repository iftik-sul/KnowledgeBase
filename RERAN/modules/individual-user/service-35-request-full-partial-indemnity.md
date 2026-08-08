---
project: RERAN
module: individual-user
type: service-flow
status: current
updated: 2026-08-09
derived_from:
  - "RERAN/modules/individual-user/RERAN_ individual user_service_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - individual-user
  - service-flow
  - property-info-certificates
---

# Service #35 – Request Full / Partial Indemnity

**Service Category:** Property Information & Certificate Services

## 1. Service Overview

The **Request Full / Partial Indemnity** service enables eligible applicants to request an official indemnity certificate or indemnity approval relating to a registered property. The service is used where a property owner or authorized party requires RERAN to recognize, release, or certify a full or partial indemnity associated with a property in accordance with applicable regulations.

## 2. Purpose

Provide an official process for requesting, reviewing, approving, and issuing Full or Partial Indemnity documentation while maintaining accurate records within the official RERAN property registry.

## 3. Description

The service allows an eligible applicant to request either a Full Indemnity or Partial Indemnity by providing the required property information, indemnity details, supporting documents, and applicable service fee. Following regulatory review and approval, RERAN issues an official indemnity certificate or approval document and updates the property's official records where applicable.

## 4. Who Can Apply

### Eligible Applicants

* Registered Property Owner  
* Joint Property Owner  
* Authorized Representative acting under a valid Power of Attorney  
* Individual or Organization with a legally recognized interest in the property, where permitted by RERAN regulations

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is registered with RERAN.  
* Applicant is authorized to submit the indemnity request.  
* Required supporting documents are available.  
* Applicable service fee is paid.

## 6. Required Information

### Applicant Information

* Full Name / Organization Name  
* National Identification Number (NIN) or Registration Number  
* Contact Number  
* Email Address

### Property Information

* Property Registration Number  
* Property Address  
* Plot Number  
* Property Type

### Indemnity Information

* Indemnity Type (Full / Partial)  
* Purpose of Request  
* Description of the Requested Indemnity  
* Supporting Reference Number (where applicable)  
* Additional Remarks (Optional)

## 7. Required Documents

* Government-issued Identification  
* Proof of Property Ownership  
* Existing Certificate of Title (where applicable)  
* Supporting Legal Documents  
* Court Order (where applicable)  
* Authorization Letter or Power of Attorney (where applicable)  
* Proof of Payment  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before the request is processed.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**Approximately 10–20 minutes.**

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Request Full / Partial Indemnity"  
↓  
Search & Select Registered Property  
↓  
Enter Indemnity Information  
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
Verify Supporting Documents  
↓  
Assess Indemnity Request  
↓  
Approve Indemnity  
↓  
Update Property Records (where applicable)  
↓  
Generate Indemnity Certificate  
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
* Payment Failed

## 14. Possible Outcomes

* Full Indemnity Approved  
* Partial Indemnity Approved  
* Indemnity Certificate Issued  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Official Full or Partial Indemnity Certificate  
* Indemnity Approval Letter  
* Updated Property Registry Record (where applicable)  
* Payment Receipt

## 16. Related Services

* Service \#31 – Request Detailed Real Estate Statement  
* Service \#32 – Request To Whom It May Concern Certificate  
* Service \#33 – Request Property Survey  
* Service \#34 – Request Property Valuation  
* Service \#4 – Register Property Ownership

## 17. UI Screens

* Services  
* Request Full / Partial Indemnity  
* Property Search  
* Indemnity Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Request Submitted  
* Application Details  
* Indemnity Certificate  
* Download Certificate

## 18. API Requirements

* Search Registered Property  
* Retrieve Property Details  
* Validate Applicant Authorization  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Indemnity Request  
* Retrieve Application Status  
* Update Property Records  
* Generate Indemnity Certificate  
* Download Certificate  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Indemnity Request  
* Indemnity Certificate  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can submit a Full or Partial Indemnity request.  
* System validates the applicant's authorization before processing.  
* Required property information is successfully validated.  
* Required supporting documents are uploaded successfully.  
* Payment is completed before regulatory review.  
* Application receives a unique application reference number.  
* Approved requests generate an official indemnity certificate.  
* Property records are updated where applicable.  
* Applicant can download the issued certificate.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only eligible applicants with appropriate authorization may submit a Full or Partial Indemnity request.  
2. The property must exist in the official RERAN property registry.  
3. Payment must be completed before the request proceeds for review.  
4. RERAN may request additional documentation before approving an indemnity request.  
5. An indemnity certificate becomes official only after approval by RERAN.  
6. Every Request Full / Partial Indemnity application receives a unique application reference number.  
7. Where applicable, the approved indemnity shall be recorded in the property's official registry.  
8. The issuance of an indemnity certificate does not transfer ownership or modify title rights unless explicitly authorized under applicable regulations.  
9. Issued indemnity certificates remain available in the applicant's document history, subject to applicable retention policies.  
10. All applications, approvals, payments, document submissions, registry updates, certificate generations, downloads, and notifications must be permanently recorded in the audit trail.
