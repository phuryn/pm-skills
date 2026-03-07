# Skill Behavior Tests

Structural validation (`validate_plugins.py`) confirms a skill is *well-formed*.
Behavior tests confirm it *works correctly* — that Claude actually produces the
right output when the skill is active.

This directory contains behavior test suites for the core skills in the
marketplace, powered by [EvalView](https://github.com/hidai25/eval-view).

## How It Works

Each `.yaml` file targets a single skill. EvalView loads the `SKILL.md`,
sends each test's `input` to Claude with the skill context active, and checks
whether the response contains or avoids the expected phrases.

```
tests/
├── pm-toolkit/
│   └── grammar-check.yaml
├── pm-execution/
│   ├── create-prd.yaml
│   ├── user-stories.yaml
│   └── test-scenarios.yaml
├── pm-product-discovery/
│   └── brainstorm-ideas-new.yaml
└── pm-product-strategy/
    └── product-vision.yaml
```

## Running Locally

```bash
# Install EvalView
pip install "evalview>=0.4.0"

# Run a single skill's tests
evalview skill test tests/pm-execution/create-prd.yaml

# Run all tests
for f in tests/**/*.yaml; do evalview skill test "$f"; done
```

You need an `ANTHROPIC_API_KEY` in your environment (or a `.env.local` file).

## CI

The `.github/workflows/skill-behavior-tests.yml` workflow runs automatically
when a skill file or test file changes. Add `ANTHROPIC_API_KEY` to your
repository secrets to enable it.

## Writing Tests for a New Skill

Copy this template into `tests/<plugin-name>/<skill-name>.yaml`:

```yaml
name: <skill-name>-tests
description: Behavior tests for the <skill-name> skill.

skill: ../../<plugin-name>/skills/<skill-name>/SKILL.md
model: claude-sonnet-4-5-20251001
min_pass_rate: 0.8

tests:
  - name: descriptive-test-name
    description: One sentence describing what behavior is being verified.
    input: |
      A realistic prompt a PM would send to this skill.
    expected:
      output_contains:
        - "key phrase the skill should produce"
      output_not_contains:
        - "phrase the skill should never produce"
```

**Test writing tips:**

- Test *behavior*, not wording. Use phrases that any correct response would include, not exact sentences.
- Cover the happy path AND at least one edge case or failure mode per skill.
- `output_not_contains` is as important as `output_contains` — it guards against hallucinations and generic responses.
- Keep `min_pass_rate` at `0.8` to account for LLM non-determinism.
