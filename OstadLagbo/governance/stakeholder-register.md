---
project: OstadLagbo
type: stakeholder-register
status: current
updated: 2026-09-26
id: OL-STK-001
owner: Iftikher
---

# Stakeholder Register

The founder currently holds every internal role. This register maps the stakeholders who exist now and those who will materialize as the project reaches research, seeding, and launch, with the engagement strategy for each.

| ID | Stakeholder | Role / interest | Influence | Interest | Engagement strategy |
|---|---|---|---|---|---|
| S-01 | Iftikher (founder) | Sponsor, project manager, product owner; sole decision-maker; author of all Bangla copy (CL-016) | High | High | Self-governance: weekly plan-vs-progress review; every decision recorded in the knowledge base |
| S-02 | Ostads (future) | Supply side — need visibility, credibility, control over offers | High — no supply, no marketplace | High | Hand-recruitment from Slice 1 in the launch-focus categories (Math/Physics/Chemistry, Spoken English, Guitar & Keyboard — OL-SKC-001); white-glove onboarding; ongoing feedback loop. The discovery sprint was declined; first recruits are the first validation |
| S-03 | Shagreds (future) | Demand side — need nearby, credible, safe choices | High | High | Invited cohort at soft launch (Slice 4); funnel monitoring via the admin panel |
| S-04 | Guardians / family | Search on behalf of learners, especially students; safety-sensitive | Medium | High | 18+ account holders act for minors (baseline); gender filter serves family-comfort dynamics (MAP-05) |
| S-05 | Admin reviewers (initially the founder) | Verify identity, approve profiles, moderate content, handle appeals | Medium | Medium | Workflow fully specified (ADM-01…22) and modeled; audit-logged so the role is transferable |
| S-06 | Future team / contractors | Design, engineering, operations help when engaged | Medium | Medium | Documentation kept hire-ready; clear specs before delegation |
| S-07 | Regulators / legal context | NID and identity-data handling under the Personal Data Protection Act, 2026 | High (compliance) | Low (passive) | Retention, privacy, ToS, and incident-response documents drafted; Bangladesh-qualified legal review before launch, including the data-residency ruling on Singapore-hosted identity documents (ADR-001 open item 1) |
| S-08 | External providers | Critical dependencies fixed by ADR-001: **Supabase** (data services), **Render** (API), **Vercel** (web), **Firebase Cloud Messaging** (push), **Cloudflare** (edge), a **Bangladesh SMS gateway** (OTP — to be selected in Slice 0), a **map tile provider** (also selected in Slice 0 — CL-035; OSM's public tiles are development-only) | Medium | Low | Free tiers through development; paid tiers from Slice 1; cost monitored via ADM-19 and provider billing alerts; portability preserved (standard PostgreSQL, portable API) |
| S-09 | Investors / partners (potential) | May fund or accelerate post-MVP | Low now | Low now | Charter and metrics kept pitch-ready; revisited post-MVP |
| S-10 | The AI development agent | Builds the platform from this knowledge base | High (delivery) | — | Held to the knowledge base as its specification; conventional stack chosen for its output quality (ADR-001); generated code reviewed at every slice gate (risk R-11) |

## Notes

S-07 acts like a stakeholder even with no person attached: identity documents are collected from day one, so legal and privacy obligations constrain design before launch. S-02 outranks everything else operationally — the supply-side cold-start risk in the charter is the engagement plan's first test. S-10 was added 2026-09-14: an unusual stakeholder, but the one whose "engagement" — the quality of this knowledge base as a specification — determines whether anything ships correctly.
