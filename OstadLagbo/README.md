---
project: OstadLagbo
type: overview
status: current
updated: 2026-09-14
---

# OstadLagbo

## Overview

**Ostad Lagbo (ওস্তাদ লাগবো)** is a Bangladesh-first, map-based marketplace for finding local skill teachers. A learner (**Shagred**) discovers verified experts (**Ostads**) near them on a map, reviews evidence-rich profiles, and contacts them with an offer; the Ostad decides whether to take it. The platform handles **discovery and trust**; the participants handle their own arrangements — no bookings, payments, pricing, or scheduling in the MVP.

- **Status:** Active — planning; requirements, NFRs, governance policies, data models, platform architecture, and seed data complete; api and ui layers next
- **Owner:** Iftikher (sole founder: sponsor, project manager, product owner)
- **Stack (ADR-001):** Flutter (Android + iOS), bilingual English + Bangla UI (CL-016) · **Supabase** (Singapore) for database, auth, storage, realtime, and scheduled jobs · **Render** (Singapore) for the API and policy layer · **Vercel** for the admin dashboard and public website · Firebase Cloud Messaging for push · a Bangladesh SMS gateway for OTP · OpenStreetMap tiles · Cloudflare at the edge. **$0 through development; ≈ $52/month + SMS from the first real user.**

## Entry points

- [Project Standards](/OstadLagbo/project-standards.md) — module definition, derivation chain, vocabulary. Read before creating any document.
- [Glossary](/OstadLagbo/glossary.md) — canonical term definitions for the whole project.
- [MVP Scope Baseline v1.1](/OstadLagbo/reference/baseline/mvp-scope-v1.1.md) — the approved, change-controlled definition of MVP scope. Scope questions are answered here, read together with the change log's pending-v1.2 entries.
- [Skill Categories v1.0](/OstadLagbo/reference/baseline/skill-categories-v1.0.md) — the approved bilingual seed taxonomy (51 categories), launch-focus categories, and the fuzzy-matching test set.
- [Non-Functional Requirements](/OstadLagbo/non-functional-requirements.md) — performance, security, device floor, and quality targets every module inherits.
- [Data Model Overview](/OstadLagbo/data-model-overview.md) — conventions, entity ownership map, cross-cutting rules, and the authorization model. The index to all eight module data models.
- [ADR-001 Platform Architecture](/OstadLagbo/decisions/adr-001-platform-architecture.md) — the accepted three-tier architecture, why it was chosen over the alternatives, the phased cost model, and the open items it created.
- [Change Log](/OstadLagbo/governance/change-log.md) — every approved scope change (CL-001…020), and the rule that changes are logged before implementation.
- [Project Charter](/OstadLagbo/governance/project-charter.md) · [Stakeholder Register](/OstadLagbo/governance/stakeholder-register.md) · [Risk Register](/OstadLagbo/governance/risk-register.md) · [Build Sequence](/OstadLagbo/governance/build-sequence.md)
- Policies: [Data Retention](/OstadLagbo/governance/data-retention-policy.md) · [Privacy Policy](/OstadLagbo/governance/privacy-policy.md) · [Terms of Service](/OstadLagbo/governance/terms-of-service.md) · [Incident Response](/OstadLagbo/governance/incident-response.md) — retention is in force; the user-facing pair need a v1.1 refresh (driving licence, email reveal, termination, Singapore data location) and then Bangladesh legal review before launch.
- `modules/<module>/requirements/` — approved requirements for all eight modules: REG, OSP, SGP, MAP, OFR, ADM, RNT, SUP.
- `modules/<module>/data-model/` — approved data models for all eight modules, each reviewed adversarially and then cross-layer reviewed.
- `decisions/` — architecture decision records; each accepted ADR is immutable and superseded only by a later ADR.
- `reference/discovery/` — dated decision capture; notes are superseded by the module documents that absorb them.

## Current phase

Planning — technical design. Requirements layer complete and twice feature-audited; governance policy bundle complete; the 2026-09-12 planning review added the build sequence, non-functional requirements, the authorization model, and the glossary; the data-model layer completed 2026-09-13 and was cross-layer reviewed the same day (adding CL-019 admin termination); ADR-001 accepted and the skill-category seed data approved 2026-09-13; a whole-KB review on 2026-09-14 placed termination in the build sequence, added REG-14 language preference, logged CL-020 (public website), reviewed the risk register (R-11: AI-generated code), and refreshed the reference documents. Next deliverables, in order: the **api** layer per module (endpoint contracts on the Render API, citing the data models); the **ui** layer (screens, and the public website's content); the **Privacy Policy and ToS v1.1 refresh** ahead of legal review; the **analytics event catalog** and **notification catalog**; **schedule, milestones, and budget** (ADR-001's phased cost model is the budget's infrastructure input); and **baseline v1.2**, cut before Execution begins, absorbing CL-009…020, after which a scope freeze applies (build sequence, principle 4). The discovery sprint was declined by the founder on 2026-09-12; R-01's supply-side assumptions remain unvalidated by decision. ADR-001's legal item (PDPA data residency for identity documents in Singapore) must close before Slice 1 collects the first NID.
