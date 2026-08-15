---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/service-flows/service-36-remote-identity-verification.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - profile
---

# Screen: Profile & KYC

**Access:** Any authenticated Individual User — own profile only.

## Purpose

Personal details, account credentials, and identity verification status — including where Remote Identity Verification (#36) lives, since it's a Profile & KYC action rather than a parallel diaspora-only catalog (matching `navigation.md`'s diaspora-specific note).

## Layout

```
Personal Information
↓
Identity Verification Status
↓
Account Settings
```

## Sections

### Section 1 — Personal Information

Name, contact details, residential address — editable, standard profile fields.

### Section 2 — Identity Verification Status

Shows whether Remote Identity Verification (#36) is complete. If not yet completed, offers **Start Verification**, opening the wizard at Pattern J. Once verified, this section gates whether #37 (Remote Property Transactions) is selectable elsewhere in the app — the hard gate `validation-rules.md` specifies.

### Section 3 — Account Settings

Login credentials, notification preferences.

## Empty State

Not applicable — every account has a profile.

## Reused Components

Buttons, Document Upload (identity documents, via the #36 wizard).

## Validation

The Identity Verification Status shown here must be the single source of truth #37 checks against — no separate verification flag should exist elsewhere in the app.

## Access

No role variation — every account type reaches the same Profile & KYC screen; a Diaspora Investor's account is not structurally different, just one that's actually completed the verification section.

## User Flow

```
Top Bar (profile menu) or Sidebar → Profile & KYC → Start Verification →
  Submit Application (Pattern J, #36)
```

## Notes

* This is deliberately the only place #36 is reachable from — `navigation.md` explicitly rejected a separate "diaspora" navigation section, since a Diaspora Investor is still just an Individual User acting through the same surfaces as everyone else once verified.
