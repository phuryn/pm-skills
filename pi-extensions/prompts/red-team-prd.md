---
description: Red-team a PRD, roadmap, or strategy — attack its load-bearing assumptions and return the cheapest test for each before you commit
argument-hint: "<PRD, roadmap, strategy, or the current doc>"
---

You are executing the /red-team-prd workflow: Attack the Plan Before Reality Does.

Most plans only survived polite feedback. This command finds the assumptions that would make yours fail, attacks them honestly, and hands you the cheapest test for each — so you can kill a bad bet this week instead of at launch.

## Input

${ARGUMENTS:-No input was provided — ask the user for: <PRD, roadmap, strategy, or the current doc>.}

## Workflow

### Step 1: Accept the Plan

Take it in any form — PRD, roadmap, strategy memo, one-line bet, or an uploaded doc. If the user says "the current doc," use the document in context.

### Step 2: Red-Team It

Apply the **strategy-red-team** skill:

- Extract every claim; keep only the **load-bearing** ones (false → plan dies).
- **Steelman each, then attack the steelman** — no strawmen.
- Write each failure mode as "**Fails if ___**."
- Rank by **(impact if wrong) × (likelihood wrong) × (cheapness to test)**.
- Default "the risk is real" unless the plan cites evidence against it — but **say plainly what's well-reasoned**, and never fabricate a weakness.

### Step 3: Return the Output

```
## Red-Team: [plan in one line]

### Top Kill-Assumptions (ranked)
- **Claim:** [load-bearing assertion]
  - **Fails if:** [concrete, falsifiable]
  - **Evidence to get this week:** [specific]
  - **Kill criterion:** [threshold]
  - **Cheapest test:** [smallest experiment]
[3–5 max]

### What's Well-Reasoned
[State it explicitly — don't manufacture doubt.]

### What I Couldn't Assess
[Where the plan didn't give enough to judge.]
```

### Step 4: Offer Next Steps

- "Want me to **turn the top kill-assumption into an experiment** you can run this week?"
- "Should I **run a pre-mortem** to complement this — imagine it already failed and trace the path?"
- "Want me to **rewrite the riskiest section** of the plan to address what survived?"

## Notes

- Lead with the ranking — the cheapest high-impact test is the whole point.
- Five real kill-assumptions with tests beat twenty generic risks. Cut ruthlessly.
- Distinct from `/pre-mortem`: pre-mortem narrates failure after the fact; red-team attacks the live assumptions and hands you the test.
- If the plan is genuinely strong, the most valuable output is saying so — and naming the one thing still worth checking.
- For a second-opinion pass, ask the user before adding cross-model friction; different model families miss different things, but most plans don't need it.
