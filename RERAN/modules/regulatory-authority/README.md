---
project: RERAN
module: regulatory-authority
type: readme
status: draft
contains_proposals: true
updated: 2026-09-12
---

# Group A — Regulatory Authority & Governance

Group A is the government / regulator side of RERAN. It is structurally different
from every other module, and that difference shapes everything in this folder:

- **It owns no services and pays no fees.** Every one of the other groups' 145
  services is filed *to* Group A; Group A initiates none of its own.
- **Its work is deciding on others' work.** Group A's "services" are the approval
  touchpoints of the platform — receive, review/audit, then approve, request more
  information, return, or reject — plus the administrative functions that run the
  agency (configuration, finance, inspection, adjudication, inter-state liaison).
- **It is organised by sub-system, not by service catalogue**, because it has no
  catalogue. The six sub-systems are the module's top-level structure.
- **It is the only place RBAC applies.** Everywhere else a role is audit attribution
  only; within Group A, roles carry real permissions and MFA.

## The shape of Group A

- **8 roles**, of which only 3 make decisions on the current 114 documented services
  (Compliance & Escrow Auditor, Licensing & Registration Officer, Dispute
  Adjudication Officer). The other five run the platform, the finances, and the
  agency's governance and field functions.
- **6 sub-systems**: Admin & Configuration Console · Licensing & Registry Engine ·
  Escrow / Trust-Account Audit System · Inspection & Enforcement Module · Tribunal &
  Remote-Litigation System · Revenue & Settlement Dashboard.
- **114 external services** route here; the Compliance & Escrow Auditor alone
  finishes 92 of them.

## Documents in this module

| Document | What it covers |
| :--- | :--- |
| [roles-and-responsibilities.md](roles-and-responsibilities.md) | Plain description of each of the 8 roles and its duties |
| [services-overview.md](services-overview.md) | The touchpoint register — all 114 external services mapped to a Group A role and channel |
| [roles-and-actions-analysis.md](roles-and-actions-analysis.md) | Whole-system analysis: the action model, the 8-vs-3 reconciliation, cross-module dependencies, proposed build scope |
| [open-questions.md](open-questions.md) | Unresolved decisions this module is waiting on |

## Status

Draft. Foundational documentation only — no service-flows or UI yet. Several role
assignments are reasoned proposals pending client confirmation; see
[open-questions.md](open-questions.md).
