---
description: Tailor a PM resume to a specific job description — keyword alignment, experience reframing, and strategic optimization
argument-hint: "<resume> + <job description>"
---

You are executing the /tailor-resume workflow: Resume-to-JD Optimization.

Take your resume and a target job description, then strategically align your experience to maximize interview chances. Keyword optimization, bullet point rewriting, and gap analysis.

## Input

${ARGUMENTS:-No input was provided — ask the user for: <resume> + <job description>.}

## Workflow

### Step 1: Accept Both Documents

Need two inputs:
- The resume (text, PDF, or DOCX)
- The target job description (text, URL, or file)

If only one is provided, ask for the other.

### Step 2: Analyze the Job Description

Extract:
- Required qualifications and skills
- Preferred qualifications
- Key responsibilities
- Industry and domain signals
- Seniority level indicators
- Cultural and team signals

### Step 3: Tailor the Resume

Apply the **review-resume** skill:

- **Keyword alignment**: Map JD keywords to resume content, add missing keywords naturally
- **Bullet point rewriting**: Reframe experience to emphasize JD-relevant accomplishments using XYZ+S formula
- **Section reordering**: Prioritize the most relevant experience
- **Summary/objective**: Rewrite to directly address the role
- **Skills section**: Align with JD requirements

### Step 4: Generate Tailored Resume + Analysis

```
## Resume Tailoring: [Job Title] at [Company]

### Alignment Score: [X/10]

### Keyword Gap Analysis
| JD Keyword | In Resume? | Recommendation |
|-----------|-----------|---------------|

### Changes Made
1. **[Section]**: [what changed and why]
2. ...

### Tailored Resume
[Full rewritten resume text]

### Gap Analysis
**Strong matches**: [where your experience directly aligns]
**Reframed matches**: [where experience was repositioned to fit]
**Gaps**: [JD requirements you don't clearly address — with suggestions]

### Cover Letter Talking Points
[3-4 points to emphasize in a cover letter that bridge remaining gaps]
```

Save tailored resume as markdown.

## Notes

- Never fabricate experience — reframe truthfully, don't invent
- The summary/objective is the highest-ROI section to customize per application
- Match the JD's language exactly where possible (if they say "cross-functional," use "cross-functional")
- For senior roles, emphasize scale and strategic impact; for IC roles, emphasize hands-on execution
