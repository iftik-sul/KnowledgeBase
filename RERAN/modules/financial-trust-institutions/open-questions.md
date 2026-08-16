---
project: RERAN
module: financial-trust-institutions
type: decision
status: draft
updated: 2026-08-16
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

Twenty-three questions arose from documenting the Financial & Trust Institutions module. Rather than hold the module until the client responds, each now carries a **proposed answer** we will build against unless told otherwise. A twenty-fourth item (B11) was added 2026-08-15, not from the original documentation pass but from a further client decision on institutional-approval payment timing — see below.

**2026-08-14 update.** The payment questions (B1, B2, B4, B5, B6) were corrected following a client decision confirmed via discussion (not a written source document): Group C runs no standing account. Payment is per-transaction, upfront, via a shared platform-wide gateway, with RERA setting the fee per service directly. B9 and B10, both built entirely on the now-retired standing-account mechanism, are superseded rather than reworked. See each answer below for what changed and why the earlier reasoning is kept rather than deleted.

**2026-08-15 update.** A4 is corrected: ownership is not role-specific at all, for any of the 18 services — a client decision, not a re-derivation. A3, B7, and B8 are confirmed by the client, matching their existing proposed answers. A6 is also confirmed by the client. **B11 is added**: the client has further decided that Service #1 (Approval/Renewal) now pays upfront, merging into the same model as Services #3–#11, and confirmed Service #2 (Cancellation) carries no fee at all — see B11 below. See each answer below.

**2026-08-16 update.** B11 is extended: the client has reviewed Services #12 and #18's payment timing directly and normalized both to pay before RERA's decision, closing the exception a fuller per-service audit had found on 2026-08-15. See B11 below for the full history. C4's answer is also corrected — see below; it had instructed adding a "Staff Records" feature that turned out to already exist inside Institution Profile.

**How to read this:** each answer states a recommendation, the reasoning behind it, how confident we are, and what breaks if it is wrong. Confidence is:

| Level | Meaning |
| :---- | :---- |
| **Sourced** | The source material answers this; we had missed it or read it too narrowly |
| **High** | A strong inference from the source, or the only option that survives contact with the PRD |
| **Medium** | A reasonable design judgement; a different answer would also be defensible |
| **Client data** | Cannot be reasoned to. Only RERA holds the answer |

**All twenty-four questions are now answered; none require client data.**

**Scope note:** post-login functionality only. Registration and onboarding are excluded.

---

## The Answer That Resolves Two Questions

A1 and D2 dissolve into a single mechanism, so it is stated once here.

**Internal certification is a permission scope on a corporate account, not a role.**

Registration Flow 5 already establishes the machinery: delegated staff are invited by the company's authorised representative, who "confirms the staff member's permission scope (e.g. escrow filing only)" before activation. A maker-checker gate is that same mechanism with a second scope — *certify* alongside *file*.

This means the platform needs no fifth Group C role, and no separate two-gate model per group. It needs one corporate-account capability — configurable maker-checker — that Groups B, C and D all switch on according to their own governance.

> **Superseded 2026-08-14.** The permission-scope mechanism described in this section is retired module-wide. Certification is now an unrestricted action any of the institution's four Group C roles may perform, attributed by role in the audit trail — see [navigation.md#audit-trail-principle](navigation.md#audit-trail-principle). Kept here for the record, per A1 and D2 below.

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

**Confirmed 2026-08-15 (client decision) — structured assessment, with supporting documents attached.**

FR-04 requires "mandatory documented reasoning" on regulatory decisions, and KPI 8 sets a 95% data-integrity target measured by automated validation. A free-form certification letter can be neither validated nor aggregated. Proposed fields: milestone reference, percentage complete, valuation of works executed, amount certified, variance against the previous certificate, certifier declaration, attachments.

**Confidence:** Confirmed (client decision, 2026-08-15). Originally a Medium-confidence design judgement, now confirmed directly rather than left as an inference.

### A4. Who owns Services #1–#18?

**Confirmed 2026-08-15 (client decision) — no service is role-specific at all. Any of the institution's four Group C roles (Mortgage Officer, Institution Relationship Manager, Account Trustee, Auditing Bureau Officer) may act on any of the 18 services.**

