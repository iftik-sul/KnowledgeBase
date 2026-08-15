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

**Updated 2026-08-15 — findings propagated.** This document's first version recorded the audit's findings without correcting the service-flow files themselves. That correction has since been made: 20 of the 43 files carried a boilerplate Section 9 ("Payment must be completed before the application is submitted") that did not match either the source or, in several cases, the file's *own* Processing Workflow section — all 20 have been corrected, along with three further client-confirmed payment questions (see "To Confirm — Summary" below). "Downstream Corrections — Propagated," at the end of this document, lists exactly what changed in each file.

## The Core Finding: Two Channels, Two Timings, One Boilerplate Line

A large share of Group E and F source rows describe **two channels** for the same service: an in-person Trustee Centre / Land Department counter path, and (where documented) an online/App path. Where both exist in source, they frequently have **different payment timing**:

- **Online/App channel:** payment is bundled into the submission step — pay, then submit. This is genuinely upfront.
- **Trustee Centre / counter channel:** the customer's documents are received and entered into the system, the transaction is **audited first**, and **only then** does the customer pay — usually immediately before receiving the certificate/output.

Every one of the 43 service-flow files carries a Section 9 that reads, verbatim or near-verbatim, "Payment must be completed before the application is submitted." For the online channel this is accurate. For the counter channel, wherever source documents one, **it is backwards** — and several files' own *Processing Workflow* sections (Option 1 / Service Center) already show the correct counter-channel order, while Section 9 a few hundred words later contradicts it. This is not a subtle reading; it is the same two sections of the same file disagreeing with each other on eight documents, listed in "Confirmed contradictions" below.

**Why this matters for the previous modules' precedent:** Group C's `payments.md` cites this module's Service #8 as evidence that "individual-user pays upfront" — true for #8, but that citation was made without checking the module's other 42 services, exactly the kind of single-service generalisation `module-roadmap.md` now warns against. This document is the missed audit.

## Payment Timing Categories

### Category 1 — Upfront, before submission (confirmed, both channels agree or only one channel is sourced)

Services #1–#4, #6, #8, #19–#22, #29, #35, #38, #43, and the extrapolated verification/complaint services (#1–#3) either have no counter-channel alternative sourced, or the sourced counter-channel order genuinely places payment before the final audit/approval decision. Section 9's "before submission" language is correct for these as written, though see the Category 4 note on #38 below.

**#30 and #37 removed from this category 2026-08-15** — see Category 9 below. Both were originally listed here as if they were ordinary upfront-paying services, but they're routing services (act-on-behalf-of-owner and remote-transaction respectively) with no independent payment rule of their own; their actual timing depends entirely on whichever underlying service is selected, which could be any of the categories in this document, not just Category 1.

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

### Category 5 — Online channel sourced with no fee step, counter channel sourced with one. Resolved.

| Service | Source row | Finding |
| :---- | :---- | :---- |
| **#27 – Cancel Tenancy Contract** | 83 | Counter channel: submit → audit → **pay** → receive. Online/App channel: *"fill details, attach docs, send; receive, review; email sent on approval"* — no fee step in the source text. |

**Confirmed by client (`open-questions.md` A5): the fee applies to both channels, on the same timing as the counter channel** — payment after RERAN's review, not before submission. The source's online-channel silence on payment was an omission in the source material, not a deliberate free path. #27's service-flow file previously documented a single undifferentiated flow with no Trustee Centre channel at all (the same gap found in #9–#16) — it has been corrected to show both channels explicitly, both fee-bearing, both paying after review. See the corrected file for the resulting two-option Processing Workflow.

### Category 6 — Legitimate conditional fee (not an error)

**Service #25 – Manage Lease** is documented correctly: *"Payment is required for lease management requests that attract a regulatory service fee"* — a genuine third payment shape (some actions under this umbrella service are free, some aren't), extrapolated rather than sourced to one row, and internally consistent. Worth naming as its own category rather than folding into Category 1, since it isn't "upfront" or "after decision" so much as "sometimes at all."

### Category 7 — A service charging to view the status of something it already charged to submit

**Service #39 – Track Complaint** states a fee is required to retrieve complaint status: *"Payment Required: Yes... Payment must be completed before complaint tracking is available."* This is not a source-vs-file conflict (#39 is extrapolated, with no master-table row) — it is an internal-consistency problem against the module's own shared platform feature. **Feature #2 – Track Application Status**, which #39 is functionally a specialised version of, is explicit: *"No additional fee. Application tracking is included as part of the submitted service. Payment Required: No... Payment is not required to track an application that has already been submitted."*

A user who files a complaint under #38 (itself fee-bearing, see Category 8 below) would, under #39 as currently written, pay a second time just to check on it — while every other application in the platform tracks for free once submitted. This is the module's clearest internal-consistency finding, independent of any master-table dispute.

