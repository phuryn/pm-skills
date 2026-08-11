---
description: Generate realistic dummy datasets for testing — CSV, JSON, SQL inserts, or Python scripts
argument-hint: "<description of the data you need>"
---

You are executing the /generate-data workflow: Test Data Generator.

Create realistic dummy datasets for development, testing, demos, or prototyping. Outputs as ready-to-use files in your preferred format.

## Input

${ARGUMENTS:-No input was provided — ask the user for: <description of the data you need>.}

## Workflow

### Step 1: Define the Dataset

Understand:
- What entities? (users, orders, events, products, etc.)
- What columns? (with data types and constraints)
- How many rows?
- Any relationships between tables?
- Any specific distributions? (e.g., "80% should be on the free plan")
- Any realistic constraints? (emails should be unique, dates should be chronological)

### Step 2: Generate the Data

Apply the **dummy-dataset** skill:

- Create a Python script that generates the dataset
- Use realistic-looking data (not random strings): proper names, valid email formats, real-seeming dates
- Respect constraints: unique IDs, foreign key relationships, chronological ordering
- Apply specified distributions
- Execute the script and produce the output file

### Step 3: Deliver

Output in the requested format (or ask):
- **CSV**: Most common, works everywhere
- **JSON**: For API testing or frontend development
- **SQL INSERT**: For populating test databases
- **Python script**: For reproducible generation (user can tweak and re-run)

```
## Generated Dataset: [Description]

**Rows**: [count]
**Columns**: [list]
**Format**: [CSV / JSON / SQL / Python]

### Schema
| Column | Type | Constraints | Distribution |
|--------|------|-----------|-------------|

### Sample (first 5 rows)
[Preview of the data]

### Files
- [data file]
- [generator script, if applicable]
```

Save data file and generator script to the user's workspace.

### Step 4: Offer Follow-ups

- "Want me to **add more columns** or **increase the dataset size**?"
- "Should I **create related tables** (e.g., orders for these users)?"
- "Want me to **write test scenarios** that use this data?"
- "Should I **create SQL queries** to analyze this dataset?"

## Notes

- Always provide the generator script so the user can regenerate with different parameters
- For demo datasets, make the data tell a story (e.g., seasonal trends, a retention problem, a power user segment)
- Respect realistic cardinality: 1000 users don't have 1000 unique cities
- For financial data, use realistic price distributions — not uniform random
- Never include real personal data — all names, emails, and identifiers must be fake
