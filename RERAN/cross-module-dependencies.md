---
project: RERAN
type: reference
status: current
updated: 2026-08-16
derived_from:
  - "RERAN/modules/individual-user/service-flows/"
  - "RERAN/modules/real-estate-developer/service-flows/"
  - "RERAN/modules/financial-trust-institutions/service-flows/"
tags:
  - cross-module
  - dependencies
  - mapping
---

# Cross-Module Service Dependencies

Where a service in one module triggers, depends on, or is required by a service in another module. Built by checking each claimed cross-module reference directly against its target file — not assumed from a service's name or description alone, following the same verification standard as the rest of this project.

**Scope:** the three modules with service flows written — Individual User, Real Estate Developer, Financial & Trust Institutions. Group D (Real Estate Service Companies) is expected to add at least one more dependency once built — see the Open Question at the bottom.

---

## The Three Confirmed Dependency Chains

### 1. Real Estate Developer → Individual User (provisional sale → purchaser record)

A developer registers a provisional sale/lease/usufruct on a unit within its project (Real Estate Developer, Services #1–#3). The purchaser side of that same transaction is where the individual person's own record lives (Individual User, Services #6, #10, #14).

| Real Estate Developer | Individual User | Relationship |
| :---- | :---- | :---- |
| Service #1 — Register Initial Sale | Service #6 — Register Property Sale | "the purchaser-side counterpart once the sale is complete" |
| Service #2 — Register Initial Rent-to-Own | Service #10 — Register Lease-to-Own | "the tenant-purchaser-side counterpart" |
| Service #3 — Register Initial Usufruct | Service #14 — Register Usufruct Right | Same pattern, presumed by symmetry — **not individually re-verified this session; check before relying on it** |

**Documentation status: one-directional, not reciprocated.** I checked both sides of the #1↔#6 and #2↔#10 pairs directly. Real Estate Developer's files cite Individual User explicitly, by service number, in their own Related Services sections. Individual User's #6 and #10 do **not** cite the corresponding Real Estate Developer service anywhere in their own Related Services — #6 lists only #3, #4, #5, #7 (all individual-user); #10 lists only #11, #12, #13, #5, #6 (all individual-user). The link exists in one file and is silently absent from its counterpart.

This is a real gap, not a design choice — nothing in either file explains why the reference isn't reciprocated, and the relationship itself is exactly the kind of thing a reader of Individual User's #6 would want to know (that a Real Estate Developer provisional sale is what typically precedes this record). Worth fixing as a small, contained correction pass: add the reciprocal note to Individual User #6, #10, and (once verified) #14.

### 2. Real Estate Developer ↔ Financial & Trust Institutions (mortgage-linked sale, real-time validation)

Built as a genuine product decision on 2026-08-16, not inherited from source. A developer registering a sale where the unit carries a mortgage must have that mortgage already registered and completed with the lending institution.

| Real Estate Developer | Financial & Trust Institutions | Relationship |
| :---- | :---- | :---- |
| Service #6 — Register Sale Associated with an Initial Mortgage | Service #3 — Mortgage Registration | Real-time, synchronous validation query |

**Documentation status: fully bidirectional, and unusually thorough on both sides** — this is the most completely specified cross-module dependency in the project. Both files independently confirm the same five-part contract:

- **Timing:** real-time, synchronous — the query happens inside Real Estate Developer #6's own submission request, not a background or batch job.
- **Match condition:** only a `Completed` record on Financial & Trust Institutions #3 counts as valid. Any earlier status (`Pending Internal Certification`, `Under Review`, `Information Requested`, etc.) is reported as "not yet valid," explicitly distinguished from "not found" — so the developer's side can tell a wrong reference apart from one that's still processing.
- **Direction of visibility:** deliberately one-way, by client decision. Financial & Trust Institutions #3's own screen, workflow, and users are unaffected and unaware — no indicator, badge, or notification exists anywhere on that side. The consequence lands entirely on Real Estate Developer #6, which finds out immediately, in its own request, if the mortgage isn't ready.
- **Practical consequence:** Financial & Trust Institutions #3's own 20–25 minute SLA becomes the practical floor for how long a developer must wait before the linked sale can proceed — a fact the institution has no visibility into and no reason to treat differently.
- **API contract:** a new read-only endpoint on Financial & Trust Institutions #3 ("Expose Mortgage Lookup / Validation"), explicitly scoped as synchronous and fast enough to sit inside a caller's own request.

Both files' Open Questions sections confirm this dependency's six sub-questions (status match, timing, visibility, etc.) are all resolved — none left open.

### 3. Real Estate Developer → Financial & Trust Institutions (escrow requests, routed to Account Trustee)

Developer-side escrow actions don't have their own approval workflow inside Real Estate Developer at all — they're submitted there but assessed and certified inside Financial & Trust Institutions.

| Real Estate Developer | Financial & Trust Institutions | Relationship |
| :---- | :---- | :---- |
| Service #8 — Escrow Account Activation | Feature #4 — Escrow Request Queue | Routed for Trustee assessment |
| Service #9 — Escrow Account Transfer | Feature #4 — Escrow Request Queue | Routed for Trustee assessment |
| Service #10 — Project Profit Withdrawal | Feature #4 — Escrow Request Queue | Routed for Trustee assessment |
| Service #12 — Receive Payment from Escrow Account | Feature #4 — Escrow Request Queue | Routed for Trustee assessment |
| Service #20 — Depositing a Mortgage into Escrow | Feature #4 — Escrow Request Queue | Routed for Trustee assessment |
| Service #21 — Bank Guarantee Cancellation | Feature #4 — Escrow Request Queue | Routed for Trustee assessment |

**Documentation status: bidirectional, cited by name.** Financial & Trust Institutions' `feature-04-escrow-request-queue.md` lists all six Real Estate Developer service files directly in its own `derived_from` frontmatter and describes the flow explicitly: "Requests arrive from Group B's escrow services... already at the `Trustee Review` stage — the developer-side `Draft` and `Submitted` stages happen before a request reaches this queue at all." The regulator role on both sides was reconciled to the same "Compliance & Escrow Auditor" on 2026-08-16 (see `module-roadmap.md`'s cross-module notes) after a status-vocabulary mismatch was found and fixed.

**One further sub-service worth flagging:** Real Estate Developer Feature #13 (Profit Withdrawal Request), split out from Fund Release Request on 2026-08-16, has **no UI screen built yet**. Its downstream Financial & Trust Institutions connection (via Escrow Request Queue's terminal-state table, which already lists "Project Profit Withdrawal (#10) → Released") is documented on the Financial & Trust Institutions side but not yet reflected anywhere on Real Estate Developer's own screens, since none exist for that feature. Worth checking once that screen is eventually built.

### 4. Individual User ↔ Financial & Trust Institutions (mortgaged property sale)

An individual selling a mortgaged property needs the lending institution to release the mortgage before the sale can complete.

| Individual User | Financial & Trust Institutions | Relationship |
| :---- | :---- | :---- |
| Service #8 — Register Sale of Mortgaged Property | Service #6 — Mortgage Release | The Mortgage Release Letter Individual User #8 requires as a document (Section 7) is issued by this service |
| Service #8 — Register Sale of Mortgaged Property | Service #3 — Mortgage Registration | The mortgage Individual User #8's sale must clear was originally registered here |

**Documentation status: fully bidirectional.** Individual User #8's Related Services section names both Financial & Trust Institutions services explicitly, with the relationship spelled out ("this is the source of the Mortgage Release Letter required at Section 7"). Financial & Trust Institutions #3's Related Services reciprocates directly: "describes the seller/purchaser side of a sale where the property carries a mortgage this service registered; that flow's Mortgage Release Letter corresponds to this module's Service #6." This is the cleanest bidirectional pair in the project — both sides name the other by module and service number, and neither overstates or understates the relationship.

---

## Summary Table

| Pair | Direction | Documentation quality |
| :---- | :---- | :---- |
| Real Estate Developer #1/#2/#3 → Individual User #6/#10/#14 | One-way (source module only) | **Gap** — not reciprocated on the Individual User side |
| Real Estate Developer #6 ↔ Financial & Trust Institutions #3 | Bidirectional | **Excellent** — full five-part contract on both sides |
| Real Estate Developer #8–#12, #20–#21 → Financial & Trust Institutions Feature #4 | Bidirectional | **Good** — cited by name in `derived_from`, described in prose |
| Individual User #8 ↔ Financial & Trust Institutions #3, #6 | Bidirectional | **Excellent** — cleanest pair in the project |

---

## Open Question — Group D's Likely Dependencies

Not yet checkable, since Real Estate Service Companies has no service-flow documents (see `module-build-playbook.md`). Two connections are already anticipated from the source material and the closed issue #34's own scoping:

1. **Jointly Owned Property (JOP) escrow services**, flagged in `module-roadmap.md` as possibly mirroring "Group B's escrow services with different actors." If JOP genuinely reuses the Group B/C escrow mechanism (dependency chain #3 above), it should cross-link to `financial-trust-institutions/ui/screens/escrow-request-queue.md` and the relevant Real Estate Developer service files the same way, rather than re-describing the mechanism independently. Whether it does, or has its own mechanism, was explicitly unresolved when the module was last touched and is Phase 2 work per the playbook.
2. **Real Estate Dispute Services (2 services)**, which may relate to Group A's proposed Tribunal & Remote-Litigation sub-system — Group A isn't documented yet, so this is a dependency to note, not to build against.

**When Group D's Phase 2/3 work happens, apply the lesson from this document's own finding above: write the cross-reference on both sides at the time the second file is created, not just the first.** The Real Estate Developer → Individual User gap happened because the developer-side files were written with full cross-module awareness, and the individual-user files predated that awareness and were never revisited once the reverse link was added elsewhere.
