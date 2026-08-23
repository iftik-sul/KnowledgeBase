---
project: 3i
module: localisation
type: overview
status: current
updated: 2026-08-23
id: 3I-LCL-OVW-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - module
  - overview
---

# Localisation

The module that owns the five supported locales, the AI-translation pipeline for static UI strings, and the human sign-off gate for the handful of strings that bypass it.

**Module status: complete.** README, data model, requirements, and the full UI stage are written. Smallest module in the project by requirement count.

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| LOC | Localisation | 6 |

One existing decision applies directly and does most of the substantive work: [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) (five specific strings are exempt from AI translation and require named human sign-off per language before launch). One new operating note, not a decision: **AI-translated strings publish immediately, with admin free to correct afterward** — confirmed 2026-08-23, no review-gate/approval-queue workflow.

## Two Very Different Translation Paths

| | Ordinary strings | The five exempt strings |
| :---- | :---- | :---- |
| Source | AI-generated automatically | Human-authored directly, never AI |
| Goes live | Immediately | Only once named sign-off exists for that language |
| Correction | Admin edits any time, no gate | Same, but a correction still needs its own sign-off before it's trusted |

The five exempt strings — registration block message, safety contact copy, profile deletion confirmation, filtered-message notice, report-a-message flow copy — are listed in full in [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) and [age-and-safeguarding.md §10](/3i/age-and-safeguarding.md#10-safeguarding-strings--exempt-from-ai-translation); not re-listed here.

## RTL Stays Inline, Not Consolidated

Every screen across every module already written states its own "Full RTL mirroring (FR-LOC-04)" line, as plain text, not a link — roughly thirty of them by this point. **Confirmed 2026-08-23: this stays as-is.** `localisation` is where the underlying rule actually lives ([data-model.md](data-model.md#locale)'s `isRtl` flag on Arabic and Urdu), but promoting it to a cross-cutting reference document (the way `age-and-safeguarding.md` and `app-store-compliance.md` work) would imply going back and re-linking every already-written screen, which is a separate, much larger cleanup nobody has asked for. The inline citations aren't broken — they're just plain text, and that's fine.

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-LCL-DM-001 | current |
| [requirements/loc-localisation.md](requirements/loc-localisation.md) | 3I-LCL-REQ-001 | current |
| [ui/README.md](ui/README.md) | 3I-LCL-UI-000 | current — 2 screens, matrix, components, validation rules |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| The five exempt strings, and why | [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md), [age-and-safeguarding.md §10](/3i/age-and-safeguarding.md#10-safeguarding-strings--exempt-from-ai-translation) |
| User-generated content is never translated (a different rule from this module's own FR-LOC-03, but the same underlying principle) | FR-CRS/CHAT/CMS content generally |

## Delivery

Phase 9, Hardening (§21.1) — accessibility, RTL QA, performance, security review. The data model and admin tooling can be built earlier; full RTL QA across every screen is naturally a late-project activity.

## Forward References

None. Every locale-dependent field this module coordinates (`Account.locale`, notification language, certificate language) already exists in the modules that own them.

## Open Against This Module

| Item | Note |
| :---- | :---- |
| Human sign-off for the five exempt strings, in each of five languages | **Outstanding client dependency**, §22.2 dependency 9 — the institute's native speakers, not this project's own work. This module is fully specified without it; nothing renders those five strings in a given language until sign-off lands for it |
| Behaviour of an exempt string with no sign-off yet for a given language | Not specified in the baseline. Modelled as: falls back to English for that string only, rather than blocking the whole page — reasonable default, not confirmed |

## Change Requests Owed to the Client

None directly from this module. [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) is already part of the Tier 2 change request listed in [decisions/README.md](/3i/decisions/README.md#scope-changes-against-srd-v20).