---
name: ab-test-analysis
description: "Analyze A/B test results with statistical significance, sample size validation, confidence intervals, and ship/extend/stop recommendations. Use when evaluating experiment results, checking if a test reached significance, interpreting split test data, or deciding whether to ship a variant."
---

## A/B Test Analysis

Evaluate A/B test results with statistical rigor and translate findings into clear product decisions.

### Context

You are analyzing A/B test results for **$ARGUMENTS**.

If the user provides data files (CSV, Excel, or analytics exports), read and analyze them directly. Generate Python scripts for statistical calculations when needed.

### Instructions

1. **Understand the experiment**:
   - What was the hypothesis?
   - What was changed (the variant)?
   - What is the primary metric? Any guardrail metrics?
   - How long did the test run?
   - What is the traffic split?

2. **Validate the test setup**:
   - **Sample size**: Is the sample large enough for the expected effect size?
     - For an independent binary conversion metric, equal allocation, and a fixed-horizon, two-sided test, use the normal-approximation sample size **per arm**:
       `n = ceil((z_(1-alpha/2) * sqrt(2*p_bar*(1-p_bar)) + z_(1-beta) * sqrt(p0*(1-p0) + p1*(1-p1)))^2 / (p1-p0)^2)`
     - Define the planned baseline `p0`, alternative `p1`, `p_bar = (p0+p1)/2`, significance level `alpha`, and target power `1-beta` (usually at least 80%). Here `z_q` is the standard normal quantile at probability `q`; `ceil` rounds up. Use the **absolute** MDE `abs(p1-p0)`, not relative lift, and report total sample size as `2*n`.
     - Example: `p0=0.20`, `p1=0.22` (2 percentage points, or 10% relative lift), `alpha=0.05`, and 80% power require approximately **6,510 observations per arm** (13,020 total). The significance-only formula omits the power term and understates the required sample.
     - Compare achieved sample sizes with the prespecified design; flag power below the target (normally 80%) at the planned MDE. Do not substitute the observed lift into a post-hoc power calculation. If baseline, MDE, or target power is missing, ask for it or label any assumption explicitly.
     - This approximation assumes independent observations and sufficiently large expected success/failure counts. Use a design-appropriate power calculation for unequal allocation, non-binary metrics, clustered observations, rare events, sequential testing, or multiplicity adjustments.
   - **Duration**: Did the test run for at least 1-2 full business cycles?
   - **Randomization**: Any evidence of sample ratio mismatch (SRM)?
   - **Novelty/primacy effects**: Was there enough time to wash out initial behavior changes?

3. **Calculate statistical significance**:
   - **Conversion rate** for control and variant
   - **Relative lift**: (variant - control) / control × 100
   - **p-value**: Using a two-tailed z-test or chi-squared test
   - **Confidence interval**: 95% CI for the difference
   - **Statistical significance**: Is p < 0.05?
   - **Practical significance**: Is the lift meaningful for the business?

   If the user provides raw data, generate and run a Python script to calculate these.

4. **Check guardrail metrics**:
   - Did any guardrail metrics (revenue, engagement, page load time) degrade?
   - A winning primary metric with degraded guardrails may not be a true win

5. **Interpret results**:

   | Outcome | Recommendation |
   |---|---|
   | Significant positive lift, no guardrail issues | **Ship it** — roll out to 100% |
   | Significant positive lift, guardrail concerns | **Investigate** — understand trade-offs before shipping |
   | Not significant, positive trend | **Extend the test** — need more data or larger effect |
   | Not significant, flat | **Stop the test** — no meaningful difference detected |
   | Significant negative lift | **Don't ship** — revert to control, analyze why |

6. **Provide the analysis summary**:
   ```
   ## A/B Test Results: [Test Name]

   **Hypothesis**: [What we expected]
   **Duration**: [X days] | **Sample**: [N control / M variant]

   | Metric | Control | Variant | Lift | p-value | Significant? |
   |---|---|---|---|---|---|
   | [Primary] | X% | Y% | +Z% | 0.0X | Yes/No |
   | [Guardrail] | ... | ... | ... | ... | ... |

   **Recommendation**: [Ship / Extend / Stop / Investigate]
   **Reasoning**: [Why]
   **Next steps**: [What to do]
   ```

Think step by step. Save as markdown. Generate Python scripts for calculations if raw data is provided.

---

### Further Reading

- [A/B Testing 101 + Examples](https://www.productcompass.pm/p/ab-testing-101-for-pms)
- [Testing Product Ideas: The Ultimate Validation Experiments Library](https://www.productcompass.pm/p/the-ultimate-experiments-library)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
