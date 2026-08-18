---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-007
tags: [decision, rbac, identity]
supersedes: dec-007-single-admin-role-at-launch.md
---

# No Hard-Coded Role Checks

## Context

The institute will eventually need differentiated staff roles. Building that structure fully at launch serves requirements the client has not yet had to articulate against a working system. Deferring it entirely means retrofitting granularity onto a schema that assumed one admin.

## Decision

**Permissions are the unit of authorisation. Roles are collections of permissions, held as data** (FR-RBAC-01, FR-RBAC-04). Adding a role requires no code change and no deployment.

Three roles are seeded: admin, instructor, and account holder. **Sub-admin roles and the wider permission matrix are deferred** (§23 item 5), with the RBAC foundation built.

Admin accounts support optional TOTP two-factor authentication (FR-RBAC-05).

## Consequences

- The acceptance criterion is absolute: no occurrence of `isAdmin`, `role === 'admin'`, or equivalent exists anywhere in application logic.
- Every route returns 403 when the required permission is absent.
- A new role created in the database with a subset of permissions behaves correctly without deployment.
- Adding roles later is configuration and review, not migration and refactor.

## Cost

The discipline is invisible. With only three coarse roles shipped, every permission check looks redundant, and a developer optimising for readability may collapse them. That is the specific regression to watch for, and the reason this is recorded rather than assumed.

## Correction

An earlier version stated one admin role ships. Three roles are seeded; it is *sub-admin* roles that are deferred.
