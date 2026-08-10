---
project: RERAN
module: financial-trust-institutions
type: decision
status: draft
updated: 2026-08-10
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/payments.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
tags:
  - financial-trust-institutions
  - open-questions
  - decisions
  - client
---

# Group C — Questions and Proposed Answers

Twenty-three questions arose from documenting the Financial & Trust Institutions module. Rather than hold the module until the client responds, each now carries a **proposed answer** we will build against unless told otherwise.

**How to read this:** each answer states a recommendation, the reasoning behind it, how confident we are, and what breaks if it is wrong. Confidence is:

| Level | Meaning |
| :---- | :---- |
| **Sourced** | The source material answers this; we had missed it or read it too narrowly |
| **High** | A strong inference from the source, or the only option that survives contact with the PRD |
| **Medium** | A reasonable design judgement; a different answer would also be defensible |
| **Client data** | Cannot be reasoned to. Only RERA holds the answer |

Only one question in twenty-three is client data.

**Scope note:** post-login functionality only. Registration and onboarding are excluded.

---

## The Answer That Resolves Two Questions

A1 and D2 dissolve into a single mechanism, so it is stated once here.

**Internal certification is a permission scope on a corporate account, not a role.**

Registration Flow 5 already establishes the machinery: delegated staff are invited by the company's authorised representative, who "confirms the staff member's permission scope (e.g. escrow filing only)" before activation. A maker-checker gate is that same mechanism with a second scope — *certify* alongside *file*.

This means the platform needs no fifth Group C role, and no separate two-gate model per group. It needs one corporate-account capability — configurable maker-checker — that Groups B, C and D all switch on according to their own governance.

Everything below follows from that.

---

## A. Roles

### A1. Is the "bank's internal auditor" the Auditing Bureau Officer?

**No. They are different actors, and the internal one is not a role at all.**

The Auditing Bureau Officer is described as an "Approved auditor" who "audits developer escrow accounts and submits independent compliance reports." Three things follow: the object of the audit is a *developer's* escrow account, not the bank's own lending; the auditor is *approved* by RERA, which Services #1 and #2 exist to grant; and the report is *independent*. A bank's internal audit desk certifying its own mortgage filing has none of those properties.

So model the internal certification step as a **checker scope** granted to a delegated staff member under Flow 5, per the mechanism above. The Auditing Bureau Officer stays what the source says it is: an approved external firm auditing developer escrow, which is Group B-facing work.

**Confidence:** High.

**If wrong:** the module gains a fifth role and a dedicated queue. The screens are broadly the same either way — what changes is provisioning, not interface.

### A2. What does the Account Trustee do in this platform?

**A full queue inside the RERA platform, not outcome recording. This is sourced — we had underread it.**

Rows 8–12 and 20–21 of the master service table put the Trustee mid-flow, acting: "Application sent to Trustee Account → Trustee Account studies capability, uploads & sends docs → Escrow account department audits by approval or rejection." The Trustee uploads documents into the flow. And the SLAs on those rows split into a waiting component and a delivery component (row 8: 20 business hours waiting, 13 delivery) — a waiting time that cannot be measured if the actor works outside the system.

So: an Escrow Request Queue with request detail, document upload, and certify/return actions.

**Confidence:** Sourced.

**Affects:** confirms the Escrow Request Queue feature already proposed in the services overview.

### A3. Is milestone certification an upload or a structured assessment?

**Structured assessment, with supporting documents attached.**

FR-04 requires "mandatory documented reasoning" on regulatory decisions, and KPI 8 sets a 95% data-integrity target measured by automated validation. A free-form certification letter can be neither validated nor aggregated. Proposed fields: milestone reference, percentage complete, valuation of works executed, amount certified, variance against the previous certificate, certifier declaration, attachments.

**Confidence:** Medium — a design judgement, not an inference.

### A4. Who owns Services #1 and #2?

**The Institution Relationship Manager. And the ownership problem is wider than these two services.**

