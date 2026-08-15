---
project: RERAN
module: individual-user
type: service-flow
status: current
source_type: extrapolated
updated: 2026-08-15
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
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

**No fee.** Tracking a complaint that has already been submitted and paid for (see Service #38) is free, matching Feature #2 – Track Application Status, which this service specialises. See `payments.md` Category 7.

## 9. Payment Required

**No**

Payment is not required to track a complaint that has already been submitted, consistent with the platform-wide principle already applied to every other trackable service in this module (Feature #2).

*(Corrected 2026-08-15 — this file previously required payment before complaint tracking was available, contradicting Feature #2's explicit "no additional fee" principle. There was no source row for this extrapolated service that could have justified the fee. See `payments.md` Category 7 and `open-questions.md` A6.)*

## 10. Processing Authority

**RERAN**

The complaint information is retrieved from the official complaint management system.

## 11. Expected Processing Time

Immediate (real-time lookup).

## 12. Processing Workflow

Login  
↓  
Open Services  
↓  
Select "Track Complaint"  
↓  
Search Complaint  
↓  
Retrieve Complaint Details  
↓  
View Complaint Timeline  
↓  
View Investigation Updates  
↓  
Download Resolution (when available)

## 13. Application Status Flow

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

## 16. Related Services

* Service \#38 – Submit Complaint  
* Feature \#3 – Respond to Information Request  
* Feature \#2 – Track Application Status

## 17. UI Screens

* Services  
* Track Complaint  
* Complaint Search  
* Complaint Details  
* Complaint Timeline  
* Investigation Updates  
* Resolution Details

## 18. API Requirements

* Search Complaint  
* Retrieve Complaint Details  
* Retrieve Complaint Timeline  
* Retrieve Investigation Updates  
* Download Decision Letter

## 19. Database Entities

* User  
* Complaint  
* Complaint Timeline  
* Investigation  
* Department  
* Service Request  
* Audit Log  
* Notification

## 20. Acceptance Criteria

* User can search for submitted complaints.  
* No payment is required to retrieve or view complaint details.  
* Complaint details are retrieved successfully.  
* Timeline displays all major complaint activities.  
* Investigation updates are displayed when available.  
* Final resolution can be downloaded after the complaint is closed.  
* All complaint access activities are recorded in the audit log.

## 21. Business Rules

1. Only the complainant or an authorized representative may view complaint details.  
2. **No payment is required to track complaint information.** *(Corrected 2026-08-15 — see Section 8/9.)*  
3. Users may only access complaints they are authorized to view.  
4. Complaint status is updated automatically as the investigation progresses.  
5. Resolution documents become available only after the complaint has been officially closed.  
6. Users cannot modify complaint information through this service.  
7. Every complaint search and access activity must be permanently recorded in the audit trail.  
8. Additional information requested by RERAN must be submitted through the **Respond to Information Request** service rather than this tracking service.
