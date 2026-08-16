---
project: RERAN
type: overview
status: current
updated: 2026-08-16
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
tags:
  - roadmap
  - modules
  - planning
---

# RERAN Module Roadmap

A survey of all eight user groups against the source material: what exists, what is documented, what is missing, and in what order to build it.

**Scope:** post-login functionality only. Registration and onboarding are excluded from this project.

Services that the source material does not contain but the PRD or Nigerian law appears to require are catalogued separately in [proposed-services.md](proposed-services.md). This roadmap covers only the sourced 145.

---

## The Landscape

| Group | Module | Services | Roles | Sub-systems | Documentation status |
| :---- | :---- | :---: | :---: | :---: | :---- |
| **A** | Regulatory Authority & Governance | **0** | 8 | 6 | Not started — see gap below |
| **B** | Real Estate Developers | 27 | 4 | 3 | UI complete (19 screens); 27/27 service flows merged (issue #33, PR #36, merged 2026-08-11); both reconciled against the unified-access and per-transaction payment decisions (issue #58); **shared-features layer rebuilt 2026-08-16 to 13 features, including a new Profit Withdrawal Request feature with no screen built yet — see the Group B profile below** |
| **C** | Financial & Trust Institutions | 18 | 4 | 3 | 18 service-flow files at full depth; 19 UI screens documented (14 in `ui/screens/`, 5 in `ui/screens-unified/` — Help & Support added 2026-08-16); the only fully round-tripped module so far — source → flows → UI, merged; **payment model fully normalized 2026-08-16 — see the Group C profile below** |
| **D** | Real Estate Service Companies | 26 | 4 | 4 | **Rebuilt from scratch 2026-08-16, all six phases of the module build playbook complete**: roles, services overview, payments, open-questions, 26 service-flow files, 12 UI screens, navigation, role-workflows, 8 shared platform features, and shared UI docs (components/status-badges/validation-rules). Two client decisions (A2 — Service #18 stays in Group D; B4 — Services #12–15 normalized to pay-before-lodging) resolved and propagated across ~30 files. Phase 6 audit complete — see the Group D profile below |
| **E+F** | Individual User | 41 | 6 | 4 | 43 service flows written; count reconciled; `payments.md`, `open-questions.md`, `navigation.md`, and `role-workflows.md` added 2026-08-15 (analysis layer), findings propagated into the service-flow files; UI package added 2026-08-15 (20 files), merged (PR #61); nine post-merge audit passes since, `open-questions.md` now fully resolved (15/15, 0 awaiting client data) |
| **G** | Allied Professionals & Service Trustees | **0** | 4 | 3 | Roles documented; interfaces not written — see note below |
| **H** | Public & Informational Users | 33 | 2 | 2 | Roles, services overview; no service flows |
| | **Total** | **145** | **28** | | |

Service counts are verified row by row against the master service table and reconcile exactly with the source workbook's own summary. The individual-user module's count now reconciles too — see Known Issues for how.

**Pattern worth naming, corrected 2026-08-15 (four times), extended 2026-08-16.** This section originally said "no module has both stages complete and merged yet," then was corrected to name **Group C** as the first module with service flows and UI both complete and merged, then corrected again to add **Group B** as equally complete and merged first (PR #36, 2026-08-11). **Individual User closed the same gap a third way, same day, and its UI package has since merged too (PR #61)** — there are now three modules with both stages complete: Group B, Group C, and Individual User. **Group D closed the gap a fourth way on 2026-08-16 — built from scratch in a single session, following all six phases of `module-build-playbook.md` in strict dependency order** (source reconciliation → foundational docs → payments/open-questions → service flows → UI screens → shared features, each phase depending only on what came before it — never UI before flows the way Group B did, never features guessed ahead of screens the way Group C's first pass did). Group C remains the cleanest example among the pre-existing modules, since its derivation ran source → flows → UI in strict order after initially being built out of order; **Group D is the first module to run every phase in the correct order from the very first commit**, rather than reaching that order through later correction.

---

## The Group A Gap

**Group A owns zero services, yet appears as approver on nearly every one of the other 145.**

The user group structure gives Group A eight roles and six platform sub-systems:

* Admin & Configuration Console
* Licensing & Registry Engine
* Escrow / Trust-Account Audit System
* Inspection & Enforcement Module
* Tribunal & Remote-Litigation System
* Revenue & Settlement Dashboard

The PRD independently specifies three feature modules covering the same ground: staff workflow and case management, reporting and analytics, and administration/security/audit.

So the regulator's own system is described at capability level in two source documents, but has no entries at all in the service table — because the service table catalogues services *offered to external users*, not the internal work of processing them.

**Why this matters:** every one of the 145 external services terminates in a Group A action. The Compliance & Escrow Auditor alone is the approver for all 18 Group C services and most of Group B's — and, as of 2026-08-16, most of Group D's as well. Without Group A documented, no external service flow can describe what happens after submission, and the back-office is the largest unspecified area of the platform.

> **Proposed** — Group A should be documented as a module organised by sub-system rather than by service, since it has no service catalogue. The six sub-systems above become the module's top-level structure, with each documenting the queues, decisions, and actions available to the roles that operate it. Needs client confirmation.

### Estimated shape

| Sub-system | Primary roles | Feeds from |
| :---- | :---- | :---- |
| Licensing & Registry Engine | Licensing & Registration Officer | B, D licensing services |
| Escrow / Trust-Account Audit | Compliance & Escrow Auditor | B escrow services, C approvals |
| Transaction Audit Queue | Compliance & Escrow Auditor | C transaction services, E title services |
| Tribunal & Remote-Litigation | Dispute Adjudication Officer | D, F dispute services |
| Inspection & Enforcement | Inspection & Enforcement Officer | B construction filings |
| Revenue & Settlement | Revenue & Finance Officer | All fee-bearing services |
| Admin & Configuration | System Super Administrator | Platform-wide |

The Inspection & Enforcement Officer is the emptiest role in the project: a named sub-system, an enforcement mandate in the PRD, and not one service anywhere in the source that produces an inspection, a stop-work notice, or a penalty. See `proposed-services.md` P-30 to P-32.

---

## The Group G Note

Group G also owns zero services, but for a different and less concerning reason.

Survey Companies, Valuers, Conveyancers and Registration Trustee Centres appear constantly *inside* other groups' workflows — "developer designates an accredited survey company", "visit Real Estate Registration Trustee Centres", "survey company prepares data and matches it to approved plans". They are participants in other groups' services rather than applicants with their own catalogue.

The Trustee Centre is the most heavily used: it is a named channel on a large share of the 145 services, acting on behalf of walk-in customers. **Group D is a notable exception** — none of its 26 sourced rows name a Trustee Centre or walk-in counter channel, suggesting this module may have no assisted-mode surface at all (flagged, not confirmed, in `modules/real-estate-service-companies/navigation.md`).

Roles are now documented (`modules/allied-professionals/roles-and-responsibilities.md`), but the interfaces themselves are not yet written.

> **Proposed** — Group G may not need a service catalogue at all, but does need documented interfaces for the actions it performs inside other groups' flows: survey data submission, valuation filing, and Trustee Centre operator transactions. Whether this is a module or a set of shared interface documents is an open question. Needs client confirmation.

**Checked 2026-08-15, unrelated to the Group C ownership correction.** This note and the Group A section above both use "owns zero services" in a group-level, catalogue-membership sense — how many of the 145 total services are filed under that group's own catalogue — not in the per-role, within-Group-C sense that `open-questions.md` A4 corrects. No change is needed here: A4 is about whether a service is restricted to a specific role *inside* Group C, not about which group a service belongs to.

**Group D's own Service #18 raised a comparable, smaller-scale ownership question on 2026-08-16** (whether Real Estate Evaluation Details Certificate belongs to Group D or Group G) — resolved by client decision to stay in Group D, though the service's own atypical shape (an evaluation company deciding on a customer's request, not RERA reviewing a company filing) still needs its own UI treatment. See the Group D profile below.

---

## Module Profiles

### Group B — Real Estate Developers (27 services)

The most heavily regulated external group, and the only one with UI documented before service flows — the reverse of the project's derivation chain. Service flows were written underneath the existing UI under issue #33 and merged by PR #36 on 2026-08-11.

| Source category | Services |
| :---- | :---: |
| Real Estate Development Services | 21 |
| Real Estate Licensing Service | 2 |
| Title Deed Data Services | 4 |

Escrow dominates: account activation, transfer, profit withdrawal, payment release, mortgage deposit, bank guarantee cancellation, expense cap amendment. Every one of these routes through a Group C Account Trustee, making B and C tightly coupled.

**Status:** all 19 screens migrated to `modules/real-estate-developer/ui/screens/`, shared component/validation/status-badge docs consolidated, source UI file retired. All 27 service-flow documents are in `modules/real-estate-developer/service-flows/`, merged by PR #36 on 2026-08-11 (issue #33), written against the pre-existing UI and cross-checked for mismatches rather than force-fit to it. Both layers were reconciled against the unified-access and per-transaction payment decisions under issue #58. Several gaps surfaced in that process: no UI screen exists for fee transfer between properties (#7), expense-cap amendment (#11), or either licensing service (#22, #23); the escrow surface's two generic actions (Register Escrow Account, Request Fund Release) represent seven distinct source rows (#8–#12, #20–#21) with no per-service UI distinction; and the Title Deed Data rows (#24, #25) can't be confidently pinned to one screen over another. Full detail in the PR description.

**Shared platform features rebuilt 2026-08-16, twice, and split once more.** The module's shared-features layer was rebuilt bottom-up from its 19 built screens (not sourced — no such concept exists in `RERAN_service_flows_v2.md`), landing at 12 features. A same-day client decision then split Service #10 (Project Profit Withdrawal) out of Fund Release Request into its own new feature — Profit Withdrawal Request — after confirming Fund Release Request's construction-milestone shape (Engineer Certificate, Quantity Surveyor Report, percentage complete) never genuinely fit a profit distribution. **No screen exists for the new feature**; its field list is proposed, not designed against a built UI. The module now stands at 13 shared features. See `modules/real-estate-developer/shared-platform-features.md`.

**Cross-module work with Group C, 2026-08-16.** Escrow status vocabulary reconciled across both modules to one sourced vocabulary, after two failed attempts that each drew from a UI screen's filter values instead of the underlying service files. "RERA Escrow Audit" (this module's term) and Group C's "Compliance & Escrow Auditor" confirmed to be the same regulatory role via the master table's Regulator/Approver column. Separately, Service #6 (Register Sale Associated with an Initial Mortgage) now validates its mortgage reference against Group C's Service #3 (Mortgage Registration) in real time, requiring a `Completed` match — a five-part product decision, not sourced, documented on both services' own files.

### Group D — Real Estate Service Companies (26 services)

Four distinct sub-domains under one group — the most internally varied module, and the only one built entirely from scratch in a single session following `module-build-playbook.md`'s six-phase sequence in strict order.

| Source category | Services |
| :---- | :---: |
| Jointly Owned Property Services | 11 |
| Real Estate Licensing Services | 8 |
| Real Estate Rental Services | 3 |
| Real Estate Transaction Services | 2 |
| Real Estate Dispute Services | 2 |

Jointly-owned property is effectively its own product: owners' associations, service-charge budgets, escrow accounts for joint properties, appointing auditors. Checked directly against source (`open-questions.md` A3): JOP's escrow-adjacent services do **not** mirror Group B's escrow mechanism the way an earlier note in this roadmap speculated — no Account Trustee intermediary is sourced anywhere in the JOP cluster; every JOP service routes directly from company to RERA's Compliance & Escrow Auditor.

**Status, 2026-08-16 — rebuilt from scratch, all six phases complete, Phase 6 audit done.** Every prior version of this module's documentation (roles-and-responsibilities.md, services-overview.md, README.md) was deleted at the client's explicit request to enable a clean rebuild, following the lessons `module-build-playbook.md` distilled from Groups B, C, and Individual User's own build histories. What follows is the result:

* **Phase 0 (Source Reconciliation):** 26 source rows (46–71, minus none) map 1:1 to 26 documented services — the cleanest reconciliation of any module in the project, with no consolidation or splitting needed, unlike Individual User (41→43) or Financial & Trust Institutions (two transposed rows).
* **Phase 1 (Foundational Docs):** `roles-and-responsibilities.md` and `services-overview.md`, built with the unified-access model from the start — Group D is the first module never to have gone through a role-permission-matrix phase at all, skipping the correction cycle Groups B and C both needed.
* **Phase 2 (Payments & Open Questions):** `payments.md` found three distinct payment models (following the 2026-08-16 B4 normalization) and a striking finding worth naming here: **19 of Group D's 26 services carry no fee at all** — a materially higher no-fee proportion than any other module (Financial & Trust Institutions: 1 of 18; Individual User: 5 of 43). `open-questions.md` answered 11 of 12 questions with a proposed position, the twelfth (exact fee amounts) being the expected client-data exception every module's payments analysis has had exactly one of.
* **Phase 3 (Service-Flow Documents):** all 26 files, 21-section template, each flagging its own proposed content explicitly.
* **Phase 4 (UI Screens):** 12 screens, `navigation.md`, `role-workflows.md`. Found three field-layout patterns (Pattern A dominant at 21 of 25 wizard-eligible services — the highest single-pattern concentration of any module), two email-only services at the time (later three, see below), and a Jointly Owned Property Register built as its own dedicated feature, matching Financial & Trust Institutions' Trust Accounts precedent.
* **Phase 5 (Shared Platform Features):** 8 features derived bottom-up from the actual screens — fewer than Financial & Trust Institutions' 12 or Real Estate Developer's 13, because Group D genuinely lacks the mechanisms (internal certification, Trustee-mediated escrow, recurring compliance reporting) those modules' extra features exist to model, not because the module itself is smaller.

**Two client decisions resolved and propagated 2026-08-16, after Phase 5 completed:**

* **A2 — Service #18 (Real Estate Evaluation Details Certificate) stays in Group D.** Its own sourced workflow still reads as a Valuer-facing process (an evaluation company deciding on a customer's request, not RERA reviewing a company's filing) — module ownership is settled, but the service's own atypical shape still has no designed screen. Propagated across 9 files.
* **B4 — Services #12–15 normalized to pay-before-lodging**, matching the precedent set for Financial & Trust Institutions' #1/#12/#18 on the very same day. Propagated across 12 files, simplifying the module's Progress Tracker, status vocabulary, and validation rules below what Phase 4 had originally built, since the post-decision payment scenario those additions existed to handle no longer occurs anywhere in the module.

**Phase 6 audit complete, 2026-08-16.** A survey pass found and corrected: **Section 17 (UI Screens) stale across 21 of 26 service-flow files** — each still said "Not yet built — Phase 4" even after Phase 4 completed, the same non-execution failure mode Individual User's and Financial & Trust Institutions' own audits found and named first. Also found during this pass, and initially flagged rather than fixed, then corrected in a follow-up: **Service #11's own Section 12 workflow contradicted its sourced email-only channel** (row 56 names only "Official email of the Jointly Owned Property," but the file's workflow text described portal-style "Sign Up / Log In," inherited uncorrected from the Service #5 cross-reference this file was originally derived from). Rewritten to match Services #6 and #19's email-based shape, propagated across nine sections of that file. **Group D now has three email-only services (#6, #11, #19), not two — the highest count of any module.** One item remains genuinely open, not yet built: **Service #18's own dedicated screen**, deliberately deferred pending a decision on whether the service's long-term home is Group D or Group G, rather than designed prematurely against an unsettled future.

### Group H — Public & Informational (33 services)

Highest service count, lowest complexity. Almost every service follows the same three-step shape: log in, select service, view information. No approver, no fee in most cases, no application lifecycle.

The exceptions worth noting: Fee Payment Receipt, Fee Refund Request (seven business days, Ministry of Finance approval), and Track Your Case — these have real workflows. The other 30 are lookups.

**Assessment:** cheapest module per service by a wide margin. A single well-designed lookup pattern covers most of it.

**Status:** roles and services overview documented. No service-flow documents written yet — the proposed single parameterised flow plus catalogue table is still just a proposal.

### Group E+F — Individual User (41 sourced services, 43 documented)

Service flows complete: 43 files under `modules/individual-user/service-flows/`. Roles, services overview, and shared platform features also documented.

The 41-to-43 relationship reconciles: ten tenant-dispute source rows are legitimately consolidated into one service, thirty-two services trace directly to source rows, and eleven are extrapolated from role descriptions rather than explicit rows. The `source_type` frontmatter field (`sourced` / `extrapolated`) records which is which.

**Status, updated 2026-08-15 — audit complete and propagated, not merely found.** The analysis layer (`payments.md`, `open-questions.md`, `navigation.md`, `role-workflows.md`) was built by checking all 43 service-flow files individually against the master table rather than trusting a module-wide pattern. That check surfaced, and this module has now corrected:

* A **systemic payment-timing documentation defect**: 19 of the 43 service-flow files carried a boilerplate Section 9 ("payment before submission") that contradicted either the file's own Trustee Centre workflow or the source row directly. Corrected across #5, #7, #9–#18, #23, #24, #26, #27, #28, #33, and #39 — see the Cross-Cutting Observations section below.
* **Five services with no fee at all**, contrary to their prior documentation: #17, #18, #33, and the Owner/Entity-Amendment half of #7. (#42 was already correctly documented as unspecified and needed no change.)
* A **genuine role-attribution conflict** on Register/Renew Lease (Services #23/#24), resolved after a conflict check: Landlord primary applicant, Tenant added as a documented secondary path. See `open-questions.md` B1.
* Four client-facing payment/mechanism questions (#27, #38, #6's Wallet Account, and — later — Fee Balance terminology) answered by the client and applied — see `open-questions.md` A5, A7, C1, C2.
* A cross-module leak — "Property Management Company," a Group D role — found in #23, #24, and #25's Who Can Apply sections and removed.

**UI package added and merged 2026-08-15, same day (PR #61).** 20 files under `modules/individual-user/ui/`, checking each of the 43 services' own Required Information sections individually rather than assuming Group C's 3-pattern model would scale unchanged — found **eleven distinct field-layout patterns**, plus two services (#30, #37) that route into other services' forms rather than collecting their own fields.

**Nine post-merge audit passes have followed, same day, each finding real issues the previous ones missed.** Summarized, not itemized here (full detail preserved in this file's own commit history): Section 13 status-flow gaps across eleven files; a stale UI status-vocabulary description that had propagated into six UI files; #30 and #37's routing-service payment rule contradicting their own architecture; a decided-but-never-executed clarifying note for #34; a missing fee-indicator option for routing services; three files (#40–#42) with stale "no UI yet" claims; #43 missing from `ui/README.md`'s Service × Form Matrix entirely (found by counting, not reading); and, in the ninth pass, a systematic check of every previously-unaudited file in the module — `navigation.md` (whose entire framing still assumed no UI existed), `role-workflows.md` (an internal contradiction about #41's payment timing), `services-overview.md` (a no-fee-exception count off by one), and `ui/validation-rules.md` (a stale Pattern C reference to #5, missed when #5 was reclassified two passes earlier).

**Both of this module's genuinely open items are now resolved, not just tracked.** `open-questions.md` D1 (the apparent Landlord/Tenant responsibility overlap in `roles-and-responsibilities.md`) turned out not to be a conflict at all — it's the module's own activity-scoped access principle (one account, multiple roles, different properties) applying correctly; the document now says so explicitly rather than leaving the overlap silent. `open-questions.md` C2 ("Fee Balance" terminology) was resolved by direct client confirmation: no such concept exists anywhere in this module, every payment settles instantly via the standard gateway. Two service-flow files (#6, #10) that had actually carried "Fee Balance Information" as an output artefact were corrected to remove it.

**Status:** the most complete and most thoroughly audited module in the project — service flows, analysis layer, and UI, all built, merged, internally consistent, and now with `open-questions.md` fully resolved (15/15, 0 awaiting client data). **The pattern worth naming across nine passes:** corrections have failed to fully land for at least three distinct reasons — drift (a fix made in one place, not propagated to documents that reference it by name), non-execution (a decision recorded but never actually carried out), and outright omission (something left out of a document entirely, not even wrongly described). All three look identical from the outside — a document says one thing, reality says another, or says nothing at all — but they need different checks to catch: drift needs cross-referencing between documents; non-execution needs checking a decision log against the file it was about; omission needs counting against a known total. **This same three-part pattern recurred in Group C on 2026-08-16, and again in Group D the same day** — see those profiles for fresh, smaller-scale instances of the same failure modes.

### Group C — Financial & Trust Institutions (18 services)

Roles, services overview, payments, and the full UI package are complete. 24 open questions sent to the client are recorded in `modules/financial-trust-institutions/open-questions.md`; all 24 are now answered, with 0 requiring client data (see that document's Summary).

**Status, fully corrected 2026-08-15.** All 18 service-flow files exist under `service-flows/`, **at full depth, not thin stubs.** This section previously claimed "only Service #1 has substantive depth... the other seventeen average around 1 KB and record workflow, documents, fees, channel, output and SLA as 'not specified in the available source material'" — that description is stale and was left uncorrected here even after the backfill it called for had actually happened. Every one of the 18 files carries genuinely sourced workflow, channel, output and SLA content traced to `RERAN_service_flows_v2.md` rows 28–45, alongside clearly marked proposed sections (required documents, business-rule inferences). The "Proposed Sequence" item below that once called this out as the top-priority next task is marked done, not pending.

Beyond the flow-depth backfill, Group C has also had its access model (no role restricts who may act on a service, A4) and payment model corrected throughout every service flow, `services-overview.md`, `payments.md`, `roles-and-responsibilities.md`, `navigation.md`, and the full 18-screen UI package. It is, as of 2026-08-15, the only module with both service flows and UI complete, merged, and internally consistent with each other — see "The Landscape" table above.

**Payment model, corrected three times now — 2026-08-15, twice, then normalized 2026-08-16.** The first 2026-08-15 pass concluded no Group C service is ever approved while payment is still pending, since #1 pays upfront (B11) and #2 carries no fee. A fuller audit of Services #12–#18 individually found that incomplete: **Services #12 and #18 genuinely sourced RERA's decision *before* the customer's counter payment**, unlike #13–#17, where the customer pays first. `Approved — Awaiting Payment` was restored, correctly scoped, across `services-overview.md`, `payments.md`, `ui/status-badges.md`, and two screens. **That exception is now retired, not just documented — a client decision on 2026-08-16 confirmed it was an artefact of the source's original counter-based process, not intentional design**, and normalized #12/#18 to pay before RERA's decision, matching #13–#17. `Approved — Awaiting Payment` no longer occurs for any Group C service, without exception. See `payments.md` and the two services' own files. **The same normalization pattern recurred the same day in Group D (#12–15, B4) — see that profile above.**

**Shared-features layer rebuilt 2026-08-16, then corrected the same day for a genuine error.** The prior 17-feature list (proposed by analogy to individual-user's count, never checked against Group C's own screens) was rebuilt bottom-up to 12 features, finding two genuinely new ones (Trust Accounts, Compliance Reports) the old list had missed entirely. Help & Support, previously `TBD` with no screen anywhere in the module, was built the same day at Claude's full discretion by client instruction — deliberately narrower than Real Estate Developer's version, dropping Training Resources and Feedback & Suggestions for an institutional audience.

**A genuine three-part error, caught and corrected the same day it was made — the same failure pattern Individual User's nine audit passes named first (see that profile above).** An earlier pass this same day incorrectly flagged Staff Management as an open gap ("no screen represents staff management at all"), when Institution Profile's Staff Records tab had already covered it in full. The client reasonably said "build one" in response to that wrong finding; a second pass then compounded it, writing a reference to a new "Feature #13 — Staff Records" into `services-overview.md` **without ever creating the file** — an omission stacked on a drift-adjacent misdiagnosis. Caught only when directly checked against the actual repository state, not assumed from the document's own prose. Corrected: no Feature #13 exists, none should, and the feature count reverts to 12.

**Cross-module work with Group B, 2026-08-16.** Escrow status vocabulary reconciled across both modules — see the Group B profile above for the full detail, which applies symmetrically here.

**What's genuinely still open:** each service-flow file's own Open Questions section (mostly exact fee amounts, still client data); #14/#18's field-layout classification in `ui/screens-unified/submit-application.md`, resolved by design judgement rather than sourced fact. **Note (2026-08-15), for whoever picks up Group C's still-open B2 (whether the wallet primitive P-22 is shared build across modules):** Individual User's Service #6 was found during that module's own payment audit to have no separate wallet mechanism after all — its "Wallet Account" language was a source-table artefact, not a real distinct payment path. Recorded here as context only; nothing in this note requires or implies a change to Group C's own files.

### Group G — Allied Professionals & Service Trustees (0 services)

Roles documented. See "The Group G Note" above for why this module has no service catalogue and what it needs instead.

**Status:** interfaces not yet written.

---

## Proposed Sequence

> **Proposed** — sequencing is our recommendation, not a client requirement. Needs confirmation.

**1. ~~Group C flow backfill.~~ Done, as of 2026-08-15.** *(Previously: "Smallest job on the list and it corrects a live inaccuracy: eighteen files currently assert the source is silent where it is not." This has been completed — see the Group C profile above. Retained here, struck through, rather than deleted, so the sequence's original numbering and reasoning stay legible.)*

**2. Group A.** Everything else terminates here, and its absence blocks every other module's flows from describing what happens after submission. Also the largest unknown, so learning its shape early de-risks the rest.

**3. Group B service flows.** UI already exists; writing the flows underneath completes the module and corrects the inverted derivation chain. Also unblocks the B↔C escrow coupling.

**4. ~~Individual User UI.~~ Done and merged, as of 2026-08-15.** *(Previously: "The mirror image of #3 — flows exist, screens don't. Closing this and #3 leaves the project with two fully round-tripped modules... to use as the house style for everything after," with a note that the Section 9 payment-timing correction pass had to land first. That correction pass finished earlier the same day, and the UI package — 20 files, checked service-by-service for field-layout pattern rather than assuming Group C's model would scale unchanged — was written immediately after and merged the same day, PR #61. See the Group E+F profile above. Retained here, struck through, rather than deleted, so the sequence's original reasoning stays legible.)*

**5. Group H.** Cheap, high volume, mostly one repeated pattern. Good candidate for batch work once the patterns from A and B are established.

**6. ~~Group D.~~ Done, as of 2026-08-16.** *(Previously: "Largest remaining unknown after A, and the JOP sub-domain may warrant splitting." Built from scratch in a single session, following `module-build-playbook.md`'s six phases in strict order, plus a Phase 6 audit that found and corrected a stale Section 17 pattern across 21 files and a genuine channel inconsistency in Service #11 — the first module to complete every phase, including the audit, without needing a later correction to fix an out-of-order build. See the Group D profile above. Retained here, struck through, rather than deleted, so the sequence's original reasoning stays legible.)*

**7. Group G interfaces.** Once the flows that reference survey companies and Trustee Centres exist, their interfaces can be derived from actual usage rather than guessed. **Group D's own finding that it may have no Trustee Centre channel at all is a useful negative data point for this item** — not every module needs a Group G interface dependency the way Group C or Individual User do.

The proposed-services list runs alongside this sequence rather than inside it: it needs a client decision before any of it becomes documentation work.

---

## Known Issues

| Issue | Module | Status |
| :---- | :---- | :---- |
| ~~17 of 18 service flows are thin stubs that record source-available data as unspecified~~ | Financial & Trust | **Resolved.** Backfilled from master table rows 28–45; all 18 files are at full depth. See the Group C profile above. |
| UI documented before service flows | Real Estate Developer | **Resolved.** 27/27 service flows written underneath the existing UI (issue #33) and merged by PR #36 on 2026-08-11. The reversed derivation order remains a historical note, not an outstanding gap. |
| ~~No UI documented at all~~ | Individual User | **Resolved 2026-08-15.** 20-file UI package written and merged (PR #61) — see the Group E+F profile above. |
| ~~Section 9 payment-timing boilerplate wrong in a subset of service-flow files~~ | Individual User | **Resolved 2026-08-15.** Corrected across #5, #7, #9–#18, #23, #24, #26, #27, #28, #33, #39. |
| ~~Register/Renew Lease role attribution unresolved (Tenant vs Landlord)~~ | Individual User | **Resolved 2026-08-15.** Landlord confirmed as primary applicant, Tenant added as a documented secondary path. See `open-questions.md` B1. |
| ~~Section 13 status flow, UI status-vocabulary drift, #30/#37 routing contradiction, #34's unexecuted B3 note, #40/#41/#42's stale UI claims, #43 missing from the Service × Form Matrix entirely, plus staleness in navigation.md/role-workflows.md/services-overview.md/validation-rules.md~~ | Individual User | **All resolved 2026-08-15**, across nine post-merge audit passes. See the Group E+F profile above for the summary and the three distinct failure modes (drift, non-execution, omission) they represent. |
| ~~`roles-and-responsibilities.md` untouched since 2026-08-09; Landlord/Tenant responsibilities still verbatim-overlap~~ | Individual User | **Resolved 2026-08-15.** Not a conflict — the module's own activity-scoped access principle (one account, both roles, different properties). Document updated to say so explicitly. See `open-questions.md` D1. |
| ~~"Fee Balance" terminology unresolved~~ | Individual User | **Resolved 2026-08-15.** Confirmed by client: no such concept exists in this module. #6 and #10's Output sections corrected. See `open-questions.md` C2. |
| ~~23 client questions outstanding~~ | Financial & Trust | **Resolved.** All 24 (23 original + B11, added 2026-08-15) are answered, 0 needing client data — see `open-questions.md`'s Summary directly rather than this table row. |
| ~~#12/#18 post-decision payment timing: intentional or artefact?~~ | Financial & Trust | **Resolved 2026-08-16.** Confirmed by client to be an artefact of the source's counter-based process, not intentional design. Normalized to pay-before-decision, matching #13–#17. `Approved — Awaiting Payment` no longer occurs for any Group C service. |
| ~~Staff Management flagged as an open gap~~ | Financial & Trust | **Resolved 2026-08-16 — the flag itself was wrong.** Institution Profile's Staff Records tab already covered this; a false gap finding led to a follow-on error (a reference to a never-built "Feature #13" written into `services-overview.md`). Both corrected the same day. See the Group C profile above. |
| ~~No documentation exists at all~~ | Real Estate Service Companies | **Resolved 2026-08-16.** Rebuilt from scratch: roles, services overview, payments, open-questions, 26 service flows, 12 UI screens, navigation, role-workflows, 8 shared features, and shared UI docs, following `module-build-playbook.md`'s six phases in order. See the Group D profile above. |
| ~~Section 17 (UI Screens) stale across 21 of 26 service-flow files~~ | Real Estate Service Companies | **Resolved 2026-08-16.** Each still said "Not yet built — Phase 4" after Phase 4 completed — the same non-execution failure mode found first in Individual User. Corrected across all 21 files. See the Group D profile above. |
| ~~Service #11's Section 12 workflow contradicts its own sourced email-only channel~~ | Real Estate Service Companies | **Resolved 2026-08-16.** Row 56 names an email-only channel; the file's workflow text previously described portal-style sign-up, inherited uncorrected from a cross-referenced service. Rewritten to match Services #6 and #19's email-based shape. See the Group D profile above. |
| Service #18 has no dedicated screen | Real Estate Service Companies | **Open, deliberately deferred.** Module ownership confirmed 2026-08-16, but the service's own atypical shape (an evaluation company deciding on a customer's request, not RERA reviewing a company's filing) doesn't fit the standard wizard. Design deferred pending clarity on whether the service's long-term home is Group D or Group G. |
| No application status vocabulary exists platform-wide | All | Proposed for Group C, **confirmed acceptable 2026-08-16**; still needs a platform-wide decision beyond Group C alone |
| Root `KnowledgeBase/README.md` lists seven projects; only RERAN is active | Project | Open |
| `RERAN/README.md` has four stub sections ("Modules", "Tech Stack", "Stakeholders", "Entry Points" all say "To be completed") despite this roadmap holding most of that detail already | Project | Open |
| The service catalogue carries instruments from its source jurisdiction that have no Nigerian equivalent (usufruct, Taqeemi certificate) while omitting ones that are mandatory here (Governor's Consent, C-of-O) | Project | Open — see proposed-services.md |

**Resolved since this roadmap was first written:** the 43 individual-user service/feature docs have been moved into `service-flows/`; the 295 KB Group B UI source file has been fully split into 19 screen files plus consolidated component/validation/status-badge docs and retired; the individual-user 39-vs-41 count discrepancy has been audited and closed; all 18 Group C service-flow files created *and backfilled to full depth*; Group C's 24 open questions fully answered (0 needing client data); Group C's payment model and role-specific ownership both corrected per client decision; **Group C's full 18-screen UI package written, reconciled, and merged (2026-08-15), then extended to 19 screens on 2026-08-16 (Help & Support)** — the first module with service flows and UI both complete; **Individual User's analysis layer written, corrected, and propagated the same day (2026-08-15)**; **Individual User's 20-file UI package written and merged the same day (PR #61)**; **nine post-merge audit passes the same day**, closing gaps of three distinct kinds (drift, non-execution, omission) across the service-flow files, the analysis layer, and the UI package, and finally **resolving both of the module's standing open questions (D1, C2) rather than leaving them tracked** — Individual User's `open-questions.md` now stands at 15/15 resolved, 0 awaiting client data, the only module in the project with a fully closed question log; **Group C's remaining payment exception (#12/#18) normalized away entirely on 2026-08-16**, and **a same-day Staff Management misdiagnosis (and its own follow-on documentation error) caught and corrected the same day it was introduced** — the drift/non-execution/omission pattern Individual User's nine passes first named, recurring at smaller scale in a different module; **Group B and C's escrow status vocabulary and terminology reconciled across both modules on 2026-08-16**, and **Group B's Service #10 (Project Profit Withdrawal) split into its own new feature**, with a new real-time cross-module mortgage-validation dependency added between Group B's Service #6 and Group C's Service #3 the same day; **Group D built from scratch in a single session on 2026-08-16**, following `module-build-playbook.md`'s six phases in order — the first module to complete all six without an out-of-order correction — with two client decisions (A2, B4) resolved and propagated across roughly 30 files, and a Phase 6 audit that found and corrected the same non-execution failure mode (stale "Not yet built" claims) that Individual User's own audit first named, across 21 of the module's 26 service-flow files, plus a genuine channel inconsistency in Service #11 that was corrected the same day it was found.

---

## Cross-Cutting Observations

**Escrow is the platform's spine.** It appears in Group B (developer drawdowns), Group C (trustee certification, auditor review), Group D (jointly-owned property accounts), and Group A (compliance audit). Four groups, one mechanism. It is the strongest candidate for a shared reference document rather than four independent descriptions. **Corrected 2026-08-16**: Groups B and C's own escrow status vocabularies were reconciled to one sourced vocabulary this session — a first concrete step toward that shared reference, though still living as duplicated-but-now-consistent content in each module rather than a single document either module points to. **Group D's own escrow-adjacent JOP services turned out not to share the mechanism at all** (`open-questions.md` A3, checked directly against source) — a useful negative data point showing "escrow" as a subject-matter label doesn't always imply a shared processing mechanism, even within one platform.

**The Trustee Centre channel is pervasive.** A large share of services across E, F and C list Real Estate Registration Trustee Centres as a channel, sometimes as the only channel. Whether those services gain online equivalents is a scope decision that affects several modules at once. **Group D is the first module found to plausibly have none of this channel at all** — none of its 26 sourced rows name a Trustee Centre or walk-in counter, flagged rather than confirmed in `modules/real-estate-service-companies/navigation.md`.

**Corrected 2026-08-14, then repeatedly on 2026-08-15 — this platform-wide claim has needed narrowing so many times it is now the case study for this roadmap's own standing skepticism rule (see below), not just a historical record of what changed.** It was originally sourced from Group C's `payments.md` pipeline definition and generalized without checking other modules. Group C's own model needed two corrections (upfront-by-default, then #12/#18's exception restored). Group B needed a correction adding six further exceptions Group C's fix hadn't anticipated. Individual User then broke the claim in three further ways: a systemic Section-9-vs-workflow contradiction across roughly half its 43 files; that fix's own Section 13 status-flow gap, found and closed in a later pass; and that closure's own new terminology never reaching the UI layer that cited it, found and closed in a third pass. **Group C's #12/#18 exception was itself retired on 2026-08-16 — and Group D's own comparable #12–15 exception was found and retired the same day**, before that module's UI package had even shipped a workaround the way Group C's briefly did. The case study's own subject matter changed again after this paragraph was last revised, which is itself further evidence for the paragraph's point. Full detail on each correction is preserved in this section's own edit history within the file, not restated here — the count is now nine corrections to one paragraph, and the paragraph's own repeated wrongness is itself the finding worth keeping.

**The actual pattern, as verified across Groups B, C, D, and Individual User: payment timing is not uniform and cannot be inferred from a neighbouring service, a category, a module, or even that module's own documentation without checking the underlying source row directly.** Roughly two-thirds of fee-bearing services pay before a decision; **as of 2026-08-16, both Group C's and Group D's own remaining exceptions have been normalized away, leaving both modules internally uniform on this question.** Group B and Individual User still carry genuine exceptions. Groups H and A remain entirely unaudited on this question. Treat any future "no exception remains" or "the documentation is accurate" claim on this topic with real skepticism until it's been checked service-by-service, section-by-section, and layer-by-layer, against the source directly — not module-by-module or file-by-file. This same skepticism now extends beyond payment timing specifically: Individual User's nine audit passes found comparable-shaped gaps (drift, non-execution, omission) in role attribution, UI architecture, and document indexing too, not just payments — **and both Group C and Group D reproduced the same three-part pattern at smaller scale on 2026-08-16** (see those modules' profiles above). The underlying lesson generalizes: a correction is not verified complete until checked against every document that could reference it, not just the one it was made in.

**Corrected 2026-08-16 — the claim below is now wrong and needs its own correction, not just a footnote.** "Three groups share the same four application-management features. Submit, Track, Respond to Information Request, Resubmit" was accurate when written for Individual User and as a starting proposal for Group C, but **neither Group B, Group C, nor Group D actually landed on that four-feature shape once their shared-features layers were rebuilt from their own actual built screens.** Group C restructured to a 2-feature Application Lifecycle (Service Requests, Applications) after finding its four originally-proposed features were really two screens described twice. Group B restructured to a 7-feature Application Lifecycle (Applications, five domain workspaces, and a newly split-out Profit Withdrawal Request) with no single canonical submission form at all — the four-feature pattern never fit Group B's actual UI shape to begin with. **Group D's own Application Lifecycle also landed on 2 features (Service Requests, Applications), matching Group C's shape rather than the original four-feature proposal** — built this way from the start, in Group D's case, rather than reached by correcting an earlier guess. **Only Individual User genuinely uses the four-feature Submit/Track/Respond/Resubmit pattern as documented.** The "define once at platform level" instinct behind the original claim may still be right, but the concrete shape it should take is not what this paragraph originally proposed — worth a fresh look, not a revival of the old four-feature model.

**The service catalogue and the PRD were written from different starting points.** The catalogue is a mature, operational service list ported from another jurisdiction's land department; the PRD is written for Nigeria from first principles. They agree on registration, licensing and payments, and diverge sharply on complaints, enforcement and title instruments. Reconciling the two is the substance of `proposed-services.md`.
