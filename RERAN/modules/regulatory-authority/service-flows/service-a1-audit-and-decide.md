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
  - "RERAN/modules/regulatory-authority/roles-and-actions-analysis.md"
  - "RERAN/modules/*/service-flows/ (the 92 originating front-office services)"
tags:
  - regulatory-authority
  - service-flow
  - back-office
  - decision-service
---

# Regulatory Authority Service A-1 — Audit & Decide (Application Review)

> **Back-office service.** This is a Regulatory Authority service — an action RERA staff take on
> work another group filed, not an application an end user submits. Where the standard
> (front-office) service-flow template describes a *submission*, this one describes a
> *decision*. Sections that don't apply to a reviewer (service fee, applicant payment)
> are marked N/A with the reason; sections specific to a reviewer (who may act, the
> review checklist, the escrow variant) are added.

## 1. Service Overview

**Audit & Decide** is the Regulatory Authority's core decision service. It is the single
review-and- decision workflow through which **92 of the 114 external services** reach
their outcome. When an applicant in another group (RED, FTI, RESC, or Individual User)
submits and pays for a service, the application lands in this service's queue; a
Compliance & Escrow Auditor reviews it against the registry and records one of four
decisions. Every property, sale, lease, mortgage, financial-institution, and escrow-
account filing on the platform is finished here.

It covers two channels handled by the same action: the **Transaction Audit Queue**
(79 general services) and the **Escrow / Trust-Account Audit** (13 escrow-apparatus
services). These are one service with a documented escrow variant (see §15), not two.

## 2. Purpose

Give RERA a single, consistent, auditable decision process for the bulk of the
platform's regulated transactions — so that every applicant is reviewed against the
same registry checks and the same four outcomes, and every decision is permanently
recorded and attributable to a named officer.

## 3. Description

A submitted, paid application arrives in the queue. A Compliance & Escrow Auditor
opens it, reviews the application data and uploaded documents, verifies them against
the platform registry (that the developer/project/property/title/applicant are valid
and consistent), and records a decision: approve, request more information, return
for correction, or reject. On approval, the system issues the applicant's output
(the certificate, title deed, map, or registry update that the originating service
defines) and writes the decision to the audit trail.

For escrow-apparatus items, an FTI Account Trustee has already assessed the request
and forwarded it (the "two-gate"); the auditor reviews that assessment alongside the
application and applies a heavier escrow checklist (§15).

## 4. Who Can Act *(replaces "Who Can Apply")*

**Compliance & Escrow Auditor** (RA), operating under real role-based access
control. **This is a genuine permission gate** — unlike every front-office service,
where a user's role is audit attribution only and gates nothing. Only a user holding
the Compliance & Escrow Auditor role may act on an item in this service, and access
requires MFA.

> **Note — the one place role gates action.** Everywhere else in RERAN, unified access
> applies. The Regulatory Authority is the exception; this section is where that exception lives.

## 5. Entry Conditions *(replaces "Prerequisites")*

- An originating front-office service has been submitted and paid, and has reached the
  status that routes it into review (typically `Submitted` → `Under Review`).
- For escrow-apparatus items: the FTI Account Trustee has completed its pre-assessment
  and forwarded the item (the second gate). Items still at the trustee stage do not
  appear in this queue.
- The acting auditor is authenticated (MFA) and holds the Compliance & Escrow Auditor
  role.

## 6. What the Reviewer Sees *(replaces "Required Information")*

- The full application as the applicant submitted it (all fields).
- All uploaded supporting documents.
- The registry records needed to verify it (developer, project, property/unit, title,
  applicant identity/authorisation) — pulled live, not re-keyed.
- The originating service's identity and its expected output and SLA.
- **Escrow variant:** the Account Trustee's uploaded assessment; the current escrow-
  account state; for mortgage-linked items, the live FTI status of the referenced
  mortgage (must read `Completed`).

## 7. Review Checklist *(replaces "Required Documents")*

**General (all items):**
- The applicant and their authorisation are valid.
- The subject (developer / project / unit / title) exists in the registry and is in a
  state that permits this action.
- Required documents are present, legible, and internally consistent.
- The application does not conflict with an existing registry record.

**Escrow variant (additional):**
- The Account Trustee's assessment is present and supports the request.
- Account-movement audit: the requested operation is consistent with the escrow
  account's balance, history, and governing caps.
- Signatory verification (for signatory-related items).

> **Proposed** — the escrow checklist is derived from the 13 escrow-apparatus services'
> own workflows; needs client confirmation against RERA's actual audit procedure.

## 8. Service Fee

**N/A.** The Regulatory Authority charges no fee for reviewing an application. The
applicant paid the service fee to the originating front-office service before
submission; no fee arises on the Regulatory Authority side.

## 9. Payment Required

**N/A (the Regulatory Authority side).** Payment timing belongs to each originating
service and is recorded there, per-service. This service never collects or holds a
payment.

## 10. Decision Authority & Access Control *(replaces "Processing Authority")*

- **Role:** Compliance & Escrow Auditor (RA).
- **Access control:** RBAC-gated + MFA (see §4).
- **Sub-system:** Escrow / Trust-Account Audit System (escrow items) and the general
  Transaction Audit Queue (all others) — one service, two queue-views.

## 11. Expected Processing Time

**Inherited from the originating service, not fixed here.** Each of the 92 external
services carries its own SLA (see touchpoint-register.md) — from a few minutes to
several business days. This service does not impose a single time; it is measured
against whichever SLA the item in hand belongs to.

## 12. Processing Workflow

