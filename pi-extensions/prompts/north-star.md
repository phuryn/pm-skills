---
description: Define your North Star Metric and supporting input metrics — classify the business game and validate against best practices
argument-hint: "<product or business>"
---

You are executing the /north-star workflow: North Star Metric Definition.

Identify the single metric that best captures the value your product delivers, plus the input metrics that drive it. Classifies your business game and validates against proven criteria.

## Input

${ARGUMENTS:-No product was provided — ask the user what product or business the North Star framework is for.}

## Workflow

### Step 1: Understand the Product

Ask:
- What is the product? What value does it deliver to users?
- What's the business model? (subscription, transaction, advertising, marketplace)
- Current metrics being tracked (if any)
- Why is this needed now? (new product, existing metric feels wrong, team alignment)

### Step 2: Classify the Business Game

Apply the **north-star-metric** skill (installed in this environment — load its SKILL.md for the full framework):

Identify which game the product is playing:
- **Attention**: Revenue from user time/engagement (media, social, ad-supported)
- **Transaction**: Revenue from purchases (e-commerce, marketplace)
- **Productivity**: Revenue from efficiency gains (SaaS, tools, B2B)

The game determines what kind of North Star makes sense.

### Step 3: Define the North Star

- Propose 2-3 North Star candidates
- Validate each against 7 criteria:
  1. Expresses value delivered to customers
  2. Is a leading indicator of revenue
  3. Is measurable and trackable
  4. Is understandable by the whole team
  5. Is actionable (teams can influence it)
  6. Is not a vanity metric
  7. Is not gameable without delivering real value
- Recommend the strongest candidate with rationale

### Step 4: Define Input Metrics

For the selected North Star, identify 3-5 input metrics:
- Each input metric should be a lever that directly drives the North Star
- Each should be ownable by a specific team
- Together, inputs should be MECE in explaining North Star movement

### Step 5: Generate Metrics Framework

```
## North Star Framework: [Product]

**Business Game**: [Attention / Transaction / Productivity]

### North Star Metric
**Metric**: [precise name]
**Definition**: [formula or measurement method]
**Why this metric**: [explains value, leads revenue, is actionable]
**Current value**: [if known]
**Target**: [goal]

### Validation
| Criterion | Pass? | Notes |
|----------|-------|-------|
| Expresses value | [Y/N] | [explanation] |
| Leading indicator | [Y/N] | [explanation] |
| Measurable | [Y/N] | [explanation] |
| Understandable | [Y/N] | [explanation] |
| Actionable | [Y/N] | [explanation] |
| Not vanity | [Y/N] | [explanation] |
| Not gameable | [Y/N] | [explanation] |

### Input Metrics
| Input Metric | Drives North Star By | Owner | Current | Target |
|-------------|---------------------|-------|---------|--------|

### Metrics Constellation
[Visual tree showing North Star → Input Metrics → Team Actions]

### Counter-Metrics
| Metric | Protects Against |
|--------|-----------------|

### Anti-Patterns Avoided
[Why we didn't choose DAU, revenue, or other common but flawed metrics]
```

Save as markdown.

### Step 6: Offer Next Steps

- "Want me to **build a full metrics dashboard** around this?"
- "Should I **create OKRs** based on these metrics?"
- "Want me to **write SQL queries** to compute these metrics?"

## Notes

- The North Star should measure *value delivered*, not just *activity* — "daily active users" is only good if active use = value delivery
- Revenue is never a good North Star — it's a lagging indicator that doesn't capture user value
- Input metrics are what make the framework actionable — without them, the North Star is just a vanity dashboard
- Revisit the North Star annually or when the business model changes significantly
- Counter-metrics prevent Goodhart's Law — when a metric becomes a target, it ceases to be a good metric
