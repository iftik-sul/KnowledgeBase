---
project: 3i
type: decision
status: current
updated: 2026-08-18
id: 3I-DEC-019
tags: [decision, localisation, safeguarding]
---

# Safeguarding Strings Are Exempt From AI Translation

## Context

FR-LOC-02 makes static UI translations AI-generated and stored, editable by admin. That is appropriate for "Save changes".

It is not appropriate for the under-13 registration block. FR-AUTH-03 requires that message to be **neutral and not to disclose the threshold in a way that invites retry** — a requirement about tone and implication, in five languages including two nobody on the build team reads. A mistranslation either teaches a child to amend their birth year or reads to a parent as an accusation.

## Decision

**A defined safeguarding string set bypasses AI translation and requires named human sign-off per language before launch.** Taken 2026-08-18.

The set:

| String | Requirement |
| :---- | :---- |
| Under-13 registration block message | FR-AUTH-03 |
| Guardian notification on 13–17 registration | FR-AUTH-05 |
| Safety contact copy, in-app and on the website | FR-CHAT-15 |
| Profile deletion confirmation | FR-FAM-10, [3I-DEC-016](dec-016-deletion-removes-content-retains-record.md) |
| Filtered-message notice | FR-CHAT-11 |
| Report-a-message flow copy | FR-CHAT-10 |

Roughly a dozen strings across five languages.

## Reasoning

These are the strings where a translation error causes harm rather than confusion. Everything else in the UI fails visibly — a mistranslated button label gets reported. A safeguarding message that reads slightly wrong in Urdu fails silently, to the people least able to report it.

The institute teaches Arabic, Urdu and Bangla speakers and has native speakers available. This is an afternoon of their time, not a translation budget.

## Consequences

- The string catalogue marks these entries as protected. FR-LOC-02's admin editing still applies — an admin can correct them — but they are never machine-generated in the first place.
- Sign-off is recorded per language per string set, and re-run when any of these strings changes. This pairs naturally with NFR-27's social media minimum age self-assessment, which is already re-run whenever social features change.
- Launch cannot proceed with an unsigned language. That is a deliberate gate.

## Cost

Adding a sixth language later carries this cost again, and it is a real dependency on the client rather than on us. Worth naming in the launch checklist so it is not discovered late.
