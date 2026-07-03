---
description: Orchestrate Notion page operations — read, create, update, section rewrites, table edits, search, and database ops with automatic fallback chains and safety verification
argument-hint: "[read|create|update|section|table|search|db|learn|diagnose] <page URL, ID, or title>"
---

# /notion — Notion Page Operations

Smart router for Notion across two MCP servers. Picks the right tool, handles failures, learns from mistakes.

## Invocation

```
/notion read <page URL or ID>
/notion create <parent URL or ID> <title> [content source]
/notion update <page URL or ID> <what to change>
/notion section <page URL or ID> <heading name> [new content or instructions]
/notion table <page URL or ID> <what to change in the table>
/notion search <query>
/notion db [query|add|update|schema] <database URL or ID> [details]
/notion learn "<finding description>"
/notion diagnose
/notion <page URL or ID>          # interactive — asks what to do
/notion                            # interactive — asks for page and operation
```

---

## Companion Files

This skill works with two companion reference files located in `skills/notion/`:

- **`notion-operations-guide.md`** — Tool inventory, decision matrices, block estimation, known pitfalls (P1–P12)
- **`notion-learnings.md`** — Living knowledge base of discovered patterns, workarounds, and optimizations

Load these before any write operation. They contain the full tool inventory, pitfall catalog, and accumulated workarounds.

---

## Safety Protocol

**Every write operation follows this protocol. No exceptions.**

### Before Writing
1. Read the page with `read_page` → store full content as `$BEFORE`
2. If `read_page` fails, fall back to alternate MCP's `fetch`
3. For destructive operations (`replace_content`, large section rewrites), confirm with the user first

### After Writing
4. Read the page again → store as `$AFTER`
5. Verify: target content changed as intended
6. Check: no unrelated content missing (compare `$BEFORE` and `$AFTER`)
7. If content was lost: IMMEDIATELY alert the user, display what was lost, offer to restore

### On Failure — Auto-Learn
8. When a primary tool fails and a fallback succeeds, append the failure pattern to the learnings file

---

## Mode: read

**Purpose:** Read and display a Notion page's content.

1. Extract page URL or ID from arguments
2. **Primary:** `read_page` — returns full markdown, no truncation
3. **Fallback:** Alternate MCP `fetch` — may truncate large pages (~54KB); warn user
4. Display the content to the user

---

## Mode: create

**Purpose:** Create a new Notion page with automatic chunking for large content.

1. Gather: parent page (URL/ID), title, content (from user, local file, or conversation)
2. **Never push partial content.** Always push the complete document.

3. **Estimate block count:**
   - Count: paragraphs, headings, list items (1 each), table rows (1 each), code blocks (1), dividers (1)
   - Tables are deceptive: a 10-column, 20-row table = 21 blocks (header + 20 rows)

4. **If estimated blocks ≤ 90:**
   - `create_page(parent_page_id, title, markdown)`

5. **If estimated blocks > 90:**
   - Split content at a natural heading boundary near block 80-90
   - `create_page(parent_page_id, title, first_chunk)`
   - `append_content(new_page_id, next_chunk)` — repeat for each remaining chunk
   - Each append chunk should also stay under 90 blocks

6. **Verify:** Read the created page back. Confirm key sections exist and content is complete.

---

## Mode: update

**Purpose:** Smart-routed targeted edit. Picks the best tool based on the edit type.

### Step 1: Read the page (Safety Protocol)

### Step 2: Classify the edit

- **Full page rewrite?** → Confirm with user, then use `replace_content` or create a new page
- **Section rewrite?** → Redirect to **section** mode
- **Table edit?** → Redirect to **table** mode
- **Targeted text edit?** → Continue to Step 3

### Step 3: Check text uniqueness

Search `$BEFORE` content for the target text.

**Case A — Text is globally unique (1 match):**
```
USE: find_replace(page_id, old_text, new_text)
```

**Case B — Text appears multiple times, ALL should change:**
```
USE: find_replace(page_id, old_text, new_text, replace_all=true)
```

**Case C — Text appears multiple times, only SOME should change:**
```
WARNING: find_replace cannot target specific instances.
Option 1: Add surrounding context to make old_str unique via alternate MCP's update_content
Option 2: Use section mode to rewrite the enclosing section
```

**Case D — "No matches found" error:**
```
CHECK: em-dash (—) vs dash (-), backtick formatting, extra whitespace
RETRY with corrected text
FALLBACK: Use alternate MCP's update_content
```

---

## Mode: section

**Purpose:** Rewrite an entire section identified by heading name.

