---
project: 3i
type: standard
status: current
updated: 2026-08-23
tags:
  - standard
  - meta
---

# 3i Project Standards

This document declares 3i's vocabulary under the repository-wide rules in [/documentation-standards.md](/documentation-standards.md). Where the two differ, the repository standards win.

The module partition was settled on 2026-08-18. Document IDs may now be assigned from the table below.

---

## Input Kinds

3i has no `reference/source-of-truth/`. The client supplied nothing in writing — the entire requirement set was gathered verbally and expanded by us. Creating the folder would breach the repository rule against empty folders and imply evidence that does not exist.

SRD v2.0 is not source of truth and is not discovery either. It is our document, but it is also the fixed, change-controlled baseline that defines scope. It lives in:

```
reference/baseline/
```

Vendor-authored, client-approved, frozen, versioned. Corrections go through §21.3 change control, not through edits. A superseded version keeps `status: superseded` and stays in place.

This category is repository-wide, not a 3i quirk — see `/documentation-standards.md`.

---

## Derivation Chain

```
reference/baseline/  →  modules/  →  ui/  →  implementation-spec
```

The baseline is the parent of every requirement document. Nothing sits above it. `implementation-spec` documents sit last in the chain — they translate an already-settled module (requirements plus any amending decisions) into build detail for a developer, and cite the requirements/UI documents they implement rather than restating them.

---

## Requirement Numbering

**The SRD's requirement codes are canonical.** Format is `FR-<CODE>-<nn>` — `FR-AUTH-03`, `FR-CHAT-07`, `FR-BILL-02` — and `NFR-<nn>` for non-functional requirements, which are unprefixed and run in a single series to 32.

A requirement number is never reassigned, renumbered, or reused, including after deprecation. When a requirement is split across documents, every resulting file carries the original code.

This matters more here than elsewhere: the SRD is client-facing. A code quoted in a client meeting and a code in this repository must mean the same thing.

Requirements proposed by us with no SRD entry take a `P-nn` number in a project-wide proposed list, exactly as RERAN handles proposed services. They enter the `FR-` series only when the client accepts them and the SRD is revised under §21.3.

### The 19 Requirement Codes

| Code | Area | Count |
| :---- | :---- | ----: |
| AUTH | Registration and authentication | 13 |
| FAM | Family accounts and learner profiles | 10 |
| RBAC | Roles and permissions | 5 |
| INST | Instructor onboarding | 7 |
| CRS | Course catalogue and management | 12 |
| MAT | Course materials and video delivery | 15 |
| BAT | Batches and live sessions | 7 |
| ENR | Enrolment, waitlist and age gating | 7 |
| QB | Question bank | 7 |
| EX | Examinations | 8 |
| CERT | Certificates | 9 |
| BILL | Subscriptions and billing | 8 |
| WAV | Waivers | 9 |
| REF | Refunds | 5 |
| CHAT | Group chat and moderation | 15 |
| NOT | Notifications | 8 |
| CMS | Content management and public site | 7 |
| REP | Reports and exports | 5 |
| LOC | Localisation | 6 |

**Note, 2026-08-23:** the CRS count above (12) does not match a direct count against SRD v2.0 §8.2, which defines FR-CRS-01 through FR-CRS-11 — 11 requirements. Left as originally recorded here rather than silently changed, since this table's numbers were set at module-partition time (2026-08-18) as a planning estimate, not verified line-by-line against the baseline at that point. The correct figure, used in [modules/catalogue/README.md](modules/catalogue/README.md), is **11**. Correcting the value below rather than leaving two contradictory counts in the repository.

---

## Modules

A module in 3i is a **functional area** owning one or more requirement codes. The code in an ID stays the SRD's; the folder is ours.

Settled 2026-08-18. Thirteen modules, covering all 19 requirement codes and the 32 NFRs.

| Module | Abbrev. | Owns | FRs |
| :---- | :---: | :---- | ----: |
| `identity-and-access` | IDA | AUTH, RBAC, FAM | 28 |
| `communication` | CMN | CHAT, NOT | 23 |
| `commerce` | CMR | BILL, WAV, REF | 22 |
| `materials` | MTL | MAT | 15 |
| `assessment` | ASM | QB, EX | 15 |
| `learning-delivery` | LDL | BAT, ENR | 14 |
| `catalogue` | CAT | CRS | 11 |
| `certification` | CRT | CERT | 9 |
| `instructors` | INS | INST | 7 |
| `public-site` | PUB | CMS | 7 |
| `localisation` | LCL | LOC | 6 |
| `reporting` | RPT | REP | 5 |
| `platform` | PLT | — | 32 NFRs |

**Module abbreviations are a separate namespace from requirement codes.** `MTL` is the module; `MAT` is the requirement code it owns. None of the thirteen abbreviations collides with any of the nineteen codes, deliberately — a document ID and a requirement code appearing in the same sentence must be unambiguous.

**Total check, added 2026-08-23:** summing this table's FR column (28+23+22+15+15+14+11+9+7+7+6+5) gives **162**, matching the total functional-requirement count stated in [3i/README.md](/3i/README.md#baseline). Before the CRS correction above, the table summed to 163 — one more than the documented total — which is what surfaced the miscount.

### Reasoning

Three calls worth recording, because a later reader will otherwise wonder:

1. **AUTH, RBAC and FAM merged into one module.** §3 of the baseline is titled "read this first" and defines Account and Learner as a single model. Splitting it across folders would fracture the thing the baseline says governs every other section. This is the largest module at 28 requirements, and that is correct — it is the load-bearing one.
2. **CMS and REP kept apart** despite both feeling administrative. A public SEO site and admin analytics share no entities. Merging them would create exactly the junk drawer this document warns against.
3. **LOC as its own module** rather than a cross-cutting note. FR-LOC-04 requires full RTL layout mirroring across web and both mobile apps, which needs real UI documentation rather than a paragraph in an NFR file.

