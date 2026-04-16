---
name: voiceflow-ui-system
description: "Build VoiceFlow UI and theme work from the spec without visual drift. Use when implementing the design system, page layouts, responsive behavior, animations, accessibility, or dark/light/system theming."
---

# VoiceFlow UI System

## Purpose

You are responsible for implementing VoiceFlow's interface exactly enough that the product feels intentional, dense, and consistent. The UI is not generic SaaS chrome. It is a precision productivity tool with a dark-first identity, a fully functional light theme, and strong developer ergonomics.

## Use When

Use this skill when the task involves:
- theme tokens and CSS variables
- Tailwind theme mapping
- public pages, app shell, settings shell, onboarding shell
- responsive layouts
- component states and animations
- accessibility, focus handling, and interaction polish

## Core Principles

- No hardcoded colors when a theme token exists.
- Dark, light, and system themes must all work.
- Preserve the declared typography: Syne, Manrope, JetBrains Mono.
- Reuse primitives only when behavior is truly shared.
- Avoid decorative excess that weakens readability or performance.

## Mandatory UI Constraints

1. Theme system
   - Implement `data-theme="dark" | "light"` at the root.
   - Store theme selection in localStorage with system fallback.
   - All key colors and shadows must come from CSS variables.

2. Layout rules
   - Public routes use `PublicShell` patterns.
   - Authenticated routes use `AppShell` patterns.
   - Mobile collapses the sidebar into a bottom tab bar.
   - Settings become accordion-first on mobile.

3. Component behavior
   - All interactive controls need visible `focus-visible` states.
   - All icon-only buttons need `aria-label`.
   - Modals need proper dialog semantics and Escape handling.
   - Decorative waveform visuals must be `aria-hidden`.

4. Motion rules
   - Animations should reinforce state: recording, loading, hover, entry.
   - Respect reduced motion preferences.
   - Do not add generic motion for its own sake.

## Workflow

1. Identify the exact UI surface.
   - page, shell, modal, card, selector, badge, toast, or theme primitive

2. Map required tokens and states.
   - background, border, text, accent, shadow, hover, focus, disabled, active

3. Build mobile and desktop behavior together.
   - do not treat mobile as a post-pass

4. Verify all states.
   - default
   - hover
   - focus
   - active
   - disabled
   - loading
   - error
   - empty

5. Check accessibility before calling it done.

## Output Expectations

When implementing or reviewing UI work, explicitly cover:

### Surfaces
- which route or component is being changed

### States
- what the user sees in idle, hover, active, loading, empty, error, and success conditions

### Responsive Behavior
- what changes on mobile, tablet, desktop, and wide layouts

### Theme Compliance
- how dark/light/system are preserved

### Accessibility
- labels, focus order, contrast, keyboard behavior, live regions

## VoiceFlow-Specific Watchouts

- Do not replace the specified electric teal + violet identity with generic defaults.
- Do not flatten the information density into oversized marketing spacing on app pages.
- Do not build one-off page styling that bypasses the shared token system.
- Dashboard, history, snippets, dictionary, and settings should feel like one product, not five disconnected pages.
- Landing and pricing can be more expressive, but the app routes must stay operational first.

## Done Criteria

This skill is complete only when the UI implementation is token-driven, responsive, accessible, and recognizably aligned with the VoiceFlow spec.
