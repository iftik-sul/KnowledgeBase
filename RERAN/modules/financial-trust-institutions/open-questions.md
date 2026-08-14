---
project: RERAN
module: financial-trust-institutions
type: decision
status: draft
updated: 2026-08-14
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

**2026-08-14 update.** The payment questions (B1, B2, B4, B5, B6) were corrected following a client decision confirmed via discussion (not a written source document): Group C runs no standing account. Payment is per-transaction, upfront, via a shared platform-wide gateway, with RERA setting the fee per service directly. B9 and B10, both built entirely on the now-retired standing-account mechanism, are superseded rather than reworked. See each answer below for what changed and why the earlier reasoning is kept rather than deleted.

**How to read this:** each answer states a recommendation, the reasoning behind it, how confident we are, and what breaks if it is wrong. Confidence is:

| Level | Meaning |
| :---- | :---- |
| **Sourced** | The source material answers this; we had missed it or read it too narrowly |
| **High** | A strong inference from the source, or the only option that survives contact with the PRD |
| **Medium** | A reasonable design judgement; a different answer would also be defensible |
| **Client data** | Cannot be reasoned to. Only RERA holds the answer |

**All twenty-three questions are now answered; none require client data**, as of the 2026-08-14 payment-model correction resolving B5 (previously the sole client-data item).

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

**Yes.** Renewals and user provisioning are meaningless without visibility of expiry dates and the staff roster. Profile management (registration flows §4) assigns institutions exactly this: renew approvals, manage user provisioning, update credentials. Proposed view: approval status and expiry countdown, staff roster, transactions in flight by stage, payment history.

**Corrected 2026-08-14** — previously proposed "staff roster with permission scopes" and "settlement account balance"; permission scopes are retired module-wide and there is no standing account to hold a balance (see the corrected A1 mechanism and B1). Reworded to "staff roster" and "payment history," consistent with `services-overview.md`'s Feature #8 (Payment History) and Feature #9 (Staff Records).

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

**Corrected 2026-08-14 (client decision, via discussion — not a written source document): direct, per-transaction payment via a shared platform-wide payment gateway. No standing account.**

Payment is required **upfront** — before the application can even be lodged, not after RERA approval. RERA sets the fee for each service directly; the amount is not derived from loan value, property value, or any other institution-side figure (see the corrected B6). This reverses the payment position in the platform-core pipeline for Group C specifically: **Pay** now comes first, ahead of Lodge/Validate/Audit, not after Audit.

**What's superseded, and why it isn't silently dropped:** the reasoning below concluded a standing pre-funded account from the source's "Fee balance" deliverable wording, on the theory that only a running account produces a balance worth issuing as an output document. That evidentiary read of the source text isn't retracted — "Fee balance" genuinely appears on those rows. What's changed is that the client has now confirmed, outside the source documents, that Group C does not actually operate this way: no standing account, per-transaction, upfront. Preserved below for the record, the same way A1/D2 were kept rather than deleted when the access model was corrected.

> **Superseded reasoning (pre-2026-08-14).** Nearly every Group C mortgage and finance-lease row lists "Fee balance" among the issued deliverables, alongside the certificate. A balance is not a receipt. A direct debit produces proof that one payment cleared; only a running account produces a balance worth issuing as an output document. Supporting evidence: the SLAs on these services are 10–25 minutes end to end. Per-transaction gateway authorisation against an external bank account does not fit inside that envelope reliably; deduction from a held balance does. **Confidence was High on the mechanism.**

**Consequence, corrected.** The earlier "Consequence, stated plainly" paragraph — flagging the settlement-account subsystem (balance display, top-up, transaction ledger, low-balance alerting, periodic statements) as unscoped, unestimated build work — no longer applies. None of that subsystem exists under the corrected model. If anything, this **removes** scope from the earlier estimate concern rather than adding to it.

**Confidence:** Confirmed (client decision, 2026-08-14).

