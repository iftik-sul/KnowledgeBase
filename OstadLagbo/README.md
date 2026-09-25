---
project: OstadLagbo
type: overview
status: current
updated: 2026-09-25
---

# OstadLagbo

## Overview

**Ostad Lagbo (ওস্তাদ লাগবো)** is a Bangladesh-first, map-based marketplace for finding local skill teachers. A learner (**Shagred**) discovers verified experts (**Ostads**) near them on a map, reviews evidence-rich profiles, and contacts them with an offer; the Ostad decides whether to take it. The platform handles **discovery and trust**; the participants handle their own arrangements — no bookings, payments, pricing, or scheduling in the MVP.

- **Status:** Active — planning. The full specification chain is complete: requirements, NFRs, governance policies, data models, platform architecture, seed data, **APIs, and UI** — all eight modules across every layer, plus the admin dashboard and public website. Next: baseline v1.2 + scope freeze, schedule/milestones/budget, and the Privacy Policy & ToS v1.1 refresh ahead of legal review.
- **Owner:** Iftikher (sole founder: sponsor, project manager, product owner)
- **Stack (ADR-001):** Flutter (Android + iOS), bilingual English + Bangla UI (CL-016) · **Supabase** (Singapore) for database, auth, storage, realtime, and scheduled jobs · **Render** (Singapore) for the API and policy layer · **Vercel** for the admin dashboard and public website · Firebase Cloud Messaging for push · a Bangladesh SMS gateway for OTP · OpenStreetMap tiles · Cloudflare at the edge. **$0 through development; ≈ $52/month + SMS from the first real user.**

## Entry points

- [Project Standards](/OstadLagbo/project-standards.md) — module definition, derivation chain, vocabulary. Read before creating any document.
- [Glossary](/OstadLagbo/glossary.md) — canonical term definitions for the whole project.
- [MVP Scope Baseline v1.1](/OstadLagbo/reference/baseline/mvp-scope-v1.1.md) — the approved, change-controlled definition of MVP scope. Scope questions are answered here, read together with the change log's pending-v1.2 entries.
- [Skill Categories v1.0](/OstadLagbo/reference/baseline/skill-categories-v1.0.md) — the approved bilingual seed taxonomy (51 categories), launch-focus categories, and the fuzzy-matching test set.
- [Non-Functional Requirements](/OstadLagbo/non-functional-requirements.md) — performance, security, device floor, and quality targets every module inherits.
- [Data Model Overview](/OstadLagbo/data-model-overview.md) — conventions, entity ownership map, cross-cutting rules, and the authorization model. The index to all eight module data models.
- [API Overview](/OstadLagbo/api-overview.md) — the api-layer rulebook: authentication, the identifier and opacity rules, the closed error enum, idempotency, media, and the endpoint template every module api obeys.
- [UI Overview](/OstadLagbo/ui-overview.md) — the ui-layer rulebook: the four surfaces, the app shells, the error-to-UI mapping, shared components, and the screen-spec template every module ui obeys.
- [ADR-001 Platform Architecture](/OstadLagbo/decisions/adr-001-platform-architecture.md) — the accepted three-tier architecture, why it was chosen over the alternatives, the phased cost model, and the open items it created.
- [Change Log](/OstadLagbo/governance/change-log.md) — every approved scope change (CL-001…021), and the rule that changes are logged before implementation.
- [Project Charter](/OstadLagbo/governance/project-charter.md) · [Stakeholder Register](/OstadLagbo/governance/stakeholder-register.md) · [Risk Register](/OstadLagbo/governance/risk-register.md) · [Build Sequence](/OstadLagbo/governance/build-sequence.md)
- Policies: [Data Retention](/OstadLagbo/governance/data-retention-policy.md) · [Privacy Policy](/OstadLagbo/governance/privacy-policy.md) · [Terms of Service](/OstadLagbo/governance/terms-of-service.md) · [Incident Response](/OstadLagbo/governance/incident-response.md) — retention is in force; the user-facing pair need a v1.1 refresh (driving licence, email reveal, termination, Singapore data location) and then Bangladesh legal review before launch.
- `modules/<module>/requirements/` — approved requirements for all eight modules: REG, OSP, SGP, MAP, OFR, ADM, RNT, SUP.
- `modules/<module>/data-model/` — approved data models for all eight modules, each reviewed adversarially and then cross-layer reviewed.
- `modules/<module>/api/` — endpoint contracts for all eight modules on the Render API, citing the data models; governed by the API Overview and cross-layer audited end to end.
- `modules/<module>/ui/` — screen specifications for all eight modules, deriving from requirements and binding to the api; the admin dashboard is `admin-review/ui/`, and the public marketing-and-legal site is [`ui/public-website.md`](/OstadLagbo/ui/public-website.md) (CL-020).
- `decisions/` — architecture decision records; each accepted ADR is immutable and superseded only by a later ADR.
- `reference/discovery/` — dated decision capture; notes are superseded by the module documents that absorb them.

## Current phase

Planning — technical design, **specification complete**. The full derivation chain now exists for all eight modules: requirements → data models → **APIs** → **UI**, on top of the governance, decisions (ADR-001/002), reference, and non-functional layers.

Milestones so far: the requirements layer was twice feature-audited; the governance policy bundle completed; the 2026-09-12 planning review added the build sequence, NFRs, the authorization model, and the glossary; the data-model layer completed 2026-09-13 with a same-day cross-layer review (adding CL-019 termination); ADR-001 and the skill-category seed data were accepted 2026-09-13; a whole-KB review on 2026-09-14 sequenced termination, added REG-14 language preference, and logged CL-020 (public website); the **api layer** was built per module against the data models, then given a full **cross-layer audit** (which surfaced CL-021 photo-as-key-field and several consistency fixes); and the **ui layer** was built per module against the api — the seven app modules, the admin dashboard, and the public website — each adversarially reviewed before merge.

Next deliverables, in order: **baseline v1.2**, cut before Execution begins, absorbing CL-009…021 and applying a scope freeze (build sequence, principle 4); **schedule, milestones, and budget** (ADR-001's phased cost model is the budget's infrastructure input); and the **Privacy Policy and ToS v1.1 refresh** (driving licence, email reveal, termination, Singapore data location) ahead of Bangladesh legal review. The analytics event catalog and notification catalog remain to be drawn out explicitly, though both are specified in-line across the api and ui layers.

Standing items: the discovery sprint was declined by the founder on 2026-09-12, so R-01's supply-side assumptions remain unvalidated by decision; and ADR-001's legal item (PDPA data residency for identity documents in Singapore) must close before Slice 1 collects the first NID.
