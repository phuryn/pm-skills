# Contributing

PM Skills Marketplace is maintained by [Paweł Huryn](https://www.productcompass.pm) (pawel@productcompass.pm). Contributions are welcome — whether it's a bug fix, a typo, or a new skill idea.

## How to Contribute

- **Bugs and small fixes** — open a PR directly.
- **New skills, commands, or larger changes** — open an issue first so we can discuss the approach.

## Guidelines

- Keep PRs focused — one change per PR.
- Follow existing patterns: skills are nouns (domain knowledge), commands are verbs (workflows).
- Every skill needs frontmatter with `name` and `description`. Every command needs `description` and `argument-hint`.
- Skill `name` must match its directory name.
- No cross-plugin references in commands. Suggest follow-ups in natural language only.
- Every contributor will be listed publicly (see Changelog & Contributor Credit below).
- Run the checks before submitting: `python3 validate_plugins.py` and `python3 -m unittest discover -s tests`.

## Changelog & Contributor Credit

Every user-facing change gets a bullet in [CHANGELOG.md](CHANGELOG.md). In a PR, add yours under a `## Unreleased` heading at the top (create it if it doesn't exist) and credit yourself at the end of the bullet — `(#123, thanks @your-handle)`. Credits ship verbatim in the GitHub Release notes and stay in the changelog permanently.

## Releases (maintainer)

`CHANGELOG.md` is the source of truth; tags and GitHub Releases are deterministic projections of it (`.github/workflows/tag-on-merge.yml`):

1. Rename `## Unreleased` to `## vX.Y.Z — YYYY-MM-DD`. Semver: breaking changes = major, new skills/commands or changed behavior = minor, fixes and docs = patch.
2. Set the same version in `.claude-plugin/marketplace.json`, `.cursor-plugin/marketplace.json` (`metadata.version`), and every plugin's `.claude-plugin/plugin.json` and `.cursor-plugin/plugin.json` - versions stay in sync across the repo (the test suite enforces this).
3. Push to `main`. CI verifies the version sync, runs the validator and test suite, then tags `vX.Y.Z` and publishes a GitHub Release with the changelog section as notes. No new heading → no release; ordinary pushes are unaffected.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
