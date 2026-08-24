---
project: 3i
type: standard
status: current
updated: 2026-08-24
tags:
  - mobile
  - cross-cutting
  - scope
---

# Mobile Scope

**This is the authoritative record of which screens exist as native Flutter mobile screens, and why.** Module `ui/README.md` files add a `Mobile (Flutter)` column to their role × screen matrix and link here rather than restating the reasoning — see [documentation-standards.md](/documentation-standards.md) on why a restated rule goes stale silently.

31 of the project's 67 documented screens are in scope for Flutter. The remaining 36 are web-only — either admin/instructor desk-work never intended for a phone, or (for `commerce`) deliberately excluded under [app-store-compliance.md](app-store-compliance.md).

---

## 1. How This Was Decided

Two modules — `materials` and `commerce` — already declared their mobile scope directly in their own `ui/README.md` files when written (`commerce` deliberately excludes everything except Subscription Status, per FR-BILL-02; `materials` includes offline/video/document consumption because that's the point of a companion app). The other eleven modules were silent.

Each remaining screen was assessed against one question: **does this action plausibly happen on a phone, in a household where the primary device may be a guardian's phone or a shared tablet rather than a laptop** — not "would a desktop version also work," which is true of nearly everything.

## 2. Scope by Module

| Module | Mobile | Total | Which screens |
| :---- | ----: | ----: | :---- |
| `identity-and-access` | 11 | 14 | All except the 3 admin-only screens (name unlock, DOB correction, TOTP setup) |
| `commerce` | 1 | 9 | Subscription status only — see [app-store-compliance.md](app-store-compliance.md) |
| `catalogue` | 3 | 6 | Catalogue browse, Course detail, Rate & review |
| `materials` | 4 | 5 | All except Material upload/manage (instructor authoring) |
| `assessment` | 2 | 7 | Take exam, Exam result |
| `learning-delivery` | 2 | 4 | Enrol & waitlist, Batch roster & attendance |
| `certification` | 1 | 3 | Certificate detail/download |
| `instructors` | 2 | 4 | WWCC renewal, Instructor application |
| `communication` | 5 | 7 | Chat room, Report message, Notification centre, Notification preferences, Instructor room management |
| `public-site` | 0 | 3 | None — marketing/SEO content, served as crawlable web pages |
| `localisation` | 0 | 2 | None — admin-only |
| `reporting` | 0 | 2 | None — admin-only |
| `platform` | 0 | 1 | None — admin-only |
| **Total** | **31** | **67** | |

## 3. Decisions Worth Recording

A few of these were genuine tradeoffs, not obvious calls, and are worth keeping the reasoning attached to rather than just the outcome:

**Registration is in scope for mobile** (Registration — adult, Registration blocked — under 18, Email verification). This was initially assumed excluded by the "read-only companion" framing in [app-store-compliance.md](app-store-compliance.md#2-why-this-exists) — that framing describes *the paid relationship* staying web-only, not account creation itself. Registration and payment are separable: a Member can create an account and profiles natively, and only be routed to web for the checkout step itself, which stays governed by FR-BILL-02 exactly as before.

**Take exam is in scope for mobile**, despite exams being timed with a negative-marking cap and including free-text questions ill-suited to a phone keyboard. The platform teaches from age five, and younger age bands (5–8, 9–12) may only have access to a household tablet or a guardian's phone, not a laptop — excluding exams from mobile would have been an access barrier for exactly the learners this platform is built for, not just a convenience gap.

**Instructor application is in scope for mobile**, matching WWCC renewal (already mobile) — both are document-heavy flows (WWCC number, credentials, certificate images) where camera-based capture is often easier than desktop scanning. Excluding the initial application while including renewal would have been inconsistent for no clear reason.

## 4. What This Does Not Change

- **FR-BILL-02 and the no-purchase-surface rule are unaffected.** Registration reaching mobile does not reopen commerce — checkout, plan changes, and cancellation stay exclusively web, per [app-store-compliance.md](app-store-compliance.md).
- **The 31/67 split is a scope decision, not a design-priority order.** It says which screens eventually need a Flutter design; it says nothing about which get built first.

## 5. Open

None against this document. Each module's `ui/README.md` has been updated to add its `Mobile (Flutter)` column and link here.
