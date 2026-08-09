---
project: RERAN
module: financial-trust-institutions
type: decision
status: draft
updated: 2026-08-09
derived_from:
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/payments.md"
tags:
  - financial-trust-institutions
  - open-questions
  - client
---

# Group C — Questions for RERA

Questions arising from documenting the Financial & Trust Institutions module. Grouped by decision area rather than by document, so each section can be taken to the right person.

Each question states what we assumed in the meantime, so work continues while answers are pending. Where an assumption turns out to be wrong, the affected documents are listed.

**Scope note:** this covers post-login functionality only. Registration and onboarding are excluded from this project.

---

## A. Roles — who does what after login

The source names four roles but assigns services to only two of them. Two roles have described functions but no system behaviour anywhere.

### A1. Is the "bank's internal auditor" the Auditing Bureau Officer?

The mortgage registration workflow includes a step where the bank's internal auditor reviews and certifies the transaction before it reaches RERA. That actor is not one of the four named Group C roles.

**Our assumption:** it is the Auditing Bureau Officer.

**Why it matters:** this makes the Auditing Bureau Officer a mandatory gate on 17 of the 18 services, rather than a peripheral role. If it is instead a fifth, unnamed role, the module needs another actor and another set of screens.

**Affects:** the entire two-gate model, every service flow, every status.

### A2. What does the Account Trustee actually see and do in this platform?

The Account Trustee appears as an approval step inside six Group B developer escrow services — account activation, transfer, profit withdrawal, payment release, mortgage deposit, bank guarantee cancellation — but has no Group C interface described anywhere.

**Our assumption:** they work from a dedicated queue in the RERA platform, reviewing routed developer requests, uploading assessments and certifying releases.

**Alternative:** they work in the bank's own systems and only the outcome is recorded in RERA.

**Affects:** whether this module needs a full escrow queue and certification interface, or just a status display.

### A3. Is milestone certification a document upload or a structured assessment?

When a Trustee certifies that a construction milestone justifies a drawdown, is that an uploaded letter, or a form with defined fields the platform validates?

### A4. Who owns the institution's own approval services?

Services #1 and #2 (approval, renewal and cancellation of Account Trustee & Auditing company standing) are assigned to the **Account Trustee** in the service table, but the role descriptions give responsibility for maintaining registration and renewing approvals to the **Institution Relationship Manager**. The source contradicts itself.

**Our assumption:** none — recorded as an open inconsistency.

### A5. Does the Institution Relationship Manager get an institution-wide view?

They are responsible for renewals and user provisioning, which implies visibility of expiry dates and staff activity, but no such view is described.

### A6. SLA for Trustee action on a routed developer request

Developer-side services state RERA's processing times but not how long the Trustee has to act.

### A7. Compliance report format

Does the Auditing Bureau Officer's independent compliance report follow a RERA-defined template, or the institution's own format?

---

## B. Payments — the largest gap

Every RERA service is chargeable, but the mechanics for institutional users are largely unspecified.

### B1. Standing account or direct debit?

Mortgage services state that fees are "deducted from the bank's account". This could mean a pre-funded account the institution holds with RERA, or a direct debit against a nominated commercial account.

**Our assumption:** a standing, pre-funded account.

**Why it matters:** a standing account requires a balance display, top-up flow, transaction ledger, low-balance alerting and periodic statements — none of which appear in any source document, and all of which are build work nobody has scoped. Direct debit requires almost none of it.

**This is the single most consequential open question in the module.**

### B2. If pre-funded: who tops up, and how?

Bank transfer, payment gateway, or an arrangement with RERA finance?

### B3. What happens when an approved transaction cannot be settled?

Payment occurs *after* audit approval. If funds are insufficient at that point, does the approval hold indefinitely, expire after a period, or void?

**Our assumption:** it holds in an approved-but-unsettled state and is retryable, with no expiry defined.

### B4. Is there a credit arrangement?

Or is settlement strictly pre-funded with no negative balance permitted?

### B5. Published fee schedule

Is there a fee schedule for the 18 Group C services that can be supplied? None exists in any source document.

### B6. Fee basis for mortgage services

Do fees scale with loan value, property value, or are they flat per transaction?

### B7. VAT applicability

Applied to all 18 services, or only some?

### B8. Institutional approval fees — annual or per application?

### B9. Are "fee balance", "payment receipt" and "e-receipt voucher" the same thing?

The source uses all three terms across different Group C services. We have treated them as one electronic payment receipt.

### B10. Do institutions request refunds through the public refund service?

A fee refund request service exists for the general public with a seven-business-day turnaround subject to Ministry of Finance approval. Whether institutions use the same route is unstated.

---

## C. Service structure

### C1. Are the proposed service categories acceptable?

The source groups the 18 services under RERA's internal filing categories — Development (2), Transaction (15), Title-Deed Data (1). We regrouped them by user-facing task:

| Proposed category | Services |
| :---- | :---: |
| Institutional Approval Services | 2 |
| Mortgage Services | 5 |
| Finance Lease Services | 4 |
| Title & Ownership Transaction Services | 6 |
| Contract Services | 1 |

The 18 services themselves are unchanged, and a reconciliation table to the source grouping is maintained.

### C2. Should Trustee Centre–only services gain an online path?

Several Group C services list only Real Estate Registration Trustee Centres as a channel, implying walk-in processing with no online equivalent today. Is bringing them online in scope for this platform, or should the documentation preserve the counter-only route?

**Our assumption:** preserved as counter-only, since changing it is a scope decision rather than a documentation one.

### C3. Do the four application-management features apply to Group C?

Submit Application, Track Application Status, Respond to Information Request, and Resubmit Returned Application are documented for individual users. Group C services follow the same six-stage pipeline, so we have assumed they apply equally.

### C4. Are the three proposed institution-specific features correct?

We proposed an Internal Certification Queue, an Escrow Request Queue, and Approval Expiry Tracking. Is anything missing, and are these the right shape?

---

## D. Platform-wide questions raised by this module

These are not Group C–specific, but surfaced here and will affect every module.

### D1. Application status vocabulary

No source document enumerates application statuses for any user group. We proposed a set for Group C's two-gate flow.

**Question:** should statuses be defined once platform-wide, or per module? A shared vocabulary is strongly preferable for reporting and for the staff back-office, but only RERA can confirm the list.

### D2. Does the two-gate pattern apply beyond Group C?

Group C actions pass through internal certification inside the institution, then external audit at RERA. Do other corporate groups — developers, service companies — have an equivalent internal gate, or do they submit directly?

---

## Summary

| Area | Questions | Blocking? |
| :---- | :---: | :---- |
| A. Roles | 7 | A1 and A2 block the service flows |
| B. Payments | 10 | B1 blocks any payment screen work |
| C. Service structure | 4 | Non-blocking; affects naming and scope |
| D. Platform-wide | 2 | D1 should be settled before other modules |
| **Total** | **23** | |

**The three to answer first:** A1 (is the internal auditor the Auditing Bureau Officer), A2 (what the Account Trustee does in this platform), and B1 (standing account or direct debit). Between them they determine the module's actor model, its screen count, and whether an entire account-management subsystem is in scope.
