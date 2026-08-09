---
project: RERAN
module: public-users
type: overview
status: draft
updated: 2026-08-09
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - public-users
  - services-overview
---

# Public & Informational Users — Services Overview

33 services, verified against the master service table (rows 113–145). All are filed under a single source category: INFORMATIVE — General.

This is the highest service count in the project and by a wide margin the lowest complexity.

## The Dominant Pattern

30 of the 33 services follow one shape:

```
Select service  →  Enter parameter (some services)  →  View result
```

No approver. No fee. No application. No output document. Immediate response.

> **Proposed** — documenting 30 near-identical services as 30 separate flow documents would produce 30 files differing only in their search parameter and result fields. This module proposes instead: one flow document describing the lookup pattern, plus a service catalogue table giving each service's parameters, result fields and channels. Needs confirmation — see To Confirm.

## Service Catalogue

### A. Directory Lookups (12)

No parameter required — the service returns a list.

* Names of ancient and modern regions
* Real Estate Registrar Centers
* Real Estate Services Trustee Centers
* Accredited surveying companies
* Approved escrow account trustees
* Approved financial (accounts) auditors
* Licensed real estate developers
* Licensed real estate brokers
* Licensed real estate brokerage companies
* Accredited real estate valuation companies
* Joint Ownership Properties Management Companies
* Real estate management companies
* Real Estate Consultation Offices

### B. Verification Lookups (6)

Parameter required — the service confirms or denies a specific record.

* Verification of Certificate of Title / Title deed
* Verification of Taqeemi Certificate
* E-card Verification — requires card type and number
* Verification of real estate licenses and permits
* Verifying the Land Department evaluation certificate
* Search for Office Trade License

### C. Status Inquiries (5)

* Inquiry about a property status
* Inquiry about a real estate project status — by land number, project number or project name
* Inquiry about an application status
* Inquiry about your real estate services
* Track Your Case — by mobile number or case number

### D. Index & Indicator Services (3)

* Inquiry about Services fees indicator — by project name, use and year
* Inquiry about the rental index — by contract expiry, property type, region, rooms, current rent
* Rental status sheet

### E. Judicial Information (4)

* Judicial Judgments
* Smart Judge
* E-executive deed
* Judicial summons

### F. Fee Services (2)

The only Group H services with real workflows.

* Fee Payment Receipt — two paths: public lookup by reference, or retrieval from an owned property's records
* Fee Refund Request — full lifecycle: create request with bank details and attachments, OTP validation, approval or rejection notified by mobile and email, funds transferred on Ministry of Finance approval. Seven business days. A second path searches an existing request by number.

## Summary

| Category | Services | Complexity |
| :---- | :---: | :---- |
| Directory Lookups | 13 | Trivial — no parameter |
| Verification Lookups | 6 | Trivial — one parameter |
| Status Inquiries | 5 | Low |
| Index & Indicator | 3 | Low — multi-parameter |
| Judicial Information | 4 | Low |
| Fee Services | 2 | Moderate — real workflow |
| **Total** | **33** | |

> **Proposed** — these six categories are ours. The source files all 33 under one category (INFORMATIVE — General) with no sub-grouping, which is unusable for building. The grouping above is by interaction shape rather than subject matter, because interaction shape is what determines the screen. Needs client confirmation.

## Channels

Most services list Land Department website and RERA App. Three services additionally list **WhatsApp**, and the group's sub-system description names a **Call Centre**.

> No source document describes a WhatsApp or Call Centre flow for any service. The channels are named but never specified. If they are in scope, they need their own specification — a WhatsApp virtual assistant is a substantially different build from a web page.

## To Confirm

1. **One parameterised lookup flow, or 30 individual documents?** This is the single decision that determines whether this module is a week of work or a day.
2. Are WhatsApp and Call Centre channels in scope? They are named in the source but never specified.
3. Fee Refund Request involves Ministry of Finance approval — is that an integration, or a manual step outside the platform?
4. Do any Group H services require the optional light account, or are all 33 fully anonymous?
5. Should the directory lookups be live queries against the register, or periodically published lists?
