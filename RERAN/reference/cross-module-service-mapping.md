---
project: RERAN
type: reference
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/service-flows/ (escrow services #8, #9, #12, #13, #20, #21)"
  - "RERAN/modules/financial-trust-institutions/service-flows/feature-04-escrow-request-queue.md"
  - "RERAN/modules/individual-user/service-flows/service-08-register-sale-of-mortgaged-property.md"
  - "RERAN/modules/financial-trust-institutions/service-flows/service-03-mortgage-registration.md"
  - "RERAN/modules/financial-trust-institutions/service-flows/service-06-mortgage-release.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-06-register-mortgage-linked-sale.md"
tags:
  - cross-module
  - service-mapping
---

# Cross-Module Service Mapping

Which service in one module depends on, feeds, or waits on a service in another — audited and confirmed tonight, not a fresh full sweep of every service in all three modules. **Three threads are confirmed and fully documented on both sides. A fourth is spotted but not yet cross-referenced anywhere** — see the note at the end.

## Thread 1 — Escrow: Real Estate Developer → Financial & Trust Institutions

Six RE-dev services all route through the same FTI gate (Escrow Request Queue → Trust Accounts), using one canonical status vocabulary confirmed and corrected across both modules: `Draft → Submitted → Trustee Review → RERA Escrow Audit → Approved → [terminal state]`.

| RE-dev service | Feature | → | FTI feature | Terminal state |
| :---- | :---- | :---: | :---- | :---- |
| #8 Escrow Account Activation | Escrow Management (#4) | → | Escrow Request Queue (#4) → Trust Accounts (#5) | Active |
| #9 Escrow Account Transfer | Escrow Management (#4) | → | Escrow Request Queue (#4) → Trust Accounts (#5) | Transferred |
| #20 Depositing a Mortgage into Escrow | Escrow Management (#4) | → | Escrow Request Queue (#4) → Trust Accounts (#5) | Deposited |
| #21 Bank Guarantee Cancellation | Escrow Management (#4) | → | Escrow Request Queue (#4) → Trust Accounts (#5) | Cancelled |
| #12 Receive Payment from Escrow Account | Fund Release Request (#5) | → | Escrow Request Queue (#4) → Trust Accounts (#5) | Released |
| #10 Project Profit Withdrawal | Profit Withdrawal Request (#13) | → | Escrow Request Queue (#4) → Trust Accounts (#5) | Released |

**Direction:** developer files → institution assesses (`Trustee Review`) → RERA audits (`RERA Escrow Audit`, performed by the Compliance & Escrow Auditor — same role FTI's mortgage services use, confirmed against the master table) → result flows back to the developer's own record.

**Status:** Fully reconciled both directions. Terminology (`RERA Escrow Audit` / `Escrow Account Department` = FTI's `Compliance & Escrow Auditor`) confirmed identical via the master source table's Regulator/Approver column.

## Thread 2 — Mortgage lifecycle: Financial & Trust Institutions → Individual User

Not a shared queue like Thread 1 — a **document handoff**, one direction, two hops.

```
FTI Service #3 (Mortgage Registration)
        ↓ registers the mortgage
   [property now carries an active mortgage]
        ↓ (later, at sale time)
Individual User Service #8 (Register Sale of Mortgaged Property)
        ↓ requires the seller to obtain...
FTI Service #6 (Mortgage Release)
        ↓ produces...
   Mortgage Release Letter
        ↓ submitted back into...
Individual User Service #8
        ↓ only then can complete
   Ownership Transfer
```

**Direction:** FTI #3 creates the mortgage → time passes → Individual User #8 (a sale) triggers the need for release → FTI #6 discharges the mortgage and produces the letter → Individual User #8 consumes that letter to finish the sale.

**Status:** Already correctly cross-referenced on both sides before tonight's audit — the one thread that didn't need fixing. Individual User #8's own SLA explicitly excludes FTI #6's processing time from its own figure, so the two services' timing doesn't double-count.

## Thread 3 — Mortgage validation: Real Estate Developer → Financial & Trust Institutions

A **real-time lookup**, decided in five steps tonight, all now implemented on both sides.

```
RE-dev Service #6 (Register Sale Associated with an Initial Mortgage)
        ↓ developer submits, pays, and — in the same request —
        ↓ validates the cited mortgage reference against...
FTI Service #3 (Mortgage Registration)
        ↓ must already be status = Completed
        ↓ if not Completed: RE-dev #6 is automatically returned, immediately
        ↓ if Completed: RE-dev #6 proceeds to RERA's own review
```

**Direction:** one-directional, RE-dev → FTI only. FTI #3 exposes a read-only lookup endpoint; nothing on FTI's side changes, and — by client decision — FTI's own users have no visibility that this dependency exists.

**Practical consequence:** despite RE-dev #6's name ("Initial Mortgage," suggesting the two might be filed together), the institution's mortgage registration must **fully complete first**. The developer finds this out immediately if they try too early, with no advance warning before submitting and paying.

**Status:** Fully decided and implemented — validation timing (real-time), required status (`Completed`), UX (reject-after, no warning), and visibility (invisible on FTI's side) all confirmed and written into both modules' service files.

## A fourth thread, spotted but not yet cross-referenced anywhere

**Individual User Services #1–#3 (Verify Developer / Verify Development Project / Verify Property)** are read-only lookups against "the official RERAN Developer Registry" (and equivalent project/property registries). Checked Service #1 directly tonight: its own Related Services section only cites its two sibling verification services (#2, #3) — it does **not** cite any Real Estate Developer service, even though the registry it queries almost certainly exists *because* a developer registered through RE-dev's own Company Profile (Feature #9) or Real Estate Licensing Application (Service #22).

**This is not confirmed the way Threads 1–3 are.** I haven't checked RE-dev's Company Profile or Service #22 to see whether either explicitly claims to populate this registry, and I haven't checked whether Individual User #2/#3 have the same gap. It's a plausible, unverified fourth link — flagged, not documented as fact.

## What this mapping is and isn't

**Is:** every cross-module link that came up during tonight's actual audit work — three fully confirmed and reconciled, one spotted in passing.

**Isn't:** an exhaustive check of all 88 services (43 individual-user + 27 real-estate-developer + 18 financial-trust-institutions) for cross-module citations. Threads 1–3 got that level of scrutiny because escrow and mortgage were the natural intersection points already under discussion. Whether other quieter dependencies exist elsewhere — tenancy services referencing a landlord's RE-dev registration, licensing services cross-checking against FTI's institutional approvals, or the verification-registry gap above — hasn't been systematically checked.

If a full 88-service sweep for cross-module citations is wanted, that's a distinct, larger task from what's captured here.
