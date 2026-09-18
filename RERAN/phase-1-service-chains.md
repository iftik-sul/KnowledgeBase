---
project: RERAN
type: cross-module-map
status: draft
contains_proposals: true
updated: 2026-09-18
derived_from:
  - "RERAN/modules/real-estate-developer/service-flows/ (#1, #6, #13, #16, #24)"
  - "RERAN/modules/financial-trust-institutions/service-flows/ (#3, #12, #13, #15, #17)"
  - "RERAN/modules/regulatory-authority/touchpoint-register.md"
  - "RERAN/modules/regulatory-authority/ui/screens/"
tags:
  - phase-1
  - cross-module
  - regulatory-authority
---

# Phase 1 — Service Chains

The end-to-end path of each of the ten Phase 1 services: who files it, every gate it
passes before the regulator sees it, which Regulatory Authority screen handles it, and
what comes back to the applicant.

This is a **cross-module map** — it spans RED, FTI and the Regulatory Authority, so it
sits at the project root rather than inside any one module. Each module's own
service-flow remains the source for its half; this file joins them.

## The ten

**RED:** #1 Register Initial Sale · #6 Register Mortgage-Linked Sale · #13 Registration
of Real Estate Project · #16 Changing the Name of a Project · #24 Registration/Amendment
of Project Details

**FTI:** #3 Mortgage Registration · #12 Register Real Estate Fund Company · #13 Sale
Procedure (Heirs) · #15 Updating Title Deed Information · #17 Issuance of Title Deed

**All ten land on the same officer and the same screens.** Every one routes to the
**Compliance & Escrow Auditor** in the **Transaction Audit Queue** — none to Licensing,
none to Dispute, none an escrow-variant item. So the Regulatory Authority back half of
all ten is:

> **[RA] Compliance & Escrow Auditor**
> → [Work Queue](modules/regulatory-authority/ui/screens/work-queue.md) (transaction view)
> → [Application Review](modules/regulatory-authority/ui/screens/application-review.md)
> → decision modal `M-DEC-01`…`M-DEC-04`

No Regulatory Authority screen outside those two is needed for Phase 1.

---

## What differs between them is the **pre-gate**

The regulator's step is identical across all ten. What varies is what happens *before*
the item reaches the queue. Five distinct shapes:

| Pre-gate | Services | What it is |
| :-- | :-- | :-- |
| **None** | RED #1, RED #16 | Developer submits; straight to the queue |
| **Automatic system check** | RED #6 | Live validation against FTI records; fails → instant auto-return, no human |
| **Internal certifier** | FTI #3 | Someone inside the institution certifies before the regulator sees it |
| **Trustee Centre operator** | FTI #12, #13, #15, #17 | Counter-based: operator enters and checks the transaction on the customer's behalf |
| **Survey Department** | RED #24 | A survey confirmation step — an independent actor, not part of any RERAN group (A2) |

---

## The chains

### RED #1 — Register Initial Sale
```
Developer (RED portal) → pay → submit
  → [RA] Compliance & Escrow Auditor → Work Queue → Application Review → decide
  → Approved: Provisional Registration e-Certificate
  → emailed to the purchaser
```
Fee **before** decision · SLA 6 business days · no pre-gate.

---

### RED #6 — Register Mortgage-Linked Sale  ← *the chained one*
```
Developer (RED portal) → pay → submit
  → [automatic] validate mortgage reference against FTI's records, live, same request
       ↳ not found / mismatched / not yet `Completed`
            → auto-returned to developer immediately, no officer involved
  → [RA] Compliance & Escrow Auditor → Work Queue → Application Review → decide
  → Approved: Mortgage Provisional Registration Certificate + Electronic Map
```
Fee **before** decision *and before validation* · SLA 6 business days.

**This is the one true chain in Phase 1.** The mortgage it validates against only reaches
`Completed` because the Compliance & Escrow Auditor approved **FTI #3**. So:

```
FTI #3 approved by the Auditor  →  mortgage = Completed  →  RED #6 can pass its check
```

Both ends are in the Phase 1 set, which makes this the path to test end-to-end first.

---

### RED #13 — Registration of Real Estate Project
```
RERA issues the developer's licence + self-registration username   (precondition)
  → Developer applies, attaches requirements
  → [RA] Compliance & Escrow Auditor → Work Queue → Application Review → audit: accept or reject
  → If accepted: developer uploads units via an approved survey company
  → Developer submits to the Registrar to open the project account
  → pay registration fee
  → Real Estate Project Approval Certificate
```
Fee **after** the decision — payment releases the output rather than gating review ·
SLA 3 business days.

> **One further touch sits outside the queue:** issuing the licence up front (Licensing
> & Registration Officer). Opening the project account is handled by "the Registrar" —
> an independent actor, not one of the Regulatory Authority's roles or part of any
> other group (A2). Neither step is the Transaction Audit decision.

---

### RED #16 — Changing the Name of a Project
```
Developer (RED portal) → open project → new name + reason → submit
  → [RA] Compliance & Escrow Auditor → Work Queue → Application Review → decide
  → Approved: Updated Real Estate Project Approval Certificate
```
**No fee** · SLA 30 minutes · the simplest chain in the set.

---

