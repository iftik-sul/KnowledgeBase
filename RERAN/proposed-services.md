---
project: RERAN
type: overview
status: draft
updated: 2026-08-10
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
tags:
  - proposals
  - services
  - gap-analysis
---

# Proposed Additional Services

> **Everything in this document is a proposal.** None of it appears in the source material. It is the output of reading all four source-of-truth documents against each other and recording where they disagree or fall silent. Nothing here should be built, and no service number here should enter a module, until the client has accepted it.

---

## Why This Document Exists

The four source documents were not written together, and it shows.

**The 145-service catalogue is an operational service list inherited from another jurisdiction's land department.** The evidence is in the vocabulary: usufruct registration, "Taqeemi certificate" verification, "names of ancient and modern regions", Real Estate Registration Trustee Centres, an escrow-first off-plan regime, and "Land Department website" as the channel on nearly every row. It is a good catalogue — mature, complete, operationally specific, with real SLAs — but it describes a market that is not Nigeria's.

**The PRD is written for Nigeria from first principles.** It names the Land Use Act, the Certificate of Occupancy, NIN/BVN/CAC verification, NDPA 2023, state-federal harmonisation, diaspora capital, and 'Omonile' fraud. The user group structure's "Nigerian Design Principles" section makes the adaptation explicit: C-of-O replaces the title-deed primitive, a State Liaison role reconciles with State Lands Bureaus, escrow gates off-plan sales.

The adaptation was declared at principle level but never carried down into the service table. The result is a catalogue that contains services Nigeria has no legal basis for, and omits services Nigerian law makes mandatory.

Three further categories of gap emerged: PRD requirements with no corresponding service, capabilities referenced inside service rows but never catalogued as services themselves, and the entire internal work of the regulator.

---

## Numbering

Proposed services use a project-wide `P-NN` series so they can never be confused with the sourced 1–145. If the client accepts one, it takes the next free number in its module's own series and its entry here is marked accepted.

---

## Tier 1 — The PRD Requires It, The Catalogue Has No Service

These are the strongest claims in the document. Each maps to a numbered requirement or user story the PRD already commits to.

| ID | Proposed service | Group | Basis | Evidence of the gap |
| :---- | :---- | :---: | :---- | :---- |
| **P-01** | File a complaint against a developer (non-delivery, abandonment, defects) | F, E | FR-11, US-07, PRD Use Case 3 | The catalogue's only dispute services are tenancy tribunal cases (rows 72–81) and joint-property suits (57–58). The PRD's flagship worked example — a buyer whose off-plan property was never delivered — has nowhere to go. |
| **P-02** | File a complaint against an agent, broker or valuer | F | FR-11 | "Misrepresentation by unlicensed agents" is named in PRD §2.1 as a top-tier problem. No service lets anyone report it. |
| **P-03** | Respondent submission to a complaint | B, D | PRD Use Case 3 | The PRD gives the developer a configurable response window (e.g. 14 days) "through the portal". No service exists on the respondent side. |
| **P-04** | CPD evidence upload and renewal eligibility check | D, G | FR-07, PRD Use Case 2 | Use Case 2 has the system validate CPD hours and block renewal where complaints or fees are outstanding. Row 62 renews the practice card on automatic approval, with no gate at all. |
| **P-05** | Licence suspension, revocation and reinstatement | A → B, D | FR-06 | FR-06 puts suspension in launch scope. Row 63 is voluntary cancellation by the holder — the opposite action. |
| **P-06** | Institutional bulk and API verification | H | FR-09, NFR-07 | Registration Flow 9 onboards Institutional Verifiers, issues scoped API keys and records usage quotas. The service table gives that role zero services to consume. |
| **P-07** | Fee estimate before application | All | FR-16 | The fee engine computes at submission. Row 128 is a project-scoped fee indicator only. An applicant cannot find out what a service costs before starting it. |
| **P-08** | USSD channel for verification, status and payment | H, E, F | FR-15, PRD risk table | FR-15 requires USSD payment support and the risk table names USSD/SMS fallback as the mitigation for connectivity limits. Not one of the 145 rows uses USSD as a channel. |

---

## Tier 2 — Nigerian Legal Instruments The Catalogue Cannot Express

