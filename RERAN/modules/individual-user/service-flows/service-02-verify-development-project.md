---
project: RERAN
module: individual-user
type: service-flow
status: current
source_type: extrapolated
updated: 2026-08-09
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - individual-user
  - service-flow
  - verification
---

# Service #2 – Verify Development Project

**Service Category:** Verification Services

## 1. Service Overview

The **Verify Development Project** service enables an Individual User to verify whether a real estate development project is officially registered and approved by RERAN before purchasing, investing, or participating in any property transaction. The service provides access to the official RERAN project registry, allowing users to confirm the legitimacy, registration status, and associated developer of a project.

## 2. Purpose

Enable users to verify the authenticity and registration status of a real estate development project before engaging in any property-related transaction.

## 3. Description

The service searches the official RERAN project registry using the information provided by the user. If the project is found, the system displays the project's public registration details, registration status, approval status, developer information, and location. If no matching project is found, the user is informed accordingly.

## 4. Who Can Apply

All registered Individual Users.

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* No prior approval is required.

## 6. Required Information

The user provides one or more search criteria.

* Project Name  
* Project Registration Number  
* Developer Name  
* Project Location  
* Project Reference Number  
* Keyword Search

## 7. Required Documents

No document upload is required.

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before the verification request is processed.

## 10. Processing Authority

**RERAN**

The service retrieves information from the official RERAN Development Project Registry.

## 11. Expected Processing Time

Immediate (real-time lookup), subject to successful payment.

## 12. Processing Workflow

Login  
↓  
Open Services  
↓  
Select "Verify Development Project"  
↓  
Enter Project Search Criteria  
↓  
Review Service Fee  
↓  
Complete Payment  
↓  
Submit Verification Request  
↓  
System Searches Official Development Project Registry  
↓  
Verification Result Generated  
↓  
View / Download Verification Report

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

### Possible Exception Statuses

* Payment Failed  
* Verification Failed  
* Cancelled

## 14. Possible Outcomes

* Project Verified  
* Project Not Found  
* Invalid Search Criteria  
* Payment Failed  
* Service Cancelled

## 15. Output

Successful verification displays the public registration details of the development project.

Typical information includes:

* Project Name  
* Project Registration Number  
* Registration Status  
* Approval Status  
* Registered Developer  
* Developer Registration Number  
* Project Location  
* Development Type  
* Registration Date  
* Verification Timestamp

Only publicly available registry information is displayed.

## 16. Related Services

* Service \#1 – Verify Developer  
* Service \#3 – Verify Property  
* Service \#4 – Register Property Ownership  
* Service \#6 – Register Property Sale

## 17. UI Screens

* Services  
* Verify Development Project  
* Payment  
* Payment Successful  
* Verification Processing  
* Verification Result  
* Download Verification Report

## 18. API Requirements

* Search Development Project  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Verification Request  
* Retrieve Verification Result  
* Download Verification Report

## 19. Database Entities

* User  
* Development Project  
* Developer  
* Service Request  
* Payment  
* Payment Transaction  
* Verification Result  
* Audit Log

## 20. Acceptance Criteria

* User can search using valid project information.  
* Payment is successfully completed before processing begins.  
* System searches only the official RERAN Development Project Registry.  
* Verification results are displayed immediately after processing.  
* User can download the verification report.  
* Every verification request is recorded in the audit log.  
* A payment receipt is generated after successful payment.

## 21. Business Rules

1. Any authenticated Individual User may request this service.  
2. Payment must be completed before verification begins.  
3. Only officially registered RERAN development projects are returned.  
4. The service is read-only and cannot modify project information.  
5. Every verification request must be recorded for audit purposes.  
6. Users may perform multiple verification requests, subject to the applicable service fee.  
7. Only public registry information may be disclosed through this service.
