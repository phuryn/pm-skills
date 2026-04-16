---
name: voiceflow-dictation-engine
description: "Implement the VoiceFlow recording loop, transcription pipeline, cleanup flow, output actions, and keyboard controls. Use when building or debugging the core dictation experience."
---

# VoiceFlow Dictation Engine

## Purpose

You own the core product loop: speak -> capture -> transcribe -> clean -> output -> save or reuse. If this flow is unstable, the product fails regardless of UI quality.

## Use When

Use this skill when the task involves:
- microphone permissions
- MediaRecorder or Web Speech API integration
- recording state machine
- silence detection
- Whisper transcription calls
- Claude cleanup calls
- output panel actions
- dictation keyboard shortcuts
- floating mic widget behavior

## Non-Negotiable Behavior

The engine must honor this state machine:
- `idle`
- `listening`
- `recording`
- `processing`
- `output_ready`
- `error`

Transitions must be explicit. Avoid hidden state jumps.

## Processing Order

1. Start capture.
2. Show live recording state.
3. Stop on second Space press, explicit stop, or configured silence threshold.
4. Send audio to Whisper for final transcript.
5. Run snippet detection before advanced formatting where required.
6. Send transcript to Claude for cleanup when AI cleanup is enabled.
7. Render clean output.
8. Support copy, save, edit, and re-process.

## Workflow

1. Confirm the user flow being built.
   - dashboard panel, floating widget, onboarding mic step, or shortcuts

2. Define the recording state transitions.
   - start trigger
   - cancel trigger
   - stop trigger
   - timeout/silence behavior
   - processing and error fallback

3. Separate responsibilities clearly.
   - hook for recording and audio capture
   - hook/lib for Whisper
   - hook/lib for Claude cleanup
   - store for current recording/output state
   - UI components for waveform, mic button, transcript output

4. Handle failures explicitly.
   - denied mic permission
   - unsupported browser APIs
   - empty transcript
   - Whisper timeout
   - Claude timeout
   - save failure after successful output

5. Validate output actions.
   - copy feedback
   - save-to-history behavior
   - inline editing
   - re-process with different tone/context

## VoiceFlow-Specific Rules

- Default hotkey is Space to start and stop, Esc to cancel.
- Do not trigger global shortcuts while an input or textarea is focused.
- Max recording length is bounded. Silence auto-stop is configurable.
- The output panel must show word count and estimated typing time saved.
- Snippet detection takes precedence over Variable Recognition when both match.
- If AI cleanup is off, the raw transcript path still needs a clean user experience.

## Output Format

When implementing or reviewing work with this skill, cover:

### Flow
- exact start -> stop -> process -> output lifecycle

### Ownership
- hooks, stores, lib modules, and components involved

### Failure Handling
- what the user sees and what gets retried

### Verification
- keyboard behavior
- timer updates
- clipboard/save/edit/re-process actions
- browser compatibility assumptions

## Watchouts

- Do not couple waveform rendering to the data persistence layer.
- Do not let UI components own transcription business logic.
- Do not send API keys from the client in a multi-user-ready implementation.
- Do not claim real-time transcript accuracy that the chosen browser APIs cannot deliver.

## Done Criteria

This skill is complete only when the dictation loop is deterministic, debuggable, and usable without relying on optimistic assumptions.
