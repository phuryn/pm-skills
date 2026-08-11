---
description: Break a feature into backlog items — user stories, job stories, or WWA format with acceptance criteria
argument-hint: "[user|job|wwa] <feature description or PRD>"
---

You are executing the /write-stories workflow: Backlog Item Generator.

Break a feature into well-structured backlog items. Choose from three formats based on your team's preference, each with full acceptance criteria.

## Input

${ARGUMENTS:-No mode or feature provided — ask which format they want (user, job, or wwa stories) and about the feature or PRD.}

## Formats

### User Stories
**Format**: "As a [user type], I want [capability], so that [benefit]"
Apply the **user-stories** skill:
- Follow the 3 C's: Card (brief), Conversation (context), Confirmation (acceptance criteria)
- Validate against INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable
- Include design links or mockup references where relevant

### Job Stories
**Format**: "When [situation], I want to [motivation], so I can [outcome]"
Apply the **job-stories** skill:
- Focus on the situation and context, not the user role
- Ground in real user scenarios observed in research
- Ideal for JTBD-oriented teams

### WWA (Why-What-Acceptance)
**Format**: Why [strategic context] → What [deliverable] → Acceptance [criteria]
Apply the **wwas** skill:
- Includes strategic reasoning (why we're building this)
- Produces independent, valuable, testable items
- Good for cross-functional teams that need business context

## Workflow

### Step 1: Accept the Feature

Accept in any form: PRD, feature description, user research finding, or verbal idea. If a PRD is provided, extract the requirements to decompose.

### Step 2: Determine Format

If not specified in the invocation, ask:
- "Which format does your team use? **User stories**, **Job stories**, or **WWA**?"
- If unsure, recommend user stories as the default

### Step 3: Decompose the Feature

- Break the feature into 5-15 independent stories (small enough to complete in one sprint)
- Ensure each story is independently valuable (delivers user value on its own)
- Order by dependency and priority
- Write 3-5 acceptance criteria per story
- Flag stories that need design input or technical spikes

### Step 4: Generate Stories

```
## Backlog: [Feature Name]

**Format**: [User Stories / Job Stories / WWA]
**Total stories**: [count]
**Estimated total effort**: [if possible]

### Stories

#### Story 1: [Short title]
**[The story in chosen format]**

Acceptance Criteria:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

Priority: [P0/P1/P2] | Effort: [S/M/L] | Dependencies: [none or list]

---
[Repeat for each story]

### Story Map
[Visual ordering: must-have → should-have → nice-to-have]

### Technical Notes
[Cross-cutting concerns: API changes, data migration, infrastructure]

### Open Questions
[Things that need answers before implementation can start]
```

Save as markdown.

### Step 5: Offer Next Steps

- "Want me to **generate test scenarios** for these stories?"
- "Should I **create dummy data** for development and testing?"
- "Want me to **estimate sprint capacity** for these stories?"
- "Should I **convert to a different format** (user stories ↔ job stories ↔ WWA)?"

## Notes

- One story = one deployable unit of value — if it needs another story to be useful, they should be combined
- Acceptance criteria should be testable by QA without additional interpretation
- Error handling and edge cases deserve their own stories, not bullet points within a happy-path story
- If the feature is large (15+ stories), suggest grouping into epics or phases
- Flag any story that requires a spike (technical investigation before estimation is possible)
