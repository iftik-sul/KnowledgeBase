---
project: 3i
type: decision
status: current
updated: 2026-08-16
id: 3I-DEC-004
tags: [decision, infrastructure, integration]
---

# Video Is Hosted on Bunny Stream

## Context

Course delivery is video-heavy. Hosting, transcoding, and delivery were modelled across candidate providers, principally Bunny Stream against Amazon's CDN offering, at projected library size and viewing volume.

## Decision

**Bunny Stream**, selected on cost modelling at the projected scale.

## Consequences

- Transcoding and adaptive delivery are the provider's concern, not the application's.
- Access control depends on the provider's token signing rather than on application-served media, so an authorisation failure is a signing failure. This must be tested against the learner-context rule in [3I-DEC-001](dec-001-learner-as-unit-of-study.md), not against session identity.
- Delivery cost scales with viewing rather than with storage, which matters for a subscription business where a small number of learners may view heavily.

## Cost

The cost advantage holds at the modelled scale. It was not evaluated for a materially larger library or a materially different viewing distribution, and the model should be re-run before either is assumed.

Provider lock-in is real: video identifiers, transcoding profiles, and signing are all Bunny-shaped. Migration would touch every lesson record.
