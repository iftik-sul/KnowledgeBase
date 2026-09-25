---
project: OstadLagbo
module: shagred-profile
type: ui
status: current
updated: 2026-09-25
id: OL-SGP-UI-001
derived_from: /OstadLagbo/modules/shagred-profile/requirements/shagred-profile-requirements.md
owner: Iftikher
---

# Shagred Profile — UI

Screens for the Shagred's own profile and its editor, the narrow card an Ostad sees of a Shagred, and the Shagred's private Ostad history. Conventions per [UI Overview](/OstadLagbo/ui-overview.md); behaviour and endpoints per [SGP API](/OstadLagbo/modules/shagred-profile/api/shagred-profile-api.md); the account-creation entry that first opens the editor is REG-08 (REG ui).

**The design principle drives every screen: Ostads exist to be found, Shagreds must never be findable.** So this module has **no** browse, search, list, or map surface for Shagreds — none exists to build. A Shagred profile is seen by exactly one audience (a permitted Ostad), only as a fixed narrow card, and only inside a live offer or connection.

## Group A — The Shagred's own profile

### Own profile & editor
- **Purpose:** the Shagred views and edits their minimal profile; the same editor, empty, is the first-time setup right after registration.
- **Shell:** Shagred shell → **Profile/Settings**. First-time setup is reached from `register/verify` (REG-08, REG ui) when `profile_complete` is false.
- **Structure, from `GET /v1/shagred-profile`:** display name (required); profile photo (optional); gender (optional); the **cascading address picker** — street line + Division→District→Thana→Postal (SGP-02, the shared component); joined date. A plain line noting that **only your name, photo, gender, and your Thana + District are shown — to an Ostad you've sent an offer to, and no one else**; the street line and postal code stay private. The same line notes the one exception to contact: **when an Ostad accepts your offer, your phone number and any verified email are shared with them (and theirs with you)** — the contact reveal governed by OFR-04.
- **First-time setup vs later edits (the api's two paths):** the **empty** first-time form saves with `PUT /v1/shagred-profile` (all-at-once); every later change uses `PATCH /v1/shagred-profile` (omitted fields stay unchanged; `photo: null` removes the photo, `gender: null` clears it). The client picks by `profile_complete`, so re-opening the form and saving can never wipe an existing photo.
- **States:** edits are **instant, no review** (SGP-06); `validation_failed details.address = "invalid_chain"` on a bad Division→postal chain; setup on an already-complete profile returns `state_conflict details.use = "patch"`.
- **No coordinates, ever:** the editor never captures or sends a pin or lat/lng. Live GPS is used only on-device to centre the Shagred's own map view; it is never transmitted. A client bug that tried to send `lat`/`lng` is rejected outright (`validation_failed`), not ignored (SGP-02).
- **Completeness:** `profile_complete` is derived (name + valid address). The Shagred is not blocked from the map by an incomplete profile — the guest map is open (MAP-03) — but **sending an offer** requires it, so an incomplete profile is caught there (`profile_incomplete` → back to this editor, OFR/overview).
- **Never shows:** the Shagred has **no "my public profile" preview**, because there is no public Shagred profile — nothing to preview.

## Group B — The Ostad's view of a Shagred

### The Shagred card (a component, not a navigable screen)
- **Purpose:** the only way any Ostad ever sees a Shagred — a fixed narrow card, surfaced inside a live offer or connection, never browsable.
- **Where it appears:** embedded in a **received offer** (OFR ui) and in a **connection/chat header** (OFR ui); an Ostad can refresh it while permitted via `GET /v1/shagreds/{id}` (the `{id}` is the Shagred's profile id — the only Shagred handle any client holds).
- **Structure — the fixed projection (`GET /v1/shagreds/{id}`):** display name, photo (if set), gender (if set), **area: District + Thana only**, joined date. Never more.
- **Visibility lifecycle (SGP-05), what the Ostad sees as an offer moves:** **pending** or **accepted** → the card shows; **declined / expired / withdrawn** → the card is **gone** — no name, photo, or area — leaving only the offer's own message and dates (OFR ui); **either party blocks** → gone within one request cycle; **Shagred deletes** → gone. Every one of these refusals returns the identical `not_found` (opacity) — the Ostad's UI shows the same "no longer available" state whichever it was.
- **After the card is gone (binding with OFR/RNT):** the Ostad can still **report** or **block** the Shagred from the lapsed offer — the actions target the **offer id**, the API resolves the Shagred server-side, and the Ostad never sees the profile again (RNT ui).
- **Never shows:** street address, postal code, date of birth, phone, email, or account id — none are in the projection (contact reveal on acceptance is OFR's, and returns only phone + verified email); and it is never reachable except from a live offer/connection.

## Group C — The Shagred's Ostad history (private)

### Ostad history
- **Purpose:** the Shagred's own record of who they've connected with — read-only, private, permanent.
- **Shell:** Shagred shell → Profile/Settings → **Ostad history**.
- **Structure, from `GET /v1/shagred-profile/history`:** entries ordered by connection date, newest first — each the **Ostad's name captured at connection time** and the date, with a link to that Ostad's public profile; once an Ostad's account is gone the entry shows **"deleted account"** with no link.
- **States:** the snapshot name and date never change; a tapped link resolves under the Ostad's *public* profile rules (OSP ui) — an Ostad who later blocked the Shagred, was suspended, or left all resolve to the same "not available", so no entry reveals by its behaviour what happened after.
- **It is read-only, structurally:** there is **no** add, edit, or delete anywhere — entries are created only by the offer-acceptance transaction (OFR). The Shagred cannot hide or remove one.
- **Never shows:** the list, its contents, or even its existence to anyone but the owning Shagred — not to the listed Ostads, not as a count (admin sees it only through the audited ADM path).

## Flows

**Set up and go.** `register/verify` (Shagred) → this editor, empty → `PUT /v1/shagred-profile` (name + address, optional photo/gender) → the map. Later, a photo swap is a `PATCH` from Profile — instant, and it never drops the fields left untouched.

**An Ostad sees, then stops seeing.** A Shagred sends an offer → the Ostad's received-offer shows the Shagred card → the Ostad declines → the card vanishes; only the message and dates remain, with report/block on the offer id → the Shagred is invisible to that Ostad again, permanently unless a new offer is sent and accepted.

## What this module's screens never show

No screen lists, searches, maps, or counts Shagreds — none of those surfaces exist; no screen ever shows an Ostad a Shagred's street address, postal code, DOB, phone, email, or account id (contact reveal on acceptance is OFR's, and returns only phone + verified email); no screen stores or sends a coordinate for a Shagred; no screen lets anyone but the owning Shagred see the Ostad history, in any form; reads of a Shagred profile are **never recorded** as analytics (SGP api — the observation record the invisibility principle exists to prevent); and no refusal to an Ostad distinguishes a lapsed offer from a block or a deletion — all are the same "not available".
