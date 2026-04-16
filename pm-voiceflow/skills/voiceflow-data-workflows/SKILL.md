---
name: voiceflow-data-workflows
description: "Implement VoiceFlow persistence and authenticated workflows with Supabase. Use when building auth, onboarding, history, snippets, dictionary, settings, or the underlying schema and RLS policies."
---

# VoiceFlow Data Workflows

## Purpose

You are responsible for every persistent workflow in VoiceFlow. Your job is to make auth, onboarding, settings, and saved artifacts behave like one coherent system instead of a collection of disconnected CRUD screens.

## Use When

Use this skill when the task involves:
- Supabase auth
- PostgreSQL schema and RLS
- onboarding persistence
- history storage and search
- snippets CRUD and usage counts
- personal dictionary CRUD and suggestions
- user preferences and settings persistence
- account management and export/delete flows

## Data Model Baseline

Respect the spec tables unless the user explicitly changes them:
- `transcriptions`
- `snippets`
- `dictionary_words`
- `user_preferences`
- `ai_agents`

Each user-owned table must enforce isolation with RLS.

## Workflow

1. Identify the exact user workflow.
   - sign up, sign in, onboarding, save history, import words, edit snippet, save settings, delete account

2. Trace the full path.
   - UI trigger
   - validation
   - Supabase call
   - optimistic update or refetch
   - toast/inline feedback
   - empty/loading/error states

3. Enforce ownership and defaults.
   - user-specific queries only
   - default preferences created once
   - onboarding guards respect completed steps

4. Keep storage rules explicit.
   - what lives in auth metadata
   - what lives in `user_preferences`
   - what belongs in app state only

5. Verify destructive actions carefully.
   - deleting snippets
   - clearing history
   - removing dictionary words
   - account deletion

## Implementation Rules

- Hooks manage Supabase reads and writes.
- Hooks should expose `isLoading`, `error`, and mutation functions.
- Forms validate on blur and on submit.
- Per-field validation errors are shown inline, not as toasts.
- Save indicators should reflect actual persistence, not assumed success.
- Search, filters, and exports should operate on a clear source of truth.

## VoiceFlow-Specific Requirements

- Onboarding cannot be treated as optional if later flows depend on preferences.
- Snippets support `[variable]` placeholders and must handle fill-in prompts.
- History cards need copy, edit, delete, and re-dictate flows.
- Dictionary words should support bulk import and auto-learn suggestions.
- Settings changes are mostly auto-save, but account mutations remain explicit save flows.
- For personal-use mode, temporary client-side AI calls are tolerated. For multi-user readiness, proxy them server-side.

## Output Format

When using this skill, provide:

### Workflow Definition
- the exact user action and persistence boundary

### Schema / RLS Impact
- tables, columns, defaults, and policies affected

### Hook + UI Contract
- fetch behavior, mutation behavior, validation behavior, feedback behavior

### Verification
- success path
- empty path
- error path
- unauthorized path

## Watchouts

- Do not mix onboarding completion with mere authentication.
- Do not leave usage counters or timestamps undefined when the UI depends on them.
- Do not perform account-destructive operations without deliberate confirmation.
- Do not let local state drift from persisted settings without a clear sync strategy.

## Done Criteria

This skill is complete only when the requested workflow is persisted correctly, guarded by ownership rules, and recoverable when failures happen.
