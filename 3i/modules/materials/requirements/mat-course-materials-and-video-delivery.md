---
project: 3i
module: materials
type: requirements
status: current
updated: 2026-08-23
id: 3I-MTL-REQ-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - materials
---

# Course Materials and Video Delivery

Baseline §9. Fifteen requirements, none amended by decision — [3I-DEC-004](/3i/decisions/dec-004-bunny-stream-video-hosting.md) selects the video provider but doesn't change any FR's behaviour.

---

## Types, Upload, and Validation

| ID | Requirement |
| :---- | :---- |
| **FR-MAT-01** | Material types: video, document, audio, external link. Ordered within a course |
| **FR-MAT-02** | Upload limits: video 4 GB, audio 500 MB, document 100 MB, image 10 MB. Video uses resumable (TUS) upload |
| **FR-MAT-03** | File type is validated server-side by content inspection, not by extension |

FR-MAT-03's content-inspection requirement exists because this is a public-facing upload surface (any approved instructor can upload) — extension or declared-MIME-type validation is trivially defeated and would let a malicious file through under a video or document extension.

---

## Video Delivery

| ID | Requirement |
| :---- | :---- |
| **FR-MAT-04** | Video is hosted on **Bunny Stream**, primary region Sydney, transcoded to adaptive-bitrate HLS |
| **FR-MAT-05** | Video is served exclusively via short-expiry signed token URLs. No permanent URL is ever exposed to a client |
| **FR-MAT-06** | **English caption files are required at video upload.** Admin may trigger paid auto-transcription as a fallback |

**FR-MAT-05 is tested against the learner-context rule, not session identity** — [3I-DEC-004](/3i/decisions/dec-004-bunny-stream-video-hosting.md) is explicit on this. A signing failure is the correct outcome when the *learner* lacks entitlement (no active enrolment, no active seat, wrong device), even if the *account* session is perfectly valid — a Member logged in with three profiles, only one of which is enrolled in a given course, must not be able to sign a token for that course under any of their other two profiles.

FR-MAT-06 has no exception path other than the admin-triggered paid fallback — a video cannot be published without a caption, full stop, since §22.3 risk 3 names caption omission as a direct threat to WCAG AA compliance (NFR-12).

---

## Viewing

| ID | Requirement |
| :---- | :---- |
| **FR-MAT-07** | On web, documents render in an in-browser viewer. **No download is offered on web** for any material type |
| **FR-MAT-08** | On mobile, materials may be downloaded for offline use, subject to §9.2 |
| **FR-MAT-09** | Materials are not admin-moderated before publication, except within courses requiring approval under FR-CRS-04 |

FR-MAT-07's no-download rule applies to **every** material type on web, not just video — a document or audio file is equally protected from direct download, viewed only through the platform's own viewer/player. FR-MAT-09 means the content-moderation burden for a non-under-13 course sits entirely with the instructor's own judgement — there is no admin queue standing between "instructor uploads" and "learner sees it" for the ordinary case.

---

## Offline Protection

The baseline's most detailed subsection (§9.2), and the one place this module carries real implementation weight beyond "call the provider's API."

| ID | Requirement |
| :---- | :---- |
| **FR-MAT-10** | Downloads are stored in the app's private sandbox, encrypted with a per-device key held in Keychain or Android Keystore |
| **FR-MAT-11** | Playback decrypts in memory. No plaintext file is written to disk |
| **FR-MAT-12** | Maximum **20 offline items per device** |
| **FR-MAT-13** | Offline content revalidates online at least every **7 days**. On failure, or on subscription lapse, or on device de-authorisation, local content is wiped |
| **FR-MAT-14** | Screen capture is blocked on Android (`FLAG_SECURE`) and detected on iOS with video blanked |
| **FR-MAT-15** | No DRM at launch. The chosen vendor supports Widevine and FairPlay as a later upgrade without migration |

**This is deterrence, not cryptographic defeat-proofing** — §22.3 risk 4 accepts this explicitly: offline protection without DRM can be defeated by a sufficiently motivated actor, and the mitigation is that it deters casual sharing while preserving a DRM upgrade path that requires no vendor change (since Bunny Stream already supports Widevine/FairPlay). This module should not be over-built past what §9.2 actually specifies on the theory that it should resist a determined attacker — that's explicitly out of scope at launch.

FR-MAT-13's three wipe triggers (revalidation failure, subscription lapse, device de-authorisation) are the same event conceptually: **the device can no longer prove current entitlement.** They're listed separately in the baseline because they're detected differently (a failed network check; a `commerce` webhook-driven status change; an explicit account-holder action in `identity-and-access`'s Device Management), but they should trigger the identical wipe routine, not three separate ones.

---

## Acceptance Criteria

1. A downloaded video is not visible or playable outside the app on a standard device.
2. Content is wiped when a subscription lapses and the app next reaches the network — no manual learner action required.
3. A signed video URL fails after expiry.
4. A video cannot be published without a caption file, with no bypass other than the admin-triggered auto-transcription fallback.
5. A Member with three profiles, only one enrolled in a given course, cannot obtain a valid signed video URL for that course under either of the other two profiles.
6. A 21st offline download on a device already holding 20 is refused, naming the limit.
7. A document's completion status (FR-CERT-03) requires an actual continuous 30-second viewer session — closing and reopening the viewer at 29 seconds does not carry the count forward.
8. Video/audio completion percentage accumulates correctly across multiple separate viewing sessions on different days.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-MTL-DM-001](../data-model.md) |
| Video hosting decision, learner-context signing rule | [3I-DEC-004](/3i/decisions/dec-004-bunny-stream-video-hosting.md) |
| Certificate completion thresholds this module feeds | FR-CERT-02, FR-CERT-03 — `certification` (not yet built) |
| Course a material belongs to | `catalogue` |
| Enrolment gating access (forward-referenced) | `learning-delivery` (not yet built) |