**Proposed position:** #39 should be free, matching Feature #2's pattern and every other trackable service in this module. No source row exists to override this — the current fee requirement appears to be an artefact of extrapolating #39 too closely from #1–#3's "Yes, pay per lookup" pattern (verification searches), which is a different kind of request (a fresh registry query) from checking on a case that already exists and was already paid for.

### Category 8 — Should a consumer-protection complaint carry a fee at all? Resolved.

**Services #38 (Submit Complaint) and #39 (Track Complaint)** are both extrapolated, with no master-table row to check against. **Confirmed by client (`open-questions.md` A7): #38's fee stands as originally documented** — RERAN wants the deterrent effect against frivolous complaints, the same logic behind court filing fees. This closes the question as "confirmed as originally written," not a correction — #38's service-flow file needs no changes. #39 remains a separate, already-resolved finding (Category 7 below): tracking a complaint that has already been paid for and submitted should be free, matching Feature #2, and that fix is unaffected by A7's confirmation that *filing* the complaint carries a fee.

### Category 9 — Routing services with no independent payment rule of their own. Found and corrected in a later audit pass.

| Service | What it does | Original documentation | Corrected |
| :---- | :---- | :---- | :---- |
| **#30 – Act on Behalf of Property Owner** | Validates a PoA, then routes into whichever of #4–#35 the representative selects | Section 9 hedged ("where applicable") but Sections 12/13 showed one fixed unconditional "pay before submission" sequence regardless of what was selected | Explicitly inherits the selected service's own fee status, payment timing, fields, documents, status flow, and output — no independent rule |
| **#37 – Remote Property Transactions** | Confirms identity (#36), then routes into whichever transaction the user selects | Section 9 stated flatly "payment must be completed before the application is submitted" (no hedge) — directly contradicting the file's own Business Rule 4, which already said transactions follow the selected service's own rules | Same fix as #30 |

**Neither of these is a source-vs-file contradiction like Categories 2–5** — both are extrapolated services with no master-table row to check against. This is a design-consistency problem: both files predate the UI package's routing-wrapper architecture (`ui/screens-unified/submit-application.md`, which documents #30 and #37 as reopening the wizard at the selected service's own pattern) and were never reconciled with it. #30's own text had already partially caught this (the "where applicable" hedges), but its diagrams hadn't; #37's text hadn't caught it at all, producing a direct rule-vs-rule contradiction within the same file. Neither belongs in Category 1 (upfront) or any other single category — their actual timing is whatever the selected underlying service's own category says, which could be any of Categories 1–8 depending on what's chosen.

## Settlement Mechanism

The source names the same three settlement routes seen platform-wide: payment gateway (card, bank transfer, USSD per the PRD), escrow deduction, and institution account debit. **Individual User uses payment gateway only** — there is no escrow relationship or institution account for a natural person acting in their own capacity.

**Resolved (`open-questions.md` C1): there is no separate Wallet Account mechanism in this module.** The master table's row 86 names "pay via Wallet Account" for Service #6's purchaser sub-flow, and this document previously flagged that language as an open question about whether a wallet primitive applies module-wide. The client has confirmed there is no distinct wallet mechanism — Service #6 uses the same shared platform payment gateway as every other service in this module, and as Groups B and C. #6's service-flow file has been corrected to describe standard gateway payment rather than a Wallet Account.

**Note for whoever eventually resolves Group C's still-open B2** (whether the wallet primitive P-22 is shared build across modules): Individual User's Service #6 no longer needs P-22 at all, now that its "Wallet Account" language is confirmed to have been a source-table artefact rather than a real distinct payment path. This is recorded here as context only — Group C's own `open-questions.md` and `payments.md` are untouched by this correction.

## Fee Calculation

Consistent with Group C's confirmed principle (`financial-trust-institutions/open-questions.md` B5/B6): RERAN sets the fee for each service directly via the fee-schedule engine (FR-16), as configuration rather than a value derived from property price, transaction value, or any other user-side figure. No individual-user service-flow file describes an ad valorem fee, so this module never carried the misreading Group C's B6 had to correct — worth noting as confirmation, not correction.

## Payment Artefacts

