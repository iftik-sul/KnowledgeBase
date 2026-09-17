---
project: RERAN
module: regulatory-authority
type: analysis
status: draft
contains_proposals: true
updated: 2026-09-17
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/modules/real-estate-developer/service-flows/"
  - "RERAN/modules/financial-trust-institutions/service-flows/"
  - "RERAN/modules/real-estate-service-companies/service-flows/"
  - "RERAN/modules/individual-user/service-flows/"
  - "RERAN/module-roadmap.md"
---

# Group A — Roles & Actions Analysis

## Purpose

Group A owns no services of its own and pays no fees. It exists only as the
approval side of work initiated by every other group. This analysis therefore
does not start from Group A's org chart — it starts from the 114 documented
external services (RED 27, FTI 18, RESC 26, IU 43), extracts every action that
lands on Group A, and lets the roles fall out of the actual work. The finding is
that Group A's job is a small, repeated decision loop carried by three roles,
wrapped in a larger set of platform and oversight functions that the current
service catalogue does not yet exercise.

---

## 1. The action model — what Group A actually does

Read across all 114 services, every Group A interaction reduces to one of two
kinds of action.

### 1a. The application decision loop (every routed service)

Every service that reaches Group A follows the same four-step shape. The role and
the queue change; the shape does not.

1. **Receive** — the paid, submitted application lands in a role's queue.
2. **Review / audit** — examine the application and its documents; verify against
   the registry (developer exists, project registered, unit available, title
   valid, applicant authorised).
3. **Decide** — exactly one of four outcomes:
   - **Approve** → issue the output (see §1c)
   - **Request additional information** → returns to the applicant, then re-enters
     the queue when they respond
   - **Return** → send back for correction
   - **Reject** → terminal
4. **Record** — every step is written to the permanent audit trail.

This is not inferred. The outcome vocabulary across the 114 files is dominated by
exactly these four: **Application Rejected (91 services), Additional Information
Requested (87), Application Returned (52)**, against Approved/registered outputs.
The workflow text names the decision directly — "Approve, Return or Reject" and
"Accept or Reject" appear as literal steps.

### 1b. The two-gate variant (15 services)

For escrow- and finance-related services, someone acts *before* Group A sees the
application:

- **FTI custody chain (9 services):** a developer or service company touches an
  escrow account; the FTI Account Trustee assesses and forwards it; only then does
  Group A audit and decide.
- **FTI internal certify (6 services):** for mortgage and finance-lease
  registrations, an internal certifier inside the institution certifies the
  transaction first, then Group A approves.

In both cases the Group A action is unchanged — it is still the decision loop of
§1a. What changes is that the queue receives a pre-vetted item, and there is an
extra return path ("Returned by Certifier").

### 1c. What approval produces

On approval Group A issues one of a small set of artifacts: electronic
certificates, electronic title deeds, property maps, and registry-record updates,
each with a payment receipt and an audit entry. These are the tangible outputs of
the decision loop — the reason the applicant filed in the first place.

### 1d. Actions with no application

The role definitions in source describe a second class of action that no current
service routes to — work Group A initiates itself rather than in response to a
filing:

- **Configure** — fee schedules and levies; modules and role permissions
- **Provision** — staff accounts, audit trails, data security, disaster recovery
- **Inspect** — geo-tagged site visits, construction-milestone verification
- **Enforce** — stop-work and violation notices, penalty escalation
- **Adjudicate** — mediation, remote-litigation sessions, recorded judgments
- **Reconcile** — gateway settlement, penalty collection, remittance to accounts
- **Harmonise** — C-of-O reconciliation with State Lands Bureaus, jurisdictional
  conflicts

These matter because they are what most of the eight roles are *for*, even though
the 114 services barely touch them.

---

## 2. The eight roles, defined by actual work

The source-of-truth defines eight Group A roles. Sorting them by what the 114
services actually demand produces three tiers.

### Tier 1 — Approval-queue roles (carry all 105 decisions)

