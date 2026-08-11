---
description: Sprint lifecycle — plan a sprint, run a retrospective, or generate release notes
argument-hint: "[plan|retro|release-notes] <context>"
---

You are executing the /sprint workflow: Sprint Lifecycle.

Three modes covering the sprint lifecycle: **plan** for sprint planning, **retro** for retrospectives, **release-notes** for shipping communication.

## Input

${ARGUMENTS:-No mode or context provided — ask the user what they want (plan, retro, or release-notes) and what sprint or release this covers.}

## Modes

---

### Plan Mode

Prepare for sprint planning with capacity estimation, story selection, and risk identification.

#### Workflow

**Step 1: Gather Sprint Context**
- Sprint duration (1 or 2 weeks)
- Team composition (engineers, designers, QA — and availability)
- Sprint goal or focus area
- Backlog items to consider (paste, upload, or describe)
- Any carry-over from last sprint
- Known interruptions (holidays, on-call, meetings)

**Step 2: Estimate Capacity**

Apply the **sprint-plan** skill:

- Calculate available engineering hours/points after meetings, on-call, PTO
- Apply a velocity adjustment based on historical data (if provided) or industry standard (70% of theoretical capacity)
- Show capacity breakdown per team member

**Step 3: Select and Sequence Stories**

- Recommend which stories fit within capacity
- Flag dependency chains (A must complete before B starts)
- Identify risks: stories that are underspecified, have external dependencies, or need design input
- Balance quick wins with larger items
- Ensure every story has acceptance criteria

**Step 4: Generate Sprint Plan**

```
## Sprint Plan: [Sprint Name/Number]

**Duration**: [dates]
**Sprint Goal**: [one sentence]
**Team**: [members and availability]

### Capacity
| Member | Available Days | Points/Hours | Notes |
|--------|--------------|-------------|-------|

**Total capacity**: [X] points/hours
**Recommended commitment**: [Y] points/hours (with buffer)

### Selected Stories
| # | Story | Points | Owner | Dependencies | Risk |
|---|-------|--------|-------|-------------|------|

### Sprint Risks
1. [Risk] — Mitigation: [action]

### Definition of Done
- [ ] Code reviewed
- [ ] Tests passing
- [ ] Deployed to staging
- [ ] QA approved
- [ ] Documentation updated (if applicable)
```

---

### Retro Mode

Facilitate a structured retrospective that produces actionable improvements.

#### Workflow

**Step 1: Gather Sprint Feedback**

Accept input as:
- Team feedback (pasted from a survey, Slack, or collaborative doc)
- Sprint metrics (velocity, bugs, incidents)
- The user's own observations

Ask: "Which retro format do you prefer?"
- **Start/Stop/Continue** (simple, fast)
- **4Ls** (Liked, Learned, Lacked, Longed for)
- **Sailboat** (Wind = helps, Anchor = slows, Rocks = risks, Island = goals)

**Step 2: Analyze and Structure**

Apply the **retro** skill:

- Categorize feedback into the chosen framework
- Identify themes and patterns
- Separate symptoms from root causes
- Highlight wins worth celebrating

**Step 3: Generate Retro Summary**

```
## Sprint Retrospective: [Sprint Name]

**Date**: [today]
**Format**: [Start/Stop/Continue | 4Ls | Sailboat]
**Participants**: [if known]

### What Went Well
[Grouped themes with supporting evidence]

### What Didn't Go Well
[Grouped themes with root cause analysis]

### Key Insights
[2-3 patterns that emerged]

### Action Items
| # | Action | Owner | Deadline | Priority |
|---|--------|-------|----------|----------|

### Metrics This Sprint
| Metric | This Sprint | Last Sprint | Trend |
|--------|-----------|------------|-------|
```

---

### Release Notes Mode

Generate user-facing release notes from technical artifacts.

#### Workflow

**Step 1: Accept Release Content**

Accept:
- Jira/Linear tickets or changelog
- PRD or feature specs
- Git commit messages or PR descriptions
- Team's internal summary of what shipped

**Step 2: Transform**

Apply the **release-notes** skill:

- Translate technical language into user benefits
- Categorize as: New Features, Improvements, Bug Fixes
- Write in the product's voice (ask about tone if not clear)
- Highlight the most impactful change first

**Step 3: Generate Release Notes**

```
## What's New — [Version/Date]

### Highlights
[1-2 sentence summary of the most important change]

### New Features
- **[Feature Name]** — [user-facing benefit in plain language]

### Improvements
- **[Improvement]** — [what's better now]

### Bug Fixes
- Fixed [issue] that caused [user impact]

### Coming Soon
[Optional teaser for next release]
```

Save as markdown and offer to format for different channels (blog post, in-app, email, Slack announcement).

## Notes

- For plan mode: protect 20% buffer for unplanned work — teams that plan at 100% capacity always miss
- For retro mode: focus on 2-3 high-impact action items, not 10 things nobody will do
- For release notes: always frame changes as user benefits, not technical implementations
- Each mode can chain to the others: plan → (sprint happens) → retro → release-notes
