---
project: RERAN
type: overview
status: current
updated: 2026-08-15
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
| **B** | Real Estate Developers | 27 | 4 | 3 | UI complete (19 screens); 27/27 service flows merged (issue #33, PR #36, merged 2026-08-11); both reconciled against the unified-access and per-transaction payment decisions (issue #58) |
| **C** | Financial & Trust Institutions | 18 | 4 | 3 | 18 service-flow files at full depth; 18 UI screens documented (13 in `ui/screens/`, 5 in `ui/screens-unified/`); the only fully round-tripped module so far — source → flows → UI, merged |
| **D** | Real Estate Service Companies | 26 | 4 | 4 | Roles, services overview; no service flows |
| **E+F** | Individual User | 41 | 6 | 4 | 43 service flows written; count reconciled; `payments.md`, `open-questions.md`, `navigation.md`, and `role-workflows.md` added 2026-08-15 (analysis layer), findings propagated into the service-flow files; UI package added 2026-08-15 (20 files: README, components, validation-rules, status-badges, 4 `ui/screens-unified/`, 12 `ui/screens/`), merged (PR #61) |
| **G** | Allied Professionals & Service Trustees | **0** | 4 | 3 | Roles documented; interfaces not written — see note below |
| **H** | Public & Informational Users | 33 | 2 | 2 | Roles, services overview; no service flows |
| | **Total** | **145** | **28** | | |

Service counts are verified row by row against the master service table and reconcile exactly with the source workbook's own summary. The individual-user module's count now reconciles too — see Known Issues for how.

**Pattern worth naming, corrected 2026-08-15 (four times).** This section originally said "no module has both stages complete and merged yet," then was corrected to name **Group C** as the first module with service flows and UI both complete and merged, then corrected again to add **Group B** as equally complete and merged first (PR #36, 2026-08-11). **Individual User closed the same gap a third way, same day, and its UI package has since merged too (PR #61)** — this section previously said the package was "complete and PR-ready" but "not merged into `main` yet as of this writing," which was accurate when written and is now stale; the merge happened later the same day. There are now **three** modules with both stages complete and merged, not two: Group B, Group C, and Individual User. Group C remains the cleanest house-style example, since its derivation ran source → flows → UI in strict order; Individual User's ran the same order but with an analysis layer inserted between flows and UI; Group B's ran backwards (UI first).

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

**Why this matters:** every one of the 145 external services terminates in a Group A action. The Compliance & Escrow Auditor alone is the approver for all 18 Group C services and most of Group B's. Without Group A documented, no external service flow can describe what happens after submission, and the back-office is the largest unspecified area of the platform.

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

The Trustee Centre is the most heavily used: it is a named channel on a large share of the 145 services, acting on behalf of walk-in customers.

Roles are now documented (`modules/allied-professionals/roles-and-responsibilities.md`), but the interfaces themselves are not yet written.

> **Proposed** — Group G may not need a service catalogue at all, but does need documented interfaces for the actions it performs inside other groups' flows: survey data submission, valuation filing, and Trustee Centre operator transactions. Whether this is a module or a set of shared interface documents is an open question. Needs client confirmation.

**Checked 2026-08-15, unrelated to the Group C ownership correction.** This note and the Group A section above both use "owns zero services" in a group-level, catalogue-membership sense — how many of the 145 total services are filed under that group's own catalogue — not in the per-role, within-Group-C sense that `open-questions.md` A4 corrects. No change is needed here: A4 is about whether a service is restricted to a specific role *inside* Group C, not about which group a service belongs to.

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

### Group D — Real Estate Service Companies (26 services)

Four distinct sub-domains under one group — the most internally varied module.

| Source category | Services |
| :---- | :---: |
| Jointly Owned Property Services | 11 |
| Real Estate Licensing Services | 8 |
| Real Estate Rental Services | 3 |
| Real Estate Transaction Services | 2 |
| Real Estate Dispute Services | 2 |

Jointly-owned property is effectively its own product: owners' associations, service-charge budgets, escrow accounts for joint properties, appointing auditors. Several JOP services mirror Group B's escrow services with different actors.

**Status:** roles and services overview documented. No individual service-flow documents written yet.

### Group H — Public & Informational (33 services)

Highest service count, lowest complexity. Almost every service follows the same three-step shape: log in, select service, view information. No approver, no fee in most cases, no application lifecycle.

The exceptions worth noting: Fee Payment Receipt, Fee Refund Request (seven business days, Ministry of Finance approval), and Track Your Case — these have real workflows. The other 30 are lookups.

**Assessment:** cheapest module per service by a wide margin. A single well-designed lookup pattern covers most of it.

**Status:** roles and services overview documented. No service-flow documents written yet — the proposed single parameterised flow plus catalogue table is still just a proposal.

### Group E+F — Individual User (41 sourced services, 43 documented)

Service flows complete: 43 files under `modules/individual-user/service-flows/`. Roles, services overview, and shared platform features also documented.

The 41-to-43 relationship reconciles: ten tenant-dispute source rows are legitimately consolidated into one service, thirty-two services trace directly to source rows, and eleven are extrapolated from role descriptions rather than explicit rows. The `source_type` frontmatter field (`sourced` / `extrapolated`) records which is which.

**Status, updated 2026-08-15 — audit complete and propagated, not merely found.** The analysis layer (`payments.md`, `open-questions.md`, `navigation.md`, `role-workflows.md`) was built by checking all 43 service-flow files individually against the master table rather than trusting a module-wide pattern. That check surfaced, and this module has now corrected:

* A **systemic payment-timing documentation defect**: 19 of the 43 service-flow files carried a boilerplate Section 9 ("payment before submission") that contradicted either the file's own Trustee Centre workflow or the source row directly. Corrected across #5, #7, #9–#18, #23, #24, #26, #27, #28, #33, and #39 — see the Cross-Cutting Observations section below, which this finding now feeds into alongside the existing Group B and Group C exceptions. (A 20th file, #25, was also corrected in this pass, but for an unrelated reason — see the cross-module-leak bullet below, not this one.)
* **Five services with no fee at all**, contrary to their prior documentation: #17, #18, #33, and the Owner/Entity-Amendment half of #7. (#42 was already correctly documented as unspecified and needed no change.) The same shape as Group C's Service #2 and Group B's Service #19.
* A **genuine role-attribution conflict** on Register/Renew Lease (Services #23/#24) between the master table (names Tenant), the service-flow files (previously framed Landlord-only), and this module's own `roles-and-responsibilities.md` (gives both roles overlapping "register/renew lease" responsibilities). Resolved by client instruction after a conflict check found nothing else in the module assumed single-actor exclusivity: Landlord remains primary applicant, Tenant added as a documented secondary path. See `open-questions.md` B1.
* Three client-facing payment/mechanism questions (online-channel fee parity for #27, whether Submit Complaint should charge at all, and whether a separate Wallet Account mechanism exists) were answered by the client and applied — see `open-questions.md` A5, A7, C1.
* A cross-module leak — "Property Management Company," a Group D role — found in #23, #24, and #25's Who Can Apply sections and removed.

**UI package added and merged 2026-08-15, same day (PR #61).** 20 files under `modules/individual-user/ui/`: a README with a Service × Form Matrix, `components.md`, `validation-rules.md`, `status-badges.md`, 4 `screens-unified/` files (Services Catalog, Service Details, the configurable Submit Application wizard, Application Review), and 12 `screens/` files (Dashboard, My Properties, My Leases, Applications, Application Details, My Complaints, Power of Attorney, Documents, Payment History, Notifications, Profile & KYC, Help & Support). Checking each of the 43 services' own Required Information sections individually — rather than assuming Group C's 18-service, 3-pattern wizard model would scale up unchanged — found **eleven distinct field-layout patterns**, not three, plus two services (#30, #37) that route into other services' forms rather than collecting their own fields. Two genuine gaps remain, both flagged rather than guessed at: Pattern G's ten dispute sub-types (#26) need their own field/document matrix before that branch of the wizard can be built out fully, and #42's field set is inferred from #29's mirror shape since the source itself specifies nothing for it.

**Audit pass, 2026-08-15, after the UI merge.** A full pass over the merged module found and corrected two further gaps the correction pass itself had introduced: (1) Section 13 (Application Status Flow) in #9–#16, #23, #24, and #26 still showed only the online channel's upfront payment sequence, with no status reflecting the Trustee Centre / Service Center channel's audit-then-pay timing that Section 9/12 already documented for the same eleven files — an "Audited — Awaiting Payment" status was added to each, following the files' own existing convention for channel-specific statuses (#27 was checked and needed no change). (2) The module's own top-level `README.md` had never been updated to index the analysis layer or UI package, still reflecting the module's 2026-08-10 state. Also found, not fixed: `roles-and-responsibilities.md` remains unedited since 2026-08-09 and still gives Landlord and Tenant verbatim-overlapping responsibilities — B1 had flagged this as needing a client flag but the flag was never actually raised anywhere trackable; it is now tracked as `open-questions.md` D1.

**Status:** the most complete module in the project — service flows, analysis layer, and UI, all built, merged, and internally consistent with each other, including a post-merge audit pass. One standing item remains client-facing: `open-questions.md` D1.

### Group C — Financial & Trust Institutions (18 services)

Roles, services overview, payments, and the full UI package are complete. 24 open questions sent to the client are recorded in `modules/financial-trust-institutions/open-questions.md`; all 24 are now answered, with 0 requiring client data (see that document's Summary).

**Status, fully corrected 2026-08-15.** All 18 service-flow files exist under `service-flows/`, **at full depth, not thin stubs.** This section previously claimed "only Service #1 has substantive depth... the other seventeen average around 1 KB and record workflow, documents, fees, channel, output and SLA as 'not specified in the available source material'" — that description is stale and was left uncorrected here even after the backfill it called for had actually happened. Every one of the 18 files carries genuinely sourced workflow, channel, output and SLA content traced to `RERAN_service_flows_v2.md` rows 28–45, alongside clearly marked proposed sections (required documents, business-rule inferences). The "Proposed Sequence" item below that once called this out as the top-priority next task is marked done, not pending.

Beyond the flow-depth backfill, Group C has also had its access model (no role restricts who may act on a service, A4) and payment model corrected throughout every service flow, `services-overview.md`, `payments.md`, `roles-and-responsibilities.md`, `navigation.md`, and the full 18-screen UI package. It is, as of 2026-08-15, the only module with both service flows and UI complete, merged, and internally consistent with each other — see "The Landscape" table above.

**Payment model, corrected twice on 2026-08-15.** The first pass concluded no Group C service is ever approved while payment is still pending, since #1 pays upfront (B11) and #2 carries no fee. A fuller audit of Services #12–#18 individually — checking each one's own sourced workflow order, not just the ones the correction was originally scoped to — found that conclusion was incomplete: **Services #12 and #18 genuinely source RERA's decision *before* the customer's counter payment**, unlike #13–#17, where the customer pays first. `Approved — Awaiting Payment` is real for exactly these two services and has been restored, correctly scoped, across `services-overview.md`, `payments.md`, `ui/status-badges.md`, and the two screens (`applications.md`, `application-details.md`) that reference it.

**What's genuinely still open:** each service-flow file's own Open Questions section (mostly exact fee amounts, still client data); #14/#18's field-layout classification in `ui/screens-unified/submit-application.md`, resolved by design judgement rather than sourced fact; and whether #12/#18's post-decision payment timing is intentional or should be normalized, flagged for the client in `payments.md`'s and `services-overview.md`'s own To Confirm sections. **Note (2026-08-15), for whoever picks up Group C's still-open B2 (whether the wallet primitive P-22 is shared build across modules):** Individual User's Service #6 was found during that module's own payment audit to have no separate wallet mechanism after all — its "Wallet Account" language was a source-table artefact, not a real distinct payment path. Recorded here as context only; nothing in this note requires or implies a change to Group C's own files.

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

**6. Group D.** Largest remaining unknown after A, and the JOP sub-domain may warrant splitting.

**7. Group G interfaces.** Once the flows that reference survey companies and Trustee Centres exist, their interfaces can be derived from actual usage rather than guessed.

The proposed-services list runs alongside this sequence rather than inside it: it needs a client decision before any of it becomes documentation work.

---

## Known Issues

| Issue | Module | Status |
| :---- | :---- | :---- |
| ~~17 of 18 service flows are thin stubs that record source-available data as unspecified~~ | Financial & Trust | **Resolved.** Backfilled from master table rows 28–45; all 18 files are at full depth. See the Group C profile above. |
| UI documented before service flows | Real Estate Developer | **Resolved.** 27/27 service flows written underneath the existing UI (issue #33) and merged by PR #36 on 2026-08-11. The reversed derivation order remains a historical note, not an outstanding gap. |
| ~~No UI documented at all~~ | Individual User | **Resolved 2026-08-15.** 20-file UI package written and merged (PR #61) — see the Group E+F profile above. |
| ~~Section 9 payment-timing boilerplate wrong in a subset of service-flow files~~ | Individual User | **Resolved 2026-08-15.** Corrected across #5, #7, #9–#18, #23, #24, #26, #27, #28, #33, #39. See the Group E+F profile above and `payments.md`'s Downstream Corrections section. |
| ~~Register/Renew Lease role attribution unresolved (Tenant vs Landlord)~~ | Individual User | **Resolved 2026-08-15.** Landlord confirmed as primary applicant, Tenant added as a documented secondary path, after a conflict check found nothing else in the module assumed single-actor exclusivity. See `open-questions.md` B1. |
| ~~Application Status Flow (Section 13) in #9–#16, #23, #24, #26 didn't reflect the Trustee Centre / Service Center channel's audit-then-pay timing~~ | Individual User | **Resolved 2026-08-15**, found in a post-merge audit pass. "Audited — Awaiting Payment" added to each. See the Group E+F profile above. |
| `roles-and-responsibilities.md` untouched since 2026-08-09; Landlord/Tenant responsibilities still verbatim-overlap | Individual User | Open — flagged to the client as `open-questions.md` D1 rather than silently edited. |
| ~~23 client questions outstanding~~ | Financial & Trust | **Resolved.** All 24 (23 original + B11, added 2026-08-15) are answered, 0 needing client data — see `open-questions.md`'s Summary directly rather than this table row. |
| No application status vocabulary exists platform-wide | All | Proposed for Group C; needs a platform decision |
| Root `KnowledgeBase/README.md` lists seven projects; only RERAN is active | Project | Open |
| `RERAN/README.md` has four stub sections ("Modules", "Tech Stack", "Stakeholders", "Entry Points" all say "To be completed") despite this roadmap holding most of that detail already | Project | Open |
| The service catalogue carries instruments from its source jurisdiction that have no Nigerian equivalent (usufruct, Taqeemi certificate) while omitting ones that are mandatory here (Governor's Consent, C-of-O) | Project | Open — see proposed-services.md |

**Resolved since this roadmap was first written:** the 43 individual-user service/feature docs have been moved into `service-flows/`; the 295 KB Group B UI source file has been fully split into 19 screen files plus consolidated component/validation/status-badge docs and retired; the individual-user 39-vs-41 count discrepancy has been audited and closed, with four genuinely undocumented services added and a `source_type` field introduced to distinguish sourced from extrapolated services; all 18 Group C service-flow files created *and backfilled to full depth*; Group C's 24 open questions fully answered (0 needing client data); Group C's payment model and role-specific ownership both corrected per client decision, with the payment correction itself needing a follow-up fix once #12/#18's exception was found; **Group C's full 18-screen UI package written, reconciled against both corrections, and merged (2026-08-15)** — the first module with service flows and UI both complete; **Individual User's analysis layer written (2026-08-15)**, surfacing a payment-timing documentation defect and a role-attribution conflict; **both of those findings corrected and propagated into the affected service-flow files, and three further client-facing payment questions answered and applied, the same day (2026-08-15)**; **Individual User's 20-file UI package written and merged the same day (PR #61)**, checked service-by-service for field-layout pattern (11 patterns found, not Group C's 3) rather than assumed; **a post-merge audit pass the same day** found and fixed a Section 13 status-flow gap across 11 files and an out-of-date module README — Individual User is now the most complete module in the project across every layer, with one standing client-facing flag (`open-questions.md` D1).

---

## Cross-Cutting Observations

**Escrow is the platform's spine.** It appears in Group B (developer drawdowns), Group C (trustee certification, auditor review), Group D (jointly-owned property accounts), and Group A (compliance audit). Four groups, one mechanism. It is the strongest candidate for a shared reference document rather than four independent descriptions.

**The Trustee Centre channel is pervasive.** A large share of services across E, F and C list Real Estate Registration Trustee Centres as a channel, sometimes as the only channel. Whether those services gain online equivalents is a scope decision that affects several modules at once.

**Corrected 2026-08-14, then three more times on 2026-08-15 — this platform-wide claim has needed repeated narrowing, not one clean fix.** It was originally sourced from Group C's `payments.md` pipeline definition and generalized here without checking the other modules against it. Individual User's Service #8 (`Payment must be completed before the application proceeds for regulatory review`) and Real Estate Developer's Service #1 (identical pattern) both pay **upfront, before submission** — the opposite of what this observation first claimed. Group C's own payment model was then corrected (2026-08-14, `open-questions.md` B1) so that most of its 18 services pay upfront too. A second correction (2026-08-15, B11) moved Service #1 to upfront payment as well and confirmed Service #2 carries no fee, which this document briefly took to mean "no documented exception remains anywhere." **That was also wrong.** A fuller per-service check of #12–#18 — the group this document had been treating as a single uniform "pays at the point of service" category — found that Services #12 and #18 genuinely source payment *after* RERA's decision, not before or alongside it like #13–#17. **Corrected a fourth time, 2026-08-15 (issue #58) — and the skepticism this paragraph asked for was warranted within days.** The claim that "Group C Services #12 and #18 are the platform's remaining documented exception" was itself another module-blind generalization: it was made without auditing Group B's 27 services, and Group B turns out to hold **six more exceptions**. Services #13, #15, #17, #22 and #26 each place RERA's accept/reject decision *before* the fee is paid, and Service #24 has **two** payment steps — one before Survey Department review and one after approval — the only dual-stage fee on the platform. Service #19, meanwhile, was documented as carrying no fee at all when its source row plainly reads "Pay fees and send application online."

**Corrected a fifth time, 2026-08-15 — Individual User was the third module checked, and it broke this claim in a new way none of the first four corrections anticipated.** Every correction so far had been about *where in the sequence* payment falls relative to RERA's decision. Individual User's audit (`payments.md`) found something structurally different: **the module's own service-flow files asserted a uniform "pay before submission" rule in their Section 9 field that was simply wrong against their own cited source, for roughly half of the module's 43 files.** Individual User's Service #28 (Request Rental Valuation, row 84) is the cleanest single exception found on the whole platform so far — the source states outright, with no ordering to infer, "Pay fees after approval." Individual User also holds **five services flagged as no-fee or unspecified-fee**, contrary to their original documentation: #17, #18, #33, and one branch of #7 are confirmed no-fee on the same contrast-with-neighbours evidence Group C used for its own Service #2; #42 is a softer case, correctly flagged as unspecified in source rather than confirmed either way. That's the same shape as Group C's Service #2 and Group B's (apparently mis-documented) Service #19 — meaning at least three of the platform's eight modules now have a confirmed or suspected no-fee exception, not one.

**Updated 2026-08-15, same day — this is a correction to the correction, not a sixth new finding.** The paragraph above was written when Individual User's payment-timing defect had only been *found*, not yet *fixed*. It has since been fixed: all twenty affected service-flow files (#5, #7, #9–#18, #23, #24, #26, #27, #28, #33, #39) have been corrected to match their source rows, and three further payment questions (online-channel fee parity for tenancy cancellation, whether complaint filing should charge, and a suspected Wallet Account mechanism that turned out not to exist) were put to the client and resolved. Individual User's documentation no longer contains the defect described above — it is recorded here as a completed finding, not an open one. This is itself worth noting as a small piece of evidence for the pattern below: a module-wide documentation defect, once found and checked service-by-service, can be fixed completely in the same pass it was discovered in — the earlier corrections to this section (Groups B and C) took multiple passes each because the underlying payment *model* itself needed a client decision each time; Individual User's defect was a transcription error against an already-settled source, which is a faster class of problem to close. **Except that claim itself needed one more narrowing, found in a later audit pass the same day: the correction pass fixed Section 9/12 (the payment-timing narrative) in #9–#16, #23, #24, and #26, but left Section 13 (the Application Status Flow) in those same eleven files still showing only the online channel's upfront sequence — a fix applied to two of a file's three payment-relevant sections is not yet a complete fix.** That gap has since been closed too, but the pattern holds: even a same-day, service-by-service fix can leave a section unchecked if the check itself doesn't enumerate every section a finding touches.

**The actual pattern, as verified as of 2026-08-15 across Groups B, C, and Individual User: payment timing is not uniform and cannot be inferred from a neighbouring service, a category, or a module — and in at least one module, it could not even be trusted from that module's own documentation without checking the underlying source row directly (though that module's documentation has since been corrected to match).** Roughly two-thirds of fee-bearing services pay before a decision; at least eight pay after; one pays twice; several carry no fee at all. Groups D, H, and A remain entirely unaudited on this question. Given this observation has now been wrong in six successive ways — never checked against other modules; then checked against other modules but not against every service within Group C itself; then corrected for Group C's edges but not its own internal exceptions; then corrected for all of Group C while still asserting a platform-wide conclusion with Group B entirely unaudited; then corrected for Group B while assuming every module's own documentation could be trusted at face value, which Individual User's audit disproved; then, even after Individual User's fix, incomplete within its own scope until a status-flow section was separately checked — treat any future "no exception remains" or "the documentation is accurate" claim on this topic with real skepticism until it's been checked service-by-service and section-by-section, against the source directly, not module-by-module or file-by-file.

**Three groups share the same four application-management features.** Submit, Track, Respond to Information Request, Resubmit. Documented for Individual User, proposed for Group C, and certainly needed by B and D. These should be defined once at platform level.

**The service catalogue and the PRD were written from different starting points.** The catalogue is a mature, operational service list ported from another jurisdiction's land department; the PRD is written for Nigeria from first principles. They agree on registration, licensing and payments, and diverge sharply on complaints, enforcement and title instruments. Reconciling the two is the substance of `proposed-services.md`.