| Role | Decides | Sub-system | Actions |
| :--- | :--- | :--- | :--- |
| **Compliance & Escrow Auditor** | **92 of 114** services | Transaction Audit Queue (79) + Escrow / Trust-Account Audit (13) | Full decision loop; escrow-account audit; disclosure monitoring |
| **Licensing & Registration Officer** | **9** services | Licensing & Registry Engine | Vets and approves licences, permits, practice cards, accreditations |
| **Dispute Adjudication Officer** | **4** services | Tribunal & Remote-Litigation | Receives suits/complaints, adjudicates, records judgments |

One role — the Compliance & Escrow Auditor — carries 81% of every decision on the
platform. This is the single most important fact about Group A: it is not eight
roles sharing a load, it is one role carrying it, with two specialists handling
small tributaries.

### Tier 2 — Platform & configuration roles (active, no approval queue)

| Role | Function | Sub-system | Note |
| :--- | :--- | :--- | :--- |
| **System Super Administrator** | Provisions accounts, configures modules and role permissions, owns the audit trail | Admin & Configuration Console | The role that operates RBAC itself. One role, no break-glass override (A7). |
| **Revenue & Finance Officer** | Configures the fee schedule every fee-bearing service reads; reconciles gateway settlements | Revenue & Settlement Dashboard | A background/config role — no per-service decision, but the fee engine cannot run without it |

### Tier 3 — Oversight roles (no primary service route; two now have screens)

| Role | Function | Screen status |
| :--- | :--- | :--- |
| **Director-General / Registrar** | Approves policy, signs statutory instruments, authorises licence revocations and final enforcement | An escalation/sign-off tier, not a first-line queue — but A-2 *does* escalate revocations here, so its screens are built (A5). Also has read-only access to Application Review (A7). |
| **Inspection & Enforcement Officer** | Site inspections, milestone verification, stop-work notices | Inspection appears only as a *sub-step* (RED #27; IU inspection-required) — but A-1 depends on the report, so inspection screens are built (A5), on a mobile/tablet form factor. Enforcement is proactive and stays deferred. |
| **State Liaison Coordinator** | Reconciles C-of-O data with State Lands Bureaus, resolves jurisdictional conflicts | Nothing routes to it. Per A4 this is manual reconciliation, not integration; screens deferred. |

---

## 3. The six sub-systems

Group A's source structure is six platform sub-systems. Mapping the services onto
them shows where the build weight sits.

| Sub-system | Primary role | Services feeding it | Build weight |
| :--- | :--- | :--- | :--- |
| **Escrow / Trust-Account Audit** (incl. the general Transaction Audit Queue) | Compliance & Escrow Auditor | 92 | **Heaviest — build first** |
| **Licensing & Registry Engine** | Licensing & Registration Officer | 9 | Medium |
| **Tribunal & Remote-Litigation** | Dispute Adjudication Officer | 4 | Light |
| **Admin & Configuration Console** | System Super Administrator | 0 (platform-wide) | Required — hosts RBAC |
| **Revenue & Settlement Dashboard** | Revenue & Finance Officer | 0 (all fee-bearing) | Required — hosts fee engine |
| **Inspection & Enforcement Module** | Inspection & Enforcement Officer | 0 primary (2 sub-steps) | Inspection built (A-1 depends on it); enforcement deferred |
| **Governance (sign-off)** | Director-General / Registrar | 0 primary (A-2 escalations) | Built — A-2 revocations escalate here |

The Tribunal sub-system, though it carries only four services, is the one place a
Group A role does something genuinely different from the decision loop —
adjudication is a multi-session process, not an approve/reject. It cannot be
folded into the audit queue.

---

## 4. The role reconciliation — 8 named, 3 active, why

The gap between "eight roles" and "three roles that appear in any service" is the
central thing to resolve before completing Group A. It is not an error in the
sources; it is the difference between a *regulator's full mandate* and the *slice
of that mandate the first 114 services exercise*.

- **The 114 services are almost all transactional** — register a sale, approve a
  licence, file a dispute. Transactional work needs an auditor, a licensing
  officer, and an adjudicator. That is the three active roles.
- **The other five roles are the regulator's institutional apparatus** —
  governance (DG), platform operations (Super Admin), money (Revenue & Finance),
  physical oversight (Inspection & Enforcement), and federalism (State Liaison).
  They are not exercised by transactions; they run the agency.

**Resolved (open-questions A5).** All eight roles are defined in RBAC, so the
permission model and MFA cover the whole staff. Functional screens are then built
**where an active service already escalates work into the role**, not by
completeness:

- **Built:** the three approval roles, System Super Administrator, Revenue & Finance
  (configuration surface), plus **DG sign-off** (A-2 escalates revocations there and
  would otherwise dead-end) and **Inspection** (A-1 expects inspection reports that
  nothing could produce).
- **Deferred:** Enforcement (proactive only, nothing triggers it) and Harmonisation
  (nothing routes to it, and per A4 it is now simple manual reconciliation).

The dependency rule is what makes this defensible: a screen exists because work
arrives at it, not because a role appears on an org chart.

---

## 5. Cross-system dependencies (what makes Group A un-buildable in isolation)

Three connections mean Group A cannot be specced separately from the modules it
serves:

1. **The FTI handshake (15 services).** The FTI Account Trustee's "forward to RERA"
   step and Group A's "receive → audit → decide" step are two ends of one
   handshake. They need a shared status vocabulary or they will not connect at
   runtime.
2. **RED #6 ↔ FTI #3 live validation.** Register Mortgage-Linked Sale runs a
   real-time check against Mortgage Registration; the mortgage must read
   `Completed` on the FTI side. Group A's decision on the mortgage is what flips
   that status. This is already live and synchronous.
3. **Shared status vocabulary.** Every module's Application Status Flow ends in
   Group A's decision states (Under Review, Information Requested, Returned,
   Approved, Rejected). If Group A's queue uses different words, every module's
   status display breaks.

