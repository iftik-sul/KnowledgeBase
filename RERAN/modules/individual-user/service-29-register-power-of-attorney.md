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
  - power-of-attorney
---

# Service #29 – Register Power of Attorney

**Service Category:** Power of Attorney Services

## 1. Service Overview

The **Register Power of Attorney** service enables a property owner to officially register a Power of Attorney (PoA) with RERAN, authorizing another individual to act on their behalf in relation to one or more properties. The registered authorization allows the appointed representative to perform approved property-related transactions within the scope and validity period specified in the Power of Attorney.

## 2. Purpose

Enable property owners to legally appoint an authorized representative to carry out approved property-related activities on their behalf through the RERAN platform.

## 3. Description

The service allows a property owner to submit a Power of Attorney registration application by providing the details of the principal, the appointed attorney, the properties covered by the authorization, the scope of authority, and supporting legal documents. After review and approval by RERAN, the Power of Attorney is registered and becomes available for use in eligible services.

## 4. Who Can Apply

* Registered Property Owner  
* Joint Property Owner  
* Individual legally authorized to grant a Power of Attorney

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is registered with RERAN.  
* Applicant is the legal owner of the property.  
* A valid Power of Attorney document has been executed.  
* Required supporting documents are available.

## 6. Required Information

### Principal (Property Owner) Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address  
* Residential Address

### Attorney Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address  
* Residential Address

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Power of Attorney Information

* Power of Attorney Number (if applicable)  
* Type of Power of Attorney  
* Scope of Authority  
* Effective Date  
* Expiry Date (if applicable)  
* Purpose of Authorization  
* Additional Remarks (Optional)

## 7. Required Documents

* Signed Power of Attorney Document  
* Government-issued Identification of the Principal  
* Government-issued Identification of the Attorney  
* Proof of Property Ownership  
* Supporting Legal Documents  
* Court Order (where applicable)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before the Power of Attorney registration application is submitted.

## 10. Processing Authority

**RERAN**

The Power of Attorney registration application is reviewed by the appropriate RERAN department before the authorization is recorded in the official registry.

## 11. Expected Processing Time

Subject to RERAN's regulatory service standards.

## 12. Processing Workflow

Login  
↓  
Open Services  
↓  
Select "Register Power of Attorney"  
↓  
Select Property  
↓  
Enter Principal Information  
↓  
Enter Attorney Information  
↓  
Define Scope of Authority  
↓  
Upload Power of Attorney Documents  
↓  
Review Application  
↓  
Review Service Fee  
↓  
Complete Payment  
↓  
Submit Application  
↓  
Application Validation  
↓  
RERAN Review  
↓  
Additional Information Requested (if required)  
↓  
Applicant Responds  
↓  
Final Review  
↓  
Application Approved  
↓  
Power of Attorney Registered  
↓  
Download Registration Confirmation

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted  
↓  
Validation  
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
* Withdrawn  
* Cancelled  
* Expired

## 14. Possible Outcomes

* Power of Attorney Successfully Registered  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful approval, the system generates:

* Power of Attorney Registration Confirmation  
* Registered Power of Attorney Record  
* Authorization Reference Number  
* Digital Registration Certificate  
* Payment Receipt

## 16. Related Services

* Service \#30 – Act on Behalf of Property Owner  
* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership  
* Service \#6 – Register Property Sale

## 17. UI Screens

* Services  
* Register Power of Attorney  
* Select Property  
* Principal Information  
* Attorney Information  
* Scope of Authority  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Registration Confirmation

## 18. API Requirements

* Retrieve User Properties  
* Retrieve Property Details  
* Validate Property Ownership  
* Validate Attorney Information  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Power of Attorney Registration  
* Retrieve Application Status  
* Generate Registration Confirmation  
* Download Registration Certificate

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Power of Attorney  
* Principal  
* Attorney  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Audit Log  
* Notification

## 20. Acceptance Criteria

* User can register a Power of Attorney for an eligible property.  
* System validates that the applicant is the legal property owner.  
* Attorney information is successfully validated.  
* Required documents are uploaded successfully.  
* Payment is completed before submission.  
* Application receives a unique reference number.  
* User can monitor the application status throughout the review process.  
* Approved applications create an official Power of Attorney record.  
* Registration confirmation is generated upon approval.  
* Payment receipt is generated after successful payment.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the legal property owner or a person legally authorized to grant a Power of Attorney may submit this application.  
2. The property must already be registered in the RERAN property registry.  
3. Payment must be completed before the application is submitted.  
4. The Power of Attorney becomes effective only after approval and registration by RERAN.  
5. The attorney may perform only those actions expressly authorized in the registered Power of Attorney.  
6. A Power of Attorney may have a defined validity period or remain effective until revoked, in accordance with applicable law.  
7. Revoked or expired Powers of Attorney cannot be used to perform property-related services.  
8. Every registered Power of Attorney receives a unique authorization reference number.  
9. All submissions, approvals, document uploads, payments, and subsequent changes to the authorization must be permanently recorded in the audit trail.
