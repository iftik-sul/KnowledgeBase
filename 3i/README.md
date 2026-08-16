---
project: 3i
type: overview
status: current
updated: 2026-08-16
tags:
  - project
  - overview
---

# 3i

## Purpose

3i (3i International Islamic Institute) is a subscription-based learning management system (LMS) delivering a general academic curriculum — sciences, humanities, and professional subjects — within an Islamic institutional identity.

The platform serves a broad learner base that includes minors. Minors are reached through **guardian-held accounts carrying learner profiles**, not through direct registration, which shapes identity, communication, and billing throughout the system.

This engagement is a rebuild of an existing platform, not a greenfield build.

## Status

Active development, approximately three weeks in as of 2026-08-16.

| Area | State |
| :---- | :---- |
| Requirements | SRD v2.0 complete — ~130 numbered functional requirements, acceptance criteria, NFRs, scope exclusions, risk register |
| Backend | Complete against the milestone plan current at the time of writing |
| Frontend | Screen development underway; designs generated via Figma AI against a fixed prompt kit |
| Client review | Design direction review stage — designs are iterative, not final deliverables |

Documentation migration into this KnowledgeBase has just begun. This folder currently holds the project scaffold and decision register only; requirements and UI documentation have not yet been migrated from their working locations.

## Modules

3i partitions by **functional area**. See [project-standards.md](project-standards.md) for the module table, abbreviations, and stage folders.

> `modules/` is not yet populated. Module folders are created as their first document is written, per the repository standard on empty folders.

## Tech Stack

| Layer | Technology |
| :---- | :---- |
| Backend | NestJS, Prisma |
| Web frontend | Next.js |
| Mobile | Flutter |
| Database | PostgreSQL |
| Cache / queues | Redis |
| Video hosting | Bunny Stream |
| Payments | Stripe |
| Transactional email | AWS SES |
| Infrastructure | DigitalOcean, SYD1 region |

Rationale for the video and payment choices is recorded in [decisions/](decisions/README.md), not here — this table records what is used, not why.

## Stakeholders

| Party | Role |
| :---- | :---- |
| 3i International Islamic Institute | Client; owns curriculum, pricing, and waiver policy |
| Guardians | Account holders for learners under the age gate; billing party |
| Learners | Primary users; may be minors or independent adults |
| Instructors | Course delivery and assessment |
| Administration | Institute staff operating the platform |

## Compliance Posture

The platform is designed against Australian privacy law, COPPA, and the Apple and Google app store policies. The minor-account model and the web-only checkout model are both direct consequences of this posture and are recorded as decisions.

> A dedicated compliance analysis document has not yet been migrated into this folder.

## Entry Points

| To understand | Start at |
| :---- | :---- |
| How this project's documentation is organized | [project-standards.md](project-standards.md) |
| Why the system is built the way it is | [decisions/README.md](decisions/README.md) |
| Repository-wide documentation rules | [/documentation-standards.md](/documentation-standards.md) |

## Known Documentation Gaps

These are gaps, not omissions. Each needs source material migrated before it can be written honestly.

1. **SRD v2.0** has not been placed in `reference/discovery/`. Until it is, no module requirement document can cite a parent under `derived_from`.
2. **The nine-phase delivery sequence** is defined in the SRD but not reproduced here; phase names and ordering must be transcribed rather than reconstructed.
3. **The data model** is implemented in Prisma but not documented as entities and relationships in any module.
4. **The Figma AI Prompt Kit** exists outside the repository and has no home in this structure yet.
5. **Client clarification rounds** — the question-and-answer history behind the locked decisions — belong in `reference/discovery/` and are not yet migrated.
