---
name: notion
description: "Orchestrate Notion page operations — read, create, update, section rewrites, table edits, search, and database ops. Routes across two MCP servers with automatic fallback chains, safety verification, and self-learning. Use whenever working with Notion pages."
---

## Notion Page Operations

Smart router for Notion across two MCP servers. Picks the right tool, handles failures, learns from mistakes.

### Context

You are performing Notion page operations for **$ARGUMENTS**.

Before any write operation, load the companion reference files in this directory:
- `notion-operations-guide.md` — Tool inventory, decision matrices, block estimation, known pitfalls (P1–P12)
- `notion-learnings.md` — Living knowledge base of discovered patterns, workarounds, and optimizations

### Instructions

**Safety Protocol — every write follows this. No exceptions.**

1. Read the page with `read_page` → store full content as `$BEFORE`
2. If `read_page` fails, fall back to alternate MCP's `fetch`
3. For destructive operations (`replace_content`, large section rewrites), confirm with the user first
4. After writing, read the page again → store as `$AFTER`
5. Verify: target content changed as intended, no unrelated content missing
6. If content was lost: IMMEDIATELY alert the user, display what was lost, offer to restore
7. When a primary tool fails and a fallback succeeds, append the failure pattern to the learnings file

**Tool selection decision tree:**

- Full page rewrite → `replace_content` (NEVER on pages with children) or create new page
- Section rewrite → `update_section` (falls back to heading-match trick on TypeError)
- Unique text in paragraph/heading/callout → `find_replace`
- Non-unique text → alternate MCP's `update_content` with surrounding context, or section rewrite
- Table cell edit → ALWAYS use section rewrite (find_replace fails silently on table cells)
- Large page create (>90 blocks) → `create_page` + `append_content` in chunks

**Critical rules:**
- NEVER use `replace_content` on pages with children — it archives all child pages
- `find_replace` only works on rich text blocks — paragraphs, headings, callouts, lists. Never on table cells.
- `append_content` on tables creates a NEW table, not a new row — rewrite the section instead
- Never use `|` inside table cell values — use `/` instead
- Em-dash `—` ≠ dash `-` — copy exact characters from read output
- After `update_section` TypeError, IMMEDIATELY re-read — it partially deletes content
- Maintain a local page ID index file for multi-page structures
- Batch updates: list_pages → restore missing → sample read → batches of 3-4 → verify

### Output

After completing the operation:
- Confirm what changed with a brief summary
- If any fallback was triggered, report which tool failed and which succeeded
- Offer relevant follow-up actions