**Affects:** `payments.md` (near-total rewrite), the Institution Account Management section (removed), Section 8/9 of every mortgage and finance-lease service-flow file (#3–#11), Group C's use of the `Approved — Awaiting Payment` status, and B9/B10 (both superseded below).

### B2. If pre-funded, who tops up and how?

**Corrected 2026-08-14 — the question dissolves along with B1.** There is no standing account to top up. Payment is per-transaction, via **one shared platform-wide payment gateway** — not two funding rails (bank transfer plus gateway), and not restricted to the Institution Relationship Manager. Any user at the institution can initiate and complete payment for a transaction they're working on.

**On the P-22 equivalence claim, checked rather than assumed.** The original answer below proposed reusing individual-user's wallet primitive (`proposed-services.md` P-22) for institutional top-ups. Re-checking P-22's actual description ("Wallet account — top-up, balance, statement, refund-to-wallet") shows it is itself a **balance-holding wallet** — top-up and balance are exactly the standing-account shape B1 has now ruled out for Group C. So the equivalence claim doesn't carry over cleanly: Group C's corrected payment model (no balance, no top-up, pay-per-transaction) is not the same primitive as P-22 as P-22 is actually documented. What likely *is* shared is the underlying **payment gateway integration** (the card/bank-transfer/USSD rails P-22 presumably sits on top of) — a narrower, lower-confidence claim than "same primitive," flagged here rather than asserted. Needs a decision on whether the shared gateway is genuinely one build artefact reused two ways (wallet-fronted for individuals, direct-charge for institutions) or two separate integrations against the same payment providers.

> **Superseded reasoning (pre-2026-08-14).** The IRM authorises; two rails — bank transfer against a unique institution reference for large amounts, payment gateway for smaller ones. Recommend this uses the same wallet primitive proposed for individuals (`proposed-services.md` P-22) with two account types rather than two separate builds. **Confidence was Medium.**

**Confidence:** Confirmed on "no standing account, one shared gateway, any user can pay" (client decision, 2026-08-14). Open on the P-22 build-sharing question — flagged above, not resolved.

**Affects:** `payments.md`'s Institution Account Management section (removed).

### B3. What happens when an approved transaction cannot be settled?

**Approval holds for 30 calendar days, then lapses to Approval Expired.** Resubmission is required; re-audit is not, unless the underlying title has changed in the interim, in which case it is.

An indefinite hold accumulates a register of half-registered mortgages — approved but unregistered interests, invisible to a searcher. That is precisely the fraud surface the platform exists to close.

**Confidence:** Medium. The 30 days is a proposal; the principle that approvals must expire is the part we would defend.

### B4. Is there a credit arrangement?

**Corrected 2026-08-14 — moot.** There is no account to extend credit against, and nothing that could carry a negative balance. Payment is per-transaction and upfront; a transaction either pays successfully or it doesn't proceed. The original question assumed a standing balance that could run below zero, which no longer exists under the corrected B1.

> **Superseded reasoning (pre-2026-08-14).** No negative balance. Regulatory fees are public revenue; extending credit makes RERA an unsecured creditor of a licensed institution it also regulates. Block submission when the projected balance after fees would go negative, and warn at a configurable threshold before that. **Confidence was High.**

**Confidence:** Confirmed — moot, not answered (client decision, 2026-08-14).

### B5. Published fee schedule

**Corrected 2026-08-14 — resolved, not client data.** There is no fee schedule document to obtain from the client. RERA sets a fee per service directly; the amount is configuration, populated through the fee-schedule engine (FR-16), the same way the corrected B6 (below) describes it — not missing source data to chase.

> **Superseded framing (pre-2026-08-14).** Client data — the only question here we cannot answer. It does not block build; FR-16 specifies a fee schedule engine, meaning fees are configuration rather than code. Treat the schedule as empty configuration to be populated at Phase 1 discovery.

The FR-16 configuration-engine reasoning survives intact — it was correct — only the framing changes: from "waiting on the client for missing data" to "this is how the system is meant to work, and RERA populates its own configuration," since there was never a separate published document to request. Build the engine against a representative test schedule; see `proposed-services.md` P-33 for who configures it.

**Confidence:** Confirmed (client decision, 2026-08-14). **This is now 23 of 23 questions answered, 0 needing client data** — see the corrected Summary below.

**Affects:** `payments.md`'s Fee Calculation and To Confirm — Summary sections; `services-overview.md`'s To Confirm item on the payer-model split.

### B6. Fee basis for mortgage services

**Corrected 2026-08-14 — two separate things, previously conflated.**

1. **The financial institution's own commercial relationship with its customer** — loan amount, interest rate, mortgage term, and any other lending economics — is entirely outside RERA's concern. It is never derived, referenced, or documented in any RERA-facing fee description in this module.
2. **RERA's own per-service fee** is set by RERA directly, configured through the fee-schedule engine (FR-16), independent of loan value, property value, banding, floor, or cap. A flat, RERA-determined figure per service code — the same mechanism the corrected B5 describes.

The earlier answer's "ad valorem on the secured amount" reasoning blurred this boundary, pricing RERA's fee off a figure that belongs to the FI-customer relationship, not to RERA.

> **Superseded reasoning (pre-2026-08-14).** Ad valorem on the secured amount, banded, with a floor and a cap. FR-16 computes fees from "application type, property value, and classification", which rules out flat-rate. Banding rather than a pure percentage keeps the calculation legible to applicants and matches how registration fees are normally struck. **Confidence was Medium.**

**Confidence:** Confirmed on the RERA-sets-it-directly principle (client decision, 2026-08-14). FR-16's "application type... classification" language may still describe how RERA itself varies the fee by service type — compatible with "RERA sets a fee per service" — but a per-loan ad valorem calculation is specifically ruled out.

**Affects:** `payments.md`'s Fee Calculation section; Section 8 (Service Fee) of every mortgage and finance-lease service-flow file (#3–#11).

### B7. VAT applicability

**Applied by default to all fee-bearing services, configurable per service code.** The off-plan workflow states that "seller and purchaser fees plus VAT are computed automatically", and row 11 concerns a cap on "administrative, marketing and VAT expenses". VAT is clearly in the model; exemptions, if any, are exceptions to be configured.

**Confidence:** Medium-high.

### B8. Institutional approval fees — annual or per application?

**Per approval term, with a two-year validity and a renewal fee at renewal.**

Service #1 is "approval **/ renewal**", which is only meaningful if approvals expire. So a validity period exists and must be stated. Two years is proposed; the platform should hold it as configuration and drive the Approval Expiry Tracking feature from it.

**Confidence:** Medium-high on the structure, proposal on the duration.

### B9. Are "fee balance", "payment receipt" and "e-receipt voucher" the same thing?

**Superseded by the corrected B1 — not reworked, retired.** B9's question was built entirely on the standing-account mechanism B1 established: it distinguished a "fee balance" (a standing-account statement line) from a "payment receipt" (proof a single transaction settled) precisely because both artefacts existed side-by-side under the old model. With no standing account, there is no fee balance to distinguish from anything — every payment is a single, per-transaction event, and **payment receipt** (the same artefact "e-receipt voucher" already named under a different name) is simply what every Group C service now issues. See `payments.md`'s reworked Payment Artefacts section.

**Affects:** `payments.md`; every mortgage and finance-lease service-flow file's Output section (the "Fee Balance" bullet is removed, not renamed); `service-01`'s payment section.

### B10. Do institutions use the public refund service?

**Superseded by the corrected B1 — not reworked, retired.** B10's "same-day automatic credit-back" answer assumed a standing account to credit back into. With no standing account, there is nothing to credit back to automatically. A failed institutional payment is handled the same way any other per-transaction payment failure is (see `payments.md`'s reworked Failed and Reversed Payments section); a settled payment needing reversal now has no obvious reason to bypass the platform's public refund route the way the old answer argued — that argument rested on protecting a standing account's same-day reconciliation, which no longer exists. Whether Group C should still get an expedited refund path on other grounds is not addressed here and is not assumed either way.

