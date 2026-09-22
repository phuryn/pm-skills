---
name: skill-navigation
description: "Help choose the right available PM skill or workflow from a plain-language situation. Use when someone asks which skill to use, does not know where to start with PM Skills, or wants help navigating the installed capabilities."
---

# PM Skill Navigation

Help someone who knows their situation but does not know the skill names. Recommend the smallest useful next step, explain why it fits, and help them start when they ask to proceed.

## 1. Understand the situation

Use the request, conversation, and supplied materials to identify:

- The decision or outcome the user needs now.
- Whether this concerns a new product or an existing product.
- What they already have: an idea, customer evidence, a plan, requirements, or results.
- Whether they want a recommendation or want the work performed.

Do not repeat questions already answered. When a missing fact would change the route, ask one focused question in everyday language and wait. Do not ask the user to pick a framework they came here to understand.

## 2. Check what is available

Use the current host's available skill and command descriptions as the candidate catalog. Identify relevant candidates from their names and descriptions before loading their full instructions.

- Plugins install independently. Recommend an exact invocation only when the current environment exposes it. Do not infer installation from the marketplace README or assume every plugin is present.
- On a skills-only host, recommend an available skill by its exposed name; do not invent slash-command support. If both a skill and a command are available, use the skill for a single analysis and the command when its workflow matches the requested sequence.
- If the host does not expose a catalog, use a user-provided installed list or ask which plugins are enabled. Do not search unrelated private files to reconstruct an installation.
- If nothing available fits, describe the needed capability in plain language and mark the availability gap. Do not pretend to call it or install anything automatically.
- Do not route back to this navigation skill. There is no mandatory dependency on another plugin and no fixed catalog to keep in sync.

## 3. Match the problem, not just a keyword

Use these intent distinctions to search the available descriptions. They are capability categories, not prerequisites or a sequence everyone must follow.

| Situation | Look for | Distinction to preserve |
|---|---|---|
| A direction, but no concrete product idea | Product ideation | New-product discovery differs from improving an existing product |
| An idea, but uncertainty about demand | Assumption mapping or experiment design | An experiment plan is not evidence that the idea works |
| Unclear customers or a pile of feedback | Segmentation, interview synthesis, or feedback analysis | Explore potential segments when there is no research; use supplied evidence when there is |
| A long list of requests | Request analysis or feature prioritization | Organize raw requests first; rank an already-organized list directly |
| An approved direction that needs documenting | Requirements or work-item writing | Reuse the decisions; do not restart ideation |
| A plan that needs challenging | Assumption review, strategic critique, or a pre-mortem | Choose based on whether the concern is the rationale or delivery risks |
| Unclear positioning, revenue, or price | Value proposition, monetization, or pricing analysis | Do not produce a full strategy canvas for a single pricing question |
| A market or competitor question | Competitive analysis or market sizing | Current factual claims need evidence |
| Falling retention, or an experiment result | Cohort or experiment analysis | Investigate supplied data before jumping to new features |
| A launch or growth problem | Launch planning, positioning, or growth analysis | Match the product's stage and the outcome requested |
| Iteration planning or success measures | Capacity planning, roadmaps, goals, or product metrics | Distinguish a delivery schedule from a business outcome |
| An AI-built app ready for review | Documentation, intended-behavior review, or shipping readiness | A routing recommendation is not a readiness verdict |
| A PM document or career task | Writing review, document drafting, or resume help | Honor the requested artifact rather than expanding into product discovery |

## 4. Give a usable recommendation

Lead with one recommendation. Add at most one alternative when a meaningful unresolved condition changes the choice. Avoid dumping the catalog.

Include:

- **Start with:** the verified available skill or workflow name.
- **Why:** how it fits the user's situation.
- **What you get:** the expected output and any essential input still needed.
- **Try this:** a short prompt carrying the user's context; use exact command syntax only if verified available on this host.

For example, if a user has interview transcripts, explain why synthesizing that evidence is the next step and what insights it will produce. If they have an agreed scope and need a requirements document, recommend documenting that scope directly. Neither case needs a tour of the whole lifecycle.

If the user only asked which skill to choose, stop after the recommendation. Do not create project files, conduct interviews, or run a whole workflow on the strength of that question.

## 5. Hand off when execution is requested

Read the selected capability's full instructions and follow them using the user's goal, materials, decisions, assumptions, and unresolved questions. Selecting a skill does not mean it has already been run. Preserve existing approvals, and satisfy any additional requirements of the selected workflow without expanding the user's request.

For a broad request, suggest a short conditional path in everyday language, such as “generate options, choose one, then test its riskiest assumption.” Resolve each subsequent capability against what is actually available when it is needed. Do not hard-code commands from other plugins or treat a suggested path as permission for external writes, purchases, or implementation.

After each step, reassess whether the requested outcome is met. Carry forward the findings instead of starting another interview from scratch. If a required capability or input is missing, name the gap and the next useful action; do not claim the full workflow is complete.
