---
description: Run a pre-mortem risk analysis on a PRD, launch plan, or feature — identify what could go wrong before it does
argument-hint: "<PRD, plan, or feature description>"
---

You are executing the /pre-mortem workflow: Pre-Launch Risk Analysis.

Imagine your launch has failed. Now work backward to figure out why. This workflow applies the Tigers/Paper Tigers/Elephants framework to surface real risks and create mitigation plans.

## Input

${ARGUMENTS:-No plan was provided — ask the user for the PRD, feature spec, launch plan, or project brief to analyze.}

## Workflow

### Step 1: Accept the Plan

Accept in any format: PRD, feature spec, launch plan, project brief, or verbal description. The more detail provided, the sharper the risk analysis. If the user referenced a file, read it.

### Step 2: Risk Identification

Apply the **pre-mortem** skill (installed in this environment — load its SKILL.md for the full framework):

Imagine the product has launched and failed. Generate risks across categories:
- **Technical**: Performance, scalability, integration failures, data issues
- **User**: Adoption barriers, usability problems, unmet expectations
- **Business**: Revenue impact, competitive response, market timing
- **Operational**: Support load, documentation gaps, training needs
- **Dependencies**: Third-party services, cross-team handoffs, regulatory

### Step 3: Classify Risks

Categorize each risk:

**Tigers** — Real, substantive risks that could cause failure
- Assess severity: Launch-blocking / Fast-follow / Track
- For launch-blocking Tigers: immediate mitigation required
- For fast-follow Tigers: plan to address within first sprint post-launch
- For track Tigers: monitor but don't delay launch

**Paper Tigers** — Risks that feel scary but are overblown
- Explain why the concern is manageable
- Note what would need to change for this to become a real Tiger

**Elephants** — Unspoken risks the team knows about but avoids discussing
- Surface political, organizational, or uncomfortable risks
- Frame constructively with suggested conversation starters

### Step 4: Generate Pre-Mortem Report

```
## Pre-Mortem: [Feature/Launch]

**Date**: [today]
**Status**: [Draft / Reviewed]

### Risk Summary
- **Tigers**: [count] ([launch-blocking], [fast-follow], [track])
- **Paper Tigers**: [count]
- **Elephants**: [count]

### Launch-Blocking Tigers
| # | Risk | Likelihood | Impact | Mitigation | Owner | Deadline |
|---|------|-----------|--------|-----------|-------|----------|

### Fast-Follow Tigers
| # | Risk | Likelihood | Impact | Planned Response | Owner |
|---|------|-----------|--------|-----------------|-------|

### Track Tigers
[Risks to monitor post-launch with trigger conditions]

### Paper Tigers
[Concerns that seem big but are manageable — with reasoning]

### Elephants in the Room
[Uncomfortable truths the team should discuss]

### Go/No-Go Checklist
- [ ] All launch-blocking Tigers mitigated
- [ ] Fast-follow plan documented and assigned
- [ ] Monitoring in place for Track Tigers
- [ ] Rollback plan defined
- [ ] Support team briefed
```

Save as markdown.

### Step 5: Offer Next Steps

- "Want me to **update the PRD** with risk mitigations?"
- "Should I **create test scenarios** for the riskiest areas?"
- "Want me to **draft a launch checklist** from these findings?"

## Notes

- The best pre-mortems happen when the plan is 80% done — early enough to change course, late enough to have substance
- Push past the obvious risks — the most dangerous risks are the ones nobody mentions
- Elephants are the highest-value output — surfacing what the team avoids discussing
- For each Tiger, the mitigation should be specific and assignable, not "be careful"
- If the pre-mortem reveals too many launch-blocking Tigers, recommend delaying or phasing the launch
