---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/service-flows/"
  - "RERAN/modules/financial-trust-institutions/payments.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - service-request
---

# Screen: Service Request

**Roles:** Mortgage Officer (`file`) · Institution Relationship Manager (`file`, for #1, #2, #18)

The configurable form behind all eighteen Group C services. One shell, not eighteen form specs — what varies by service is documented here as a matrix, not as eighteen repeated sections.

## Purpose

Let a `file`-scoped user select a service, enter its particulars, attach its documents and submit for internal certification (where configured) or directly to RERAN. Unlike the individual-user module, **this screen never collects payment** — per answer B1, Group C fees are deducted from the institution's settlement account after RERAN approval, not at submission. There is no checkout step in this form.

## Layout

```
Top Bar
↓
Institution Context Header
↓
Service Selection
↓
Applicant & Representation
↓
Transaction Details (service-specific)
↓
Supporting Documents (service-specific)
↓
Review & Submit
```

## Sections

### Section 1 — Service Selection

A catalogue of the eighteen services, filtered to what the signed-in user's `file` scope and institution type permit. Selecting a service configures every section below it.

* Institutions with an expired approval (answer B8) see the full catalogue but cannot proceed past Review & Submit — see Validation.
* Group B escrow requests are **not** in this catalogue. They arrive from the developer module and are worked in [escrow-request-queue.md](escrow-request-queue.md), never created here.

### Section 2 — Applicant & Representation

* Institution and filing officer, pre-filled from the signed-in session.
* Counterparty (borrower, lessee, heir, purchasing party, or the institution itself for #1/#2/#18) — fields vary by service, see the matrix below.
* **Assisted Mode** block, shown only when the request originates from [assisted-service-terminal.md](assisted-service-terminal.md): operator identity, represented customer, and a consent/representation record. This screen and the terminal are the same underlying form — the terminal is not a separate build, per answer C2.

### Section 3 — Transaction Details

Field groups by service. This replaces a per-service form spec:

| Service group | Field groups | Instrument-specific fields |
| :---- | :---- | :---- |
| #1–#2 Institutional approval | Institution Information, Application Information | New approval vs. renewal (#1); cancellation reason (#2) |
| #3–#7 Mortgage lifecycle | Institution/Officer, Borrower, Property, Mortgage Information | Loan amount, term, rate (#3); amendment details (#4); new mortgagee (#5); release grounds (#6); same as #3 (#7) |
| #8–#11 Finance lease lifecycle | Institution/Officer, Lessee, Property, Lease Information | Lease term, payment schedule (#8); amendment/transfer/release details (#9–#11) |
| #12 Fund company registration | Fund Company Information, Registration Information | Nature of privilege being registered |
| #13–#17 Title & ownership | Varies by service — heir/company/property reference | See each service's Required Information in `service-flows/` |
| #18 Contract cancellation | Institution Information, Contract Information | Contract reference, cancellation reason |

Field-level detail for each service is authoritative in its own service-flow document (`service-flows/service-NN-*.md`, Sections 4–6), not restated here. This table exists so the form's *shape* is visible without opening eighteen files.

### Section 4 — Supporting Documents

Document Uploader, configured per service from the Required Documents list in that service's own service-flow document. Every one of the eighteen document lists is itself marked **Proposed** at source — the workbook says "submit docs" without enumerating them — so this screen's document slots inherit that same proposed status per service.

Documents already in the institution repository can be attached by reference — see [components.md](../components.md#document-reference-picker) and [validation-rules.md](../validation-rules.md#documents).

### Section 5 — Review & Submit

* Validation summary: required fields and documents outstanding.
* **Certification requirement indicator** — states whether this submission will route through internal certification before RERAN, per the service's own routing (see the Service × Form Matrix in [README.md](../README.md#service--form-matrix)). Where certification is not sourced for a service (institutional approval, #1/#2; several title & ownership services), the indicator says so rather than defaulting to "no."
* **No payment step.** The submit action lodges the request; settlement happens later, from [settlement-account.md](settlement-account.md), only after RERAN approval.
* Submit button is disabled, not hidden, where institutional approval has expired — see Validation.

## Empty State

Applies to the Service Selection catalogue when a filter matches nothing.

**Message**

> No services match this filter. Clear filters to see the full catalogue.

**Primary Button:** Clear Filters

## Reused Components

See [components.md](../components.md). Uses Institution Operations Sidebar, Top Bar, Institution Context Header, Document Uploader, Document Reference Picker, Status Badge, Progress Tracker (post-submission), Buttons.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. Submission is blocked while institutional approval is expired (answer B8); the form remains fillable and saveable as draft. See [validation-rules.md](../validation-rules.md#institutional-standing).
2. Submission is **not** blocked by settlement account balance. Per answer B1/B4, balance only matters at settlement, after approval — this form does not check it.
3. A title reference must resolve to a registered property; an unresolved reference is a hard error, not a warning (see [validation-rules.md](../validation-rules.md#property-and-party-references)).
4. Where a service acts on an existing instrument (amendment, transfer, release), the instrument must be active — acting on a released mortgage or lease is blocked.
5. Required documents must all be present before Submit is enabled; optional documents may be added later, up to the internal certification gate.

## Role Variations

### Mortgage Officer

Sees the full catalogue for the mortgage lifecycle (#3–#7), finance lease lifecycle (#8–#11), fund company registration (#12), and title & ownership services where bank-originated (#13–#17) — per answer A4's conditional, this last group is not sourced as bank-originated for any of rows 38, 40–44, so the catalogue shows them as available but flags that assisted-mode origination is the confirmed path; see each service's Open Questions.

### Institution Relationship Manager

Sees only #1 (approval/renewal), #2 (cancellation) and #18 (contract cancellation) — the three services sourced or re-derived to this role under answer A4.

## User Flow

```
Dashboard / Applications
↓
Service Request
├─ Select Service → Transaction Details → Supporting Documents → Review & Submit
├─ Submit (certification configured) → Internal Certification Queue
├─ Submit (no certification) → Application Details (Submitted)
└─ Save Draft → Applications (Draft)
```

## Notes

* **Fee amounts are not shown anywhere on this form.** Answer B5 is client data; the fee schedule engine (FR-16) computes the amount at RERAN's audit stage, not here.
* **The Transaction Details matrix is a navigation aid, not a new source.** Every field group it names is already documented, service by service, in `service-flows/`; this screen restates none of it beyond the grouping.
* Whether internal certification is sourced or merely configurable differs by service — see the Service × Form Matrix in [README.md](../README.md#service--form-matrix), which is the authoritative per-service answer, not this file.
* Assisted-mode submissions carry the same validation as direct submissions; the operator is not a lighter-weight path.
