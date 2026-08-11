---
description: Create a comprehensive Product Requirements Document from a feature idea or problem statement
argument-hint: "<feature or problem statement>"
---

You are executing the /write-prd workflow: Product Requirements Document.

Create a structured PRD that aligns stakeholders and guides development. Accepts anything from a vague idea to a detailed brief.

## Input

${ARGUMENTS:-No feature description was provided — start by asking the user what to write the PRD for.}

## Workflow

### Step 1: Understand the Feature

Accept the input in any form:
- A feature name ("SSO support")
- A problem statement ("Enterprise customers keep asking for centralized auth")
- A user request ("Users want to export their data as CSV")
- A vague idea ("We should do something about onboarding drop-off")
- A file or document the user referenced (read it)

If the input is thin, ask for the missing essentials conversationally — most important questions first.

### Step 2: Gather Context

Ask conversationally — most important questions first, fill gaps as you go:

1. **User problem**: What problem does this solve? Who experiences it? How painful is it?
2. **Target users**: Which user segment(s)? How many? What's their current workaround?
3. **Success metrics**: How will we know this worked? What moves if we nail it?
4. **Constraints**: Technical constraints, timeline, regulatory, dependencies on other teams?
5. **Prior art**: Has this been attempted before? Existing solutions in the market?
6. **Scope preference**: Full solution or phased approach?

If the user provides a document with context, extract what's available and only ask about gaps.

### Step 3: Generate the PRD

Apply the **create-prd** skill (installed in this environment — load its SKILL.md for the full framework) to produce this 8-section document:

```
## Product Requirements Document: [Feature Name]

**Author**: [user]
**Date**: [today]
**Status**: Draft
**Stakeholders**: [if known]

### 1. Executive Summary
[2-3 sentences: what, for whom, why now]

### 2. Background & Context
[Problem space, prior research, market context, what prompted this]

### 3. Objectives & Success Metrics
**Goals** (what success looks like):
1. [Specific, measurable goal]
2. [...]

**Non-Goals** (explicitly out of scope):
1. [What we're not doing, and why]
2. [...]

**Success Metrics**:
| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|

### 4. Target Users & Segments
[Who this serves, user profiles, segment sizing]

### 5. User Stories & Requirements

**P0 — Must Have**:
| # | User Story | Acceptance Criteria |
|---|-----------|-------------------|

**P1 — Should Have**:
| # | User Story | Acceptance Criteria |
|---|-----------|-------------------|

**P2 — Nice to Have / Future**:
| # | User Story | Acceptance Criteria |
|---|-----------|-------------------|

### 6. Solution Overview
[High-level approach, key design decisions, technical approach if known]

### 7. Open Questions
| Question | Owner | Deadline |
|----------|-------|----------|

### 8. Timeline & Phasing
[Milestones, dependencies, phasing if applicable]
```

### Step 4: Review and Iterate

After generating, offer:
- "Want me to **tighten the scope**? I can challenge which P1s should really be P2s."
- "Should I **run a pre-mortem** on this PRD?"
- "Want me to **break this into user stories** for engineering?"
- "Should I **create a stakeholder update** to socialize this?"

Save the PRD as a markdown file to the user's workspace.

## Notes

- Be opinionated about scope — a tight PRD is better than an expansive vague one
- If the idea is too big, proactively suggest phasing and spec only Phase 1
- Non-goals are as important as goals — they prevent scope creep
- Success metrics must be specific: "improve NPS" is bad, "increase NPS from 32 to 45 within 90 days of launch" is good
- Open questions should be genuinely unresolved — don't list things you can answer from context
- If the user provides research, weave insights into the Background section with attribution
