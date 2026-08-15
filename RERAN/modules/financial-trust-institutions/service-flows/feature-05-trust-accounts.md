---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: extrapolated
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/screens/trust-accounts.md"
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - escrow
---

# Feature #5 – Trust Accounts

**Feature Category:** Shared Platform Features – Institution-Specific

> **Newly identified 2026-08-16** during the bottom-up rebuild of this module's shared-features layer — absent from both the original 17-feature list and the externally-drafted document reviewed the same day. Sourced directly from the Account Trustee's documented responsibility: *"Maintain the register of trust accounts under management"* (`roles-and-responsibilities.md`), distinct from processing the intake queue (Feature #4).

## 1. Feature Overview

**Trust Accounts** is the institution's register of every trust account under its trusteeship — what exists, whether its periodic statement is current, and whether it carries an audit flag. It is the object Escrow Request Queue draws requests against and Compliance Reports covers; this feature is where an account itself lives, not where activity against it is processed.

## 2. Purpose

Give the institution a standing register of trust accounts, separate from the transactional queue of requests against them, so account-level state (balance, statement currency, audit status) is visible independent of any single pending request.

## 3. Description

Any institution user can view the register, open an account's Detail Panel (particulars, statement history, linked escrow requests, findings, audit history), file a periodic statement, or open/close an audit engagement against an account. An account reaches **Flagged** status only through a Material finding raised on Compliance Reports — there is no manual "flag" action here, keeping the flag traceable to a specific finding rather than settable at will.

## 4. Used By

Not one of the 18 numbered Group C services — the register underlying Real Estate Developer's escrow services and this module's own Escrow Request Queue and Compliance Reports features.

## 5. Prerequisites

* User is logged into a verified institution account.
* At least one trust account exists under the institution's trusteeship (accounts appear once escrow activity for a project routes through the institution).

## 6. Required Information

Search/filter by: Account reference · Project · Developer · Statement filing state (Current / Due Soon / Overdue).

## 7. Required Documents

Periodic statements, uploaded via File Statement. Statement filing does not require the account to be Active — filing a statement is the action that clears an Overdue state.

## 8. Service Fee

No fee — this is a register, not a chargeable service.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Any of the institution's four Group C roles**, unrestricted. **Corrected 2026-08-15**: previously gated File Statement behind `escrow` and Mark Under Audit behind `audit`; both scopes are retired. Typically maintained by the Account Trustee (register, statements) and the Auditing Bureau Officer (audit engagements) in practice — not a restriction.

## 11. Expected Processing Time

Register and account detail retrieval is immediate. Statement filing frequency ("periodic") has no concrete cycle given in source — not sourced, flagged as a gap.

## 12. Processing Workflow

Escrow Request Queue / Compliance Reports / Dashboard
↓
Open Trust Accounts
↓
Search / Filter / Sort (default: statement due date)
↓
View an Account → Account Detail Panel
↓
File Statement (clears Overdue) **or** Mark Under Audit (opens an audit engagement) **or** View Escrow Requests / Findings

## 13. Application Status Flow

Pending Activation → Active
↓
*(ongoing)* Statement Current ↔ Statement Overdue *(cleared by filing)*
↓
Under Audit *(opened/closed via Compliance Reports engagement)*
↓
Flagged *(only via a Material finding — no manual trigger)*
↓
Suspended *(set by RERA, blocks new certifications against the account)*

**Account activation (Pending Activation → Active) is not specified in source** — who triggers it and what evidence is required is an open gap, not assumed here.

## 14. Possible Outcomes

* Statement Filed, Overdue State Cleared
* Audit Engagement Opened / Closed
* Account Flagged *(via a Material finding elsewhere)*
* Account Suspended *(by RERA — blocks new certifications, remains visible)*

## 15. Output

* Statement History entry (date, filer, document link)
* Audit History entry (engagement opened/closed, distinct from any findings it produced)
* Findings list (open and resolved, cross-referenced with Compliance Reports)

## 16. Related Features

* Escrow Request Queue *(the transactional side — View Trust Account row action)*
* Compliance Reports *(findings that can flag an account; View Covered Accounts)*

## 17. UI Screens

* Trust Accounts (register + Account Detail Panel)

## 18. API Requirements

* Retrieve Trust Accounts Register
* Retrieve Account Detail (particulars, statement history, linked requests, findings, audit history)
* Submit Statement Filing
* Open / Close Audit Engagement
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Institution, Institution Staff, User
* Trust Account, Statement
* Audit Engagement
* Finding *(cross-referenced from Compliance Reports)*
* Escrow Request *(cross-referenced from Feature #4)*
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can view the register, file a statement, and open/close an audit engagement on any account.
* An account's Flagged status is set only by a Material finding, never a direct action on this screen.
* A Suspended account blocks new escrow certifications against it (enforced on Escrow Request Details, not duplicated here) but remains visible and filterable.
* Statement filing is possible regardless of the account's current status, and clears an Overdue state.
* All register access, statement filing, and audit-engagement activity is recorded in the audit log.

## 21. Business Rules

1. An account reaches Flagged only through a Material finding raised on Compliance Reports — no manual flag action exists.
2. A Suspended account blocks new escrow requests being certified against it, but stays visible in the register.
3. Statement filing does not require an Active status — it is the action that clears Overdue.
4. Any of the institution's four Group C roles may file a statement or open/close an audit engagement — not restricted to the Account Trustee or Auditing Bureau Officer by title.
5. Account activation criteria are not specified in source and are not assumed here.
6. All register activity is permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. What triggers account activation (Pending Activation → Active), and what evidence is required? Not specified in source.
2. What is the concrete statement filing cycle behind "periodic"? Not given by any answer — same gap Compliance Reports flags for reporting cycle generally.
3. `services-overview.md` To Confirm item 2 remains open and covers this feature too.