### `platform`

Holds what genuinely belongs to no functional area: the 32 NFRs, deployment topology, capacity baseline (§20.2), and integration contracts for Stripe, Bunny Stream, and AWS SES.

It is not a drawer for anything hard to place. A document that could live in a real module belongs in that module.

### Not a partition

The delivery phases in §21.1 are **not** a partition. They are temporal, and Hardening is not a subsystem. Documentation is never organised by phase.

---

## Module Folder Shape

```
modules/<module-name>/
├── README.md                    # module index
├── data-model.md                # entities owned by this module
├── backend-spec.md              # optional — implementation-spec type, added once build begins
├── requirements/
│   └── <code>-<n>.md
└── ui/
    ├── README.md                # role × screen matrix
    ├── components.md
    ├── validation-rules.md
    └── screens/
        └── <screen-name>.md
```

A module is not required to have every stage.

Entities are documented in the module that **owns** them, once. A module that reads another module's entity links to it rather than restating its fields.

---

## The `ui/` Stage

Screens and requirements cross — a screen such as Checkout or Video Player serves several requirements.

1. **One file per distinct screen.** Never one file per role-screen pair.
2. **Role differences go inside the screen file**, under `## Role Variations`.
3. **Shared logic documented once** and linked — `components.md`, `validation-rules.md`.
4. **`ui/README.md` carries the role × screen matrix**, which is what makes a missing screen visible.
5. **Screens cite the requirement codes they satisfy**, and requirement documents list the screens realising them.
6. **`figma:` frontmatter** records the design generated from a screen file.

### Accessibility

NFR-12 requires WCAG 2.2 Level AA with 4.5:1 contrast. Every screen document states its contrast pairs explicitly. A near-black background carrying navy text shipped once on this project and was caught late — contrast belongs in the specification, where it is reviewable, not in the design tool, where it is discovered.

RTL is not a rendering concern. FR-LOC-04 requires navigation, alignment, icon direction, and progress indicators to mirror for Arabic and Urdu. Every screen document states its RTL behaviour.

---

## Cross-Cutting Documents

Some rules span every module. They are documented **once**, at project root, and linked — never restated, because restated rules go stale silently.

| Document | Why it cannot live in a module |
| :---- | :---- |
| [age-and-safeguarding.md](age-and-safeguarding.md) | Age rules sit in AUTH, FAM, CRS, ENR, CHAT and INST simultaneously |
| [app-store-compliance.md](app-store-compliance.md) | The no-purchase-surface rule spans BILL, NOT and the NFRs at once |
| [decisions/](decisions/README.md) | The consequential decisions constrain several modules at once |
| [open-questions.md](open-questions.md) | Tracks unresolved items across the whole project |

**On app store compliance.** FR-BILL-02 forbids any purchase surface in the apps, FR-NOT-06 forbids purchase prompts in push notifications, and NFR-15 through NFR-21 govern the multiplatform-services submission model, registration being web-first, and the 13+ age rating. That is one rule enforced in three modules — `commerce`, `communication`, and `platform` — and §22.3 names store rejection under Guideline 3.1.1 as the highest-uncertainty item in the plan. It is now written — see [app-store-compliance.md](app-store-compliance.md).

---

## Additional Document Types

| Type | Purpose |
| :---- | :---- |
| `functional-requirement` | A group of SRD requirements for one module, with acceptance criteria |
| `compliance` | Analysis of a legal or platform-policy constraint and what it forces |
| `integration` | Contract with a third-party service — Stripe, Bunny Stream, SES |
| `implementation-spec` | Developer-facing build detail for one module — schema, endpoints, middleware. Sits below `requirements` and `ui-spec` in the derivation chain: it translates *what* a module must do into *how* it is built, and cites the requirements/decisions it implements rather than restating them. First used in [3I-IDA-IMPL-001](modules/identity-and-access/backend-spec.md) |

---

## File Naming

| Location | Pattern | Example |
| :---- | :---- | :---- |
| `reference/baseline/` | `srd-v<version>.md` | `srd-v2.0.md` |
| `requirements/` | `<code>-<n>.md` | `chat-moderation.md` |
| `ui/screens/` | `<screen-name>.md` | `checkout.md` |
| `decisions/` | `dec-NNN-<n>.md` | `dec-001-learner-as-unit-of-study.md` |
| module root, `implementation-spec` | `backend-spec.md` (or `frontend-spec.md` when written) | `3i/modules/identity-and-access/backend-spec.md` |

---

## Document IDs

**Format:** `3I-<MODULE>-<TYPE>-<NNN>` — for example, `3I-IDA-REQ-001`, `3I-CMN-UI-004`, `3I-IDA-IMPL-001`.

Numbers are assigned sequentially within a project-module-type combination and are never reused, even after deprecation. An ID does not change when a file is renamed or moved.

Cross-cutting documents omit the module segment: `3I-DEC-001`. A cross-cutting decision has no single module, and inventing one to satisfy the format would misfile it permanently.

---

## Decisions

A decision is never edited to reflect a change of mind. A reversed decision gets `status: superseded` and a new file citing it under `supersedes`.

---

## Exceptions

| Exception | Reason |
| :---- | :---- |
| No `reference/source-of-truth/` | The client supplied nothing in writing. Verified 2026-08-18, not assumed. |
| `reference/baseline/` | New input kind — vendor-authored, client-approved, change-controlled. Now repository-wide. |
| Project-root cross-cutting documents | Rules spanning six modules belong in none of them. RERAN sets the precedent with `module-roadmap.md`. |