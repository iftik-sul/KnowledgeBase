---
project: RERAN
module: financial-trust-institutions
type: ui-build-tracking
status: current
updated: 2026-08-18
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/README.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens-unified/submit-application.md"
  - "RERAN/modules/financial-trust-institutions/service-flows/service-03-mortgage-registration.md"
  - "RERAN/modules/financial-trust-institutions/service-flows/service-12-register-real-estate-fund-company.md"
  - "RERAN/modules/financial-trust-institutions/service-flows/service-13-sale-procedure-heirs.md"
  - "RERAN/modules/financial-trust-institutions/service-flows/service-15-update-title-deed-information.md"
  - "RERAN/modules/financial-trust-institutions/service-flows/service-17-issue-title-deed.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - figma
  - index
---

# Figma Screen Register — Financial & Trust Institutions

**What this file is.** A build tracker for the Figma design file. It records which screens have been *specified as Figma prompts*, which have been *built*, and which have been *reviewed* — plus the design decisions and assumptions those screens carry.

**What this file is not.** It is not a UI specification. The specs live in [`screens/`](screens/) and [`screens-unified/`](screens-unified/), and remain the source of truth for behaviour. This file tracks the downstream Figma artefact only. Where the two diverge, the divergence is recorded here explicitly rather than silently resolved.

---

## Status legend

| Status | Meaning |
| :--- | :--- |
| `Specified` | A Figma AI prompt exists for this screen |
| `Built` | The screen exists in the Figma file |
| `Reviewed` | Built and checked by the project lead |
| `—` | Not yet started |

---

## Scope decision

Five of the module's eighteen services were selected for UI design, chosen for maximum design-pattern coverage rather than for business priority. The remaining thirteen are expected to reuse the components these five establish.

**Selected:** #3 Mortgage Registration · #12 Fund Company Registration · #13 Sale Procedure (Heirs) · #15 Updating Title Deed Information · #17 Issuance of Title Deed

**Excluded from selection by the project lead:** #1, #2, #7, #8, #9, #10, #11, #14

**Journey depth:** full end-to-end per service — service details through to output documents — rather than the wizard shell plus per-service detail steps. This produces deliberate repetition across services (see Repetition Risk below).

---

## Shell structure

Every screen uses the same three-part shell. Layer naming is fixed and must not vary:

```
[Screen Name]
├── FI-Sidebar        (component instance)
└── MainContent
    ├── TopBar        (component instance)
    └── Workspace     (scrolling content)
```

Frame width 1440px. Sidebar fixed, workspace scrolls. `FI-Sidebar` carries 12 nav items plus Sign Out, matching the module's 12 shared platform features. The active nav item is set per screen and is recorded in each prompt.

---

## Screen register

### Pre-existing screens

Screens that existed in the Figma file before this design pass. This list is incomplete — global numbering runs at least to #5, so screens #2–#4 exist but have not been catalogued here.

| # | Screen | Status | Notes |
| :--- | :--- | :--- | :--- |
| 1 | Dashboard | Built | Establishes metric card, quick actions strip, data table, summary panel, activity feed |
| 5 | Application Review | Built | Establishes the 6-step tracker, metadata strip, section cards with inline Edit, document table, payment summary, validation checklist, declaration |
| 2–4 | *(uncatalogued)* | Built | To be added to this register |

### S3 — Mortgage Registration (11 screens)

| ID | Screen | Status | Notes |
| :--- | :--- | :--- | :--- |
| S3 – 01 | Service Details | Specified | |
| S3 – 02 | Step 1 — Application Info | Specified | Institution + borrower |
| S3 – 03 | Step 2 — Service Info | Specified | Property lookup + mortgage information |
| S3 – 04 | Step 3 — Documents | Specified | |
| S3 – 05 | Step 5 — Payment | Specified | Upfront, before certification |
| S3 – 06 | Payment Confirmation | Specified | |
| S3 – 07 | Step 6 — Review & Submit | Specified | Submits to internal certification, not to RERA |
| S3 – 08 | Submitted for Internal Certification | Specified | **Unique to this service** |
| S3 – 09 | Internal Certification — Review Transaction | Specified | **Unique to this service.** Detail screen reached from the existing Internal Certification Queue |
| S3 – 10 | Application Details | Specified | Timeline includes the certification stage |
| S3 – 11 | Registration Confirmation | Specified | |

