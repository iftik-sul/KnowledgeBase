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
  - tenancy
---

# Service #40 – Upload Building Details for Leasing

**Service Category:** Tenancy Services

## 1. Service Overview

The **Upload Building Details for Leasing** service allows a Landlord to submit the details of a building or unit to RERAN before it can be listed and registered for lease. Unlike most Individual User services, this one is not a self-service digital form submission in the source material — it is specified as an email-based data intake process reviewed and entered by RERAN staff.

## 2. Purpose

Enable a Landlord to get a building's details into the RERAN tenancy system so that leases against that building can subsequently be registered.

## 3. Description

The Landlord sends building details to RERAN via an approved email channel. RERAN staff review and approve the data, then upload it into the lease system. This is a prerequisite step that precedes lease registration (Service #23) for buildings not already on file.

## 4. Who Can Apply

* Landlord

## 5. Prerequisites

* Registered RERAN Individual User account.
* Building/property ownership or landlord status.

## 6. Required Information

The source material does not itemize the specific data fields submitted — it describes the channel and steps only, not a field-level form. Reasonable candidates, consistent with what other RERAN property services request, would include building address, unit count, and unit-level details, but this is not confirmed by the source and should not be treated as final without client confirmation.

## 7. Required Documents

Not specified in the source material.

## 8. Service Fee

Not specified in the source material.

## 9. Payment Required

Not specified in the source material. Unlike most other Individual User services, this row in the master service table has no payment step in its workflow.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**One business day**

## 12. Processing Workflow

Landlord sends building details via approved email
↓
RERA staff receive and review the data
↓
RERA staff approve the data
↓
Data uploaded into the lease system

**Note:** the source describes this as an off-platform, email-based intake process rather than an in-app self-service flow, which is a different shape from every other Tenancy Service in this module. Whether this should eventually become a proper in-app form (matching the rest of the module's UX) or remain an email/back-office process is a scope question for the client, not a documentation decision.

## 13. Application Status Flow

Submitted (via email)
↓
Under Review
↓
Approved
↓
Uploaded to System

### Additional Statuses

* Rejected / Returned for correction (implied by the review step; not detailed in source)

## 14. Possible Outcomes

* Building details successfully uploaded and available for lease registration
* Data rejected or returned for correction

## 15. Output

Not specified in the source material beyond "data uploaded into the lease systems" — no certificate or document output is described for this service.

## 16. Related Services

* Service #23 – Register Lease
* Service #24 – Renew Lease

## 17. UI Screens

Not yet designed — this module has no UI documentation yet (see module README). Given the email-based nature of this service per the source, it may not need the same screen set as other services; worth confirming before UI work begins.

## 18. API Requirements

Not specified in the source material.

## 19. Database Entities

* Landlord
* Building
* Building Details Submission

## 20. Acceptance Criteria

* Landlord can submit building details via the approved channel.
* RERA staff can review and approve or reject submitted data.
* Approved data becomes available for subsequent lease registration against that building.

## 21. Business Rules

1. Building details must be reviewed and approved by RERA before the building can be used in lease registration.
2. The source specifies this as an email-based process; it is unclear whether an in-app equivalent is intended for this platform. **Flagged for client confirmation** rather than assumed.
