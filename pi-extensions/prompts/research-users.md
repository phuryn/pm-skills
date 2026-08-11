---
description: Comprehensive user research — build personas, segment users, and map the customer journey from research data
argument-hint: "<research data, survey results, or product description>"
---

You are executing the /research-users workflow: User Research Synthesis.

Turn raw research data into actionable user personas, behavioral segments, and customer journey maps. Accepts survey data, interview notes, feedback, analytics, or a product description for exploratory research.

## Input

${ARGUMENTS:-No research input was provided — ask the user what research they have (survey results, interview notes, feedback data) or what product to run exploratory research on.}

## Workflow

### Step 1: Accept Research Inputs

Accept from any combination:
- Survey responses (CSV, spreadsheet, pasted)
- Interview notes or transcripts
- Support tickets or feature requests
- Product analytics / behavioral data
- NPS or satisfaction data
- Product description (for exploratory research without data)
- Files the user references (read them)

Ask:
- What research do you have? What format?
- What do you want to understand? (who are our users, how do they differ, where's the friction)
- What decisions will this inform? (roadmap, positioning, pricing, onboarding)

### Step 2: Build Personas

Apply the **user-personas** skill (installed in this environment — load its SKILL.md for the full framework):

- Identify 3-4 distinct personas from the data
- For each persona: name, role, goals (JTBD), pains, gains, behavioral patterns
- Include unexpected insights — things that surprised you in the data
- Note persona prevalence (what % of your base each represents, if data allows)

### Step 3: Segment Users

Apply the **user-segmentation** and **market-segments** skills:

- Create behavioral segments (not just demographics)
- For each segment: size, JTBD, product fit, willingness to pay, engagement level
- Identify the highest-value segment and the highest-growth segment
- Map segments to personas (how they overlap)

### Step 4: Map the Customer Journey

Apply the **customer-journey-map** skill:

- Map the end-to-end journey: Awareness → Consideration → Onboarding → Active Use → Expansion → Advocacy
- For each stage: touchpoints, emotions, pain points, aha moments
- Identify the biggest drop-off points
- Highlight moments of delight worth amplifying

### Step 5: Generate Research Report

```
## User Research Report: [Product]

**Date**: [today]
**Data sources**: [what was analyzed]
**Sample size**: [if applicable]

### Executive Summary
[3-5 sentences: key findings and implications]

### Personas

#### Persona 1: [Name] — "[Quote that captures them]"
- **Who**: [role, context, experience level]
- **Primary JTBD**: [When..., I want to..., so I can...]
- **Key pains**: [top 3]
- **Key gains**: [what delights them]
- **Behavioral pattern**: [how they use the product]
- **Prevalence**: [X% of user base]

[Repeat for each persona]

### User Segments
| Segment | Size | Primary JTBD | Product Fit | Value | Growth |
|---------|------|-------------|-------------|-------|--------|

### Customer Journey Map
| Stage | Touchpoints | Emotion | Pain Points | Opportunities |
|-------|------------|---------|-------------|---------------|

### Key Insights
1. [Insight with supporting evidence]
2. ...

### Recommendations
1. [Actionable recommendation tied to findings]
2. ...

### Open Questions
[What the data didn't answer — suggested follow-up research]
```

Save as markdown.

### Step 6: Offer Next Steps

- "Want me to **create interview scripts** to go deeper on a specific persona?"
- "Should I **analyze sentiment** across these segments?"
- "Want me to **build a value proposition** for the top persona?"
- "Should I **prioritize the journey map pain points** as feature opportunities?"

## Notes

- If data is thin, be transparent about confidence levels — 5 interviews → hypotheses, not conclusions
- Personas should be useful, not decorative — every persona should influence a product decision
- Behavioral segments are more actionable than demographic segments for product decisions
- The journey map should surface emotions, not just actions — where users feel frustrated vs. delighted drives prioritization
- If no data is provided, generate research-informed hypotheses and recommend how to validate them
