---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-10
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-licensing-service
---

# Service #23 – Accreditation of Training Entities

**Service Category:** Real Estate Licensing Service

## 1. Service Overview

The **Accreditation of Training Entities** service allows an organization to become an RERA-accredited provider of real estate training, through an email-based partnership process distinct from the portal-based application flow the rest of this module uses.

> **UI gap — flagged, not resolved.** No screen in the 19-screen UI set represents this service; it is also the only Group B service the source channels through email rather than the developer portal. There is no reasonable existing screen to anchor a "closest match" to, unlike several other gapped services above.

## 2. Purpose

Accredit organizations able to deliver real estate training relevant to RERA's regulatory ecosystem, formalized as a signed partnership agreement.

## 3. Description

An organization applies for accreditation by request; a meeting is held; the applicant reviews RERA's proposal; the applicant submits a partnership application; and the parties sign an agreement. The entire process runs over email, not the developer portal.

## 4. Who Can Apply

* An organization seeking accreditation as a real estate training entity — not necessarily an existing Group B developer account holder, since the source's process is email-based rather than portal-based. **Proposed**: documenting the applicant as the Developer Principal / Director where the applicant is already a registered developer entity; needs client confirmation for non-developer applicants.

## 5. Prerequisites

* Organizational capacity to deliver real estate training.
* Willingness to enter a formal partnership agreement with RERA.

## 6. Required Information

* Organization Name and Contact Information
* Proposed Training Scope

## 7. Required Documents

> **Proposed** — not itemized in the source beyond the workflow's named steps. Needs client confirmation.

* Organizational Profile / Credentials
* Draft Partnership Proposal

## 8. Service Fee

Not specified in the source. **Proposed**: none, given the partnership-agreement framing; needs client confirmation.

## 9. Payment Required

Not specified in the source. **Proposed**: no; needs client confirmation.

## 10. Processing Authority

**Licensing & Registration Officer**

## 11. Expected Processing Time

**4 business working days**

## 12. Processing Workflow

Apply Request (via Email)
↓
Meeting Held
↓
Applicant Views RERA's Proposal
↓
Applicant Submits Partnership Application
↓
Agreement Signed

**Channel:** Email — the only Group B service documented as email-only rather than portal-based.

## 13. Application Status Flow

Requested
↓
Meeting Scheduled
↓
Proposal Reviewed
↓
Partnership Application Submitted
↓
Agreement Signed
↓
Accredited

### Additional Statuses

* Declined
* Withdrawn

## 14. Possible Outcomes

* Training Entity Successfully Accredited
* Partnership Declined
* Application Withdrawn

## 15. Output

* Signed Agreement

## 16. Related Services

* Service #22 – Real Estate Licensing Application

## 17. UI Screens

Not currently represented in the 19-screen UI set, and not expected to be — the source documents this as an email-based process outside the portal. No **proposed** UI surface is offered here, unlike other gapped services, since the source itself specifies a non-portal channel.

## 18. API Requirements

Not applicable in the same sense as portal-based services — the source specifies an email workflow. **Proposed**: if a portal record of accredited entities is desired, a minimal Accredited Training Entities register would need: Create Accreditation Record, Update Accreditation Status, Retrieve Accredited Entities List. Needs client confirmation of whether this is in scope.

## 19. Database Entities

* Training Entity
* Partnership Agreement
* Accreditation Record

## 20. Acceptance Criteria

* An organization can request accreditation as a training entity.
* A meeting and proposal review precede a formal partnership application.
* A signed agreement completes the accreditation.

## 21. Business Rules

1. This service runs over email rather than the developer portal — the only Group B service documented this way.
2. Accreditation is finalized only once the partnership agreement is signed by both parties.
3. **No UI screen exists or is proposed for this service**, consistent with its non-portal channel — flagged for the client to confirm scope before any UI work is considered.
