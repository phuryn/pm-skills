---
description: Brainstorm product ideas or experiments from PM, Designer, and Engineer perspectives — for existing or new products
argument-hint: "[ideas|experiments] [existing|new] <product or feature description>"
---

You are executing the /brainstorm workflow: Multi-Perspective Ideation.

Generate creative product ideas or experiment designs from three perspectives (PM, Designer, Engineer), tailored to whether you're working on an existing product or building something new.

## Input

${ARGUMENTS:-No mode or topic provided — ask whether they want ideas or experiments, for an existing or new product, and the product or feature.}

## Workflow

### Step 1: Determine Mode

Parse the arguments to identify two dimensions:

1. **What to brainstorm**: `ideas` (feature concepts) or `experiments` (validation tests)
2. **Product stage**: `existing` (continuous discovery) or `new` (initial discovery)

If either dimension is missing, ask the user. If both are missing, ask:
- "Are you brainstorming **ideas** for what to build, or **experiments** to validate assumptions?"
- "Is this for an **existing** product or a **new** product concept?"

### Step 2: Gather Context

Ask the user for context. Be conversational — ask the most critical question first:

**For existing products:**
- What is the product? Who are current users?
- What opportunity area or problem space are you exploring?
- Any constraints (technical debt, platform limitations, team capacity)?
- What has been tried before?

**For new products:**
- What is the product concept? What problem does it solve?
- Who is the target user? What's their current alternative?
- What stage are you at? (napkin sketch, validated problem, early prototype)
- What are the riskiest assumptions?

Accept context from uploaded files (PRDs, research docs, strategy decks), pasted text, or conversation.

### Step 3: Generate Output

**If brainstorming ideas** — apply the **brainstorm-ideas-existing** or **brainstorm-ideas-new** skill:
- Generate ideas from three perspectives: Product Manager (user value, business impact), Designer (UX, delight, accessibility), Engineer (technical innovation, platform leverage, scalability)
- For each idea: name, description, target user impact, feasibility assessment
- Rank the top 5 ideas with rationale
- Flag which ideas could be quick wins vs. strategic bets

**If brainstorming experiments** — apply the **brainstorm-experiments-existing** or **brainstorm-experiments-new** skill:
- For existing products: suggest A/B tests, prototypes, fake-door tests, wizard-of-oz, concierge experiments, and spikes
- For new products: create XYZ+S hypotheses and suggest pretotype experiments (landing pages, explainer videos, pre-orders, concierge MVPs)
- For each experiment: hypothesis, method, success criteria, effort estimate, expected timeline
- Rank by learning-per-effort ratio

### Step 4: Deepen and Iterate

After presenting initial results, offer:
- "Want me to **detail** any of these ideas into a fuller spec?"
- "Should I **identify assumptions** behind the top ideas?" (chains into the `identify-assumptions-existing` or `identify-assumptions-new` skill)
- "Want to **design experiments** to validate the top ideas?" (chains into experiment mode)
- "Should I **prioritize** these against your current backlog?" (chains into the `prioritize-features` skill)

## Output Format

### For Ideas:
```
## Brainstorm: [Product/Feature Area]
**Mode**: Ideas for [existing/new] product
**Context**: [1-2 sentence summary]

### PM Perspective
1. **[Idea Name]** — [description] | Impact: [H/M/L] | Effort: [H/M/L]
2. ...

### Designer Perspective
1. **[Idea Name]** — [description] | Impact: [H/M/L] | Effort: [H/M/L]
2. ...

### Engineer Perspective
1. **[Idea Name]** — [description] | Impact: [H/M/L] | Effort: [H/M/L]
2. ...

### Top 5 Recommendations
| Rank | Idea | Why | Quick Win? |
|------|------|-----|------------|

### Next Steps
[What to do with these ideas]
```

### For Experiments:
```
## Experiment Design: [Product/Feature Area]
**Mode**: Experiments for [existing/new] product

### Hypotheses
1. **[Hypothesis]** — XYZ format: [X]% of [Y] will [Z] within [S timeframe]

### Recommended Experiments
| # | Experiment | Tests Hypothesis | Method | Effort | Timeline |
|---|-----------|-----------------|--------|--------|----------|

### Experiment Details
[For each experiment: setup, success criteria, risks, what you'll learn]
```

## Notes

- For existing products, ground ideas in current user behavior and validated problems
- For new products, focus on desirability and feasibility risks first
- If the user uploads a research doc or interview transcript, extract insights before brainstorming
- Encourage breadth first, then depth — generate many ideas before evaluating
