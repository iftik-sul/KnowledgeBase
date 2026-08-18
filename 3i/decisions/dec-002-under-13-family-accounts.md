---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-002
tags: [decision, compliance, safeguarding]
supersedes: dec-002-guardian-held-accounts.md
---

# Under-13s Exist Only as Profiles

## Context

The platform teaches from age five. Australian privacy law, GDPR where relevant, and both store policies constrain what may be collected from a child and who may consent.

Issuing accounts to children would require verifiable parental consent flows, child-specific data minimisation, and Kids/Families programme exposure on every store release.

## Decision

**Under-13 learners cannot register by any route, including social login** (FR-AUTH-03). They exist only as learner profiles under an account held by someone 18 or over (FR-FAM-01). Under-13 independent accounts are explicitly out of scope (§23 item 19).

**13–17 is different.** A 13–17 learner *may* hold a standalone account, with guardian name and email captured and the guardian notified automatically (FR-AUTH-05). They may equally exist as a profile. Both are supported.

## Consequences

- Consent sits with the guardian, where it is legally meaningful.
- A profile holds no email and no credentials (FR-FAM-03), so there is no independent contact channel to a child.
- Date of birth on a profile is not user-editable (FR-FAM-07). This is the control preventing a chat restriction being lifted by editing a field.
- Blocked registrations are recorded against a hashed session identifier, so a retry with an amended birth year is identifiable (FR-AUTH-04).
- Store marketing addresses parents rather than children (NFR-20), keeping the apps out of the Families and Kids programmes.

## Cost

The 13–17 band supports two different shapes for the same person, and they do not behave identically — chat permission, enrolment authority, and seat consumption all differ. Any feature touching this band must be specified for both. See [3I-DEC-008](dec-008-ageing-up-at-13.md).

## Correction

An earlier version of this decision stated that children never hold accounts. That is true under 13 and false for 13–17, who may log in. The error came from writing before reading §3 of the baseline.
