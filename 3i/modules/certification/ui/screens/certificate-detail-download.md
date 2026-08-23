---
project: 3i
module: certification
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CRT-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - certificates
---

# Screen: Certificate Detail / Download

Satisfies: FR-CERT-06, FR-CERT-08

---

## Purpose

View and download a single issued certificate — the screen a guardian reaches from the [Guardian Dashboard](/3i/modules/identity-and-access/ui/screens/guardian-dashboard.md)'s certificate list.

## Access Gate

Member, for a certificate belonging to one of their own profiles — including a **deleted** profile's surviving certificates, per [3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md) and the deleted-profile view already specified in `identity-and-access`.

## Contents

The certificate's snapshotted content — learner name, course title, type, issue date — rendered as a downloadable PDF carrying the verification code, QR code, institute seal, and signature image (FR-CERT-06). **This screen's actual visual output is blocked on the outstanding certificate-design-asset dependency** (§22.2 item 5) — the data and logic are fully specified; the artwork is not yet available to render against.

If the certificate has been revoked or superseded by a reissuance, that status is shown plainly — same [Verification Status Badge](../components.md#verification-status-badge) concept as the public page, so a guardian sees the same status a third party checking independently would see.

## Role Variations

Member only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04) for the surrounding page chrome; **the certificate itself is always English** (FR-CERT-05) and does not mirror regardless of the viewer's locale.