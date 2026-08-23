---
project: 3i
module: localisation
type: data-model
status: current
updated: 2026-08-23
id: 3I-LCL-DM-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - data-model
  - localisation
---

# Localisation — Data Model

Entities owned by this module. Other modules reference these; they do not restate them.

---

## Locale

| Field | Notes |
| :---- | :---- |
| Code | One of exactly five — `en`, `bn`, `hi`, `ur`, `ar` (FR-LOC-01). Fixed, same closed-set treatment `public-site`'s `Page` slugs get — no code path creates a sixth |
| RTL | Boolean. `true` for `ur` and `ar` only. **The single source of truth every "Full RTL mirroring (FR-LOC-04)" citation across the project ultimately refers to**, even though those citations are inline text, not links — see [README.md](README.md#rtl-stays-inline-not-consolidated) |

Five rows, seeded once, never more.

---

## TranslationString

| Field | Notes |
| :---- | :---- |
| Key | Unique identifier for one static UI string |
| Source text | The canonical English text — authored by whoever writes the platform's UI copy, not translated itself |
| Category | Loose grouping (e.g. which screen or flow it belongs to), for the admin tooling's own organisation — not a baseline concept |
| Exempt | Boolean — true for exactly the five strings [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) names |

---

## TranslationValue

| Field | Notes |
| :---- | :---- |
| String | FK to TranslationString |
| Locale | FK, one of the four non-English locales — English itself lives on `TranslationString.sourceText`, not as a TranslationValue row |
| Text | |
| AI generated | Boolean. `true` until an admin edits it, then `false` — not because AI text is deleted, but because a human-corrected value is no longer purely machine output |
| Last edited by, last edited at | Nullable until first admin correction |

**For an exempt string, this row is never AI-generated** — `aiGenerated` is always `false`, `text` is human-authored from the start, and the row additionally requires a linked **SignOff** (below) before it's actually served to any visitor in that locale.

**Ordinary strings publish the moment AI generates them** — confirmed 2026-08-23, no approval queue. An admin correction afterward simply overwrites `text` and flips `aiGenerated` to `false`; there's no draft/live distinction to manage.

---

## SignOff

| Field | Notes |
| :---- | :---- |
| Translation value | FK, **only ever set for exempt strings** — an ordinary string has no SignOff concept at all |
| Signed off by | Name of the named human reviewer ([3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md)'s requirement) |
| Signed off at | |

**An exempt string's TranslationValue is not served to visitors in that locale until a SignOff exists for it.** Where none exists yet, that specific string falls back to English for that locale — not a blocked page, not a placeholder, just the English text standing in until sign-off lands. This is a reasonable default for an unspecified case, not a baseline-mandated fallback; see [README.md](README.md#open-against-this-module).

**A correction to an already-signed-off exempt string clears its SignOff.** Editing the text of a safeguarding-critical string is exactly the kind of change that should require fresh named confirmation, not silently carry forward an approval of different words.

---

## Forward References

None. `Account.locale` (`identity-and-access`), notification language (`communication`), and certificate language (`certification`, always English regardless) are all already-built fields this module coordinates against, not entities it owns or waits on.

---

## Referenced By

| Module | Reads |
| :---- | :---- |
| Every module with a UI stage | TranslationString/TranslationValue — every static string rendered anywhere on the platform resolves through this module's data, though individual screens don't restate that — it's implicit in "the platform is localised," the same way every screen doesn't restate NFR-12's contrast requirement as a per-screen dependency either |
| `communication` | Locale — FR-NOT-05's notification-language routing reads `Account.locale` (owned by `identity-and-access`) against this module's five-locale list |

## Referenced

| Entity | Owned by | Read here |
| :---- | :---- | :---- |
| Account | `identity-and-access` | `locale` field — this module doesn't own it, only validates it against the five-locale closed set |