**Every fee-bearing service in this module issues exactly one payment artefact: a Payment Receipt, generated at checkout.** There is no Fee Balance concept anywhere in this module — confirmed by client, `open-questions.md` C2 (2026-08-15). Source rows 86–95 name a "Fee balance (all e-deliverables)" output line, and this document previously treated that as a real artefact needing a definition of its own (an inference toward "a single-transaction balance line," having already ruled out Group C's now-retired standing-account reading). The client has since confirmed there is no such thing at all: every payment settles instantly through the standard payment gateway when the payment step is reached, with no wallet, no running balance, and no partial-payment state to report. The source's "Fee balance" phrasing was never describing a feature to build — it doesn't correspond to anything in this module's payment model.

**Downstream correction:** #6 and #10 were the two service-flow files that had actually carried "Fee Balance Information" into their own Output sections (Section 15) — both corrected 2026-08-15, removed and, where the file was missing it entirely (#10), replaced with the standard Payment Receipt line every other fee-bearing service already has. #11–#16 (siblings of #10, same source-row inheritance) were checked and already correctly listed Payment Receipt with no Fee Balance reference, so needed no change.

## To Confirm — Summary

**All items below are now resolved.**

1. ~~**#17, #18, #33, and #7's Owner/Entity Amendment component**~~ — resolved as no-fee (proposed answer confirmed by adoption; no client pushback received). Corrected in each file.
2. ~~**#28**~~ — resolved: payment moves to after-approval, matching row 84's explicit wording. Corrected.
3. ~~**#23, #24, #26, #41**~~ — resolved: Section 9 corrected to match each file's own (already-correct) workflow. #41 needed no change.
4. ~~**#5, #9–#16**~~ — resolved: a Trustee Centre channel with post-audit payment has been added alongside the existing online channel in each file; #5's Option 1 reordered to match row 106.
5. ~~**#27**~~ — resolved by client (A5): the fee applies to both channels, on the counter channel's timing (after review). #27 corrected to document both channels explicitly, mirroring the #9–#16 fix.
6. ~~**#39**~~ — resolved: Track Complaint is now free, matching Feature #2. Corrected.
7. ~~**#38**~~ — resolved by client (A7): the fee stands as originally documented. No file change needed.
8. ~~**#6's Wallet Account reference**~~ — resolved by client (C1): no wallet mechanism exists; #6 uses the standard shared gateway. Corrected.
9. ~~**"Fee Balance" meaning in this module**~~ — resolved by client (C2): there is no Fee Balance concept at all; every payment settles instantly, no wallet, no balance. #6 and #10 corrected to remove the artefact from their Output sections.
10. ~~**#30, #37**~~ — resolved: both corrected to explicitly inherit the selected underlying service's payment rule rather than asserting an independent, always-upfront one. Corrected.

## Downstream Corrections — Propagated

All corrections identified above have now been applied to the affected service-flow files, in the same PR that carries this update:

- **Section 9** corrected in #5, #7 (split), #9–#18, #23, #24, #26, #27, #28, #33, #39. #6, #38, #40, #41, #42 needed no Section 9 change (already correct or already confirmed as-is).
- **Service #5's Processing Workflow**, Option 1 reordered to match row 106 (pay before the combined audit-and-approval step, not after an isolated audit step).
- **Services #9–#16's and #27's Processing Workflow**, Trustee Centre channel added alongside the existing online channel.
- **Service #7** split into two fee models under Section 8/9 (Owner/Entity Amendment: no fee; Property Information Amendment: fee, unchanged).
- **Services #17, #18, #33** corrected to no-fee throughout (Section 8/9, Processing Workflow, Application Status Flow, Output, Acceptance Criteria, Business Rules).
- **Service #28** reordered so payment follows RERAN's approval, not submission.
- **Service #39** corrected to no-fee, matching Feature #2.
- **Services #23, #24, #25**: "Property Management Company" removed from Who Can Apply (cross-module leak from Group D — see `open-questions.md` B3). #23/#24 additionally gained Tenant as a documented secondary applicant path (see `open-questions.md` B1).
- **`module-roadmap.md`'s** cross-cutting payment-timing observation, updated to remove the "unaudited" label for this module and record the audit's findings.
- **Application Status Flow (Section 13) in #9–#16, #23, #24, #26** — found in a later audit pass to still show only the online channel's upfront "Payment Pending / Payment Successful" sequence, with no status reflecting the Trustee Centre / Service Center channel's audit-then-pay timing that Section 9/12 already documented for these same eleven files. Added an "Audited — Awaiting Payment" additional status to each, following the file's own existing convention for channel-specific statuses. #27 was checked and needed no change — it was rebuilt from scratch during the correction pass rather than edited in place, so its Section 13 already reflected the post-review payment timing correctly.
- **Services #30, #37** — found in a fourth audit pass to describe an independent, always-upfront payment rule that contradicted (in #37's case, directly) their own acknowledgment that they're routing services. Corrected to explicitly inherit the selected underlying service's fee status and payment timing throughout — Sections 8, 9, 12, 13, 14, 15, and the relevant Business Rules in each file. See Category 9 above.
- **Services #6, #10** — "Fee Balance Information" removed from Output sections, per client confirmation there is no such artefact anywhere in this module (C2, above).

Nothing remains outstanding from this document. All ten items on the To Confirm list are resolved.
