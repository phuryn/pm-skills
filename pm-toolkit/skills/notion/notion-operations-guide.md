# Notion Operations Guide

Quick-reference for tool selection, known pitfalls, and workarounds. Loaded by `/notion` skill during write operations.

---

## 1. Tool Inventory

### Primary MCP: `mcp__notion__*`

| Tool | Purpose |
|------|---------|
| `read_page` | Read full page as markdown (no truncation) |
| `create_page` | Create page from markdown (100-block limit) |
| `append_content` | Append markdown to existing page |
| `find_replace` | Find/replace text (requires globally unique match) |
| `update_section` | Replace section by heading name |
| `replace_content` | Replace entire page content |
| `update_page` | Update title, icon, or cover |
| `search` | Search pages and databases |
| `list_pages` | List child pages under parent |
| `duplicate_page` | Duplicate a page |
| `archive_page` / `restore_page` | Archive or restore |
| `move_page` | Move page to new parent |
| `share_page` | Get shareable URL |
| `add_comment` / `list_comments` | Page comments |
| `get_database` | Get database schema |
| `query_database` | Query with filters and sorts |
| `add_database_entry` / `add_database_entries` | Create entries (single/bulk) |
| `update_database_entry` / `delete_database_entry` | Update/delete entries |
| `create_database` | Create new database |
| `list_databases` | List accessible databases |

### Alternate MCP: `mcp__78651ef0-b949-45c5-8b08-0f97b6f05863__notion-*`

**Note:** The UUID prefix may change if the MCP reconnects. Match by tool name suffix (e.g., `notion-update-page`, `notion-fetch`).

| Tool | Purpose |
|------|---------|
| `notion-fetch` | Fetch page in enhanced markdown (may truncate large pages) |
| `notion-update-page` | Versatile update with multiple commands (see below) |
| `notion-create-pages` | Create pages with properties |
| `notion-search` | Search with advanced filters (date range, created_by) |
| `notion-duplicate-page` | Duplicate page |
| `notion-move-pages` | Bulk move pages |
| `notion-create-view` / `notion-update-view` | View CRUD (table, board, calendar, etc.) |
| `notion-update-data-source` | Schema management (add/rename/drop columns) |
| `notion-create-comment` / `notion-get-comments` | Rich text comments with threading |
| `notion-get-teams` / `notion-get-users` | Team and user listing |

**`notion-update-page` commands:**

| Command | What it does |
|---------|-------------|
| `update_content` | Find/replace with `old_str`/`new_str` pairs — matches within single blocks |
| `replace_content` | Replace entire page (warns about child page deletion) |
| `update_properties` | Update page properties (title, etc.) |
| `apply_template` | Apply a template to the page |
| `update_verification` | Set verification status |

---

## 2. Tool Selection Matrix

| Operation | Best Tool | Fallback | Known Limits |
|-----------|-----------|----------|-------------|
| **Read page** | `read_page` (primary) | `notion-fetch` (alt) | Alt truncates at ~54KB |
| **Create page (<90 blocks)** | `create_page` (primary) | `notion-create-pages` (alt) | 100-block limit |
| **Create page (>90 blocks)** | `create_page` + `append_content` | Split at heading boundary | Estimate blocks first |
| **Replace unique text** | `find_replace` (primary) | `update_content` (alt) | Must be globally unique |
| **Replace all instances** | `find_replace` + `replace_all: true` | — | All instances change |
| **Replace non-unique text** | `update_content` (alt) with context | Section rewrite | Can't cross block boundaries |
| **Rewrite section** | `update_section` (primary) | `update_content` heading trick (alt) | TypeError on large pages |
| **Insert before a block** | `update_content` heading trick (alt) | — | Match heading, prepend in replacement |
| **Edit unique table cell** | `find_replace` on cell text (no pipes) | Section rewrite | Cell text must be globally unique |
| **Edit non-unique table cell** | Section rewrite | — | Rewrite entire table under heading |
| **Search pages** | `search` (primary) | `notion-search` (alt, advanced) | Alt has date/user filters |
| **Database query** | `query_database` (primary) | — | Use `get_database` for schema first |
| **Database schema change** | `notion-update-data-source` (alt) | — | Primary has no schema tool |
| **View management** | `notion-create-view` / `update-view` (alt) | — | Primary has no view tools |

---

## 3. Known Pitfalls

### P1: update_section TypeError
**Symptom:** `Cannot read properties of undefined (reading 'trim')` on any heading.
**Trigger:** Large pages with complex block structures (observed on pages >100 blocks).
**Danger:** Partially deletes section content without writing replacement.
**Mitigation:** ALWAYS re-read page after a TypeError. Use heading-match trick as fallback.

### P2: find_replace table cell failure
**Symptom:** "No matches found" for `| cell1 | cell2 |` syntax.
**Cause:** Notion stores table cells as separate blocks. The pipe-delimited markdown is a read-time representation, not stored text.
**Mitigation:** Search for cell text only (without pipes). If non-unique, rewrite the entire table section.

### P3: find_replace "Multiple matches found"
**Symptom:** Error when target text appears in 2+ locations.
**Cause:** No "first match only" option. Tool requires uniqueness or explicit `replace_all: true`.
**Mitigation:** Use `replace_all: true` if all should change. Otherwise, add surrounding context to make match unique via alt MCP's `update_content`.

