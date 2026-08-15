---
project: RERAN
module: individual-user
type: overview
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
  - "RERAN/modules/individual-user/open-questions.md"
tags:
  - individual-user
  - payments
---

# Individual User — Payments

Every one of the 43 documented services was checked individually against its own sourced row in `RERAN_service_flows_v2.md` (rows 72–112, Groups E and F) before writing anything below. `module-roadmap.md`'s own cross-cutting note on payment timing — corrected four times while auditing Groups B and C, and explicitly warning that this module was "unaudited" — is the standing instruction this document follows. The short version of what that audit found: **payment timing in this module is not uniform, cannot be inferred from a neighbouring service, and every one of the 43 files needed to be read on its own terms.** Several were.

**This is a first pass, not a correction of prior work** — `payments.md` did not exist before this document. But 33 of the 43 existing service-flow files carry a boilerplate Section 9 ("Payment must be completed before the application is submitted") that this audit found does not match either the source or, in several cases, the file's *own* Processing Workflow section. Those files are not corrected here — this document records what the audit found; propagating the correction into each service-flow file is separate follow-up work, listed at the end.

## The Core Finding: Two Channels, Two Timings, One Boilerplate Line

A large share of Group E and F source rows describe **two channels** for the same service: an in-person Trustee Centre / Land Department counter path, and (where documented) an online/App path. Where both exist in source, they frequently have **different payment timing**:

- **Online/App channel:** payment is bundled into the submission step — pay, then submit. This is genuinely upfront.
- **Trustee Centre / counter channel:** the customer's documents are received and entered into the system, the transaction is **audited first**, and **only then** does the customer pay — usually immediately before receiving the certificate/output.

Every one of the 43 service-flow files carries a Section 9 that reads, verbatim or near-verbatim, "Payment must be completed before the application is submitted." For the online channel this is accurate. For the counter channel, wherever source documents one, **it is backwards** — and several files' own *Processing Workflow* sections (Option 1 / Service Center) already show the correct counter-channel order, while Section 9 a few hundred words later contradicts it. This is not a subtle reading; it is the same two sections of the same file disagreeing with each other on eight documents, listed in "Confirmed contradictions" below.

**Why this matters for the previous modules' precedent:** Group C's `payments.md` cites this module's Service #8 as evidence that "individual-user pays upfront" — true for #8, but that citation was made without checking the module's other 42 services, exactly the kind of single-service generalisation `module-roadmap.md` now warns against. This document is the missed audit.

## Payment Timing Categories

### Category 1 — Upfront, before submission (confirmed, both channels agree or only one channel is sourced)

Services #1–#4, #6, #8, #19–#22, #29, #30, #35–#38, #43, and the extrapolated verification/diaspora/complaint services (#1–#3, #36–#37) either have no counter-channel alternative sourced, or the sourced counter-channel order genuinely places payment before the final audit/approval decision. Section 9's "before submission" language is correct for these as written, though see the Category 4 note on #38 below.

Representative source: Service #8 (row 87) — *"Customer pays fees, receives receipt via email. Auditor of Department processes..."* — payment precedes the auditor's processing. Services #19–#22 and #35 (rows 100–105) all read the same way: "...employee enters data, **pay**, transaction audited and approved, receive link via email."

### Category 2 — Sourced to pay *after* RERA's audit/decision, but the file's Section 9 claims "before submission." Confirmed contradictions.

These are the clearest, most defensible findings — the source is unambiguous and, in three cases, the file's own Processing Workflow section already documents the correct order two sections above the contradicting Section 9.

| Service | Source row | Source order | File's Section 9 | File's own workflow |
| :---- | :---- | :---- | :---- | :---- |
| **#23 – Register Lease** | 82 | submit → enter & audit → **pay** → receive certificate | "before submission" (wrong) | Option 1 (Service Center) already correctly shows Audited → Pay → Approved |
| **#24 – Renew Lease** | 82 | same as #23 | "before submission" (wrong) | Option 1 already correct, same pattern as #23 |
| **#26 – Submit Tenancy Dispute** | 72–81 (all 10 consolidated rows) | submit → enter & audit → **pay** → attend hearing/session → decision | "before submission" (wrong) | Option 1 already correct: Audited → Complete Payment → Dispute Assigned |
| **#28 – Request Rental Valuation** | 84 | *"...Upload documents. → **Pay fees after approval**. → Receive rental evaluation certificate."* | "before submission" (wrong) | Single (online) workflow shows payment before submission throughout — no channel split documented at all |
| **#41 – Register Company** | 96 | submit → enter data → audit → **pay** → receive email | *(no "before submission" claim — file just says "Yes")* | Already correct: Audit → Pay Fees → Receive Email |

