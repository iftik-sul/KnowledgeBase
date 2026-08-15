---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-15
derived_from:
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/real-estate-developer/ui/screens/application-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/project-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registration-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/sales-and-disclosure-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/fund-release-request.md"
  - "RERAN/modules/real-estate-developer/ui/screens/document-details.md"
tags:
  - real-estate-developer
  - ui-spec
  - validation
---

# Validation Rules

Validation patterns shared by two or more form and detail screens in this module. Validation genuinely specific to a single screen — the exact business checks for that screen's own fields — stays documented in that screen's own file and is linked from here rather than repeated.

## The Automatic Validation Mechanism

> **Updated 2026-08-15.** The per-role screen variants are retired — every screen listed here is now a
> single unified screen (see [README.md](README.md)). References below that used to name a role variant
> now name an **application or record type** instead, which is what the differing check sets were
> actually keyed to.

Every form/detail screen with a "Validation Summary" (or, on Document Details, "Verification Summary")
follows the same interaction pattern, worded almost identically across six screens
([application-details.md](screens/application-details.md), [project-details.md](screens/project-details.md),
[property-registration-details.md](screens/property-registration-details.md),
[sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md),
[fund-release-request.md](screens/fund-release-request.md)):

* Validation runs automatically before submission — the user does not trigger it manually.
* Each check displays one of three results: ✅ Passed, ⚠ Warning, ❌ Error.
* Selecting a failed or warned check navigates directly to the affected field or section.
* The screen's primary submit action remains **disabled** until all mandatory checks pass.
* **The Validation Summary applies to every user.** It previously appeared only on the operational
  variants of these screens, because the Developer Principal / Director variants had no editing
  controls. That was an access restriction, not a property of validation.

## Field-Level Rules

These specific checks recur, worded almost identically, across three or more of the six screens listed above:

* **[Mandatory / Required] fields completed** — appears on every one of the six screens (wording alternates between "Mandatory fields completed" and "Required fields completed" with no discernible pattern by role or screen type).
* **Required documents uploaded** — appears on five of the six screens (all except Document Details, which validates the single document being uploaded rather than a checklist of required documents).
* **File verification [completed]** — appears on five of the six screens, again with minor wording variation ("File verification" vs. "File verification completed").

## Document Upload Rules

[document-details.md](screens/document-details.md) validates the uploaded file itself rather than a
checklist of required documents, under an "Automatic Validation" heading distinct from the "Validation
Summary" pattern above.

**Resolved 2026-08-15 — six checks:**

| Check | Applies to |
| :---- | :---- |
| File uploaded successfully | Every document |
| Supported file format | Every document |
| File size within limit | Every document |
| Virus scan completed | Every document |
| Metadata completed | Every document |
| Required document linked | Documents filed against a project, property, sale or escrow record |

> **How this was resolved.** This section previously recorded a conflict between three role variants
> of `document-details.md`:
>
> * **Registration Officer** (5 checks): File uploaded successfully, Correct file format, File size
>   within limit, Virus scan completed, Metadata complete
> * **Sales & Disclosure Officer / Escrow Liaison** (identical, 6 checks): the same, but "Supported
>   file format" / "Metadata completed", plus **Required document linked**
>
> It was deliberately not normalized while three variants existed, since the extra check is a real
> business rule rather than a wording difference. With `document-details.md` rebuilt as a single
> screen, three check sets is no longer an option, so:
>
> * **"Correct file format" / "Supported file format" and "Metadata complete" / "Metadata completed"
>   are wording variants of the same check.** Merged, keeping the two-thirds-majority wording.
> * **"Required document linked" is kept**, and scoped to what it actually tests. It was absent from
>   the Registration Officer's list, but a registration document is filed against a project or
>   property just as a disclosure document is filed against a sale — so its absence reads as an
>   omission in that variant rather than a rule that genuinely does not apply. **Flagged**: if the
>   client intends registration documents to be uploadable without a linked record, this check needs
>   a documented exemption rather than removal.

## Cross-Field & Business Rules

Everything below this point is validation content that looked like it *might* generalize but turned out to be genuinely specific to one screen's business domain — each check exists in only one screen's Validation Summary and has no counterpart, even loosely, elsewhere. Left in place in the originating screen file rather than centralized here, per this batch's instruction not to centralize something used once:

* **Related project eligibility** / **Related property validation** / **Property eligibility verified** — [application-details.md](screens/application-details.md), [sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md)
* **Duplicate [submission / application / project / property registration / disclosure / release request] check** — present on all six screens but worded around a different entity name each time; not centralized because the entity being checked for duplication is exactly the screen-specific part.
* **Buyer information completed** / **Buyer identity validation** / **Sale amount validation** / **Sale value validation** — [application-details.md](screens/application-details.md) (**sales disclosure** applications), [sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md)
* **Escrow account is active** / **Milestone eligible for release** / **Requested amount within approved limit** / **Engineer verification completed** / **Quantity Surveyor verification completed** — [fund-release-request.md](screens/fund-release-request.md)
* **Escrow account verified** / **Financial institution selected** — [application-details.md](screens/application-details.md) (**escrow** applications)
* **Date validation** / **Location validation** — [project-details.md](screens/project-details.md)
* **Approved project selected** / **Unit number uniqueness** / **Address validation** — [property-registration-details.md](screens/property-registration-details.md)

## Screens With No Validation Summary

**Rewritten 2026-08-15.** This section previously listed the Developer Principal / Director variants of
Application Details, Project Details, Property Registration and Sales & Disclosure Details as having no
Validation Summary because "those screens are read-only for that role." Those variants no longer exist,
and the reasoning did not survive unified access — validation is a property of submitting a record, and
every user can submit.

Two screens still carry no Validation Summary in the source, for reasons unrelated to roles:

* [company-profile.md](screens/company-profile.md) — a single screen with no second variant; permits
  limited editing but the source declares no validation checks.
* [fund-release-request-details.md](screens/fund-release-request-details.md) — a details/review screen
  rather than a creation form. Its sibling [fund-release-request.md](screens/fund-release-request.md)
  (the creation form) does have one. Edits here are governed by status instead: a request may be
  updated only while Draft, Returned or Information Requested, and becomes read-only once Approved or
  Funds Released.

Both are noted in their own files. Neither gap is a role restriction.
