---
project: OstadLagbo
module: ostad-profile
type: api
status: current
updated: 2026-09-25
id: OL-OSP-API-001
derived_from: /OstadLagbo/modules/ostad-profile/requirements/ostad-profile-requirements.md
owner: Iftikher
---

# Ostad Profile — API

Endpoints for reading and editing the Ostad profile, the key-field revision flow, pause, insights, and the two reference lookups every profile form needs (skill categories and administrative areas). Also defines the **payloads for onboarding stages 1, 3, and 5**, which the REG api's wizard delegates here. Conventions per [API Overview](/OstadLagbo/api-overview.md); entities per [OSP Data Model](/OstadLagbo/modules/ostad-profile/data-model/ostad-profile-data-model.md).

## Where each edit goes — by approval state

The same profile field is written through different endpoints depending on where the Ostad is in their lifecycle. **Key fields** are legal names, identity documents, skills, and the profile photo (OSP-10, CL-021). This table is the routing rule the whole document follows:

| `approval_status` | Non-key fields (display name, gender, headline, about, occupation, experience years, languages, address, education, experience) | Key fields (legal names, photo, skills) and identity | Portfolio |
|---|---|---|---|
| `draft` · `changes_requested` · `rejected` | Onboarding stages 1, 3, 5 (REG api), using the payloads below | Onboarding stages 1, 2, 5 | Portfolio endpoints |
| `pending` (initial review in progress) | `PATCH /v1/profile` and the entry endpoints — saved to the record; not public yet | **Locked** — `state_conflict` until the verdict. Review examines a fixed identity, photo, and skill set | Portfolio endpoints |
| `approved` | `PATCH /v1/profile` and the entry endpoints — **public immediately** (OSP-10) | Through a **revision** (below) — the public keeps seeing the approved values until a verdict | Portfolio endpoints |

Non-key edits during initial review are permitted because REG-11 lets a pending Ostad edit their profile, and because non-key fields publish without review once approved anyway; key fields are locked because they are exactly what the review is deciding (OSP-10). A suspended Ostad can edit nothing (restricted session).

## Endpoints — reading profiles

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `GET /v1/ostads/{id}` | Anyone, incl. guests (MAP-03). Returns only a profile that is **approved and belongs to an active account**; per-IP rate limit (MAP-09 scraping resistance) | `Accept-Language` for guests | **Public profile** (below) — approved values only; an open revision is never joined (Data Model Overview rule 3). A paused profile is returned with `accepting_offers: false` (OSP-11) | `not_found` — for a blocked viewer (**opacity rule**), and equally for an unapproved, suspended, or purged Ostad, so neither blocks nor suspensions are visible to the public |
| `GET /v1/profile` | The Ostad themself, any state except restricted | — | **Own profile** — every profile field including internal ones (street address), plus `approval_status`, `open_revision` summary, `completion_pct`, `paused`. Identity appears **as metadata only** — `{ doc_type, verification_status, submitted_at }` of the current document — never the images or the full ID number, even to their owner (REG api) | `forbidden` (Shagred) |

**Public profile shape:**

```
{ id, legal_name_en, legal_name_bn, display_name, photo_url (signed), gender,
  headline, about, occupation, years_experience, languages[],
  area: { division, district, thana, postal_code },        // names localized to the viewer
  location: { lat, lng },                                   // exact — public by design (MAP-01, R-04)
  skills[]:     { category: { id, name }, skill_name, level, years_experience },
  education[]:  { level, credential_name, institution, passing_year },     // grouped by level, highest first
  experience[]: { group, title, organization, period, description },
  portfolio[]:  { id, item_type, url (signed) | external_url, duration_seconds? },
  stats: { rating_avg | null, rating_count, joined_at, last_active },  // last_active a day-granularity label; the client renders "New" when rating_count == 0 (RNT-03), as it does on the map
  trust: { verified, completion_pct },
  accepting_offers,
  viewer?: { favorited, offer: { id, status } | null } }    // authenticated viewers only; values computed by the MAP and OFR rules
```

Never in a public profile: date of birth, street address, phone, email, identity documents, `approval_status` history, insight counts, the open revision.

**Profile-view events.** A successful public read emits a `profile_view` analytics event **server-side** (ADR-002) — excluding reads by the Ostad themself — deduplicated per viewer per Ostad per day: by account for signed-in viewers; by guest session **and** IP for guests; and excluding rate-limited traffic. Counting server-side stops a client from inflating views by re-requesting. **Known limit:** guest session ids are generated on the device, so a determined script rotating sessions across IPs can still add views; the IP key and rate limits make this costly, not impossible, and insight counts are presented as indicative.

## Endpoints — editing non-key fields

