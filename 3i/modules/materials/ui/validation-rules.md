---
project: 3i
module: materials
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-MTL-UI-VAL
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - validation
---

# Materials — Validation Rules

Field-level and upload-level validation shared across two or more materials screens.

---

## Upload Size Limits

On [Material upload / manage](screens/material-upload-manage.md): video 4 GB, audio 500 MB, document 100 MB, image (thumbnails) 10 MB (FR-MAT-02). Enforced client-side (immediate feedback, no wasted upload time) **and** server-side (the actual control — client-side checks are UX, not security).

## File Type Validation

Server-side content inspection, not extension matching (FR-MAT-03). The upload UI shows a generic "file type not supported" message on rejection rather than exposing inspection details — not a baseline requirement, standard practice to avoid handing a would-be attacker a map of what the validator checks for.

## Caption Requirement

On [Material upload / manage](screens/material-upload-manage.md): a video upload cannot be marked ready for publish without an attached English caption file, or admin's paid auto-transcription fallback having run (FR-MAT-06). The upload flow should surface this **before** the (potentially very long) video upload completes, not after — asking an instructor to upload a 3 GB video and only then telling them captions are missing wastes real time and bandwidth on a mistake that was knowable up front.

## Video Upload — Resumable

Video uploads use the TUS protocol (FR-MAT-02). A connection drop mid-upload resumes from the last confirmed chunk on retry, not from zero — the UI should reflect actual resume behaviour (showing progress picking back up near where it left off) rather than a naive restarted progress bar, since a naive bar would misrepresent what TUS is actually doing underneath.