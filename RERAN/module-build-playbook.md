---
project: RERAN
type: playbook
status: current
updated: 2026-08-16
derived_from:
  - "RERAN/module-roadmap.md"
  - "RERAN/modules/individual-user/"
  - "RERAN/modules/real-estate-developer/"
  - "RERAN/modules/financial-trust-institutions/"
tags:
  - playbook
  - methodology
  - module-build
---

# RERAN Module Build Playbook

How Individual User, Real Estate Developer, and Financial & Trust Institutions were actually built — reconstructed from what worked, what had to be corrected, and why, across all three. This is the sequence to follow for **Real Estate Service Companies (Group D)**, built from scratch rather than picked up mid-way.

None of the three reference modules followed this order the first time. Individual User built flows then UI, with an analysis layer inserted late. Real Estate Developer built UI first, flows underneath it — backwards. Financial & Trust Institutions ran flows → UI → features in the order below, and is the cleanest result of the three specifically because of that order. This playbook is the corrected sequence, not a description of any one module's actual history.

---

## Phase 0 — Source Reconciliation

**Before writing anything new.**

1. Read `RERAN/reference/source-of-truth/RERAN_service_flows_v2.md`'s Service Workflows table and pull every row belonging to Group D. `module-roadmap.md` already records the expected shape — Jointly Owned Property (11) + Real Estate Licensing (8) + Real Estate Rental (3) + Real Estate Transaction (2) + Real Estate Dispute (2) = 26 — treat that as a check to verify, not a number to assume.
2. Build the row-to-service mapping explicitly, and **do not assume row order equals file order.** Financial & Trust Institutions had rows 38 and 39 transposed against file order and it was only caught by checking directly. Individual User's 41-vs-43 count only reconciled once every row was traced to a specific file — ten dispute rows consolidated into one service, one lease row split into two, two amendment rows merged into one, the rest 1:1.
3. Where a service is genuinely not traceable to any row, mark it `extrapolated` in frontmatter (`source_type: extrapolated`) rather than silently treating it as sourced. Individual User's convention — 32 `sourced`, 11 `extrapolated` — is the house style; carry it forward.
4. Write the row-to-mapping down somewhere durable (a PR description, or a table in `services-overview.md` itself) before moving on. Don't rely on remembering it three phases later.

---

## Phase 1 — Foundational Docs

Two files, written from the source's Groups & Roles table and the Service Workflows rows — not yet touching payments or open questions.

**`roles-and-responsibilities.md`** — the group's roles (Group D: Brokerage Principal, Owners'-Association Manager, Property Management Officer, Company Dispute Filing Officer), each with purpose, responsibilities, and a worked example grounded in an actual row from the source table, not invented.

**`services-overview.md`** — categorize the 26 services into logical groups (the five source categories are a reasonable starting point, but check whether they group sensibly for a user browsing them, the way individual-user's five business-service categories were regrouped from RERA's internal filing categories). Include a Business Services Summary table with counts per category, and leave a **Service Provenance** section for Phase 0's `sourced`/`extrapolated` breakdown.

Do not touch payment timing, fee amounts, or role-ownership-per-service in this phase — that's Phase 2, and doing it here risks the same mistake Group C made initially (assuming one payment model before checking).

---

## Phase 2 — Payments & Open Questions

This is where two of the three reference modules found their most consequential corrections, and it's worth doing thoroughly rather than quickly.

**`payments.md`** — work out how Group D's 26 services are actually paid for, service by service, not assumed as one model. Group C started from "one standing account model" and it took two separate corrected passes before the real shape (per-transaction, two timing patterns, later three, then normalized back to two) was right. Specific things to check for Group D:

- Does a single payer/timing model actually hold, or does it vary by sub-domain (JOP vs. Licensing vs. Rental vs. Transaction vs. Dispute)?
- **The JOP escrow question, specifically:** the roadmap flags Jointly Owned Property services as mirroring "Group B's escrow services with different actors." Check directly whether JOP genuinely reuses the Group B/C escrow-account mechanism (in which case it should cross-link to `financial-trust-institutions/ui/screens/escrow-request-queue.md` rather than re-describing it) or has its own distinct mechanism. Don't assume either way — this was explicitly unresolved when the module was last touched.
- Check every row's own workflow text for where "pay" actually sits in the sequence, the same way Financial & Trust Institutions found Services #12 and #18 paying *after* the regulator's decision, contrary to the module's own general pattern — a fact only found by checking those two rows individually, not inferred from neighbors.

