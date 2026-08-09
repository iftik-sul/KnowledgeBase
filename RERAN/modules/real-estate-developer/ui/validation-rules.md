---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-09
derived_from:
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

Every form/detail screen with a "Validation Summary" (or, on Document Details, "Verification Summary") follows the same interaction pattern, worded almost identically across six screens ([application-details.md](screens/application-details.md) — all three operational roles; [project-details.md](screens/project-details.md); [property-registration-details.md](screens/property-registration-details.md); [sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md); [fund-release-request.md](screens/fund-release-request.md)):

* Validation runs automatically before submission — the user does not trigger it manually.
* Each check displays one of three results: ✅ Passed, ⚠ Warning, ❌ Error.
* Selecting a failed or warned check navigates (screen text varies: "scrolls" or "navigates") directly to the affected field or section.
* The screen's primary submit action (worded per screen — "Submit to RERA," "Submit to RERA / Financial Institution," "Submit Request") remains **disabled** until all mandatory checks pass.

## Field-Level Rules

These specific checks recur, worded almost identically, across three or more of the six screens listed above:

* **[Mandatory / Required] fields completed** — appears on every one of the six screens (wording alternates between "Mandatory fields completed" and "Required fields completed" with no discernible pattern by role or screen type).
* **Required documents uploaded** — appears on five of the six screens (all except Document Details, which validates the single document being uploaded rather than a checklist of required documents).
* **File verification [completed]** — appears on five of the six screens, again with minor wording variation ("File verification" vs. "File verification completed").

## Document Upload Rules

[document-details.md](screens/document-details.md) validates the uploaded file itself rather than a checklist of required documents, under an "Automatic Validation" heading distinct from the "Validation Summary" pattern above. This check set is shared across that screen's three operational role variants (Registration Officer, Sales & Disclosure Officer, Escrow Liaison), but **the three variants don't fully agree**:

* **Registration Officer** (5 checks): File uploaded successfully, Correct file format, File size within limit, Virus scan completed, Metadata complete
* **Sales & Disclosure Officer / Escrow Liaison** (identical, 6 checks): File uploaded successfully, Supported file format, File size within limit, Virus scan completed, Metadata completed, Required document linked

The Registration Officer's list is missing "Required document linked" — present in the other two roles' — and uses "Correct file format" / "Metadata complete" where the other two say "Supported file format" / "Metadata completed." This looked like a shared, identical rule at first glance (same heading, same mechanism, same first four items) but differs in detail once compared line by line — reported here rather than silently normalized to one version. Both variants are preserved verbatim in [document-details.md](screens/document-details.md)'s own Role Variations rather than collapsed into a single rule here, since the difference (the extra "Required document linked" check) is exactly the kind of thing this batch's instructions warn against smoothing over.

This file-integrity check set is conceptually generic enough that it would likely apply anywhere else in the platform a file gets uploaded, but no other screen's Supporting Documents section actually declares it explicitly — every other screen's document upload table (Application Details, Project Details, Property Registration Details, Sales & Disclosure Details, Fund Release Request) instead folds "Required documents uploaded" and "File verification" into its own Validation Summary (see Field-Level Rules above) without a parallel per-file integrity checklist. Not generalized further than what the source actually states.

## Cross-Field & Business Rules

Everything below this point is validation content that looked like it *might* generalize but turned out to be genuinely specific to one screen's business domain — each check exists in only one screen's Validation Summary and has no counterpart, even loosely, elsewhere. Left in place in the originating screen file rather than centralized here, per this batch's instruction not to centralize something used once:

* **Related project eligibility** / **Related property validation** / **Property eligibility verified** — [application-details.md](screens/application-details.md), [sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md)
* **Duplicate [submission / application / project / property registration / disclosure / release request] check** — present on all six screens but worded around a different entity name each time; not centralized because the entity being checked for duplication is exactly the screen-specific part.
* **Buyer information completed** / **Buyer identity validation** / **Sale amount validation** / **Sale value validation** — [application-details.md](screens/application-details.md) (Sales & Disclosure Officer variant), [sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md)
* **Escrow account is active** / **Milestone eligible for release** / **Requested amount within approved limit** / **Engineer verification completed** / **Quantity Surveyor verification completed** — [fund-release-request.md](screens/fund-release-request.md)
* **Escrow account verified** / **Financial institution selected** — [application-details.md](screens/application-details.md) (Escrow Liaison variant)
* **Date validation** / **Location validation** — [project-details.md](screens/project-details.md)
* **Approved project selected** / **Unit number uniqueness** / **Address validation** — [property-registration-details.md](screens/property-registration-details.md)

## Screens Read-Only, No Validation

The Developer Principal / Director's versions of Application Details, Project Details, Property Registration workflows, and Sales & Disclosure Details have no Validation Summary at all — those screens are read-only for that role, so there is nothing to validate. [company-profile.md](screens/company-profile.md) (Principal only) and [fund-release-request-details.md](screens/fund-release-request-details.md) (Escrow Liaison, but a details/review screen rather than a creation form) likewise have no Validation Summary in the source, even though both allow limited editing while a record is in an editable status — noted in each of those files individually.
