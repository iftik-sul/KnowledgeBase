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

# Service #31 – Request Detailed Real Estate Statement

**Service Category:** Property Information & Certificate Services

## 1. Service Overview

The **Request Detailed Real Estate Statement** service enables users to obtain an official statement containing comprehensive information about a registered property. The statement provides authenticated property records maintained by RERAN, including ownership information, registration history, encumbrances, and other regulatory information associated with the property.

## 2. Purpose

Provide an official and comprehensive property statement that can be used for due diligence, legal verification, financial transactions, regulatory compliance, and property management.

## 3. Description

The service allows an eligible applicant to request a Detailed Real Estate Statement for a registered property by submitting the property details and paying the applicable service fee. Following verification, RERAN generates an official statement containing the property's registered information and makes it available electronically.

## 4. Who Can Apply

### Eligible Applicants

* Registered Property Owner  
* Joint Property Owner  
* Authorized Representative acting under a valid Power of Attorney  
* Individual User with legal authority or a legitimate interest, where permitted by RERAN regulations

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is registered with RERAN.  
* Applicant is authorized to request the statement.  
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
* Plot Number (where applicable)  
* Property Type

### Request Information

* Purpose of Request (Optional)  
* Additional Remarks (Optional)

## 7. Required Documents

* Government-issued Identification  
* Proof of Property Ownership (where applicable)  
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

**Approximately 10–15 minutes.**

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Request Detailed Real Estate Statement"  
↓  
Search & Select Registered Property  
↓  
Review Property Details  
↓  
Review Service Fee  
↓  
Complete Payment  
↓  
Submit Request

↓

RERAN

Validate Property Information  
↓  
Verify Applicant Authorization  
↓  
Generate Detailed Real Estate Statement  
↓  
Apply Digital Authentication  
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
Processing  
↓  
Completed

### Additional Statuses

* Information Requested  
* Payment Failed  
* Cancelled  
* Request Rejected

## 14. Possible Outcomes

* Detailed Real Estate Statement Successfully Generated  
* Property Not Found  
* Unauthorized Request  
* Additional Information Requested  
* Payment Failed  
* Request Cancelled

## 15. Output

Upon successful completion, the system generates:

* Official Detailed Real Estate Statement (PDF)  
* Property Ownership Information  
* Property Registration Information  
* Ownership History  
* Registered Encumbrances (where applicable)  
* Property Transaction History (where applicable)  
* Property Status  
* Property Map  
* Digital Authentication Information  
* Payment Receipt

## 16. Related Services

* Service \#3 – Verify Property  
* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership  
* Service \#7 – Update Property Ownership Information  
* Service \#32 – Request To Whom It May Concern Certificate  
* Service \#33 – Request Property Survey  
* Service \#34 – Request Property Valuation  
* Service \#35 – Request Full / Partial Indemnity

## 17. UI Screens

* Services  
* Request Detailed Real Estate Statement  
* Property Search  
* Property Details  
* Payment  
* Payment Successful  
* Request Submitted  
* Statement Processing  
* Statement Details  
* Download Statement

## 18. API Requirements

* Search Registered Property  
* Retrieve Property Details  
* Validate Applicant Authorization  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Statement Request  
* Generate Detailed Real Estate Statement  
* Apply Digital Authentication  
* Retrieve Request Status  
* Download Statement  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Property Registration  
* Property Transaction  
* Encumbrance  
* Statement Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can search for an eligible property.  
* System validates the applicant's authorization before processing the request.  
* Payment is completed before the statement is generated.  
* The system generates an official Detailed Real Estate Statement.  
* The generated statement contains the latest approved property information.  
* The statement includes digital authentication information.  
* Applicant can download the statement in PDF format.  
* Applicant receives a notification when the statement is ready.  
* Every request receives a unique request reference number.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only eligible applicants with appropriate authorization may request a Detailed Real Estate Statement.  
2. The property must exist in the official RERAN property registry.  
3. Payment must be completed before the statement is generated.  
4. The statement reflects the property's official registry information as of the generation date.  
5. The statement is issued in electronic format with digital authentication.  
6. Every statement request receives a unique request reference number.  
7. Previously issued statements remain available as part of the request history, subject to applicable retention policies.  
8. The issuance of a Detailed Real Estate Statement does not modify any property registration or ownership information.  
9. Downloaded statements are considered official only when digitally authenticated by RERAN.  
10. All requests, payments, statement generations, downloads, and notifications must be permanently recorded in the audit trail.
