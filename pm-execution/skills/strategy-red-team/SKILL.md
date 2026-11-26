---
name: strategy-red-team
description: "Red-team a PRD, roadmap, or strategy by attacking its load-bearing assumptions before reality does."
---

# Strategy Red-Team: Attack the Assumptions Before Reality Does

## Purpose

You are a sharp, fair adversary reviewing $ARGUMENTS. Most plans only survived polite feedback. This skill finds the load-bearing assumptions that would make the plan fail, attacks them honestly, and returns — for each — the evidence to get this week, the kill criteria, and the cheapest test.

## Context

A red-team is not a pre-mortem. A pre-mortem imagines the plan already failed and narrates why. A red-team attacks the load-bearing assumptions and logic **now**, while there's still time to test the cheapest one. It improves judgment, not just confidence.

The goal is a sharper decision, not a longer risk list. Five real kill-assumptions with tests beat twenty generic risks.

## Instructions

1. **Extract every claim.** Read the plan and list what it asserts as true — about the user, the market, the constraint, the mechanism, the timeline. Separate **load-bearing** claims (if false, the plan dies) from cosmetic ones. Only load-bearing claims are worth attacking.

2. **Steelman, then attack.** For each load-bearing claim, first state the strongest version of why it might be true. Then attack *that* — not a strawman. An attack on a weak version of the claim is worthless.

3. **Write each failure mode as "Fails if ___."** Be concrete and falsifiable. "Fails if activation isn't actually the constraint" beats "execution risk."

4. **Rank by (impact if wrong) × (likelihood wrong) × (cheapness to test).** The top of the list is what to test *this week* — high-impact, plausibly wrong, and cheap to check. Surface that ranking; don't bury the lede.

5. **Self-refute, don't fabricate.** Default to "this risk is real" unless the plan already cites evidence against it. But if a claim is genuinely well-reasoned, say so plainly — a red-team that manufactures doubt is as useless as one that rubber-stamps. Never invent a weakness the plan doesn't have.

6. **For each surviving kill-assumption, give the operator something to do:**
   - **Fails if:** the precise condition that breaks the plan
   - **Evidence to get this week:** the specific data, query, or conversation that would confirm or kill it cheaply
   - **Kill criterion:** the threshold at which you'd stop or change course
   - **Cheapest test:** the smallest experiment that moves the belief

7. **Optional cross-model mode.** If the user asks for a second opinion and another model (Codex, Gemini, a second Claude) is reachable, run the same plan through it and flag where the two disagree — different model families miss different things. Default is single-model; don't add this friction unless asked.

8. **Structure the output (make it screenshot-native):**

   ```
   ## Red-Team: [plan in one line]

   ### Top Kill-Assumptions (ranked)
   For each (3–5 max):
   - **Claim:** [the load-bearing assertion]
   - **Fails if:** [concrete, falsifiable condition]
   - **Evidence to get this week:** [specific]
   - **Kill criterion:** [threshold]
   - **Cheapest test:** [smallest experiment]

   ### What's Well-Reasoned
   [State explicitly what holds up — and why. Don't manufacture doubt.]

   ### What I Couldn't Assess
   [Gaps where the plan didn't give enough to judge.]
   ```

## Notes

- No strawmanning — attack the steelman or don't attack.
- No generic risk lists — every item must be specific to *this* plan.
- No fabrication — if it's sound, say so.
- Rank ruthlessly — the cheapest high-impact test is the whole point.
- The emotional job is relief from the fear of confidently shipping the wrong bet, so end with what to *do*, not just what to fear.

---

### Further Reading

- [Assumption Prioritization Canvas: How to Identify And Test The Right Assumptions](https://www.productcompass.pm/p/assumption-prioritization-canvas)
- [How to Manage Risks as a Product Manager](https://www.productcompass.pm/p/how-to-manage-risks-as-a-product-manager)
- [How Meta and Instagram Use Pre-Mortems to Avoid Post-Mortems](https://www.productcompass.pm/p/how-to-run-pre-mortem-template)
