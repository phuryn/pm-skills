# pm-toolkit

PM utility skills: skill navigation, resume review, NDA drafting, privacy policy generation, and grammar/flow checking. Essential tools for product managers beyond core product work.

## Skills (5)

- **skill-navigation** — Choose the right available PM skill or workflow from a plain-language situation, with a recommendation, rationale, and next prompt.
- **draft-nda** — Draft a detailed Non-Disclosure Agreement between two parties.
- **grammar-check** — Identify grammar, logical, and flow errors in text and suggest targeted fixes without rewriting the entire text.
- **privacy-policy** — Draft a detailed privacy policy for a product covering data types, jurisdiction, compliance considerations, and clauses needing legal review.
- **review-resume** — Comprehensive PM resume review and tailoring against 10 best practices including XYZ+S formula, keyword optimization, job-specific tailoring, and structure.

## Commands (6)

- `/pm-toolkit:ask-pm` — Describe your situation to find the right available skill or workflow; ask it to proceed when you want the work performed.
- `/pm-toolkit:draft-nda` — Draft a Non-Disclosure Agreement between two parties with jurisdiction-appropriate clauses.
- `/pm-toolkit:privacy-policy` — Draft a privacy policy covering data collection, usage, storage, and compliance requirements.
- `/pm-toolkit:proofread` — Check grammar, logic, and flow in any text — targeted fixes without rewriting.
- `/pm-toolkit:review-resume` — Comprehensive PM resume review against 10 best practices — structure, impact metrics, keywords, and actionable feedback.
- `/pm-toolkit:tailor-resume` — Tailor a PM resume to a specific job description — keyword alignment, experience reframing, and strategic optimization.

## Not sure where to start?

With this plugin installed in Claude Code or Cowork, try:

```
/pm-toolkit:ask-pm I know the product direction but not what to build first
/pm-toolkit:ask-pm We already agreed on scope; which workflow helps write it down?
```

On a skills-only host, ask: "Use the skill-navigation skill to help me choose the right PM skill for this situation: ..."

The navigator checks capabilities available in your session, so it works with partial plugin installations. It recommends one next step and explains the expected output. If a capability is unavailable, it says so. Asking for advice alone does not start the work; include "then help me do it" to request a handoff.

## Author

Paweł Huryn — [The Product Compass Newsletter](https://www.productcompass.pm)

## License

MIT
