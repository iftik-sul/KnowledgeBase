---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-015
tags: [decision, identity, devices]
---

# Device Allowance Scales With Seats

## Context

FR-AUTH-11 caps devices at 3 per account. FR-AUTH-12 caps concurrent streams by seats purchased. A family buying five seats cannot use them from three devices — seats four and five are structurally unusable.

## Decision

**Device allowance is seats plus two, with a floor of three.** Taken 2026-08-18.

| Seats | Devices |
| ----: | ----: |
| 1 | 3 |
| 2 | 4 |
| 3 | 5 |
| 6 | 8 |

The swap limit is unchanged: **twice per 30 days** (FR-AUTH-11). Devices remain visible and de-authorisable by the account holder.

## Reasoning

The argument is not convenience. Selling a seat that cannot be used by anyone is a consumer problem, and **FR-REF-05 already acknowledges that Australian Consumer Law guarantees apply regardless of policy terms.** A structurally unusable seat is not something the refund policy can write its way out of.

The plus-two allows for a shared household device and a guardian's own phone alongside one device per learner. A family of six children plausibly has six tablets, a parent's phone, and a laptop.

## Scope

FR-AUTH-11 states a flat 3. Making it variable is a change requiring sign-off under §21.3.

## Consequences

- The device management screen shows a total that changes when seats change. Cancelling a seat lowers the allowance — if the account is over the new limit, devices must be de-authorised before another can be registered, and the message should name which.
- The acceptance criterion in §5 refers to "a fourth device registration" being refused. That criterion now applies at the account's current allowance, not at a fixed four.

## Cost

A variable limit is harder to explain than a fixed one, and support will field questions about why the number moved. Worth stating the formula plainly in the UI rather than showing only the current total.
