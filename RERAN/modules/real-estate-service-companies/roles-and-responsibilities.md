---
project: RERAN
module: real-estate-service-companies
type: user-group
status: draft
updated: 2026-08-16
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
tags:
  - real-estate-service-companies
  - roles
---

# Real Estate Service Companies — Roles & Responsibilities

Group D covers licensed brokerages, jointly-owned-property (JOP) administrators, and property management firms that operate under a single verified company account.

This document describes post-login responsibilities only. Account creation and onboarding are out of scope for this project.

> **Unified access, from the start.** None of the four roles below gates access. Every user of a registered Group D company can see and act on every screen, action, and service in this module. The descriptions below say what each role *typically* does and why the role exists, not what it is *permitted* to do. Every action is logged with the acting user and the role they held at the time — that is the only thing role controls here. This module does not repeat the role-permission-matrix-then-correction cycle Groups B and C both went through; it starts where they ended up.

## Role Summary

| Role | Player | Typical focus (descriptive, not restrictive) |
| :---- | :---- | :---- |
| Brokerage Principal | Licensed broker | Firm licensing, agent registration, listings, auction transactions |
| Owners'-Association Manager | JOP / strata manager | Jointly-owned-property administration, escrow, budgets, audits |
| Property Management Officer | Management firm staff | Management contracts, tenancy-system user registration |
| Company Dispute Filing Officer | Firm legal staff | Primary suits and execution cases for managed/joint properties |

---

## 1. Brokerage Principal

**Player:** Licensed broker

### Purpose

Holds the firm's RERA licence and oversees the company's licensing standing, listings, and transaction logging. The highest-authority role in the module by source description, though not an exclusive one — any of the company's four Group D roles may perform the same actions.

### Responsibilities

* Hold the firm's real estate licence and keep it in good standing
* Apply for real estate permits (advertisement types: electronic, classified, billboard, SMS)
* Issue, renew, cancel, and amend real estate professional practice cards for agents
* Register real estate evaluation details certificates *(confirmed 2026-08-16 as a Group D service — see Open Questions for what remains genuinely unresolved about this one)*
* Apply for accreditation of the firm as a training entity
* Apply for permits to sell real estate by public auction
* Register properties sold by public auction

### Practical Example

A brokerage wants to list a new billboard advertisement for an upcoming project launch. The Brokerage Principal opens the licensing system, selects the real estate permit service, fills in the advertisement details, attaches supporting documents, pays the fee upfront via the shared platform gateway, and sends the application. RERA audits the request and, on acceptance, delivers the permit e-certificate through the digital system.

**Corrected 2026-08-16, by client decision (`open-questions.md` B4).** This example previously described payment happening after RERA's acceptance, matching the row's original sourced sequence. Payment now happens before submission, matching the normalization applied to this service and #12, #14, and #15.

> **Proposed** — the source's Responsible Role column attributes all eight Licensing Services rows (59–66) to Brokerage Principal uniformly. Whether that attribution holds up service-by-service, the way Group C's did not for several of its rows, is checked in `open-questions.md` rather than assumed here — and, per A1, does hold up cleanly for this module, unlike Group B or C's equivalent columns.

---

## 2. Owners'-Association Manager

**Player:** JOP / strata manager

### Purpose

Administers jointly-owned-property matters on behalf of an owners' association: registering the association itself, managing its escrow account, and coordinating the appointment of auditors.

### Responsibilities

* Register a real estate company for administrative supervision of a jointly-owned property
* Register an Owners' Association
* Register employees with professional competence in JOP management
* Secure approval of service fees and utilization fees for a joint property
* Request transfer of a joint property's escrow account
* Request a no-objection letter to close a project's escrow account
* Request accreditation of authorized signatories on the escrow account
* Appoint a financial auditor with specific responsibilities
* Appoint an audit office to audit a joint property's financial accounts
* Appoint an audit office to audit a joint property's budget
* Apply for approval or renewal of a Financial Auditing Company

### Practical Example

An owners' association at a mixed-use development needs its annual accounts audited. The Owners'-Association Manager opens the JOP system, selects the appropriate audit-office-appointment service, and submits the request with the proposed auditor's details. RERA reviews and approves; the appointment is recorded against the joint property's own record.

