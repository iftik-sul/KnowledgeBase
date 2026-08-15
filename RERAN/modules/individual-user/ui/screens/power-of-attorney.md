---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/service-flows/service-29-register-power-of-attorney.md"
  - "RERAN/modules/individual-user/service-flows/service-30-act-on-behalf-of-property-owner.md"
  - "RERAN/modules/individual-user/service-flows/service-42-cancel-power-of-attorney.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - power-of-attorney
---

# Screen: Power of Attorney

**Access:** Any authenticated Individual User — PoAs granted and PoAs held, both shown.

## Purpose

Two distinct lists in one screen: PoAs the account has granted to someone else (as the property owner) and PoAs the account holds on someone else's behalf (as the representative) — different directions of the same relationship, both needed since one account can be either party.

## Layout

```
Tabs: Granted by Me / Held by Me
↓
PoA List
↓
Per-PoA Actions
```

## Sections

### Section 1 — Granted by Me

PoAs the account has registered (#29), naming an attorney/representative. Each row: representative name, scope of authority, PoA Status badge (Active, Expired, Revoked — `status-badges.md`). Action: Cancel (#42).

### Section 2 — Held by Me

PoAs where the account is the named representative. Each row: property owner name, scope, status. Action: **Act on Behalf of Property Owner** (#30) — opens the wizard's routing flow, validating the PoA is Active before letting the account select which underlying service to perform.

## Empty State

**Message** (either tab, if empty):

> No Powers of Attorney [granted / held]. Register one to authorize someone to act on your behalf, or ask a property owner to register one naming you.

## Reused Components

Status Badge, Buttons.

## Validation

An Active status is a hard gate before #30 can proceed — matches #30's own Business Rule and its Application Status Flow, which puts `Authorization Validation` first. This screen must not let a user start #30 against an Expired or Revoked PoA and only discover the block mid-wizard.

## Access

No role variation — the two tabs aren't roles, they're directions of the same relationship, and any account may have entries in either or both.

## User Flow

```
Sidebar → Power of Attorney → [Granted / Held] → [select PoA] →
  Cancel (#42) or Act on Behalf (#30 → Submit Application, routed)
```

## Notes

* **#42's action and outcome are genuinely unspecified in source** — its own service-flow file documents this as the thinnest-specified service in the module. This screen's Cancel action and the resulting status change to Revoked are inference from #29's mirror shape, not confirmed. Flagged the same way in `ui/README.md`'s Open Items.