```
Item enters queue  (submitted + paid; escrow: after trustee pre-assessment)
        ↓
Auditor opens item  (RBAC + MFA)
        ↓
Review application + documents
        ↓
Verify against registry  (developer / project / unit / title / applicant)
        ↓
[Escrow variant] Review trustee assessment + account-movement audit + signatories
        ↓
Decide  ──────────────┬───────────────┬──────────────┬───────────────┐
        ↓             ↓               ↓              ↓
     Approve   Request Information   Return      Reject
        ↓             ↓               ↓              ↓
 Issue output   Back to applicant  Back to     Close (terminal)
 (per origin    → re-enters queue  applicant
  service)       on response       for correction
        ↓
Write decision + actor to audit trail  (every branch)
```

## 13. Application Status Flow *(shared vocabulary — do not localise)*

This service drives the decision half of every originating service's status flow. It
must use exactly these states, because each front-office module's status display
reads them:

```
Under Review
   ↓
Information Requested   → (applicant responds) → Under Review
   ↓
Returned               → (applicant corrects) → Under Review
   ↓
Approved   /   Rejected
```

> **Critical dependency.** If this service uses different status words than the
> originating modules expect, every module's status display breaks. See §16.

## 14. Possible Outcomes

- **Approved** — the output is issued; the originating application completes.
- **Additional Information Requested** — returned to the applicant; re-enters the queue
  on their response.
- **Returned** — sent back for correction.
- **Rejected** — terminal.

## 15. Escrow Variant *(back-office-specific section)*

Escrow-apparatus items (13 services: RED #8–12, #20, #21; FTI #1, #2; RESC #5, #6, #7,
#11) run the identical decision loop of §12 with three differences:

1. **Two-gate entry.** An FTI Account Trustee assesses and forwards the item before it
   reaches this queue. There is an additional pre-queue return path ("Returned by
   Certifier") that happens before the Regulatory Authority ever sees the item.
2. **Extra context on screen.** The trustee assessment and the escrow-account state
   are shown alongside the application (§6).
3. **Heavier checklist.** The escrow checks in §7 apply in addition to the general ones.

This is a variant of one service, not a separate service (resolved, open-questions
A3). The UI presents escrow as its own queue-view with its own checklist.

## 16. Cross-Module Dependencies *(back-office-specific section)*

1. **The FTI handshake (15 services).** This service's "receive → decide" is the second
   half of a handshake whose first half is the FTI Account Trustee's "forward to RERA."
   Both sides must share the status vocabulary of §13.
2. **RED #6 ↔ FTI #3 live validation.** When this service approves a mortgage
   registration (FTI #3), that approval flips the mortgage to `Completed`, which is the
   status RED #6 (Register Mortgage-Linked Sale) checks in real time. A decision here
   has a synchronous downstream effect.
3. **Shared status vocabulary (§13).** Non-negotiable across all originating modules.

## 17. Related Services

- **A-6 Provision & manage access (RBAC)** — must exist before this service can be used.
- **A-7 Conduct site inspection** — feeds an inspection result back into a decision for
  the small number of items that require a field visit.
- **The 92 originating front-office services** — listed in touchpoint-register.md; not
  repeated here.

## 18. UI Screens

- **Queue / worklist** — pending items, filterable by originating service, status, age,
  and channel (transaction vs escrow). One screen, two queue-views.
- **Application detail / review** — the application, documents, and live registry checks
  in one view; the escrow variant adds trustee-assessment and account panels.
- **Decision panel** — the four-outcome control with a mandatory reason/notes field.
- **Audit-trail view** — the item's full history.

## 19. API Requirements

- Fetch queue (filtered, paginated)
- Fetch application detail + documents
- Registry verification calls (developer / project / unit / title / applicant)
- Fetch trustee assessment + escrow-account state *(escrow variant)*
- Fetch live FTI mortgage status *(mortgage-linked items)*
- Record decision (approve / request-info / return / reject) with actor + reason
- Trigger output issuance (delegates to the originating service's output)
- Notify applicant
- Write audit-log entry

## 20. Database Entities

- Application *(shared with originating module)*
- Review / Decision *(new — actor, outcome, reason, timestamp)*
- Staff User + Role + Permission *(RBAC)*
- Registry records *(read)*
- Escrow Account *(escrow variant, read)*
- Audit Log
- Notification

## 21. Acceptance Criteria

- Only a Compliance & Escrow Auditor with MFA can open or decide an item.
- Every item shows the application, its documents, and live registry checks.
- The auditor can record exactly one of the four outcomes, and a reason is mandatory
  for request-info / return / reject.
- Approval triggers the originating service's defined output.
- Escrow items display the trustee assessment and escrow-account state before a
  decision can be recorded.
- A mortgage-registration approval flips the mortgage to `Completed` for RED #6's check.
- Every decision, with its actor and reason, is written to the audit trail.
- Status transitions use only the shared vocabulary of §13.

## 22. Business Rules

1. Access is role-gated (Compliance & Escrow Auditor) and MFA-protected — the one
   RBAC-enforced action surface in RERAN.
2. No item may be decided without the registry checks of §7 being available.
3. Escrow items may not be decided before the trustee pre-assessment is present.
4. A mortgage registration may not be approved unless its own prerequisites are met;
   its approval is what makes RED #6's dependency valid.
5. Every outcome except plain approval requires a recorded reason.
6. All decisions are permanently recorded in the audit trail with the acting officer.
7. Status words are the shared platform vocabulary (§13); this service must not invent
   local ones.
