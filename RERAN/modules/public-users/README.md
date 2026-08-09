---
project: RERAN
module: public-users
type: overview
status: draft
updated: 2026-08-09
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - public-users
  - index
---

# Public & Informational Users Module

RERAN user Group H — unauthenticated and lightly-authenticated users consuming verification, inquiry and awareness services.

**Scope:** post-login functionality only. Note that most Group H services require no account at all, which makes "post-login" a loose fit for this module — see Scope Note.

## Contents

| Section | Count |
| :---- | :---: |
| Roles | 2 |
| Business Services | 33 |

* [roles-and-responsibilities.md](roles-and-responsibilities.md)
* [services-overview.md](services-overview.md)

## Scope Note

Group H is the highest service count in the project and the lowest complexity. Of the 33 services, 30 follow a near-identical three-step shape: select the service, enter a search parameter where required, view the result. No approver, no fee, no application lifecycle, no output document.

The source describes public verification as requiring no registration. This module therefore documents mostly *unauthenticated* behaviour, which sits at the edge of the project's post-login scope. It is included because the same lookups appear inside authenticated experiences across other modules — a buyer verifying a developer, a bank verifying a title.

## The Three Exceptions

Three services have real workflows and belong to a different class from the other 30:

| Service | Why it differs |
| :---- | :---- |
| Fee Payment Receipt | Two distinct paths — public lookup, or retrieval from an owned property record |
| Fee Refund Request | Full application lifecycle: submit with bank attachments, OTP validation, Ministry of Finance approval, seven business days |
| Track Your Case | Case-status lookup by mobile or case number |

## Platform Sub-systems

* Public Register & Verification
* Inquiry Services — App, Web, WhatsApp, Call Centre

## Service Flows

> Not yet written. Expected to consolidate heavily — see the services overview.

## UI Specifications

> Not yet written.

## Open Questions

1. Is Group H in scope for this project at all, given that most of it is unauthenticated?
2. Should the 30 lookup services be documented individually, or as one parameterised pattern with a service catalogue?
3. The WhatsApp and Call Centre channels appear in the source but no flow describes them. Are they in scope?
4. The optional light account (email plus phone OTP) saves searches and complaint references — is that in scope, given registration is excluded?
