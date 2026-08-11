---
description: Create a comprehensive product strategy using the 9-section Strategy Canvas — from vision to defensibility
argument-hint: "<product or company>"
---

You are executing the /strategy workflow: Product Strategy Canvas.

Build a complete product strategy document using the 9-section Product Strategy Canvas. Covers vision, segments, value propositions, trade-offs, metrics, growth, capabilities, and defensibility.

## Input

${ARGUMENTS:-No product was provided — ask the user what product or company the strategy is for.}

## Workflow

### Step 1: Understand the Product

Accept context from:
- Product description (verbal or written)
- Uploaded documents (strategy decks, pitch decks, PRDs, business plans) — read any file the user references
- Existing strategy to refine or challenge

Ask key questions:
- What does the product do? Who is it for?
- What stage is it in? (idea, MVP, growth, mature)
- What's the business model?
- What triggered the need for a strategy document? (new product, pivot, annual planning, fundraise)

### Step 2: Build the Strategy Canvas

Apply the **product-strategy** and **product-vision** skills (installed in this environment — load their SKILL.md files for the full frameworks):

Work through all 9 sections of the Strategy Canvas:

1. **Vision**: Inspiring north star that motivates the team
2. **Target Segments**: Who you serve (and who you don't)
3. **Pain Points & Value**: Problems you solve and the value you create
4. **Value Propositions**: JTBD-framed value for each segment
5. **Strategic Trade-offs**: What you choose NOT to do (as important as what you do)
6. **Key Metrics**: How you measure success
7. **Growth Engine**: How you acquire and expand users
8. **Core Capabilities**: What you need to build and maintain
9. **Defensibility**: What makes this hard to copy (network effects, data, brand, switching costs)

For each section, provide specific content — not generic advice.

### Step 3: Generate Strategy Document

```
## Product Strategy: [Product Name]

**Date**: [today]
**Stage**: [idea / MVP / growth / mature]
**Author**: [user]

### 1. Vision
[Inspiring, achievable, emotional — 2-3 sentences max]

### 2. Target Segments
| Segment | Size | Pain Level | Current Alternative | Priority |
|---------|------|-----------|-------------------|----------|

**Primary segment**: [who and why]
**Explicitly not serving**: [who and why]

### 3. Pain Points & Value Created
[For each segment: the problem, current cost, and value your solution delivers]

### 4. Value Propositions
**For [Segment A]**: When [situation], they want [motivation], so they can [outcome]
**For [Segment B]**: When [situation], they want [motivation], so they can [outcome]

### 5. Strategic Trade-offs
| We Choose | Over | Because |
|-----------|------|---------|

### 6. Key Metrics
- **North Star**: [metric]
- **Input Metrics**: [3-5 levers]
- **Health Metrics**: [guardrails]

### 7. Growth Engine
[How you acquire, activate, and expand — specific mechanisms, not generic]

### 8. Core Capabilities
| Capability | Build / Buy / Partner | Investment Level | Timeline |
|-----------|---------------------|-----------------|----------|

### 9. Defensibility
[What creates a moat — be specific about which type: network effects, data, brand, switching costs, economies of scale]

### Strategic Risks
[Top 3 things that could invalidate this strategy]

### Next Steps
[What to do with this strategy — socialize, test, build]
```

Save as markdown.

### Step 4: Offer Next Steps

- "Want me to **build a Lean Canvas** or **Business Model Canvas** for this?"
- "Should I **create a roadmap** aligned to this strategy?"
- "Want me to **run a macro environment scan** to stress-test assumptions?"
- "Should I **define OKRs** based on Section 6?"

## Notes

- A good strategy is more about what you say NO to than what you say YES to — push hard on trade-offs
- Vision should be emotional and memorable, not a corporate statement
- Defensibility is the hardest section — most products don't have a real moat yet, and that's OK to acknowledge
- If the product is early-stage, some sections will be hypotheses — label them as such
- Strategy should fit on one page for executives — offer a condensed version
