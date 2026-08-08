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
  - title-land-registration
---

# Service #18 – Grant Completion

**Service Category:** Title & Land Registration Services

## 1. Service Overview

The **Grant Completion** service enables an applicant to complete the registration process for a previously approved land grant. Upon successful completion, the property is formally recorded in the official registry, and the final title documents and property map are issued electronically.

## 2. Purpose

Enable grant recipients to complete all statutory requirements necessary for the issuance of final title documents following an approved land grant.

## 3. Description

The service allows an eligible applicant to finalize a previously approved grant registration by submitting the required documentation, completing the applicable service fee, and undergoing regulatory review. Once approved, the grant registration is completed and the official title documents are issued electronically.

## 4. Who Can Apply

### Grant Recipient

* Registered Individual User  
* Registered Legal Entity (where applicable)  
* Authorized Representative acting under a valid Power of Attorney

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Grant Registration has been approved.  
* Applicant is the lawful grant recipient or authorized representative.  
* Required supporting documents are available.

## 6. Required Information

### Applicant Information

* Full Name / Organization Name  
* National Identification Number (NIN) or Registration Number  
* Contact Number  
* Email Address

### Grant Information

* Grant Registration Number  
* Grant Reference Number  
* Grant Date

### Property Information

* Property Registration Number  
* Property Address  
* Plot Number  
* Property Type

### Completion Information

* Completion Date  
* Additional Remarks (Optional)

## 7. Required Documents

* Grant Registration Approval  
* Government Grant Letter  
* Government-issued Identification  
* Survey Plan  
* Property Map (where applicable)  
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

**Approximately 25 minutes.**

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Grant Completion"  
↓  
Select Approved Grant Registration  
↓  
Review Grant Information  
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
Verify Grant Registration  
↓  
Verify Supporting Documents  
↓  
Confirm Completion Requirements  
↓  
Approve Grant Completion  
↓  
Update Property Registry  
↓  
Generate Final Title Documents  
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

* Grant Successfully Completed  
* Final Property Registration Completed  
* Title Documents Successfully Issued  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Electronic Certificate of Title  
* Electronic Title Deed  
* Property Registration Certificate  
* Property Map  
* Payment Receipt

## 16. Related Services

* Service \#17 – Grant Registration  
* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership  
* Service \#7 – Update Property Ownership Information

## 17. UI Screens

* Services  
* Grant Completion  
* Select Approved Grant  
* Grant Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Completion Confirmation

## 18. API Requirements

* Retrieve Approved Grant Registrations  
* Retrieve Grant Details  
* Validate Grant Registration  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Grant Completion Application  
* Retrieve Application Status  
* Update Property Registry  
* Generate Final Title Documents  
* Download Registration Documents  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Land Grant  
* Grant Completion  
* Property Registration  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Applicant can complete an approved grant registration.  
* System validates that the grant registration is eligible for completion.  
* Required information is validated before submission.  
* Required supporting documents are uploaded successfully.  
* Payment is completed before regulatory review.  
* Application receives a unique application reference number.  
* Approved applications complete the official property registration.  
* Final title documents are generated upon approval.  
* Applicant receives completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the approved grant recipient or an authorized representative may submit a Grant Completion application.  
2. Grant Registration must already be approved before Grant Completion can be requested.  
3. All completion requirements and supporting documents must be satisfied before approval.  
4. Payment must be completed before the application proceeds for review.  
5. Grant Completion becomes legally effective only after approval by RERAN.  
6. Final title documents are issued only after the completion process has been approved.  
7. The official property registry is updated upon successful completion.  
8. Every Grant Completion application receives a unique application reference number.  
9. The completed grant becomes part of the permanent ownership history of the property.  
10. All applications, approvals, payments, registry updates, document submissions, title issuance, and notifications must be permanently recorded in the audit trail.
