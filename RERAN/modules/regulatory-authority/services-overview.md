---
project: RERAN
module: regulatory-authority
type: services-overview
status: draft
contains_proposals: true
updated: 2026-09-17
---

# Group A — Services Overview

This is Group A's own (back-office) service catalogue. Group A files no applications,
but it *does* perform a small, well-defined set of actions on the work other groups
submit. Each distinct action is a Group A service.
This is the back-office counterpart to the 145 front-office (applicant-filed)
services: an applicant files a front-office service, which lands as an item in one of
these back-office services.

The catalogue is small — ~10 services — because the whole-system analysis showed the
114 external touchpoints collapse onto a handful of repeated actions. A decision
service is a **queue**: one workflow that processes many external services, not one
service per touchpoint. (See [roles-and-actions-analysis.md](roles-and-actions-analysis.md)
for how the collapse was derived, and the touchpoint register for which external
service feeds which Group A service.)

**Status column:** *Active* = external services feed it today. *In scope* = no external
service routes to it directly, but an active service escalates work into it, so its screens
are built (open-questions A5). *Deferred* = nothing routes to it and nothing escalates into
it; screens deferred.

## Catalogue

| # | Group A service (action) | Role | Sub-system | Feeds from | Status |
| :-- | :-- | :-- | :-- | :-- | :-- |
| [A-1](service-flows/service-a1-audit-and-decide.md) | Audit & decide — application review | Compliance & Escrow Auditor | Transaction Audit Queue + Escrow / Trust-Account Audit | 92 external services (79 transaction, 13 escrow/trust) | Active |
| [A-2](service-flows/service-a2-vet-and-decide-licensing.md) | Vet & decide — licensing | Licensing & Registration Officer | Licensing & Registry Engine | 9 external services | Active |
| [A-3](service-flows/service-a3-adjudicate-dispute.md) | Adjudicate — dispute | Dispute Adjudication Officer | Tribunal & Remote-Litigation | 4 external services | Active |
| [A-4](service-flows/service-a4-configure-fee-schedule.md) | Configure fee schedule | Revenue & Finance Officer | Revenue & Settlement Dashboard | none (every fee-bearing service reads it) | Active |
| [A-5](service-flows/service-a5-reconcile-settlements.md) | Reconcile settlements | Revenue & Finance Officer | Revenue & Settlement Dashboard | none (gateway events) | Active |
| [A-6](service-flows/service-a6-provision-and-manage-access.md) | Provision & manage access (RBAC) | System Super Administrator | Admin & Configuration Console | none (internal) | Active |
| [A-7](service-flows/service-a7-conduct-site-inspection.md) | Conduct site inspection | Inspection & Enforcement Officer | Inspection & Enforcement Module | 2 sub-steps (RED #27; IU inspection-required) | **In scope** — A-1 depends on its report |
| [A-8](service-flows/service-a8-issue-enforcement-notice.md) | Issue enforcement notice | Inspection & Enforcement Officer | Inspection & Enforcement Module | none (proactive) | Deferred |
| [A-9](service-flows/service-a9-harmonise-land-records.md) | Harmonise land records | State Liaison Coordinator | Data harmonisation layer | none (periodic manual reconciliation) | Deferred |
| [A-10](service-flows/service-a10-executive-signoff-revocation.md) | Executive sign-off / revocation | Director-General / Registrar | Governance | none directly; **A-2 escalates revocations here** | **In scope** |

---

Each service ID links to its full service-flow in `service-flows/`.

## Service detail

### A-1 — Audit & decide (application review)
- **Trigger:** a paid, submitted application lands in the queue. For escrow/trust
  items, this is *after* the FTI Account Trustee's pre-assessment (the two-gate).
- **Inputs:** application data; uploaded documents; registry records to verify
  against; for escrow items, the trustee pre-assessment; for mortgage-linked items,
  the live FTI status check.
- **Steps:** receive → review & audit, verifying against the registry → decide.
- **Outcomes:** Approve · Request additional information · Return for correction · Reject.
- **Outputs (on approve):** the applicant's artifact (e-certificate, e-title deed,
  property map, or registry-record update) + payment receipt + audit-trail entry.
- **Escrow variant (A3, resolved):** transaction and escrow items are one service,
  not two — the decision loop is identical. Escrow items are handled as a documented
  variant within this service: they arrive through the FTI Account Trustee pre-gate,
  show escrow-account context, and carry a heavier review checklist (account-movement
  audit, trustee-assessment review, signatory verification). The UI gives escrow its
  own queue-view and checklist; the service-flow is one flow with an escrow branch.

