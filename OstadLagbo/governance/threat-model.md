---
project: OstadLagbo
type: threat-model
status: current
updated: 2026-09-26
id: OL-THR-001
derived_from: /OstadLagbo/non-functional-requirements.md
owner: Iftikher
---

# Threat Model

What an attacker would go after, what stops them, and where the specification currently says "engineering default" in a place that deserves a number. Written for the person who has to choose those numbers, not as a compliance artefact.

NFR-05 sets the security baseline and NFR-06 the privacy floor; this document is the **adversarial** reading of them. It pairs with the incident playbooks (OL-INC-001), which are what happens after one of these lands.

## Assets, by what it costs to lose

| Asset | Why an attacker wants it | Loss if taken |
|---|---|---|
| **The identity vault** — NID/passport images, ID numbers, ID-holding selfies | Identity fraud, resale; the single highest-value data on the platform | Catastrophic. PDPA breach notification, every Ostad's legal identity exposed, the product's trust premise gone |
| **Ostads' exact coordinates + names + skills** | A ready-made lead list to resell or spam; **public by design**, which makes scraping the realistic attack | Ostads harassed; the platform becomes a spam vector |
| **Phone numbers** | Direct contact for fraud; revealed on connection (OFR-04) | Scam calls traced to the platform |
| **Chat content and voice notes** | Blackmail, exposure | Severe; irreplaceable |
| **The admin dashboard** | It reaches everything above at once | Total compromise |
| **The API's JWT signing key** (ADR-005) | Forges any user's session | Total compromise, silently |

## Threats

### T-1 Pin scraping — the most likely attack, and the one the design already fights
Ostad pins are deliberately public at exact precision (MAP-01), so the attack is not a breach but **enumeration**: page the discovery endpoint across viewports until the whole supply is copied.

**Existing mitigations:** clustering above the viewport cap and no list view (MAP-02, MAP-09); the radius merge into one capped read, which closed a hole where a caller could page through every Ostad within 30 km (CL-033); guest rate limits by IP; a tighter limit on the expensive fuzzy `q` parameter (MAP ui).

**Residual:** a distributed scraper with many IPs still wins slowly. That is accepted — the data is public by design, and the goal is to make bulk copying cost more than it returns, not to make it impossible.

**Needs a number (engineering, Slice 2):** the viewport cap, the per-IP and per-account request rates, and the `q` rate. Set them so a full sweep of Dhaka takes days rather than minutes, and alert on any single source approaching the cap — the alert matters more than the exact limit.

### T-2 Contact harvesting through the offer flow
Phone and verified email are revealed on acceptance (OFR-04), so an attacker wants acceptances.

- **Fake Shagred → many Ostads:** blunted because the *Ostad* chooses to accept, and by the 5-pending-offer cap (OFR-DM).
- **Fake Ostad → many Shagreds:** the more dangerous direction, since Shagreds send offers to a plausible-looking profile. This is exactly what the identity gate exists for — a fake Ostad needs a real NID and a selfie holding it to get approved, and duplicate-ID detection plus banned tombstones (REG-DM) stop cheap reuse.

**Residual:** a real person with a real ID can still behave badly. That is a moderation problem, not a security one — Playbook 1.

### T-3 Identity-vault compromise
The realistic route is not breaking encryption; it is **stealing an admin session**.

**Existing:** TOTP on every admin (ADM-20, CL-018); every identity-document view audit-logged at the data-access layer so no code path can skip it (NFR-06); rate-limited short-lived signed URLs; encryption at rest with keys outside application code (NFR-05).

**Residual and unaddressed:** there is no alert on *anomalous* admin behaviour. One admin viewing two hundred identity documents in an hour is indistinguishable, today, from a normal review day — until someone reads the audit log. **Recommend (Slice 5, with ADM analytics): an alert on identity-document views per admin per hour.** The log already holds the data; nothing watches it.

### T-4 OTP abuse — the spend and harassment vector
Each OTP costs money (CL-036) and each one rings a real phone. Two attacks: pumping cost, and harassing a specific number.

**Existing:** 5 requests per number per 24 h, 5 wrong attempts per code, 60-second resend floor (REG-02); ADM-19 monitors volume and rate-limit hits; the 18+ and consent gates run *before* the OTP is sent, so no SMS is spent on a registration that cannot complete (REG-03).

