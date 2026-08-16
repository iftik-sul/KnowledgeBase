---
project: 3i
type: decision
status: current
updated: 2026-08-16
id: 3I-DEC-002
tags: [decision, compliance, identity]
---

# Minors Are Reached Through Guardian-Held Accounts

## Context

3i's learner base includes children below the age at which an account can lawfully be issued directly. Australian privacy law, COPPA, and both app store policies constrain what may be collected from a child, what consent is required, and who may give it.

Issuing accounts to children directly would require verifiable parental consent flows, child-specific data minimisation, and store review exposure on every release.

## Decision

**Children do not hold accounts. Guardians do.** A guardian account carries one or more learner profiles. Registration is age-gated: a date of birth below the threshold routes to guardian registration rather than to learner registration.

Communication follows the same principle. A guardian participates in chat on behalf of their child, and a room containing any guardian-represented learner switches automatically to guardian-only mode. Profanity filtering runs across five languages.

## Consequences

- Consent is held against the guardian, where it is legally meaningful.
- Data collected about a child is limited to what study requires. No independent contact details, no independent login credentials.
- Chat moderation is structural rather than reactive. A room does not have to be policed into safety after the fact; it is guardian-only by construction whenever a minor is present.
- The billing party and the studying party are different entities. See [3I-DEC-001](dec-001-learner-as-unit-of-study.md).

## Cost

Automatic guardian-only mode is a blunt instrument: one guardian-represented learner changes the room for every participant, including adults. This is deliberate — the alternative is a per-message check that fails open. It should be stated plainly to the client rather than discovered by them.

## Open

The age threshold varies by jurisdiction. The configured value and whether it is single or per-region must be confirmed against the SRD before implementation is treated as settled.
