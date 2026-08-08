---
project: RERAN
module: individual-user
type: reference
status: current
updated: 2026-08-09
derived_from:
  - "RERAN/modules/individual-user/RERAN_ individual user_service_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - individual-user
  - shared-feature
  - application-management
---

# Shared Platform Features – Application Management

## Feature #1 – Submit Application

Used by every service that requires an official submission to RERAN.

Examples:

* Register Property Ownership  
* Transfer Property Ownership  
* Register Property Sale  
* Register Lease  
* Renew Lease  
* Register Power of Attorney  
* Submit Complaint

See [feature-01-submit-application.md](feature-01-submit-application.md) for full detail.

## Feature #2 – Track Application Status

Allows users to monitor every submitted application from one place.

Examples:

* Property Registration  
* Lease Registration  
* Title Transfer  
* Complaint  
* Power of Attorney  
* Remote Transactions

See [feature-02-track-application-status.md](feature-02-track-application-status.md) for full detail.

## Feature #3 – Respond to Information Request

Allows users to respond when RERAN requests additional information, documents, or corrections.

Examples:

* Upload missing documents  
* Correct application details  
* Provide additional explanations  
* Submit revised supporting evidence

See [feature-03-respond-to-information-request.md](feature-03-respond-to-information-request.md) for full detail.

## Feature #4 – Resubmit Returned Application

Allows users to correct returned applications and resubmit them without creating a new application.

Examples:

* Incorrect ownership details  
* Missing documents  
* Invalid information  
* Incorrect payment evidence

See [feature-04-resubmit-returned-application.md](feature-04-resubmit-returned-application.md) for full detail.

## This order mirrors the lifecycle of almost every RERAN application:

Choose Service  
        ↓  
Complete Form  
        ↓  
Submit Application  
        ↓  
Track Application Status  
        ↓  
Information Requested? ── Yes ──► Respond to Information Request  
        │  
        No  
        │  
Returned? ─────────────── Yes ──► Resubmit Returned Application  
        │  
        No  
        │  
Approved / Rejected
