# pm-ai-shipping — AI Shipping Kit

For PMs and founders accountable for AI-built code. Build an MVP from a finished PRD, document a vibe-coded app, audit it for intended-vs-implemented security gaps and performance issues, and produce a reviewer-ready shipping packet.

## Overview

AI agents write code fast but leave no record of *intent* — what the system should do, who may do what, where the secrets live. Without that record, no human and no auditing agent can tell whether the code is safe to ship. This kit covers the build and the accountability: turn a finished PRD into a working, deployed app in one disciplined pass, then restore reviewability — document the system and audit the gap between what the docs say and what the code does, the class of bug generic scanners miss because they have no model of intent.

Start with `/ship-mvp` to build from a PRD, `/ship-check` for the full audit sequence, or run a single stage with the specialist commands.

## Install

Install from the [pm-skills marketplace](https://github.com/phuryn/pm-skills) and enable the `pm-ai-shipping` plugin. Each command can be triggered with `/pm-ai-shipping:<command>` or its short `/<command>` form; skills auto-load when the topic matches.

## Skills (3)

- **shipping-artifacts** — The durable documentation set that makes an AI-built app reviewable: a core every app needs (architecture, user/permission flows, permissions, variables/secrets, test-coverage map) plus conditional docs added only when they apply (emails, cron, SEO, embedded agents/automation). Defines what each doc must capture and how a reviewer uses it.
- **intended-vs-implemented** — The method for finding the gap between what a system is documented to do and what the code actually does, with cited evidence on both sides and without hand-wavy findings.
- **prd-to-mvp** — The method for turning a finished PRD or spec into a working, deployed app in one disciplined pass: settle the decisions an AI agent must never guess, sequence the build as a walking skeleton, choose the backend path (including a temporary backend the agent creates when none exists), and deliver a live URL with an honest build report.

## Commands (6)

- `/pm-ai-shipping:ship-mvp` — Turn a finished PRD or spec into a working, deployed app in one disciplined pass: settle the pre-build decisions, build the core journey as a walking skeleton, provision the backend when one is needed, verify the acceptance walkthrough, and deliver a live URL with an honest build report.
- `/pm-ai-shipping:ship-check` — Turn a vibe-coded repo into a reviewer-ready shipping packet: document, wire agent context, run security and performance audits, map test coverage, and compile the results.
- `/pm-ai-shipping:document-app` — Reverse-engineer a codebase into the system documents reviewers and auditors need — a core set (architecture, flows, permissions, variables) plus conditional docs (emails, cron, SEO, automation) when they apply.
- `/pm-ai-shipping:derive-tests` — Turn documented intent into a test-coverage map: inventory the tests that exist today, separate them from proposed tests and unverified gaps, mark each unit / guarded-live / manual, and recommend a green-before-merge CI gate.
- `/pm-ai-shipping:security-audit-static` — Static security audit: map trust boundaries, cross-reference documented intent, self-refute every finding, and report only evidence-backed risks.
- `/pm-ai-shipping:performance-audit-static` — Static performance audit: find N+1 queries and request waterfalls, over-fetching, missing indexes, and caching opportunities, ranked by effort and impact.

## Author

Paweł Huryn — [The Product Compass Newsletter](https://www.productcompass.pm)

## License

MIT
