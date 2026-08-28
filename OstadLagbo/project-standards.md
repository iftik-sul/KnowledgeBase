---
project: OstadLagbo
type: standard
status: current
updated: 2026-08-28
tags:
  - standard
  - meta
---

# OstadLagbo Project Standards

This document declares how OstadLagbo applies the repository's [documentation standards](/documentation-standards.md): what a module means here, the derivation chain, project-specific document types, and the one declared exception. Everything not declared here follows the base standards.

## What a module means in this project

A module is a **functional area** of the platform. OstadLagbo partitions by functional area because a single feature (e.g., map discovery) serves both user roles; partitioning by user group would duplicate most rules across Ostad and Shagred folders.

Planned modules:

| Module | Abbrev. | Covers |
|---|---|---|
| `registration-and-verification` | REG | Role selection, phone/email verification, onboarding, identity-document submission |
| `ostad-profile` | PRO | The Ostad profile: personal info, skills, education, experience, portfolio, statistics |
| `map-discovery` | MAP | Location capture (GPS/manual pin), map browsing, nearby search, profile viewing |
| `contact-and-offers` | OFR | Shagred→Ostad contact, offer lifecycle, take/decline, communication handoff |
| `admin-review` | ADM | Verification queue, approval workflow, verified badge, moderation |
| `ratings-and-trust` | TRU | Ratings, reviews, trust signals, profile completion, safety reporting |

Module folders are created when their first document exists.

## Derivation chain

```
reference/baseline/  →  requirements/  →  data-model/ + api/  →  ui/
```

- `baseline/` — founder-approved scope specification.
- `requirements/` — what each module must do, with acceptance criteria.
- `data-model/` and `api/` — entities and endpoint contracts derived from requirements. Both cite the requirements document as `derived_from`.
- `ui/` — screen specifications derived from requirements (and citing relevant data-model/api documents where behavior depends on them).

`derived_from` cites the immediate parent, per base standards.

## Input kinds in this project

There is no external client. The founder is author and approver in one.

- `reference/baseline/` — specifications written and approved by the founder. `approval: written` when confirmed in a committed document or explicit written sign-off; changes go through change control (new version file, old one `status: superseded`).
- `reference/discovery/` — research capture (Phase-1 interviews, market findings) when it exists.
- `reference/source-of-truth/` — **not used.** There is no client-supplied material in this project, and founder-authored documents are never filed here, per base standards.

## Project-specific document types

Declared in addition to the base types:

| Type | Purpose | Lives in |
|---|---|---|
| `charter` | Formal project authorization | `governance/` |
| `stakeholder-register` | Stakeholders, influence, engagement strategy | `governance/` |
| `risk-register` | Identified risks, impact, mitigation, owner | `governance/` |
| `change-log` | Record of scope/baseline change decisions | `governance/` |

## Declared exception: `governance/`

OstadLagbo adds a top-level `governance/` folder for project-management lifecycle documents (charter, stakeholder register, risk register, change log, status reports). These are neither input material (`reference/`) nor development documentation (`modules/`), so the base structure has no home for them. Governance documents are editable, carry full frontmatter, and are authoritative for project authority and process — never for implementation, which remains `modules/`.

## Document IDs

Project abbreviation: **OL**. Format per base standards: `OL-<MODULE>-<TYPE>-<NNN>` using the module abbreviations above. Governance and other cross-cutting documents omit the module segment (e.g., `OL-CHR-001`).

## AI agent notes

A development AI works from `modules/` with `status: current`, answers scope questions from `reference/baseline/`, and treats `governance/` as context about authority and process. Gaps are raised, never invented, per the base AI guidelines.