### S12 — Registration of Real Estate Fund Companies (10 screens)

| ID | Screen | Status | Notes |
| :--- | :--- | :--- | :--- |
| S12 – 01 | Service Details | Specified | |
| S12 – 02 | Step 1 — Application Info | Specified | Institution + fund company + authorized representative |
| S12 – 03 | Step 2 — Service Info | Specified | Registration details + conditional linked asset |
| S12 – 04 | Step 3 — Documents | Specified | **Document-dominant.** Extended table with File and Uploaded columns |
| S12 – 05 | Step 5 — Payment | Specified | |
| S12 – 06 | Payment Successful | Specified | |
| S12 – 07 | Step 6 — Review & Submit | Specified | |
| S12 – 08 | Application Submitted | Specified | |
| S12 – 09 | Application Details | Specified | |
| S12 – 10 | Registration Confirmation | Specified | Merges the source's separate Ownership Certificate and Registration Confirmation screens |

### S13 — Sale Procedure (Heirs) (11 screens)

| ID | Screen | Status | Notes |
| :--- | :--- | :--- | :--- |
| S13 – 01 | Service Details | Specified | |
| S13 – 02 | Step 1 — Application Info | Specified | **Defines the repeatable heir block.** Institution + deceased owner + heirs |
| S13 – 03 | Step 2 — Service Info | Specified | Property lookup + sale information + distribution preview |
| S13 – 04 | Step 3 — Documents | Specified | Split into estate-level and per-heir tables |
| S13 – 05 | Step 5 — Payment | Specified | |
| S13 – 06 | Payment Successful | Specified | |
| S13 – 07 | Step 6 — Review & Submit | Specified | Heirs rendered as a table, not label/value pairs |
| S13 – 08 | Application Submitted | Specified | |
| S13 – 09 | Application Details | Specified | Timeline includes the distribution stage |
| S13 – 10 | Distribution Confirmation | Specified | **Unique to this service.** Trusts Department transfers |
| S13 – 11 | Registration Confirmation | Specified | |

### S15 — Updating Title Deed Information (10 screens)

| ID | Screen | Status | Notes |
| :--- | :--- | :--- | :--- |
| S15 – 01 | Service Details | Specified | Carries the "what can be updated" field list |
| S15 – 02 | Step 1 — Application Info | Specified | Institution + requestor |
| S15 – 03 | Step 2 — Service Info | Specified | **Defines the conditional field selector.** Property lookup + field checklist + changes-to-apply blocks |
| S15 – 04 | Step 3 — Documents | Specified | |
| S15 – 05 | Step 5 — Payment | Specified | |
| S15 – 06 | Payment Successful | Specified | |
| S15 – 07 | Step 6 — Review & Submit | Specified | Changes rendered as a Field / Current / New table |
| S15 – 08 | Application Submitted | Specified | |
| S15 – 09 | Application Details | Specified | |
| S15 – 10 | Updated Title Deed | Specified | **Unique to this service.** Same deed number, incremented version |

### S17 — Issuance of Title Deed (10 screens)

| ID | Screen | Status | Notes |
| :--- | :--- | :--- | :--- |
| S17 – 01 | Service Details | Specified | |
| S17 – 02 | Step 1 — Application Info | Specified | Institution + applicant |
| S17 – 03 | Step 2 — Service Info | Specified | Property information + basis for issuance |
| S17 – 04 | Step 3 — Documents | Specified | |
| S17 – 05 | Step 5 — Payment | Specified | |
| S17 – 06 | Payment Successful | Specified | |
| S17 – 07 | Step 6 — Review & Submit | Specified | |
| S17 – 08 | Application Submitted | Specified | |
| S17 – 09 | Application Details | Specified | |
| S17 – 10 | Title Deed Issued | Specified | **Unique to this service.** Output certificate as a document record |

**Total: 52 screens specified across five services.**

---

## New components introduced

Three components exist in no pre-existing screen and are defined by exactly one screen each. If that screen is skipped, the component never gets built.

| Component | Defined by | Used by |
| :--- | :--- | :--- |
| Repeatable field group | `S13 – 02` (heir block) | #13; also needed by #16 Split Ownership if it returns to scope |
| Conditional field selector | `S15 – 03` (field checklist → current/new value pairs) | #15 only — the module's sole Pattern C service |
| Extended document table | `S12 – 04` (adds File and Uploaded columns) | #12; candidate for a table variant in the library |

