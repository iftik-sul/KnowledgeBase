---
project: 3i
type: standard
status: current
updated: 2026-08-20
tags:
  - commerce
  - mobile
  - cross-cutting
---

# App Store Compliance

**This is the authoritative statement of the no-purchase-surface rule spanning the mobile apps.** Modules link here. They do not restate it — see [documentation-standards.md](/documentation-standards.md) on why a restated rule goes stale silently.

§22.3 risk 1 names app store rejection under Guideline 3.1.1 as **the highest-uncertainty item in the entire plan**, with 1–2 weeks of review buffer budgeted. This document exists to make that risk something the team can check against, rather than something everyone individually remembers not to break.

Referenced from [OQ-09](open-questions.md#oq-09--app-store-compliancemd-not-yet-written), which this document resolves.

---

## 1. The Rule, Stated Once

**Neither mobile app contains a purchase surface of any kind.** No prices, no "Subscribe" or "Upgrade" buttons, no links to checkout, no text — anywhere, in any string, in any of the five supported languages — directing a user to pay somewhere else.

This is not satisfied by simply omitting a Subscribe button. It means:

- No numeric price appears anywhere in either app.
- No button or link leads to, or names, the web checkout flow.
- No copy implies payment is possible or necessary ("Unlock full access", "Get more seats") without an accompanying route to act on it in-app — because there is no such route, that copy is itself the violation.
- Push notifications carry the same restriction (FR-NOT-06) — a payment-prompting notification is the same violation delivered through a different surface.

## 2. Why This Exists

Apple Guideline 3.1.1 (In-App Purchase) requires that if an app unlocks content or functionality with real-world payment, that payment must go through Apple's IAP system — Apple takes a commission. Google Play has an equivalent policy for digital goods.

3i avoids this by keeping the apps **read-only companions**: the paid relationship is established and managed entirely on the web, and the apps consume access that already exists. This is the multiplatform-services model (NFR-15–21) — it is why FR-BILL-01 puts all purchase, plan-change, and cancellation functionality on the web, and why [3I-DEC-003](decisions/dec-003-web-only-stripe-checkout.md) made that call early rather than discovering it at submission.

**The moment any purchase surface appears in the apps, this model breaks** and the fallback is Apple/Google's in-app purchase system — a different payment integration, a different cut of revenue, and a different Stripe/App Store reconciliation problem than anything currently designed for.

## 3. What the Apps Show Instead

| Scenario | Mobile behaviour |
| :---- | :---- |
| Account has no active subscription | A **neutral status message** and a **support email address** only. No URL, no price, no call to action of any kind (NFR-18) |
| Account has an active subscription | Normal app access, no billing chrome at all |
| Account's subscription is suspended (failed payment) | Same neutral treatment as "no active subscription" — the apps do not distinguish never-subscribed from lapsed, since either distinction risks becoming a prompt |
| Waiver active, capped to one profile | No visible difference from a normal paid subscription — the cap and the discount are both purely account-side state; nothing about them is mobile-visible |

See [Subscription Status screen](modules/commerce/ui/screens/subscription-status-mobile.md) for the actual spec.

**"Contact support" is the only permitted path off this screen**, and it must open the device's mail client or an in-app support form — never a web view that could itself become a checkout surface by accident.

## 4. Enforced Across Three Modules

| Module | Requirement | What it covers |
| :---- | :---- | :---- |
| `commerce` | FR-BILL-02 | The rule itself — no purchase surface in either app |
| `communication` | FR-NOT-06 | Push notifications carry no purchase prompts |
| `platform` | NFR-15–21 | The multiplatform-services submission model this rule exists to satisfy |

Each module's own requirements document links here rather than restating the rule — see [3I-CMR-REQ-001](modules/commerce/requirements/bill-subscriptions-and-billing.md#where-commerce-lives) for the commerce-side acceptance criteria this document backs.

## 5. Review and Submission Notes

- **Age rating 13+ on both stores**, developer-assigned to match the terms of service (NFR-19) — noted in [age-and-safeguarding.md](age-and-safeguarding.md#8-store-and-marketing) and repeated here because store reviewers check age rating and monetization model together.
- **Store listings and marketing copy address parents, not children** (NFR-20) — a reviewer reading the listing should never conclude the app is meant to be operated by a minor without adult involvement.
- **Screenshots submitted for review must not include any billing-adjacent screen** — the neutral status screen is acceptable to show; a hypothetical pricing screen (which should not exist) would not be.
- **1–2 weeks of review buffer is budgeted** in the schedule specifically for this risk (§22.3). If a build is rejected under 3.1.1, the fix is almost certainly a missed string or an accidentally-surfaced link, not a redesign — this document is what to check first.

## 6. What Would Break This

A short, deliberately blunt list, because these are the mistakes most likely to slip in during implementation rather than being deliberately chosen:

- A developer adds a "Manage subscription" button that deep-links to the web billing portal, thinking it's a convenience. **This is the violation** — any link that leads toward payment, even indirectly, counts.
- A translator renders the neutral status message in a way that implies urgency to pay ("Your access has expired — renew now"). The English source string must be written so that a faithful translation cannot drift into this, and per [3I-DEC-019](decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md)'s logic for safeguarding strings, this string is a strong candidate for the same human-translation treatment even though it is not itself a safeguarding string — worth a decision if it isn't already covered.
- A push notification reminds a lapsed subscriber that they're missing content, without technically naming a price. Still a violation under FR-NOT-06's spirit even if it passes a literal keyword check.

## 7. Open

None against this document itself. It resolves [OQ-09](open-questions.md#oq-09--app-store-compliancemd-not-yet-written) in full.

One item raised while writing it, not yet decided: whether the neutral status string (§3 above) should join the safeguarding-strings exempt-from-AI-translation set ([3I-DEC-019](decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md)), given how easily a mistranslation could turn "neutral" into "urgent." Worth a quick decision before that string is actually written, not a blocker to this document.