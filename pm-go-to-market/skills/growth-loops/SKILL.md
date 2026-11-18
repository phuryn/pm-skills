---
name: growth-loops
description: "Identify growth loops (flywheels) for sustainable traction. Evaluates 5 loop types: Viral, Usage, Collaboration, User-Generated, and Referral. Use when designing growth mechanisms, building product-led traction, or understanding how growth loops work."
---
# Growth Loops

Identify and design growth loops (flywheels) that create sustainable, product-led traction. Analyze the user's product against five proven loop types and deliver a ranked recommendation with implementation details.

## When to Use
- Designing growth mechanisms for a product
- Building sustainable viral or referral traction
- Reducing reliance on paid acquisition
- Analyzing competitor growth strategies
- Optimizing product for product-led growth

## The 5 Growth Loop Types

### 1. Viral Loop
Product content created by users gets shared on external platforms, bringing new users back to the product.
- **Mechanism**: Users create content in-product → Share on social/external platforms → New users discover and signup
- **Example**: Figma designs shared as links, Loom videos shared in emails
- **Strength**: Exponential user acquisition if content is inherently shareable
- **Challenge**: Requires highly shareable output and strong incentive to share

### 2. Usage Loop
Users create content or value within the product, then share it, which invites new users or drives re-engagement.
- **Mechanism**: User creates → Shares creation → Others consume → Become engaged users
- **Example**: Twitter threads, Medium articles, Notion templates shared publicly
- **Strength**: Growth tied directly to product usage and network effects
- **Challenge**: Requires content creation friction to be very low

### 3. Collaboration Loop
Users invite colleagues to co-create or collaborate within the product, expanding the user base within organizations.
- **Mechanism**: User creates → Invites colleagues for collaboration → Colleagues discover product value
- **Example**: Google Docs invitations, Figma team projects, Slack channels
- **Strength**: Deep organizational penetration and high retention
- **Challenge**: Works best for collaborative/team-based products

### 4. User-Generated Loop
Users discover new content or features through other users' creations, then create and share their own content.
- **Mechanism**: User discovers content → Creates similar content → Shares creation → Others discover
- **Example**: TikTok, Pinterest, YouTube trends driving creator participation
- **Strength**: Creates content flywheel and network effects
- **Challenge**: Requires critical mass of quality content to sustain

### 5. Referral Loop
Users invite other potential users in exchange for rewards, incentives, or social recognition.
- **Mechanism**: User refers → Referred user joins → Referrer gets reward → Shares more referrals
- **Example**: Dropbox referral bonus, Uber rider referrals, PayPal signup bonuses
- **Strength**: Directly incentivizes acquisition; easy to measure ROI
- **Challenge**: Requires valuable incentive without eroding unit economics

## Loop Selection Matrix

Score each factor 1-3 for the user's product to determine fit:

| Factor | Viral | Usage | Collab | UGC | Referral |
|--------|-------|-------|--------|-----|----------|
| Output is shareable outside product | 3 | 2 | 1 | 2 | 1 |
| Users create content as core action | 2 | 3 | 2 | 3 | 1 |
| Product improves with more team members | 1 | 1 | 3 | 1 | 1 |
| Users browse/discover others' work | 1 | 2 | 1 | 3 | 1 |
| Clear value moment in first session | 2 | 1 | 2 | 1 | 3 |

Highest-scoring loop = primary recommendation. Second-highest = secondary loop to layer later.

## How It Works

### Step 1: Gather Product Context
Extract from $ARGUMENTS:
- Core user action and value delivered
- Whether output is shareable or collaborative
- Existing network effects or sharing features
- Current acquisition channels and growth rate

### Step 2: Score Loop Fit
Apply the selection matrix above. Present results as a ranked table with scores out of 15 and fit assessment (Strong / Moderate / Weak).

### Step 3: Design the Primary Loop
For the top-scoring loop, specify:
1. **Trigger**: Exact user action that initiates the loop
2. **Share mechanism**: How value reaches new potential users
3. **Conversion hook**: What compels the new user to sign up
4. **Activation step**: First action that delivers value to the new user
5. **Re-engagement**: What brings the new user back to repeat the loop

### Step 4: Estimate Loop Coefficient
```
Loop Coefficient = (Actions per user per cycle)
                 x (Shares per action)
                 x (Conversion rate per share)

Example: 5 actions/week x 0.3 shares/action x 0.10 conversion = 0.15
```

- Coefficient > 1.0: Self-sustaining viral growth
- Coefficient 0.3-1.0: Meaningful growth amplifier
- Coefficient < 0.3: Supplement with other channels

### Step 5: Deliver Implementation Plan
Provide a 30-60-90 day roadmap:
- **Days 1-30**: Instrument baseline metrics, ship minimum loop mechanic
- **Days 31-60**: Optimize conversion at weakest step, A/B test share prompts
- **Days 61-90**: Layer secondary loop, set coefficient targets

## Output Format

Structure every response as:

1. **Product Summary**: One-sentence restatement of the product and core user action
2. **Loop Fit Scores**: Ranked table from Step 2
3. **Primary Loop Design**: Full loop specification from Step 3
4. **Loop Coefficient Estimate**: Calculation from Step 4 with assumptions stated
5. **Secondary Loop**: Brief design for the second-best loop to layer later
6. **Implementation Roadmap**: 30-60-90 plan from Step 5
7. **Key Metrics to Track**: 3-5 specific metrics with target ranges

## Example

**Input**: "B2B project management tool where teams create and assign tasks. Free tier available. 5,000 MAU."

**Output summary**:
- Loop Fit: Collaboration (13/15), Viral (8/15), Referral (8/15)
- Primary Loop: User creates project > Invites teammates > Teammates see value in shared board > Create their own projects > Invite their teams
- Coefficient: 3 projects/user/month x 2.5 invites/project x 0.25 conversion = 1.88
- Roadmap: Ship "invite to board" flow (Day 1-30), optimize invite email conversion (Day 31-60), add cross-org sharing for Viral loop (Day 61-90)

## Framework
Based on growth loops research by Ognjen Bošković. Focuses on compounding user acquisition through built-in, product-native sharing and collaboration mechanisms.

## Tips
- Master one loop before layering a second
- Collaboration loops drive the strongest retention and lifetime value
- Measure loop health weekly; a declining coefficient signals friction buildup
- Combine loops for multiplicative effect only after the primary loop exceeds 0.5 coefficient

---

### Further Reading

- [Product-Led Growth 101, Part 1/2](https://www.productcompass.pm/p/product-led-growth-101-12)
- [OpenAI's Product Leader Shares 3-Layer Distribution Framework To Win Mind & Market Share in the AI World](https://www.productcompass.pm/p/distribution-framework-ai-products)
- [How to Design a Value Proposition Customers Can't Resist?](https://www.productcompass.pm/p/how-to-design-value-proposition-template)
