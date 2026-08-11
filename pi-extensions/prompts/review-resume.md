---
description: Comprehensive PM resume review against 10 best practices — structure, impact metrics, keywords, and actionable feedback
argument-hint: "<resume as text or file>"
---

You are executing the /review-resume workflow: PM Resume Review.

Get a thorough resume review against product management best practices. Evaluates structure, impact metrics, keyword optimization, and provides specific improvement suggestions with examples.

## Input

${ARGUMENTS:-No resume was provided — ask the user to paste their resume text or give you a file path to read.}

If the input is a file path (or the user references a file), read the full file content first. Otherwise treat the input as pasted resume text.

## Workflow

### Step 1: Accept the Resume

Accept as pasted text or a file (PDF, DOCX, markdown, text). Parse the full content. If the file can't be read directly (e.g. binary PDF), extract the text with the tools available and tell the user what you could and couldn't parse.

### Step 2: Evaluate Against 10 Best Practices

Apply the **review-resume** skill (installed in this environment — load its SKILL.md for the full framework):

1. **Impact Metrics**: Are accomplishments quantified? (revenue, users, conversion rates)
2. **XYZ+S Formula**: "Accomplished [X] as measured by [Y], by doing [Z] using [S skill/tool]"
3. **PM-Specific Language**: Uses product terminology (shipped, led discovery, defined strategy)
4. **Structure & Readability**: Clear sections, consistent formatting, scannable
5. **Keyword Optimization**: Matches common PM job description keywords
6. **Story Arc**: Shows career progression and increasing scope
7. **Brevity**: One page (junior), two pages max (senior). No fluff.
8. **Relevance**: Experience tailored to PM roles, not generic
9. **Technical Credibility**: Demonstrates working with engineering, data, design
10. **Leadership Signals**: Cross-functional influence, stakeholder management, mentoring

### Step 3: Generate Review

```
## Resume Review

**Overall Score**: [X/10]
**Strongest area**: [which best practice]
**Biggest opportunity**: [which best practice]

### Scorecard
| # | Best Practice | Score | Assessment |
|---|-------------|-------|-----------|
| 1 | Impact Metrics | [/10] | [brief assessment] |
| 2 | XYZ+S Formula | [/10] | [brief assessment] |
| ... | ... | ... | ... |

### Top 3 Improvements

**1. [Most impactful change]**
- Current: "[exact text from resume]"
- Suggested: "[improved version]"
- Why: [reasoning]

**2. [Second improvement]**
[same format]

**3. [Third improvement]**
[same format]

### Section-by-Section Feedback
[Specific notes for each resume section: summary, experience, education, skills]

### Missing Elements
[What's absent that should be present for a PM resume]

### Keywords to Add
[PM-relevant keywords missing from the resume that appear in typical job descriptions]
```

Save as markdown.

### Step 4: Offer Next Steps

- "Want me to **tailor this resume** to a specific job description?"
- "Should I **rewrite specific bullet points** using the XYZ+S formula?"
- "Want me to **generate a cover letter** based on this resume?"

## Notes

- Be specific and constructive — "add metrics" is unhelpful, "change 'improved onboarding' to 'reduced onboarding drop-off by 23% (450 → 347 users/month)'" is actionable
- PM resumes should emphasize outcomes over outputs, influence over authority
- ATS (Applicant Tracking System) optimization matters — mention relevant keywords naturally
- Different PM levels have different expectations: APM = potential, Senior PM = impact, Director+ = scale
