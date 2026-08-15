---
project: RERAN
module: individual-user
type: service-flow
status: current
source_type: sourced
updated: 2026-08-15
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - individual-user
  - service-flow
  - tenancy
---

# Service #28 – Request Rental Valuation

**Service Category:** Tenancy Services

## 1. Service Overview

The **Request Rental Valuation** service enables property owners, landlords, tenants, prospective tenants, and other eligible applicants to request an official rental valuation of a property. The service provides an independent assessment of the property's fair rental value based on applicable regulations, market conditions, and approved valuation methodologies.

## 2. Purpose

Provide an official and transparent rental valuation that supports leasing decisions, dispute resolution, regulatory compliance, financing, and other property-related transactions.

## 3. Description

The service allows an eligible applicant to request a rental valuation for a residential, commercial, industrial, or mixed-use property. The applicant submits the required property information and supporting documents. Following verification and valuation by RERAN, and once the valuation is approved, the applicable fee is paid and an official Rental Valuation Report is generated and made available to the applicant.

## 4. Who Can Apply

### Eligible Applicants

* Registered Property Owner  
* Registered Landlord  
* Registered Tenant  
* Prospective Tenant  
* Authorized Representative acting under a valid Power of Attorney

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* Property information is available.  
* Applicant has sufficient authority or interest to request the valuation.  
* Required supporting documents are available.

## 6. Required Information

### Applicant Information

* Full Name  
* National Identification Number (NIN)  
* Contact Number  
* Email Address

### Property Information

* Property Registration Number (if available)  
* Property Address  
* Property Type  
* Property Usage  
* Number of Units (where applicable)  
* Floor Area  
* Land Area (where applicable)

### Valuation Information

* Purpose of Valuation  
* Preferred Inspection Date (if required)  
* Additional Remarks (Optional)

## 7. Required Documents

* Government-issued Identification  
* Proof of Property Ownership (where applicable)  
* Registered Tenancy Agreement (where applicable)  
* Property Photographs (where applicable)  
* Site Plan or Property Map (where applicable)  
* Previous Valuation Report (Optional)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

**Payment is completed after RERAN approves the valuation, not before submission.** Source row 84 states this directly: *"Add details → Upload documents → Pay fees after approval → Receive rental evaluation certificate."*

*(Corrected 2026-08-15 — this file previously required payment before submission, the opposite of what the source explicitly states. This was the clearest single-service finding in `payments.md`'s audit — see Category 2.)*

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**Approximately 20–30 minutes.**

## 12. Processing Workflow

Applicant

Login  
↓  
Open Services  
↓  
Select "Request Rental Valuation"  
↓  
Enter Property Information  
↓  
Enter Valuation Details  
↓  
Upload Required Documents  
↓  
Review Application  
↓  
Submit Application

↓

RERAN

Review Application  
↓  
Verify Property Information  
↓  
Review Supporting Documents  
↓  
Conduct Property Valuation  
↓  
Prepare Rental Valuation Report  
↓  
Approve Report

↓

Applicant

Review Service Fee  
↓  
Pay Service Fee

↓

RERAN

Notify Applicant  
↓  
Release Rental Valuation Report

## 13. Application Status Flow

Draft  
↓  
Submitted  
↓  
Under Review  
↓  
Property Inspection Scheduled (if required)  
↓  
Valuation in Progress  
↓  
Approved — Awaiting Payment  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Completed

### Additional Statuses

* Information Requested  
* Resubmitted  
* Returned  
* Rejected  
* Cancelled

## 14. Possible Outcomes

* Rental Valuation Successfully Completed  
* Rental Valuation Report Issued  
* Property Inspection Required  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed

## 15. Output

Upon successful completion, the system generates:

* Official Rental Valuation Report  
* Estimated Fair Rental Value  
* Property Valuation Summary  
* Payment Receipt

## 16. Related Services

* Service \#23 – Register Lease  
* Service \#24 – Renew Lease  
* Service \#25 – Manage Lease  
* Service \#26 – Submit Tenancy Dispute  
* Service \#27 – Cancel Tenancy Contract

## 17. UI Screens

* Services  
* Request Rental Valuation  
* Property Information  
* Valuation Details  
* Document Upload  
* Application Review  
* Application Submitted  
* Valuation Approved — Payment Due  
* Payment  
* Payment Successful  
* Application Details  
* Rental Valuation Report

## 18. API Requirements

* Validate Applicant  
* Retrieve Property Details  
* Validate Property Information  
* Upload Documents  
* Submit Rental Valuation Request  
* Schedule Property Inspection  
* Generate Rental Valuation Report  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Retrieve Application Status  
* Download Valuation Report  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Rental Valuation  
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

* Applicant can submit a rental valuation request.  
* System validates the property information before submission.  
* Required supporting documents are uploaded successfully.  
* Property inspection can be scheduled where required.  
* Application receives a unique application reference number.  
* An official rental valuation report is prepared and approved by RERAN before payment is requested.  
* Payment is completed after approval, before the report is released to the applicant.  
* Applicant can download the completed valuation report once payment is confirmed.  
* Applicant receives completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only eligible applicants with a legitimate interest in the property may request a rental valuation.  
2. The valuation shall be conducted using RERAN-approved valuation standards and methodologies.  
3. A physical property inspection may be required depending on the property type or regulatory requirements.  
4. **Payment is completed after RERAN approves the valuation report, not before submission.** *(Corrected 2026-08-15 — see Section 9.)*  
5. The rental valuation report becomes official only after approval by RERAN and is released only once payment is confirmed.  
6. The issued valuation reflects the property's estimated rental value as of the valuation date and should not be interpreted as a guaranteed rental price.  
7. Every Request Rental Valuation application receives a unique application reference number.  
8. Rental valuation reports remain part of the property's historical records and may be referenced in future regulatory processes.  
9. Applicants may submit a new valuation request whenever an updated assessment is required.  
10. All applications, approvals, valuation reports, payments, document submissions, and notifications must be permanently recorded in the audit trail.
