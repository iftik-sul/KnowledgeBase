---
project: OstadLagbo
module: ostad-profile
type: ui
status: current
updated: 2026-09-25
id: OL-OSP-UI-001
derived_from: /OstadLagbo/modules/ostad-profile/requirements/ostad-profile-requirements.md
owner: Iftikher
---

# Ostad Profile — UI

Screens for viewing an Ostad's public profile, the Ostad's own Profile tab, editing (non-key fields instantly, key fields through a revision), pause, and insights. Conventions per [UI Overview](/OstadLagbo/ui-overview.md); behaviour and endpoints per [OSP API](/OstadLagbo/modules/ostad-profile/api/ostad-profile-api.md); field definitions and validation per the OSP requirements, cited not repeated. Onboarding-stage editing (draft states) belongs to the REG ui; the map pin and its self-preview to the MAP ui; ratings to the RNT ui.

The **routing rule** governs which editor a field uses, by `approval_status`: **draft / changes_requested / rejected** → the onboarding wizard (REG ui); **pending** → non-key fields via the editors here (saved, not yet public), key fields **locked**; **approved** → non-key edits publish immediately, key edits go through a **revision**. Every screen here honours it.

## Group A — The public Ostad profile

### Public profile — the read everyone shares
- **Purpose:** the single profile view a guest, Shagred, or Ostad sees when opening an Ostad.
- **Shell(s):** all — reached from a map pin/card, search, a share link, favourites, or an offer.
- **Entry:** tapping a preview card (MAP), a deep link (MAP-07), a favourite, or an offer's counterpart.
- **Structure (top to bottom), the `GET /v1/ostads/{id}` shape:** header — profile photo, **full legal name** (English; Bangla shown alongside), display name, **gender**, **verified badge** (approved only), headline; **trust** — the verified badge and **profile completion %** (both public, OSP-09; `trust: { verified, completion_pct }`); **stats** — rating average + review count (or **"New"** when count is 0), joined date, last active as a **day-granularity label** ("3 days ago", never live presence); area (Division/District/Thana/Postal — never the street line); the **exact map pin** (public by design, MAP-01) with a "view on map" affordance; About, occupation, years of experience, languages; **skills** (category + skill name, level, years); **education** grouped by level, highest first; **experience** in its four groups; **portfolio** — image gallery, the one intro video in an inline player, PDF documents, and external links with a domain preview (YouTube links render an embedded player); and the **reviews** section — the written reviews with their star ratings and the Ostad's replies (the RNT list component; RNT ui owns it).
- **States:** **loading** → skeleton, profile open ≤2 s (NFR-02); **paused** → a "not currently accepting offers" banner and the offer action disabled, everything else normal (OSP-11); **not available** → the neutral `not_found` state, shown identically whether the Ostad is unapproved, suspended, purged, or has blocked the viewer (opacity rule) — the screen never hints which.
- **Viewer actions (signed-in only; a guest attempting any routes to registration, MAP-03):** **Send offer** (Shagred only; disabled when paused or when the viewer already has a pending offer — the `viewer.offer` state; a `profile_incomplete` result routes the Shagred to setup) → OFR ui; **Favourite / unfavourite** (`viewer.favorited`) → MAP ui; **Share** (`GET /v1/ostads/{id}/share`); **Report / Block** → RNT ui. Reviews are read here (RNT ui owns the list component and the write).
- **Never shows:** date of birth, street address, phone, email, identity documents, insight counts, approval history, or any open revision's contents — none of these are in the public shape; and it never distinguishes a block from a missing profile.

## Group B — The Ostad's own Profile tab

### Profile home (own)
- **Purpose:** the Ostad's control centre — their profile as they hold it, plus status, completeness, and the doors to editing, pause, and insights.
- **Shell:** Ostad shell → **Profile/Settings**.
- **Entry:** the Profile tab (present once the account exists and the initial wizard is done — during initial onboarding the wizard owns the screen, REG ui).
- **Structure, from `GET /v1/profile`:** the **review-status banner** when not approved (REG ui component); **completion %** (OSP-09) with a nudge toward the fields that would raise it; a **View as public** action; every profile section (personal, address, professional, skills, education, experience, portfolio) with an **Edit** affordance whose target depends on the routing rule; **identity** shown **as metadata only** — document type, verification status, submitted date — **never the images or the full ID number, even to the Ostad themselves**; the **pause** toggle (Group E, approved only); and links to **Insights** (Group F) and account **Settings** (REG ui).
- **View as public:** for an **approved** Ostad, opens their own public profile (`GET /v1/ostads/{own_id}`) exactly as others see it; the **pin + preview-card** self-preview (`GET /v1/profile/location/preview`, MAP) works in **any** state, so a pending Ostad can still check their card.
- **States:** the banner reflects pending / changes-requested / rejected / approved; key-field Edit affordances are **locked with a note** while `pending` or while a revision is `under_review`.
- **Never shows:** its own identity images (metadata only); insight *identities* (counts live under Insights, and even there never who).

## Group C — Editing non-key fields

Non-key fields: display name, gender, headline, about, occupation, years of experience, languages, address, education, experience, portfolio. Callable when `pending` or `approved`; in draft states the same edits are made in the onboarding wizard (an edit attempt here returns `state_conflict details.use = "onboarding"` → route to the wizard).