**Build order recommendation:** `S13 – 02`, `S15 – 03` and `S12 – 04` first, since each requires iteration before the screens depending on them can be finalised.

---

## Design decisions applied across all five services

| Decision | Rationale |
| :--- | :--- |
| **Six-step tracker, identical labels** — Application Info · Service Info · Documents · Validation · Payment · Review & Submit | Follows the built Application Review screen rather than the spec doc, which uses different labels. Consistency across services outweighs matching the doc. |
| **Validation has no standalone screen** | Auto-passes between Documents and Payment; surfaces as the Validation Summary card on Review & Submit. Keeps the tracker at six steps. |
| **Select Property folded into Step 2** | Several service files list it as a separate screen. A seventh tracker step on some services and six on others would be a visible inconsistency. |
| **Payment is a wizard step on every service** | Every one of the five pays before RERA's decision. The "services #12–#18 skip payment" rule in the unified spec does not survive contact with these services' own sequences. |
| **Institution-portal channel assumed throughout** | See Open Assumptions below. |
| **No decorative certificate artwork** | Output documents are rendered as document records with actions, never as drawn certificates, seals, or watermarks. |
| **Simplicity constraint** | Stacked white cards, one blue primary action per screen, plain label/value grids. No illustrations, gradients, charts, or brand logos. |

---

## Open assumptions requiring sign-off

These are documented positions, not sourced facts. Each is flagged in the relevant prompt pack.

| # | Assumption | Affects | Source status |
| :--- | :--- | :--- | :--- |
| 1 | **Bank-originated channel exists** for #12, #13, #15, #17 | All four services' entire journeys | Unconfirmed by source. Rows 38, 40–44 describe only Trustee Centre walk-in entry. Portal shell chosen because a Group G terminal UI doesn't belong in this file. |
| 2 | **Updatable field list for #15** — 10 fields across owner and property particulars | `S15 – 01`, `S15 – 03` | Open question 1 in `service-15`. Proposed, bounded by the service's own no-transfer/no-encumbrance rule. **Recommended for client sign-off as a proposal.** |
| 3 | **Updated deed keeps its number, gains a version** | `S15 – 10` | Open question 2 in `service-15`. |
| 4 | **Filer certifies their own transaction** in the #3 sample | `S3 – 09` | Permitted and deliberate — demonstrates the unified-access model rather than implying a maker-checker gate that no longer exists. |
| 5 | **Fee amounts are placeholders** across all five | Every Payment and Review screen | Open question B5 module-wide. Shape follows the built sample: service fee + processing levy + 7.5% VAT. |
| 6 | **#3 output shown as Certificate of Title** | `S3 – 11` | Open question 2 in `service-03` — source lists five possible outputs without selection criteria. |
| 7 | **#12 merges two output screens into one** | `S12 – 10` | Both documents issue from the same event, unlike #13 where distribution and registration are distinct events. |

---

## Known repository defect

`service-03-mortgage-registration.md` §9 opens with the corrected upfront payment model, then its second paragraph still states that submission is free and the fee settles only after RERA approval. This contradicts §5, §12, §13, §20 and Business Rule 4. The 2026-08-14 payment correction landed everywhere except that paragraph — a drift failure.

The `S3` prompt pack follows the upfront model. **The doc itself is not yet fixed.**

---

## Repetition risk

Nine screens repeat across all five services with only content differences: Service Details, the four wizard steps, Payment Successful, Review & Submit, Application Submitted, Application Details. That is 45 of the 52 screens.

This is the direct and accepted consequence of specifying full end-to-end journeys per service. The exposure is maintenance: a later change to a shared pattern — the tracker, the metadata strip, the document table — must be propagated to five copies rather than one. Worth converting the repeated screens to component instances or variants in Figma once the first service is built and settled, rather than leaving five independent copies.

---

## Not yet scoped

The remaining thirteen services have no Figma screens specified: #1, #2, #4, #5, #6, #7, #8, #9, #10, #11, #14, #16, #18.

Of these, #16 Split Ownership is the one that would need genuinely new UI machinery — it uses a repeatable group like #13's, but with a quantity field governing the required entry count. Everything else should be reachable by recombining the components these five establish.
