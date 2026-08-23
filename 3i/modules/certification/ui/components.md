---
project: 3i
module: certification
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CRT-UI-COMP
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - components
---

# Certification — Shared Components

Documented once here. Screens link to this file rather than restating.

---

## Certificate Card

Used on: [Certificate Detail / Download](screens/certificate-detail-download.md), and referenced from `identity-and-access`'s [Guardian Dashboard](/3i/modules/identity-and-access/ui/screens/guardian-dashboard.md) certificate list.

Shows type (attendance/completion), course title (snapshot, not live), issue date, and a status indicator — current, revoked, or (for a reissued original) superseded. A revoked or superseded card is visually distinct from a current one, same distinct-not-greyed-out principle already applied to profile state elsewhere in this project — a guardian scanning a list of certificates shouldn't need to open each one to know which are still valid.

## Verification Status Badge

Used on: [Public Verification Page](screens/public-verification-page.md).

Three states: **Valid** (current, unrevoked), **Revoked** (with the recorded reason shown — FR-CERT-09), or **Not Found** (the code doesn't resolve to anything, phrased identically whether the code was never valid or was mistyped, since there's no meaningful distinction to a verifier either way).