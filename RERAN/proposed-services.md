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
| **P-22** | Wallet account — top-up, balance, statement, refund-to-wallet | All | Row 86 | The purchaser workflow instructs the buyer to "pay via Wallet Account". No service anywhere defines the wallet, how it is funded, or what happens to a balance. |
| **P-23** | Digital safe / document vault | All | Row 87 | "All uploaded via digital safe." Referenced once, defined nowhere, and implicitly relied on by every service that reuses previously submitted documents. |
| **P-24** | Power of Attorney registration and revocation | E | Row 97, Registration Flow 2 | Row 97 covers PoA *cancellation* notarisation only. Flow 2 requires a notarised PoA before a diaspora investor's representative gains transactional rights — with no service to lodge one. The catalogue can cancel a PoA it has no way to create. |
| **P-25** | Manage delegated staff and permission scopes | B, C, D | Registration flows §4 | Companies are given the duty to "add or revoke delegated staff" post-registration. In scope by our own scope rule, and unwritten. |
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

| Sourced service | Concern |
| :---- | :---- |
| Rows 3, 93–95 — usufruct registration, amendment, termination | Usufruct is a civil-law instrument. Nigeria's nearest equivalents are the statutory and customary rights of occupancy under the Land Use Act, which behave differently. Either these map onto rights of occupancy and should be renamed, or they do not apply. |
| Row 126 — Verification of Taqeemi certificate | Taqeemi is a named valuation scheme in the source jurisdiction. The Nigerian equivalent would be ESVARBON-registered valuation. |
| Row 114 — Names of ancient and modern regions | A locality-naming lookup specific to the source jurisdiction's history. |
| Rows 2, 89–92 — rent-to-own / lease-to-own | Exists in Nigeria but is not a registered instrument in the same way. Needs legal confirmation before it is built as a registration service. |
| "Land Department" as channel on most rows | Nigeria has no federal Land Department; land vests in State Governors. Every channel reference needs remapping to RERAN, the State Lands Bureau, or a Trustee Centre. |

---

## Questions For The Client

1. Is the 145-service catalogue a fixed contractual scope, or a starting point we are expected to adapt to Nigerian law?
2. Governor's Consent (P-09): does the platform track it, mediate it, or ignore it? The answer changes every transfer service in Groups C and E.
3. Does the complaints capability the PRD specifies (P-01 to P-03) sit inside the existing tribunal services, or is it a separate consumer-protection surface?
4. Which services from the source jurisdiction have no Nigerian legal basis and should be retired before we document them?
5. Is USSD in launch scope? FR-15 says yes; the service catalogue says the channel does not exist.
6. Who owns the wallet (P-22) and the document vault (P-23) — are they platform features rather than services, and if so, whose module documents them?
