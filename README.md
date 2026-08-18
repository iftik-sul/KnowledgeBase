# KnowledgeBase

## Overview

KnowledgeBase is the centralized documentation repository for all software projects.

The goal of this repository is to maintain a single source of truth for project documentation, business rules, workflows, system design, APIs, UI/UX, and technical decisions.

This repository is designed to be AI-friendly, making it easy for AI assistants such as ChatGPT and GitHub Copilot to understand project context and generate accurate responses.

## Projects

- **RERAN** — active. Regulatory platform. See [RERAN/README.md](RERAN/README.md) and [RERAN/module-roadmap.md](RERAN/module-roadmap.md).
- **3i** — active. Subscription learning platform for Islamic studies, serving learners from age five. See [3i/README.md](3i/README.md) and [3i/age-and-safeguarding.md](3i/age-and-safeguarding.md).
- ERP, SkudX, LoyaltyPoints, OstadLagbo, FindYourClone — reserved placeholders. Not yet active; each real client engagement gets its own project folder when work begins (ERP in particular is a sample folder, not a specific client).

Each project maintains its own documentation while following the same documentation standards.

Projects differ in how they are documented, and those differences are declared rather than assumed. RERAN partitions by user group and works from client-supplied documents; 3i partitions by functional area and works from a baseline we wrote, because the client supplied nothing in writing. See [documentation-standards.md](documentation-standards.md#input-kinds) and each project's `project-standards.md`.

## Future Vision

This repository will later be connected to an AI Knowledge Platform that provides:

- Semantic search
- AI-powered question answering
- Automatic indexing
- Version-controlled project knowledge

The KnowledgeBase will serve as the central knowledge source for multiple AI tools, including but not limited to:

- GitHub Copilot
- ChatGPT
- Claude
- Codex
- Other AI assistants that support MCP (Model Context Protocol) or API integration
