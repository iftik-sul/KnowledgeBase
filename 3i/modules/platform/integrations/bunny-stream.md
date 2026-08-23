---
project: 3i
module: platform
type: integration
status: current
updated: 2026-08-23
id: 3I-PLT-INT-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - integration
  - bunny-stream
---

# Integration: Bunny Stream

Contract with Bunny Stream, the platform's video hosting and delivery provider ([3I-DEC-004](/3i/decisions/dec-004-bunny-stream-video-hosting.md)). Consumed entirely by `materials`; documented here per the same `integration` document-type convention as [Stripe](stripe.md).

---

## What 3i Uses

- **Upload** — resumable (TUS protocol) ingest for videos up to 4 GB (FR-MAT-02).
- **Transcoding** — adaptive-bitrate HLS, primary region Sydney (FR-MAT-04, NFR-07).
- **Signed token URLs** — short-expiry, the only way video is ever served (FR-MAT-05). No permanent URL is ever exposed to a client.

## The One Rule That Matters Most

**A signing failure is tested against the learner-context rule, not session identity** — [3I-DEC-004](/3i/decisions/dec-004-bunny-stream-video-hosting.md)'s own explicit instruction, made concrete in `materials`' [Video Player](/3i/modules/materials/ui/screens/video-player.md): a token is issued on behalf of a specific **Learner's** enrolment and entitlement, never merely "any profile under this logged-in account." This is the single most important thing to get right in the actual Bunny integration code, since getting it wrong doesn't fail loudly — it just lets one profile stream video another profile in the same account was never entitled to.

## Performance Targets

Video start time under 3 seconds on a 5 Mbps connection (NFR-30); adaptive bitrate rendition switching without playback interruption (NFR-31). Both are Bunny's own delivery characteristics at the modelled scale, not something the platform's own code independently guarantees — see [3I-DEC-004](/3i/decisions/dec-004-bunny-stream-video-hosting.md)'s Cost section on why the provider choice was scale-dependent and should be re-modelled if usage grows materially beyond the §20.2 capacity baseline.

## Related

| | |
| :---- | :---- |
| Owning module | `materials` |
| Provider selection | [3I-DEC-004](/3i/decisions/dec-004-bunny-stream-video-hosting.md) |
| Learner-context signing rule, applied | `materials` [Video Player](/3i/modules/materials/ui/screens/video-player.md) |
| Offline protection (separate from streaming, same provider relationship) | `materials` [OfflineDownload](/3i/modules/materials/data-model.md#offlinedownload-mobile-only) |