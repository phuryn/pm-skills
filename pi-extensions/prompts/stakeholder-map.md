---
description: Map stakeholders on a Power × Interest grid and create a tailored communication plan
argument-hint: "<project, initiative, or launch>"
---

You are executing the /stakeholder-map workflow: Stakeholder Mapping & Communication Plan.

Identify all stakeholders for a project, map them by influence and interest, and generate a communication plan that ensures the right people get the right information at the right time.

## Input

${ARGUMENTS:-No input was provided — ask the user for: <project, initiative, or launch>.}

## Workflow

### Step 1: Understand the Initiative

Ask:
- What is the project or initiative?
- What phase is it in? (planning, building, launching, post-launch)
- Who are the obvious stakeholders you already know about?
- Are there any politically sensitive dynamics to be aware of?

### Step 2: Identify Stakeholders

Brainstorm stakeholders the user might not have considered:
- **Internal**: Engineering, Design, QA, Data, Legal, Finance, Marketing, Sales, Support, Leadership
- **External**: Customers, partners, vendors, regulators, board members
- **Often missed**: Adjacent teams, on-call engineers, customer success, documentation team

### Step 3: Map to Power × Interest Grid

Apply the **stakeholder-map** skill:

Place each stakeholder in a quadrant:

```
                    HIGH INTEREST
                         │
    KEEP SATISFIED       │      MANAGE CLOSELY
    (High Power,         │      (High Power,
     Low Interest)       │       High Interest)
                         │
   ──────────────────────┼──────────────────────
                         │
    MONITOR              │      KEEP INFORMED
    (Low Power,          │      (Low Power,
     Low Interest)       │       High Interest)
                         │
                    LOW INTEREST
```

### Step 4: Generate Communication Plan

```
## Stakeholder Map: [Initiative]

### Stakeholder Grid
| Stakeholder | Role | Power | Interest | Quadrant | Stance |
|------------|------|-------|----------|----------|--------|

### Communication Plan

#### Manage Closely (High Power, High Interest)
| Stakeholder | Channel | Frequency | Content | Owner |
|------------|---------|-----------|---------|-------|

#### Keep Satisfied (High Power, Low Interest)
| Stakeholder | Channel | Frequency | Content | Owner |
|------------|---------|-----------|---------|-------|

#### Keep Informed (Low Power, High Interest)
| Stakeholder | Channel | Frequency | Content | Owner |
|------------|---------|-----------|---------|-------|

#### Monitor (Low Power, Low Interest)
[Minimal communication — include in broad updates only]

### Potential Conflicts
[Where stakeholder interests may clash — with mitigation strategies]

### Escalation Path
[Who to go to when decisions are blocked]

### RACI Matrix
| Decision Area | Responsible | Accountable | Consulted | Informed |
|--------------|-------------|-------------|-----------|----------|
```

Save as markdown.

### Step 5: Offer Next Steps

- "Want me to **draft the first stakeholder update** for the 'Manage Closely' group?"
- "Should I **create a meeting prep brief** for key stakeholder conversations?"
- "Want me to **set up a communication cadence** as a recurring checklist?"

## Notes

- The "Manage Closely" quadrant is where PMs spend most of their political capital — get these relationships right
- "Stance" (supportive, neutral, resistant) helps prioritize where to invest relationship-building effort
- Don't forget downstream stakeholders: support, docs, and sales enablement teams are often surprised by launches
- Update the map as the project evolves — stakeholder interest shifts with project phase
