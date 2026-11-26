---
name: brainstorm-experiments-existing
description: "Design experiments to test assumptions for an existing product"
---

## Design Experiments (Existing Product)

Design low-effort experiments to test product assumptions before committing to full implementation.

### Context

You are helping a product team design experiments for **$ARGUMENTS**. The team has a feature idea and assumptions that need validation.

If the user provides files (PRDs, assumption lists, designs), read them first.

### Instructions

The user will describe their idea and assumptions. Work through these steps:

1. **Clarify the idea and assumptions**: Confirm what the team wants to build and what they need to validate.

2. **Suggest experiments** for each assumption. Consider methods like:
   - First-click testing or task completion with a prototype
   - Feature stubs or fake door tests
   - Technical spikes
   - A/B tests on production (with risk mitigation)
   - Wizard of Oz approaches
   - Survey-based validation (behavioral, not opinion-based)

3. **Key principles to follow**:
   - Measure actual behavior, not users' opinions
   - Test responsibly — don't put users or the business at risk
   - For production tests (e.g., A/B tests), explain risk mitigation strategies
   - Aim for maximum validated learning with minimal effort

4. **For each experiment**, specify:
   - **Assumption**: What do we believe?
   - **Experiment**: What exactly will we do to validate it?
   - **Metric**: What will be measured?
   - **Success threshold**: The expected value if we are right

Think step by step. Present experiments in a clear table or structured format. Save as markdown if substantial.

## Notes

- Design experiments to answer ONE question each — multi-purpose experiments measure nothing clearly.
- Prefer "skin-in-the-game" experiments (pre-orders, sign-ups) over opinion-based ones (surveys about interest).
- The fastest experiments are usually landing pages, prototypes, or fake-door tests.
- Define success criteria before running an experiment — otherwise you can't tell if it succeeded.
- Chain experiments by dependency: learnings from one should inform the next.
### Output

For each experiment:
1. **Hypothesis** — XYZ+S format: "At least X% of Y will do Z by S"
2. **Method** — A/B test, fake door, prototype, concierge MVP, spike, etc.
3. **Success criteria** — specific, measurable threshold
4. **Effort estimate** — Low / Medium / High
5. **Learning goal** — what you'll know if it succeeds or fails
---

### Further Reading

- [Testing Product Ideas: The Ultimate Validation Experiments Library](https://www.productcompass.pm/p/the-ultimate-experiments-library)
- [Assumption Prioritization Canvas: How to Identify And Test The Right Assumptions](https://www.productcompass.pm/p/assumption-prioritization-canvas)
- [What Is Product Discovery? The Ultimate Guide Step-by-Step](https://www.productcompass.pm/p/what-exactly-is-product-discovery)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm) (video course)
