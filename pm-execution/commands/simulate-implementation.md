---
description: Simulate building a PRD, epic, or stories with a panel of developer personas and get a Pre-Handoff Simulation Report with a punch list to fix before handoff
argument-hint: "<PRD, epic, or stories: file, pasted text, or the current doc>"
---

# /simulate-implementation -- Dry-Run the Build Before Handoff

Most handoff friction is a missing decision, not a wrong one: an undefined state, an unnamed error path, an unmapped field, a rollout nobody planned. This command has a panel of developer personas build your spec on paper, keeps only what would stop them or force a silent guess, and hands you a punch list with an owner and a recommended default for each item.

## Invocation

```
/simulate-implementation [paste or upload a PRD, epic, or stories]
/simulate-implementation team-invites-prd.md plus the stories in team-invites-stories.md
/simulate-implementation the current doc
```

## Workflow

### Step 1: Accept the Work

Take a PRD, an epic, a set of stories, or all of them together, as files or pasted text. If the user says "the current doc," use the document in context. If there is only a one-line idea, say the simulation needs a written spec and offer to draft the PRD or stories first.

### Step 2: Simulate the Build

Apply the **implementation-simulation** skill to: $ARGUMENTS

- Split the spec into **build units** and tag each with the seats it touches.
- Run the seats one at a time, skipping any seat that no build unit touches: Backend, Frontend and mobile, Integrations, Data and analytics, Security and privacy, QA and release.
- Log a finding only where a developer would stop to ask, silently guess, meet an unmentioned state or edge case, or call an integration with a missing contract detail. Quote the spec line or name the missing section.
- Run a **separate skeptic pass** that re-reads the spec from scratch and sorts every finding into a dev blocker, a PM scope question, or noise.

### Step 3: Return the Report

Return the Pre-Handoff Simulation Report in the skill's structure:

```
# Pre-Handoff Simulation Report: [spec name]
Date: [date] | Seats run: [list]

## Summary
## Blockers (resolve before handoff)
## Silent assumptions to confirm
## Missing requirements (states and edge cases)
## Integration gaps
## Scope questions for the PM (not dev blockers)
## Dropped as noise
## Punch list (dev blockers only)
| Item | Owner | Recommended default | Severity |
```

Save as markdown.

### Step 4: Offer Next Steps

- "Want me to **update the PRD and stories** with the recommended defaults from the punch list?"
- "Should I **write stories** (`/write-stories`) for the scope questions you decide to keep in this release?"
- "Want me to **generate test scenarios** (`/test-scenarios`) for the edge cases this surfaced?"
- "Should I **run a pre-mortem** (`/pre-mortem`) next, to check launch risk rather than build readiness?"

## Notes

- Distinct from `/pre-mortem` and `/red-team-prd`: red-team asks whether the bet is right, and pre-mortem asks how the launch could fail. This command assumes both and asks whether engineers can build the spec as written without stopping to ask or silently guessing.
- Run it after the PRD, epic, and stories are drafted, and before refinement or sprint planning. Re-run it after the punch list is resolved.
- It prepares engineering review; it does not replace it. Items marked "Verify with engineering, not confirmed" are suspected conflicts with the existing system, not facts.
- An empty report is a valid result. The seats never manufacture findings to fill a section.