The role descriptions are the more considered source: the IRM "maintains registration, renews trustee/auditor approvals, provisions users." That is exactly what Services #1 and #2 do. Registration Flow 4 reinforces it — the IRM is the company-level representative, and approval of the institution's own standing is a company-level act.

The service table's responsible-role column looks like a group-level default rather than a per-service assignment: it gives the Mortgage Officer seventeen of eighteen services, including heirs' sale procedures, company share sales, title-deed issuance and split ownership. Those are Trustee Centre counter transactions with no lending component. A mortgage desk does not run them.

**Recommendation:** re-derive ownership per service rather than accepting the column. Proposed:

| Services | Proposed owner |
| :---- | :---- |
| #1, #2 — institutional approval | Institution Relationship Manager |
| #3–#7 — mortgage lifecycle | Mortgage Officer |
| #8–#11 — finance lease lifecycle | Mortgage Officer |
| #12–#18 — title and ownership transactions | Mortgage Officer where bank-originated; otherwise executed by a Trustee Centre operator on the customer's behalf (Group G) |

**Confidence:** High for #1/#2. Medium for the wider re-derivation — it contradicts a source column, and that should be visible to the client.

**Affects:** the Service Ownership table in `services-overview.md`, which currently reports Mortgage Officer 17 / IRM 1.

### A5. Does the IRM get an institution-wide view?

**Yes.** Renewals and user provisioning are meaningless without visibility of expiry dates and the staff roster. Profile management (registration flows §4) assigns institutions exactly this: renew approvals, manage user provisioning, update credentials. Proposed view: approval status and expiry countdown, staff roster with permission scopes, transactions in flight by stage, settlement account balance.

**Confidence:** High.

### A6. What SLA applies to Trustee action on a routed request?

**Take it from the waiting-time figure already in the source.**

The escrow service rows carry two numbers — "waiting time 20 business hours; service delivery 13 business hours". The most plausible reading is that waiting time is the queue-and-counterparty portion and delivery is RERA's own processing. On that reading the Trustee SLA is already specified per service, and no new figure is needed.

Where a row gives only one number, propose 24 business hours with escalation to the Compliance & Escrow Auditor on breach.

**Confidence:** Medium — the two-number interpretation is an inference and should be put to the client explicitly, because every escrow SLA in Group B depends on it.

### A7. Does the compliance report follow a RERA template?

**RERA-defined template.** FR-19 requires configurable reports exportable across all regulatory service areas, and KPI 8 measures data integrity by automated validation. Neither works over documents in institution-specific formats. Allow a free-text findings narrative inside a fixed structure.

**Confidence:** Medium.

---

## B. Payments

### B1. Standing account or direct debit?

**Standing pre-funded account. The source settles this, in a detail we had treated as noise.**

Nearly every Group C mortgage and finance-lease row lists **"Fee balance"** among the issued deliverables, alongside the certificate. A balance is not a receipt. A direct debit produces proof that one payment cleared; only a running account produces a balance worth issuing as an output document.

Supporting evidence: the SLAs on these services are 10–25 minutes end to end. Per-transaction gateway authorisation against an external bank account does not fit inside that envelope reliably; deduction from a held balance does.

**Consequence, stated plainly:** the account-management subsystem is in scope. Balance display, top-up, transaction ledger, low-balance alerting and periodic statements are all real build work that appears in no source document and no estimate. That is the item to raise with the client — not the mechanism, which the source supports, but the cost of it.

**Confidence:** High on the mechanism. The scope consequence needs sign-off.

### B2. If pre-funded, who tops up and how?

The IRM authorises; two rails — bank transfer against a unique institution reference for large amounts, payment gateway for smaller ones. Recommend this uses the **same wallet primitive proposed for individuals** (`proposed-services.md` P-22) with two account types rather than two separate builds.

**Confidence:** Medium.

### B3. What happens when an approved transaction cannot be settled?

**Approval holds for 30 calendar days, then lapses to Approval Expired.** Resubmission is required; re-audit is not, unless the underlying title has changed in the interim, in which case it is.

