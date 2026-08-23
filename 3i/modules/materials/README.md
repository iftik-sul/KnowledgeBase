---
project: 3i
module: materials
type: overview
status: current
updated: 2026-08-23
id: 3I-MTL-OVW-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - module
  - overview
---

# Materials

The module that gets a course's actual content — video, documents, audio, external links — in front of a learner safely, tracks how much of it they've consumed, and protects it against casual redistribution on mobile.

**Module status: complete.** README, data model, requirements, and the full UI stage are written.

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| MAT | Course materials and video delivery | 15 |

One existing decision applies directly: [3I-DEC-004](/3i/decisions/dec-004-bunny-stream-video-hosting.md) (Bunny Stream selected for video hosting). No new decisions were needed to scaffold this module — the baseline is unusually prescriptive here (§9.1–9.2 name specific mechanisms: TUS resumable upload, HLS, Keychain/Keystore, `FLAG_SECURE`), leaving little that's genuinely undecided.

## What This Module Owns, and What It Doesn't

**Owns:** the `Material` record itself (video, document, audio, external link, ordered within a course), per-material consumption tracking for video/audio/document (`MaterialProgress`), the Bunny Stream integration for video, and the mobile offline-download protection scheme.

**Does not own:**

- The **Course** a material belongs to — that's `catalogue`, a real reference.
- **Quiz/exam completion**, despite FR-CERT-03 listing it alongside video/audio/document completion. A submitted exam attempt already carries its own submitted state in `assessment`'s `ExamAttempt` record — duplicating that as a `MaterialProgress` row here would create two sources of truth for the same fact. See [data-model.md](data-model.md#quizexam-completion-is-not-a-materialprogress-row).
- **Course-level progress** ("this learner is 60% through this course") — that's an aggregation over enrolment and every material/exam in the course, `learning-delivery`'s concern, computed there.

## The Access Model

Video is served exclusively through short-expiry signed Bunny Stream token URLs (FR-MAT-05) — no permanent URL is ever exposed. [3I-DEC-004](/3i/decisions/dec-004-bunny-stream-video-hosting.md) is explicit that this **must be tested against the learner-context rule** ([3I-DEC-001](/3i/decisions/dec-001-learner-as-unit-of-study.md)), not session identity: a token grants access on behalf of a specific **Learner's** enrolment and entitlement, not merely "any profile under this logged-in account." An authorisation failure here is a signing failure, and the thing being authorised is a learner, not a session.

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-MTL-DM-001 | current |
| [requirements/mat-course-materials-and-video-delivery.md](requirements/mat-course-materials-and-video-delivery.md) | 3I-MTL-REQ-001 | current |
| [ui/README.md](ui/README.md) | 3I-MTL-UI-000 | current — 5 screens, matrix, components, validation rules |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| Bunny Stream as video provider, and the learner-context signing rule | [3I-DEC-004](/3i/decisions/dec-004-bunny-stream-video-hosting.md) |
| Age tagging and catalogue filtering (a course's age tag governs who can reach its materials at all) | [age-and-safeguarding.md](/3i/age-and-safeguarding.md#4-course-age-tagging), `catalogue` |
| WCAG 2.2 AA, including captions | NFR-12, FR-MAT-06 |

## Delivery

Phase 3, Catalogue (§21.1) — the baseline's phase table groups `catalogue` and `materials` together even though they're separate modules here; see [project-standards.md](/3i/project-standards.md#modules) for the partition rationale.

## Open Against This Module

| Item | Note |
| :---- | :---- |
| Document completion: continuous 30s view vs. cumulative across sessions | FR-CERT-03 says "opened in the viewer for ≥30 seconds" without specifying continuous-vs-cumulative. Modelled as continuous (a single viewing session reaching 30s), the more literal reading — flagged, not confirmed |

**Resolved 2026-08-23:** the enrolment/entitlement check gating video and offline access, and the quiz/exam completion feed for certificates, were both originally forward-referenced here pending `learning-delivery` and `assessment`. Both now exist and are real references — see [data-model.md](data-model.md#forward-references).

## Change Requests Owed to the Client

None. Nothing in this module amends or reverses the baseline; §9 is followed as written.