**`open-questions.md`** — work through the same four categories Financial & Trust Institutions' document uses: role ownership (does the source's Responsible Role column hold up service-by-service, or is it a coarse default the way Group C's "Mortgage Officer" attribution turned out to be for #12–#17?), payment/settlement mechanics, service structure and categorization, platform-wide questions (status vocabulary — reuse Group C's platform-core-plus-extension proposal, D1, rather than inventing a new one).

Every question gets a **proposed answer**, a confidence level (Sourced / High / Medium / Client data), and what breaks if it's wrong. Reserve "Client data" for things that genuinely cannot be reasoned to from the source — Group C's 23 original questions had exactly one (the fee schedule amount itself). If Group D's answer to a question is "same as Group C's, unchanged," say that and cite the answer rather than re-deriving it from scratch.

**Do not defer this phase's findings into Phase 3 as TODOs.** Every open question needs a proposed answer before service-flow writing starts, so Phase 3 is applying decisions, not making them mid-file.

---

## Phase 3 — Service-Flow Documents

One file per service, `service-01-*.md` through `service-26-*.md`, using the individual-user 21-section template (`service-08-register-sale-of-mortgaged-property.md` is the reference example) — roughly 6–10 KB per file.

Apply every Phase 2 decision consistently across all 26 files as they're written, not after. This is materially cheaper than the alternative: Individual User's Section 9 payment-timing defect had to be corrected across 19 of 43 files *after* the fact because a single wrong boilerplate paragraph got copied forward before the real per-service timing was checked.

Mark every genuinely unsourced field (`Required Documents` where the source just says "attach documents," an assumed SLA, an assumed field list) explicitly as **Proposed**, with the reasoning for the assumption stated inline — this is the house style across all three modules and makes later audit passes possible, since a reviewer can immediately tell sourced fact from reasonable inference.

Where a service is a near-duplicate of another (the source often just says "same as X" for a whole cluster of rows), expand it in full rather than leaving a bare cross-reference — Financial & Trust Institutions' Services #32–#37 and #35 are the pattern to follow, not to abbreviate.

---

## Phase 4 — UI Screens

**Do not propose the UI package's screen count or field-layout patterns in the abstract.** Check each of the 26 services' own Section 6 (Required Information) individually before assuming a pattern from another module will scale. Individual User assumed Group C's 3-pattern model (flat fields / repeatable groups / field-selection pairs) would carry over and found 11 distinct patterns once every service was actually checked. Group D likely needs its own audit here — JOP's escrow-adjacent services, licensing services, rental services, transaction services and dispute services are different enough in shape that a single shared submission-form pattern is not a safe starting assumption.

Build:
- **`navigation.md`** — sidebar structure and access model. Both Group B and Group C ended up at the same unified-access conclusion (no per-role gating, role as audit-trail attribution only) after starting from a role-scoped model and correcting it by client decision. Consider proposing the unified model from the start for Group D rather than repeating that correction cycle, but flag it as a proposal needing the same client confirmation, not an assumption.
- **`role-workflows.md`** — the shared user journey, written after the access model is settled, not before (a role-scoped journey written first has to be substantially rewritten if the access model later changes, which is exactly what happened twice).
- **`ui/screens/`** — one file per screen, following the section template (Purpose / Layout / Sections / Empty State / Reused Components / Validation / User Flow / Notes) used consistently across all three modules.
- **`ui/screens-unified/`** (or equivalent) — if a canonical multi-service submission form makes sense for Group D the way it did for Financial & Trust Institutions' 18 services, build it here; if the 26 services split too unevenly across sub-domains for one form, say so explicitly rather than forcing a single-form design that doesn't fit.

---

## Phase 5 — Shared Platform Features

**Derive this from the actual built screens, bottom-up — never propose it by analogy to another module's feature count.** This is the single most repeated mistake across all three modules: Group C's original 17-feature list (proposed by analogy to Individual User's count) was wrong and had to be rebuilt to 12 by checking Group C's own screens directly, finding two genuinely missed features (Trust Accounts, Compliance Reports) in the process. Group B's shared-features layer was never sourced at all and had to be built the same way, arriving at 13 features including a late split (Profit Withdrawal Request separated from Fund Release Request once the two services' actual field shapes were compared and found genuinely different).

For Group D: once Phase 4's screens exist, walk every screen and ask what cross-cutting capability it represents (application lifecycle tracking, a domain-specific queue, a settings/profile area, documents, notifications, help) — the feature list falls out of that, not the other way around.