**#28 is the cleanest single-service finding in this module.** Row 84's own wording — "Pay fees after approval" — needs no inference. The current file states the opposite timing with no counter-channel alternative even sourced. This is the individual-user equivalent of Group C's #12/#18 exception, except here it isn't a minority exception inside an otherwise-upfront category — it's simply what the one sourced row says, misdocumented.

**#41 shows what "done right" looks like** — it's the one file in the module that both gets the order right in its workflow *and* doesn't carry the contradicting boilerplate line, because it was written 2026-08-10 alongside #40, #42, #43 (the four services added to close the 39-vs-41 count gap), a later and evidently more careful pass than the original 2026-08-09 batch.

### Category 3 — Sourced counter channel pays after audit; file's *only* documented channel is an upfront online flow not grounded in that row

Unlike Category 2, these files don't contain a contradicting Option 1 — they simply never document the sourced counter-channel timing at all, having generalised straight to an upfront online model.

| Service | Source row | Source order | What the file documents |
| :---- | :---- | :---- | :---- |
| **#5 – Transfer Property Ownership** | 106 | submit → enter data → **pay** → audited and approved (one combined step) | Option 1 workflow inserts an *audit* step **before** pay, then approval after — reordering the source's own sequence, not just omitting a channel |
| **#9 – Register Gift Transfer** | 88 | submit → enter system and audit → **pay** → receive output | Only a Donor/Recipient/RERAN online-style flow is documented, upfront throughout; the row's one sourced channel (Trustee Centre) is not reflected at all |
| **#10 – Register Lease-to-Own** | 89 ("same as sale registration," inherits row 86's -V pattern) | submit → enter & audit → **pay** → receive | Same as #9 — no counter-channel path documented |
| **#11 – Transfer Lease-to-Own** | 90 (same inheritance) | same | same gap |
| **#12 – Release Lease-to-Own** | 91 (same) | same | same gap |
| **#13 – Amend Lease-to-Own** | 92 (same) | same | same gap |
| **#14 – Register Usufruct Right** | 93 (same) | same | same gap |
| **#15 – Amend Usufruct Right** | 94 (same) | same | same gap |
| **#16 – Terminate Usufruct Right** | 95 (same) | same | same gap |

**Proposed position** (per the standing instruction to propose rather than defer): document each of #5, #9–#16 with the same two-option structure #23/#24/#26/#41 already use — an online path (pay upfront, as currently written) and a Trustee Centre path (pay after the audit/data-entry step, before receiving output), rather than silently generalising to one channel. #5 additionally needs its Option 1 reordered to match row 106's actual sequence (pay before the combined audit-and-approval step, not after an isolated audit step).

### Category 4 — No payment step in source at all

| Service | Source row | Source workflow | File's claim |
| :---- | :---- | :---- | :---- |
| **#17 – Grant Registration** | 98 | submit → enter data (front line) → audited and approved → notify. No pay step anywhere. | "Yes... before the application is submitted" (conflict) |
| **#18 – Grant Completion** | 99 | submit → enter data → audited and approved → link sent. No pay step. | "Yes... before the application is submitted" (conflict) |
| **#33 – Request Property Survey** | 111 | application → review → schedule → site visit → prepare data → issue report. No pay step. | "Yes... before the survey request is processed" (conflict) |
| **#7 – Update Property Ownership Info** (Owner/Entity component only) | 107 | visit → submit → employee enters and updates. No pay step. | Section 9 blanket "Yes," though the file's own Option 1 (Owner/Entity Amendment) workflow doesn't show a Pay step either — internally split, not fully wrong |
| #40 – Upload Building Details | 85 | *(already correctly documented as unspecified/no fee)* | Correct as written |
| #42 – Cancel Power of Attorney | 97 | *(already correctly documented as unspecified)* | Correct as written |

