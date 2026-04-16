---
name: voiceflow-dev-modes
description: "Implement VoiceFlow's advanced developer features: Variable Recognition, File Tagging in Chat, AI Prompt context, and AI Agent Import. Use when building or reviewing the product's code-aware and agent-aware functionality."
---

# VoiceFlow Dev Modes

## Purpose

You own the advanced features that make VoiceFlow useful for developers and AI-heavy workflows. These features are higher risk than the base dictation loop because they blend transcription, transformation, context inference, and compliance constraints.

## Use When

Use this skill when the task involves:
- Variable Recognition
- File Tagging in Chat
- AI Prompt context
- Vibe Coding settings
- AI Agent Import
- agent extraction, reconstruction, and storage
- conflict handling between snippets and code-aware formatting

## Mandatory Guardrails

- Do not claim exact replication of third-party GPTs, Gems, or Claude Projects.
- Only use publicly visible metadata when reconstructing agents.
- Show the approximation disclaimer in the agent review flow.
- Snippet detection and Variable Recognition cannot both win silently; respect the configured conflict rule.
- File Tagging must be suppressed in non-dev contexts as defined in the spec.

## Feature Rules

### Variable Recognition
- Wrap likely identifiers in backticks.
- Use dictionary words, custom hints, context, and transcript content.
- Support camelCase, PascalCase, snake_case, and SCREAMING_SNAKE_CASE.
- Avoid wrapping ordinary prose that merely sounds technical.

### File Tagging
- Convert spoken filenames to `@filename` references in supported dev contexts.
- Highest confidence path is filename with extension.
- Support trigger words such as `at`, `tag`, and `open`.
- Suppress in Email, Slack, and General Note unless the spec explicitly changes that rule.

### AI Prompt Context
- Treat it as a first-class context, not a hack on top of Code Comment.
- Enable aggressive filler removal, technical tone, variable recognition, and file tagging.

### AI Agent Import
- Validate source URL and platform.
- Fetch public page content server-side.
- Use Claude to infer a local system prompt and metadata.
- Persist reconstructed agents to `ai_agents` with confidence and source platform.
- Offer manual fallback when extraction confidence is low.

## Workflow

1. Identify which advanced feature is being built.
2. Map the exact settings, prompt additions, and UI indicators involved.
3. Separate deterministic logic from AI inference.
   - deterministic: extension matching, context suppression, trigger words, conflict routing
   - AI inference: identifier reconstruction, agent prompt approximation
4. Make failure and confidence visible.
   - low confidence extraction
   - unsupported URL
   - ambiguous code identifier
   - conflicting snippet match
5. Verify the output formatting in the final user-visible text.

## Output Format

When using this skill, always cover:

### Feature Contract
- what the feature should do and when it must not run

### Prompt / Logic Changes
- deterministic rules
- prompt additions
- precedence rules

### UI + Settings Impact
- badges, toggles, tabs, modals, review states, warnings

### Compliance / Risk
- approximation disclaimer
- public-data-only constraint
- privacy and ToS boundaries

## Watchouts

- Do not hide low-confidence extraction behind confident UI copy.
- Do not enable file tagging in terminal-like or non-dev contexts by default.
- Do not let advanced formatting mutate saved transcripts without preserving the original raw text.
- Do not mix third-party agent branding with claims of true compatibility.

## Done Criteria

This skill is complete only when advanced features are useful, explicit about uncertainty, and constrained enough that they do not corrupt the base dictation experience.