### RED #24 — Registration/Amendment of Project Details
```
Developer (RED portal) → enter updated details
  → pay application approval fee                      (payment 1 of 2)
  → [Survey Department] review and confirm data  (independent actor, A2)
  → submit
  → [RA] Compliance & Escrow Auditor → Work Queue → Application Review → decide
  → pay approval fee in real-estate records            (payment 2 of 2)
  → Project completed?  → Electronic Certificate of Title / Title Deed
    Project not completed? → Electronic Map
```
**Two payments**, one either side of the decision — the only service in the set that does
this · SLA 5 business days · conditional output.

---

### FTI #3 — Mortgage Registration  ← *feeds RED #6*
```
Borrower completes mortgage requirements with the bank
  → Institution user files it (select property, enter details, upload docs)
  → pay via the shared gateway
  → [Internal Certifier, inside the institution] review → certify, or return to filer
  → [RA] Compliance & Escrow Auditor → Work Queue → Application Review → decide
  → Approved: title-type certificate (Certificate of Title / Title Deed / Usufruct /
    Statement Certificate / Provisional Sale Registration Certificate — whichever matches
    the property's existing registration)
  → emailed to the customer
  → record reaches `Completed` → RED #6 can now validate against it
```
Fee **before** submission · SLA 20–25 minutes · **two gates**: certifier, then regulator.

> Also has an assisted counter path (Trustee Centre operator files on the institution's
> behalf) — marked `Proposed` in the source.

---

### FTI #12 — Register Real Estate Fund Company
```
Fund company rep visits the Trustee Centre → submits documents
  → pay at the counter → e-receipt          (moved ahead of review, client decision 2026-08-16)
  → [Trustee Centre Operator] enter and check the transaction
  → [RA] Compliance & Escrow Auditor → Work Queue → Application Review → decide
  → Approved: E-Ownership Certificate + Register of Privileges registration number
  → both delivered by email
```
Fee **before** decision · SLA 25–30 minutes · counter-originated.

---

### FTI #13 — Sale Procedure (Heirs)
```
Heirs / representative visit the Trustee Centre → submit documents
  → [Trustee Centre Operator] enter data → initial audit
  → heirs pay at the counter
  → [RA] Compliance & Escrow Auditor → Work Queue → Application Review → audit and decide
  → Approved:
      → [Trusts Department] transfer each heir's share to their bank account  (independent actor, A2)
      → Certificate of Title + Title Deed + Map + receipts, by email
```
Fee **before** decision · SLA 25–30 minutes · **the only service in the set with a
post-approval money movement.**

---

### FTI #15 — Updating Title Deed Information
```
Customer visits the Trustee Centre → submits documents
  → [Trustee Centre Operator] verify completeness → enter data
  → customer pays → receipt
  → [RA] Compliance & Escrow Auditor → Work Queue → Application Review → decide
  → Approved: updated Electronic Title Deed — same deed number, incremented version
  → link delivered by email
```
Fee **before** decision · SLA 25 minutes.

---

### FTI #17 — Issuance of Title Deed
```
Customer visits the Land Department → submits documents
  → [Operator] enter transaction data
  → customer pays
  → [RA] Compliance & Escrow Auditor → Work Queue → Application Review → decide
  → Approved: Electronic Title Deed Certificate, by email
```
Fee **before** decision · SLA 25 minutes · the cleanest counter-originated chain.

---

## The return path (all ten)

Every service shares the same not-approved routes, because they share the decision loop:

```
Application Review → Request Additional Information (M-DEC-02)  ─┐
                   → Return for Correction        (M-DEC-03)  ─┤→ back to applicant
                   → Reject                       (M-DEC-04)     → terminal

applicant responds → re-enters the Work Queue
   · routed back to the officer who queried it, where available
   · flagged as a Resubmission, original query shown
   · SLA clock RESETS — a fresh full window (Total elapsed keeps the real duration visible)
```

RED #6 has one extra return that no other service has: the **automatic** mortgage-validation
return, which happens before any officer and is not a decision.

---

## A2 — three independent actors, not part of any group

Two of these ten chains route through a label that isn't one of the Regulatory
Authority's eight roles: RED #24's pre-decision review ("Survey Department") and FTI
#13's post-approval share transfer ("Trusts Department"). RED #13's account-opening
step ("Registrar") is the same kind of case.

**Closed, not mapped to any role.** An earlier pass mapped all three onto existing RA
roles; that was wrong and was reverted. Checked directly against the client's AGIS
document: none of the three terms appears there either — AGIS has a Survey Unit and an
external Surveyor-General's office (neither is "Survey Department"), a "Deed registrar"
job title inside its Deeds Registry division (not a standalone Registrar role), and no
trust-related unit at all. **All three are independent actors that RERAN's eight-group
model never placed anywhere** — not RA, not Group G, not any other group. RED and FTI
keep the labels exactly as their own source describes them. See
`modules/regulatory-authority/open-questions.md` A2 for the full account.

---

## What this confirms for the Regulatory Authority build

- **Two screens cover all ten services.** Work Queue (transaction view) + Application
  Review. Nothing deferred is needed.
- **The SLA spread is real**: 25 minutes (FTI #15, #17) to 6 business days (RED #1, #6)
  within the same queue. This is exactly why the queue sorts by urgency, not age.
- **Payment timing varies and the queue must not assume it**: eight pay before the
  decision, RED #13 pays after, RED #24 pays twice.
- **FTI #3 → RED #6 is the integration to test first** — both ends are in scope and the
  dependency is live and synchronous.
