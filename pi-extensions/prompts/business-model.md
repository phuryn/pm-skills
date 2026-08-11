---
description: Explore business models using Lean Canvas, Business Model Canvas, Startup Canvas, or Value Proposition frameworks
argument-hint: "[lean|full|startup|value-prop] <product or business>"
---

You are executing the /business-model workflow: Business Model Exploration.

Build and analyze business models using four complementary frameworks. Choose one or run all for a complete picture.

## Input

${ARGUMENTS:-No mode or business provided — ask which canvas they want (lean, full, startup, or value-prop) and about the product or business.}

## Modes

---

### Lean Canvas Mode

Best for: Early-stage ideas, startups, new product lines.

Apply the **lean-canvas** skill to produce a complete Lean Canvas:

```
## Lean Canvas: [Product]

| Problem (Top 3) | Solution | Unique Value Proposition |
|-----------------|----------|------------------------|
| 1. [problem]    | [solution to each] | [single clear message] |
| 2. [problem]    |          |                        |
| 3. [problem]    |          |                        |

| Key Metrics | Unfair Advantage |
|------------|-----------------|
| [what you measure] | [what can't be copied] |

| Channels | Customer Segments |
|---------|------------------|
| [how you reach them] | [who, early adopters first] |

| Cost Structure | Revenue Streams |
|---------------|----------------|
| [fixed + variable] | [how you make money] |

### Riskiest Assumptions
[What must be true for this to work — prioritized by risk]

### Experiments to Run
[How to validate the riskiest assumptions cheaply]
```

---

### Full Business Model Canvas Mode

Best for: Established products, strategic planning, investor materials.

Apply the **business-model** skill to produce all 9 building blocks:

```
## Business Model Canvas: [Product]

| Key Partners | Key Activities | Value Propositions | Customer Relationships | Customer Segments |
|-------------|---------------|-------------------|----------------------|------------------|
| [who helps you] | [core actions] | [why customers choose you] | [how you interact] | [who you serve] |

| Key Resources | | Channels | |
|-------------|---|---------|---|
| [what you need] | | [how you deliver] | |

| Cost Structure | Revenue Streams |
|---------------|----------------|
| [your costs] | [your revenue] |

### Analysis
[Strengths and weaknesses of this model]
[How the pieces reinforce each other]
[Vulnerabilities and dependencies]
```

---

### Startup Canvas Mode

Best for: New products and startups that need both strategy and business model in one artifact. Recommended over Lean Canvas and BMC for new products.

Apply the **startup-canvas** skill to produce a Startup Canvas with 9 strategy sections + business model:

```
## Startup Canvas: [Product]

### Part 1: Product Strategy

| Vision | Market Segments | Relative Costs |
|--------|----------------|---------------|
| [inspiring why] | [JTBD, first segment] | [low cost vs unique value] |

| Value Proposition | Trade-offs | Key Metrics |
|------------------|-----------|------------|
| [What before → How → What after → Alternatives] | [what you won't do] | [North Star + OMTM] |

| Growth | Capabilities | Can't/Won't |
|--------|-------------|------------|
| [PLG vs Sales-Led, channels] | [build vs partner] | [why competitors can't copy] |

### Part 2: Business Model

| Cost Structure | Revenue Streams |
|---------------|----------------|
| [fixed + variable, how they scale] | [pricing model, revenue per channel] |

### Strategy Coherence Check
[Do all elements reinforce each other?]

### Riskiest Assumptions
[What must be true — and how to test it]
```

---

### Value Proposition Mode

Best for: Refining messaging, understanding user value, product-market fit analysis.

Apply the **value-proposition** skill to produce a JTBD-framed value proposition:

```
## Value Proposition: [Product]

### For [Segment]:
1. **Who**: [target user profile]
2. **Why**: [the job they're trying to do]
3. **What Before**: [their current painful reality]
4. **How**: [your solution approach]
5. **What After**: [their improved reality]
6. **Alternatives**: [what they'd use without you, and why you're better]

### Value Proposition Statement
[One sentence: For [who] who [need], [product] is a [category] that [benefit]. Unlike [alternative], we [differentiator].]
```

---

### All Mode

Runs all four frameworks and adds a synthesis section comparing insights across frameworks.

## Workflow (All Modes)

### Step 1: Gather Context

Ask:
- What is the product or business idea?
- What stage? (idea, validated, scaling)
- Any existing business model to refine?
- Who is the target customer?

### Step 2: Generate the Selected Framework(s)

Apply the relevant skill(s) as described above.

### Step 3: Save and Iterate

Save as markdown. Offer:
- "Want me to **stress-test this model** with a SWOT or PESTLE analysis?"
- "Should I **design a pricing strategy** for the revenue streams?"
- "Want me to **build a strategy canvas** around this model?"
- "Should I **identify the beachhead segment**?"

## Notes

- **Startup Canvas** is the recommended starting point for new products — it separates strategy from business model and covers what BMC and Lean Canvas miss (vision, trade-offs, metrics, Can't/Won't)
- **Lean Canvas** is best for speed and hypothesis testing — don't overthink it, but be aware it mixes strategy and business model into one artifact
- **BMC** is better for mature businesses that need to articulate how everything connects, but lacks strategic sections (vision, trade-offs, metrics)
- **Value Proposition** is the sharpest tool for product-market fit conversations
- In "all" mode, highlight where frameworks agree (strong signal) and where they diverge (needs investigation)
