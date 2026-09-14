---
project: OstadLagbo
type: standard
status: current
updated: 2026-09-14
tags:
  - standard
  - meta
---

# OstadLagbo Project Standards

This document declares how OstadLagbo applies the repository's [documentation standards](/documentation-standards.md): what a module means here, the derivation chain, project-specific document types, and the one declared exception. Everything not declared here follows the base standards.

## What a module means in this project

A module is a **functional area** of the platform. OstadLagbo partitions by functional area because a single feature (e.g., map discovery) serves both user roles; partitioning by user group would duplicate most rules across Ostad and Shagred folders.

Modules:

| Module | Abbrev. | Covers |
|---|---|---|
| `registration-and-verification` | REG | Role selection, phone/email verification, account creation for both roles, onboarding, identity-document submission, language preference |
| `ostad-profile` | OSP | The Ostad profile: personal info, skills, education, experience, portfolio, statistics, visibility pause, insights |
| `shagred-profile` | SGP | The Shagred profile: account basics, address, Ostad history, and its strict visibility rules |
| `map-discovery` | MAP | Location capture (GPS/manual pin), map browsing, nearby search, filters, favorites, share links, profile viewing |
| `contact-and-offers` | OFR | Shagred→Ostad contact, offer lifecycle, take/decline, chat, contact reveal, inboxes |
| `admin-review` | ADM | Verification queue, approval workflow, verified badge, moderation incl. termination, admin panel, analytics, broadcasts, audit |
| `ratings-and-trust` | RNT | Ratings, replies, reporting, blocking |
| `support` | SUP | In-app help: Help & Support screen, categorized ticket threads, suspension appeals; tickets handled in the admin panel (ADM-22) |

Shagred **account creation** (phone, password, OTP) is documented in `registration-and-verification`; the Shagred **profile** — its fields, Ostad history, and who may view it — is documented in `shagred-profile`. Module folders are created when their first document exists.

## Derivation chain

```
reference/baseline/  →  requirements/  →  data-model/ + api/  →  ui/
```

- `baseline/` — founder-approved scope specification, and founder-approved **seed data** (skill categories, `OL-SKC`), both under the same version-and-supersede change control.
- `requirements/` — what each module must do, with acceptance criteria.
- `data-model/` and `api/` — entities and endpoint contracts derived from requirements. Both cite the requirements document as `derived_from`. The cross-cutting [Data Model Overview](/OstadLagbo/data-model-overview.md) at project root declares conventions, the entity ownership map, and the authorization model.
- `ui/` — screen specifications derived from requirements (and citing relevant data-model/api documents where behavior depends on them). The ui layer also covers the public website (CL-020).

`derived_from` cites the immediate parent, per base standards.

## Architecture decisions

Technical decisions that bind the build — platform, hosting, framework-level choices — are recorded as **architecture decision records** in `decisions/` (base type `decision`, ID prefix `OL-DEC`). An accepted ADR is immutable; it is changed only by a later ADR that names it as superseded. ADR-001 fixes the platform stack; all api and ui documents assume it.

## Input kinds in this project

There is no external client. The founder is author and approver in one.

- `reference/baseline/` — specifications and seed data written and approved by the founder. `approval: written` when confirmed in a committed document or explicit written sign-off; changes go through change control (new version file, old one `status: superseded`).
- `reference/discovery/` — research capture (interviews, market findings, dated decision notes) when it exists; notes are superseded by the documents that absorb them.
- `reference/source-of-truth/` — **not used.** There is no client-supplied material in this project, and founder-authored documents are never filed here, per base standards.

## Project-specific document types

Declared in addition to the base types:

| Type | Purpose | Lives in |
|---|---|---|
| `charter` | Formal project authorization | `governance/` |
| `stakeholder-register` | Stakeholders, influence, engagement strategy | `governance/` |
| `risk-register` | Identified risks, impact, mitigation, owner | `governance/` |
| `change-log` | Record of scope/baseline change decisions | `governance/` |
| `retention-policy` | Data retention and deletion rules | `governance/` |
| `privacy-policy` | User-facing privacy disclosure (PDPA 2026) | `governance/` |
| `terms-of-service` | User-facing platform terms | `governance/` |
| `incident-response` | Safety, breach, and crisis handling process | `governance/` |
| `build-plan` | Sequencing of approved scope into build slices with gates | `governance/` |
| `glossary` | Canonical term definitions for the whole project | project root |

User-facing legal documents (`privacy-policy`, `terms-of-service`) carry a `legal_review` frontmatter field (`pending` until reviewed by a Bangladesh-qualified lawyer). Dated planning reviews use the base `meeting-note` type with a `planning-review` tag. Non-functional requirements use the base `requirements` type at project root (`OL-NFR-001`), since they cut across every module rather than belonging to one.

## Declared exception: `governance/`

OstadLagbo adds a top-level `governance/` folder for project-management lifecycle documents (charter, stakeholder register, risk register, change log, policies, build plan, planning reviews, status reports). These are neither input material (`reference/`) nor development documentation (`modules/`), so the base structure has no home for them. Governance documents are editable, carry full frontmatter, and are authoritative for project authority, process, and policy — never for implementation, which remains `modules/`.

## Document IDs

Project abbreviation: **OL**. Format per base standards: `OL-<MODULE>-<TYPE>-<NNN>` using the module abbreviations above. Governance and other cross-cutting documents omit the module segment (e.g., `OL-CHR-001`, `OL-RET-001`, `OL-BLD-001`, `OL-NFR-001`, `OL-GLS-001`, `OL-DEC-001`, `OL-SKC-001`).

## AI agent notes

A development AI works from `modules/` with `status: current`, answers scope questions from `reference/baseline/` read together with the change log's pending entries, **builds on the stack fixed in `decisions/adr-001-platform-architecture.md`** (Supabase, Render, Vercel, FCM — free tiers through development), builds in the slice order of `governance/build-sequence.md`, honors `non-functional-requirements.md` for every module, loads seed data from `reference/baseline/skill-categories-v1.0.md`, resolves undefined terms via `glossary.md`, and treats `governance/` as context about authority, process, and policy. Access-control implementation follows the authorization model in `data-model-overview.md`: the policy layer lives in the Render API, with Supabase row-level security mirroring it as a second line of defense. Retention behavior in data models and tooling must honor `governance/data-retention-policy.md`. Generated code is reviewed at every slice gate (risk R-11). Gaps are raised, never invented, per the base AI guidelines.
