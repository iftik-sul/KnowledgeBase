---
project: RERAN
module: individual-user
type: service-flow
status: current
updated: 2026-08-09
derived_from:
  - "RERAN/modules/individual-user/RERAN_ individual user_service_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
tags:
  - individual-user
  - service-flow
  - diaspora
---

# Service #36 – Remote Identity Verification

**Service Category:** Diaspora Services

## 1. Service Overview

The **Remote Identity Verification** service enables Nigerians living outside Nigeria to securely verify their identity through the RERAN platform without visiting a RERAN office. The verified identity allows eligible users to access remote property-related services, complete regulatory requirements, and participate in property transactions from anywhere in the world.

## 2. Purpose

Enable eligible users to complete identity verification remotely, allowing secure access to RERAN services without requiring physical attendance.

## 3. Description

The service allows users to submit personal information, upload identification documents, complete biometric verification where required, and undergo identity validation through RERAN's remote verification process. Upon successful verification, the user's identity status is updated, enabling access to eligible online services.

## 4. Who Can Apply

* Diaspora Investor  
* Nigerian Citizen Living Abroad  
* Property Owner Living Abroad  
* Property Buyer Living Abroad  
* Authorized Representative (where applicable)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* User resides outside Nigeria or requires remote identity verification.  
* Valid government-issued identification is available.  
* Internet connection with camera access for biometric verification (where required).

## 6. Required Information

### Personal Information

* Full Name  
* Date of Birth  
* National Identification Number (NIN)  
* Passport Number (where applicable)  
* Country of Residence  
* Residential Address  
* Contact Number  
* Email Address

### Verification Information

* Identity Verification Method  
* Selfie Photograph  
* Live Facial Verification (where applicable)  
* Additional Verification Information

## 7. Required Documents

* International Passport  
* National Identification Card  
* Driver's License (where accepted)  
* Residence Permit or Visa (where applicable)  
* Proof of Address  
* Other identification documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before the identity verification request is processed.

## 10. Processing Authority

**RERAN**

Identity verification is reviewed and validated by the appropriate RERAN verification unit.

## 11. Expected Processing Time

Subject to RERAN's identity verification service standards.

## 12. Processing Workflow

Login  
↓  
Open Services  
↓  
Select "Remote Identity Verification"  
↓  
Enter Personal Information  
↓  
Select Verification Method  
↓  
Upload Identification Documents  
↓  
Complete Biometric Verification  
↓  
Review Application  
↓  
Review Service Fee  
↓  
Complete Payment  
↓  
Submit Verification Request  
↓  
Identity Validation  
↓  
RERAN Review  
↓  
Verification Approved  
↓  
Identity Verified  
↓  
Receive Verification Confirmation

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Submitted  
↓  
Identity Validation  
↓  
Under Review  
↓  
Information Requested  
↓  
Resubmitted  
↓  
Verified  
↓  
Completed

### Additional Statuses

* Verification Failed  
* Returned  
* Rejected  
* Withdrawn  
* Cancelled

## 14. Possible Outcomes

* Identity Successfully Verified  
* Additional Information Requested  
* Identity Verification Failed  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful verification, the system generates:

* Identity Verification Confirmation  
* Verified User Status  
* Verification Reference Number  
* Verification Certificate (where applicable)  
* Payment Receipt

## 16. Related Services

* Service \#37 – Remote Property Transactions  
* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership  
* Service \#6 – Register Property Sale

## 17. UI Screens

* Services  
* Remote Identity Verification  
* Personal Information  
* Identity Verification  
* Document Upload  
* Biometric Verification  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Verification Status  
* Verification Confirmation

## 18. API Requirements

* Validate User  
* Upload Identity Documents  
* Perform Biometric Verification  
* Validate Identity  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Verification Request  
* Retrieve Verification Status  
* Generate Verification Confirmation

## 19. Database Entities

* User  
* Identity Verification  
* Identity Document  
* Biometric Verification  
* Application  
* Service Request  
* Payment  
* Payment Transaction  
* Audit Log  
* Notification

## 20. Acceptance Criteria

* User can submit a remote identity verification request.  
* Required personal information is validated.  
* Identity documents are uploaded successfully.  
* Biometric verification is completed where required.  
* Payment is completed before submission.  
* Application receives a unique reference number.  
* User can monitor the verification status.  
* Approved applications update the user's identity verification status.  
* Verification confirmation is generated upon approval.  
* Payment receipt is generated after successful payment.  
* All verification activities are recorded in the audit log.

## 21. Business Rules

1. Only registered Individual Users may request remote identity verification.  
2. Payment must be completed before the application is submitted.  
3. Identity verification must be completed successfully before accessing services that require verified identity.  
4. Identity documents must be valid, authentic, and unexpired.  
5. Biometric verification may be mandatory depending on the selected verification method or regulatory requirements.  
6. A user may have only one active identity verification request at a time.  
7. Once verified, the user's verification status may be reused for eligible RERAN services until re-verification is required.  
8. All verification activities, document submissions, biometric checks, approvals, and status changes must be permanently recorded in the audit trail.  
9. RERAN may require re-verification if identity information changes or if required by regulatory policy.