**#17, #18, and #33 are three more services that should very plausibly carry no fee**, on the same standard of evidence Group C used for its Service #2 (B11): the source row simply has no payment step, and — for #17/#18 specifically — they sit either side of #19 (Heirs Ownership), #20, #21 which all *do* have an explicit "pay" step at the same point in an otherwise near-identical workflow shape. That contrast (some rows in this cluster name a fee step, some plainly don't) reads as a deliberate distinction in the source, not an omission, the same reasoning Group C used to conclude cancellation genuinely carries no fee rather than being merely unspecified.

**#7 is a split service** (per `services-overview.md`'s note that #7 consolidates two source rows). Row 112 (Property Information Amendment) does carry a fee; row 107 (Owner/Entity Information Amendment) does not. The file should document these as two fee models under one service, not one blanket "Yes."

**Proposed position:** treat #17, #18, #33, and #7's Owner/Entity-Amendment component as no-fee, pending client confirmation — consistent with #40 and #42, which are already documented this way and needed no correction here.

### Category 5 — Online channel sourced with no fee step, counter channel sourced with one

| Service | Source row | Finding |
| :---- | :---- | :---- |
| **#27 – Cancel Tenancy Contract** | 83 | Counter channel: submit → audit → **pay** → receive. Online/App channel: *"fill details, attach docs, send; receive, review; email sent on approval"* — **no fee step at all.** The file states a fee is required uniformly, with no channel distinction. |

**Proposed position:** flag rather than silently resolve — it's plausible the online path is genuinely free (a policy choice to encourage self-service cancellation) or that the source simply omitted a fee step present in the counter path. Either is defensible; the file currently asserts neither and instead states a single, unqualified fee.

### Category 6 — Legitimate conditional fee (not an error)

**Service #25 – Manage Lease** is documented correctly: *"Payment is required for lease management requests that attract a regulatory service fee"* — a genuine third payment shape (some actions under this umbrella service are free, some aren't), extrapolated rather than sourced to one row, and internally consistent. Worth naming as its own category rather than folding into Category 1, since it isn't "upfront" or "after decision" so much as "sometimes at all."

### Category 7 — A service charging to view the status of something it already charged to submit

**Service #39 – Track Complaint** states a fee is required to retrieve complaint status: *"Payment Required: Yes... Payment must be completed before complaint tracking is available."* This is not a source-vs-file conflict (#39 is extrapolated, with no master-table row) — it is an internal-consistency problem against the module's own shared platform feature. **Feature #2 – Track Application Status**, which #39 is functionally a specialised version of, is explicit: *"No additional fee. Application tracking is included as part of the submitted service. Payment Required: No... Payment is not required to track an application that has already been submitted."*

A user who files a complaint under #38 (itself fee-bearing, see Category 8 below) would, under #39 as currently written, pay a second time just to check on it — while every other application in the platform tracks for free once submitted. This is the module's clearest internal-consistency finding, independent of any master-table dispute.

**Proposed position:** #39 should be free, matching Feature #2's pattern and every other trackable service in this module. No source row exists to override this — the current fee requirement appears to be an artefact of extrapolating #39 too closely from #1–#3's "Yes, pay per lookup" pattern (verification searches), which is a different kind of request (a fresh registry query) from checking on a case that already exists and was already paid for.

### Category 8 — Should a consumer-protection complaint carry a fee at all?

**Services #38 (Submit Complaint) and #39 (Track Complaint)** are both extrapolated, with no master-table row to check against, and both currently charge a fee. Group F is explicitly named "Tenants & Consumers" in the source's own group structure, and Consumer Protection Services exist specifically so an aggrieved party has recourse against a developer, landlord, or practitioner. Charging a fee to *file* that complaint — on top of #39's fee to check on it — sits awkwardly next to that stated purpose, and is different in kind from #26 (Submit Tenancy Dispute), which *does* carry a clearly sourced fee (rows 72–81 all show a "pay" step) because it's a formal adjudication/litigation process, not a regulatory grievance mechanism.

