---
project: OstadLagbo
module: shagred-profile
type: requirements
status: current
updated: 2026-08-29
id: OL-SGP-REQ-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.0.md
owner: Iftikher
---

# Shagred Profile — Requirements

Derived from MVP Scope Baseline v1.0 §1–§2 (by asymmetry) and the founder decisions of 2026-08-28/29. Supersedes the discovery note at `/OstadLagbo/reference/discovery/shagred-profile-decisions.md`. Account creation is governed by `registration-and-verification` (REG-08); offer mechanics by `contact-and-offers`; blocking by `ratings-and-trust`.

## Design principle

The profile is deliberately minimal and deliberately hidden. Ostads exist to be found; Shagreds must never be findable. Every requirement below serves that asymmetry.

## SGP-01 Fields

| Field | Required | Visibility |
|---|---|---|
| Display name | Yes | Visible to permitted Ostads (SGP-05) |
| Profile photo | Optional | Visible to permitted Ostads |
| Date of birth | Yes (18+ gate, REG-03) | Internal — never shown to anyone |
| Gender | Optional | Visible to permitted Ostads if provided |
| Phone (verified) / email (optional) | Per REG | Never shown; phone reveal on offer acceptance is governed by `contact-and-offers`, not the profile |

**Acceptance:** no API response to an Ostad ever contains a Shagred's DOB, phone, or email via profile endpoints.

## SGP-02 Coarse location

The Shagred selects District and Area from the Bangladesh administrative dataset (same source as OSP-02). **No map pin, no latitude/longitude, is ever stored for a Shagred.** Live GPS is used only on-device to center the Shagred's own map view and is never transmitted for storage.

**Acceptance:** the Shagred data model contains no coordinate fields; permitted Ostads see District + Area as text only.

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
| Expired (7 days) or declined | **No — visibility lapses** |
| Accepted | Yes — visibility persists for the life of the relationship |
| Either party blocks the other | No — visibility severed immediately (per `ratings-and-trust`) |
| Shagred deletes account | No — all visibility ends |

**Acceptance:** an Ostad whose offer expired or was declined receives no profile data on any endpoint; acceptance grants durable visibility that survives app restarts and sessions; blocking cuts visibility within one request cycle.

## SGP-06 Editing

All Shagred-editable fields (display name, photo, gender, District/Area) are changeable at any time with immediate effect. No review process applies to Shagreds.

## Proposed technical defaults summary

Photo size/format limits follow OSP image rules. Everything else in this document — the field set, the no-coordinates rule, history immutability and privacy, and the visibility lifecycle — changes only with founder approval.
