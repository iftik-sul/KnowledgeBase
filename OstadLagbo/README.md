---
project: OstadLagbo
type: overview
status: current
updated: 2026-08-30
---

# OstadLagbo

## Overview

**Ostad Lagbo (ওস্তাদ লাগবো)** is a Bangladesh-first, map-based marketplace for finding local skill teachers. A learner (**Shagred**) discovers verified experts (**Ostads**) near them on a map, reviews evidence-rich profiles, and contacts them with an offer; the Ostad decides whether to take it. The platform handles **discovery and trust**; the participants handle their own arrangements — no bookings, payments, pricing, or scheduling in the MVP.

- **Status:** Active — planning; requirements complete for all eight modules; governance policies in force; technical design (data-model / api / ui) next
- **Owner:** Iftikher (sole founder: sponsor, project manager, product owner)
- **Stack:** Flutter (Android + iOS), bilingual English + Bangla UI (CL-016); separate web dashboard for admin (English); backend not yet decided

## Entry points

- [Project Standards](/OstadLagbo/project-standards.md) — module definition, derivation chain, vocabulary. Read before creating any document.
- [MVP Scope Baseline v1.1](/OstadLagbo/reference/baseline/mvp-scope-v1.1.md) — the approved, change-controlled definition of MVP scope. Scope questions are answered here, read together with the change log's pending-v1.2 entries.
- [Change Log](/OstadLagbo/governance/change-log.md) — every approved scope change (CL-001…016), and the rule that changes are logged before implementation.
- [Project Charter](/OstadLagbo/governance/project-charter.md) · [Stakeholder Register](/OstadLagbo/governance/stakeholder-register.md) · [Risk Register](/OstadLagbo/governance/risk-register.md)
- Policies: [Data Retention](/OstadLagbo/governance/data-retention-policy.md) · [Privacy Policy](/OstadLagbo/governance/privacy-policy.md) · [Terms of Service](/OstadLagbo/governance/terms-of-service.md) · [Incident Response](/OstadLagbo/governance/incident-response.md) — retention is in force; the user-facing pair await Bangladesh legal review before launch.
- `modules/<module>/requirements/` — approved requirements for all eight modules: REG, OSP, SGP, MAP, OFR, ADM, RNT, SUP.
- `reference/discovery/` — dated decision capture; notes are superseded by the module documents that absorb them.

## Current phase

Planning — requirements layer complete and twice feature-audited (2026-08-30); governance policy bundle complete. Next deliverables, in order: per-module **data-model** documents (then api, then ui, per the derivation chain); the **seed skill-category list** with English and Bangla names (ADM-11/CL-013); **schedule, milestones, and budget** (closing the charter's open sections); and **baseline v1.2**, cut before Execution begins, absorbing CL-009…016.