---

## 6. Gaps and decisions needed

See [open-questions.md](open-questions.md) for the live tracking of these. In brief:

- **Authority-label drift** — "Survey Department" (4 RED services), "Registrar" (RED
  #13), "Trusts Department" (FTI #13) are not among the 8 sourced roles. Proposed
  homes recorded in open-questions A2. **The one item still open**, deliberately — it
  requires editing other modules' files.
- **Role assignments where the source named no officer** — 20 services (12 IU, 8 RESC).
  All confirmed 2026-09-17; `[proposed]` tags removed. See A1.
- **9 services need no Group A decision** — automated lookups + wrappers; documented
  as system actions, no role, no queue.
- **Escrow sub-system** — 79 transaction vs 13 escrow, verified against source;
  modelled as one service with an escrow variant (A3, resolved).
- **AGIS** — resolved (A4): a design reference, not a live integration. A-9 is therefore
  manual reconciliation, not a system-to-system sync.
- **Screen scope** — resolved (A5): DG sign-off and Inspection screens are built because
  active services escalate into them; Enforcement and Harmonisation stay deferred.
- **Operating decisions** — resolved (A6, A7): shared-pool work allocation with
  claim-on-open and a 30-minute lapse; SLA clock resets on resubmission; no supervisory
  review tier (one auditor's decision is final); in-app notifications only; step-up
  authentication on the five widest-consequence actions; no separation-of-duties
  requirement.

---

## 7. Proposed build scope to complete Group A

Given the analysis, completing Group A means building, in priority order (this is a
proposed sequence, not a fixed plan):

1. **The Transaction Audit Queue + decision loop** (Compliance & Escrow Auditor) —
   one queue, one screen pattern (receive → review → approve/return/request/reject
   → issue output), covering 92 services. This single build unblocks the back half
   of almost every external service.
2. **RBAC + Admin Console** (System Super Administrator) — the permission model for
   all 8 roles, MFA, and the audit trail. Required before any staff can act.
3. **The FTI handshake contract** — shared statuses so the 15 two-gate services
   connect.
4. **Licensing & Registry Engine** (Licensing & Registration Officer) — 9 services.
5. **Tribunal & Remote-Litigation** (Dispute Adjudication Officer) — 4 services,
   distinct multi-session flow.
6. **Fee-schedule configuration** (Revenue & Finance Officer) — background surface.

Then, per the A5 resolution: **DG sign-off screens** (queue + detail) and the
**Inspection screens** (queue, on-site capture, report — mobile/tablet form factor).

Still deferred: the Enforcement half of A-7/A-8, and State Liaison harmonisation —
neither has work arriving at it today.
