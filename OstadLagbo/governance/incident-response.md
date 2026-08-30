---
project: OstadLagbo
type: incident-response
status: current
updated: 2026-08-30
id: OL-INC-001
approved: 2026-08-30
owner: Iftikher
---

# Incident Response Process

Internal playbook for when things go wrong. Written for the actual responder — currently one person — as checklists to follow under stress, not process theater. Required before soft launch (risk R-03); operationalizes the breach-notification duty of the Personal Data Protection Act, 2026. Every action taken under this process is recorded in the audit log (ADM-17); legal holds triggered here follow the Retention Policy (OL-RET-001).

## Severity levels

- **SEV-1 — Someone may be in danger, or identity data is exposed.** Drop everything. Act within the hour.
- **SEV-2 — Serious harm alleged or platform integrity attacked, no immediate danger.** Act same day.
- **SEV-3 — Contained violation.** Normal moderation flow (ADM-07); this playbook doesn't apply.

When unsure between levels, treat it as the higher one.

## Playbook 1 — Safety incident

*A report alleges real-world harm connected to a platform connection: assault, threat, stalking, a minor endangered, fraud with real losses.*

1. **Read the full report and the cited chat context immediately.** If the report suggests danger is ongoing or imminent — advise the reporter, in plain language, to contact police (999) now. The platform is never the substitute for emergency services, and say so.
2. **Freeze:** suspend the reported account (ADM-08). Suspension is reversible — err toward suspending on credible allegation; reinstating later costs nothing compared to a second victim.
3. **Preserve:** place a legal hold (OL-RET-001) on both accounts' data — profiles, the chat thread, offer history, identity documents. Do this before anything else can expire or purge.
4. **Document:** write a dated incident record — what was alleged, what you saw, what you did, timestamps. You will not remember details later; the record is what protects everyone including you.
5. **Cooperate:** if police or a court contacts you, follow Playbook 3. Do not conduct your own investigation beyond the platform's records, and do not mediate between the parties.
6. **Close:** resolution recorded in the reports queue; if the account is banned, banned-account retention applies; review whether the incident reveals a product gap (e.g., a missing warning) and file it as a change-request candidate.

## Playbook 2 — Data breach

*Evidence or credible suspicion that identity documents, chats, phone numbers, or other personal data were accessed or exposed improperly — including a lost admin credential.*

1. **Contain first:** revoke/rotate the compromised credential or access path; take the affected system offline if exposure is ongoing. Containment beats investigation in hour one.
2. **Assess scope:** what data categories, how many users, over what window — using the audit log (ADM-17) and infrastructure logs. Write the assessment down as you go.
3. **Notify:** the PDPA requires notifying affected users and the relevant authority. Notify **users** plainly: what was exposed, when, what we did, what they should do (e.g., beware of scam calls if phone numbers leaked). Notify the **authority** per the Act's procedure. Statutory deadlines apply — confirm the current notification window with legal counsel *now, before any incident*, and record it here. Do not delay notification to make the message more comfortable.
4. **Remediate:** fix the vulnerability; document root cause; add the fix to the risk register review.
5. **Record:** full incident timeline into a dated record; audit-logged.

## Playbook 3 — Law-enforcement or legal contact

*Police, a court, a lawyer, or a government body requests data or action.*

1. **Verify:** identify the requester and demand the legal instrument in writing (warrant, court order, formal notice). No data moves on a phone call.
2. **Preserve, don't volunteer:** place a legal hold on the referenced data immediately — preservation is always safe. Disclose only what the valid instrument specifically compels, per the Privacy Policy's public commitment.
3. **Get counsel:** for anything beyond a routine verified request, engage a lawyer before responding. The cost of one consultation is smaller than one wrong disclosure.
4. **Record:** the request, its instrument, your response, and dates — audit-logged.

## Playbook 4 — Abuse wave

*Coordinated fraud ring, fake-profile farm, review manipulation, scraping surge, or OTP-spam attack.*

1. **Measure:** confirm the pattern in analytics (ADM-12/14/15) and the SMS monitor (ADM-19) — one bad actor is moderation, a wave is an incident.
2. **Stem:** suspend the involved accounts; where the vector is technical (scraping, OTP abuse), tighten the relevant engineering limits.
3. **Sweep:** search the directories (ADM-10) for the same pattern — shared documents, sequential phone numbers, identical portfolios.
4. **Harden and record:** convert the lesson into a change request or engineering task; document the wave, accounts involved, and actions.

## Standing preparations (before soft launch)

- [ ] Confirm PDPA breach-notification deadlines and authority contact procedure with counsel; record them in Playbook 2.
- [ ] Establish the incident contact email (also closes the Privacy Policy / ToS placeholders).
- [ ] Keep an offline copy of this document and admin recovery credentials — an incident may take the dashboard down.
- [ ] Verify legal-hold and suspension tooling work end-to-end in staging before any real user exists.

## Review

Revisited after every SEV-1/SEV-2 incident, on any PDPA change, and annually. Lessons learned append to this document; they are its purpose.
