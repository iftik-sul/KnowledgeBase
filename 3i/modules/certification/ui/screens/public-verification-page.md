---
project: 3i
module: certification
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CRT-UI-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - certificates
  - public
---

# Screen: Public Verification Page

Satisfies: FR-CERT-07, FR-CERT-08, FR-CERT-09

---

## Purpose

Resolve a verification code to a certificate's public facts — no authentication, reachable by anyone who has the code (typically via the QR code on a printed or shared certificate).

## Access Gate

Public. No session of any kind required (FR-CERT-07) — not "public but rate-limited to logged-in-adjacent traffic," genuinely open.

## Contents

Given a valid code: learner name, course title, type, issue date, and the [Verification Status Badge](../components.md#verification-status-badge). A revoked certificate shows its recorded reason (FR-CERT-09) — not hidden, since the whole point of "revoked certificates show as revoked" is that a verifier checking a credential should see exactly that, not a not-found response indistinguishable from an invalid code.

**Reads only the certificate's own snapshot fields** ([3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md)) — never the live Learner or Course record, which may no longer exist. This is what makes the page work identically the day after issuance and ten years later, profile deleted or not.

## Role Variations

None — identical for every visitor, authenticated or not.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04) for the page's own chrome — labels, layout; the certificate facts themselves display in English regardless (FR-CERT-05).