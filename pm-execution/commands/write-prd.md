---
description: Create a lean Product Requirements Document from a feature idea or problem statement, with a fuller spec on request
argument-hint: "<feature or problem statement>"
---

# /write-prd -- Product Requirements Document

Create a lean PRD that aligns stakeholders and guides development. Accepts anything from a vague idea to a detailed brief.

## Invocation

```
/write-prd SSO support for enterprise customers
/write-prd Users are dropping off during onboarding — we need to fix step 3
/write-prd [upload a brief, research doc, or strategy deck]
```

## Workflow

### Step 1: Understand the Feature

Accept the input in any form:
- A feature name ("SSO support")
- A problem statement ("Enterprise customers keep asking for centralized auth")
- A user request ("Users want to export their data as CSV")
- A vague idea ("We should do something about onboarding drop-off")
- An uploaded document (brief, research, Slack thread, email)

### Step 2: Fill Only the Gaps That Matter

Extract what the input already gives you, and research what the web can answer (prior art, competitors, market context) instead of asking. If any of these three is missing, ask about it before writing, in one message, three questions at most:

1. **User problem**: What problem does this solve? Who experiences it, and how painful is it?
2. **Target users**: Which user segment(s)? What's their current workaround?
3. **Success metrics**: How will we know this worked? What moves if we nail it?

Constraints, prior art, and scope preference are worth asking about only if the user wants the detailed version. If the user says "just write it", go ahead and mark the gaps as assumptions.

### Step 3: Generate the PRD

Apply the **create-prd** skill: its 8-section template, lean by default (about one to two pages). Write the detailed version only if the user asks for it. Start the document with:

```
## Product Requirements Document: [Feature Name]

**Author**: [user]
**Date**: [today]
**Status**: Draft
```

Then the eight sections: Summary, Contacts (if known), Background, Objective, Market Segment(s), Value Proposition(s), Solution, Release. Market Segments and Value Propositions are always included; each value proposition uses the 6-part template (Who, Why, What before, How, What after, Alternatives). Put what the first version will not do in Release, and what's still unknown in Solution → Assumptions and open questions.

### Step 4: Review and Iterate

After generating, say in one line what you left out on purpose, then offer:
- "Want the **detailed version**, or should I expand a specific section?"
- "Want me to **tighten the scope** further? I can challenge what really needs to be in the first version."
- "Should I **run a pre-mortem** on this PRD?"
- "Want me to **break this into user stories** for engineering?"
- "Should I **create a stakeholder update** to socialize this?"

Save the PRD as a markdown file to the user's workspace.

## Notes

- Be opinionated about scope — a tight PRD is better than an expansive vague one
- If the idea is too big, proactively suggest phasing and spec only Phase 1
- Non-goals are as important as goals — they prevent scope creep
- Success metrics must be specific: "improve NPS" is bad, "increase NPS from 32 to 45 within 90 days of launch" is good
- Open questions should be genuinely unresolved — don't list things you can answer from context
- If the user provides research, weave insights into the Background section with attribution
