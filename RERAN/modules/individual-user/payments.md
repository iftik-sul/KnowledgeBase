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

Every RERAN service is chargeable **except a small set of genuinely sourced no-fee services** — see "No-Fee Services" below. This document corrects a documentation-wide defect found by checking all 43 service-flow files individually against their own source row, per the standing instruction not to generalize a payment pattern across a module.

## The Core Finding: A Boilerplate Defect, Not a Payment-Model Decision

Services #1–#39 (all authored 2026-08-09) carry an identical Section 9 line — **"Payment must be completed before the application is submitted"** — regardless of what their own source row actually says. Checking each row individually against the master service table (`RERAN_service_flows_v2.md`, rows 72–112) found this boilerplate is wrong for at least fifteen of those thirty-nine files. By contrast, Services #40–43 (authored 2026-08-10, the most recently added batch) each correctly state "not specified in the source material" or reproduce the sourced order exactly, with no boilerplate at all.

This is not a payment-model correction in the sense Group C needed (where the client changed *how the platform should work* from what the source said). This is a **documentation accuracy defect**: thirty-nine files asserting a uniform rule that their own cited source contradicts, in a majority of the cases actually checked.

**Confidence:** Sourced, wherever a row exists (see the per-service table below). Fifteen of the sourced rows checked (of the ~30 with clear enough workflow detail to check payment position against) show a Section-9-vs-source conflict. This is treated as systemic rather than a handful of edge cases, and a full correction pass against every one of the 43 files' Section 9 and Processing Workflow sections is recommended as immediate follow-up work — see `open-questions.md` for the itemized list.

## Payment Timing Models

Five distinct timing patterns exist across the 43 services, once checked individually. Unlike Group C, these are not alternate *payer* models — every fee is paid by the individual user themselves, via the shared platform gateway or at a Trustee Centre counter — the variation is entirely in **when**, relative to RERAN's review.

| Model | Timing | Services |
| :---- | :---- | :---- |
| **A — Upfront** | Before submission / before RERAN's substantive review begins | #1–#4, #19–#22, #29, #34–#37 (sourced or extrapolated; no conflict found) |
| **B — Pay after initial audit, before hearing/decision** | RERAN's clerical/eligibility check happens first; payment is the gate into the substantive process (hearing, conciliation, certification) | #23, #24, #26 (sourced — rows 82, 72–81) |
| **C — Pay after RERAN's decision** | The customer pays only once approved, at the point of issuing/collecting the output | **#28 (sourced, row 84 — explicit: "Pay fees after approval")** |
| **D — No fee** | Source row has no payment step at all | #17, #18, #33, #40, #42, and the "Owner/Entity Information Amendment" half of #7 (row 107) |
| **E — Conditional** | Fee applies only to the specific chargeable action selected within the service | #25, #30 (extrapolated; already correctly documented this way) |

Model A is what the retired blanket Section 9 line correctly describes — for those services where it happens to be right. It is not the platform default; it is one of five patterns, and the boilerplate's mistake was applying it to all 43 files regardless of which pattern each one's own source actually shows.

### Model C in detail — the clearest single-service finding

