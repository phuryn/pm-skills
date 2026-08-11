/**
 * Port remaining Claude commands to pi prompt templates.
 *
 * Mechanical transformation of the pm-* plugin commands (markdown files)
 * into pi-extensions/prompts/*.md templates:
 *   1. Keep frontmatter description + argument-hint (drop pi-irrelevant keys
 *      like allowed-tools).
 *   2. Drop the "# /name -- Title" H1 and the "## Invocation" section.
 *   3. Prepend a workflow header and an "## Input" section whose
 *      ${ARGUMENTS:-default} fallback tells the agent what to ask for.
 *   4. Keep the workflow body verbatim (pi's engine substitutes $ARGUMENTS
 *      at expansion time, which is the desired behavior).
 *
 * Idempotent: skips templates that already exist.
 *
 * Run: node scripts/port-commands.mjs   (from pi-extensions/)
 */

import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const here = fileURLToPath(new URL(".", import.meta.url));
const packageRoot = join(here, "..");
const repoRoot = join(packageRoot, "..");
const promptsDir = join(packageRoot, "prompts");

// Commands already ported by hand (skip).
const ALREADY_PORTED = new Set([
  "write-prd", "pre-mortem", "discover", "strategy", "research-users",
  "write-query", "plan-launch", "north-star", "review-resume", "ship-check",
]);

// Per-command Input defaults for commands whose argument selects a mode or
// where the generic default reads poorly. Keyed by command name.
const INPUT_DEFAULTS = {
  "sprint":
    "No mode or context provided — ask the user what they want (plan, retro, or release-notes) and what sprint or release this covers.",
  "business-model":
    "No mode or business provided — ask which canvas they want (lean, full, startup, or value-prop) and about the product or business.",
  "interview":
    "No mode or topic provided — ask whether they want to prepare an interview script (prep) or summarize a transcript (summarize), and the topic or transcript.",
  "write-stories":
    "No mode or feature provided — ask which format they want (user, job, or wwa stories) and about the feature or PRD.",
  "brainstorm":
    "No mode or topic provided — ask whether they want ideas or experiments, for an existing or new product, and the product or feature.",
};

function parseFrontmatter(text) {
  const match = text.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return {};
  const fm = {};
  for (const line of match[1].split("\n")) {
    const idx = line.indexOf(":");
    if (idx === -1) continue;
    const key = line.slice(0, idx).trim();
    let value = line.slice(idx + 1).trim();
    if (value.length >= 2 && value.startsWith('"') && value.endsWith('"')) {
      value = value.slice(1, -1);
    }
    fm[key] = value;
  }
  return fm;
}

function defaultFor(name, hint) {
  if (INPUT_DEFAULTS[name]) return INPUT_DEFAULTS[name];
  return `No input was provided — ask the user for: ${hint ?? "the details needed to run this workflow"}.`;
}

function transform(filePath, name) {
  const raw = readFileSync(filePath, "utf8");
  const fm = parseFrontmatter(raw);

  // Strip frontmatter and H1.
  let body = raw.replace(/^---\n[\s\S]*?\n---\n?/, "").replace(/^\n+/, "");
  const titleMatch = body.match(/^#\s+\/[a-z0-9-]+\s+--\s+(.+)$/m);
  const title = titleMatch ? titleMatch[1].trim() : name;
  body = body.replace(/^#\s+\/[a-z0-9-]+\s+--\s+.+$\n?/m, "");

  // Drop the "## Invocation" section (up to the next ## heading or EOF).
  body = body.replace(/## Invocation\n[\s\S]*?(?=^## )/m, "");

  // Split intro (before first ## heading) from workflow body.
  const firstHeading = body.search(/^## /m);
  let intro = firstHeading === -1 ? body : body.slice(0, firstHeading);
  let workflow = firstHeading === -1 ? "" : body.slice(firstHeading);
  intro = intro.trim();

  const description = fm.description ?? title;
  const hint = fm["argument-hint"] ?? "";

  return `---
description: ${description}
argument-hint: ${JSON.stringify(hint)}
---

You are executing the /${name} workflow: ${title}.

${intro}

## Input

${"${ARGUMENTS:-" + defaultFor(name, hint) + "}"}

${workflow.trim()}
`;
}

mkdirSync(promptsDir, { recursive: true });
const written = [];
for (const plugin of readdirSync(repoRoot, { withFileTypes: true })) {
  if (!plugin.isDirectory() || !plugin.name.startsWith("pm-")) continue;
  const commandsDir = join(repoRoot, plugin.name, "commands");
  if (!existsSync(commandsDir)) continue;
  for (const file of readdirSync(commandsDir)) {
    if (!file.endsWith(".md")) continue;
    const name = file.replace(/\.md$/, "");
    if (ALREADY_PORTED.has(name)) continue;
    const outPath = join(promptsDir, `${name}.md`);
    if (existsSync(outPath)) continue; // idempotent
    const template = transform(join(commandsDir, file), name);
    writeFileSync(outPath, template, "utf8");
    written.push(name);
  }
}

console.log(`Wrote ${written.length} prompt templates: ${written.join(", ")}`);