| ID | Proposed service | Group | Basis | Note |
| :---- | :---- | :---: | :---- | :---- |
| **P-09** | Governor's Consent application and tracking | E, G | Land Use Act s.22 | **The single largest legal gap.** No assignment, mortgage, sublease or transfer of a statutory right of occupancy is valid in Nigeria without the Governor's consent. Every transfer service in the catalogue (rows 86–96) assumes no consent gate exists. |
| **P-10** | C-of-O verification against the State Lands Bureau | H, E | User group structure §4 | The design principles state C-of-O verification "replaces the Title-Deed primitive throughout", and give the State Liaison Coordinator responsibility for harmonising C-of-O data. No service implements either. |
| **P-11** | Perfection-of-title case (consent → stamp duty → registration as one tracked case) | E | Business goal 2 | Perfection is the actual Nigerian pain point: three processes, three agencies, months of elapsed time. Tracking it as one case is where the 80% processing-time reduction would come from. |
| **P-12** | Family and community land registration with attestation of family consent | E | Design principles | 'Omonile' fraud is named as a target of the platform. Row 101 covers descendant/charity community land in the source jurisdiction's sense, not Nigerian family land held under customary tenure. |
| **P-13** | Excision and gazette verification | H | Anti-fraud principle | Whether land has been excised from state acquisition, and gazetted, is the first question any Nigerian buyer asks. Nothing answers it. |
| **P-14** | Stamp duty assessment and remittance | E, C | Business goal 7 (NRS) | Named as a target integration. Currently no service touches tax at all. |

---

## Tier 3 — Anti-Fraud and Consumer Protection

Fraud prevention is the PRD's first-stated problem and its tenth KPI, but the catalogue serves it almost entirely through passive lookups.

| ID | Proposed service | Group | Basis | Note |
| :---- | :---- | :---: | :---- | :---- |
| **P-15** | Title watch / dealing alert subscription | E, F | Diaspora + anti-fraud principles | Notify the registered owner whenever any filing touches their property. Cheap to build, and the strongest single deterrent to the double-sale and forged-transfer patterns the PRD describes. Particularly valuable for absent and diaspora owners. |
| **P-16** | Caveat lodgement and removal (title freeze) | E, F, G | Anti-fraud principle | A standard land-registry instrument: block dealings on a disputed or stolen title pending resolution. Entirely absent. |
| **P-17** | Duplicate-transaction conflict flag and resolution | A, E | KPI 10 | KPI 10 measures "duplicate title attempts detected and blocked". No service in the catalogue detects, records or resolves one — the metric has no mechanism behind it. |
| **P-18** | Lost or damaged title certificate replacement | E | — | Routine registry service with a publication/objection period. Not in the catalogue. |
| **P-19** | Report an unlicensed practitioner or fake project (anonymous) | H | FR-11, PRD §2.1 | Whistleblower intake, no account required. Feeds the enforcement queue in P-30 to P-32. |
| **P-20** | Off-plan escrow transparency view for purchasers | F | Escrow-first principle | Escrow exists to protect the off-plan buyer, but only the developer, trustee and regulator can see the account. Giving purchasers a read-only view of balance and milestone releases converts a compliance mechanism into a consumer-confidence one. |
| **P-21** | Advertisement and listing verification by permit number | H | Row 60 | Row 60 issues advertising permits, including for SMS and billboard ads. Nothing lets a buyer check one against a listing they have seen. |

---

## Tier 4 — Referenced In The Source, Never Catalogued As A Service

These are capabilities the source material assumes exist because its own service steps depend on them.

