# Changelog

## Unreleased

### pm-execution

- **create-prd** is now lean by default: a first PRD is about one to two pages, with the detailed version on request. Feedback was that the skill fought itself, asking for a "comprehensive" document and for brevity at the same time. "Complete" now means no gap that blocks a decision about the first version; the section questions are a checklist to pick from rather than a form to fill; Market Segments and Value Propositions are always included; unknowns go to Assumptions and open questions instead of being invented; it asks up to three questions when the problem, the users, or the success metric is missing; it researches the market, competitors, and alternatives freely, citing sources, and puts a finding in the PRD only when it changes a decision; and it ends by naming what it left out so you can expand any section. The Value Proposition section now uses the 6-part JTBD template (Who, Why, What before, How, What after, Alternatives, by Paweł Huryn and Aatir Abdul Rauf), one per segment (two or three segments at most for a first version), and is the spine of the PRD: the Solution delivers its How and the Key Results measure its What after. It also gained a short checklist for reviewing an existing PRD.
- **`/write-prd`** now uses the create-prd template. It had carried its own, different 8-section template while also invoking the skill. It asks at most three questions up front.

### pm-ai-shipping

- Added the **code-review** skill: correctness is the core engine, with performance and security as optional sub-cases of it rather than separate methods. It anchors on agreements between participants across a boundary — the defects that stay invisible file-by-file because each side reads as reasonable alone — forces a violating execution, and refutes every candidate before reporting.
- Added a correctness taxonomy reference built from real fix history, plus performance and security reference sheets the same engine reads.
- `/ship-check` gained a correctness review as Step 3, before the security and performance audits, and an independent unsteered pass by a second model as Step 6.
- `/security-audit-static` gained an OWASP Top 10 coverage backstop: every surviving finding is mapped to a category, and any category with zero findings is flagged "not covered — double-check" rather than silently passing. It is a coverage check, not a mandate to invent findings.
- Docs, the test-coverage map and reports now follow the host repo's setup. Before writing, the kit reads the repo's agent instructions (`AGENTS.md`, `CLAUDE.md` and what they import), its docs folder, and any existing equivalent of each document under any name; it updates those instead of creating parallel files and keeps their naming and date conventions. `documentation/`, `documentation/tests.md`, `reports/` and the default file names apply only where the repo has none, and the output says so. It never creates a file that differs from an existing one only in letter case (`tests.md` beside `TESTS.md`), which collides on Windows and macOS. The rule lives once, in the **shipping-artifacts** skill.
- `/ship-check` edits the agent instruction file the repo already uses. Where one of `CLAUDE.md` and `AGENTS.md` only imports or points to the other (a `CLAUDE.md` that is just `@AGENTS.md`), it edits the file pointed to and leaves the pointer alone; where only one exists, it edits that one. `CLAUDE.md` plus a thin `AGENTS.md` is created only in a repo with neither.
- The independent review in `/ship-check` Step 6 is a fresh session of a model family different from the one that built the code, using the reviewer the repo's own instructions name. It no longer names a specific model as the usual choice.
- `/derive-tests` defers to the repo's stated gate policy. A repo whose instructions make the gate a local command plus a human go keeps that: the coverage map records the policy and whether the deterministic tests run inside it, instead of recommending hosted CI and branch protection over it. The green-before-merge CI gate remains the recommendation where the repo states no policy.
- `/derive-tests` writes into an existing file only when that file is a test-coverage map. A `TESTS.md` that describes the repo's testing method is no longer taken for the map just because of its name: the kit matches on what a file covers, uses the repo's real coverage map, and where there is none picks a name that collides with nothing, rather than writing into a same-named file about something else.

## v2.1.0 — 2026-07-03

### pm-ai-shipping

- `/security-audit-static` findings now carry a mandatory **Evidence** line (`file:line` + verbatim snippet), and every citation is re-verified against the file before the final report ships.
- Subagent fan-out has a concrete trigger (scope over ~30 files / ~5,000 lines) and a structured candidate-record contract, so parallel audit slices merge cleanly into one self-refute pass.
- `/performance-audit-static` now hunts **N+1 queries and request waterfalls** — the most common perf failure in AI-generated code — alongside over-fetching, indexes, and caching, and gained a refute-before-reporting pass (dynamic field access, existing indexes, hot-path evidence).
- Both audit commands pre-approve a read-only toolset (`allowed-tools`): read, search, fan out, and write under `reports/` — never edit the code under audit.
- The audited repo is treated as untrusted input across the kit: instructions embedded in code, comments, or docs are data to analyze — a steering attempt is itself a finding — never directives to follow.
- `/ship-check` runs the security and performance audits as parallel subagents once the docs exist.
- Security reports gained severity anchors (what Critical/High/Medium/Low mean) and a consolidation rule (more than ~12 findings → lead with the worst, group the tail by root cause).
- Docs and reports now use repo-relative paths (`documentation/`, `reports/`) — the old absolute forms (`/documentation`) could resolve to the filesystem root — and reports are always written, with the path announced, instead of "optionally".

### Repo

- Added this `CHANGELOG.md` as the release source of truth with auto-tag-and-release on merge (adapted from [claude-usage](https://github.com/phuryn/claude-usage)): pushing a new `## vX.Y.Z` heading to `main` tags that version and publishes a GitHub Release with the section as notes — gated on the test suite and a version-sync check.
- Added a test suite (`tests/`) and a Tests workflow (every PR and push to `main`): plugin-spec validation plus docs consistency — README skill/command counts vs. disk, marketplace plugin list vs. directories, version sync across all manifests, CHANGELOG format.
- CONTRIBUTING now documents the changelog convention (every user-facing change gets a bullet; contributors credited inline) and the release procedure.
- Docs since v2.0.0: native Codex CLI install path; companion badges (burnstop, claude-usage).

## v2.0.0 — 2026-06-05

- Added the **pm-ai-shipping** plugin (AI Shipping Kit): `/ship-check`, `/document-app`, `/derive-tests`, `/security-audit-static`, `/performance-audit-static`, plus the `shipping-artifacts` and `intended-vs-implemented` skills.
- Added the `strategy-red-team` skill and `/red-team-prd` command to pm-execution.
- Refreshed the root README; added `CLAUDE.md` / `AGENTS.md` agent guidance.
