---
project: 3i
module: materials
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-MTL-UI-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - materials
  - video
---

# Screen: Video Player

Satisfies: FR-MAT-04, FR-MAT-05, FR-MAT-06, FR-MAT-07, FR-MAT-08

---

## Purpose

Stream a video material via a short-expiry signed Bunny Stream URL, tracking cumulative watch progress.

## Access Gate

Member with a qualifying enrolment (forward-referenced, fails closed — see [ui/README.md](README.md#blocked)). **The signed URL is issued per learner, not per session** — [3I-DEC-004](/3i/decisions/dec-004-bunny-stream-video-hosting.md): a failure here is a signing failure tied to the active learner profile's entitlement, not a generic "are you logged in" check.

## Contents

Adaptive-bitrate HLS playback (FR-MAT-04), [Caption Toggle](../components.md#caption-toggle) defaulting on (FR-MAT-06), standard playback controls, and a [Progress Indicator](../components.md#progress-indicator) reflecting cumulative watch percentage.

**No download button anywhere on web** (FR-MAT-07) — not hidden behind a permission check, structurally absent from the web build. On mobile, a download affordance appears instead, leading into the offline-protection flow — see [Mobile Offline Manager](mobile-offline-manager.md).

## Behaviour

Progress is reported to `MaterialProgress` continuously during playback (not only at video end), so a learner closing the app mid-video doesn't lose progress toward the 90% cumulative threshold (FR-CERT-03). **Progress never decreases** — rewatching from the start doesn't reset a percentage already earned; the stored value is a high-water mark, cumulative across all sessions.

Signed URLs expire quickly (exact duration is Bunny Stream's own token-expiry configuration, not specified in the baseline) — a long-paused video may need to silently re-request a fresh signed URL on resume rather than surfacing an error to the learner for what is, from their perspective, normal behaviour.

## Role Variations

**Member:** full playback with progress tracking.
**Instructor:** preview access to their own course's videos, no progress tracked (an instructor previewing their own content isn't "completing" it in the FR-CERT-03 sense).

## Contrast and RTL

Standard, 4.5:1 (NFR-12) — player controls must clear contrast against the video itself, which the player cannot control, so controls need a scrim or solid background behind them rather than relying on contrast against arbitrary video content. Full RTL mirroring (FR-LOC-04) for surrounding chrome; the video content itself does not mirror.