**Proposed position:** #39 should be free regardless (Category 7). #38's fee is a closer call — RERAN plausibly wants to deter frivolous complaints the same way court filing fees deter frivolous suits — but it's worth flagging as a genuine open question rather than assuming either answer, since nothing in the source settles it either way for an extrapolated service. See `open-questions.md`.

## Settlement Mechanism

The source names the same three settlement routes seen platform-wide: payment gateway (card, bank transfer, USSD per the PRD), escrow deduction, and institution account debit. **Individual User uses payment gateway only** — there is no escrow relationship or institution account for a natural person acting in their own capacity. Service #6's Purchaser workflow additionally names a **Wallet Account** ("pay via Wallet Account") — this is the same P-22 wallet primitive flagged as an open question in Group C's `payments.md` B2, which found P-22 is balance-based and doesn't fit Group C's model. It fits here, in principle, since an individual purchaser is exactly the kind of user a top-up wallet is designed for — but nothing else in this module's 43 files references a wallet, so whether #6's purchaser flow is the wallet's only use in this module, or whether it should be the default payment method module-wide, is unresolved. See `open-questions.md`.

## Fee Calculation

Consistent with Group C's confirmed principle (`financial-trust-institutions/open-questions.md` B5/B6): RERAN sets the fee for each service directly via the fee-schedule engine (FR-16), as configuration rather than a value derived from property price, transaction value, or any other user-side figure. No individual-user service-flow file describes an ad valorem fee, so this module never carried the misreading Group C's B6 had to correct — worth noting as confirmation, not correction.

## Payment Artefacts

Every fee-bearing service in this module issues a **Payment Receipt**, generated at checkout. Where the transaction produces a title-adjacent document, source additionally names a **"Fee Balance"** line (e.g. rows 86–95's "Fee balance (all e-deliverables)") — the same artefact name Group C's `payments.md` (B9) found attached to its now-retired standing-account model. Individual User has no standing account of any kind (there is no institution-level account structure for natural persons), so this module's "Fee Balance" cannot mean the same thing it meant in Group C's superseded model. It most plausibly means a running total or balance-due line on a single transaction receipt, not a multi-transaction account balance — but this is an inference, not confirmed by source. See `open-questions.md`.

## To Confirm — Summary

1. **#17, #18, #33, and #7's Owner/Entity Amendment component** — confirm these carry no fee (source has no pay step for any of them), matching #40/#42's existing treatment.
2. **#28** — confirm payment moves to after-approval, matching row 84's explicit wording.
3. **#23, #24, #26, #41** — no client input needed; these just need Section 9 corrected to match each file's own (already-correct) workflow.
4. **#5, #9–#16** — confirm whether a Trustee Centre channel with post-audit payment should be documented alongside the existing online/upfront channel, or whether the online-only model is an intentional platform redesign that supersedes the physical-counter sourcing.
5. **#27** — confirm whether the online cancellation path is genuinely fee-free, or whether a fee step was simply omitted from that part of the source.
6. **#39** — confirm Track Complaint should be free, matching Feature #2.
7. **#38** — open question on whether a consumer complaint should carry a fee at all; no proposed resolution given, genuinely undecided.
8. **#6's Wallet Account reference** — confirm whether this is the module's standard payment method or an isolated mention, and its relationship to Group C's P-22 primitive.
9. **"Fee Balance" meaning in this module** — confirm it denotes a single-transaction balance line, not a Group-C-style standing account (which does not exist here).

## Downstream Corrections Needed

This document is new; nothing else in the repository claims to match it yet. But its findings mean the following existing files will need correction once these questions are resolved, so they don't become another isolated fix the way Group C's B1 initially was:

- All 43 service-flow files' **Section 9**, for the subset identified above.
- **Service #5's Processing Workflow**, Option 1 specifically (reorder, not just reword).
- **Services #9–#16's Processing Workflow**, to add the missing Trustee Centre channel if the proposed position in Category 3 is confirmed.
- **Service #7**, to split Section 8/9 into its two components.
- **`module-roadmap.md`'s** cross-cutting payment-timing observation, which currently lists this module as "unaudited" — that line needs updating now that the audit exists, with individual-user's own count of exceptions added alongside Group B's six and Group C's two.