1. Read the page (Safety Protocol)
2. Identify the exact heading name — must match what `read_page` returns
3. Prepare the complete new section content

4. **Primary:** `update_section(page_id, heading, new_content)`

5. **On TypeError ("Cannot read properties of undefined"):**
   - **IMMEDIATELY** re-read the page — `update_section` may have partially deleted content
   - Compare with `$BEFORE` to identify what was lost
   - **Fallback — Heading-Match Trick:**
     Find the NEXT heading after the target section. Match it via alternate MCP's `update_content`, prepend your new content + the original heading.

6. **On "Heading not found" error:**
   - Heading text must match EXACTLY (case-insensitive, but full text including parentheticals)
   - Some headings may not exist as proper heading blocks (bold text or paragraphs)

7. Verify (Safety Protocol)

---

## Mode: table

**Purpose:** Table-specific operations — the hardest case in Notion.

**Critical:** Notion stores table cells as separate blocks. Markdown `| row |` notation is a read-time representation — it cannot be matched by any find/replace tool.

### Decision Tree

**Edit a cell with UNIQUE content:**
```
USE: find_replace(page_id, "cell text without pipes", "new cell text")
NOTE: This may still fail on table cells — verify after writing
```

**Edit a cell with NON-UNIQUE content:**
```
Must rewrite the entire table.
1. Find the heading above the table
2. Use section mode to rewrite that heading's content (including the full corrected table)
```

**Add a new row:**
```
WARNING: append_content creates a NEW table, not an additional row.
Use section mode to rewrite the section containing the table with the new row included.
```

**Add/remove columns or restructure:**
```
Use section mode to rewrite the entire table section with the new structure
```

### Formatting Rules
- **Never use `|` inside cell values** — use `/` instead (e.g., `option_a / option_b`)
- **Em-dash `—` ≠ dash `-`** — copy exact character from read output
- **Block count:** Each table row ≈ 1 block. A 20-row table ≈ 21 blocks

---

## Mode: search

**Purpose:** Find Notion pages or databases.

1. **Primary:** `search(query)` — simple text search
2. **For advanced filters:** Alternate MCP search — supports date ranges, created_by, type filters
3. Display results with titles, URLs, and last edited dates

---

## Mode: db

**Purpose:** Database operations — query, add entries, update entries, manage schema.

**Query:** `get_database(db_id)` first for schema, then `query_database(db_id, filter, sort)`

**Add entry:** `add_database_entry(db_id, properties)` — bulk: `add_database_entries(db_id, entries[])`

**Update entry:** `update_database_entry(entry_id, properties)`

**Schema changes:** Alternate MCP's `update-data-source` — add, rename, drop columns

**View management:** Alternate MCP's `create-view` / `update-view` (table, board, calendar, etc.)

---

## Mode: learn

**Purpose:** Append a new discovery to the living knowledge base.

1. Read the learnings file
2. Determine category: `pitfall`, `workaround`, `new-tool`, `behavior-change`, `optimization`
3. Append a new entry with date, category, description, workaround, applicable tools
4. Write the updated file

If the file exceeds 200 lines, suggest consolidating duplicate entries (but never auto-delete).

---

## Mode: diagnose

**Purpose:** Check which Notion MCPs are connected and what tools are available.

1. Probe primary MCP — try a search call
2. Probe alternate MCP — try a search call
3. Report status: CONNECTED / DISCONNECTED for each
4. If UUID prefix changed, log the new prefix

---

## Fallback Chain Summary

| Operation | Primary | Fallback 1 | Fallback 2 |
|-----------|---------|------------|------------|
| Read | `read_page` | Alt `fetch` | — |
| Create | `create_page` + `append` | Alt `create-pages` | — |
| Unique text edit | `find_replace` | Alt `update_content` | Section rewrite |
| Non-unique edit | Alt `update_content` | Section rewrite | Full replace |
| Section rewrite | `update_section` | Heading-match trick | Full replace |
| Table cell (unique) | `find_replace` | Section rewrite | — |
| Table cell (non-unique) | Section rewrite | — | — |
| Search | `search` | Alt `search` | — |
| DB schema | Alt `update-data-source` | — | — |

## Notes

- The Heading-Match Trick: match a heading as `old_str`, replace with `[new content]\n### Heading Name` to insert content before it
- `update_section` TypeError is page-specific — triggered by deep nesting, not raw block count. Try it first, fall back on error
- `append_content` on tables creates a new table, not a new row — always rewrite the section instead
- `find_replace` fails on table cells even for unique text — only reliable on paragraphs, headings, callouts, lists
- Always maintain a local page ID index file for multi-page Notion structures