An indefinite hold accumulates a register of half-registered mortgages — approved but unregistered interests, invisible to a searcher. That is precisely the fraud surface the platform exists to close.

**Confidence:** Medium. The 30 days is a proposal; the principle that approvals must expire is the part we would defend.

### B4. Is there a credit arrangement?

**No negative balance.** Regulatory fees are public revenue; extending credit makes RERA an unsecured creditor of a licensed institution it also regulates. Block submission when the projected balance after fees would go negative, and warn at a configurable threshold before that.

**Confidence:** High.

### B5. Published fee schedule

**Client data — the only question here we cannot answer.**

It does not block build. FR-16 specifies a fee schedule engine, meaning fees are configuration rather than code. Treat the schedule as empty configuration to be populated at Phase 1 discovery, and build the engine against a representative test schedule. See `proposed-services.md` P-33 for who configures it.

### B6. Fee basis for mortgage services

**Ad valorem on the secured amount, banded, with a floor and a cap.** FR-16 computes fees from "application type, property value, and classification", which rules out flat-rate. Banding rather than a pure percentage keeps the calculation legible to applicants and matches how registration fees are normally struck.

**Confidence:** Medium — and it is configuration, so a wrong guess is cheap.

### B7. VAT applicability

**Applied by default to all fee-bearing services, configurable per service code.** The off-plan workflow states that "seller and purchaser fees plus VAT are computed automatically", and row 11 concerns a cap on "administrative, marketing and VAT expenses". VAT is clearly in the model; exemptions, if any, are exceptions to be configured.

**Confidence:** Medium-high.

### B8. Institutional approval fees — annual or per application?

**Per approval term, with a two-year validity and a renewal fee at renewal.**

Service #1 is "approval **/ renewal**", which is only meaningful if approvals expire. So a validity period exists and must be stated. Two years is proposed; the platform should hold it as configuration and drive the Approval Expiry Tracking feature from it.

**Confidence:** Medium-high on the structure, proposal on the duration.

### B9. Are "fee balance", "payment receipt" and "e-receipt voucher" the same thing?

**No — two things, and our earlier assumption that they were one was wrong.** This follows directly from B1.

| Term | What it is |
| :---- | :---- |
| Payment receipt / e-receipt voucher | Proof that a single transaction settled. These two are the same artefact under different names. |
| Fee balance | The standing account position after that deduction — a statement line, not a receipt. |

**Confidence:** Medium-high, contingent on B1.

**Affects:** `payments.md`, which treats all three as one electronic receipt.

### B10. Do institutions use the public refund service?

**No.** Overpayment or a voided transaction credits back to the standing account automatically, same-day. Cash-out to a commercial account happens only on account closure, and that route can reuse the public refund workflow's Ministry of Finance approval.

The public route requires bank attachments and a seven-business-day turnaround subject to Ministry approval. Applying that to a bank whose fee failed to settle on a 20-minute service is disproportionate.

**Confidence:** Medium.

---

## C. Service Structure

### C1. Are the proposed five categories acceptable?

**Adopt them, keep the reconciliation table.** Navigation is built from user-facing task grouping; RERA's internal filing categories are preserved for reporting through the reconciliation. Reversible at any point, since the services and their numbers are unchanged.

**Confidence:** High.

### C2. Should Trustee Centre–only services gain an online path?

**The question dissolves. There is one service with two access modes, not two services.**

Registration Flow 7 provisions Trustee Centre operators with individual NIMC-verified accounts and "per-operator transaction scopes", under audit. That is not a parallel paper channel — it is the same online service, operated by a trained intermediary on a walk-in customer's behalf. The counter is an *assisted mode*, not a separate system.

This is also the only reading compatible with the PRD. US-14 requires diaspora users to transact fully from outside Nigeria; Business Goal 2 targets an 80% processing-time reduction; the platform's stated purpose is removing in-person visits. A title service that can only be performed by physically attending a centre in Lagos fails all three.

