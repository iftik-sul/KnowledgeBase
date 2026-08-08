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
  - consumer-protection
---

# Service #39 – Track Complaint

**Service Category:** Consumer Protection Services

## 1. Service Overview

The **Track Complaint** service enables users to monitor the progress of complaints submitted to RERAN. The service provides real-time visibility into complaint status, assigned department, requested actions, investigation progress, and final resolution, ensuring transparency throughout the complaint lifecycle.

## 2. Purpose

Enable complainants to track the progress, current status, and outcome of complaints submitted to RERAN.

## 3. Description

The service allows users to access complaint details using their complaint reference number or from their complaint history. Users can monitor the complaint's current status, review investigation updates, respond to information requests, view communications from RERAN, and download the final resolution once the complaint has been concluded.

## 4. Who Can Apply

* Property Owner  
* Property Buyer  
* Property Seller  
* Tenant  
* Landlord  
* Diaspora Investor  
* Authorized Representative  
* Any Registered Individual User who previously submitted a complaint

## 5. Prerequisites

* Registered RERAN Individual User account.  
* User is logged into the platform.  
* A complaint has previously been submitted to RERAN.

## 6. Required Information

The user may search using one or more of the following:

* Complaint Reference Number  
* Complaint Category  
* Property Reference Number (where applicable)  
* Application Reference Number (where applicable)  
* Date Submitted

## 7. Required Documents

No document upload is required.

If additional information is requested during the investigation, supporting documents may be submitted through the **Respond to Information Request** service.

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment must be completed before complaint tracking is available.

## 10. Processing Authority

**RERAN**

The complaint information is retrieved from the official complaint management system.

## 11. Expected Processing Time

Immediate (real-time lookup), subject to successful payment.

## 12. Processing Workflow

Login  
↓  
Open Services  
↓  
Select "Track Complaint"  
↓  
Search Complaint  
↓  
Review Service Fee  
↓  
Complete Payment  
↓  
Retrieve Complaint Details  
↓  
View Complaint Timeline  
↓  
View Investigation Updates  
↓  
Download Resolution (when available)

## 13. Application Status Flow

Payment Pending  
↓  
Payment Successful  
↓  
Complaint Retrieved  
↓  
Under Review  
↓  
Investigation  
↓  
Information Requested  
↓  
Resolved  
↓  
Closed

### Additional Statuses

* Returned  
* Rejected  
* Withdrawn  
* Cancelled

## 14. Possible Outcomes

* Complaint Found  
* Complaint Not Found  
* Investigation In Progress  
* Information Requested  
* Complaint Resolved  
* Complaint Closed  
* Payment Failed

## 15. Output

The system displays:

* Complaint Reference Number  
* Complaint Category  
* Date Submitted  
* Current Status  
* Assigned Department  
* Investigation Progress  
* Timeline of Activities  
* Communications from RERAN  
* Final Resolution (when available)  
* Downloadable Decision Letter  
* Payment Receipt

## 16. Related Services

* Service \#38 – Submit Complaint  
* Feature \#3 – Respond to Information Request  
* Feature \#2 – Track Application Status

## 17. UI Screens

* Services  
* Track Complaint  
* Complaint Search  
* Payment  
* Payment Successful  
* Complaint Details  
* Complaint Timeline  
* Investigation Updates  
* Resolution Details

## 18. API Requirements

* Search Complaint  
* Retrieve Complaint Details  
* Retrieve Complaint Timeline  
* Retrieve Investigation Updates  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Download Decision Letter

## 19. Database Entities

* User  
* Complaint  
* Complaint Timeline  
* Investigation  
* Department  
* Service Request  
* Payment  
* Payment Transaction  
* Audit Log  
* Notification

## 20. Acceptance Criteria

* User can search for submitted complaints.  
* Payment is completed before complaint details are displayed.  
* Complaint details are retrieved successfully.  
* Timeline displays all major complaint activities.  
* Investigation updates are displayed when available.  
* Final resolution can be downloaded after the complaint is closed.  
* Payment receipt is generated after successful payment.  
* All complaint access activities are recorded in the audit log.

## 21. Business Rules

1. Only the complainant or an authorized representative may view complaint details.  
2. Payment must be completed before complaint information is retrieved.  
3. Users may only access complaints they are authorized to view.  
4. Complaint status is updated automatically as the investigation progresses.  
5. Resolution documents become available only after the complaint has been officially closed.  
6. Users cannot modify complaint information through this service.  
7. Every complaint search and access activity must be permanently recorded in the audit trail.  
8. Additional information requested by RERAN must be submitted through the **Respond to Information Request** service rather than this tracking service.
