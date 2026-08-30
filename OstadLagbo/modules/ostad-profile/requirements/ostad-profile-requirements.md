---
project: OstadLagbo
module: ostad-profile
type: requirements
status: current
updated: 2026-08-30
id: OL-OSP-REQ-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.1.md
owner: Iftikher
---

# Ostad Profile — Requirements

Derived from MVP Scope Baseline v1.1 §2. Defines every field of the Ostad profile, its validation, and its visibility. Capture flow is governed by `registration-and-verification` (REG-09, REG-10); location capture by `map-discovery`; re-review triggers by `admin-review`; rating aggregation by `ratings-and-trust`.

## Visibility classes

Every field belongs to one class. **Public** — visible to any user viewing the profile. **Internal** — visible only to the Ostad themselves and admin review. **System** — computed, not directly editable.

## OSP-01 Names and personal information

| Field | Required | Visibility |
|---|---|---|
| Full legal name (English) | Yes | Public |
| Full legal name (Bangla) | Yes | Public |
| Display name | Yes | Public — used on map cards and chat headers; full legal name heads the profile page |
| Profile photo | Yes | Public |
| Date of birth | Yes (18+ gate, REG-03) | Internal — age and DOB never shown |
| Gender | Yes | Public |

Legal names must match the identity document; mismatch is grounds for admin change-request. Bangla legal name must accept full Bangla script input even though the UI is English.

**Acceptance:** profile page shows both legal names; DOB is absent from every public surface and API response for other users.

## OSP-02 Address

The Ostad provides a manual street-address text line plus **Thana, District, Division, and Postal Code, each selected from dropdown lists** on a Bangladesh administrative dataset (Division → District → Thana cascading; postal code list filtered by the selection — dataset and cascade mechanics are engineering defaults shared with SGP-02). **Public:** Division, District, Thana, and Postal Code (the exact map pin is already public per baseline §3, so these add no exposure). **Internal:** the street-address text line.

**Acceptance:** dropdowns cascade correctly; the street line never appears on any public surface or API response.

## OSP-03 Professional information

Headline (max 80 chars), About (max 1,000 chars), Occupation, Years of experience (0–60), Languages spoken (multi-select from list including Bangla, English, Arabic, Hindi, Urdu + free-text other). All public, all required except About.

## OSP-04 Skills and taxonomy

Skill categories come from a **fixed, admin-managed category list**; skill names within a category are free text. An Ostad selects 1–5 category+skill entries, each with level (Beginner / Intermediate / Expert) and years of experience.

**Fuzzy category matching (hard requirement):** category entry is a typeahead that matches misspelled and partial input **in both English and Bangla** to the fixed list — e.g., "gitar" → Guitar, "cooking clas" → Cooking, and "গিটার" → Guitar via the category's Bangla alias (ADM-11, CL-013) — using edit-distance or equivalent fuzzy matching per script. Free-text category creation is impossible; if no match satisfies the Ostad, they pick the nearest category and put specifics in the skill name. The same matching serves Shagred keyword search (see `map-discovery`).

**Acceptance:** common misspellings of every category resolve to it in the typeahead in both scripts; no path creates a category outside the admin list.

## OSP-05 Education

Repeatable entries, each: education level (SSC / HSC / Bachelor / Masters / PhD / Other Certification), certificate or degree name, institution name, passing year (1950–current). Zero entries allowed (a craft Ostad may have none); entries are public and shown grouped by level, highest first.

## OSP-06 Experience

Repeatable public entries in four groups: work experience, teaching experience, certifications, awards. Each entry: title, organization (optional), period or year, short description (max 300 chars).

## OSP-07 Portfolio

| Type | Limit | Rules |
|---|---|---|
| Images | Max 10, 5MB each | JPEG/PNG/WebP; compressed client-side |
| Intro video | **Exactly one, max 45 seconds** | Recorded in-app or uploaded; duration enforced client-side before upload and validated server-side; compressed to ≤720p; stored natively |
| Documents | Max 5, 10MB each | PDF only |
| External links | Max 5 | https URLs; shown with domain preview; YouTube links render an embedded player |

All portfolio items are public. Longer video content is served via external links, not native storage.

**Acceptance:** a 46-second video cannot be stored by any path; an Ostad can complete the profile with zero portfolio items (completion % reflects it).

## OSP-08 Statistics (system)

Public, computed: average rating and review count (rules in `ratings-and-trust`), joined date, last active (day granularity — "today", "3 days ago" — never live presence).

## OSP-09 Trust signals (system)

Public: identity-verification status, admin-approval status, verified badge (granted per `admin-review`), and **profile completion %** — proposed formula: required fields complete = 70 points, plus 10 each for About, any education entry, and any portfolio item, capped at 100. Formula is an engineering default, tunable without founder re-approval.

## OSP-10 Editing and re-review

All fields are editable by the Ostad at any time. Edits to **key fields** — legal names, identity documents, skills — return the profile to review per baseline §5, remaining discoverable with the last approved version until re-approved. All other edits publish immediately. Field-level change tracking must make the diff visible to admin review.

**Acceptance:** editing a skill triggers re-review and the public profile keeps showing the prior approved skill set until approval; editing the About publishes instantly.

Non-key-field edits publishing without review is a deliberate trade-off: post-approval abuse of freely-editable fields (display name, headline, about, portfolio) is moderated reactively through reports (RNT-07) and admin action, not preemptively.

## OSP-11 Visibility pause

An approved Ostad can **pause their visibility** from a profile setting — effective immediately, reversible anytime, no admin involvement (change log CL-010). While paused: the Ostad disappears from the map, search, and category results (MAP-02) and cannot receive new offers (OFR-01); existing chats continue, pending offers already received remain actionable, and the profile stays reachable by deep link and favorites, showing "not currently accepting offers" with the offer action disabled. Pause state is instrumented so ADM-13 dormancy distinguishes paused from inactive.

**Acceptance:** toggling pause removes/restores the map pin within one request cycle; a paused profile opened by deep link shows the notice and no enabled offer action; an already-received pending offer can still be accepted while paused.

## OSP-12 Ostad insights (system, private)

A private insights screen for the Ostad (CL-014): **profile view counts** (7- and 30-day), **offers received by outcome** (pending, accepted, declined, expired), and **total connections** — sourced from the same instrumentation that feeds ADM-12 and MAP-11. Counts only, never identities: who viewed, favorited, or browsed is never shown, preserving the Shagred-invisibility principle (SGP). Visible only to the Ostad themselves.

**Acceptance:** insight counts match admin analytics for the same account and period; no endpoint exposes viewer identities to any Ostad.

## Proposed technical defaults summary

Character caps, image/document size limits, video resolution, completion formula, insight refresh cadence, and the Bangladesh address dataset choice are engineering defaults, changeable without founder re-approval. Field inventory, visibility classes, the one-video-45s rule, taxonomy structure, cross-script fuzzy matching, the visibility-pause semantics, counts-only insights, and re-review triggers change only with founder approval.
