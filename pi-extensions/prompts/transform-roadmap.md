---
description: Convert a feature-based roadmap into an outcome-focused roadmap that communicates strategic intent
argument-hint: "<roadmap as text, file, or list of planned features>"
---

You are executing the /transform-roadmap workflow: Outcome-Focused Roadmap.

Take a list of planned features or an output-focused roadmap and rewrite it as an outcome-focused roadmap that communicates *why* instead of *what*.

## Input

${ARGUMENTS:-No input was provided — ask the user for: <roadmap as text, file, or list of planned features>.}

## Workflow

### Step 1: Accept the Current Roadmap

Accept in any format:
- Feature list or backlog items
- Roadmap document (Now/Next/Later, quarterly, timeline)
- Spreadsheet or Gantt chart export
- Screenshot of a roadmap tool

Parse each item to extract: feature name, description, target date/timeframe, and any context.

### Step 2: Understand Strategic Context

Ask:
- What are the product goals or OKRs for this period?
- Who is the audience for this roadmap? (execs, engineering, customers, board)
- What format do you prefer? (Now/Next/Later, quarterly, timeline)

### Step 3: Transform Each Item

Apply the **outcome-roadmap** skill:

For each feature/output on the roadmap:
1. Identify the **user or business outcome** it's trying to achieve
2. Rewrite as an outcome statement: "[Verb] [metric/experience] for [user segment]"
3. Group features that serve the same outcome under one initiative
4. Add success metrics to each outcome

**Before → After examples:**
- "Build SSO integration" → "Reduce enterprise onboarding friction — target: 50% faster time-to-first-value for enterprise accounts"
- "Redesign dashboard" → "Help power users find insights faster — target: 30% reduction in time-to-insight"
- "Add CSV export" → "Enable teams to share data outside the product — target: 25% increase in report sharing"

### Step 4: Generate Transformed Roadmap

```
## Outcome-Focused Roadmap: [Product] — [Period]

**Strategic themes**: [2-3 high-level themes]

### Now (Current Quarter)
**Theme: [Strategic Theme]**
| Outcome | Success Metric | Key Initiatives | Status |
|---------|---------------|----------------|--------|

### Next (Next Quarter)
**Theme: [Strategic Theme]**
| Outcome | Success Metric | Key Initiatives | Confidence |
|---------|---------------|----------------|------------|

### Later (Future)
**Theme: [Strategic Theme]**
| Outcome | Success Metric | Key Initiatives | Dependencies |
|---------|---------------|----------------|-------------|

### Transformation Notes
| Original Feature | Transformed Outcome | Why This Framing |
|-----------------|--------------------|-----------------|

### What Changed
[Summary of how the roadmap narrative shifted]
```

Save as a markdown file.

### Step 5: Review

Offer:
- "Want me to **add OKR alignment** for each outcome?"
- "Should I **draft a stakeholder presentation** of this roadmap?"
- "Want me to **identify risks** for the Now items?"

## Notes

- Outcomes should be measurable and have a clear "done" state
- Multiple features can map to one outcome — this is a feature, not a bug
- If an output doesn't clearly serve an outcome, flag it for the user to justify or deprioritize
- The audience matters: exec roadmaps should be outcome-only, engineering roadmaps can include deliverables under each outcome
- "Later" items should be less specific — outcomes without committed solutions
