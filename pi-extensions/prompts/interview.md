---
description: Prepare a customer interview script or summarize an interview transcript into structured insights
argument-hint: "[prep|summarize] <topic or transcript>"
---

You are executing the /interview workflow: Customer Interview Prep & Summary.

Two modes: **prep** creates a structured interview script before you talk to customers, **summarize** extracts insights after you've done the interview.

## Input

${ARGUMENTS:-No mode or topic provided — ask whether they want to prepare an interview script (prep) or summarize a transcript (summarize), and the topic or transcript.}

## Modes

---

### Prep Mode

Create a structured interview script tailored to your research question.

#### Workflow

**Step 1: Understand the Research Goal**

Ask the user:
- What are you trying to learn? (specific research question)
- Who are you interviewing? (segment, role, relationship to product)
- How much time do you have? (15 min, 30 min, 60 min)
- What decisions will this research inform?

**Step 2: Generate Interview Script**

Apply the **interview-script** skill:

- Follow "The Mom Test" principles — ask about their life, not your idea
- No leading questions, no pitching, focus on past behavior and real situations
- Structure the script in sections:

```
## Interview Script: [Research Topic]

**Research Question**: [what we're trying to learn]
**Target Participant**: [who]
**Duration**: [X] minutes

### Warm-up (3-5 min)
[Rapport-building questions, role/context understanding]

### Core Exploration (15-40 min)
[JTBD probing, past behavior, current workflow, pain points]
- For each question: the question + why you're asking it + follow-up prompts

### Specific Topics (5-10 min)
[Targeted questions about specific features or concepts — if needed]

### Wrap-up (3-5 min)
[Open-ended closing, referral ask, next steps]

### Note-Taking Template
[Pre-formatted template to capture insights during the interview]

### Red Flags to Watch For
[Signs the conversation is going off-track or the participant is being polite rather than honest]
```

**Step 3: Customize and Review**

- Adjust question count to fit the time slot
- Add probing questions for specific hypotheses the user wants to test
- Flag questions that might lead the witness
- Offer a printable version (markdown file saved to workspace)

---

### Summarize Mode

Transform an interview transcript into structured, actionable insights.

#### Workflow

**Step 1: Accept the Transcript**

Accept in any format:
- **Pasted text**: Raw transcript or notes
- **Uploaded file**: Document, text file, or meeting notes export
- **Audio summary**: If the user describes what was said (not a full transcript)

If the input is rough notes rather than a full transcript, work with what's available and note the limitations.

**Step 2: Extract and Structure**

Apply the **summarize-interview** skill:

Parse the transcript to identify:
- **Participant profile**: Role, experience level, segment, context
- **Jobs to Be Done**: What the participant is trying to accomplish
- **Current workflow**: How they solve the problem today
- **Pain points**: Frustrations, workarounds, time sinks
- **Satisfaction signals**: What works well, moments of delight
- **Quotes**: Verbatim quotes that capture key insights (with timestamps if available)
- **Surprises**: Anything unexpected or that contradicts assumptions
- **Feature reactions**: If specific features/concepts were discussed, capture reactions

**Step 3: Generate Interview Summary**

```
## Interview Summary

**Participant**: [anonymized profile — role, segment, experience]
**Date**: [if known]
**Duration**: [if known]
**Interviewer**: [if known]

### Key Insights
1. **[Insight]** — [supporting evidence/quote]
2. **[Insight]** — [supporting evidence/quote]
3. ...

### Jobs to Be Done
- **Primary JTBD**: [When I..., I want to..., so I can...]
- **Related JTBDs**: [additional jobs]

### Current Workflow
[How the participant currently solves the problem, step by step]

### Pain Points
| Pain Point | Severity | Quote |
|-----------|----------|-------|

### Satisfaction Signals
| What Works | Why | Quote |
|-----------|-----|-------|

### Notable Quotes
> "[quote]" — on [topic]

### Assumptions Validated / Invalidated
| Assumption | Status | Evidence |
|-----------|--------|----------|

### Action Items
- [ ] [Follow-up action from this interview]
- [ ] [Research question to explore further]

### Raw Notes
[If helpful, include annotated key sections]
```

Save the summary as a markdown file.

**Step 4: Connect to Broader Research**

Offer:
- "Want me to **compare this with other interview summaries** you've done?"
- "Should I **update assumptions** based on what this participant said?"
- "Want me to **extract personas** from multiple interviews?"

## Notes

- In prep mode, always include "why you're asking" annotations — they help the interviewer stay on track
- In summarize mode, distinguish between what the participant *said* vs. what they *did* (behavioral > stated)
- Flag contradictions within the same interview (says one thing, describes doing another)
- If the transcript mentions competitor products, capture competitive intelligence
- For summarize mode, if multiple transcripts are provided, synthesize across them with cross-participant patterns