### P4: update_content cross-block matching
**Symptom:** "No matches found" for text that spans two blocks (e.g., paragraph + heading separated by `\n`).
**Cause:** Blocks are independent objects. `\n` between blocks isn't part of either block's text.
**Mitigation:** Match within a single block only. For cross-block operations, use the heading-match trick.

### P5: create_page 100-block limit
**Symptom:** `body.children.length should be <= 100, instead was N`.
**Cause:** Hard limit on blocks per API call.
**Mitigation:** Estimate blocks before creating. Split at heading boundary near block 80-90, create + append remaining chunks.

### P6: replace_content formatting breakage
**Symptom:** `\n` renders as literal text, tables collapse, pipes show as `\|`.
**Cause:** Large escaped content strings don't parse correctly.
**Mitigation:** Never use `replace_content` for large content. Create a new page instead, or use targeted `update_content` edits.

### P7: Pipe characters in table cells
**Symptom:** Cell content truncated at first `|` character.
**Cause:** Notion interprets `|` inside a cell value as a cell separator.
**Mitigation:** Use `/` instead of `|` for enum notation (e.g., `option_a / option_b`).

### P8: Em-dash matching
**Symptom:** "No matches found" when searching for text containing `—`.
**Cause:** Em-dash (U+2014 `—`) and regular dash/hyphen (U+002D `-`) are different characters.
**Mitigation:** Copy the exact character from the read output. When in doubt, read the page first and use the exact string.

### P9: notion-fetch truncation
**Symptom:** Content near the end of a large page is missing from fetch output.
**Cause:** Alt MCP truncates at ~54KB.
**Mitigation:** Use `read_page` (primary) for reading. Fall back to `notion-fetch` only when primary is disconnected.

### P10: Primary MCP disconnection
**Symptom:** All `mcp__notion__*` tools fail.
**Cause:** MCP server disconnects during long sessions.
**Mitigation:** Run `/notion diagnose` to check status. Route through alt MCP equivalents.

### P11: replace_content on parent pages archives all children
**Symptom:** After `replace_content` on a parent page, `list_pages` returns fewer children than expected. Child pages return "Could not find block" on read.
**Cause:** `replace_content` deletes ALL blocks including child page link blocks. The child pages become archived/orphaned.
**Mitigation:** NEVER use `replace_content` on pages with children. Use `update_section` or `find_replace` for targeted edits. Before writing to any page, check if it has children via `list_pages`.

### P12: find_replace fails on table cell content (even unique text)
**Symptom:** "No matches found" when targeting text inside a table cell, even when the text is unique and copied exactly from read output.
**Cause:** Table cells have different internal storage from rich text blocks. Even individual cell text (without pipe delimiters) may not be matchable.
**Mitigation:** For any text change inside a table, use `update_section` to rewrite the entire section containing the table. Only trust `find_replace` on paragraphs, headings, callouts, and list items.

---

## 4. Table Operations Deep Dive

### How Notion Stores Tables

Internally, a Notion table is a `table` block containing `table_row` child blocks. Each row has a `cells` array where each cell is an array of rich text objects. The markdown `| col1 | col2 |` representation is generated by the read tools — it does not exist as searchable text.

**Implications:**
- `find_replace` and `update_content` cannot match across cells
- Each cell's text content IS individually searchable (without pipes)
- Identical cell values in different rows cause "Multiple matches found"
- Table rows are ~1 block each for block-count estimation

### Table Edit Decision Tree

```
NEED: Edit a specific table cell
  |
  ├─ Cell content is globally unique on page?
  |   YES → find_replace(cell_text, new_text)
  |   NO  → ↓
  |
  ├─ ALL cells with this content should change?
  |   YES → find_replace(cell_text, new_text, replace_all=true)
  |   NO  → ↓
  |
  └─ Rewrite entire table section
      1. Identify the heading above the table
      2. Use SECTION mode to rewrite heading content (includes full table)
```

---

## 5. Block Count Estimation

| Element | Blocks |
|---------|--------|
| Paragraph | 1 |
| Heading (any level) | 1 |
| List item | 1 per item |
| Table | 1 (table block) + 1 per row (including header) |
| Code block | 1 |
| Divider (`---`) | 1 |
| Callout / Quote | 1 |
| Toggle block | 1 |
| Image / Embed | 1 |

**Quick estimate:** Count lines in your markdown (excluding blank lines), then add extra for table rows. If estimate > 85, plan to split.

---

## 6. The Heading-Match Trick

**Purpose:** Insert content BEFORE an existing heading when no other tool can do it.

**How it works:**
1. Read the page to find the exact heading text (e.g., `### Two-Component Home Model (D78)`)
2. Use the alt MCP's `update_content` command
3. Set `old_str` to the heading text
4. Set `new_str` to: `[content you want to insert]\n### Two-Component Home Model (D78)`
5. The heading is preserved at the end; your content appears before it

**Why it works:** Headings are single blocks with exact, usually unique text. By matching the heading and replacing it with "new content + original heading", you effectively insert before the heading.

**When to use:**
- Content was accidentally deleted by a failed `update_section` call
- You need to add a new section between two existing sections
- There's no heading above your target insertion point

**Limitations:**
- The heading text must be globally unique on the page
- New content in `new_str` is limited to what fits in a single API call
- If the heading contains special characters, copy them exactly from the read output
