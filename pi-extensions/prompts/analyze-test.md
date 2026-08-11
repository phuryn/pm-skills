---
description: Analyze A/B test results — statistical significance, sample size validation, and ship/extend/stop recommendations
argument-hint: "<test results as data, screenshot, or description>"
---

You are executing the /analyze-test workflow: A/B Test Analysis.

Evaluate experiment results with statistical rigor and translate findings into a clear product decision: ship, extend, or stop.

## Input

${ARGUMENTS:-No input was provided — ask the user for: <test results as data, screenshot, or description>.}

## Workflow

### Step 1: Accept Test Data

Accept in any format:
- Summary statistics (conversion rates, sample sizes per variant)
- Raw event data (CSV with user_id, variant, converted, timestamp)
- Screenshot from an experimentation platform (Optimizely, LaunchDarkly, etc.)
- Description of the experiment and results

### Step 2: Validate Test Design

Before analyzing results, check:
- Was sample size sufficient? (run a power analysis)
- Was the test run long enough? (capture weekly cycles, minimum 1-2 business cycles)
- Was randomization clean? (check for sample ratio mismatch)
- Were there any external factors during the test period?

Flag issues if found — results from a flawed test can be misleading.

### Step 3: Analyze Results

Apply the **ab-test-analysis** skill:

- **Statistical significance**: Calculate p-value and confidence interval
- **Effect size**: Absolute and relative difference between variants
- **Practical significance**: Is the effect large enough to matter for the business?
- **Confidence interval**: What's the range of plausible true effects?
- **Segment analysis**: If data allows, check for differential effects by user segment

### Step 4: Generate Analysis

```
## A/B Test Analysis: [Test Name]

**Date**: [today]
**Test duration**: [X days/weeks]
**Total sample**: [N users]

### Results Summary
| Variant | Sample | Metric | Rate | 95% CI |
|---------|--------|--------|------|--------|
| Control | [n] | [metric] | [X%] | [X% - Y%] |
| Variant | [n] | [metric] | [X%] | [X% - Y%] |

### Statistical Analysis
- **Relative lift**: [+X%] ([CI range])
- **P-value**: [X]
- **Statistically significant**: [Yes/No] at 95% confidence
- **Minimum detectable effect**: [X%] (what the test was powered to detect)

### Sample Size Check
- **Required sample**: [N] per variant (for [X%] MDE at 80% power)
- **Actual sample**: [N] per variant
- **Verdict**: [Sufficiently powered / Underpowered / Overpowered]

### Decision

**Recommendation: [SHIP / EXTEND / STOP]**

[Clear explanation of why, considering both statistical and practical significance]

### Business Impact Estimate
If shipped to 100% of users:
- **Expected impact**: [metric change per month/quarter]
- **Revenue impact**: [if applicable]
- **Confidence**: [How certain we are about this estimate]

### Caveats
- [Any concerns about the test validity]
- [Segments where results differ]
- [Novelty effects or other biases to consider]

### Follow-Up
- [What to test next based on learnings]
- [Monitoring plan if shipping the variant]
```

### Step 5: Offer Next Steps

- "Want me to **design a follow-up experiment** based on these findings?"
- "Should I **run the analysis for specific segments**?"
- "Want me to **generate the SQL** to monitor this metric post-launch?"

## Notes

- Statistical significance ≠ practical significance — a 0.1% lift can be significant with enough data but not worth shipping
- Always check for sample ratio mismatch before trusting results
- Novelty effects can inflate short-term results — recommend monitoring for 2-4 weeks post-launch
- If the test is underpowered, the right answer is usually "extend" not "no effect"
- For revenue metrics, use confidence intervals to estimate best-case and worst-case business impact
- If data is provided as CSV, generate the full analysis using Python with scipy.stats
