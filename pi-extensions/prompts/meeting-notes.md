---
description: Summarize a meeting transcript into structured notes with decisions, action items, and follow-ups
argument-hint: "<transcript or meeting notes>"
---

You are executing the /meeting-notes workflow: Meeting Summary.

Transform a raw meeting transcript or rough notes into clear, structured meeting minutes with decisions captured and action items assigned.

## Input

${ARGUMENTS:-No input was provided — ask the user for: <transcript or meeting notes>.}

## Workflow

### Step 1: Accept the Transcript

Accept in any format:
- Full transcript (from Otter, Fireflies, Google Meet, Zoom, etc.)
- Rough notes taken during the meeting
- Audio summary or meeting recap from a transcription tool
- Multiple inputs (e.g., transcript + the user's own notes)

If the input is sparse, work with what's available and flag gaps.

### Step 2: Extract and Structure

Apply the **summarize-meeting** skill:

Parse the content to identify:
- **Participants**: Who was present (from introductions, speaker labels, or mentions)
- **Topics discussed**: Major agenda items or conversation threads
- **Decisions made**: Explicit agreements or conclusions reached
- **Action items**: Tasks assigned, with owner and deadline if mentioned
- **Open questions**: Unresolved items that need follow-up
- **Key quotes**: Important statements worth preserving verbatim
- **Context**: Meeting type, project, and background

### Step 3: Generate Meeting Summary

```
## Meeting Summary

**Date**: [date if known]
**Participants**: [names/roles]
**Meeting type**: [standup, planning, review, 1:1, stakeholder, etc.]
**Topic**: [primary subject]

### Summary
[3-5 sentence overview of what was discussed and concluded]

### Key Decisions
1. **[Decision]** — [context and rationale]
2. ...

### Action Items
| # | Action | Owner | Deadline | Status |
|---|--------|-------|----------|--------|

### Discussion Highlights
**[Topic 1]**: [key points, different perspectives, conclusion]
**[Topic 2]**: [key points, different perspectives, conclusion]

### Open Questions
- [Question] — needs input from [person/team]

### Next Steps
- [What happens next]
- Next meeting: [if mentioned]
```

Save as markdown.

### Step 4: Offer Follow-ups

- "Want me to **email these notes** to participants?"
- "Should I **create tickets** from the action items?"
- "Want me to **draft a stakeholder update** based on the decisions made?"

## Notes

- Decisions are the most valuable output — make sure every decision is captured clearly
- Action items without owners are useless — if no owner was mentioned, flag it
- Keep the summary concise — people who weren't in the meeting should get the gist in 30 seconds
- If the transcript is very long (60+ min meeting), offer a TL;DR before the full summary
- Distinguish between "discussed" and "decided" — many topics are explored without reaching a conclusion