### A-2 — Vet & decide (licensing)
- **Trigger:** a licence, permit, practice-card, or accreditation application is submitted.
- **Inputs:** applicant credentials; supporting documents; the national practitioner register.
- **Steps:** receive → vet against eligibility → decide → issue and update the register.
- **Outcomes:** Approve · Request information · Reject. (Some source workflows are
  auto-approve — e.g. practice-card renew/amend — where this service records rather
  than manually reviews.)
- **Outputs:** e-licence / permit / practice card / accreditation; register entry.

### A-3 — Adjudicate (dispute)
- **Trigger:** a suit, execution case, tenancy dispute, or complaint is filed.
- **Inputs:** the filing; the parties; submitted evidence.
- **Steps:** receive → schedule mediation / hearing → conduct session(s) → record judgment.
- **Outcomes:** multi-stage — resolved / partially resolved / dismissed / referred.
- **Outputs:** judgment record; assignment.
- **Note:** unlike A-1/A-2 this is a multi-session case process, not a single
  approve/reject — it needs its own case-management workflow, not the decision loop.

### A-4 — Configure fee schedule
- **Trigger:** internal — a policy change or a new fee-bearing service.
- **Inputs:** fee and levy definitions.
- **Steps:** create / edit fee entries → publish the schedule.
- **Outputs:** the active fee schedule that every fee-bearing service reads at checkout.
- **Note:** a configuration surface, not a queue.

### A-5 — Reconcile settlements
- **Trigger:** periodic, or on gateway settlement events.
- **Inputs:** gateway settlement data; amounts owed.
- **Steps:** match collected against owed → flag discrepancies → remit to accounts.
- **Outputs:** reconciliation report; remittance records.

### A-6 — Provision & manage access (RBAC)
- **Trigger:** internal — staff onboarding or a role change.
- **Inputs:** staff identity; role assignment; permission configuration.
- **Steps:** create account → assign role → set permissions → enrol MFA.
- **Outputs:** a provisioned, MFA-protected staff account; audit-trail entry.
- **Note:** this service *is* the RBAC operation. It must exist before any other
  Group A service can be used.

### A-7 — Conduct site inspection (In scope)
- **Trigger:** a sub-step of certain services (RED #27 field visit; IU
  inspection-required), or proactive.
- **Inputs:** site/project reference; inspection checklist; geo-tag.
- **Steps:** schedule → visit → record geo-tagged findings → verify milestones.
- **Outputs:** inspection report, which feeds back into an A-1 decision.
- **Screens in scope (A5):** inspection queue, on-site findings capture, inspection report.
  The capture screen is **mobile/tablet** — this is the only Group A role that works on site.

### A-8 — Issue enforcement notice (Deferred)
- **Trigger:** proactive — a violation is detected.
- **Inputs:** violation details; the entity concerned.
- **Steps:** assess → issue stop-work / violation notice → escalate penalty.
- **Outputs:** notice; penalty referral.

### A-9 — Harmonise land records (Deferred)
- **Trigger:** internal / periodic, or when a jurisdictional conflict is detected.
- **Inputs:** state-bureau records obtained out-of-band; C-of-O data; platform records.
- **Steps:** compare → detect conflicts → resolve / harmonise.
- **Outputs:** reconciled records.
- **A4 resolved:** AGIS is a **design reference, not a live integration** — so this is
  periodic **manual reconciliation**, not a system-to-system sync. No data contract, no
  sync API, no external uptime dependency.

### A-10 — Executive sign-off / revocation (In scope)
- **Trigger:** escalation — a revocation, final enforcement action, or statutory instrument.
- **Inputs:** the escalated case; the recommendation.
- **Steps:** review escalation → sign off / authorise.
- **Outputs:** signed instrument; revocation record.
- **Screens in scope (A5):** sign-off queue, sign-off detail. They support two escalation
  sources — A-2 licence revocations (**live**) and A-8 final enforcement (**deferred**) —
  so only one currently feeds them. Intended, not a defect.

---

## How this relates to the front-office services

Each external (front-office) service names, in its own service-flow, the Group A
service that finishes it. The touchpoint register is the join table: it lists all
114 external services and which of A-1 to A-3 (or none) each one feeds. This
catalogue is the reverse view — Group A's own services, each aggregating many
external ones.

The platform total is best stated as: **145 front-office services + ~10 Group A
back-office services.**
