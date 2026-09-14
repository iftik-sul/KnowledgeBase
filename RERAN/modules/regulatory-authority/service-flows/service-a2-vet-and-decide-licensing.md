---
project: RERAN
module: regulatory-authority
type: service-flow
status: draft
contains_proposals: true
source_type: derived
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/services-overview.md"
  - "RERAN/modules/regulatory-authority/touchpoint-register.md"
  - "RERAN/modules/regulatory-authority/service-flows/service-a1-audit-and-decide.md"
  - "RERAN/modules/real-estate-developer/service-flows/ (services #22, #23)"
  - "RERAN/modules/real-estate-service-companies/service-flows/ (services #12–17, #19)"
tags:
  - regulatory-authority
  - service-flow
  - back-office
  - decision-service
  - licensing
---

# Group A Service A-2 — Vet & Decide (Licensing)

> **Back-office service.** Follows the reviewer-side template established by A-1
> (Audit & Decide). Sections that don't apply to a reviewer are marked N/A with the
> reason; reviewer-specific sections (who may act, the review checklist, service
> variants) are retained. Read A-1 first for the shared conventions.

## 1. Service Overview

**Vet & Decide** is Group A's licensing decision service. It is the review-and-decision
workflow that finishes the **9 licensing services** — the licences, permits,
professional practice cards, and training-entity accreditations that developers and
service companies need before they can operate. A Licensing & Registration Officer
vets each application against eligibility criteria and the National Practitioner
Register, records a decision, and — on approval — issues the credential and updates the
register.

Where A-1 decides *transactions*, A-2 decides *standing* — who is permitted to operate
in the sector.

## 2. Purpose

Give RERA a single, consistent gate for market entry: one place where every applicant
for a licence, permit, card, or accreditation is checked against the same eligibility
rules and recorded in the same national register, so the register stays authoritative
and every credential is traceable to a decision.

## 3. Description

A licensing application (or a card renewal, amendment, or cancellation) arrives. A
Licensing & Registration Officer opens it, checks the applicant's credentials and
supporting documents against the eligibility rules and the existing register, and
records a decision: approve, request more information, return, or reject. On approval
the system issues the credential (e-licence, permit, practice card, or accreditation)
and writes or updates the practitioner register entry.

Three of the nine items don't follow the plain queue-review shape — two are automatic
approvals and two are handled through an off-platform meeting-and-agreement process.
See §15.

## 4. Who Can Act *(replaces "Who Can Apply")*

**Licensing & Registration Officer** (Group A), under real RBAC + MFA — the same
permission-gated model as A-1 (the one place role gates action in RERAN). Only a user
holding this role may act on a licensing item.

## 5. Entry Conditions *(replaces "Prerequisites")*

- An originating licensing service has been submitted and paid, and has reached the
  status that routes it into review.
- For the accreditation variant (§15c): the off-platform meeting stage has produced a
  signed partnership application to be recorded.
- The acting officer is authenticated (MFA) and holds the Licensing & Registration
  Officer role.

## 6. What the Reviewer Sees *(replaces "Required Information")*

- The full application as submitted (all fields).
- All uploaded supporting documents (credentials, qualifications, company records).
- The applicant's existing entry in the National Practitioner Register, if any.
- The originating service's identity and its expected credential output and SLA.

## 7. Review Checklist *(replaces "Required Documents")*

**General (all licensing items):**
- The applicant's identity and, for companies, corporate standing are valid.
- The claimed qualifications / credentials meet the eligibility rules for the
  credential sought.
- Supporting documents are present, legible, and consistent.
- The application does not conflict with an existing register entry (e.g. a duplicate
  or already-cancelled credential).

> **Proposed** — the specific eligibility rules per credential type are not itemised in
> the current source beyond "vets and approves"; they need client confirmation against
> RERA's actual licensing criteria.

## 8. Service Fee

**N/A.** Group A charges no fee for vetting. The applicant paid the originating
service's fee before submission (several licensing services are free at source; that
belongs to their own flows).

## 9. Payment Required

**N/A (Group A side).** This service never collects or holds a payment.

## 10. Decision Authority & Access Control *(replaces "Processing Authority")*

- **Role:** Licensing & Registration Officer (Group A).
- **Access control:** RBAC-gated + MFA.
- **Sub-system:** Licensing & Registry Engine.

## 11. Expected Processing Time

**Inherited from the originating service.** Most licensing items are quick (minutes for
cards, licences, and permits); accreditation runs to several business days; the
auto-approval variant is immediate. Measured per-item against the originating SLA (see
touchpoint-register.md).

## 12. Processing Workflow

```
Item enters queue  (submitted + paid)
        ↓
Officer opens item  (RBAC + MFA)
        ↓
Vet credentials + documents against eligibility rules
        ↓
Check against the National Practitioner Register
        ↓
Decide  ──────────────┬───────────────┬──────────────┬───────────────┐
        ↓             ↓               ↓              ↓
     Approve   Request Information   Return      Reject
        ↓             ↓               ↓              ↓
 Issue credential  Back to        Back to       Close (terminal)
 + update register applicant      applicant
        ↓
Write decision + actor to audit trail  (every branch)
```

