---
project: OstadLagbo
type: overview
status: current
updated: 2026-09-12
---

# OstadLagbo

## Overview

**Ostad Lagbo (ওস্তাদ লাগবো)** is a Bangladesh-first, map-based marketplace for finding local skill teachers. A learner (**Shagred**) discovers verified experts (**Ostads**) near them on a map, reviews evidence-rich profiles, and contacts them with an offer; the Ostad decides whether to take it. The platform handles **discovery and trust**; the participants handle their own arrangements — no bookings, payments, pricing, or scheduling in the MVP.

- **Status:** Active — planning; requirements, NFRs, and governance policies complete; technical design (data-model / api / ui) in progress
- **Owner:** Iftikher (sole founder: sponsor, project manager, product owner)
- **Stack:** Flutter (Android + iOS), bilingual English + Bangla UI (CL-016); separate web dashboard for admin (English, TOTP-secured); backend not yet decided

## Entry points

- [Project Standards](/OstadLagbo/project-standards.md) — module definition, derivation chain, vocabulary. Read before creating any document.
- [Glossary](/OstadLagbo/glossary.md) — canonical term definitions for the whole project.
- [MVP Scope Baseline v1.1](/OstadLagbo/reference/baseline/mvp-scope-v1.1.md) — the approved, change-controlled definition of MVP scope. Scope questions are answered here, read together with the change log's pending-v1.2 entries.
- [Non-Functional Requirements](/OstadLagbo/non-functional-requirements.md) — performance, security, device floor, and quality targets every module inherits.
- [Data Model Overview](/OstadLagbo/data-model-overview.md) — conventions, entity ownership map, and the authorization model.
- [Change Log](/OstadLagbo/governance/change-log.md) — every approved scope change (CL-001…018), and the rule that changes are logged before implementation.
- [Project Charter](/OstadLagbo/governance/project-charter.md) · [Stakeholder Register](/OstadLagbo/governance/stakeholder-register.md) · [Risk Register](/OstadLagbo/governance/risk-register.md) · [Build Sequence](/OstadLagbo/governance/build-sequence.md)
- Policies: [Data Retention](/OstadLagbo/governance/data-retention-policy.md) · [Privacy Policy](/OstadLagbo/governance/privacy-policy.md) · [Terms of Service](/OstadLagbo/governance/terms-of-service.md) · [Incident Response](/OstadLagbo/governance/incident-response.md) — retention is in force; the user-facing pair await Bangladesh legal review before launch.
- `modules/<module>/requirements/` — approved requirements for all eight modules: REG, OSP, SGP, MAP, OFR, ADM, RNT, SUP.
- `modules/<module>/data-model/` — data models as they are produced (REG done; 7 remain).
- `reference/discovery/` — dated decision capture; notes are superseded by the module documents that absorb them.

## Current phase

Planning. Requirements layer complete and twice feature-audited; governance policy bundle complete; a 2026-09-12 planning review (`governance/planning-review-2026-09-12.md`) added the build sequence, non-functional requirements, the authorization model, and this glossary. Next deliverables, in order: the **discovery sprint** (real Ostad/Shagred interviews, run in parallel); remaining per-module **data-model** documents (OSP next, then SGP, ADM, MAP, OFR, RNT, SUP); the **seed skill-category list** with English and Bangla names (ADM-11/CL-013); an **architecture decision record** for the backend with a cost model; **schedule, milestones, and budget**; and **baseline v1.2**, cut before Execution begins, absorbing CL-009…018, after which a scope freeze applies (build sequence, principle 4).