Callers: the Ostad themself when `approval_status` is `pending` or `approved` (routing table above). In draft states these fields are written through the onboarding stages instead; these endpoints return `state_conflict` with `details.use = "onboarding"`.

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `PATCH /v1/profile` | Ostad (pending/approved) | Any subset of: `display_name`, `gender`, `headline` (≤80), `about` (≤1,000), `occupation`, `years_experience` (0–60), `languages[]`, `address: { street_address, division_id, district_id, thana_id, postal_code_id }` | own profile | `validation_failed` (`details.address = "invalid_chain"`; length limits); `state_conflict` (`details.field` names any key field included — legal names, photo, skills — which go through a revision) |
| `POST /v1/profile/education` | Ostad (pending/approved) | `level` (ssc\|hsc\|bachelor\|masters\|phd\|other_certification), `credential_name`, `institution`, `passing_year` (1950–current) | `{ id }` | `validation_failed` |
| `PATCH /v1/profile/education/{id}` · `DELETE …/{id}` | Owner | any of the above fields | `204` | `not_found` |
| `POST /v1/profile/experience` | Ostad (pending/approved) | `group` (work\|teaching\|certification\|award), `title`, `organization?`, `period`, `description` (≤300) | `{ id }` | `validation_failed` |
| `PATCH /v1/profile/experience/{id}` · `DELETE …/{id}` | Owner | any of the above fields | `204` | `not_found` |

## Endpoints — portfolio

Available in **every** non-suspended state, including draft onboarding: portfolio is optional (OSP-07 allows zero items) and is never a key field.

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `GET /v1/profile/portfolio` | Owner | — | `[ { id, item_type, url (signed) \| external_url, duration_seconds? } ]` | — |
| `POST /v1/profile/portfolio` | Owner | `item_type` (image\|intro_video\|document\|external_link) + `upload_id` (purpose `portfolio_image` / `portfolio_video` / `portfolio_document`) **or** `external_url` (https) for links | `{ id }` | `conflict` (`details.limit` — 10 images, **1 intro video**, 5 documents, 5 links; OSP-07); `validation_failed` (video over 45 s, document not PDF, image over 5 MB, non-https link — re-checked on the stored object, OSP-07/NFR-04) |
| `DELETE /v1/profile/portfolio/{id}` | Owner | — | `204` — the storage object is deleted in the same operation (OSP-DM) | `not_found` |

Replacing the intro video is delete-then-add; the one-video rule is a database constraint (OSP-DM), so a second video can never coexist even briefly.

## Endpoints — key-field revisions (approved Ostads)

The revision holds proposed changes to legal names, photo, skills, and identity while the public keeps seeing the approved values (OSP-10, OSP-DM). Its review state is **derived** — `editing`, `under_review`, or `changes_requested` — per OSP-DM.

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `GET /v1/profile/revision` | Approved Ostad | — | `{ open: null \| { state, proposed: { legal_name_en?, legal_name_bn?, photo_url?, skills?, identity? }, last_verdict: { verdict, note, at }?, discards_at? }, last_closed: null \| { outcome: "approved" \| "rejected" \| "abandoned", note?, at } }` — `last_closed` keeps a rejection's reason visible after the revision closes; `discards_at` warns of the 90-day abandonment date | — |
| `PUT /v1/profile/revision` | Approved Ostad; **refused while `under_review`** | Any subset of: `legal_name_en`, `legal_name_bn`, `photo_upload_id` (purpose `profile_photo`), `skills[]` (the **complete** proposed set, 1–5 entries: `{ category_id, skill_name, level, years_experience }`), `identity` (the REG stage-2 identity payload) | the open revision | `state_conflict` (`details.reason = "under_review"`); `validation_failed` (`details.skills[i] = "category_inactive"` — a new skill set may not use a deactivated category, ADM-11; skills count outside 1–5) |
| `POST /v1/profile/revision/submit` | Approved Ostad; revision in `editing` or `changes_requested` | — | `{ state: "under_review" }` — opens a `review_case` of kind `revision`, with `identity_recheck_required` set when legal names or identity change; a photo change is reviewed against the current identity selfie (ADM-DM, OSP-DM) | `state_conflict` (nothing to submit, or already under review) |
| `DELETE /v1/profile/revision` | Approved Ostad; revision in `editing` and **never submitted** | — | `204` — discards the revision, its proposed photo, and any draft identity row it carries (images deleted in the same operation, REG-DM) | `state_conflict` (the revision has been reviewed — it is evidence and cannot be discarded; edit and resubmit instead) |

**Amend-in-place** (OSP-DM): a `PUT` in `editing` or `changes_requested` updates the same open revision; there is never more than one, and it is locked while `under_review`. Identity in a revision follows REG-DM's draft-row rule: re-saving replaces the draft identity row until the revision is submitted, after which that row is frozen. **Abandonment:** an unsubmitted or returned revision inactive for 90 days is discarded after a prior notice (push, and `discards_at` in the read above), and its uploads are deleted (OSP-10, OL-RET-001). The verdict's effects — publishing on approve, discarding on reject — are ADM's (ADM-DM verdict table); the Ostad learns the outcome by push (REG-11) and through `last_closed`.

