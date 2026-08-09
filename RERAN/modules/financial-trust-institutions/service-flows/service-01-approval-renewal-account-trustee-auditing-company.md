---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
updated: 2026-08-10
source_type: sourced
derived_from:
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - financial-trust-institutions
  - service-flow
  - approval
  - renewal
  - account-trustee
  - auditing-company
---

# Service #1 — Approval / Renewal of Account Trustee & Auditing Company

## Purpose

Provides for approval or renewal of an institution's standing as an approved Account Trustee or Auditing Company within RERAN.

## Service Classification

- **Module:** Financial & Trust Institutions (Group C)
- **Service Category:** Institutional Approval Services
- **Service Number:** 1
- **Responsible Role:** Account Trustee is assigned in the source service table. The module documentation records a role-assignment inconsistency because the Institution Relationship Manager is described as maintaining registration and renewing trustee/auditor approvals.
- **Regulator / Approver:** Compliance & Escrow Auditor (Group A)
- **Channel:** Not specified in the available source material for this service.
- **SLA:** Not specified in the available source material.
- **Output:** Approval / renewal of the institution's approved standing. The exact output document is not specified in the available source material.

## Eligibility

The service applies to an institution seeking approval or renewal of its standing as an approved trustee or auditor.

The source material does not specify the detailed eligibility criteria.

## Required Information and Documents

The source material does not enumerate the required information or supporting documents for this service.

**Do not infer these requirements until confirmed by the client.**

## Fee / Payment

A fee/payment mechanism is not specified for this service in the available source material.

The module-level documentation identifies fee settlement as an open Group C question and does not establish whether the proposed institution-account deduction model applies to all 18 services.

## Workflow

The available source material establishes the service purpose and approval relationship but does not provide a complete numbered workflow for Service #1.

Therefore, the workflow is intentionally not reconstructed here.

### Confirmed Flow Elements

1. An institution seeks approval or renewal of its standing as an approved Account Trustee or Auditing Company.
2. The application is subject to Group A regulatory review/approval by the **Compliance & Escrow Auditor**.
3. On approval, the institution's approved standing is established or renewed.

### Unspecified Steps

The source does not specify:

- application initiation screen/channel;
- required documents;
- validation steps;
- internal institutional certification steps;
- payment timing and method;
- approval/renewal decision criteria;
- rejection or return flow;
- notification mechanism;
- exact issued document;
- exact SLA.

## Status Flow

No service-specific status vocabulary is defined in the source material.

The module's proposed Group C application status vocabulary is documented in `../services-overview.md`, but it is explicitly marked as proposed and awaiting client confirmation. It is therefore **not adopted as authoritative for this service**.

## Outcome

The intended outcome is approval or renewal of the institution's standing as an approved Account Trustee or Auditing Company.

The exact certificate, licence, or electronic document issued is not specified in the source material.

## Open Questions

1. Should Service #1 be owned by the **Account Trustee** or the **Institution Relationship Manager**? The source assigns it to the Account Trustee, while the role description assigns maintenance and renewal of trustee/auditor approvals to the Institution Relationship Manager.
2. What are the required eligibility criteria and supporting documents?
3. Which channel is used for the application?
4. What fee applies, and when/how is it paid?
5. What are the approval, return, and rejection rules?
6. What document or electronic record is issued after approval/renewal?
7. What is the SLA?

## Source Boundary

This document deliberately records only what is supported by the current RERAN source material. Missing workflow details are left unspecified rather than invented.