| ID | Proposed service | Group | Referenced at | Note |
| :---- | :---- | :---: | :---- | :---- |
| **P-22** | Wallet account — top-up, balance, statement, refund-to-wallet | All | Row 86 | The purchaser workflow instructs the buyer to "pay via Wallet Account". No service anywhere defines the wallet, how it is funded, or what happens to a balance. The institutional settlement account (Group C, question B1) is the same primitive with a different account type. |
| **P-23** | Digital safe / document vault | All | Row 87 | "All uploaded via digital safe." Referenced once, defined nowhere, and implicitly relied on by every service that reuses previously submitted documents. |
| **P-24** | Power of Attorney registration and revocation | E | Row 97, Registration Flow 2 | Row 97 covers PoA *cancellation* notarisation only. Flow 2 requires a notarised PoA before a diaspora investor's representative gains transactional rights — with no service to lodge one. The catalogue can cancel a PoA it has no way to create. |
| **P-25** | Manage delegated staff and permission scopes | B, C, D | Registration flows §4 | Companies are given the duty to "add or revoke delegated staff" post-registration. In scope by our own scope rule, and unwritten. Also the mechanism that carries maker-checker certification — see Group C question A1. |
| **P-26** | Appointment booking for Trustee Centre and Land Department visits | E, F | Channel analysis | A large share of services are walk-in only. In a system whose SLAs are measured in minutes, the queue is the real service time. |
| **P-27** | NDPA data-subject request (access, correction, erasure, consent withdrawal) | All | NFR-04 | NDPA 2023 compliance is a stated constraint and NDPC is a named stakeholder. Data-subject rights are a statutory obligation with no service behind them. |
| **P-28** | Multi-currency statement and FX view | F | Registration Flow 2 | Diaspora accounts are activated "with multi-currency tracking enabled". Nothing in the catalogue tracks anything in multiple currencies. |
| **P-29** | Service satisfaction survey and complaint about RERAN service quality | All | KPI 7 | KPI 7 targets NPS ≥ +30 from post-transaction surveys. No service collects one. |

---

## Tier 5 — Group A Internal Services

The roadmap already records that Group A has no services. These are the specific ones whose absence is most visible from the external side.

| ID | Proposed service | Basis | Note |
| :---- | :---- | :---- | :---- |
| **P-30** | Site inspection scheduling and geo-tagged inspection report | User group structure | The Inspection & Enforcement Officer has a named sub-system and a geo-tagged inspection mandate, and zero services. |
| **P-31** | Stop-work notice, violation notice and penalty assessment | PRD Module 4 | "Enforcement action recording (suspensions, license revocations, referrals to prosecution)" is specified in the PRD and exists nowhere in the catalogue. |
| **P-32** | Enforcement register and sanctions publication | FR-08, Module 3 | Licence status must be publicly visible in real time. Enforcement outcomes are what change it. |
| **P-33** | Fee schedule configuration, reconciliation and remittance | FR-16, Revenue & Finance Officer | The fee engine is configured by someone. No service says by whom or how. |
| **P-34** | State Lands Bureau record sync and jurisdictional conflict resolution | Design principles | Pipeline stage 6 ("Record & Sync") assigns this to the State Liaison Coordinator. It is the only pipeline stage with no service behind it. |

---

## Services That May Need Retiring Or Renaming

The reverse of this analysis. Not proposed additions — proposed subtractions, and lower confidence than anything above.

| Sourced service | Concern | Proposed disposition |
| :---- | :---- | :---- |
| Rows 3, 93–95 — usufruct registration, amendment, termination | Usufruct is a civil-law instrument. Nigeria's nearest equivalents are the statutory and customary rights of occupancy under the Land Use Act, which behave differently. | **Rename, do not retire.** The underlying need — registering a right to use land short of ownership — is real in Nigeria. Map to right of occupancy and re-derive the workflow. |
| Row 126 — Verification of Taqeemi certificate | Taqeemi is a named valuation scheme in the source jurisdiction. | **Rename** to ESVARBON-registered valuation verification, which registration Flow 6 already treats as the accreditation authority for valuers. |
| Row 114 — Names of ancient and modern regions | A locality-naming lookup specific to the source jurisdiction's history. | **Retire.** No Nigerian analogue. If a locality gazetteer is wanted, it is a different service against state and LGA boundaries. |
| Rows 2, 89–92 — rent-to-own / lease-to-own | Exists in Nigeria but is not a registered instrument in the same way. | **Reclassify** from title registration to contract registration, pending legal opinion. Do not build against a title-transfer model. |
| "Land Department" as channel on most rows | Nigeria has no federal Land Department; land vests in State Governors. | **Remap** every channel reference to RERAN, the State Lands Bureau, or a Trustee Centre. This is a find-and-replace across the whole catalogue and should be done once, deliberately. |

**Caveat that applies to this whole section:** these are documentation judgements, not legal opinions. The PRD's own risk table commits to "legal advisory engagement in Phase 1". This table is what that engagement should be handed on day one.

---

## Proposed Answers To The Open Questions

Rather than hold this document pending client input, each question carries the position we will work to unless told otherwise.

### 1. Is the 145-service catalogue fixed contractual scope, or a starting point?

