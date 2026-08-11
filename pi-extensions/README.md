# pm-skills-pi — pi slash commands

Pi package that ports the **pm-skills** Claude Code commands to [pi](https://pi.dev).
All **42 commands** plus all **68 skills** are ported — same names, same
descriptions, same workflows — as a **fully declarative package**: no code at
all, just manifest entries pointing at Markdown files.

- **Commands are prompt templates** — plain Markdown files in `prompts/`, the pi
  equivalent of the Claude `pm-*/commands/*.md` files. pi expands them via
  `/command args` with `$ARGUMENTS` interpolation, exactly like Claude.
- **Skills stay SKILL.md files** — the workflows reference the pm skills by name
  (e.g. *apply the **create-prd** skill*), and the manifest points pi at the
  repo's skill directories.

## Install

The repo root and `pi-extensions/` are both pi packages (same name, `pm-skills-pi`),
so you can install either entry point:

```bash
# The whole repo as a pi package (git-style install — clone root has the manifest)
pi install git:phuryn/pm-skills

# Or just the pi-extensions directory (local path)
pi install ./pi-extensions
```

Then type `/` in pi — the pm commands appear in the command list. No config needed.

## Commands (42, grouped by plugin)

**pm-product-discovery**
`/brainstorm` — multi-perspective ideation (ideas|experiments, existing|new) ·
`/discover` — full discovery cycle: ideation → assumptions → experiments ·
`/interview` — customer interview script prep or transcript summary ·
`/setup-metrics` — product metrics dashboard design ·
`/triage-requests` — feature request analysis, categorization, prioritization

**pm-product-strategy**
`/business-model` — Lean / Business Model / Startup Canvas / value prop ·
`/market-scan` — SWOT + PESTLE + Porter's Five Forces + Ansoff in one scan ·
`/pricing` — pricing models, willingness-to-pay, pricing experiments ·
`/strategy` — 9-section Product Strategy Canvas ·
`/value-proposition` — 6-part JTBD value proposition

**pm-execution**
`/write-prd` — structured PRD from a feature idea or problem statement ·
`/pre-mortem` — Tigers / Paper Tigers / Elephants risk analysis ·
`/plan-okrs` — team OKRs aligned with company objectives ·
`/red-team-prd` — attack load-bearing assumptions ·
`/sprint` — sprint lifecycle (plan | retro | release-notes) ·
`/stakeholder-map` — Power × Interest grid + communication plan ·
`/write-stories` — backlog items (user | job | wwa) ·
`/test-scenarios` — happy paths, edge cases, error handling ·
`/transform-roadmap` — feature-based → outcome-focused roadmap ·
`/meeting-notes` — structured meeting summary with decisions + actions ·
`/generate-data` — realistic dummy datasets (CSV, JSON, SQL, Python)

**pm-market-research**
`/research-users` — personas, segments, customer journey ·
`/analyze-feedback` — sentiment + theme extraction at scale ·
`/competitive-analysis` — landscape, differentiation opportunities

**pm-data-analytics**
`/write-query` — SQL generation from natural language ·
`/analyze-cohorts` — retention curves, feature adoption ·
`/analyze-test` — A/B test significance + ship/extend/stop

**pm-go-to-market**
`/plan-launch` — beachhead, ICP, messaging, channels, timeline ·
`/battlecard` — sales-ready competitive battlecard ·
`/growth-strategy` — growth loops + GTM motions

**pm-marketing-growth**
`/north-star` — North Star Metric + input metrics ·
`/market-product` — marketing ideas, positioning, naming

**pm-toolkit**
`/review-resume` — PM resume review vs 10 best practices ·
`/tailor-resume` — tailor resume to a job description ·
`/draft-nda` — Non-Disclosure Agreement ·
`/privacy-policy` — data collection / usage / storage / compliance ·
`/proofread` — grammar, logic, flow check

**pm-ai-shipping**
`/ship-check` — reviewer-ready shipping packet ·
`/document-app` — reverse-engineer the system docs ·
`/derive-tests` — test-coverage map from documented intent ·
`/security-audit-static` — evidence-backed static security audit ·
`/performance-audit-static` — N+1s, over-fetching, indexes, caching

Run a command with an argument: `/write-prd SSO support for enterprise customers`.
Without an argument, the template's `${ARGUMENTS:-...}` default tells the agent to
ask for the essentials — same conversational behavior as the Claude commands.
Mode-based commands parse their mode from the argument (`/sprint retro`, `/business-model lean`).

## How it works

The package is **fully declarative** — the `pi` manifest in `package.json` is the
whole implementation:

```json
{
  "pi": {
    "prompts": ["./pi-extensions/prompts"],
    "skills": ["./pm-*/skills"]
  }
}
```

(From `pi-extensions/package.json`, the local-path entry point: `"prompts": ["./prompts"]`, `"skills": ["../pm-*/skills"]`.)

- `prompts` → every `.md` file becomes a `/command` prompt template (filename =
  command name, frontmatter = description + argument-hint, `$ARGUMENTS` = args).
- `skills` → the glob expands to all nine plugins' `skills/` directories, so the
  68 SKILL.md files load as first-class skills.

No TypeScript, no event handlers, nothing to fail at load time.

### Skills and global installs

If the same skills are also installed globally (`~/.pi/agent/skills`), the global
copies win — pi loads user skills first and keeps the first registration of a
name. The package's copies are silently skipped (a stored, non-displayed
diagnostic), so there's no startup noise and no version shadowing. On a machine
without the skills installed, the package is fully self-contained.

## Development

```bash
cd pi-extensions
npm install          # dev deps: typescript, @types/node, pi types
npm run typecheck    # tsc --noEmit (test files only — the package itself is declarative)
npm test             # parity + manifest tests (node --test)
```

The tests pin every prompt template to its Claude source of truth
(`pm-*/commands/*.md`): the command name, `description`, and `argument-hint`
must match the frontmatter of the corresponding markdown file; the body must use
`$ARGUMENTS` and only reference skills that exist in the repo; bodies must not
contain `$<digit>` sequences (pi's template engine would substitute them). The
tests also verify both package manifests: declared prompt and skill globs must
resolve to exactly 42 commands and 68 skills, and the extension entry must be
absent (the package is declarative by design).

To port new commands after adding them to the Claude repo, regenerate:

```bash
node scripts/port-commands.mjs   # creates prompts/<name>.md for any command without one
```

## Roadmap

- Add the pi-extensions directory to the repo's validation/CI checks (version
  sync for the package.json manifests, `npm test` in the workflow).
