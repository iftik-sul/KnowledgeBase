---
project: RERAN
module: financial-trust-institutions
type: workflow
status: draft
updated: 2026-08-14
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/modules/financial-trust-institutions/navigation.md"
tags:
  - financial-trust-institutions
  - workflow
---

# Financial & Trust Institutions Role Workflows

The path any user of a Group C institution account takes through the system, from login to logout. This describes the user's route, not the interface — screen-level detail lives in [ui/screens/](ui/screens/), access rules in [navigation.md](navigation.md).

**Proposed.** Group C's roles are described in the source; the post-login journey below is not — it is reconstructed from the services and screens this module documents.

**Confirmed 2026-08-14: access is unified, not role-gated.** Any of the four roles can perform any action in this module — service requests, internal certification, escrow requests, compliance reporting, settlement, staff records. Because of that, this document no longer describes four separate role-bound journeys. What follows is **one shared journey** covering the full range of actions available in the module. The per-role notes after it describe what each role *typically* does in practice — useful for context and for reading the audit trail — but they are **descriptive, not access-restrictive**: nothing stops a Mortgage Officer from certifying a record, or an Auditing Bureau Officer from filing a service request.

---

## The Shared Journey

```
Login
↓
View Dashboard
↓
[ Any of the following, in any order, any number of times, by any role: ]

   Service Request
   Start Service Request → Select Service & Property → Enter Transaction Particulars →
     Attach Supporting Documents → Submit to Internal Certification

   Internal Certification
   Open Internal Certification Queue → Review Request & Attached Documents →
     Certify → routes to RERAN Transaction Audit
     or Return → back to the filer with mandatory reason
   (No maker ≠ checker restriction: the acting user may certify a record they themselves filed.)

   Escrow Request (routed from Group B)
   Open Escrow Request Queue → Assess Solvency & Milestone Evidence →
     Upload Supporting Assessment → Certify, Return, or Request Information →
     Forward to RERAN Escrow Audit → Execute Approved Transfer

   Institutional Standing
   Review Approval Standing & Expiry → Submit Approval Renewal (#1) or Cancellation (#2, #18)

   Settlement
   Monitor Settlement Position → Fund Settlement Account → Settle Approved Transactions

   Compliance Reporting
   Review Reporting Obligations → Examine Trust Accounts & Statements → Raise Findings →
     Prepare Compliance Report → Submit to RERAN → Escalate Material Findings

   Trust Account Register
   Maintain Trust Account Register & File Periodic Statements

   Staff Records
   Manage Staff Records (contact/attribution details only — there are no scopes left to provision)

↓
Track Application Status / Respond to RERAN Information Requests
↓
Confirm Settlement & Retrieve Output Document (where applicable)
↓
Logout
```

Every branch is reachable by every logged-in user of the institution account. Which branches a given person actually uses is a matter of their role in practice, described below — not a system restriction.

---

## What Each Role Typically Does

### Mortgage Officer

The highest-volume role in the module, in practice.

* Mortgage lifecycle — registration, amendment, transfer, release (#3–#7)
* Finance lease lifecycle — registration, amendment, transfer, release (#8–#11)
* Fund company registration (#12)
* Title and ownership transactions where bank-originated (#13–#17)

### Institution Relationship Manager

Typically maintains the institution's standing and its people, in practice.

* Institutional approval and renewal (#1)
* Approval cancellation (#2)
* Contract cancellation (#18)
* Settlement account funding and settlement
* Staff records and institution-wide oversight — no longer "permission scopes" to provision, since scopes are retired; see the note below
* Institution-wide oversight of outcomes

### Account Trustee

Typically works inbound escrow requests from the developer module.

* Account activation, account transfer, profit withdrawal, payment release, mortgage deposit and bank guarantee cancellation — all routed from Group B
* Milestone certification
* Trust account register maintenance and periodic audited statements

Answer A2 confirms from source rows 8–12 that this work happens inside the platform — the Trustee studies capability, uploads documents and sends them on — not externally with an outcome recorded afterwards. The SLA governing the assessment step remains open (answer A6). This is descriptive of typical practice, not an access restriction: under the unified model, any of the four roles can act on an escrow request.

### Auditing Bureau Officer

Typically provides independent assurance over trust accounts under the institution's trusteeship.

* Independent compliance reporting to RERAN
* Escrow audit of developer trust accounts
* Findings and escalation

**This role's definition was corrected once already**, per answer A1 (see [roles-and-responsibilities.md](roles-and-responsibilities.md) for the full history) — to remove internal certification of Mortgage Officer filings from its responsibilities, on the grounds that certification was a `certify` scope, not this role. That correction is itself now superseded by the 2026-08-14 unified-access decision: there is no `certify` scope any more, only an action any of the four roles may take, attributed by role in the audit trail. The practical upshot for this role is unchanged (it typically doesn't certify Mortgage Officer filings) — but the *reason* is different: not because it lacks a scope, but because certification isn't gated by role or scope at all, for anyone.

---

## Superseded By This Document

Until 2026-08-14, this document described four fully separate role journeys, plus a "Scope-Driven Variations" section in which holding the `certify`, `settlement`, or `admin` permission scope inserted extra steps into a person's journey, and a user's route forked depending on whether they held `certify` for the specific record they were looking at. That forking model is retired along with the scopes themselves. See [navigation.md](navigation.md) for the confirmed unified-access model this document now follows.
