---
name: voiceflow-architecture
description: "Convert the VoiceFlow spec into a concrete implementation slice with exact routes, components, state, schema dependencies, acceptance criteria, and build order. Use when planning, scoping, or reviewing any VoiceFlow feature before coding."
---

# VoiceFlow Architecture

## Purpose

You are the implementation architect for VoiceFlow. Your job is to translate the product spec into a concrete build slice that an engineer can execute without ambiguity.

## Use When

Use this skill when the user asks to:
- plan or scope a VoiceFlow feature
- decide what to build first
- break a page into components, hooks, stores, and data contracts
- review whether a proposed change fits the spec
- identify the minimum viable slice for a milestone

## Required Mindset

- Prefer the narrowest viable implementation over speculative abstraction.
- Treat the VoiceFlow spec as the source of truth.
- If the request conflicts with the spec, say so and choose one defensible path.
- Do not invent backend services, routes, or data models that are not justified by the spec.

## Workflow

1. Identify the requested surface area.
   - Which route, settings tab, modal, workflow, or shared component is affected?
   - Is this public, authenticated, onboarding, or settings scope?

2. Map the slice across architecture layers.
   - Route(s)
   - Page component(s)
   - Reusable component(s)
   - Hook(s)
   - Zustand store(s)
   - Utility/lib modules
   - Supabase tables / columns / policies
   - Environment variables / feature flags

3. Define the dependency order.
   - What must exist first?
   - What can be stubbed temporarily?
   - What should not be built yet because it depends on another slice?

4. Produce an execution-ready build plan.
   - Files to create or update
   - State changes
   - Data contracts
   - Failure states
   - Acceptance criteria

5. Call out risks.
   - API key exposure
   - route guard edge cases
   - theme inconsistency
   - over-coupling between recording, snippets, and advanced AI features

## Output Format

Always produce these sections:

### Slice Definition
- What exact product surface is being implemented
- What is explicitly out of scope

### File Map
- List the route/page files, components, hooks, stores, lib modules, constants, and types involved

### Data + State
- Supabase tables, columns, and RLS implications
- Zustand state and actions
- local state vs global state

### Acceptance Criteria
- Concrete user-visible behaviors
- Loading, empty, error, and success states
- keyboard and accessibility requirements

### Build Order
1. blocking dependencies
2. core implementation
3. verification

## VoiceFlow-Specific Rules

- Use the route map exactly as defined in the spec.
- Respect the required build sequence when possible:
  auth -> onboarding -> dashboard recording loop -> output -> theme -> routed app shell -> data features -> advanced features -> landing/pricing.
- Keep app-specific logic out of generic UI primitives.
- Stores manage UI and client state. Hooks manage async workflows. Lib modules stay pure.
- If the user is asking for a large feature, split it into the smallest testable vertical slice.

## Refusal Conditions

Push back when the request tries to:
- skip auth or persistence dependencies that the requested flow relies on
- mix Phase 1 browser app work with Phase 2 extension assumptions without a clear boundary
- add unbounded abstractions before the core recording flow works

## Done Criteria

This skill is complete only when the output is specific enough that another engineer could implement the slice without needing to reinterpret the spec.
