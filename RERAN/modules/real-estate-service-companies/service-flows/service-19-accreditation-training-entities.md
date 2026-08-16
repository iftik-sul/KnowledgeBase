---
project: RERAN
module: real-estate-service-companies
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-service-companies/services-overview.md"
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-23-accredit-training-entities.md"
tags:
  - real-estate-service-companies
  - service-flow
  - licensing
  - accreditation
---

# Service #19 – Accreditation of Training Entities (Real Estate Companies)

**Service Category:** Real Estate Licensing Services

**Source row:** 66 of `RERAN_service_flows_v2.md`.

> **Near-duplicate of Real Estate Developer's Service #23, same name pattern.** Checked directly: both rows describe an identical five-step email process (Apply → Meeting → View Proposal → Submit Partnership Application → Sign Agreement), with the same 4-business-day SLA and the same "Agreement" output. This reads as two genuinely separate accreditation tracks — a company can seek Group B (developer-facing) training accreditation, Group D (real-estate-company-facing) accreditation, or both — rather than one row duplicated across two group listings by source error. Treated as distinct here; flagged for client confirmation rather than assumed.

## 1. Service Overview

The **Accreditation of Training Entities (Real Estate Companies)** service accredits an organization as a RERA-recognized provider of real estate training relevant to Group D's professional community, formalized as a signed partnership agreement — identical in shape to Real Estate Developer's own training-accreditation service, but a distinct accreditation specific to real estate service companies.

## 2. Purpose

Accredit organizations able to deliver real estate training relevant to Group D's regulatory ecosystem (brokerage, JOP management, property management), formalized as a signed partnership agreement.

## 3. Description

An organization applies for accreditation by request; a meeting is held; the applicant reviews RERA's proposal; the applicant submits a partnership application; and the parties sign an agreement. The entire process runs over email, not the platform.

## 4. Who Can Apply

An organization seeking accreditation as a real estate training entity for Group D's professional community — not necessarily an existing Group D company account holder, since the process is email-based rather than portal-based.

*Typically filed in practice by the Brokerage Principal*, where the applicant is already a registered Group D company — sourced (row 66). **Proposed**: for non-company applicants, needs client confirmation, matching the same caveat Real Estate Developer's equivalent service carries.

## 5. Prerequisites

* Organizational capacity to deliver real estate training relevant to Group D's domain.
* Willingness to enter a formal partnership agreement with RERA.

## 6. Required Information

* Organization Name and Contact Information
* Proposed Training Scope

## 7. Required Documents

> **Proposed** — not itemized in source beyond the workflow's named steps.

* Organizational Profile / Credentials
* Draft Partnership Proposal

## 8. Service Fee

**None. This service is free.**

Sourced (row 66) — the workflow contains no payment step, matching Real Estate Developer's identical service exactly.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Licensing & Registration Officer** (Group A) — sourced (approver column, row 66).

## 11. Expected Processing Time

**4 business working days.** Sourced from row 66.

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

**Channel:** Email — the only channel sourced, matching Service #6 (No-Objection Letter) as one of two email-only services in Group D, and matching Real Estate Developer's Service #23 exactly.

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

* Signed Agreement — sourced (row 66)

## 16. Related Services

* Service #12 – Real Estate Licensing Application
* Real Estate Developer Service #23 – Accreditation of Training Entities *(cross-module: the near-identical Group B equivalent — see the note under Service Overview above)*

## 17. UI Screens

**Corrected 2026-08-16 — Phase 4 is complete; this section previously said "Not yet built."** Given the sourced email-only channel, this service does not use a portal wizard:

* Services
* Accreditation of Training Entities — static instructional screen, matching the treatment already built for Service #6

## 18. API Requirements

Not applicable in the same sense as portal-based services. **Proposed**: if a portal record of accredited entities is desired, a minimal Accredited Training Entities register would need: Create Accreditation Record, Update Accreditation Status, Retrieve Accredited Entities List. Needs client confirmation of whether this is in scope.

## 19. Database Entities

* Training Entity
* Partnership Agreement
* Accreditation Record

## 20. Acceptance Criteria

* An organization can request accreditation as a training entity for Group D's domain.
* A meeting and proposal review precede a formal partnership application.
* A signed agreement completes the accreditation.

## 21. Business Rules

1. This service runs over email rather than the platform — the same channel as Real Estate Developer's equivalent service.
2. Accreditation is finalized only once the partnership agreement is signed by both parties.
3. This service carries no fee, at any point.
4. **This is treated as a distinct accreditation from Real Estate Developer's Service #23**, not a duplicate — flagged for client confirmation, not assumed.

## Open Questions

1. **Whether this service is genuinely distinct from Real Estate Developer's Service #23, or a source-table duplication of the same underlying accreditation process** — the primary open question, not resolved by this document. Client data.
2. **No portal-based UI screen exists or is proposed for this service**, consistent with its non-portal channel — flagged for the client to confirm scope before any further UI work is considered.
