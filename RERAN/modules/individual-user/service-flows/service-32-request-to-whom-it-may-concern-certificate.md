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

# Service #32 – Request To Whom It May Concern Certificate

**Service Category:** Property Information & Certificate Services

## 1. Service Overview

The **Request To Whom It May Concern Certificate** service enables eligible applicants to obtain an official certificate issued by RERAN confirming specific property-related information maintained in the official property registry. The certificate serves as an authenticated document that can be presented to government agencies, financial institutions, legal entities, and other authorized organizations.

## 2. Purpose

Provide an official certificate verifying registered property information for use in legal, financial, administrative, and regulatory processes.

## 3. Description

The service allows an eligible applicant to request a **To Whom It May Concern Certificate** for a registered property by submitting the required property information and paying the applicable service fee. Following verification, RERAN generates an official certificate containing the verified property information and makes it available electronically.

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
* Applicant is authorized to request the certificate.  
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

### Certificate Information

* Purpose of Request  
* Recipient Organization (Optional)  
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

Payment must be completed before the certificate is generated.

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
Select "Request To Whom It May Concern Certificate"  
↓  
Search & Select Registered Property  
↓  
Review Property Information  
↓  
Enter Certificate Purpose  
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
Generate Certificate  
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

* Certificate Successfully Generated  
* Property Not Found  
* Unauthorized Request  
* Additional Information Requested  
* Payment Failed  
* Request Cancelled

## 15. Output

Upon successful completion, the system generates:

* Official **To Whom It May Concern Certificate**  
* Verified Property Information  
* Property Ownership Information  
* Certificate Reference Number  
* Digital Authentication Information  
* Payment Receipt

## 16. Related Services

* Service \#3 – Verify Property  
* Service \#31 – Request Detailed Real Estate Statement  
* Service \#33 – Request Property Survey  
* Service \#34 – Request Property Valuation  
* Service \#35 – Request Full / Partial Indemnity

## 17. UI Screens

* Services  
* Request To Whom It May Concern Certificate  
* Property Search  
* Property Details  
* Certificate Information  
* Payment  
* Payment Successful  
* Request Submitted  
* Certificate Processing  
* Certificate Details  
* Download Certificate

## 18. API Requirements

* Search Registered Property  
* Retrieve Property Details  
* Validate Applicant Authorization  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Certificate Request  
* Generate Certificate  
* Apply Digital Authentication  
* Retrieve Request Status  
* Download Certificate  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Property Registration  
* Certificate Request  
* Certificate  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can search for an eligible property.  
* System validates the applicant's authorization before processing the request.  
* Payment is completed before the certificate is generated.  
* The system generates an official To Whom It May Concern Certificate.  
* The certificate contains the latest approved property information.  
* The certificate includes digital authentication information.  
* Applicant can download the certificate in PDF format.  
* Applicant receives a notification when the certificate is ready.  
* Every request receives a unique request reference number.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only eligible applicants with appropriate authorization may request a To Whom It May Concern Certificate.  
2. The property must exist in the official RERAN property registry.  
3. Payment must be completed before the certificate is generated.  
4. The certificate reflects the property's official registry information as of the date of issuance.  
5. The certificate is issued electronically with digital authentication.  
6. Every certificate request receives a unique request reference number.  
7. Previously issued certificates remain available in the request history, subject to applicable retention policies.  
8. The issuance of the certificate does not modify any property registration or ownership records.  
9. Downloaded certificates are considered official only when digitally authenticated by RERAN.  
10. All requests, payments, certificate generations, downloads, and notifications must be permanently recorded in the audit trail.
