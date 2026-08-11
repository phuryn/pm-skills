---
description: Design a value proposition using the 6-part JTBD template — Who, Why, What before, How, What after, Alternatives
argument-hint: "<product or feature>"
---

You are executing the /value-proposition workflow: Value Proposition Design.

Design a clear, compelling value proposition for a product or feature using the 6-part JTBD template. An alternative to Strategyzer's Value Proposition Canvas that starts with the customer and focuses on practical outcomes.

## Input

${ARGUMENTS:-No input was provided — ask the user for: <product or feature>.}

## Workflow

### Step 1: Understand the Product and Market

Accept context from:
- Product description (verbal or written)
- Uploaded documents (pitch decks, PRDs, competitive analyses)
- Existing value propositions to refine

Ask key questions:
- What does the product do? Who is it for?
- What alternatives or workarounds exist today?
- What customer insights or research do you have?

### Step 2: Build the Value Proposition

Apply the **value-proposition** skill to produce the 6-part template:

```
## Value Proposition: [Product]

### For [Segment]:

1. **Who**: [target user profile and characteristics]
2. **Why**: [the job they're trying to do, desired outcomes]
3. **What Before**: [their current painful reality — existing tools, friction, workarounds]
4. **How**: [your solution — specific features and capabilities that deliver value]
5. **What After**: [the improved outcome — what becomes possible]
6. **Alternatives**: [what they'd use without you, and why you're better]

### Value Proposition Statement
[One sentence: For [who] who [need], [product] is a [category] that [benefit]. Unlike [alternative], we [differentiator].]

### Value Proposition Statements (Reusable)
- Marketing: [...]
- Sales: [...]
- Onboarding: [...]
```

If the user has multiple segments, create a separate value proposition for each.

### Step 3: Save and Offer Next Steps

Save as markdown. Offer:
- "Want me to **compare this against competitors** with a Value Curve?"
- "Should I **build a full strategy** around this value proposition?"
- "Want me to **create a Lean Canvas** or **Startup Canvas** using this?"
- "Should I **generate marketing messaging** from these value prop statements?"

## Notes

- This template starts with the customer (Who/Why) and works toward the solution — unlike Strategyzer's canvas which places the product on the left
- Each value proposition is segment-specific — different segments get different value props
- Use a Value Curve (Blue Ocean Strategy) to visually compare your offering against competitors across key factors
- Value Proposition is one element of product strategy — use `/strategy` for the full picture
