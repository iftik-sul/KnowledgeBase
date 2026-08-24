---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-24
id: 3I-IDA-UI-012
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - devices
figma: null
---

# Screen: Device Management

Satisfies: FR-AUTH-11

---

## Purpose

Lists registered devices on the account; allows de-authorisation.

**Reached from [Account Settings](account-settings.md)' "Devices" section** — per [3I-DEC-032](/3i/decisions/dec-032-account-settings-hub.md). Previously undocumented: this screen existed with no stated route to it.

## Content

One row per device: name/type, last seen. A summary line states the current allowance and how many are in use — **the allowance is variable**, per [3I-DEC-015](/3i/decisions/dec-015-device-allowance-scales-with-seats.md): seats plus two, floor of three. The formula, not just the current number, should be visible ("You have 3 seats, so up to 5 devices") so a Member understands why the number moves when they buy or cancel a seat.

## Behaviour

De-authorising a device frees a slot immediately. Registering a new device beyond the current allowance is refused with a message naming the allowance and offering either de-authorisation of an existing device or a link to purchase another seat (`commerce`).

Swap limit: **twice per 30 days** (FR-AUTH-11, unchanged by decision). Approaching the limit should be visible on this screen, not discovered only on refusal.

**If a seat is cancelled and the account is now over its new (lower) device allowance**, existing devices are **not** forcibly de-authorised — the account simply cannot register a new one until it is back under the allowance. This is a judgement call, not specified in the baseline; state it plainly rather than leaving the behaviour to be inferred from the refusal message alone.

## Role Variations

Any authenticated role — Member, Instructor, Admin all manage their own devices identically. Only the seat-linked allowance formula is Member-specific; Instructor and Admin accounts (which do not hold seats in the same sense) default to the floor of 3.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).
