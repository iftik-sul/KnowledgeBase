---
project: 3i
module: certification
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CRT-UI-VAL
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - validation
---

# Certification — Validation Rules

Field-level and flow-level validation shared across two or more certification screens.

---

## Revocation Reason Required

On [Admin Certificate Management](screens/admin-certificate-management.md): revoking a certificate requires a reason — free text, non-empty (FR-CERT-09). No silent or reason-less revocation exists anywhere in this module, since a revoked certificate remains publicly visible as revoked and the reason is part of what makes that meaningful rather than just an unexplained status flip.

## Reissuance Linkage

On [Admin Certificate Management](screens/admin-certificate-management.md): a reissuance action always performs both halves atomically — revoke the original **and** create the new certificate with `reissuedFrom` set, in one action, never as two separate steps an admin could complete only one of. See [data-model.md](../data-model.md#reissuance).