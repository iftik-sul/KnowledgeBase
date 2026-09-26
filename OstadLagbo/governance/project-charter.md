---
project: OstadLagbo
type: charter
status: current
updated: 2026-09-26
id: OL-CHR-001
approved: 2026-08-28
owner: Iftikher
---

# Project Charter — Ostad Lagbo (ওস্তাদ লাগবো)

## Purpose and justification

People in Bangladesh find skill teachers through Facebook groups, scattered phone numbers, and word of mouth. Proximity is hard to establish, credibility is unverifiable, trust is guesswork, and skilled people have no structured way to be discovered. Ostad Lagbo addresses this with a map-first marketplace: a learner (Shagred) discovers verified experts (Ostads) nearby, reviews evidence-rich profiles, and connects directly. The platform handles discovery and trust; the participants handle their own arrangements.

## Measurable objectives (MVP)

1. Ostads can register, verify identity, and become discoverable on a map.
2. Shagreds can find, evaluate, and contact Ostads and make offers.
3. A functioning admin verification process protects marketplace quality.
4. Success at MVP = a live funnel from discovery → profile view → contact → accepted offer, in at least one launch area.

## High-level scope

| In scope | Out of scope |
|---|---|
| Registration for both roles (verified phone; optional verified email) | Payments, banking, payouts |
| Verified Ostad profiles: identity, skills, education, experience, portfolio | Platform-set or stored pricing |
| GPS and manual map-pin location for Ostads | Availability calendars and bookings |
| Map-based nearby discovery and full profile viewing | Platform-managed teaching location after discovery |
| Shagred→Ostad contact and offers; Ostad take/decline | Preference matching |
| Admin verification, approval, verified badge | |
| Ratings, reviews, profile statistics | |

The detailed, change-controlled scope definition lives in `reference/baseline/` (currently baseline v1.2, frozen 2026-09-25); this table is the charter-level summary.

## Stakeholders and governance

Sponsor, project manager, and product owner: **Iftikher** (sole founder), holding full authority over scope, budget, and approvals. Future stakeholders (users, admins, team members, partners) are tracked in the [Stakeholder Register](/OstadLagbo/governance/stakeholder-register.md).

## High-level risks

1. **Supply-side cold start** — an empty map is a dead marketplace; supply must be seeded before demand is opened.
2. **Sensitive identity data** — NID/passport images and selfies require careful storage, access control, and retention policy.
3. **Trust and safety** — the platform facilitates in-person meetings between strangers.
4. **Solo-founder capacity** — single point of failure for delivery and operations.

Risks are tracked in the [Risk Register](/OstadLagbo/governance/risk-register.md).

## Summary milestones

Charter approval → planning documentation complete → MVP build → supply seeding → soft launch → public launch. Dates are set in the schedule and milestone plan, still to be produced (a standing execution item).

## Budget

Still to be produced; ADR-001's phased cost model ($0 through development, ≈ $52/month + SMS from the first real user — rising to **≈ $72–82/month** once map tiles become a paid line at soft launch, or staying at ≈ $52 if Google's free mobile SDK is chosen; ADR-001 amendment, CL-035) is the infrastructure input. Working assumption: solo, bootstrap.

## Approval

Approved by Iftikher (sponsor), 2026-08-28.
