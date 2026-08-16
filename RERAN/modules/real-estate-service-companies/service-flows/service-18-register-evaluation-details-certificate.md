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
tags:
  - real-estate-service-companies
  - service-flow
  - licensing
  - valuation
---

# Service #18 – Register Real Estate Evaluation Details Certificate

**Service Category:** Real Estate Licensing Services

**Source row:** 65 of `RERAN_service_flows_v2.md`.

> **Provenance flagged — not resolved.** This service's own workflow text reads as a Valuer-facing service (Group G — Allied Professionals & Service Trustees), not a Brokerage-facing one: the acting party "accepts or rejects" a customer's evaluation request and performs the valuation itself, a structurally different shape from every other Group D service, where RERA is always the one accepting or rejecting. Kept in Group D's catalogue per the source table's own group assignment, per `open-questions.md` A2, but documented here with that provenance question unresolved rather than presented as settled. **If reassigned to Group G, this file should move rather than be duplicated.**

## 1. Service Overview

The **Register Real Estate Evaluation Details Certificate** service lets an evaluation company process a customer's property valuation request and issue an evaluation certificate directly through the RERA App — with no RERA regulatory review step described in the sourced workflow at all.

## 2. Purpose

Give an evaluation company a platform through which to receive, assess, and respond to customer valuation requests, issuing a certificate the customer can download once the evaluation is complete.

## 3. Description

The evaluation company signs up and logs in via the evaluation-company option. It views existing applications or prepares a new one on the customer's behalf, accepts or rejects the request, performs the evaluation, adds the evaluation details, value, and notes, and issues the certificate via the app — informing the customer to download it.

## 4. Who Can Apply

**Sourced as the evaluation company itself**, acting on a customer's behalf — not, on this row's own text, a company applying *to RERA* the way every other Group D service works. Any of the company's four Group D roles may act, consistent with the unified-access model, though which role this maps to in practice is unclear given the provenance question above (Brokerage Principal is Group D's licensing-cluster role by convention, but this service's actual actor description — "evaluation company" — doesn't map cleanly onto any of Group D's four defined roles).

## 5. Prerequisites

* Registered evaluation-company account (the specific registration path for this account type is not sourced elsewhere in Group D — possibly a Group G credential, reinforcing the provenance question).
* A customer's valuation request exists or is being prepared on the customer's behalf.

## 6. Required Information

### Customer / Property Information

* Customer Name and Contact Details
* Property Reference / Address

### Evaluation Information

* Evaluation Details
* Evaluation Value
* Notes

Sourced (row 65) at a high level — "add evaluation details, value and notes" — without field-level enumeration.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Customer's Valuation Request
* Property Documentation Supporting the Evaluation
* Other supporting documents, where relevant

## 8. Service Fee

**Not specified in source.** No payment step appears anywhere in row 65's workflow, but unlike Services #16/#17 (explicitly free, cancellation/amendment shape), this row's silence reads more like the same "not itemized" gap several other under-specified Group D rows have.

## 9. Payment Required

**Not specified in source — treated as no, consistent with the workflow's silence, but flagged rather than asserted with full confidence** given the service's own atypical shape (a company-to-customer transaction, not a company-to-RERA one) makes a fee — charged by the evaluation company to its own customer, not to RERA — plausible even though it wouldn't appear in this row's RERA-facing workflow text.

## 10. Processing Authority

**Licensing & Registration Officer** (Group A) — sourced (approver column, row 65), though the workflow text itself describes no RERA review step; the "accept or reject" decision described belongs to the evaluation company, not RERA. **This is the clearest evidence for the provenance question** — RERA's own approver role is named in the source table's structure, but does not appear to act anywhere in the actual described process.

## 11. Expected Processing Time

**Immediate.** Sourced from row 65.

## 12. Processing Workflow

Evaluation Company

Sign Up / Log In via Evaluation Company Option
↓
View Existing Applications, or Prepare New Application on Customer's Behalf
↓
Accept or Reject the Application
↓
*(if accepted)* Perform Real Estate Evaluation
↓
Add Evaluation Details, Value, and Notes
↓
Issue Evaluation Certificate via App
↓
Inform Customer to Download Certificate

*Channel: RERA App — the only channel sourced.*

## 13. Application Status Flow

Draft
↓
Submitted
↓
Accepted / Rejected *(by the evaluation company, not RERA — see Section 10)*
↓
Evaluation in Progress
↓
Completed

### Additional Statuses

* Withdrawn

**Proposed**, given the source's atypical shape — this status flow is inferred from the workflow steps rather than confirmed against a sourced Application Status column, which this row (like most Group D rows) does not separately provide.

## 14. Possible Outcomes

* Evaluation Certificate Issued
* Customer's Request Rejected by the Evaluation Company

## 15. Output

* **Real Estate Evaluation e-Certificate** — sourced (implied by the service name and "issue evaluation certificate via app"), though row 65's own Issued Document column is blank.

## 16. Related Services

* Service #12 – Real Estate Licensing Application
* Financial & Trust Institutions — no direct equivalent; this service's shape (professional-to-customer valuation) is closer to what Group G's Valuer role would perform, per the provenance question above

## 17. UI Screens

Not yet built — Phase 4.

## 18. API Requirements

* Validate Evaluation Company Account
* Retrieve / Create Customer Valuation Request
* Submit Accept / Reject Decision
* Record Evaluation Details
* Generate Evaluation Certificate
* Notify Customer

## 19. Database Entities

* Evaluation Company
* Customer
* Property
* Valuation Request
* Evaluation Certificate
* Audit Log

## 20. Acceptance Criteria

* An evaluation company can view or create a valuation request on a customer's behalf.
* The evaluation company can accept or reject the request.
* An accepted request results in an evaluation and an issued certificate the customer can download.
* All activities are recorded in the audit log.

## 21. Business Rules

1. This service's own workflow describes the evaluation company, not RERA, as the party accepting or rejecting the customer's request — sourced directly, not an inference.
2. Fee treatment is unresolved — see Section 9.
3. Every valuation request and its outcome should be permanently recorded in the audit trail.

## Open Questions

1. **Whether this service genuinely belongs to Group D or to Group G (Allied Professionals — Valuer)** — the primary open question for this service, carried from `open-questions.md` A2. Recommend resolving this before building any UI for it, since the answer changes which module's navigation and role model it should live under.
2. **Fee treatment** — whether the evaluation company charges the customer directly (outside RERA's fee schedule) is not addressed in source.
3. **Registration path for an "evaluation company" account** is not described anywhere in Group D's source rows — possibly a Group G registration flow this module doesn't own.
4. **Required information and document lists are proposed, not sourced beyond the high-level workflow text.**
