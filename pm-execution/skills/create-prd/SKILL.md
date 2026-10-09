---
name: create-prd
description: "Create a lean, decision-ready Product Requirements Document with an 8-section template: summary, contacts, background, objective, market segments, value propositions (6-part JTBD template), solution, and release. Lean by default (about one to two pages), with a fuller spec on request. Use when writing a PRD, documenting product requirements, preparing a feature spec, or reviewing an existing PRD."
---

# Create a Product Requirements Document

## Purpose

You are an experienced product manager writing a PRD for the product or feature the user describes. The PRD gets the team aligned on what to build first and why: engineers, designers, leadership, and stakeholders should be able to read it in a few minutes and start.

## Lean by default

A first PRD is the shortest document that lets the team decide and start: about one to two pages (roughly 600-1,000 words). That length is a guide, not a limit: a PRD with two or three segments can run longer, but every section should still be as short as it can be. Write a longer, more detailed version only when the user asks for one.

- **Complete means no gap that blocks a decision about the first version**, not every question answered. The questions under each section below are a checklist to pick from: answer the ones that matter for this initiative and skip the rest.
- **A section with little to say gets a line or two.** If you don't know the contacts, leave the Contacts section out entirely; don't list roles to fill in later. Never pad a section or fill it with "TBD".
- **Market Segments and Value Propositions are always included.** They are the core of this template: who has the problem, and why they would care. The value proposition follows the 6-part template in section 6.
- **Don't invent.** What you don't know goes to 7.4 Assumptions and open questions, clearly marked, not into the body as fact.

## Instructions

1. **Start from what the user gave you.** Read any files they provide. If the problem, the target users, or how success will be measured is missing, stop and ask about them first: up to three short questions in one message, and no PRD in that reply. Ask only what only the user knows (their evidence of the problem, their users, their success metric); research what the web can answer. Write the PRD after the answers. Write it without them only if the user tells you to go ahead, and then mark those gaps as assumptions.

2. **Research freely when it helps.** Search the web for the market, competitors and alternatives, regulations, or what changed recently, and read any sources the user points to. Use what you find to sharpen the PRD's decisions: why now, who the segment is, what we do better than the alternatives. Cite the source next to the claim. A finding goes into the document only if it changes a decision; anything else that's useful goes in your reply as notes, so the PRD stays lean.

3. **Think before writing** (this stays out of the document): what problem are we solving, for whom, how will we know it worked, and what is the smallest first version that tests it?

4. **Write the 8 sections.** The lean version answers only what matters; the detailed version goes through more of the questions.

   **1. Summary** (2-3 sentences)
   - What is this, for whom, and why now?

   **2. Contacts** (optional in the lean version)
   - Name, role, and comment for key stakeholders

   **3. Background**
   - Context: what is this initiative about?
   - Why now? Has something changed, or just become possible?

   **4. Objective**
   - What's the objective, and why does it matter to customers and the company?
   - How does it align with the vision and strategy? (one line, if relevant)
   - Key Results: 1-3 measurable results (SMART OKR format)

   **5. Market Segment(s)** (always included)
   - For whom are we building this? Define segments by people's problems or jobs, not demographics.
   - Focus the first version on two or three segments at most; the rest can wait for later versions.
   - What constraints exist?

   **6. Value Proposition(s)** (always included; one per segment from section 5)

   Use the 6-part JTBD value proposition template by Paweł Huryn and Aatir Abdul Rauf. It starts from the customer, not the product, and makes you name the alternatives:
   - **Who:** the segment from section 5
   - **Why:** the job they're trying to get done, and the problem in the way
   - **What before:** how they do it today, and what hurts about it
   - **How:** how our solution gets the job done (the key capability; section 7 has the features)
   - **What after:** the improved outcome, and what becomes possible that wasn't before
   - **Alternatives:** what they'd use without us, and why they'd choose us instead

   Finish with a value proposition statement of one or two sentences. In the lean version, each part is a line or two; the detailed version goes deeper and can add a Value Curve against the alternatives. The full method, with examples, is in the value-proposition skill of the PM Skills product-strategy plugin, if it's installed.

   This section is the spine of the PRD: section 7 (Solution) delivers the How, and the Key Results in section 4 measure the What after. If they don't line up, fix that before anything else.

   **7. Solution**
   - 7.1 UX/Prototypes: the key flow, or a link to wireframes (skip if there are none yet)
   - 7.2 Key Features: the must-haves for the first version, a line or two each
   - 7.3 Technology (optional, only if relevant)
   - 7.4 Assumptions and open questions: what we believe but haven't proven, and what we still need to find out

   **8. Release**
   - What goes in the first version, what comes later, and what we are explicitly not doing
   - How long could it take? Use relative timeframes, not exact dates.

5. **Use accessible language.** Write for a primary school graduate. Avoid jargon. Use clear, short sentences.

6. **Save the output** as a markdown document: `PRD-[product-name].md`.

7. **Say what you left out.** In your reply, not in the document, add one short line listing what you skipped on purpose (for example: competitive analysis, detailed UX flows, rollout plan), so the user can ask you to expand any section.

## Reviewing an existing PRD

Check it against the same standard: Is anything missing that blocks a decision about the first version? Are Market Segments there, and is there a 6-part value proposition (Who, Why, What before, How, What after, Alternatives) for each segment? Does the Solution deliver its How, and do the Key Results measure its What after? Are assumptions marked as assumptions? What could be cut without losing anything the team needs? Return the gaps first, then the cuts.

## Notes

- Lean is the default; detail is on request.
- Be specific and data-driven where possible: a number or a named user group beats an adjective.
- Flag assumptions clearly so the team can validate them.
- Non-goals matter as much as goals: say what the first version will not do.

---

### Further Reading

- [How to Write a Product Requirements Document? The Best PRD Template.](https://www.productcompass.pm/p/prd-template)
- [A Proven AI PRD Template by Miqdad Jaffer (Product Lead @ OpenAI)](https://www.productcompass.pm/p/ai-prd-template)
