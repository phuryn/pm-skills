---
description: Design a pricing strategy — models, competitive analysis, willingness-to-pay estimation, and pricing experiments
argument-hint: "<product or pricing question>"
---

You are executing the /pricing workflow: Pricing Strategy Design.

Build a pricing strategy from first principles: analyze pricing models, estimate willingness to pay, benchmark against competitors, and design pricing experiments.

## Input

${ARGUMENTS:-No input was provided — ask the user for: <product or pricing question>.}

## Workflow

### Step 1: Understand the Pricing Context

Ask:
- What is the product? What value does it deliver?
- Current pricing (if any): model, price points, packaging
- What's the trigger? (new product, pricing change, competitive pressure, growth stall)
- Target customer profile and their budget context
- Any constraints? (contractual obligations, market expectations, competitive positioning)

### Step 2: Analyze Pricing Models

Apply the **pricing-strategy** and **monetization-strategy** skills:

Evaluate applicable models:
- **Flat-rate**: Simple, predictable — best for commoditized products
- **Per-seat/user**: Scales with adoption — best for collaboration tools
- **Usage-based**: Aligns cost with value — best for infrastructure and API products
- **Tiered**: Captures different willingness to pay — best for segmented markets
- **Freemium**: Drives adoption — best for products with network effects
- **Hybrid**: Combines models — best for complex products with multiple value levers

For each relevant model: pros, cons, fit for your product, revenue projection approach.

### Step 3: Competitive Pricing Analysis

Using web research:
- Benchmark pricing against 3-5 competitors
- Identify pricing model patterns in the category
- Note pricing trends (e.g., shift from per-seat to usage-based in B2B SaaS)
- Find pricing page screenshots and data points

### Step 4: Willingness to Pay Estimation

If the user has survey data or customer feedback:
- Apply Van Westendorp analysis (if data available)
- Segment willingness to pay by user type

If no data:
- Estimate based on value delivered, competitive anchoring, and market norms
- Design a willingness-to-pay survey the user can run

### Step 5: Generate Pricing Recommendation

```
## Pricing Strategy: [Product]

**Date**: [today]
**Current pricing**: [if applicable]

### Recommended Model: [Model Name]

**Why this model**: [rationale tied to product value delivery]

### Pricing Structure
| Tier | Price | Includes | Target Segment | Key Limit |
|------|-------|---------|---------------|-----------|

### Free / Trial Strategy
[What's free, what's gated, conversion triggers]

### Competitive Benchmark
| Competitor | Model | Price Range | Positioning |
|-----------|-------|-----------|------------|

### Revenue Projections
| Scenario | Assumptions | Year 1 ARR | Year 2 ARR |
|----------|-----------|-----------|-----------|
| Conservative | [X] | [Y] | [Z] |
| Expected | [X] | [Y] | [Z] |
| Optimistic | [X] | [Y] | [Z] |

### Migration Plan
[If changing pricing: how to transition existing customers]
- Grandfathering approach
- Communication plan
- Timeline

### Pricing Experiments
| Experiment | What We're Testing | Method | Duration |
|-----------|-------------------|--------|----------|

### Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|

### Key Metrics to Track
- Conversion rate by tier
- Average revenue per user (ARPU)
- Upgrade/downgrade rates
- Churn by price sensitivity
- Price elasticity signals
```

Save as markdown.

### Step 6: Offer Next Steps

- "Want me to **create a monetization strategy** with alternative revenue models?"
- "Should I **run a market scan** to validate pricing assumptions?"
- "Want me to **draft customer communication** for the pricing change?"
- "Should I **design the A/B test** for pricing experiments?"

## Notes

- Pricing is the most powerful lever for revenue growth — a 1% improvement in pricing typically has 3-4x the impact of 1% improvement in customer acquisition
- Value-based pricing always beats cost-plus — start from customer value, not your costs
- The best pricing is simple to understand and predictable for the customer
- Freemium only works if free users generate value (network effects, word of mouth, marketplace liquidity)
- Always design a migration path for existing customers — pricing changes that alienate your base destroy trust
