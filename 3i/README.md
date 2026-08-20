---
project: 3i
type: overview
status: current
updated: 2026-08-20
tags:
  - project
  - overview
---

# 3i

## Purpose

3i International Islamic Institute is a subscription learning platform delivering **self-paced and live-taught Islamic studies courses** to learners **from age five upward**.

The build is **greenfield**. No data, users, or content migrate from any earlier system — data migration is explicitly out of scope (§23 item 1).

Because the learner base includes young children, age is not a profile attribute here. It determines whether an account may exist at all, who may enrol, who may speak in a room, which courses may be published, and which instructors may teach them. Those rules are consolidated in [age-and-safeguarding.md](age-and-safeguarding.md) and should be read before any module work.

## Baseline

Scope is fixed by **SRD v2.0**, which supersedes `3i_2nd_phase_requirements_final.docx` v1.0 and consolidates five clarification rounds.

| | |
| :---- | :---- |
| Functional requirements | 162, across 19 requirement codes |
| Non-functional requirements | 32 |
| Explicit exclusions | 21 |
| Client dependencies outstanding | 7 (of 8 — per-seat pricing received 2026-08-20) |
| Change control | §21.3 — written approval before work begins |
| Acceptance | Per module, 10 working-day client review window. No separate UAT phase |

The document closes with: anything not described in it is not in scope.

## Commercial Model

| Item | Value |
| :---- | :---- |
| Pricing | **Two tiers, by learner age** — no flat subscription fee. Every seat, including the first, is priced by its occupant's tier ([3I-DEC-024](decisions/dec-024-two-tier-age-based-seat-pricing.md)) |
| Adult seat (18+) | AUD $9.99/month, AUD $99.99/year, GST-inclusive, auto-renewing |
| Under-18 seat | AUD $5.99/month, AUD $49.99/year, GST-inclusive, auto-renewing |
| Maximum profiles | 6 per account |
| Free trial | None |
| Payment rail | Stripe, **web checkout only** |
| Refunds | 14-day self-service on first payment; renewals at admin discretion |
| Waivers | Four fixed tiers — 25%, 50%, 75%, 100%, applied to the whole subscription across both seat tiers |

Total charge is the sum across both tiers at one billing cadence chosen for the whole account — a family with 2 adult and 2 child profiles pays AUD $31.96/month or AUD $299.96/year. A learner turning 18 reprices from the under-18 tier to the adult tier at the account's next renewal, never mid-cycle. See [modules/commerce/README.md](modules/commerce/README.md) for the full model.

The mobile apps carry **no purchase surface of any kind** — no prices, no buttons, no links, no text directing users to pay elsewhere (FR-BILL-02, NFR-15–21). §22.3 names app store rejection under Guideline 3.1.1 as the highest-uncertainty item in the plan.

## Delivery Sequence

Nine phases (§21.1):

| # | Phase | Covers |
| :---: | :---- | :---- |
| 1 | Foundation | RBAC, identity, registration, age gate, family accounts, email |
| 2 | Commerce | Stripe, seats, subscriptions, waivers, refunds |
| 3 | Catalogue | Courses, materials, Bunny integration, age filtering |
| 4 | Learning | Enrolment, progress, batches, attendance, waitlist |
| 5 | Assessment | Question bank, exams, grading, certificates |
| 6 | Communication | Chat, moderation, notifications |
| 7 | Surface | CMS, blog, SEO, reports, exports, admin panel |
| 8 | Mobile | Flutter apps, offline, store submission |
| 9 | Hardening | Accessibility, RTL QA, performance, security review |

Commerce sits second deliberately: the app store submission strategy depends on it, and store review is the least predictable part of the schedule.

## Tech Stack

| Layer | Choice |
| :---- | :---- |
| Backend | Node.js |
| Database | PostgreSQL |
| Cache, queues, WebSocket adapter | Redis |
| Web | Next.js |
| Mobile | Flutter |
| Video | Bunny Stream, Sydney primary |
| Object storage | DigitalOcean Spaces |
| Email | AWS SES (Sydney) / Resend |
| Payments | Stripe |
| Hosting | DigitalOcean SYD1, containerised, load-balanced |

All data resident in Sydney (NFR-07).

## Capacity Baseline

| Metric | Launch | Month 12 |
| :---- | ----: | ----: |
| Registered accounts | 500 | 5,000 |
| Active subscribers | 200 | 2,000 |
| Peak concurrent users | 100 | 500 |
| Instructors | 20 | 100 |
| Published courses | 30 | 200 |
| Video library | 100 h | 400 h |

Materially higher usage changes infrastructure sizing (§22.1).

## Compliance Posture

Australian Privacy Act 1988 and the Australian Privacy Principles; GDPR where EU or UK learners enrol; WCAG 2.2 Level AA on public and learner-facing web; Apple and Google store policies under the multiplatform services model. A written social media minimum age self-assessment is a project deliverable, to be reviewed by the client's lawyer and re-run whenever social features change (NFR-27).

## Entry Points

| To understand | Start at |
| :---- | :---- |
| The rules governing children | [age-and-safeguarding.md](age-and-safeguarding.md) |
| How this project's documentation is organised | [project-standards.md](project-standards.md) |
| Why the system is built the way it is | [decisions/README.md](decisions/README.md) |
| What is still unresolved | [open-questions.md](open-questions.md) |
| Repository-wide documentation rules | [/documentation-standards.md](/documentation-standards.md) |

## Provenance

The client supplied **no written material**. Requirements were gathered verbally and expanded by us into SRD v2.0. There is therefore no `reference/source-of-truth/` folder for this project, and there will not be one unless the institute supplies something in writing.

SRD v2.0 is filed under `reference/baseline/` — vendor-authored, client-approved, change-controlled. See [project-standards.md](project-standards.md#input-kinds) for why that category exists.

Approval of the baseline is **verbal only**. Under the repository standard, verbal agreements have no standing until written into a document here.
