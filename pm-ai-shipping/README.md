# pm-ai-shipping — AI Shipping Kit

For PMs and founders accountable for AI-built code. Document a vibe-coded app, review it for correctness, security and performance defects, and produce a reviewer-ready shipping packet.

## Overview

AI agents write code fast but leave no record of *intent* — what the system should do, who may do what, where the secrets live. Without that record, no human and no auditing agent can tell whether the code is safe to ship. This kit restores reviewability: it documents the system, then audits the gap between what the docs say and what the code does — the class of bug generic scanners miss because they have no model of intent.

Start with `/ship-check` for the full sequence, or run a single stage with the specialist commands.

Folders and file names are defaults. The kit follows the repo's own setup — its agent instructions, its docs folder, and the documents and test-coverage file it already has — and falls back to `documentation/`, `documentation/tests.md` and `reports/` only where the repo has none, saying so in its output.

## Install

Install from the [pm-skills marketplace](https://github.com/phuryn/pm-skills) and enable the `pm-ai-shipping` plugin. Each command can be triggered with `/pm-ai-shipping:<command>` or its short `/<command>` form; skills auto-load when the topic matches.

## Skills (3)

- **shipping-artifacts** — The durable documentation set that makes an AI-built app reviewable: a core every app needs (architecture, user/permission flows, permissions, variables/secrets, test-coverage map) plus conditional docs added only when they apply (emails, cron, SEO, embedded agents/automation). Defines what each doc must capture and how a reviewer uses it.
- **code-review** — The top-level review skill. Correctness is its core; **performance and security are optional sub-cases** of the same engine. Anchors on agreements between participants across a boundary — the defects that are invisible file-by-file because each side looks reasonable alone — forces a violating execution, and refutes every candidate before reporting.
- **intended-vs-implemented** — The method for finding the gap between what a system is documented to do and what the code actually does, with cited evidence on both sides and without hand-wavy findings.

## Commands (5)

- `/pm-ai-shipping:ship-check` — Turn a vibe-coded repo into a reviewer-ready shipping packet: document, wire agent context, run correctness, security and performance reviews, add an independent unsteered pass by a second model, map test coverage, and compile the results.
- `/pm-ai-shipping:document-app` — Reverse-engineer a codebase into the system documents reviewers and auditors need — a core set (architecture, flows, permissions, variables) plus conditional docs (emails, cron, SEO, automation) when they apply.
- `/pm-ai-shipping:derive-tests` — Turn documented intent into a test-coverage map: inventory the tests that exist today, separate them from proposed tests and unverified gaps, mark each unit / guarded-live / manual, and recommend a gate that follows the repo's stated gate policy (a green-before-merge CI gate where it states none).
- `/pm-ai-shipping:security-audit-static` — Static security audit: map trust boundaries, cross-reference documented intent, self-refute every finding, and report only evidence-backed risks.
- `/pm-ai-shipping:performance-audit-static` — Static performance audit: find N+1 queries and request waterfalls, over-fetching, missing indexes, and caching opportunities, ranked by effort and impact.

## Author

Paweł Huryn — [The Product Compass Newsletter](https://www.productcompass.pm)

## License

MIT
