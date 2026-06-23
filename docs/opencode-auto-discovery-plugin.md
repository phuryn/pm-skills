# Proposal: a bundled OpenCode plugin so PM Skills just works

OpenCode is the one first-class target with no native PM Skills path. This proposes shipping a small plugin inside the repo (`.opencode/plugins/pm-skills.js`) that auto-registers every skill and `/slash` command at runtime — one-line install, nothing to copy, nothing to keep in sync.

## Today's gap

OpenCode can't read the Claude-style `marketplace.json`, so right now its users get the worst deal of any supported assistant. Skills have to be hand-copied into OpenCode's skill paths with no source of truth — every plugin update means re-copying and risking drift. The 42 guided workflows (`/discover`, `/write-prd`, `/red-team-prd`, …) don't register at all, since nothing turns `commands/*.md` into real OpenCode commands. And there's no incremental story: add a skill upstream, and every OpenCode user has to redo their setup.

## What I'm proposing

A repo-bundled plugin (npm manifest in `.opencode/package.json`, depends on `gray-matter`) that, on init, does the boring work itself:

1. Scans the repo root for `pm-*/` dirs (the 9 plugins).
2. Pushes each `pm-*/skills/` path into `config.skills.paths` — OpenCode then lazily discovers every `SKILL.md`. No symlinks, no config edits. This works because `Config.get()` is a cached singleton, so the mutation is visible when skills get resolved later.
3. Frontmatter-parses every `pm-*/commands/*.md` and registers it as `config.command[name] = { template, ...data }`.
4. Logs init / scan / load / totals under `opencode-pm-skills` so setup is observable instead of silent.

The skill and command files stay the single source of truth — on `git pull`, new ones just show up.

### Install

```jsonc
{
  "plugin": ["pm-skills@git+https://github.com/phuryn/pm-skills.git"]
}
```

Then restart OpenCode.

## What you get

All 68 skills and 42 commands, native; one-line install; stays in sync.

## Verification

- Plugin logs `Found 9 plugin directories`.
- 9 paths land in `config.skills.paths`; 42 commands register in `config.command`.
- `/write-prd` and the `create-prd` skill resolve in a fresh session.
