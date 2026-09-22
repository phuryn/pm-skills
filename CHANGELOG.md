# Changelog

## Unreleased

### pm-toolkit

- Added the **skill-navigation** skill and `/ask-pm` command to help users choose an available PM capability from their situation, with support for partial installations and skills-only hosts (#63, thanks @qshanx).

### pm-ai-shipping

- Added the **code-review** skill: correctness is the core engine, with performance and security as optional sub-cases of it rather than separate methods. It anchors on agreements between participants across a boundary — the defects that stay invisible file-by-file because each side reads as reasonable alone — forces a violating execution, and refutes every candidate before reporting.
- Added a correctness taxonomy reference built from real fix history, plus performance and security reference sheets the same engine reads.
- `/ship-check` gained a correctness review as Step 3, before the security and performance audits, and an independent unsteered pass by a second model as Step 6.
- `/security-audit-static` gained an OWASP Top 10 coverage backstop: every surviving finding is mapped to a category, and any category with zero findings is flagged "not covered — double-check" rather than silently passing. It is a coverage check, not a mandate to invent findings.

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
