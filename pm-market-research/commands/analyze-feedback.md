---
description: Analyze user feedback at scale — sentiment analysis, theme extraction, and segment-level insights
argument-hint: "<feedback data as CSV, text, or file>"
---

# /analyze-feedback -- User Feedback Analysis

Process large volumes of user feedback (reviews, surveys, support tickets, NPS responses) into structured insights with sentiment analysis and segment-level patterns.

## Invocation

```
/analyze-feedback [upload a CSV of NPS responses]
/analyze-feedback [paste app store reviews or survey responses]
/analyze-feedback [upload support ticket export]
```

## Workflow

### Step 1: Accept Feedback Data

Accept in any format:
- CSV/Excel with feedback text (and optional metadata: date, segment, rating)
- Pasted text (reviews, survey responses, Slack messages)
- Uploaded documents or exports from feedback tools
- Social listening exports, including Hermes Tweet X/Twitter result sets with post URL, author handle, timestamp, and engagement metadata

Ask:
- What kind of feedback is this? (NPS, reviews, support tickets, survey, etc.)
- Any segments to analyze separately? (user tier, plan, geography)
- What are you looking for? (general themes, specific issues, trends over time)

### Step 2: Analyze

Apply the **sentiment-analysis** skill:

- **Sentiment scoring**: Classify each piece of feedback (positive, neutral, negative)
- **Theme extraction**: Identify recurring topics and cluster related feedback
- **Frequency analysis**: Count how often each theme appears
- **Segment analysis**: Break down sentiment and themes by user segment (if data available)
- **Trend detection**: If dates are available, identify sentiment shifts over time

### Step 3: Generate Analysis Report

```
## Feedback Analysis Report

**Date**: [today]
**Feedback analyzed**: [count] responses
**Source**: [NPS survey / app reviews / support tickets / etc.]
**Period**: [date range if available]

### Overall Sentiment
- Positive: [X%] | Neutral: [Y%] | Negative: [Z%]
- Average sentiment score: [X/10]
- Trend: [improving / stable / declining]

### Top Themes
| # | Theme | Mentions | Sentiment | Segments Most Affected |
|---|-------|----------|-----------|----------------------|

### Theme Deep-Dive

#### Theme 1: [Name] — [X] mentions, [sentiment]
- **What users are saying**: [summary with representative quotes]
- **Root cause**: [what's driving this feedback]
- **Impact**: [how this affects retention, satisfaction, or revenue]
- **Recommendation**: [what to do about it]

[Repeat for top 5-8 themes]

### Segment Analysis
| Segment | Volume | Avg Sentiment | Top Theme | Key Difference |
|---------|--------|-------------|-----------|---------------|

### Notable Quotes
> "[quote]" — [segment, sentiment]

### Trends Over Time
[If date data available: chart-ready data showing sentiment shifts]

### Actionable Insights
1. [Insight + recommended action]
2. ...

### Gaps
[What this feedback doesn't tell you — suggested follow-up research]
```

Save as markdown. If input was structured data (CSV), also save enriched data with sentiment scores as CSV.

### Step 4: Offer Next Steps

- "Want me to **create user personas** from these feedback patterns?"
- "Should I **triage the top themes as feature requests**?"
- "Want me to **design an interview script** to go deeper on a specific theme?"

## Notes

- Sentiment analysis is approximate — flag edge cases (sarcasm, mixed sentiment, non-English text)
- Theme extraction should look for needs behind requests, not just surface-level topics
- If sample sizes are small per segment, note limited confidence
- For NPS data specifically, analyze Detractors (0-6), Passives (7-8), and Promoters (9-10) separately
- Output enriched CSV when input is structured, so the user can use it in their own tools