Row 84 (Service #28, Request Rental Valuation) is unambiguous, unlike Group C's #12/#18 exception, which had to be inferred from step ordering: the source states outright — *"Select property to evaluate rental → Add details → Upload documents → **Pay fees after approval** → Receive rental evaluation certificate."* There is no channel split, no alternate reading. The current file's Section 9 and workflow both show payment before submission, directly contradicting this. This is the highest-confidence correction in this document.

### Model B in detail — the ten dispute rows and lease registration/renewal

Rows 72–81 (all ten tenancy-dispute procedures, consolidated into Service #26) and row 82 (Service #23/#24, lease registration and renewal) share the same shape at the Trustee Centre/service-centre channel: **submit documents → RERA enters the application and performs an initial audit → pay → then proceed to the substantive stage** (hearing, conciliation, or certificate issuance). Interestingly, Services #23, #24, and #26's own "Option 1 – Service Center" processing workflows already show this correctly (`... → Application Audited → Pay Service Fee → ... → Receive Certificate`). Only their Section 9 lines are wrong, contradicting their own Option 1 workflow a few hundred words later in the same file. This internal inconsistency — not just a source mismatch — is itself worth noting to whoever corrects these files: the fix is to bring Section 9 into line with each file's own Option 1, not to invent new workflow detail.

### No-Fee Services — a real category, not a gap

Five sourced no-fee cases were found, all with no payment step anywhere in their source row:

* **#17 – Grant Registration** (row 98): "Move to Customer Center, submit docs, employee enters data, transaction audited and approved, customer notified" — no Pay step.
* **#18 – Grant Completion** (row 99): same shape, no Pay step.
* **#33 – Request Property Survey** (row 111): "Owner application → Review by Survey Department → Set appointment → Visit site → Prepare survey data → Issue final report" — no Pay step anywhere, including no fee-collection step before the multi-day survey process begins.
* **#40 – Upload Building Details for Leasing** (row 85) and **#42 – Cancel Power of Attorney** (row 97) already correctly document this in their current files — both are good models for how the other three should read once corrected.
* **The "Owner/Entity Information Amendment" component of #7** (row 107, distinct from the "Property Information Amendment" component sourced to row 112, which *is* fee-bearing): "Visit Real Estate Services Trustee Centers, submit docs, employee enters and updates data into system" — no Pay step. Service #7's file already gets this right in its own Option 1 workflow (no Pay step shown) but its blanket Section 9 claims a fee applies regardless.

This mirrors Group C's Service #2 finding almost exactly — a real no-fee service sitting inside a module where "every service is chargeable" was treated as a universal rule rather than a general pattern with genuine exceptions.

**Proposed resolution, pending client confirmation:** treat these five as confirmed no-fee, on the same basis Group C's Service #2 was confirmed — the source's silence on a fee, in a document that is otherwise consistently explicit about fees where they exist (nearly every other row names "pay" as a distinct step), reads as an intentional omission rather than incomplete transcription. Medium-high confidence, not "sourced," because unlike Group C's B11 this has not had a direct client decision — see `open-questions.md`.

### The Trustee Centre / Online channel split — a second, related gap

Independent of the Section 9 defect, ten services (#6, #9–#16, and partially #27) source a genuine **two-channel payment split** that their current files only document one side of:

* **#6 (Register Property Sale, row 86)** — the Trustee Centre channel (`-V`) pays *after* audit; the App channel (seller/purchaser workflow) pays essentially at submission, with the purchaser's payment step explicitly naming a **Wallet Account** (`pay via Wallet Account`). The file documents only the App channel.
* **#9 (Register Gift Transfer, row 88)** — sourced with only a Trustee Centre channel (`-V: submit docs, enter system and audit, pay, receive outputs`), i.e. pay *after* audit. The file's only documented workflow is an online-style flow with payment before submission — the online channel is not itself sourced for this service, so its inclusion may be a reasonable platform extension, but presenting it as *the* payment timing, with no mention of the sourced counter-channel timing, drops the one channel the source actually specifies.
* **#10–#16 (the Lease-to-Own and Usufruct families, rows 89–95, "same as sale registration")** — inherit row 86's two-channel split by explicit source cross-reference. None of the seven files document a Trustee Centre option at all; all seven describe only an online-first, pay-upfront flow.
* **#27 (Cancel Tenancy Contract, row 83)** — the Trustee Centre channel pays after audit; the source's own Online/App channel workflow (`fill details, attach docs, send; receive, review; email sent on approval`) has **no payment step mentioned at all**, suggesting cancellation might be free through that channel specifically. The file states a fee applies uniformly, with a single undifferentiated workflow.

**Proposed resolution:** this is lower-confidence than the no-fee findings above and is flagged rather than resolved, because closing it properly means adding a documented Trustee Centre option to seven files that currently have none — closer to a workflow-design decision than a one-line correction. See `open-questions.md` for the itemized list and proposed next step.

## Fee Calculation

No published fee schedule exists in source for the Individual User module, matching Group C's finding under its own B5/B6: RERA sets each service's fee directly, populated through the platform's fee-schedule engine (FR-16), independent of any figure belonging to the transaction itself (sale price, rent value, property value). Nothing in the 41 sourced rows for Groups E+F suggests an ad valorem calculation tied to sale price or rent — even the highest-value services (Register Property Sale, Register Lease-to-Own) list only a flat processing SLA, never a percentage.

**Confidence:** Medium-high, by analogy with Group C's confirmed B6 answer, not independently confirmed for this module. Flagged in "To Confirm" below.

## Settlement Mechanisms

Two payment routes appear across the 41 sourced rows:

* **Payment gateway** — used wherever the workflow says "select payment, pay" without further detail; the default for online/App submissions.
* **Wallet Account** — named explicitly and only once, in row 86's purchaser workflow (Service #6): "pay via Wallet Account." This is very likely the same primitive `proposed-services.md` P-22 describes — "Wallet account — top-up, balance, statement, refund-to-wallet" — which that document already flags as referenced at row 86 with no service anywhere defining it. **Individual User is therefore the module that actually sources P-22**, not just an analogous user of it; Group C's `open-questions.md` B2 correctly guessed the wallet was "designed for individuals" when ruling out reusing it for institutions, and this confirms that guess directly. Building P-22 is now something this module has a concrete, sourced reason to prioritize, not just a platform-wide nice-to-have.
* **Trustee Centre counter payment** — cash, card, or bank deposit at a physical Trustee Centre, referenced generically ("pay") without further specification of instrument. Row 75 (Grievance Case, part of Service #26) additionally specifies "pay by bank deposit then visit center with receipt" as a distinct sub-pattern within the counter channel — the only row in Groups E+F naming bank deposit specifically rather than a generic "pay."

**Confidence:** Sourced on the Wallet Account's existence and single point of reference; Medium on treating it as the platform-wide P-22 primitive rather than a service-specific mechanism, since no source document confirms the two are literally the same build artefact.

## Failed and Reversed Payments

Not addressed anywhere in the 41 sourced rows or in any of the 43 service-flow files. No source row describes what happens to a fee already paid if:

* a Model B service's application is later rejected after the post-audit payment (#23/#24/#26 — payment happens before the hearing/decision, so a rejection after payment is a real, undocumented scenario, structurally similar to Group C's "a rejected application has already paid" open item for its own Model-A-equivalent services);
* a Model C service (#28) never reaches approval — since payment happens *after* approval here, this scenario cannot occur for #28 specifically, but is worth stating explicitly so it isn't confused with the Model B risk above;
* a Trustee Centre counter payment fails or is disputed after being taken in cash or by bank deposit, which has no obvious digital retry path the way an online gateway failure does.

**Confidence:** Genuinely unaddressed — flagged in "To Confirm" below rather than proposed, since Group C's own equivalent questions (B3, B4, B9, B10) needed a direct client decision rather than a documentation-inferred answer, and there's no comparable client input for this module yet.

## Additional Statuses

The platform core status vocabulary proposed in Group C's `open-questions.md` D1 includes `Approved — Awaiting Payment` as a core status. On the evidence gathered here:

* **`Approved — Awaiting Payment` applies to exactly one Individual User service: #28**, on the same logic as Group C's #12/#18 — RERAN's decision is sourced as preceding the customer's payment. No other Individual User service sources this ordering with the same clarity; the Model B services (#23/#24/#26) pay *before* the decision, not after, so the status does not apply to them despite superficially resembling Group C's pattern (payment happening partway through the process rather than strictly upfront).
* Whether it should also apply to any of the Trustee Centre-channel services flagged under "channel split" above (#6, #9–#16, #27) depends on resolving that gap first — see `open-questions.md`.

## To Confirm — Summary

1. **Whether the five identified no-fee services (#17, #18, #33, and #7's Owner/Entity Information Amendment component) should be built as genuinely free**, matching Group C's Service #2 precedent, or whether the source's silence reflects incomplete source material rather than an intentional no-fee design. Proposed: treat as free (Medium-high confidence) — see `open-questions.md`.
2. **Whether the Trustee Centre / Online channel-payment-timing split found for #6, #9–#16, and #27 should be documented as two distinct sub-flows per service**, matching what the source actually specifies, or whether the Trustee Centre channel should be treated as out of scope for the digital platform (per the same reasoning Group C's C2 used to argue the Trustee Centre is "an assisted mode," not a separate system). Not proposed here — this affects workflow design, not just documentation accuracy, and is flagged for client input.
3. **Whether Service #38 (Submit Complaint) and #39 (Track Complaint) should genuinely carry a fee at all.** Both are extrapolated, with no source row to check against, and #39 in particular duplicates the function of the shared **Feature #2 – Track Application Status**, which is explicitly sourced as free ("No additional fee. Application tracking is included as part of the submitted service.") Charging to track a complaint you already paid to file, when tracking every other application type is free, is an internal inconsistency worth raising with the client rather than assuming. See `open-questions.md`.
4. **The fee basis** (flat per-service vs. any value-linked component) — proposed flat, by analogy with Group C's confirmed B6, not independently confirmed for this module.
5. **Failed/reversed payment handling** — entirely unaddressed in source; no proposal offered, flagged for client input.
6. **Whether the Wallet Account referenced at row 86 is the same build artefact as `proposed-services.md` P-22** — Medium confidence it is; not independently confirmed.
