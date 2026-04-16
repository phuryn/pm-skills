# pm-voiceflow

VoiceFlow-specific build skills for turning the product spec into a working React + Tailwind + Supabase application.

## Skills (5)

- **voiceflow-architecture** — Turn the spec into an implementation slice with routes, state, data dependencies, acceptance criteria, and build order.
- **voiceflow-ui-system** — Build the design system, theme tokens, layouts, responsive behavior, and page UI without drifting from the spec.
- **voiceflow-dictation-engine** — Implement the recording loop, Whisper/Claude pipeline, output actions, shortcuts, and recording state machine.
- **voiceflow-data-workflows** — Implement Supabase auth, onboarding persistence, history, snippets, dictionary, and settings storage.
- **voiceflow-dev-modes** — Implement Variable Recognition, File Tagging, AI Agent Import, and the related guardrails.

## Recommended Usage Order

1. Use `voiceflow-architecture` to define the exact slice you are building.
2. Use `voiceflow-ui-system` for theme, layout, and component work.
3. Use `voiceflow-data-workflows` for auth, schema, and persistent flows.
4. Use `voiceflow-dictation-engine` for the recording and cleanup pipeline.
5. Use `voiceflow-dev-modes` for the advanced developer features.

## Scope

These skills assume the VoiceFlow product spec is the source of truth. They are opinionated about:

- React + Vite + TypeScript + Tailwind CSS v3
- Zustand for client state
- Supabase for auth and persistence
- OpenAI Whisper for transcription
- Anthropic Claude for cleanup and agent-style output
- Strict adherence to the defined route structure, theme system, and coding standards

## Commands

None yet. This pack is intentionally skills-first so you can call the right workflow directly instead of hiding implementation choices behind broad slash commands.

## Notes

- These skills are implementation-focused, not generic PM workflows.
- If a requested change conflicts with the spec, the skills should call that out and choose the narrower path.
- For multi-user launch work, move AI calls behind server-side functions and do not expose keys client-side.

## Author

Amit Jangra — [GitHub](https://github.com/AmitJangra25)

## License

MIT
