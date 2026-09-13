---
project: OstadLagbo
type: overview
status: current
updated: 2026-09-13
---

# OstadLagbo

## Overview

**Ostad Lagbo (ওস্তাদ লাগবো)** is a Bangladesh-first, map-based marketplace for finding local skill teachers. A learner (**Shagred**) discovers verified experts (**Ostads**) near them on a map, reviews evidence-rich profiles, and contacts them with an offer; the Ostad decides whether to take it. The platform handles **discovery and trust**; the participants handle their own arrangements — no bookings, payments, pricing, or scheduling in the MVP.

- **Status:** Active — planning; requirements, NFRs, governance policies, and **data models complete**; api and ui layers next
- **Owner:** Iftikher (sole founder: sponsor, project manager, product owner)
- **Stack:** Flutter (Android + iOS), bilingual English + Bangla UI (CL-016); separate web dashboard for admin (English, TOTP-secured); backend not yet decided — the data-model layer now states the requirements the backend must satisfy

## Entry points

- [Project Standards](/OstadLagbo/project-standards.md) — module definition, derivation chain, vocabulary. Read before creating any document.
- [Glossary](/OstadLagbo/glossary.md) — canonical term definitions for the whole project.
- [MVP Scope Baseline v1.1](/OstadLagbo/reference/baseline/mvp-scope-v1.1.md) — the approved, change-controlled definition of MVP scope. Scope questions are answered here, read together with the change log's pending-v1.2 entries.
- [Non-Functional Requirements](/OstadLagbo/non-functional-requirements.md) — performance, security, device floor, and quality targets every module inherits.
- [Data Model Overview](/OstadLagbo/data-model-overview.md) — conventions, entity ownership map, cross-cutting rules, and the authorization model. The index to all eight module data models.
- [Change Log](/OstadLagbo/governance/change-log.md) — every approved scope change (CL-001…018), and the rule that changes are logged before implementation.
- [Project Charter](/OstadLagbo/governance/project-charter.md) · [Stakeholder Register](/OstadLagbo/governance/stakeholder-register.md) · [Risk Register](/OstadLagbo/governance/risk-register.md) · [Build Sequence](/OstadLagbo/governance/build-sequence.md)
- Policies: [Data Retention](/OstadLagbo/governance/data-retention-policy.md) · [Privacy Policy](/OstadLagbo/governance/privacy-policy.md) · [Terms of Service](/OstadLagbo/governance/terms-of-service.md) · [Incident Response](/OstadLagbo/governance/incident-response.md) — retention is in force; the user-facing pair await Bangladesh legal review before launch.
- `modules/<module>/requirements/` — approved requirements for all eight modules: REG, OSP, SGP, MAP, OFR, ADM, RNT, SUP.
- `modules/<module>/data-model/` — approved data models for all eight modules, each reviewed adversarially before approval.
- `reference/discovery/` — dated decision capture; notes are superseded by the module documents that absorb them.

## Current phase

Planning — technical design. Requirements layer complete and twice feature-audited; governance policy bundle complete; the 2026-09-12 planning review added the build sequence, non-functional requirements, the authorization model, and the glossary; the **data-model layer completed 2026-09-13** (eight module models plus the overview, with every model passing an adversarial review before approval — the reviews surfaced and fixed defects in six of the eight). Next deliverables, in order: an **architecture decision record** for the backend with a cost model (the data models now state exactly what it must satisfy — spatial + fuzzy cross-script indexing, request-log coordinate scrubbing, append-only audit storage); the **seed skill-category list** with English and Bangla names (ADM-11/CL-013); the **api** and **ui** layers per the derivation chain; **schedule, milestones, and budget**; and **baseline v1.2**, cut before Execution begins, absorbing CL-009…018, after which a scope freeze applies (build sequence, principle 4). The discovery sprint was declined by the founder on 2026-09-12; R-01's supply-side assumptions remain unvalidated by design.
