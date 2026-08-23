---
project: 3i
module: localisation
type: requirements
status: current
updated: 2026-08-23
id: 3I-LCL-REQ-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - localisation
---

# Localisation

Baseline §19. Six requirements. [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) amends FR-LOC-02 for exactly five strings; every other requirement is implemented as written.

---

## Supported Locales

| ID | Requirement |
| :---- | :---- |
| **FR-LOC-01** | Supported locales: **English, Bangla, Hindi, Urdu, Arabic** |

Fixed set of five — see [data-model.md](../data-model.md#locale). No code path creates a sixth.

---

## Translation Scope

| ID | Requirement |
| :---- | :---- |
| **FR-LOC-02** | **Static UI strings only** are translated. Translations are AI-generated and stored, editable by admin |
| **FR-LOC-03** | **User-generated content is never translated** — course titles, descriptions, materials, exam questions, chat, reviews, and CMS content all remain as authored |

**Confirmed workflow for FR-LOC-02: AI-generated translations publish immediately**, with admin free to correct afterward — no approval queue, no draft state for ordinary strings. See [data-model.md](../data-model.md#translationvalue).

**[3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) carves out exactly five strings from FR-LOC-02's AI-generation default** — not restated here, see [README.md](../README.md#two-very-different-translation-paths) for the two-path comparison.

FR-LOC-03 is the same principle `catalogue` (reviews), `communication` (chat), and `public-site` (CMS content) already each state for their own content — this requirement is the umbrella statement; the individual modules don't restate it, and this module doesn't restate their specifics either.

---

## Layout

| ID | Requirement |
| :---- | :---- |
| **FR-LOC-04** | **Full RTL layout mirroring** for Arabic and Urdu across web and both mobile apps — not merely character rendering |

The underlying flag (`Locale.isRtl`) lives here; the requirement itself is satisfied screen-by-screen across every module already written, each stating its own RTL behaviour inline — see [README.md](../README.md#rtl-stays-inline-not-consolidated) for why this document doesn't attempt to enumerate or link them all.

---

## Locale-Dependent Behaviour

| ID | Requirement |
| :---- | :---- |
| **FR-LOC-05** | Notifications and emails follow the account's locale preference |
| **FR-LOC-06** | Certificates are always English |

FR-LOC-05 is already implemented in `communication` (`Notification.title`/`body` are "locale-rendered per the account's own locale preference"); FR-LOC-06 is already implemented in `certification` (`Certificate.language` is always `en`, regardless of the learner's or account's own locale). Both restated here only as the umbrella requirements they satisfy, not re-specified.

---

## Acceptance Criteria

1. Switching to Arabic mirrors navigation, alignment, icon direction, and progress indicators across web and both mobile apps.
2. No user-authored string — a course title, a chat message, a review — passes through the AI translation pipeline at any point.
3. An admin can correct a machine translation without a deployment, and the correction is live immediately.
4. An ordinary (non-exempt) string is visible in a given locale the moment AI generates it — no separate publish step.
5. An exempt string with no sign-off yet for a given locale falls back to English for that string only; the rest of the page renders normally in the visitor's chosen locale.
6. A certificate renders in English regardless of the learner's or account's locale, with no locale-switching control offered on the certificate itself.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-LCL-DM-001](../data-model.md) |
| Exempt strings | [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md), [age-and-safeguarding.md §10](/3i/age-and-safeguarding.md#10-safeguarding-strings--exempt-from-ai-translation) |
| Notification locale routing (implemented) | `communication` |
| Certificate English-only rule (implemented) | `certification` |