Build the UI shared docs the same way, from what the screens actually contain, not from a template:
- **`ui/components.md`** — every reused component, defined once.
- **`ui/status-badges.md`** — every status vocabulary, sourced from the individual service files' own Section 13, not from a screen's filter dropdown values. This exact mistake — treating a UI filter list as if it were the sourced status flow — caused a real, multi-file correction in Financial & Trust Institutions on 2026-08-15/16 (the `Approved — Awaiting Payment` saga). Check the service-flow file directly, every time.
- **`ui/validation-rules.md`** — shared validation patterns, cross-referenced from screens rather than restated per screen.

---

## Phase 6 — Audit & Correction Passes

**Budget for this. It is not optional cleanup — it is where most of the real errors in the other three modules were actually found**, and it takes multiple passes because corrections themselves introduce new inconsistencies that need their own pass to catch.

Every correction found during this phase falls into one of three failure modes — named after Individual User's nine audit passes first identified all three, and Financial & Trust Institutions reproduced the same three-part pattern independently on 2026-08-16:

1. **Drift** — a fix made in one file never propagated to another document that references it by name or describes the same fact. (Example: Financial & Trust Institutions' `#12/#18` payment-timing normalization landed in `payments.md` and the two service files, but not in seven other UI screens and feature docs that separately described the same exception.)
2. **Non-execution** — a decision is recorded as made but never actually carried out. (Example: Real Estate Developer's `feature-05` claimed a "Bank → Trustee" terminology correction had been applied to a UI screen; the screen itself was never touched.)
3. **Omission** — something is left out of a document entirely, not even described wrongly. (Example: Financial & Trust Institutions' `services-overview.md` referenced a new "Feature #13 — Staff Records" that was never actually built as a file.)

All three look identical from the outside — a document says one thing and reality says another, or says nothing at all — but need different checks: drift needs cross-referencing between every document that could mention the same fact; non-execution needs checking a decision log against the actual file it claims to have changed; omission needs counting against a known total (does the feature list's count match the number of files that actually exist?).

**Practical audit method, proven across two full-module passes:** read every file in the module, not a sample. Check every specific factual claim — a cited source row, a claimed correction, a cross-reference to another file — against its actual target, not just for internal self-consistency. When a genuine finding turns up, before fixing it, check whether the same underlying fact is asserted anywhere else in the module (it usually is, in at least one more place than expected).

**A correction is not verified complete until checked against every document that could reference it — not just the one it was made in.**

---

## What Not To Do

Collected from corrections made across all three modules, since each of these cost real rework when it happened the first time:

- Don't assume a single payment/timing model across a whole module without checking individual rows.
- Don't trust the source table's Responsible Role column as a genuine per-service assignment without checking it against the role descriptions and worked examples — it read as a coarse category default in both Group B and Group C.
- Don't assume row order equals file order in the source table.
- Don't propose a shared-features list or a UI field-pattern count by analogy to another module — derive both from the actual built material.
- Don't build `role-workflows.md` or a role-scoped UI before the access model (`navigation.md`) is settled — write the journey after the access model, not before it.
- Don't take a UI screen's filter dropdown values as the sourced status vocabulary — check the individual service files' own status-flow sections.
- Don't treat a correction as finished once it's made in the file that prompted it. Check every other file that could reference the same fact.
- Don't skip marking something "Proposed" just because it seems obvious — the whole audit method depends on being able to tell sourced fact from inference at a glance.

---

## Sequence Summary

| Phase | Output | Depends on |
| :---- | :---- | :---- |
| 0 — Source Reconciliation | Row-to-service mapping | Source table only |
| 1 — Foundational Docs | `roles-and-responsibilities.md`, `services-overview.md` | Phase 0 |
| 2 — Payments & Open Questions | `payments.md`, `open-questions.md` | Phase 1 |
| 3 — Service-Flow Documents | 26 files under `service-flows/` | Phase 2 |
| 4 — UI Screens | `navigation.md`, `role-workflows.md`, `ui/screens/`, `ui/screens-unified/` | Phase 3 |
| 5 — Shared Platform Features | `shared-platform-features.md`, `ui/components.md`, `ui/status-badges.md`, `ui/validation-rules.md` | Phase 4 (derived from it, not planned ahead of it) |
| 6 — Audit & Correction Passes | Everything above, checked and cross-referenced | All prior phases complete |

This is the order Financial & Trust Institutions actually followed, and it produced the module `module-roadmap.md` calls "the cleanest house-style example" of the three. Individual User and Real Estate Developer both reached the same end state, but at the cost of extra correction passes because features or UI were built before the layer beneath them was settled. Follow this order for Group D and the Phase 6 work should be smaller, not eliminated.
