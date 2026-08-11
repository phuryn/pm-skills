---
description: Brainstorm marketing ideas, positioning, value prop statements, and product names — creative marketing toolkit
argument-hint: "<product or marketing challenge>"
---

You are executing the /market-product workflow: Marketing Creative Toolkit.

Generate creative marketing assets: campaign ideas, positioning statements, value prop copy, and product naming options. All in one workflow or pick specific modules.

## Input

${ARGUMENTS:-No input was provided — ask the user for: <product or marketing challenge>.}

## Workflow

### Step 1: Understand the Marketing Need

Ask:
- What is the product? Target audience?
- What do you need? (full marketing toolkit, or specific: ideas, positioning, naming, copy)
- What's the context? (launch, rebrand, campaign, competitive repositioning)
- Any existing brand guidelines or tone of voice?

### Step 2: Generate Based on Need

**Marketing Ideas** — apply **marketing-ideas** skill:
- 5 creative, cost-effective campaign ideas
- Each with: channel, messaging angle, engagement rationale, estimated effort
- Mix of quick wins and bigger bets

**Positioning** — apply **positioning-ideas** skill:
- Identify top 5 competitors for positioning context
- Generate 3-5 positioning statements differentiated from each
- Include rationale for each positioning angle

**Value Proposition Statements** — apply **value-prop-statements** skill:
- Generate copy for marketing, sales, and onboarding contexts
- Segment-specific variations
- Short (tagline), medium (elevator pitch), and long (landing page) versions

**Product Naming** — apply **product-name** skill:
- Brainstorm 5 unique, memorable names
- Each with: rationale, brand alignment, domain availability notes
- Check for unintended meanings or conflicts

### Step 3: Generate Output

```
## Marketing Toolkit: [Product]

**Date**: [today]
**Context**: [launch / rebrand / campaign / etc.]

### Marketing Campaign Ideas
| # | Idea | Channel | Effort | Expected Impact |
|---|------|---------|--------|----------------|

### Positioning Options
| # | Positioning | vs Competitor | Strength | Risk |
|---|-----------|--------------|----------|------|

**Recommended positioning**: [which and why]

### Value Prop Copy
**Tagline**: [one line]
**Elevator pitch**: [2-3 sentences]
**Landing page hero**: [headline + subheading]
**Sales one-liner**: [for sales conversations]

### Product Name Options (if requested)
| # | Name | Rationale | Domain | Risk |
|---|------|----------|--------|------|

### Messaging Matrix
| Audience | Key Message | Proof Point | CTA |
|----------|-----------|------------|-----|
```

Save as markdown.

### Step 4: Offer Next Steps

- "Want me to **draft full marketing content** (blog post, email, social)?"
- "Should I **define the North Star metric** for this campaign?"
- "Want me to **create a competitive battlecard** to support positioning?"
- "Should I **plan the full launch**?"

## Notes

- Positioning should be tested, not assumed — recommend A/B testing headlines
- Value prop copy should use the customer's language, not internal jargon
- Marketing ideas should be specific and actionable, not generic ("use social media")
- Product names should be checked for trademark conflicts before committing
- Always tie marketing back to customer JTBD, not product features
