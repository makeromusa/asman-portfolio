---
title: "Architecting My Engineering Portfolio: Following Industry SDLC"
date: "2026-10-21"
excerpt: "Why jumping straight into code is a trap, and how adhering to formal software engineering phases transformed my portfolio build."
tags: ["Engineering & Architecture", "SDLC", "Next.js"]
published: true
---

# Architecting My Engineering Portfolio: Following Industry SDLC

Most developers begin a portfolio project by opening a code editor and randomly tweaking CSS styles until something looks presentable. While tempting, this chaotic approach frequently leads to bloated architectures, inconsistent design patterns, and projects that remain unfinished for months.

For this engineering portfolio, I chose a different path: **following a structured Software Development Life Cycle (SDLC)** from day one.

---

## Phase 1: Requirements Gathering & MoSCoW Prioritization

Before touching a terminal or writing a component, I conducted a formal requirements elicitation:
- **Target Audience:** Recruiters, hiring managers, and prospective collaborators.
- **Functional Requirements:** Type-safe project showcases, dynamic category filters, contact pipeline with email delivery, and a markdown-powered publishing system.
- **MoSCoW Prioritization:** Separating *Must-Haves* (core responsive UI, dark/light mode, contact API) from *Could-Haves* (comments, multi-language) to prevent scope creep.

---

## Phase 2: System Architecture & Blueprints

Once requirements were signed off, I mapped out the system design:
1. **Frontend Architecture:** Next.js 15 App Router with TypeScript for strict type checking.
2. **Styling & Theming:** Tailwind CSS combined with `next-themes` to support system-aware and manual dark mode toggling.
3. **Data Layer Strategy:** Instead of introducing heavy database dependencies for a static portfolio, all data models (projects, skills, testimonials) were designed as version-controlled TypeScript schemas.
4. **Content Layer:** File-based MDX/Markdown parsing using frontmatter extraction, enabling lightning-fast build-time pre-rendering.

```
Request → Next.js App Router → Static Pre-Render (SSG) → Global CDN
```

---

## Phase 3: Modular Implementation & Continuous Validation

By breaking the build into distinct sprints, each component had a clear **Definition of Done**:
- Reusable UI primitives (`SectionHeading`, `SocialLinks`, `BackToTop`).
- Isolated section modules (`HeroSection`, `ProjectsSection`, `SkillsSection`).
- Robust API route handling for `POST /api/contact` featuring server-side sanitization and error handling.

Every sprint was validated with production builds to catch TypeScript discrepancies and prerendering edge cases before they compounded.

---

## Key Takeaway

Adopting industry software engineering practices doesn't slow development down — it accelerates it. When every requirement is documented and every interface is specified in advance, coding becomes an exercise in precision rather than guesswork.