**Needs a number:** a **per-IP** OTP limit, which the spec does not have — the per-number limit alone does not stop one source cycling through thousands of numbers. Add it with the gateway integration in Slice 0, plus a daily spend ceiling that alerts.

### T-5 Account takeover
Users have password login with no second factor (admins have TOTP). Lockout is 5 failures per 15 minutes keyed on the phone string (REG ui).

**Residual, accepted:** SIM-swap defeats phone-based recovery, and no user 2FA exists in the MVP. Given what an account holds — chat history and revealed contacts, not money — this is a reasonable MVP position, but it should be a **recorded** decision rather than an omission. Revisit if the platform ever touches payments.

### T-6 Review manipulation
One rating per pair, ever, gated on a real connection, unremovable by the user (RNT-01/02/05/06). Manufacturing praise means manufacturing accepted offers between two verified accounts — expensive. Terminated accounts keep their review weight (CL-024), so a ring cannot launder its own history by getting banned.

**Watch for:** clusters of connections between the same small set of accounts. Playbook 4.

### T-7 The JWT signing key (ADR-005)
Compromise forges any session, silently, with no failed logins to notice.

**Existing:** the private key lives only in the Render environment, never in the repository (NFR-05); rotation is a zero-downtime standby→current promotion.

**Residual:** nothing detects forged-but-valid tokens. Accepted for the MVP; the mitigation is key hygiene and short token lifetimes, not detection.

### T-8 Real-world harm from a connection
The platform's purpose is to put strangers in a room together. This is the threat with the worst tail, and it is not a technical one.

**Existing:** identity verification with a live selfie for Ostads; report and block; suspension and termination; Playbook 1, which says plainly that the platform is never a substitute for emergency services.

**Note honestly:** Shagreds are **not** identity-verified — only Ostads are. The asymmetry is deliberate (it is the Ostad who is publicly listed) but it means the risk is not symmetric either, and safety guidance in-app should reflect that.

### T-9 Minors on the platform
The 18+ gate is a self-declared date of birth (REG-03). A determined minor passes it.

**Residual, accepted:** stronger age assurance would require identity documents from Shagreds, which contradicts collecting the minimum necessary. Recorded so the choice is visible. Note the tutoring context makes under-18 learners *plausible* users, which makes this more live than for most apps — a reason to keep the gate, the Terms, and Playbook 1's minor-endangerment path prominent.

## Unverified assumptions

*Tracked live in [OL-OPN-001](/OstadLagbo/governance/open-items.md).*


1. **Cloudflare's free plan rate-limiting capacity is unchecked.** ADR-001 relies on Cloudflare for "infrastructure-level request-log control and rate limiting" (NFR-05's requirement (d)), but nobody has confirmed the free plan offers enough rules, or enough granularity, to express the per-IP, per-endpoint and per-parameter limits T-1 and T-4 need. **Verify in Slice 0** — if it does not, either the limits move into the API or the edge tier becomes a cost line.
2. **Monitoring and crash-reporting tools are unnamed** (NFR-09, OL-OPS-001 open item 1). A threat you cannot see is unmitigated regardless of the controls on paper.
3. **No content filter exists** (store-release checklist, section B) — Apple Guideline 1.2 requires one, and it is also T-6's and T-8's cheapest partial mitigation.

## Moderation response commitment

Neither store publishes a numeric SLA; Apple requires *"timely responses to concerns"* and Google requires *"ongoing UGC moderation"*. Absent a stated target, "timely" becomes whatever happened. Proposed, and consistent with ADM-15's existing 48-hour review turnaround target:

| Report type | Triage target |
|---|---|
| Alleged real-world harm, a minor at risk, identity data exposed (SEV-1) | **Within 1 hour** — Playbook 1 |
| Serious harm alleged, no immediate danger (SEV-2) | **Same day** |
| Ordinary content or conduct report (SEV-3) | **48 hours**, matching ADM-15 |

These belong in the published community guidelines the store checklist requires, since a commitment nobody can read is not a commitment.

## Review

Revisited when a new data category is collected, when a payment flow is ever added, after any SEV-1 or SEV-2 incident, and annually.