This resolves, rather than re-derives, the ownership question the source table raised. The source's responsible-role column is still unreliable as a per-service assignment — it names the Mortgage Officer for 15 of the 18 rows (30–44), including heirs' sale, company share sales, split ownership, and title-deed issuance, transactions with no lending component that a bank's mortgage desk would not plausibly run alone. That observation, which motivated the per-service re-derivation below, remains accurate as a critique of the source. What's changed is the conclusion: rather than building a corrected per-role assignment table, the client has confirmed that Group C simply does not assign services to roles at all. Role is retained solely for audit-trail attribution — who performed which action — consistent with the access-model correction ([navigation.md#audit-trail-principle](navigation.md#audit-trail-principle)), not for gating who may initiate, own, or act on a service.

**Trustee Centre Operator (Group G) is not part of this answer.** It is a channel/assisted-mode role, not a Group C role — a Trustee Centre operator may still act on an institution's or customer's behalf in assisted mode, exactly as C2 describes, but that is a channel question, not an ownership one, and it is unaffected by this correction.

> **Superseded reasoning (pre-2026-08-15).** The role descriptions were the more considered source: the IRM "maintains registration, renews trustee/auditor approvals, provisions users." That is exactly what Services #1 and #2 do. Registration Flow 4 reinforces it — the IRM is the company-level representative, and approval of the institution's own standing is a company-level act.
>
> The service table's responsible-role column looked like a group-level default rather than a per-service assignment: it gives the Mortgage Officer seventeen of eighteen services, including heirs' sale procedures, company share sales, title-deed issuance and split ownership. Those are Trustee Centre counter transactions with no lending component. A mortgage desk does not run them.
>
> **Recommendation was:** re-derive ownership per service rather than accepting the column. Proposed:
>
> | Services | Proposed owner |
> | :---- | :---- |
> | #1, #2 — institutional approval | Institution Relationship Manager |
> | #3–#7 — mortgage lifecycle | Mortgage Officer |
> | #8–#11 — finance lease lifecycle | Mortgage Officer |
> | #12–#18 — title and ownership transactions | Mortgage Officer where bank-originated; otherwise executed by a Trustee Centre operator on the customer's behalf (Group G) |
>
> **Confidence was High for #1/#2. Medium for the wider re-derivation** — it contradicted a source column, and that was flagged to be put in front of the client, which is how this question reached the 2026-08-15 decision above.

**Confidence:** Confirmed (client decision, 2026-08-15).

**Affects:** `services-overview.md`'s Service Ownership section (removed entirely, not reworked); Section 4 (Who Can Apply) and Business Rule 1 of Services #3–#11 and #12–#18; `service-01` and `service-02`'s ownership framing; `roles-and-responsibilities.md`'s Role Summary table.

### A5. Does the IRM get an institution-wide view?

**Yes.** Renewals and user provisioning are meaningless without visibility of expiry dates and the staff roster. Profile management (registration flows §4) assigns institutions exactly this: renew approvals, manage user provisioning, update credentials. Proposed view: approval status and expiry countdown, staff roster, transactions in flight by stage, payment history.

**Corrected 2026-08-14** — previously proposed "staff roster with permission scopes" and "settlement account balance"; permission scopes are retired module-wide and there is no standing account to hold a balance (see the corrected A1 mechanism and B1). Reworded to "staff roster" and "payment history," consistent with `services-overview.md`'s Feature #8 (Payment History) and Feature #9 (Staff Records).

**Confidence:** High.

### A6. What SLA applies to Trustee action on a routed request?

**Confirmed 2026-08-15 (client decision) — the two-number reading is correct. No new SLA needed.**

The escrow service rows carry two numbers — "waiting time 20 business hours; service delivery 13 business hours". Waiting time is the queue-and-counterparty portion (how long the request sits before the Account Trustee acts on it); delivery time is RERA's own processing after that. The client has confirmed this reading directly. The Trustee SLA is already specified per service, in source, and no new figure needs to be invented — this applies across Group B's escrow services as well as Group C's, since the same two-number pattern and the same question applied to both.

Where a row gives only one number, propose 24 business hours with escalation to the Compliance & Escrow Auditor on breach. This part of the answer was not put to the client and remains a proposal, not a confirmed figure — see Confidence below.

> **Superseded framing (pre-2026-08-15).** This reading was carried as a Medium-confidence inference, flagged explicitly to put in front of the client because every escrow SLA in Group B depended on it. That flag is resolved now; the reasoning survives unchanged, only the confidence status changes.

**Confidence:** Confirmed on the two-number reading (client decision, 2026-08-15). The 24-business-hour single-number fallback remains a Medium-confidence proposal, not separately confirmed.

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

**Confidence:** Confirmed (client decision, 2026-08-14).

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

**Confirmed 2026-08-15 (client decision) — VAT applies to all 18 services. No exemptions.**

The off-plan workflow states that "seller and purchaser fees plus VAT are computed automatically", and row 11 concerns a cap on "administrative, marketing and VAT expenses". VAT is clearly in the model, and the client has now confirmed it applies universally across the service catalogue rather than being configurable per service or subject to exemption.

**Confidence:** Confirmed (client decision, 2026-08-15). Previously Medium-high, proposed as "applied by default, configurable per service code, with exemptions as exceptions" — the exemption possibility is now ruled out rather than left configurable.

### B8. Institutional approval fees — annual or per application?

**Confirmed 2026-08-15 (client decision) — per approval term, renewing, matching the existing proposal.**

Service #1 is "approval **/ renewal**", which is only meaningful if approvals expire. The client has confirmed the renewing structure directly. The two-year validity period itself remains a proposal, not a sourced or separately confirmed figure — the platform should hold it as configuration and drive the Approval Expiry Tracking feature from it.

**Confidence:** Confirmed on the renewing structure (client decision, 2026-08-15). The two-year duration specifically remains a proposal.

### B9. Are "fee balance", "payment receipt" and "e-receipt voucher" the same thing?

**Superseded by the corrected B1 — not reworked, retired.** B9's question was built entirely on the standing-account mechanism B1 established: it distinguished a "fee balance" (a standing-account statement line) from a "payment receipt" (proof a single transaction settled) precisely because both artefacts existed side-by-side under the old model. With no standing account, there is no fee balance to distinguish from anything — every payment is a single, per-transaction event, and **payment receipt** (the same artefact "e-receipt voucher" already named under a different name) is simply what every Group C service now issues. See `payments.md`'s reworked Payment Artefacts section.

**Affects:** `payments.md`; every mortgage and finance-lease service-flow file's Output section (the "Fee Balance" bullet is removed, not renamed); `service-01`'s payment section.

### B10. Do institutions use the public refund service?

**Superseded by the corrected B1 — not reworked, retired.** B10's "same-day automatic credit-back" answer assumed a standing account to credit back into. With no standing account, there is nothing to credit back to automatically. A failed institutional payment is handled the same way any other per-transaction payment failure is (see `payments.md`'s reworked Failed and Reversed Payments section); a settled payment needing reversal now has no obvious reason to bypass the platform's public refund route the way the old answer argued — that argument rested on protecting a standing account's same-day reconciliation, which no longer exists. Whether Group C should still get an expedited refund path on other grounds is not addressed here and is not assumed either way.

**Affects:** `payments.md`'s Failed and Reversed Payments and Additional Statuses sections.

### B11. Does Service #1 (Approval/Renewal) pay upfront or after RERA's decision, and does Service #2 (Cancellation) carry a fee at all?

**Confirmed 2026-08-15 (client decision) — Service #1 now pays upfront, before lodging, merging into the same Upfront Gateway Payment model as Services #3–#11. Service #2 carries no fee at all.**

Row 28's sequencing — "Payment of fees" listed after the approval decision — was the sourced basis for the previous **Institution Fee Payment** model, in which #1–#2 paid only after RERA's audit decision, and a new #1 approval additionally required a signed partner agreement before completion. The client has now confirmed a change from that sourced sequencing: Service #1's fee is paid upfront, via the same shared-gateway checkout used by Services #3–#11, before the application is lodged. Service #2 is confirmed to carry no fee at all — resolving `service-02`'s own Open Questions item 1 ("does cancellation carry a fee?"), which had been left genuinely open pending confirmation either way.

**With this decision, the Institution Fee Payment model as a distinct payer/timing category is retired.** Service #1 folds into Upfront Gateway Payment; Service #2 has no payment step to categorize at all. Group C now runs **two** payment models, not three: Upfront Gateway Payment (#1, #3–#11) and Customer Payment at Counter (#12–#18).

**The partner agreement signing required for a new Service #1 approval (sourced, row 28) is unaffected by this change.** It remains a post-audit-decision step, independent of when payment happens: payment funds the application at lodging; the agreement is signed once RERA has approved, before completion.

This is a genuinely new decision, not a re-derivation or a resolution of an ambiguity in the source — row 28's post-decision payment sequencing was correctly read the first time; the client has since decided to build differently from what the source describes for #1, and has separately clarified that #2 was never chargeable at all.

**Extended 2026-08-16 — Services #12 and #18 normalized to the same before-decision pattern.** A fuller per-service audit on 2026-08-15 found that #12 (Registration of Real Estate Fund Companies) and #18 (Contract Cancellation) genuinely sourced RERA's decision *before* the customer's counter payment — a real exception within the Customer Payment at Counter model, distinct from #13–#17, which pay before the decision. The client has since reviewed that exception directly, confirmed it was an artefact of the source's original physical-counter process rather than intentional design, and normalized both services to pay before RERA's decision, closing the gap. **Group C's payment models are now genuinely two, without exception**: Upfront Gateway Payment (#1, #3–#11) and Customer Payment at Counter, before RERA's decision (#12–#18). See `service-12` and `service-18`'s own files for the normalization itself.

**Confidence:** Confirmed (client decision, 2026-08-15; extended 2026-08-16).

**Affects:** `payments.md` (pipeline table, Who Pays table, sequence diagrams, Fee Calculation, Additional Statuses); `services-overview.md` (Payments feature bullet, Application Status Vocabulary's `Approved — Awaiting Payment` and `Expired` notes — neither now applies to any Group C service); `service-01`'s Sections 8, 9, 12, 13, 21; `service-02`'s Sections 8, 9, and Open Questions; `service-12` and `service-18`'s Sections 3, 9, 12, 13, 20, 21 (2026-08-16 extension); `status-badges.md`, `validation-rules.md`, `role-workflows.md`, and every UI screen and feature document that had described the #12/#18 exception.

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

**Correct but incomplete. Five, not three — and one of the two additions turned out already built into an existing feature, not a new one.**

| Feature | Status |
| :---- | :---- |
| Internal Certification Queue | Keep — now understood as an unrestricted action any of the institution's four roles may perform (A1), not a maker-checker scope view |
| Escrow Request Queue | Keep — confirmed sourced (A2) |
| Approval Expiry Tracking | Keep — now driven by a defined validity period (B8) |
| **Payment History** | **Add** — per-transaction payment records: receipts, amounts, service references, status (B1) |
| **Staff Records** | **Already covered — not a separate feature.** Roster and staff-record management (A1, A5) is part of the existing Institution Profile feature's own scope, not a new addition — see the correction note below. |

**Corrected 2026-08-14** — this row previously read "Settlement Account | Add — balance, top-up, ledger, statements (B1)" and "Staff & Permission Scopes | Add — roster, scope assignment, revocation (A1, A5)". The first survives, renamed, as Payment History: there is no standing account for it to describe any more (B1, corrected). The second was originally kept as a separate "Staff Records" addition, reasoning that there were no longer scopes to assign or revoke, only a roster.

**Corrected again 2026-08-16.** That "Staff Records" addition was never built as a separate feature or screen — when [feature-10-institution-profile.md](service-flows/feature-10-institution-profile.md) was written, the staff roster was documented as one section of Institution Profile (Section 3, "Description"), not as a standalone feature. On review, that turns out to be the more accurate design: staff records are institution-standing information, the same category as approval status and expiry, and belong alongside it rather than as a separately-numbered feature. This table is corrected to say so directly, so a future reader doesn't treat "Staff Records: Add" as an outstanding action — it is neither outstanding nor a new feature; it was folded into Institution Profile from the start of that document's own rebuild.

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

**Note, added 2026-08-16:** `Approved — Awaiting Payment` remains part of this proposed platform-wide core list — it is a generic status a module *could* need, and other modules (e.g. Real Estate Developer's Service #24, which has two separate payment stages) may still use it. It no longer describes any Group C service specifically, following the 2026-08-16 normalization of Services #12 and #18 (see B11) — Group C's own status vocabulary is documented in `status-badges.md`, not this platform-wide proposal.

**Confidence:** High on the principle, proposal on the specific list.

### D2. Does the two-gate pattern apply beyond Group C?

**Yes, and it is a corporate-account feature rather than a group property** — see the mechanism at the top of this document.

The evidence cited here was Group B: the Developer Principal "authorises project registrations, escrow drawdowns and completion filings" that the Project Registration Officer and Escrow Liaison prepare — a maker-checker gate under a different name. Group D shows the same shape with the Company Dispute Filing Officer under the Brokerage Principal.

> **Corrected 2026-08-15 — the Group B half of this evidence no longer holds.** Issue #58 applied the same unified-access decision to Group B: its four roles no longer gate access, and there is explicitly no maker ≠ checker restriction there either (see [`../real-estate-developer/navigation.md`](../real-estate-developer/navigation.md)). A Developer Principal's authorisation is now customary practice, not an enforced gate. **Group D remains valid evidence** and the answer above is unchanged on its merits — the two-gate pattern is still a configurable corporate-account feature rather than a group property — but it now rests on Group D and Group C's own certification step, not on Group B.

Build it once, configurable per corporate account, with the scope set at the point Flow 5 already provides for it.

**Confidence:** High.

---

## Summary

**Updated 2026-08-16** — A4 and A6 moved from "flagged for the client" to confirmed by client decision; A3, B7, B8 moved from proposed to confirmed. B5 moved from "needs client data" to "answered" on 2026-08-14, per the payment-model correction (B1). **B11 added and then extended**: Service #1 pays upfront, Service #2 carries no fee (2026-08-15); Services #12 and #18 normalized to pay before RERA's decision, closing the exception a fuller audit had found (2026-08-16). **C4 corrected**: its "Staff Records — Add" instruction is stale; that content already lives inside Institution Profile. **All 24 questions are now confirmed or resolved, and nothing remains on the "put in front of the client" list.**

| Area | Questions | Answered | Needs client data |
| :---- | :---: | :---: | :---: |
| A. Roles | 7 | 7 | 0 |
| B. Payments | 11 | 11 | 0 |
| C. Service structure | 4 | 4 | 0 |
| D. Platform-wide | 2 | 2 | 0 |
| **Total** | **24** | **24** | **0** |

### The answers that change existing documents

| Answer | What it changes |
| :---- | :---- |
| **A4** — confirmed 2026-08-15: no service is role-specific | `services-overview.md`'s Service Ownership section (removed entirely); Section 4 and Business Rule 1 of Services #3–#18; `roles-and-responsibilities.md`'s Role Summary table |
| **A6** — confirmed 2026-08-15: the two-number SLA reading is correct | No document changes required — this confirms the reading already reflected in `services-overview.md`'s Escrow Request Queue feature and the individual escrow service flows in Group B; no new SLA figure needs to be introduced |
| **B1** — corrected 2026-08-14: no standing account, pay-per-transaction upfront via a shared gateway | `payments.md` (near-total rewrite); every mortgage/finance-lease service flow's Service Fee, Payment Required and Output sections; `services-overview.md`'s status vocabulary and features list; `navigation.md` and `role-workflows.md`'s settlement references; `module-roadmap.md`'s platform-wide payment-pipeline claim (see that file's own note on why) |
| **B11** — confirmed 2026-08-15, extended 2026-08-16: Service #1 pays upfront, Service #2 carries no fee, Services #12/#18 normalized to pay before RERA's decision | `payments.md` (pipeline/Who Pays tables, sequence diagrams, Fee Calculation, Additional Statuses); `services-overview.md`'s Payments feature bullet and Application Status Vocabulary notes; `service-01`'s Sections 8, 9, 12, 13, 21; `service-02`'s Sections 8, 9, and Open Questions; `service-12` and `service-18`'s own files; `status-badges.md`, `validation-rules.md`, `role-workflows.md`, and every UI screen and feature document describing the #12/#18 exception |
| **C2** — counter is an assisted mode | Every Group C service flow's channel section; reverses a prior assumption |
| **C4** — corrected 2026-08-16: "Staff Records" already lives in Institution Profile, not a separate feature | This document's own C4 table above; no other document needed correction, since `feature-10-institution-profile.md` had it right from the start |

B9 and B10 are not listed separately above — both are superseded by the corrected B1 rather than independently reworked; see their entries for what that means for `payments.md`.

### The client-facing list — now empty

As of 2026-08-15, all items that had been flagged to put in front of the client directly are resolved:

1. ~~**A4**~~ — resolved by client decision 2026-08-15; no service is role-specific.
2. ~~**A6**~~ — resolved by client decision 2026-08-15; the two-number SLA reading is confirmed correct.
3. ~~**B11**~~ — resolved by client decision 2026-08-15, extended 2026-08-16; Service #1 pays upfront, Service #2 carries no fee, and Services #12/#18 are normalized to the same before-decision timing as the rest of the Customer Payment at Counter model. This one was never on the original flagged list (it wasn't recognized as ambiguous until raised directly), but is included here for completeness since it's the same kind of direct client confirmation as A4 and A6.

**One remaining item, still flagged for internal design rather than the client:** B2's claim that the shared payment gateway reuses individual-user's wallet primitive (P-22) doesn't survive a check against P-22's actual description, which is itself balance-based — the opposite of Group C's now-confirmed no-standing-account model. Worth a decision on whether the gateway integration is genuinely shared build, but this is an internal design question, not something requiring the client's input the way A4, A6, and B11 did.
