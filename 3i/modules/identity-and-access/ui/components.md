---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-18
id: 3I-IDA-UI-COMP
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - components
---

# Identity and Access — Shared Components

Documented once here. Screens link to this file rather than restating.

---

## PIN Pad

Used on: [Profile picker](screens/profile-picker.md), [Profile create/edit](screens/profile-create-edit.md) (setting), [Guardian dashboard](screens/guardian-dashboard.md) (reset).

4-digit numeric entry. Large touch targets — the primary users on the entry side are children.

**RTL note (FR-LOC-04):** digit entry order does not mirror in Arabic or Urdu. Numerals are entered left-to-right regardless of overall page direction; only the surrounding chrome (labels, back button position) mirrors.

**Contrast (NFR-12):** digits and the entry dots must clear 4.5:1 against the pad background in both light and dark contexts. This is the kind of small, high-repetition UI element where a low-contrast choice is easy to miss in design review and painful once shipped, since it's used on every profile switch.

**No numeric keyboard autofill or browser-saved-value suggestion.** A saved PIN suggestion defeats the control's purpose — it would let a sibling's device offer up a PIN it has seen before.

---

## Age Band Badge

Used on: [Profile picker](screens/profile-picker.md), [Profile create/edit](screens/profile-create-edit.md), [Guardian dashboard](screens/guardian-dashboard.md).

Displays one of the six age bands from FR-CRS-06 (5–8, 9–12, 13–15, 16–17, 18+, All ages) against a learner profile, derived from date of birth. Never editable from this component — date of birth correction is admin-only (FR-FAM-07), reached only from [Admin — DOB correction](screens/admin-dob-correction.md).

---

## Profile State Indicator

Used on: [Guardian dashboard](screens/guardian-dashboard.md), [Profile picker](screens/profile-picker.md) (active/never-activated profiles only — inactive and deleted profiles do not appear in the picker).

Four states, per [3I-IDA-DM-001](../data-model.md): Active, Never activated, Inactive (Cancelled), Deleted.

**Inactive and Deleted must be visually distinct, not variants of the same "greyed out" treatment.** One preserves every record; the other destroys most of them. A guardian scanning the dashboard should not need to open a profile to know which kind of gone it is.