**Affects:** `payments.md`'s Failed and Reversed Payments and Additional Statuses sections.

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
| **Payment History** | **Add** — per-transaction payment records: receipts, amounts, service references, status (B1) |
| **Staff Records** | **Add** — roster and staff-record management (A1, A5) |

**Corrected 2026-08-14** — this row previously read "Settlement Account | Add — balance, top-up, ledger, statements (B1)" and "Staff & Permission Scopes | Add — roster, scope assignment, revocation (A1, A5)". Both features survive, renamed: there is no standing account for the first (B1, corrected) and no scopes to assign or revoke for the second (A1, corrected) — see `services-overview.md`'s Feature #8 and Feature #9, which this table now matches.

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

**Updated 2026-08-14** — B5 moved from "needs client data" to "answered," per the payment-model correction (B1).

| Area | Questions | Answered | Needs client data |
| :---- | :---: | :---: | :---: |
| A. Roles | 7 | 7 | 0 |
| B. Payments | 10 | 10 | 0 |
| C. Service structure | 4 | 4 | 0 |
| D. Platform-wide | 2 | 2 | 0 |
| **Total** | **23** | **23** | **0** |

### The answers that change existing documents

| Answer | What it changes |
| :---- | :---- |
| **A4** — ownership re-derived per service | `services-overview.md` Service Ownership table |
| **B1** — corrected 2026-08-14: no standing account, pay-per-transaction upfront via a shared gateway | `payments.md` (near-total rewrite); every mortgage/finance-lease service flow's Service Fee, Payment Required and Output sections; `services-overview.md`'s status vocabulary and features list; `navigation.md` and `role-workflows.md`'s settlement references; `module-roadmap.md`'s platform-wide payment-pipeline claim (see that file's own note on why) |
| **C2** — counter is an assisted mode | Every Group C service flow's channel section; reverses a prior assumption |

B9 and B10 are not listed separately above — both are superseded by the corrected B1 rather than independently reworked; see their entries for what that means for `payments.md`.

### The two to put in front of the client anyway

Not because we lack an answer, but because the answer costs money, contradicts the source, or rests on an assumption worth surfacing:

1. **A4** — our proposed ownership contradicts a column in the source workbook.
2. **A6** — the waiting-time / delivery-time reading sets the SLA for every escrow service in Group B, not just Group C.

**One more, downgraded from "put in front of the client" to "flagged for design":** B2's claim that the shared payment gateway reuses individual-user's wallet primitive (P-22) doesn't survive a check against P-22's actual description, which is itself balance-based — the opposite of Group C's now-confirmed no-standing-account model. Worth a decision on whether the gateway integration is genuinely shared build, but this is an internal design question, not something requiring the client's input the way A4 and A6 do.
