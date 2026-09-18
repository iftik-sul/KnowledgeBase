---
project: RERAN
module: regulatory-authority
type: readme
status: draft
contains_proposals: true
updated: 2026-09-17
---

# Regulatory Authority & Governance

The Regulatory Authority is the government / regulator side of RERAN. It is structurally
different from every other module, and that difference shapes everything in this folder:

- **It owns no front-office services and pays no fees.** Every one of the other
  groups' 145 applicant-filed services is filed *to* the Regulatory Authority; it initiates none.
  It does, however, have its own small **back-office service catalogue** — the ~10
  distinct actions it performs on that filed work (see services-overview.md).
- **Its work is deciding on others' work.** The Regulatory Authority's "services" are the approval
  touchpoints of the platform — receive, review/audit, then approve, request more
  information, return, or reject — plus the administrative functions that run the
  agency (configuration, finance, inspection, adjudication, inter-state liaison).
- **It is organised around six sub-systems**, which its ~10 back-office services sit
  within. The sub-systems are the module's top-level structure.
- **It is the only place RBAC applies.** Everywhere else a role is audit attribution
  only; within the Regulatory Authority, roles carry real permissions and MFA.

## The shape of the Regulatory Authority

- **8 roles**, of which only 3 make decisions on the current 114 documented services
  (Compliance & Escrow Auditor, Licensing & Registration Officer, Dispute
  Adjudication Officer). The other five run the platform, the finances, and the
  agency's governance and field functions. Screens are built for **six of the eight** —
  those three, plus System Super Administrator and Revenue & Finance, plus the
  Director-General and the Inspection & Enforcement Officer, because active services
  escalate work into both (open-questions A5).
- **6 sub-systems**: Admin & Configuration Console · Licensing & Registry Engine ·
  Escrow / Trust-Account Audit System · Inspection & Enforcement Module · Tribunal &
  Remote-Litigation System · Revenue & Settlement Dashboard.
- **114 external services** route here; the Compliance & Escrow Auditor alone
  finishes 92 of them.
- **~10 back-office services** of its own. Platform total: **145 front-office
  services + ~10 Regulatory Authority back-office services.**

## Documents in this module

| Document | What it covers |
| :--- | :--- |
| [roles-and-responsibilities.md](roles-and-responsibilities.md) | Plain description of each of the 8 roles and its duties |
| [services-overview.md](services-overview.md) | Regulatory Authority's own back-office service catalogue — the ~10 actions it performs |
| [touchpoint-register.md](touchpoint-register.md) | The join table — all 114 external services mapped to the Regulatory Authority role, channel, and service that finishes each |
| [roles-and-actions-analysis.md](roles-and-actions-analysis.md) | Whole-system analysis: the action model, the 8-vs-3 reconciliation, cross-module dependencies, proposed build scope |
| [open-questions.md](open-questions.md) | Unresolved decisions this module is waiting on |
| [ui/README.md](ui/README.md) | The back-office UI layer — screens, modals, RBAC matrix, flows |

## Status

Draft. The module now holds its foundation, **10 service-flows** (A-1 to A-10) and **11
screen specs** plus the modal catalogue, RBAC matrix, and the Compliance & Escrow Auditor
flow. Screens for A-7 (inspection) and A-10 (sign-off) are in scope but **not yet specced**;
A-8 and A-9 screens are deferred. One open question remains — A2, the authority-label drift
— deliberately parked. See [open-questions.md](open-questions.md).
