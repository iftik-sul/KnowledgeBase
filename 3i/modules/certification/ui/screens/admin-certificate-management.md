---
project: 3i
module: certification
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CRT-UI-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - certificates
  - admin
---

# Screen: Admin Certificate Management

Satisfies: FR-CERT-09

---

## Purpose

Admin searches issued certificates, revokes one with a recorded reason, or reissues a corrected replacement.

## Access Gate

Admin only.

## Contents

Search/lookup across every issued certificate — by verification code, learner name (snapshot, searchable even for a deleted profile), or course title. Each result shows the [Certificate Card](../components.md#certificate-card) with **Revoke** and **Reissue** actions.

**Revoke** requires a reason (see [validation-rules.md](../validation-rules.md#revocation-reason-required)) and marks the certificate revoked in place — used when a certificate should simply no longer be valid, with no replacement.

**Reissue** is a distinct action from a plain revoke — it opens a form pre-filled with the original's snapshot data, editable (the correction itself: a misspelled name, for instance), and on confirm performs both halves atomically per [validation-rules.md](../validation-rules.md#reissuance-linkage): the original is revoked with `revokeReason = "Correction — reissued"`, and a new certificate is created with the corrected data and `reissuedFrom` pointing at the original.

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).