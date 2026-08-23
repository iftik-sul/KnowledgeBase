---
project: 3i
module: materials
type: data-model
status: current
updated: 2026-08-23
id: 3I-MTL-DM-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - data-model
  - materials
---

# Materials — Data Model

Entities owned by this module. Other modules reference these; they do not restate them.

---

## Material

| Field | Notes |
| :---- | :---- |
| Course | FK to `catalogue` Course — real reference. Materials are ordered within a course (FR-MAT-01) |
| Type | `video`, `document`, `audio`, or `external_link` (FR-MAT-01) |
| Order | Integer, position within the course |
| Title | |
| File / URL | Type-dependent — see below |
| Caption file (video only) | **English caption file required at upload** (FR-MAT-06). Admin may trigger paid auto-transcription as a fallback where an instructor omits one |

**Type-specific storage:**

| Type | Storage | Notes |
| :---- | :---- | :---- |
| Video | Bunny Stream video ID | Transcoded to adaptive-bitrate HLS by the provider (FR-MAT-04). This module stores the Bunny-assigned ID, not the media itself |
| Document | DigitalOcean Spaces object key, private bucket | Rendered via in-browser viewer only — never a direct download link (FR-MAT-07) |
| Audio | DigitalOcean Spaces object key, private bucket | Same access pattern as document |
| External link | URL | No hosting or protection — this module just stores and displays the link |

**Upload limits** (FR-MAT-02): video 4 GB, audio 500 MB, document 100 MB, image (thumbnails, etc.) 10 MB. Video upload is **resumable (TUS protocol)**, since a 4 GB upload over an unreliable connection failing at 95% and restarting from zero is the exact failure mode TUS exists to prevent.

**File type is validated server-side by content inspection** (FR-MAT-03), not by file extension or declared MIME type — an uploaded file claiming to be an MP4 by its extension is actually inspected before being accepted, since extension-based validation is trivially spoofable and this is a public-facing upload surface.

**Materials are not admin-moderated before publication** (FR-MAT-09), except indirectly through the course-level approval gate in `catalogue` (FR-CRS-04, under-13 courses). An instructor uploading a document to an already-published, non-under-13 course sees it go live immediately — there is no separate per-material review queue.

---

## MaterialProgress

| Field | Notes |
| :---- | :---- |
| Material | FK |
| Learner | FK to `identity-and-access` Learner — progress is tracked per learner, never per account (consistent with [3I-DEC-001](/3i/decisions/dec-001-learner-as-unit-of-study.md)) |
| Percent consumed | Video/audio: percentage of duration, **cumulative across sessions**, not reset on each replay (FR-CERT-03) |
| Viewer session seconds | Document: seconds the viewer has been open in the current continuous session — see the open item on continuous-vs-cumulative below |
| Completed at | Null until the type's threshold is crossed, then set once and never cleared |
| Last accessed at | |

**Completion thresholds** (FR-CERT-03), the reason this entity exists at all — certificates read from it:

| Type | Complete when |
| :---- | :---- |
| Video | ≥90% of duration watched, cumulative |
| Audio | ≥90% played, cumulative |
| Document | Opened in the viewer for ≥30 seconds |

**"Cumulative" for video/audio is explicit in the baseline** — a learner watching a 20-minute video in four 5-minute sessions across different days still reaches 100%. **Document is ambiguous** — the baseline just says "opened ≥ 30 seconds," not whether that's one continuous sitting or summed across visits. Modelled here as **continuous** (a single session reaching 30 seconds), the more literal reading of "opened ... for" — flagged in [README.md](README.md#open-against-this-module), not confirmed.

**`completedAt` is set once and never cleared or recalculated downward.** A learner who later re-watches only 10% of an already-completed video does not lose their completion — completion is a floor crossed, not a live percentage.

### Quiz/exam completion is not a MaterialProgress row

FR-CERT-03's fourth completion type — "Quiz/exam: submitted, regardless of score" — is **not modelled here**. A quiz or exam is not a `Material` record; it's owned entirely by `assessment` (QB, EX codes), and its submission state already lives on that module's `ExamAttempt` record. Certificate issuance (owned by `certification`) reads video/audio/document completion from `MaterialProgress` here, and reads quiz/exam completion directly from `assessment`'s own records — two sources for two genuinely different kinds of thing, not duplicated tracking of the same fact.

---

## OfflineDownload (Mobile Only)

| Field | Notes |
| :---- | :---- |
| Material | FK — video or audio only. Documents and external links are not offline-downloadable, since FR-MAT-08/§9.2's protection scheme is specified for video/audio, not document viewing |
| Device | FK to `identity-and-access` Device |
| Learner | FK |
| Downloaded at | |
| Last revalidated at | |
| Encryption key reference | A reference into the device's Keychain (iOS) or Keystore (Android) — **never the key itself**, which never leaves secure hardware storage (FR-MAT-10) |

**Maximum 20 offline items per device** (FR-MAT-12), enforced at download time — the 21st download is refused with a message naming the limit and offering to remove an existing item.

**Revalidates online at least every 7 days** (FR-MAT-13). On revalidation failure, subscription lapse, or device de-authorisation, the **local content is wiped** — not just marked inaccessible, actually deleted from the device sandbox. This is a background check the app performs when it has network access, not something the learner triggers manually.

**Playback decrypts in memory only** (FR-MAT-11) — no plaintext file is ever written to disk during playback, which is why this entity stores a key *reference* rather than the key, and why there is no "exported file" concept anywhere in this model.

See [requirements](requirements/mat-course-materials-and-video-delivery.md#offline-protection) for the full offline-protection requirement set, including screen-capture blocking, which has no data-model footprint (it's a client-side OS API call, not a stored fact).

---

## Forward References — Resolved (2026-08-23)

This module was originally scaffolded before `learning-delivery` existed. Both dependencies originally flagged here are now real:

| Reference | Resolved by |
| :---- | :---- |
| Video/offline access gate — "does this Learner have an active enrolment on this Material's Course" | `learning-delivery`'s `Enrolment` |
| Concurrent stream limit (FR-AUTH-12, limited to purchased seats) | `commerce` — already built when this module was scaffolded, included here for completeness since it's easy to assume this module owns stream-count enforcement when it actually just reads `commerce`'s seat count |

---

## Referenced By

| Module | Reads |
| :---- | :---- |
| `certification` | MaterialProgress — video/audio/document completion feeds attendance and completion certificate eligibility (FR-CERT-02, FR-CERT-03) |
| `learning-delivery` | Material — course-level progress aggregation reads across every Material in a course |
| `reporting` | Material, MaterialProgress — learner activity and course performance reports (FR-REP-01) |

## Referenced

| Entity | Owned by | Read here |
| :---- | :---- | :---- |
| Course | `catalogue` | Owner of every Material |
| Learner | `identity-and-access` | Subject of MaterialProgress and OfflineDownload |
| Device | `identity-and-access` | Subject of OfflineDownload; device de-authorisation triggers the local wipe |
| Subscription | `commerce` | Concurrent stream limit and offline-wipe-on-lapse both read subscription/seat status |
| Enrolment | `learning-delivery` | Video/offline access gate |