**Recommendation:** document every Group C service as online-capable, with an assisted-mode annotation where the source lists the Trustee Centre as the only channel. Whether direct customer access to a given service is *enabled at launch* is then a configuration decision, not an architecture one.

**Confidence:** High.

**Reverses** the earlier assumption that counter-only should be preserved as documented.

### C3. Do the four application-management features apply?

**Yes**, unchanged. Same six-stage pipeline, same needs. They should be defined once at platform level rather than per module — see the answer to Q6 in `proposed-services.md`.

**Confidence:** High.

### C4. Are the three institution-specific features correct?

**Correct but incomplete. Five, not three.**

| Feature | Status |
| :---- | :---- |
| Internal Certification Queue | Keep — now understood as a maker-checker scope view (A1) |
| Escrow Request Queue | Keep — confirmed sourced (A2) |
| Approval Expiry Tracking | Keep — now driven by a defined validity period (B8) |
| **Settlement Account** | **Add** — balance, top-up, ledger, statements (B1) |
| **Staff & Permission Scopes** | **Add** — roster, scope assignment, revocation (A1, A5) |

**Confidence:** Medium-high.

---

## D. Platform-Wide

### D1. Status vocabulary — platform-wide or per module?

**Platform-wide core, with module extensions.**

FR-18 requires a live operational dashboard across all submissions and FR-19 requires configurable reports "covering all regulatory service areas". Neither is buildable over per-module vocabularies — you cannot count what is at-risk across the platform if each module names its own states.

**Proposed core lifecycle, applying to every module:**

| Status | Meaning |
| :---- | :---- |
| Draft | Started, not submitted |
| Submitted | Lodged, awaiting regulator pickup |
| Under Review | With the regulator |
| Information Requested | Regulator has raised a query |
| Returned for Correction | Sent back to the applicant |
| Approved — Awaiting Payment | Passed audit; fee not yet settled |
| Rejected | Refused with documented reason |
| Completed | Settled and output document issued |
| Withdrawn | Abandoned by the applicant |
| Expired | Lapsed against a statutory or configured window (see B3) |

**Group C extension:** *Pending Internal Certification* and *Returned by Certifier*, both sitting before Submitted. Any group that enables maker-checker inherits the same two.

**Confidence:** High on the principle, proposal on the specific list.

### D2. Does the two-gate pattern apply beyond Group C?

**Yes, and it is a corporate-account feature rather than a group property** — see the mechanism at the top of this document.

The evidence is already in Group B: the Developer Principal "authorises project registrations, escrow drawdowns and completion filings" that the Project Registration Officer and Escrow Liaison prepare. That is a maker-checker gate under a different name. Group D shows the same shape with the Company Dispute Filing Officer under the Brokerage Principal.

Build it once, configurable per corporate account, with the scope set at the point Flow 5 already provides for it.

**Confidence:** High.

---

## Summary

| Area | Questions | Answered | Needs client data |
| :---- | :---: | :---: | :---: |
| A. Roles | 7 | 7 | 0 |
| B. Payments | 10 | 9 | 1 (B5, fee schedule) |
| C. Service structure | 4 | 4 | 0 |
| D. Platform-wide | 2 | 2 | 0 |
| **Total** | **23** | **22** | **1** |

### The four answers that change existing documents

| Answer | What it changes |
| :---- | :---- |
| **A4** — ownership re-derived per service | `services-overview.md` Service Ownership table |
| **B1** — standing account confirmed | `payments.md`; adds a Settlement Account feature and an unscoped subsystem to the estimate |
| **B9** — fee balance is not a receipt | `payments.md`, which currently merges all three terms |
| **C2** — counter is an assisted mode | Every Group C service flow's channel section; reverses a prior assumption |

### The three to put in front of the client anyway

Not because we lack an answer, but because the answer costs money or contradicts the source:

1. **B1** — the settlement account subsystem is real build work that nobody has estimated.
2. **A4** — our proposed ownership contradicts a column in the source workbook.
3. **A6** — the waiting-time / delivery-time reading sets the SLA for every escrow service in Group B, not just Group C.
