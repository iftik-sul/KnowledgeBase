---
project: 3i
module: localisation
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-LCL-UI-VAL
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - validation
---

# Localisation — Validation Rules

Field-level validation shared across two or more localisation screens.

---

## Sign-Off Gates Exempt-String Visibility

On [Exempt String Sign-Off](screens/exempt-string-signoff.md): an exempt string's `TranslationValue` for a given locale is not servable to any visitor in that locale until a `SignOff` row exists for it (see [data-model.md](../data-model.md#signoff)). This isn't a soft warning shown to the admin — it's a hard gate; the platform-wide string-rendering logic checks for the SignOff before ever returning that string's translated text, falling back to English when it's absent. Correcting the text of an already-signed-off exempt string clears the existing SignOff and re-triggers the gate.