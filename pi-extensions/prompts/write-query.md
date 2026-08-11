---
description: Generate SQL queries from natural language — supports BigQuery, PostgreSQL, MySQL, and more
argument-hint: "<what you want to know, in plain English>"
---

You are executing the /write-query workflow: SQL Query Generator.

Describe what data you need in plain English and get an optimized SQL query. Supports multiple dialects and can read a schema from files the user references.

## Input

${ARGUMENTS:-No request was provided — ask the user what data they need in plain English.}

## Workflow

### Step 1: Understand the Question

Parse the user's natural language request to identify:
- What data is being requested (metrics, dimensions, filters)
- Time range and granularity
- Grouping and ordering preferences
- Output expectations (raw data, aggregated, ranked)

### Step 2: Determine Schema

If a schema is available (uploaded diagram, DDL, description, or a file the user references — read it):
- Map the request to specific tables and columns
- Identify necessary joins

If no schema is provided:
- Ask for the database type (BigQuery, PostgreSQL, MySQL, etc.)
- Infer a reasonable schema from the question and ask the user to confirm
- Use common SaaS data model conventions as defaults

### Step 3: Generate Query

Apply the **sql-queries** skill (installed in this environment — load its SKILL.md for the full framework):

- Write the SQL query in the correct dialect
- Optimize for readability and performance
- Include comments explaining key logic
- Add CTEs for complex queries to improve readability
- Handle edge cases (NULLs, timezone considerations, duplicate handling)

### Step 4: Present and Iterate

```
## SQL Query: [What It Does]

**Dialect**: [BigQuery / PostgreSQL / MySQL / etc.]
**Tables used**: [list]

### Query
[SQL code block with comments]

### What This Returns
[Description of the output: columns, rows, expected result shape]

### Assumptions
- [Schema assumptions made]
- [Business logic assumptions]

### Notes
- [Performance considerations for large datasets]
- [Edge cases handled or flagged]
```

Offer:
- "Want me to **modify this** — add filters, change grouping, extend the time range?"
- "Should I **create a companion query** for a related metric?"
- "Want me to **build a dashboard** around this query?"
- "Need a **cohort analysis** version of this?"

## Notes

- Always include comments in the SQL — PMs share queries with analysts who need to understand intent
- Default to readable over clever — CTEs over nested subqueries
- Flag queries that might be slow on large datasets and suggest optimization
- If the request is ambiguous (e.g., "active users"), ask the user to define the metric precisely
- Offer to generate the query in multiple dialects if the user is unsure which database they're using
