---
project: RERAN
module: regulatory-authority
type: analysis
status: draft
contains_proposals: true
updated: 2026-09-12
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

### 1d. Actions with no application (the latent half)

The role definitions in source describe a second class of action that no current
service routes to — work Group A initiates itself rather than in response to a
filing:

- **Configure** — fee schedules and levies; modules and role permissions
- **Provision** — staff accounts, audit trails, data security, disaster recovery
- **Inspect** — geo-tagged site visits, construction-milestone verification
- **Enforce** — stop-work and violation notices, penalty escalation
- **Adjudicate** — mediation, remote-litigation sessions, recorded judgments
- **Reconcile** — gateway settlement, penalty collection, remittance to accounts
- **Harmonise** — C-of-O sync with State Lands Bureaus, jurisdictional conflicts

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
| **System Super Administrator** | Provisions accounts, configures modules and role permissions, owns the audit trail | Admin & Configuration Console | The role that operates RBAC itself |
| **Revenue & Finance Officer** | Configures the fee schedule every fee-bearing service reads; reconciles gateway settlements | Revenue & Settlement Dashboard | A background/config role — no per-service decision, but the fee engine cannot run without it |

### Tier 3 — Oversight & latent roles (real functions, no current service route)

| Role | Function | Why no service routes to it |
| :--- | :--- | :--- |
| **Director-General / Registrar** | Approves policy, signs statutory instruments, authorises licence revocations and final enforcement | An escalation/sign-off tier, not a first-line queue. No routine service needs the DG. |
| **Inspection & Enforcement Officer** | Site inspections, milestone verification, stop-work notices | Inspection appears only as a *sub-step* inside two services (RED #27 field visit; two IU services flag "Property Inspection Required"). Enforcement is proactive, not application-triggered. |
| **State Liaison Coordinator** | Syncs C-of-O data with State Lands Bureaus, resolves jurisdictional conflicts | A background integration function. This is the AGIS-integration territory (see §5). |

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
| **Inspection & Enforcement Module** | Inspection & Enforcement Officer | 0 primary (2 sub-steps) | Deferrable |

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

**Proposed position for RBAC:** define all eight roles (so the permission model is
complete and MFA covers the whole staff), but build functional screens and queues
for only four: the three approval roles plus System Super Administrator. Revenue &
Finance gets a configuration surface (the fee schedule) but no queue. Inspection &
Enforcement and State Liaison get role definitions and placeholder permissions,
with functional build deferred until services that exercise them exist. This keeps
the RBAC model whole without building five back-offices for work the platform
cannot yet generate. (Scope/sequencing is a proposal — see open-questions.md A5.)

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
  homes recorded in open-questions A2.
- **Unconfirmed role assignments** — 12 IU services name only "RERAN"; several RESC
  services were assigned by pattern. Marked `[proposed]`; see A1.
- **9 services need no Group A decision** — automated lookups + wrappers; documented
  as system actions, no role, no queue.
- **Escrow sub-system** — 79 transaction vs 13 escrow, verified against source;
  modelled as one service with an escrow variant (A3, resolved).
- **AGIS reference vs integration** — the largest external unknown (A4).

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

Deferrable to a later phase: the Inspection & Enforcement module and State Liaison
integration, pending services that exercise them and the AGIS decision.
