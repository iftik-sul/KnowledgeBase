---
project: OstadLagbo
type: requirements
status: current
updated: 2026-09-12
id: OL-NFR-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.2.md
owner: Iftikher
---

# Non-Functional Requirements

Cross-cutting quality targets every module inherits. Each is a testable target, not an aspiration; "engineering default" marks values the builder may tune without founder re-approval. Grounded in the Bangladesh device and network market the platform actually serves.

## NFR-01 Device and platform floor

Android **8.0 (API 26)** and above; iOS **15** and above. The app must be fully usable on a **2 GB-RAM, entry-level Android device** — the reference test device class for every performance target below. Screen support from 5-inch 720p upward; portrait-first, no landscape requirement in MVP. Download size ≤ 40 MB (engineering default).

## NFR-02 Performance on the reference device

Cold start to map ≤ 3 s. Map first pins visible ≤ 2 s on 4G, ≤ 5 s on 3G. Profile open ≤ 2 s. Screen transitions < 300 ms. Chat message send-to-delivered ≤ 2 s on 4G. Search typeahead results < 500 ms. Images served in responsive sizes; never full originals to list views.

## NFR-03 Network resilience

The app assumes intermittent 3G/4G. Every submit (onboarding stage, offer, message, ticket) survives a dropped connection: queued locally, retried with backoff, never silently lost. The last-loaded map view and open chats remain readable offline with a clear offline indicator. OTP entry tolerates delayed SMS (resend per REG-02). No screen dead-ends on network failure — every error state offers retry.

## NFR-04 Media and storage budgets

Per-Ostad ceilings, consistent with OSP-07: images compressed client-side to ≤ 500 KB each; intro video ≤ 20 MB after compression (≤ 720p, 45 s); documents ≤ 10 MB each; voice notes compressed (Opus-class, ~24 kbps → a 2-minute note ≈ 400 KB). Media is served via short-lived signed URLs, never public buckets; identity-document objects are never URL-addressable outside admin review. Storage growth per 1,000 Ostads must stay within the cost posture (NFR-13).

## NFR-05 Security baseline

TLS 1.2+ everywhere; no plaintext endpoints. Identity vault objects and ID numbers encrypted at rest (AES-256-class or provider-managed KMS) with keys outside application code. Passwords hashed with a memory-hard/strong algorithm — **Argon2id, scrypt, or bcrypt**; user-account passwords use **scrypt** as the authentication authority specifies (ADR-004), admin passwords any of the three; OTP codes stored hashed only. Secrets in a secret manager or environment — never in the repository. Rate limiting on OTP, login, search, and viewport queries (REG-02, MAP-03). Audit log append-only at the storage level, not merely by convention. Dependency vulnerability scanning in CI. **Admin dashboard requires a second factor (TOTP)** in addition to email + password (ADM-20, CL-018) — the panel holds identity documents; a single stolen password must not open it.

## NFR-06 Privacy by design

No personal data in application logs, crash reports, or analytics payloads: analytics use pseudonymous account IDs, never phone, name, or location; user positions are never logged (MAP-10). Crash reporting scrubs PII. Every identity-document read is audit-logged (ADM-17) at the data-access layer so no code path can bypass it.

## NFR-07 Backup and recovery

Daily automated backups; **backups retained no longer than 90 days** so purged data ages out per OL-RET-001. Recovery point objective 24 h; recovery time objective 24 h. A full restore is rehearsed in staging before soft launch and repeated quarterly.

## NFR-08 Availability and capacity

Target 99.5 % monthly availability in MVP; planned maintenance announced by broadcast (ADM-16). Architecture must serve, without redesign: **1,000 approved Ostads, 20,000 Shagreds, 500 concurrent users**, and the map/search query load that implies. Beyond that scale, a capacity review — not an emergency.

## NFR-09 Observability

Crash reporting on both platforms; error tracking with alerting for backend failures; uptime monitoring with alerts to the founder; structured logs (PII-free per NFR-06). The founder can answer "is the app up and are users failing at anything" within five minutes from a phone.

## NFR-10 Accessibility and inclusivity

Touch targets ≥ 44 dp; text respects OS font scaling without layout breakage; color contrast WCAG AA; interactive elements labeled for screen readers on registration, onboarding, map, offers, and chat. **Bangla rendering is complete** — conjunct consonants, vowel signs, and numerals render correctly on the reference device with the chosen Bangla typeface (tested, not assumed).

## NFR-11 Localization mechanics (CL-016)

Every user-facing string externalized to locale files; no string concatenation that breaks under Bangla word order; dates and times localized; phone numbers and OTP codes always in Latin digits (engineering default); language switch applies without restart where feasible. Missing-translation fallback is English, flagged in CI so no Bangla string ships missing.

## NFR-12 Platform and store compliance

Minimal permissions — location (foreground only), camera, microphone (voice notes), notifications — each requested in context with a rationale screen, never at first launch as a wall. Data-safety and privacy-nutrition disclosures accurate to the Privacy Policy. Push delivery via the standard platform services.

## NFR-13 Cost posture

Every infrastructure choice is free or free-tier-viable at MVP scale (NFR-08) and degrades to predictable pay-as-you-grow; no commitment contracts; the monthly infrastructure ceiling is set in the budget document and monitored via the admin SMS monitor (ADM-19) and provider billing alerts.

## NFR-14 Quality and maintainability

Automated tests cover every acceptance criterion of Slices 0–3 (OL-BLD-001) before soft launch; CI runs tests, linting, and dependency scans on every change; the codebase lives in the founder's GitHub with the knowledge base as its specification of record. Any deviation from a requirements document is raised as a gap, never silently coded around (per project standards' AI-agent notes).

## Founder-approval boundary

Values marked engineering default may be tuned by the builder. The device floor, the reference device class, capacity targets, backup retention, admin second factor, and the cost posture change only with founder approval and, where user-facing, a change-log entry.
