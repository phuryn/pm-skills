---
name: summarize-interview
description: "Summarize a customer interview transcript into a structured template with JTBD, satisfaction signals, and action items."
---

## Summarize Customer Interview

Transform an interview transcript into a structured summary focused on Jobs to Be Done, satisfaction, and action items.

### Context

You are summarizing a customer interview for the product discovery of **$ARGUMENTS**.

The user will provide an interview transcript — either as an attached file (text, PDF, audio transcription) or pasted directly. Read any attached files first.

### Instructions

1. **Read the full transcript** carefully before summarizing.

2. **Fill in the summary template** below. Use "-" if information is unavailable. Replace numeric values with qualitative descriptions if needed (e.g., "not satisfied").

3. **Use clear, simple language** — a primary school graduate should be able to understand the summary.

### Output Template

```
**Date**: [Date and time of the interview]
**Participants**: [Full names and roles]
**Background**: [Background information about the customer]

**Current Solution**: [What solution they currently use]

**What They Like About Current Solution**:
- [Job to be done, desired outcome, importance, and satisfaction level]

**Problems With Current Solution**:
- [Job to be done, desired outcome, importance, and satisfaction level]

**Key Insights**:
- [Unexpected findings or notable quotes]

**Action Items**:
- [Date, Owner, Action — e.g., "2025-01-15, Paweł Huryn, Follow up with customer about pricing"]
```

Save the summary as a markdown document in the user's workspace.

## Notes

- The summary is only as good as the interview quality — if the customer gave short answers, note that as a limitation.
- Look for the gap between what customers SAY and what they DO — this is where the real insights are.
- "Not satisfied" or "very satisfied" are the strongest signals — double down on those topics in the next round of interviews.
- Action items should have a specific owner and deadline, not just "follow up."
- Share summaries with the full team — the most valuable outcome of an interview is shared understanding, not a document.
---

### Further Reading

- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
