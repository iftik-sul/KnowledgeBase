---
project: RERAN
module: regulatory-authority
type: roles-and-responsibilities
status: draft
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
---

# Group A — Roles & Responsibilities

Group A (Regulatory Authority & Governance) is the government side of RERAN. It owns
no services and pays no fees; its role is to decide on, oversee, and govern the work
every other group submits. It has eight roles across six platform sub-systems.

Group A is also the only part of RERAN where real role-based access control applies.
Everywhere else, a user's role is recorded for audit attribution only and gates
nothing; within Group A, roles carry genuine permissions and are protected by MFA.

This document explains what each role is and what it is responsible for. For the
list of which services each role finishes — the reverse, by-service view — see
[services-overview.md](services-overview.md).

## The eight roles

### 1. Compliance & Escrow Auditor
Reviews and approves the large majority of everything filed on the platform —
property registrations, sales, leases, mortgages, financial-institution filings, and
all escrow-account operations. Audits project escrow and trust accounts, vets
off-plan sale registrations, monitors developer disclosure, and sanctions
defaulters. This is the busiest role in Group A by a wide margin.

### 2. Licensing & Registration Officer
Decides who is allowed to operate in the sector. Vets and approves developer, agent,
surveyor, and company licences and permits; issues, renews, amends, and cancels
professional practice cards; accredits training entities; and maintains the national
practitioner register.

### 3. Dispute Adjudication Officer
Handles conflict rather than approvals. Receives suits and complaints, schedules and
runs mediation and remote-litigation sessions, and records judgments. This is a
multi-step case process, not a single approve/reject decision.

### 4. System Super Administrator
Runs the platform itself. Provisions staff accounts, configures modules and role
permissions (this is the role that operates RBAC), and manages the audit trail, data
security, and disaster recovery.

### 5. Revenue & Finance Officer
Owns the money configuration. Sets fee schedules and levies, reconciles what the
payment gateway collects against what was owed, and manages penalty collection and
remittance to state and federal accounts.

### 6. Director-General / Registrar
The executive head of the authority. Approves policy, signs statutory instruments,
authorises licence revocations and final enforcement actions, and chairs the
governing-board interface. A governance and sign-off tier, not a routine processing
role.

### 7. Inspection & Enforcement Officer
The physical-world verification and enforcement role. Conducts geo-tagged site
inspections, verifies construction milestones, issues stop-work and violation
notices, and escalates penalties.

### 8. State Liaison Coordinator
The federalism role. Synchronises records with State Lands Bureaus and
Surveyors-General, resolves jurisdictional conflicts, and harmonises Certificate-of-
Occupancy data across federal and state authorities.

## How the roles relate to the work

Of the eight roles, only three make decisions on the current 114 services — the
Compliance & Escrow Auditor, the Licensing & Registration Officer, and the Dispute
Adjudication Officer. The System Super Administrator and Revenue & Finance Officer
are active but run the platform rather than deciding on applications. The remaining
three — Director-General, Inspection & Enforcement, and State Liaison — carry real
regulatory functions that no current service routes to. The reasoning behind this,
and what it means for build scope, is in
[roles-and-actions-analysis.md](roles-and-actions-analysis.md).
