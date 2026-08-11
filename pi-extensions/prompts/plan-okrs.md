---
description: Brainstorm team-level OKRs aligned with company objectives — qualitative objectives with measurable key results
argument-hint: "<team, product area, or company objective>"
---

You are executing the /plan-okrs workflow: Team OKR Planning.

Generate well-structured OKRs that connect team work to company strategy. Produces 3 OKR sets with qualitative objectives and quantitative key results.

## Input

${ARGUMENTS:-No input was provided — ask the user for: <team, product area, or company objective>.}

## Workflow

### Step 1: Gather Context

Ask the user:
- What team or product area are these OKRs for?
- What time period? (quarterly is standard, but could be annual or custom)
- What are the company-level objectives these should ladder up to?
- What happened last quarter? (hits, misses, learnings)
- Any constraints or known priorities?

Accept company OKRs or strategy documents as uploads.

### Step 2: Generate OKRs

Apply the **brainstorm-okrs** skill:

- Create 3 OKR sets (Objective + 3-5 Key Results each)
- **Objectives**: Qualitative, inspiring, ambitious but achievable, action-oriented
- **Key Results**: Quantitative, measurable, time-bound, have clear owners
- Ensure OKRs ladder to company objectives with visible connection
- Balance leading indicators (activity) with lagging indicators (outcomes)

### Step 3: Validate Quality

Check each OKR against best practices:
- Is the Objective inspiring? (Would you rally a team around it?)
- Are Key Results measurable? (Can you check completion with data, not judgment?)
- Are targets ambitious but not demoralizing? (70% achievement = well-calibrated)
- Are there 3-5 KRs per Objective? (More = unfocused)
- Do KRs avoid gaming? (e.g., "ship 5 features" incentivizes shipping junk)

Flag any issues and suggest improvements.

### Step 4: Present and Iterate

```
## Team OKRs: [Team Name] — [Period]

**Aligned to**: [Company Objective(s)]

### Objective 1: [Inspiring qualitative statement]
| # | Key Result | Baseline | Target | Owner |
|---|-----------|----------|--------|-------|
| KR1 | [measurable result] | [current] | [target] | [team/person] |
| KR2 | ... | ... | ... | ... |
| KR3 | ... | ... | ... | ... |

### Objective 2: [Inspiring qualitative statement]
[same format]

### Objective 3: [Inspiring qualitative statement]
[same format]

### Alignment Map
Company Objective → Team Objective → Key Results → Expected Impact

### Scoring Guide
- 0.0-0.3: Significant miss — investigate and learn
- 0.4-0.6: Progress made but fell short
- 0.7-0.9: Well-calibrated stretch goal — this is the target zone
- 1.0: Either nailed it or target wasn't ambitious enough

### Check-in Cadence
- **Weekly**: Quick traffic-light update on each KR
- **Mid-quarter**: Deep review, adjust targets if context changed
- **End of quarter**: Score, reflect, feed into next quarter
```

Offer:
- "Want me to **adjust ambition levels** — make them more/less aggressive?"
- "Should I **create a metrics dashboard** for tracking these?"
- "Want me to **draft a stakeholder update** introducing these OKRs?"

## Notes

- OKRs should describe outcomes, not outputs ("Increase activation by 20%" not "Ship onboarding redesign")
- If the user doesn't have company OKRs, help them derive team objectives from product strategy or business goals
- Maximum 3 objectives per team per quarter — more means less focus
- Key Results should be stretch goals — if you're certain you'll hit them, they're not ambitious enough
- Flag any KR that could be gamed and suggest a counter-metric
