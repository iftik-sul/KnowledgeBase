---
project: RERAN
module: financial-trust-institutions
type: overview
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - workflow
---

# Financial & Trust Institutions Role Workflows

The linear path each role takes through the system, from login to logout. These describe the user's route, not the interface — screen-level detail lives in [ui/screens/](ui/screens/), and access rules in [navigation.md](navigation.md).

**Proposed.** Group C's roles are described in the source; their post-login journeys are not.

**One difference from the other modules:** a Group C journey is not fully determined by role. The internal certification gate is a permission scope (answer A1), so a user's route forks on whether they hold `certify` — and there is a certification path that belongs to no role at all. Those forks are set out after the four role journeys.

---

## Mortgage Officer

The highest-volume role in the module.

```
Login
↓
View Dashboard
↓
Start Service Request
↓
Select Service & Property
↓
Enter Transaction Particulars
↓
Attach Supporting Documents
↓
Submit to Internal Certification
↓
Track Application Status
↓
Respond to RERAN Information Requests
↓
Confirm Settlement & Retrieve Output Document
↓
Logout
```

### Primary Services

* Mortgage lifecycle — registration, amendment, transfer, release (#3–#7)
* Finance lease lifecycle — registration, amendment, transfer, release (#8–#11)
* Fund company registration (#12)
* Title and ownership transactions where bank-originated (#13–#17)

### Note

The officer does not settle fees — that requires the `settlement` scope. They see whether their own approved transaction can clear, and are directed to the Relationship Manager where it cannot. Per answer B1, settlement happens after approval, so the journey does not end at submission.

---

## Institution Relationship Manager

Maintains the institution's standing and the people acting under it.

```
Login
↓
View Dashboard
↓
Review Approval Standing & Expiry
↓
Monitor Settlement Position
↓
Settle Approved Transactions
↓
Fund Settlement Account
↓
Manage Staff & Permission Scopes
↓
Submit Approval Renewal (#1) or Cancellation (#2, #18)
↓
Review Institution-Wide Outcomes
↓
Logout
```

### Primary Services

* Institutional approval and renewal (#1)
* Approval cancellation (#2)
* Contract cancellation (#18)
* Settlement account funding and settlement
* Staff provisioning and scope management
* Institution-wide oversight

### Note

This is the only role whose journey is driven by deadlines rather than inbound work — approval expiry and settlement expiry both run on countdowns, and both block other people's work when missed.

---

## Account Trustee

Works inbound escrow requests from the developer module. Owns none of the eighteen Group C services.

```
Login
↓
View Dashboard
↓
Open Escrow Request Queue
↓
Assess Solvency & Milestone Evidence
↓
Upload Supporting Assessment
↓
Certify, Return, or Request Information
↓
Forward to RERAN Escrow Audit
↓
Execute Approved Transfer
↓
Maintain Trust Account Register & File Statements
↓
Logout
```

### Primary Services

* Account activation, account transfer, profit withdrawal, payment release, mortgage deposit and bank guarantee cancellation — all routed from Group B
* Milestone certification
* Trust account register maintenance and periodic audited statements

### Note

Answer A2 confirms from source rows 8–12 that this work happens inside the platform — the Trustee studies capability, uploads documents and sends them on — not externally with an outcome recorded afterwards. The SLA governing the assessment step remains open (answer A6).

---

## Auditing Bureau Officer

Independent assurance over trust accounts under the institution's trusteeship.

```
Login
↓
View Dashboard
↓
Review Reporting Obligations
↓
Examine Trust Accounts & Statements
↓
Raise Findings
↓
Prepare Compliance Report
↓
Submit to RERAN
↓
Escalate Material Findings
↓
Logout
```

### Primary Services

* Independent compliance reporting to RERAN
* Escrow audit of developer trust accounts
* Findings and escalation

### Note

**This role's definition has been corrected.** `roles-and-responsibilities.md` §4 previously listed internal certification of the Mortgage Officer's filings as its first responsibility. Answer A1 supersedes that — certification is a `certify` scope, not this role — and the roles document was fixed to match in the issue #27 pass. The journey above already reflected the corrected definition; it was written that way before the source document caught up.

---

## Scope-Driven Variations

These are not roles. Any delegated staff member may hold them, and holding one inserts a step into that person's journey.

### Certifier scope (`certify`)

```
Login
↓
View Dashboard (certification count visible regardless of role)
↓
Open Internal Certification Queue
↓
Review Request & Attached Documents
↓
Certify → routes to RERAN
   or Return by Certifier → back to the filer with mandatory reason
↓
Logout
```

A user cannot certify a record they filed. A Mortgage Officer holding `certify` therefore has two distinct routes through the system depending on whose record they are looking at.

### Settlement scope (`settlement`)

Inserts *Fund Settlement Account* and *Settle Approved Transactions* into the holder's journey. Normally the Relationship Manager, but separable.

### Admin scope (`admin`)

Inserts *Manage Staff & Permission Scopes* and *Renew Institutional Approval*.

---

## The Shape All Four Share

Every Group C journey crosses two gates: internal certification inside the institution, then external audit at RERAN. No role completes a regulated action alone.

For the Mortgage Officer and the Relationship Manager, the first gate sits between their work and RERAN's. For the Account Trustee, the developer's request has already passed its own institution's checks, and the Trustee *is* a gate. For the Auditing Bureau Officer, the work is assurance over gates other people operated — which is why the `audit` scope is exclusive of `escrow` and `certify`.