**A floor, not a ceiling — and Tier 1 is not a scope increase.**

The distinction matters commercially. The catalogue is the only artefact carrying SLAs and channels, so it is what delivery will be measured against; all 145 get built. But Tier 1 items are already contracted *through the PRD*, which carries its own numbered requirements and a sign-off page. FR-11 is as binding as any row in the workbook. Those eight services are not new asks — they are places where the catalogue undercounts an obligation the PRD already creates.

Tiers 2 to 5 are genuine additions and should be handled as costed change requests, with P-09 raised first because it has legal consequences rather than merely functional ones.

**Recommended framing to the client:** "the catalogue and the PRD disagree about scope; here is where, and here is which we think governs."

### 2. Governor's Consent — track, mediate, or ignore?

**Track in v1. Mediate in v2. Ignoring is not available.**

Ignoring fails on its own terms: an unconsented assignment is void under s.22 of the Land Use Act, so a platform that issues a registration certificate over one is issuing a worthless instrument, and doing so under a government seal. That is a liability, not a gap.

Full mediation — lodging the consent application, collecting the fee, tracking it through the Governor's office — requires exactly the state-level bilateral agreements the PRD explicitly places out of scope for v1.0.

So v1 tracks: consent status, reference number and date become mandatory fields on every transfer, mortgage and sublease service; issuance is blocked without them; the field is verified against the State Lands Bureau wherever the P-34 sync layer reaches. That is buildable now, creates the data needed for v2, and closes the liability.

### 3. Do complaints sit inside the tribunal services, or on a separate surface?

**Separate intake, shared case engine.**

They are different in kind. A tribunal case is adjudicative — RERAN judges between two private parties and issues a judgment. A PRD complaint is administrative — a citizen reports a licensee, RERAN investigates as regulator and may sanction. Different burden of proof, different outcome, different SLA: KPI 4 gives complaints 30 calendar days, while the tribunal rows run 7 to 13 business days per stage.

But both need parties, evidence, hearings, SLA timers, escalation and a determination record. Build one case-management engine with two case types, rather than two systems or one blurred one.

### 4. Which source-jurisdiction services should be retired?

**Answered in the table above** — one retirement, two renames, one reclassification, and one catalogue-wide channel remap. Every disposition is recorded there with its reasoning.

The part we cannot supply is legal sign-off. Recommend the Phase 1 legal advisor the PRD already commits to is engaged against that table specifically, as their first task rather than a general review.

### 5. Is USSD in launch scope?

**Yes, but as three services, not a porting exercise.**

FR-15 makes USSD payment a Must Have, and the risk table names USSD/SMS as the mitigation for the connectivity limits that threaten adoption in secondary markets. It cannot be deferred without dropping a Must Have.

But porting document-heavy services to a menu protocol is neither possible nor useful. Propose a deliberately narrow USSD surface: verify a title or licence by reference number, check application status, and retrieve a payment reference for offline settlement. Everything else stays on web and app.

That satisfies FR-15, serves the users the channel exists for, and costs a fraction of a full port.

### 6. Who owns the wallet and the document vault?

**Neither is a service, and neither belongs to a user group. They are platform capabilities, and the project has nowhere to put them.**

This is the more useful finding. Four separate observations converge on the same missing structure:

* the wallet (P-22) and document vault (P-23) are used by every group;
* the four application-management features are documented for individual users, proposed for Group C, and needed by B and D;
* the status vocabulary should be defined once platform-wide (Group C question D1);
* escrow spans four groups and the roadmap already flags it as needing one shared reference rather than four descriptions.

The project standards define a module as a user group. Cross-cutting capability has no home, so it keeps getting re-proposed inside whichever module hits it first.

**Recommendation:** add a `RERAN/platform/` stage alongside `modules/`, holding capabilities that no single user group owns — wallet and settlement accounts, document vault, application-management features, status vocabulary, escrow reference, notifications, payments. This is a change to `project-standards.md` and should be made deliberately rather than absorbed.

---

## What Still Needs The Client

After the answers above, three things genuinely cannot be resolved from the documents:

1. **The published fee schedule.** Only RERA holds it. Does not block build — fees are configuration under FR-16.
2. **Legal sign-off on the retire/rename table.** A documentation judgement is not a legal opinion.
3. **Commercial acceptance of Tiers 2–5.** We can recommend; only the client can fund.
