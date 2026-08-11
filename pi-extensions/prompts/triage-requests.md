---
description: Analyze, categorize, and prioritize a batch of feature requests from customers or stakeholders
argument-hint: "<feature requests as text, file, or paste>"
---

You are executing the /triage-requests workflow: Feature Request Triage.

Take a pile of feature requests — from support tickets, sales calls, surveys, or Slack — and turn them into a prioritized, actionable backlog.

## Input

${ARGUMENTS:-No input was provided — ask the user for: <feature requests as text, file, or paste>.}

## Workflow

### Step 1: Accept Feature Requests

Accept requests in any format:
- **Pasted text**: List of requests, one per line or paragraph
- **Uploaded file**: CSV, Excel, or text file with request data
- **Structured data**: If the input has columns (requester, request, date, etc.), preserve them

If no input is provided, ask the user to paste or upload their feature requests.

Parse each request to extract:
- The core ask (what the user wants)
- Context (who asked, when, why — if available)
- Frequency signals (how many people asked for similar things)

### Step 2: Gather Prioritization Context

Ask the user (conversationally, not all at once):
- What is the product? What stage is it in?
- What are the current strategic goals or OKRs? (helps assess alignment)
- Any constraints to consider? (team size, technical debt, upcoming deadlines)
- Are there segments whose requests should carry more weight? (enterprise, churning users, power users)

### Step 3: Categorize and Analyze

Apply the **analyze-feature-requests** skill:

- **Theme clustering**: Group similar requests into themes (e.g., "reporting & analytics", "collaboration", "mobile experience")
- **Request count per theme**: How many unique requests map to each theme
- **Strategic alignment**: Rate each theme against stated goals (High/Medium/Low/None)
- **Segment analysis**: Which user segments are driving which themes
- **Sentiment signals**: Are requests accompanied by frustration, churn threats, or delight?

### Step 4: Prioritize

Apply the **prioritize-features** skill:

For each theme (and the top individual requests within each theme):

| Factor | Assessment |
|--------|-----------|
| **Impact** | How many users affected? How severely? |
| **Strategic alignment** | Does it serve current goals? |
| **Effort estimate** | T-shirt size (S/M/L/XL) |
| **Risk** | What happens if we don't do this? |
| **Revenue signal** | Is this tied to deals, retention, or expansion? |

Rank themes and produce a prioritized list.

### Step 5: Generate Triage Report

```
## Feature Request Triage Report

**Date**: [today]
**Requests analyzed**: [count]
**Themes identified**: [count]

### Theme Summary
| # | Theme | Requests | Top Ask | Alignment | Impact | Effort | Priority |
|---|-------|----------|---------|-----------|--------|--------|----------|

### Priority 1: Act Now
[Themes/requests to include in near-term planning]
- **[Theme]**: [X] requests — [why it's urgent]
  - Top requests: [list]
  - Recommended action: [build / prototype / investigate]

### Priority 2: Plan Next
[Themes worth planning but not urgent]

### Priority 3: Collect More Signal
[Themes with potential but insufficient evidence]

### Priority 4: Decline or Defer
[Requests that don't align with strategy — with rationale]

### Notable Individual Requests
[High-value one-off requests that didn't cluster into themes]

### Patterns and Insights
- [Key insight about what users are telling you]
- [Segment-specific patterns]
- [Gaps between what users ask for and underlying needs]
```

Save the report as a markdown file to the user's workspace.

### Step 6: Offer Next Steps

- "Want me to **create user stories** for the top-priority items?"
- "Should I **brainstorm solutions** for any of these themes?"
- "Want me to **design experiments** to validate demand before building?"
- "Should I **draft a stakeholder update** summarizing this analysis?"

## Notes

- If the user provides a CSV with columns, preserve the data structure and enrich it
- Look for the need behind the request — "add dark mode" might really mean "reduce eye strain during long sessions"
- Flag requests that conflict with each other (e.g., "simplify the UI" vs. "add more configuration options")
- If request volume is large (50+), summarize themes first and offer to drill into specific themes on request
- Output the enriched data as a downloadable CSV if the input was structured data