> **Resolved 2026-08-16 (`open-questions.md` A3)** — the roadmap flagged JOP as potentially mirroring Group B's escrow-account mechanism (which Group C models as its own Escrow Request Queue) with different actors. Checked directly against the source: JOP's escrow-adjacent services (rows 50–56) route directly from the Owners'-Association Manager to RERA's Compliance & Escrow Auditor, with no Account Trustee intermediary sourced anywhere. This does not mirror Group B/C's mechanism.

---

## 3. Property Management Officer

**Player:** Management firm staff

### Purpose

Registers and maintains the firm's property management contracts and the users operating within the tenancy system on the firm's behalf.

### Responsibilities

* Register and renew real estate management contracts
* Request cancellation of a real estate management contract
* Register a user in the tenancy system, by category

### Practical Example

A management firm takes on a new residential block. The Property Management Officer opens the tenancy system, registers the management contract with the property details and term, and attaches the signed agreement. On submission, a registered management contract is emailed to the firm.

---

## 4. Company Dispute Filing Officer

**Player:** Firm legal staff

### Purpose

Files and pursues formal dispute proceedings on behalf of the company, for matters arising from managed or jointly-owned properties.

### Responsibilities

* File a primary suit concerning a jointly-owned property
* File and pursue an execution case for a jointly-owned property judgment

### Practical Example

An owners' association judgment needs to be enforced against a defaulting unit owner. The Company Dispute Filing Officer opens the dispute system, selects the execution case service, submits the annotated judgment and supporting documents, and pays the applicable fee. The Dispute Adjudication Officer (Group A) processes the request and issues the judge's resolution.

Only two of the module's 26 services fall to this role by source description — the smallest responsibility set of the four, but not a smaller access footprint, since any of the four roles may still act on these services under the unified-access model.

---

## How They Work Together

**Descriptive, not access-restrictive**, matching the model Groups B and C both arrived at. The table below shows who *typically* handles each stage in practice — useful for reading the audit trail — not who is *permitted* to.

| Stage | Typically handled by |
| :---- | :---- |
| Firm secures and maintains its real estate licence | **Brokerage Principal** |
| Firm lists properties, applies for advertisement permits, logs transactions | **Brokerage Principal** |
| Firm manages a jointly-owned property's administration and escrow | **Owners'-Association Manager** |
| Firm registers and renews a property management contract | **Property Management Officer** |
| Firm files or executes a dispute on a managed or joint property | **Company Dispute Filing Officer** |

Any of these stages may be carried out by any role — a Brokerage Principal may file a management contract directly, a Property Management Officer may register a JOP escrow transfer, and whoever performs an action, the audit trail records their name and the role they held at the time.

In short, each role's customary focus is:

* **Brokerage Principal** → Licensing, listings, permits, and transaction logging.
* **Owners'-Association Manager** → Jointly-owned-property administration and escrow.
* **Property Management Officer** → Management contracts and tenancy-system users.
* **Company Dispute Filing Officer** → Disputes on managed or joint properties.

## Open Questions

1. ~~**Row 65 (Real Estate Evaluation Details Certificate)** — does this row genuinely belong to Group D, or is it a Group G (Allied Professionals) service the source table filed under the wrong group?~~ **Resolved 2026-08-16 (client decision, `open-questions.md` A2)** — confirmed Group D. What remains open: this row's own workflow text still reads as a Valuer-facing process ("sign up via evaluation company option... make real estate evaluation") structurally unlike every other Group D service, and it has no designed UI screen yet — see `service-flows/service-18-register-evaluation-details-certificate.md`'s own Open Questions for the details.
2. **Role attribution for the Licensing Services cluster (rows 59–66)** is taken directly from the source's Responsible Role column without independent re-derivation. Given Group B and Group C's own Responsible Role columns each turned out to be a coarse category default rather than a genuine per-service assignment, this attribution should be checked service-by-service — checked in `open-questions.md` A1, which found the column holds up cleanly for every Group D category, including Licensing, unlike Group B or C's equivalents. Though, per the unified-access model above, this affects only the "typically handled by" framing, never actual access.
