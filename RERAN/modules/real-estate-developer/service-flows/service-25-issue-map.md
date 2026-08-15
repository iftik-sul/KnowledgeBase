---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-15
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registration-details.md"
tags:
  - real-estate-developer
  - service-flow
  - title-deed-data-services
---

# Service #25 – Issuing Map Application

**Service Category:** Title Deed Data Services

## 1. Service Overview

The **Issuing Map Application** service allows a property owner (the developer, acting on the project's behalf, or a unit owner post-transfer) to request an official survey map for a property.

> **Ambiguous screen mapping — flagged, not resolved.** Same ambiguity as Service #24: the source's "Owner applies" framing could sit under either `property-registration-details.md` (property-level) or `project-details.md` (project-level), and no screen names a standalone "Issue Map" action. Documented against `property-registration-details.md` as the closer fit, given the source frames the applicant as a property "Owner," but flagged rather than asserted with full confidence.

## 2. Purpose

Provide an authoritative, current survey map of a registered property on request.

## 3. Description

The owner applies for a map. RERA receives and reviews the application, issues the map, and sends it to the customer.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Project Registration Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* An existing registered property/unit (see Service #1–#6) or project (Service #13) the map covers.

## 6. Required Information

* Property or Project Reference Number
* Requested Map Type/Scope

## 7. Required Documents

> **Proposed** — not itemized in the source beyond "applies." Needs client confirmation.

* None specified beyond the application itself

## 8. Service Fee

Applicable according to the RERAN fee schedule. Where charged, paid through the shared platform payment gateway, per transaction. There is no standing or pre-funded RERA-fee account for developers; each application is paid for on its own.

## 9. Payment Required

**Not specified in the source** — this service's workflow contains no payment step, so neither the fee's existence nor its timing is sourced. **Proposed**: a fee applies, paid per transaction through the shared platform payment gateway at the point of submission, consistent with the other document-issuance services whose payment step *is* sourced; needs client confirmation. Flagged rather than assumed, since neighbouring services in this category differ on timing.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**One business day**

## 12. Processing Workflow

Owner Applies
↓
Receipt and Review of Application
↓
Issuance of the Map
↓
Send Map to Customer

## 13. Application Status Flow

Submitted
↓
Under Review
↓
Approved
↓
Issued

### Additional Statuses

* Rejected

## 14. Possible Outcomes

* Map Successfully Issued
* Application Rejected

## 15. Output

* Map

## 16. Related Services

* Service #5 – Complete Initial Procedures Data
* Service #24 – Registration/Amendment of Real Estate Project Details
* Service #26 – Separation or Annexing a Property

## 17. UI Screens

* Property Registration Details *(closest fit — see Section 1)*
* Application Submitted

## 18. API Requirements

* Retrieve Property or Project
* Submit Map Application
* Retrieve Application Status
* Generate Map
* Send Notifications

## 19. Database Entities

* Developer Company
* Property Unit
* Project
* Map Record
* Application
* Notification
* Audit Log

## 20. Acceptance Criteria

* Applicant can request a map for a registered property or project.
* System reviews the application before issuance.
* Approved applications generate and deliver a map to the customer.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a registered property or project may have a map issued under this service.
2. All submissions, reviews, and deliveries must be permanently recorded in the audit trail.
