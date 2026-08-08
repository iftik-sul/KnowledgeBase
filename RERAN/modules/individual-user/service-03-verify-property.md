---
project: RERAN
module: individual-user
type: service-flow
status: current
updated: 2026-08-09
derived_from:
  - "RERAN/modules/individual-user/RERAN_ individual user_service_flows.md"
tags:
  - individual-user
  - service-flow
  - verification
---

# Service #3 – Verify Property

**Service Category:** Verification Services

## 1. Service Overview

The **Verify Property** service enables an Individual User to verify whether a property is officially registered with RERAN before purchasing, leasing, investing, or conducting any property-related transaction. The service provides access to the official RERAN property registry, allowing users to confirm the authenticity, registration status, and key public information associated with a property.

## 2. Purpose

Enable users to verify the authenticity and registration status of a property before entering into any real estate transaction.

## 3. Description

The service searches the official RERAN property registry using the search information provided by the user. If the property exists, the system displays its public registration details, registration status, location, property type, and associated development information where applicable. If no matching property is found, the user is notified accordingly.

## 4. Who Can Apply

All registered Individual Users.

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* No prior approval is required.

## 6. Required Information

The user provides one or more search criteria.

* Property Registration Number  
* Property Reference Number  
* Property Address  
* Plot Number  
* Unit Number  
* Development Project Name  
* Title Number *(where applicable)*  
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

The service retrieves information from the official RERAN Property Registry.

## 11. Expected Processing Time

Immediate (real-time lookup), subject to successful payment.

## 12. Processing Workflow

Login  
↓  
Open Services  
↓  
Select "Verify Property"  
↓  
Enter Property Search Criteria  
↓  
Review Service Fee  
↓  
Complete Payment  
↓  
Submit Verification Request  
↓  
System Searches Official Property Registry  
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

* Property Verified  
* Property Not Found  
* Invalid Search Criteria  
* Payment Failed  
* Service Cancelled

## 15. Output

Successful verification displays the public registration details of the property.

Typical information includes:

* Property Registration Number  
* Property Status  
* Property Type  
* Property Address  
* Development Project *(if applicable)*  
* Registered Developer *(if applicable)*  
* Registration Date  
* Verification Timestamp

Only publicly available registry information is displayed.

## 16. Related Services

* Service \#1 – Verify Developer  
* Service \#2 – Verify Development Project  
* Service \#4 – Register Property Ownership  
* Service \#5 – Transfer Property Ownership

## 17. UI Screens

* Services  
* Verify Property  
* Payment  
* Payment Successful  
* Verification Processing  
* Verification Result  
* Download Verification Report

## 18. API Requirements

* Search Property  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Verification Request  
* Retrieve Verification Result  
* Download Verification Report

## 19. Database Entities

* User  
* Property  
* Development Project  
* Developer  
* Service Request  
* Payment  
* Payment Transaction  
* Verification Result  
* Audit Log

## 20. Acceptance Criteria

* User can search using valid property information.  
* Payment is successfully completed before processing begins.  
* System searches only the official RERAN Property Registry.  
* Verification results are displayed immediately after processing.  
* User can download the verification report.  
* Every verification request is recorded in the audit log.  
* A payment receipt is generated after successful payment.

## 21. Business Rules

1. Any authenticated Individual User may request this service.  
2. Payment must be completed before verification begins.  
3. Only officially registered properties in the RERAN registry are returned.  
4. The service is read-only and cannot modify any property information.  
5. Every verification request must be recorded for audit purposes.  
6. Users may perform multiple verification requests, subject to the applicable service fee.  
7. Only public registry information may be disclosed through this service.
