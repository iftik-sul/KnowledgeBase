---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-IDA-UI-008
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - profiles
  - safeguarding
figma: null
---

# Screen: Profile Picker

Satisfies: FR-FAM-04

---

## Purpose

Shown after Member login when the account has more than one profile. Selecting a profile enters that profile's study context for the session.

## Content

A tile per **active or never-activated** profile, using the [Age Band Badge](../components.md#age-band-badge) and display name. **Inactive and deleted profiles do not appear here** — they are reached only from [Guardian dashboard](guardian-dashboard.md), never from the picker, since the picker is a study-entry surface and those states cannot study.

## Behaviour

Selecting a tile prompts the [PIN Pad](../components.md#pin-pad) component — **mandatory on every profile**, per [3I-DEC-018](/3i/decisions/dec-018-profile-pin-mandatory-guardian-controlled.md), including the Member's own profile if they study.

**PIN lockout matches FR-AUTH-09 exactly** — [3I-DEC-022](/3i/decisions/dec-022-pin-lockout-and-dob-correction-notification.md): five failed attempts trigger a 15-minute lockout, with progressive delay and per-IP rate limiting. Same shape as password lockout, not a separate bespoke pattern. During lockout, the tile shows a countdown rather than accepting further PIN entry, consistent with how [Login](login.md) handles the same state.

On correct PIN, enters the profile's study context. On the family's only never-activated profile with no active seat available for anyone, the picker instead routes toward seat purchase (FR-BILL-04) — covered fully in `commerce`.

## Role Variations

Member only. Not shown to a Member with exactly one profile, who skips straight to that profile's PIN pad instead — [3I-DEC-026](/3i/decisions/dec-026-single-profile-skips-picker.md), see also [Login](login.md).

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04): tile order and the PIN pad's surrounding chrome mirror; digit entry order does not, per [components.md](../components.md#pin-pad).