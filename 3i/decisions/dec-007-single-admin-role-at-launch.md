---
project: 3i
type: decision
status: current
updated: 2026-08-16
id: 3I-DEC-007
tags: [decision, identity, rbac]
---

# RBAC Is Fully Modelled; One Admin Role Ships at Launch

## Context

The institute will eventually need differentiated staff roles — administrators, coordinators, instructors with varying reach. Building that role structure fully at launch delays delivery to serve requirements the client has not yet had to articulate against a working system.

Deferring it entirely is worse: retrofitting role granularity onto a schema that assumed one admin means touching every authorisation check in the platform.

## Decision

**The RBAC model is complete in the schema. One admin role ships.** Expanded roles are a scheduled future milestone, not a rewrite.

## Consequences

- Authorisation checks are written against permissions from the start, never against a role name. Code that asks whether a user *is* an admin is wrong even while only one admin role exists.
- Adding a role later is configuration plus review, not schema migration plus refactor.
- The client sees a simple administration surface at launch, which is appropriate to an organisation that has not yet operated the platform.

## Cost

The discipline is invisible and therefore easy to lose. The single shipped role makes every permission check look redundant, and a developer optimising for readability may collapse them. This is the specific regression to watch for, and the reason the decision is recorded rather than assumed.