### Non-key field editor
- **Structure:** the editable fields with inline validation (headline ≤80, about ≤1,000, years 0–60, languages multi-select including free-text other) and the **cascading address picker** for address.
- **Data & actions:** `PATCH /v1/profile` with the changed subset. **Approved** → publishes immediately (OSP-10); **pending** → saved to the record, not public until the verdict. A key field included by mistake returns `state_conflict details.field` → route it to the revision editor.
- **Copy:** when `pending`, a line clarifies edits are saved but go live at approval.

### Education & experience entries
- **Structure:** repeatable rows; education (level, credential, institution, passing year 1950–current), experience (group, title, organization?, period, description ≤300). Add / edit / remove per row.
- **Data:** `POST` / `PATCH` / `DELETE /v1/profile/education|experience[/{id}]`.

### Portfolio manager
- **Structure:** the four types with their limits shown as you fill them — images (≤10, ≤5 MB, JPEG/PNG/WebP), **the one intro video (≤45 s, replace = delete-then-add)**, documents (≤5, PDF only), external links (≤5, https; domain preview, YouTube embeds). Upload progress via the upload-ticket flow.
- **Data:** `GET` / `POST` / `DELETE /v1/profile/portfolio[/{id}]`; a limit hit returns `conflict details.limit`; a bad item (46-s video, non-PDF, oversized image, non-https link) returns `validation_failed`, re-checked on the stored object. Portfolio may be **empty** (OSP-07); completion % reflects it.

## Group D — The key-field revision (approved Ostads)

Key fields — **legal names, profile photo, skills, and identity documents** — never change the public profile until a revision is approved. One revision at a time collects all of them, so a name fix, a new photo, a skills change, and new identity docs go through **one** review (OSP-10).

### Revision editor
- **Purpose:** stage key-field changes and submit them for review, while the public keeps seeing approved values.
- **Entry:** any key-field Edit affordance on Profile home (approved only).
- **Structure:** the proposed values — legal name (EN/BN), a new **photo** (upload ticket), the **complete** proposed skills set (1–5 via the fuzzy category picker), and the **identity** re-capture (the REG stage-2 payload: document images + live selfie, same live-capture rule as onboarding); a persistent reminder that **the public still sees the approved profile**; the **Submit for review** action; and, when present, the **admin's note** (`changes_requested`) or the last rejection reason (`last_closed`).
- **States (derived, `GET /v1/profile/revision`):** **editing** → freely amendable (`PUT` amends in place — there is only ever one revision); **under review** → **locked**, no edits (`PUT` returns `state_conflict: under_review`); **changes requested** → the note shows, editable and resubmittable; a **discards_at** warning when the revision is nearing its 90-day abandonment discard (with prior push).
- **Data & actions:** `PUT /v1/profile/revision` (amend); `POST /v1/profile/revision/submit` (→ under review; opens the admin review case; identity re-check flagged when names/identity change; a photo-only change is reviewed against the current identity selfie); `DELETE /v1/profile/revision` (discard — allowed only for a revision **never submitted**; a reviewed one can't be discarded, only edited and resubmitted). Verdicts arrive by push and via `last_closed`; approval publishes atomically (old photo deleted), rejection discards.
- **Never shows:** the revision's contents to the public, ever; the Ostad's own stored identity images (only that identity is part of the pending set).

## Group E — Pause (OSP-11)

### Pause toggle
- **Purpose:** an approved Ostad turns discoverability off and on themselves, instantly, no admin.
- **Entry:** Profile home (approved only).
- **Structure:** a single toggle with a plain explanation of what pausing does and does not do.
- **Data & actions:** `PUT /v1/profile/pause {paused}`. **On:** removed from map, search, and category results by the next discovery query; no new offers; **existing chats continue**, already-received pending offers stay actionable, and the profile stays reachable by deep link and favourites showing the not-accepting banner. **Off:** restored on the next query. `state_conflict` if not approved.
- **Copy:** the toggle states that pausing is reversible anytime and does not affect existing connections.

## Group F — Insights (OSP-12, private)

### Insights
- **Purpose:** the Ostad's own private performance view — counts only.
- **Shell:** Ostad shell → **Insights** tab (approved only).
- **Structure:** a period switch (**7 days / 30 days**); **profile views**; **offers received by outcome** (pending, accepted, declined, expired); **total connections**.
- **Data:** `GET /v1/profile/insights?period=7d|30d`. `state_conflict` if not approved (the tab is hidden until then).
- **Never shows:** **who** viewed, favourited, or browsed — never any Shagred identity, in any form (OSP-12, SGP invisibility). Counts are presented as indicative (server-deduplicated views).

## Flows

**Fix a name and photo after approval.** Profile home → Edit legal name (key) → the revision editor opens → change name (EN/BN) and add a new photo → **Submit for review** → the revision locks, the public profile is unchanged → verdict by push: *approve* publishes both atomically; *changes requested* returns the note, editable; *reject* discards, reason kept in `last_closed`.

**Update the About (instant).** Profile home → Edit About (non-key) → `PATCH /v1/profile` → live immediately on the public profile (approved), no review.

**Go quiet for a month.** Profile home → Pause on → the pin leaves the map on the next query; a Shagred opening a deep link sees "not currently accepting offers"; an existing pending offer can still be accepted → later, Pause off → discoverable again.

## What this module's screens never show

No screen shows an Ostad's date of birth, street address, phone, or email to another user, or their identity images to anyone (not even the owner — metadata only; admin sees them audited, ADM ui); no screen shows an open revision's contents publicly, or lets the public tell a paused profile from a hidden one beyond the stated pause notice; no screen distinguishes a block, a suspension, or non-approval on the public read (all `not_found`); and no insight ever names a viewer, favouriter, or browser.