## 13. Application Status Flow *(shared vocabulary — do not localise)*

Uses the same shared platform status vocabulary as A-1 §13:

```
Under Review
   ↓
Information Requested   → (applicant responds) → Under Review
   ↓
Returned               → (applicant corrects) → Under Review
   ↓
Approved   /   Rejected
```

## 14. Possible Outcomes

- **Approved** — the credential is issued and the register updated.
- **Additional Information Requested** — returned to the applicant; re-enters the queue.
- **Returned** — sent back for correction.
- **Rejected** — terminal.

## 15. Service Variants *(back-office-specific section)*

The 9 licensing services take three shapes:

**15a. Standard review (queue decision)** — RED #22; RESC #12, #13, #14, #16. The plain
loop of §12: vet, check register, decide, issue. (Cancellation, RESC #16, is a
lightweight review that removes a register entry rather than issuing one.)

**15b. Automatic approval** — RESC #15 (renew practice card), #17 (amend practice card).
The source marks these auto-approve: the system issues/updates the credential without a
manual decision, and this service records the officer as system-of-record authority
rather than reviewing. No queue item is raised.

> **Proposed** — retaining the officer as system-of-record on auto-approvals is a
> modelling choice (consistent with how source attributes an approver to every row);
> needs client confirmation.

**15c. Accreditation by meeting & agreement (off-platform)** — RED #23; RESC #19. These
are not a portal queue decision. The source flow is: applicant requests by email → a
meeting is held → the applicant reviews RERA's proposal → submits a partnership
application → an agreement is signed. This service's role is to **record** the outcome
of that negotiated process (accredited / declined) and update the register — not to run
a standard review. The negotiation itself happens outside the platform.

> **Proposed** — how much of the meeting/agreement process the platform records vs.
> leaves entirely off-system needs client confirmation.

## 16. Cross-Module Dependencies *(back-office-specific section)*

1. **National Practitioner Register consistency.** A-2 is the only writer of the
   register; every other service that verifies a practitioner (e.g. front-office
   verification lookups) reads what A-2 writes. Its issue/renew/amend/cancel actions
   must keep the register authoritative.
2. **Shared status vocabulary (§13).** As with all Group A services.
3. No FTI handshake and no escrow two-gate apply to A-2.

## 17. Related Services

- **A-6 Provision & manage access (RBAC)** — must exist before this service can be used.
- **The 9 originating licensing services** — RED #22, #23; RESC #12–17, #19 (see
  touchpoint-register.md).

## 18. UI Screens

- **Queue / worklist** — pending licensing items, filterable by credential type and
  status. (Auto-approval items, 15b, don't appear here.)
- **Application detail / review** — credentials, documents, and the applicant's register
  entry in one view.
- **Decision panel** — the four-outcome control with a mandatory reason field.
- **Register view** — the National Practitioner Register (read + the entries this
  service writes).
- **Accreditation record** — a lightweight form to record the outcome of the
  off-platform meeting process (15c).

## 19. API Requirements

- Fetch queue (filtered, paginated)
- Fetch application detail + documents
- Fetch practitioner register entry
- Record decision (approve / request-info / return / reject) with actor + reason
- Issue / renew / amend / cancel credential + write register entry
- Record accreditation outcome *(variant 15c)*
- Notify applicant
- Write audit-log entry

## 20. Database Entities

- Application *(shared with originating module)*
- Review / Decision *(actor, outcome, reason, timestamp)*
- Practitioner Register Entry *(new — the register this service maintains)*
- Credential *(licence / permit / practice card / accreditation)*
- Staff User + Role + Permission *(RBAC)*
- Audit Log
- Notification

## 21. Acceptance Criteria

- Only a Licensing & Registration Officer with MFA can open or decide a licensing item.
- Every item shows the application, its documents, and the applicant's register entry.
- The officer can record exactly one of the four outcomes; a reason is mandatory for
  request-info / return / reject.
- Approval issues the correct credential and writes/updates the register entry.
- Cancellation removes or deactivates the register entry.
- Auto-approval items (15b) issue the credential without raising a manual queue item.
- The accreditation record (15c) captures the negotiated outcome and updates the
  register.
- Every decision, with actor and reason, is written to the audit trail.
- Status transitions use only the shared vocabulary of §13.

## 22. Business Rules

1. Access is role-gated (Licensing & Registration Officer) + MFA.
2. A credential may not be issued unless the eligibility checks of §7 pass.
3. This service is the sole writer of the National Practitioner Register.
4. Auto-approval items still record an accountable officer as system-of-record.
5. Every outcome except plain approval requires a recorded reason.
6. All decisions are permanently recorded in the audit trail with the acting officer.
7. Status words are the shared platform vocabulary (§13).
