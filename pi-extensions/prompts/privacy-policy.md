---
description: Draft a privacy policy covering data collection, usage, storage, and compliance requirements
argument-hint: "<product and data handling context>"
---

You are executing the /privacy-policy workflow: Privacy Policy Generator.

Draft a comprehensive privacy policy for your product. Covers data types, jurisdiction, compliance (GDPR, CCPA), and marks clauses needing legal review.

## Input

${ARGUMENTS:-No input was provided — ask the user for: <product and data handling context>.}

## Workflow

### Step 1: Gather Context

Ask:
- What product or service?
- What data is collected? (personal info, usage data, cookies, location, payment)
- Where are your users? (determines applicable regulations: GDPR, CCPA, etc.)
- Any third-party data sharing? (analytics, advertising, integrations)
- Data storage: where and how long?
- Age restrictions? (COPPA considerations)

### Step 2: Draft the Policy

Apply the **privacy-policy** skill:

Generate sections covering:
- What data is collected and how
- How data is used (purposes)
- Legal basis for processing (GDPR)
- Data sharing and third parties
- Data retention and deletion
- User rights (access, deletion, portability, opt-out)
- Cookie policy
- Security measures
- Children's privacy (if applicable)
- International transfers
- Contact information
- Policy update process

### Step 3: Deliver

```
## Privacy Policy: [Product]

[Full policy text]

### Compliance Checklist
| Regulation | Status | Notes |
|-----------|--------|-------|

### Clauses Requiring Legal Review
| Clause | Why | Priority |
|--------|-----|----------|

### Implementation Checklist
- [ ] Cookie consent banner
- [ ] Data subject request process
- [ ] Data processing records
- [ ] DPA with processors
```

Save as markdown. Offer DOCX export.

## Notes

- This is a template — legal counsel should review before publishing
- GDPR and CCPA have specific requirements that can't be approximated — flag where expert review is essential
- Privacy policies should be in plain language, not legalese
- Update the policy when data practices change, not just annually
