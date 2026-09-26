---
project: OstadLagbo
module: registration-and-verification
type: overview
status: current
updated: 2026-09-26
---

# Registration & Verification Module (REG)

Role selection, phone/email verification, account creation for both roles, onboarding, identity-document submission, and language preference. Shagred account creation (phone, password, OTP) lives here; the Shagred *profile* lives in [SGP](../shagred-profile/README.md).

The four layers derive in order — requirements → data model → api → ui ([project-standards](/OstadLagbo/project-standards.md)). Cross-cutting rules: [Data Model Overview](/OstadLagbo/data-model-overview.md), [API Overview](/OstadLagbo/api-overview.md), [UI Overview](/OstadLagbo/ui-overview.md). Authentication authority is fixed by [ADR-004](/OstadLagbo/decisions/adr-004-authentication-authority.md).

## Documents

| Layer | Document | ID | Status |
|---|---|---|---|
| Requirements | [registration-and-verification-requirements.md](requirements/registration-and-verification-requirements.md) | OL-REG-REQ-001 | Current |
| Data model | [registration-and-verification-data-model.md](data-model/registration-and-verification-data-model.md) | OL-REG-DM-001 | Current |
| API | [registration-and-verification-api.md](api/registration-and-verification-api.md) | OL-REG-API-001 | Current |
| UI | [registration-and-verification-ui.md](ui/registration-and-verification-ui.md) | OL-REG-UI-001 | Current |
