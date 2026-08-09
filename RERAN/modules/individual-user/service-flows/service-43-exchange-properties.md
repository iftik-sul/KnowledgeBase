---
project: RERAN
module: individual-user
type: service-flow
status: current
updated: 2026-08-10
source_type: sourced
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - individual-user
  - service-flow
  - title-land-registration
---

# Service #43 – Exchange Properties

**Service Category:** Title & Land Registration Services

## 1. Service Overview

The **Exchange Properties** service allows two Property Owners to formally register an exchange of two properties with RERAN, updating title records for both parties as part of a single transaction.

## 2. Purpose

Enable property owners to register a direct property-for-property exchange (rather than a sale) and have both resulting title changes officially recorded.

## 3. Description

The applicant visits the Customer Centre at the Land Department, submits documents, and RERA staff enter the exchange data into the system. After payment, the transaction is audited and approved, and both parties receive their updated title documents via email.

The source describes this from a single applicant's perspective; it does not specify whether both parties in the exchange must separately apply, jointly apply, or whether one party applies on behalf of both. This is a real process-design gap, not a documentation omission, and should be resolved with the client before UI or workflow design.

## 4. Who Can Apply

* Property Owner / Seller

## 5. Prerequisites

* Both properties involved in the exchange must already be registered with RERAN.
* Registered RERAN Individual User account.

## 6. Required Information

Not itemized field-by-field in the source. At minimum, both properties' registration details and both parties' identity information would be needed, by analogy with other title-transfer services in this module — but this is inferred, not sourced.

## 7. Required Documents

Not specified in the source material beyond "submit docs."

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**25 minutes**

## 12. Processing Workflow

Visit Customer Centre at Land Department
↓
Submit Documents
↓
RERA Staff Enter Data
↓
Pay Fees
↓
Transaction Audited and Approved
↓
Receive Title Deed and Map via Email

## 13. Application Status Flow

Submitted
↓
Under Review
↓
Approved
↓
Completed

### Additional Statuses

* Rejected (implied by the audit step)

## 14. Possible Outcomes

* Exchange successfully registered, both title records updated
* Application rejected

## 15. Output

* E-Certificate of Title / Title Deed
* E-Map

## 16. Related Services

* Service #5 – Transfer Property Ownership
* Service #6 – Register Property Sale
* Service #106 (source row) – Title Transfer, documented here as part of Service #7 – Update Property Ownership Information

## 17. UI Screens

Not yet designed — this module has no UI documentation yet.

## 18. API Requirements

Not specified in the source material.

## 19. Database Entities

* Property Owner
* Property (x2 — both sides of the exchange)
* Property Exchange Transaction

## 20. Acceptance Criteria

* Applicant can submit an exchange request covering both properties.
* RERA staff can enter, audit, and approve or reject the request.
* Approved exchanges update title records for both properties and issue documents accordingly.

## 21. Business Rules

1. Both properties involved must already be registered with RERAN before an exchange can be processed.
2. **Open question, not resolved here:** whether both owners must independently confirm the exchange (similar to the seller/purchaser two-sided flow in Service #6 – Register Property Sale) or whether a single applicant can register on behalf of both parties. The source does not specify this, and it materially affects the workflow design.
