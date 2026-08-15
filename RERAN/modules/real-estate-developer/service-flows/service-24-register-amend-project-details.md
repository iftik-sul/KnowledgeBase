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
  - "RERAN/modules/real-estate-developer/ui/screens/project-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registration-details.md"
tags:
  - real-estate-developer
  - service-flow
  - title-deed-data-services
---

# Service #24 – Registration/Amendment of Real Estate Project Details

**Service Category:** Title Deed Data Services

## 1. Service Overview

The **Registration/Amendment of Real Estate Project Details** service issues title-deed-level data for a project — an Electronic Certificate of Title / Title Deed where the project is completed, or an Electronic Map where it is not — reflecting the project's current, detailed data with RERA's Title Deed Data function rather than the general project-registration workflow.

> **Near-duplicate concern with rows 4, 5, 16, 17 — resolved 2026-08-15 (issue #37).** Checked against each of those services' own files rather than the master table's row summaries alone: **#4 and #5 act on a provisional *transaction* registration** (Services #1–#3's individual sale/rent-to-own/usufruct records), not the project record — a different object from this service entirely. **#17 (Re-registration)** is a redo-after-lapse trigger (committee resolution, notice period, fresh unit upload, new Registrar account), not ongoing maintenance — a different trigger from this service's. Neither is a genuine duplicate.
>
> **#16 (Rename) is the one real overlap, and the client has confirmed both routes are valid for a name change** — a developer may use the narrow, no-fee Rename Project service, or include the name among the fields changed here. Neither is the sole correct path; whichever the developer selects is what's recorded.

## 2. Purpose

Keep the Title Deed data record for a project current, issuing the completion-appropriate title document as project data changes.

## 3. Description

The developer submits updated project details. RERA's Compliance & Escrow Auditor function reviews. On approval, the output depends on the project's completion status: a completed project receives an Electronic Certificate of Title / Title Deed; an uncompleted project receives an Electronic Map.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Project Registration Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* An existing registered project (Service #13).
* Updated project detail data to register or amend.

## 6. Required Information

* Project Reference Number
* Project Completion Status
* Updated Project Detail Fields — **may include the project name**, per the confirmed overlap with Service #16 (see Section 1)

## 7. Required Documents

> **Proposed** — not itemized in the source. Needs client confirmation.

* Supporting Evidence for the Updated Details
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule. Paid through the shared platform payment gateway, per transaction. There is no standing or pre-funded RERA-fee account for developers; each application is paid for on its own.

## 9. Payment Required

**Yes — in two stages, one before RERA's decision and one after.** Uniquely among the 27, this service's source row contains two distinct payment steps: an *application approval fee* paid before the Survey Department reviews, and an *approval fee in the real estate records* paid after approval and before the output is issued. Both are charged per transaction through the shared platform payment gateway. Neither stage may be collapsed into the other.

> **Who tenders the first payment is not settled by the source.** The row reads "Pay application approval fees **and send from survey company to Survey Department**," which attributes the transmission — and possibly the payment itself — to the developer's designated survey company rather than to the developer directly. The workflow below documents it as a developer-side gateway payment, since that is the only payment route this module has; whether the survey company pays on the developer's behalf, or merely forwards an application the developer has already paid for, is **proposed** and needs client confirmation. The second payment is unambiguously the developer's.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**5 business days**

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Open Project Record
↓
Select "Register/Amend Project Details"
↓
Enter Updated Details
↓
Pay Application Approval Fee via Payment Gateway
↓
Submit Application Online
↓
RERA Reviews Application
↓
Pay Approval Fee in Real Estate Records via Payment Gateway
↓
If Project Completed: Electronic Certificate of Title / Title Deed Issued
↓
If Project Not Completed: Electronic Map Issued

## 13. Application Status Flow

Draft
↓
Application Fee Pending
↓
Application Fee Paid
↓
Submitted
↓
Under Review
↓
Approved
↓
Approval Fee Pending
↓
Approval Fee Paid
↓
Issued

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Title Deed Data Successfully Registered/Amended
* Additional Information Requested
* Application Rejected

## 15. Output

* Electronic Certificate of Title / Title Deed (completed project)
* Electronic Map (uncompleted project)

## 16. Related Services

* Service #4 – Amend Initial Procedures Data *(different object — acts on a transaction registration, not this project record; see Section 1)*
* Service #5 – Complete Initial Procedures Data *(different object — same reasoning as #4)*
* Service #16 – Changing the Name of a Real Estate Project *(confirmed overlap — either route may be used for a name change; see Section 1)*
* Service #17 – Project Re-registration *(different trigger — redo-after-lapse, not ongoing maintenance; see Section 1)*
* Service #13 – Registration of Real Estate Project

## 17. UI Screens

* Project Details **or** Property Registration Details *(unresolved — see Section 1)*
* Payment
* Application Submitted

## 18. API Requirements

* Retrieve Project
* Submit Project Details Registration/Amendment
* Determine Project Completion Status
* Retrieve Application Status
* Calculate Application Approval Fee
* Calculate Records Approval Fee
* Initiate Payment
* Verify Payment
* Generate Electronic Certificate of Title
* Generate Electronic Map
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Title Deed Record
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can submit project details for registration or amendment against an existing project.
* System determines the project's completion status to select the correct output document.
* Approved submissions generate the completion-appropriate title document.
* All activities are recorded in the audit log.
* The application approval fee is completed before Survey Department review, and the approval fee in the real estate records after approval and before the output is issued.

## 21. Business Rules

1. Only a registered project's details may be registered/amended under this service.
2. The output document depends on the project's completion status at time of approval.
3. **A name change may be submitted through this service or through Service #16 — client-confirmed 2026-08-15, issue #37.** Neither is the exclusive path; whichever the developer selects is what's recorded.
4. All submissions, reviews, and notifications must be permanently recorded in the audit trail.
