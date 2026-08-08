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
  - property-ownership-transaction
---

# Service #4 – Register Property Ownership

**Service Category:** Property Ownership & Transaction Services

## 1. Service Overview

The **Register Property Ownership** service enables an Individual User to officially register legal ownership of a property with RERAN. The service establishes the ownership record within the official property registry after validating the applicant's ownership claim, supporting documents, and regulatory requirements. Upon approval, the property is linked to the registered owner, allowing the owner to access future property-related services through the RERAN platform.

## 2. Purpose

Enable individuals to establish legal ownership of a property by registering it in the official RERAN property registry.

## 3. Description

The service allows an applicant to submit a property ownership registration application by providing property details, ownership information, and the required supporting documents. RERAN reviews the application, verifies the submitted information, and upon successful approval, creates or updates the official ownership record within the property registry.

## 4. Who Can Apply

* Registered Individual User  
* Property Buyer  
* Property Owner  
* Diaspora Investor  
* Authorized Representative acting on behalf of the owner (where legally permitted)

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property is eligible for ownership registration.  
* Applicant possesses valid proof of ownership.  
* Required supporting documents are available.

## 6. Required Information

### Owner Information

* Full Name  
* National Identification Number (NIN)  
* Bank Verification Number (BVN), where applicable  
* Date of Birth  
* Contact Number  
* Email Address  
* Residential Address

### Property Information

* Property Registration Number (if available)  
* Property Address  
* Plot Number  
* Unit Number  
* Development Project (if applicable)  
* Property Type

### Ownership Information

* Acquisition Method  
* Acquisition Date  
* Ownership Type  
* Purchase Price (where applicable)  
* Ownership Percentage (for joint ownership)

## 7. Required Documents

* Government-issued Identification  
* Proof of Ownership  
* Sale Agreement / Purchase Agreement  
* Deed of Assignment  
* Certificate of Occupancy (where applicable)  
* Survey Plan (where applicable)  
* Proof of Payment  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before the ownership registration application is submitted.

## 10. Processing Authority

**RERAN**

The ownership registration application is reviewed by the appropriate RERAN department before the ownership record is created or updated in the official property registry.

## 11. Expected Processing Time

Subject to RERAN's regulatory service standards.

## 12. Processing Workflow

Login  
↓  
Open Services  
↓  
Select "Register Property Ownership"  
↓  
Enter Property Information  
↓  
Enter Ownership Information  
↓  
Upload Supporting Documents  
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
Ownership Registered  
↓  
Download Ownership Registration Certificate

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

## 14. Possible Outcomes

* Ownership Successfully Registered  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful approval, the system generates:

* Property Ownership Registration Confirmation  
* Ownership Registration Number  
* Updated Property Ownership Record  
* Digital Ownership Certificate (where applicable)  
* Payment Receipt

## 16. Related Services

* Service \#3 – Verify Property  
* Service \#5 – Transfer Property Ownership  
* Service \#6 – Register Property Sale  
* Service \#7 – Update Property Ownership Information

## 17. UI Screens

* Services  
* Register Property Ownership  
* Property Information  
* Ownership Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Ownership Registration Certificate

## 18. API Requirements

* Validate Property  
* Validate Applicant  
* Retrieve Property Details  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Ownership Registration Application  
* Retrieve Application Status  
* Retrieve Ownership Certificate  
* Download Certificate

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Ownership History  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Audit Log  
* Notification

## 20. Acceptance Criteria

* User can submit an ownership registration application.  
* All mandatory information is validated before submission.  
* Required documents are uploaded successfully.  
* Payment is successfully completed before submission.  
* Application receives a unique reference number.  
* User can monitor the application status throughout the review process.  
* RERAN can request additional information where necessary.  
* Approved applications update the official property ownership registry.  
* Ownership certificate is generated upon approval.  
* Payment receipt is generated after successful payment.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only authenticated Individual Users may submit a property ownership registration application.  
2. Payment must be completed before the application is submitted.  
3. Ownership registration becomes legally effective only after RERAN approval.  
4. All mandatory supporting documents must be submitted before the application can proceed to review.  
5. Properties with multiple owners must specify ownership percentages and comply with the platform's ownership model.  
6. Joint ownership registrations requiring multiple owners must be completed in accordance with RERAN's ownership policies before approval.  
7. Every ownership registration is assigned a unique application reference number.  
8. All application activities, document submissions, approvals, and ownership changes must be permanently recorded in the audit trail.  
9. The ownership record may only be modified through approved RERAN ownership services.
