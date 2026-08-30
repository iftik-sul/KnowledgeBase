---
project: OstadLagbo
module: shagred-profile
type: requirements
status: current
updated: 2026-08-30
id: OL-SGP-REQ-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.1.md
owner: Iftikher
---

# Shagred Profile — Requirements

Derived from MVP Scope Baseline v1.1 §2. Account creation is governed by `registration-and-verification` (REG-08); offer mechanics by `contact-and-offers`; blocking by `ratings-and-trust`.

## Design principle

The profile is deliberately minimal and deliberately hidden. Ostads exist to be found; Shagreds must never be findable. Every requirement below serves that asymmetry.

## SGP-01 Fields

| Field | Required | Visibility |
|---|---|---|
| Display name | Yes | Visible to permitted Ostads (SGP-05) |
| Profile photo | Optional | Visible to permitted Ostads |
| Date of birth | Yes (18+ gate, REG-03) | Internal — never shown to anyone |
| Gender | Optional | Visible to permitted Ostads if provided |
| Address (SGP-02) | Yes | Thana + District visible to permitted Ostads; street line and postal code never shown |
| Phone (verified) / email (optional) | Per REG | Never shown; phone reveal on acceptance is governed by `contact-and-offers` |

**Acceptance:** no API response to an Ostad ever contains a Shagred's DOB, phone, email, street address, or postal code via profile endpoints.

## SGP-02 Address — no coordinates, ever

The Shagred provides: a manual street-address text line, plus **Thana, District, Division, and Postal Code, each selected from dropdown lists** on the shared Bangladesh administrative dataset (Division → District → Thana cascading; postal code list filtered by the selection — dataset and cascade mechanics are engineering defaults shared with OSP-02). Address is required at onboarding (REG-08).

**No map pin and no latitude/longitude is ever stored for a Shagred.** Live GPS is used only on-device to center their own map view and is never transmitted for storage. Of the address, permitted Ostads see **Thana and District only** — enough to judge distance, nothing more; street line and postal code remain private to the Shagred (and admin review per ADM-10).

**Acceptance:** the Shagred data model contains no coordinate fields; dropdowns cascade correctly; permitted Ostads receive Thana + District as text and nothing else of the address.

## SGP-03 Ostad history (private)

A system-derived record of this Shagred's accepted offers: each entry is the Ostad (name, link to profile) and the acceptance date. The record is **immutable and private** — the Shagred cannot hide, edit, or remove entries; no other user, including the listed Ostads, can view it in any form (not even as a count). Entries persist even if the Ostad's account is later deleted (entry shows "deleted account" in place of the link).

**Acceptance:** no endpoint exposes any history data to any account other than the owning Shagred; no mutation endpoint exists for history entries.

## SGP-04 Statistics

Joined date only, visible to permitted Ostads. No ratings of Shagreds exist (rating is one-directional per baseline §6); no offer counts, acceptance rates, or activity indicators are computed or shown.

## SGP-05 Visibility rule

A Shagred profile is **never** browsable, searchable, listable, or shown on any map. It is visible to exactly one audience: an Ostad who holds an offer from that Shagred, under this lifecycle:

| Offer state | Ostad can view profile? |
|---|---|
| Pending | Yes |
| Expired (7 days), declined, or withdrawn | **No — visibility lapses** |
| Accepted | Yes — visibility persists for the life of the relationship |
| Either party blocks the other | No — visibility severed immediately (per `ratings-and-trust`) |
| Shagred deletes account | No — all visibility ends |

**Acceptance:** an Ostad whose offer expired, was declined, or was withdrawn receives no profile data on any endpoint; acceptance grants durable visibility; blocking cuts visibility within one request cycle.

## SGP-06 Editing

All Shagred-editable fields (display name, photo, gender, address) are changeable at any time with immediate effect. No review process applies to Shagreds.

## Proposed technical defaults summary

Photo limits follow OSP image rules; address dataset and cascade mechanics are shared engineering defaults. Everything else — the field set, the no-coordinates rule, the Thana+District-only visibility, history immutability and privacy, and the visibility lifecycle — changes only with founder approval.