## Endpoints — pause and insights

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `PUT /v1/profile/pause` | Approved Ostad | `paused` (boolean) | `{ paused, paused_at }` — takes effect on the next discovery query (OSP-11): off the map and search, no new offers; existing chats and already-received pending offers continue. Emits a pause/unpause analytics event so ADM-13 dormancy separates paused from inactive | `state_conflict` (not approved) |
| `GET /v1/profile/insights` | Approved Ostad, own data only | `?period=7d\|30d` | `{ profile_views, offers: { received, accepted, declined, expired, pending }, connections_total }` — **counts only** (OSP-12) | `state_conflict` (not approved) |

Insights never include who viewed, who favorited, or any Shagred identity (OSP-12, SGP principle). View counts come from the deduplicated server-side `profile_view` events (ADR-002 rollups); offer and connection counts from OFR's records.

## Endpoints — reference lookups (public)

Owned as data by ADM (ADM-DM), exposed here because the profile forms are their first consumer; the SGP and MAP apis reuse them unchanged.

| Endpoint | Caller & policy check | Request | Response |
|---|---|---|---|
| `GET /v1/skill-categories` | Anyone | `?q=` optional | Without `q`: every **active** category, `{ id, name, name_en, name_bn }` (`name` in the viewer's language), for filter lists — cacheable. With `q`: the **fuzzy cross-script typeahead** (OSP-04, CL-013) — matches misspellings in either script against both names and synonym aliases ("gitar", "গিটার" → Guitar), ranked by match quality, max 10. **`q` must be at least 2 characters** (shorter is `validation_failed`), and the typeahead carries its **own per-IP rate limit** separate from other reads — fuzzy matching is the most expensive public query, and needs no login |
| `GET /v1/admin-areas` | Anyone | `?level=division\|district\|thana\|postal_code&parent_id=` | The children of `parent_id` at that level, `{ id, name, name_en, name_bn }` — the cascading dropdowns of OSP-02 and SGP-02; cacheable |

## Onboarding stage payloads (used by the REG api's wizard)

**Stage 1 — personal information** (`PUT /v1/onboarding/stages/1`):

```
{ legal_name_en, legal_name_bn,          // key fields; must match the identity document (ADM-02)
  display_name,
  photo_upload_id,                       // purpose profile_photo; required (OSP-01); key field
  gender }
```

Date of birth is **not** re-collected — it was captured and 18+-checked at registration (REG-03) and lives on the account. Bangla legal name accepts full Bangla script regardless of UI language (OSP-01).

**Stage 3 — address:** `{ street_address, division_id, district_id, thana_id, postal_code_id }` — chain validity enforced (`details.address = "invalid_chain"`).

**Stage 5 — professional details:**

```
{ headline, about?, occupation, years_experience, languages[],
  skills[1..5]:  { category_id, skill_name, level, years_experience },   // active categories only
  education[]:   { level, credential_name, institution, passing_year },
  experience[]:  { group, title, organization?, period, description } }
```

Stage 5 **replaces** the education and experience sets wholesale (it is a form, submitted whole); after submission, individual entries are edited through the entry endpoints. Portfolio is not part of stage 5 — it is added through the portfolio endpoints at any time and may be empty.

## Flows

**Changing a key field after approval.** `PUT /v1/profile/revision` (e.g., a corrected Bangla legal name and a new photo) → optionally more `PUT`s → `POST …/submit` → the review case opens and the revision locks; the public profile is unchanged → verdict: *approve* publishes the proposed values atomically (the old photo object is deleted); *request changes* returns the revision with the admin's note, editable and resubmittable; *reject* discards it, with the reason kept in `last_closed`. At no moment does the public profile show an unapproved key field (OSP-10 acceptance).

**Editing during initial review.** A pending Ostad may correct a typo in their headline (`PATCH /v1/profile`) but cannot change their legal name, photo, or skills until the verdict; if the verdict is *changes requested*, the onboarding stages reopen and key fields are editable again there.

**Pause.** `PUT /v1/profile/pause {paused: true}` → the next map query excludes the Ostad; `GET /v1/ostads/{id}` still returns the profile with `accepting_offers: false`, so deep links and favorites keep working (OSP-11).

## What this module does not expose

No endpoint returns an Ostad's date of birth, street address, phone, email, or identity documents to anyone but the Ostad themself — and identity documents not even to them, only as metadata — (admin sees them through the ADM api, audit-logged); an open revision's contents to the public; any Ostad's insights to anyone else; who viewed or favorited a profile, in any form; or whether a profile is missing because of a block, a suspension, or non-approval — all three return the same `not_found` (subject to the opacity rule's stated limit, API Overview).
