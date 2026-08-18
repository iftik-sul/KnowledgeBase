---
project: 3i
type: decision
status: current
updated: 2026-08-16
id: 3I-DEC-003
tags: [decision, billing, compliance]
---

# Checkout Is Web-Only, via Stripe

## Context

3i is subscription-based and ships a Flutter mobile application. Apple App Store Guideline 3.1.1 requires in-app purchase for digital content consumed within an app, and forbids steering users to external payment from inside the app.

Routing subscriptions through in-app purchase would surrender the commission, fragment the subscription record across Apple, Google, and Stripe, and make seat-based pricing and waivers difficult to express.

## Decision

**Subscription checkout happens on the web only, through Stripe.** The mobile applications do not sell. Pricing is seat-based. Waivers are implemented as a four-tier system using fixed Stripe coupons rather than bespoke discount logic.

## Consequences

- One subscription record, in one system, for every customer regardless of platform.
- Seat-based pricing and the waiver tiers are expressed in Stripe primitives, so finance reporting comes from Stripe rather than from application code.
- The mobile app must handle an unsubscribed state gracefully without offering a purchase path — and without language that reads as steering, which is itself a review risk.

## Cost

Mobile conversion is worse than it would be with in-app purchase. This is accepted deliberately: the alternative costs commission on every seat and splits the billing record three ways.

Fixed coupons mean a new waiver tier is a Stripe configuration change, not a deployment. It also means the four tiers are the four tiers — arbitrary per-customer discounting is not supported, and should not be promised.
