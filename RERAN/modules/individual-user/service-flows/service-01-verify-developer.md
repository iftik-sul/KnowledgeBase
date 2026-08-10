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

# Service #1 – Verify Developer

**Service Category:** Verification Services

## 1. Service Overview

The **Verify Developer** service allows an Individual User to verify whether a real estate developer is officially registered with RERAN before purchasing property, investing in a development, or entering into any real estate transaction. The service provides access to the official RERAN developer registry, enabling users to confirm the legitimacy and registration status of a developer and make informed decisions while reducing the risk of fraud.

## 2. Purpose

Enable users to verify that a real estate developer is officially registered and recognized by RERAN before engaging in any real estate transaction.

## 3. Description

The service searches the official RERAN developer registry using the search information provided by the user. If the developer is found, the system displays the developer's public registration information and current registration status. If no matching record exists, the user is informed that no registered developer was found.

## 4. Who Can Apply

All registered Individual Users.

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* No additional approvals are required.

## 6. Required Information

The user provides one or more search criteria.

* Developer Name  
* Developer Registration Number  
* Company Name *(where applicable)*  
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

The service retrieves information from the official RERAN Developer Registry.

## 11. Expected Processing Time

Immediate (real-time lookup), assuming successful payment.

## 12. Processing Workflow

Login  
↓  
Open Services  
↓  
Select "Verify Developer"  
↓  
Enter Developer Search Criteria  
↓  
Review Service Fee  
↓  
Complete Payment  
↓  
Submit Verification Request  
↓  
System Searches Official Developer Registry  
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

* Developer Verified  
* Developer Not Found  
* Invalid Search Criteria  
* Payment Failed  
* Service Cancelled

## 15. Output

Successful verification displays the public registration details of the developer.

Typical information includes:

* Developer Name  
* Developer Registration Number  
* Registration Status  
* License Status  
* Company Name  
* Registration Date  
* Verification Timestamp

The displayed information should be limited to publicly available registry information.

## 16. Related Services

* Service \#2 – Verify Development Project  
* Service \#3 – Verify Property

These services are commonly used together before purchasing or investing in a property.

## 17. UI Screens

* Services  
* Verify Developer  
* Payment  
* Payment Successful  
* Verification Processing  
* Verification Result  
* Download Verification Report

## 18. API Requirements

* Search Developer  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Verification Request  
* Get Verification Result  
* Download Verification Report

## 19. Database Entities

* User  
* Developer  
* Service Request  
* Payment  
* Payment Transaction  
* Verification Result  
* Audit Log

## 20. Acceptance Criteria

* User can search using valid developer information.  
* Payment is successfully completed before processing begins.  
* System searches only the official RERAN Developer Registry.  
* Verification results are displayed immediately.  
* User can download the verification report.  
* Every verification request is recorded in the audit log.  
* A payment receipt is generated after successful payment.

## 21. Business Rules

1. Any authenticated Individual User may use this service.  
2. Payment must be completed before verification begins. *(Platform Design Decision)*  
3. Only officially registered RERAN developers are returned.  
4. The service is read-only and cannot modify developer information.  
5. Every verification request must be recorded for audit purposes.  
6. Users may perform multiple verification requests, with each request subject to the applicable service fee.  
7. Only public registry information may be displayed to users.
