---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: extrapolated
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/screens/compliance-reports.md"
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - audit
---

# Feature #6 – Compliance Reports

**Feature Category:** Shared Platform Features – Institution-Specific

> **Newly identified 2026-08-16** during the bottom-up rebuild of this module's shared-features layer — absent from both the original 17-feature list and the externally-drafted document reviewed the same day, where it existed only as a one-line "Reporting / compliance alerts" example under Dashboard. Sourced directly from the Auditing Bureau Officer's documented responsibilities: *"Prepare and submit independent compliance reports to RERA... Raise findings against trust accounts... Open and close audit engagements."*

## 1. Feature Overview

**Compliance Reports** is the institution's workspace for the two things the source says an approved auditor produces: independent compliance reports filed with RERA on a RERA-defined template, and findings raised against trust accounts under the institution's trusteeship.

## 2. Purpose

Give the institution a place to track reporting obligations (what's due, what's overdue), prepare and submit structured compliance reports, and raise, track, and escalate findings against trust accounts — typically the Auditing Bureau Officer's work, but open to any of the four roles.

## 3. Description

Reports and Findings are separated into two tabs, since they're different objects with different lifecycles. A Reporting Obligations panel shows what's due and overdue, since answer A7 establishes reports follow a defined template on a defined cycle — the obligation is knowable in advance rather than something to remember. New reports are built through a structured Report Composer (header, per-account sections with opening/closing balance and reconciliation state, attached findings, auditor declaration, attachments), not a document upload — matching the same structured-over-freeform reasoning used for escrow milestone certification. A **Material** finding on an active trust account sets that account to Flagged on Trust Accounts.

## 4. Used By

Not one of the 18 numbered Group C services — a standing institutional obligation covering all trust accounts under the institution's trusteeship, distinct from and not gating any of the 18 services' own workflow.

## 5. Prerequisites

* User is logged into a verified institution account.
* At least one trust account exists under the institution's trusteeship, for findings; a reporting obligation must be due, for reports.

## 6. Required Information

**Reports:** report type (Periodic escrow audit / Trust account statement / Ad hoc compliance report), period covered, scope (which trust accounts or projects).

**Findings:** trust account, project, category (Irregular movement / Milestone evidence / Documentation / Balance discrepancy / Other), severity (Observation / Concern / Material).

## 7. Required Documents

Supporting working papers, attached to a report via the Report Composer's Attachments section.

## 8. Service Fee

No fee — not a chargeable service.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Any of the institution's four Group C roles**, unrestricted. **Corrected 2026-08-15**: previously gated behind an `audit` permission scope, with an audit-exclusivity rule barring a user holding `audit` from also holding `escrow` or `certify`. Both are retired — there is no scope combination left to prohibit. Typically the Auditing Bureau Officer's work in practice, not a restriction.

## 11. Expected Processing Time

Report preparation and finding creation are user-paced. **Reporting cycle is unresolved** — answer A7 confirms a RERA-defined template but not the filing frequency; the Reporting Obligations panel is built against a configurable cycle, not a sourced figure.

## 12. Processing Workflow

**Reports**

Dashboard → Compliance Reports → New Compliance Report → Report Composer (Header → Account Sections → Findings → Auditor Declaration → Attachments → Review & Submit) → Submitted to RERA

**Findings**

Compliance Reports → Raise Finding → Finding Detail → Open / Escalate

## 13. Application Status Flow

**Reports:** Draft → Submitted → Under RERA Review → Accepted / Returned. Submitted reports are immutable; a correction is a new report referencing the original.

**Findings:** Open → Under Response → Resolved, or Open → Escalated (referred to RERA). A Material finding on an active account also sets that account to Flagged, independently of the finding's own status.

## 14. Possible Outcomes

* Report Submitted / Accepted / Returned
* Finding Raised / Resolved / Escalated
* Trust Account Flagged *(consequence of a Material finding)*

## 15. Output

* Submitted compliance report, downloadable, referencing covered accounts
* Finding record, with severity and escalation status
* Account Detail Panel (on Trust Accounts) updated with the new finding

## 16. Related Features

* Trust Accounts *(the register findings are raised against; View Covered Accounts)*
* Escrow Request Queue *(escrow audit here concerns developer trust accounts, distinct from RERA's own audit of the institution)*

## 17. UI Screens

* Compliance Reports (Reporting Obligations, Reports tab, Findings tab, Report Composer)

## 18. API Requirements

* Retrieve Reporting Obligations
* Retrieve Reports / Findings
* Submit Compliance Report
* Raise / Escalate Finding
* Retrieve Covered Trust Accounts
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Institution, Institution Staff, User
* Compliance Report, Reporting Obligation
* Finding
* Trust Account *(cross-referenced from Feature #5)*
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can prepare, edit, and submit a report or finding.
* A report cannot be submitted while an unresolved Material finding in its period exists, unless explicitly carried into the report.
* The auditor declaration is mandatory before submission.
* Submitted reports are immutable; corrections are new reports referencing the original.
* A Material finding on an active account sets that account to Flagged.
* All report and finding activity is recorded in the audit log, including the acting user's role.

## 21. Business Rules

1. Reports and findings are separate objects with separate lifecycles, not merged into one list.
2. Any of the institution's four Group C roles may create, edit, or submit a report or finding — no scope restriction, and no exclusivity rule barring a user from also working escrow or certification.
3. A report is structured through the Report Composer, not a free-form document upload.
4. The auditor declaration is mandatory before submission.
5. Submitted reports are immutable; a correction is filed as a new report.
6. A Material finding on an active trust account sets that account to Flagged — the only way an account reaches that status.
7. All activity is permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. What is the concrete reporting cycle behind "periodic"? Answer A7 confirms a RERA-defined template, not a frequency.
2. Does RERA gate institutional approval renewal (Institution Profile) on reporting compliance? A client question, not resolved here.
3. `services-overview.md` To Confirm item 2 remains open and covers this feature too.
