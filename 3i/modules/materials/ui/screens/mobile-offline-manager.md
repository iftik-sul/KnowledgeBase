---
project: 3i
module: materials
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-MTL-UI-005
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - materials
  - mobile
  - offline
---

# Screen: Mobile Offline Manager

Satisfies: FR-MAT-08, FR-MAT-10, FR-MAT-11, FR-MAT-12, FR-MAT-13, FR-MAT-14, FR-MAT-15

---

## Purpose

**Mobile only** — the one screen in this module with no web equivalent. Manage what's downloaded for offline viewing: see current downloads against the 20-item cap, remove items, see revalidation status.

## Access Gate

Mobile (Flutter) only. Member with a qualifying enrolment, checked directly against `learning-delivery`'s `Enrolment` record.

## Contents

A list of every current `OfflineDownload` on this device: material title, course, download date, size, and a countdown or status against the **7-day revalidation window** (FR-MAT-13) — so a learner about to lose connectivity for an extended trip can see which downloads are close to needing revalidation, rather than discovering a wipe after the fact with no warning.

**Usage summary**: "14 of 20 offline items used," visible at the top — the same "show the formula, not just the current number" principle [Device Management](/3i/modules/identity-and-access/ui/screens/device-management.md) already applies to the seat-linked device allowance, reused here for the offline-item cap.

**Remove** on any item deletes it immediately and permanently from the device sandbox (FR-MAT-10) — re-downloading later is a fresh download, not a restore.

## Behaviour

**Downloads are initiated from [Video Player](video-player.md) or the audio equivalent within [Document / Audio Viewer](document-audio-viewer.md)**, not from this screen — this screen is management-only, not a browse-and-download catalogue of its own.

**Encryption and in-memory-only decryption are invisible to the learner** (FR-MAT-10, FR-MAT-11) — nothing on this screen exposes key material, file paths, or any technical detail of the protection scheme; it just works, and the screen's job is showing *what's* downloaded, not *how* it's protected.

**Screen capture blocking** (FR-MAT-14) applies during playback of a downloaded item exactly as it does during streaming — `FLAG_SECURE` on Android, capture detection with video blanking on iOS — and has no visible UI on this management screen itself; it's a playback-time behaviour, documented here for completeness since FR-MAT-14 sits in the same §9.2 cluster as everything else this screen manages.

**A wipe triggered by revalidation failure, subscription lapse, or device de-authorisation** removes the affected item(s) from this list the next time the app opens with network access — the learner sees the item simply gone, with a brief explanatory notice ("Removed — your access needs to be reconfirmed online") rather than silence, since silent disappearance would read as a bug rather than the intended protection behaviour.

## Role Variations

Member only — offline download is a learner-consumption feature, not something an instructor does with their own course's content.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).