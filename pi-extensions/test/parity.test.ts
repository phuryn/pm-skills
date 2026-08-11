/**
 * Parity tests — verify the pi package stays in sync with the Claude Code
 * commands and skills it ports.
 *
 * The package is fully declarative: package.json declares the prompt
 * templates (commands) and the skill directories. Nothing is embedded in
 * code. For every prompt template in prompts/:
 *   - the file name matches a Claude command file name (pm-* plugin commands)
 *   - the description matches the Claude frontmatter `description`
 *   - the argument hint matches the Claude frontmatter `argument-hint`
 *   - the body interpolates arguments via $ARGUMENTS / ${ARGUMENTS:-...}
 *   - the referenced skills exist in the repo (pm-* plugin skills)
 *   - bodies contain no $<digit> sequences (pi would substitute them)
 *
 * Both package manifests (repo root for git installs, pi-extensions/ for
 * local-path installs) are checked: they must declare the prompts and the
 * skills, and the declared paths must resolve to the expected files.
 *
 * Run with: npm test
 */

import assert from "node:assert/strict";
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";
import { test } from "node:test";

const PACKAGE_ROOT = resolve(import.meta.dirname, "..");
const REPO_ROOT = resolve(PACKAGE_ROOT, "..");
const PROMPTS_DIR = join(PACKAGE_ROOT, "prompts");

const EXPECTED_COMMANDS = [
  // pm-execution
  "generate-data",
  "meeting-notes",
  "plan-okrs",
  "pre-mortem",
  "red-team-prd",
  "sprint",
  "stakeholder-map",
  "test-scenarios",
  "transform-roadmap",
  "write-prd",
  "write-stories",
  // pm-product-discovery
  "brainstorm",
  "discover",
  "interview",
  "setup-metrics",
  "triage-requests",
  // pm-product-strategy
  "business-model",
  "market-scan",
  "pricing",
  "strategy",
  "value-proposition",
  // pm-market-research
  "analyze-feedback",
  "competitive-analysis",
  "research-users",
  // pm-data-analytics
  "analyze-cohorts",
  "analyze-test",
  "write-query",
  // pm-go-to-market
  "battlecard",
  "growth-strategy",
  "plan-launch",
  // pm-marketing-growth
  "market-product",
  "north-star",
  // pm-toolkit
  "draft-nda",
  "privacy-policy",
  "proofread",
  "review-resume",
  "tailor-resume",
  // pm-ai-shipping
  "derive-tests",
  "document-app",
  "performance-audit-static",
  "security-audit-static",
  "ship-check",
];

interface Frontmatter {
  [key: string]: string | undefined;
}

function parseFrontmatter(text: string): { frontmatter: Frontmatter; body: string } {
  const match = text.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  assert.ok(match, `no frontmatter found`);
  const frontmatter: Frontmatter = {};
  for (const line of match[1]!.split("\n")) {
    const idx = line.indexOf(":");
    if (idx === -1) continue;
    const key = line.slice(0, idx).trim();
    let value = line.slice(idx + 1).trim();
    if (value.length >= 2 && value.startsWith('"') && value.endsWith('"')) {
      value = value.slice(1, -1);
    }
    frontmatter[key] = value;
  }
  return { frontmatter, body: match[2]! ?? "" };
}

/** Find the pm-* plugin dir that owns a given Claude command file. */
function findClaudeCommandFile(commandName: string): string {
  for (const dir of readdirSync(REPO_ROOT, { withFileTypes: true })) {
    if (!dir.isDirectory() || !dir.name.startsWith("pm-")) continue;
    const file = join(REPO_ROOT, dir.name, "commands", `${commandName}.md`);
    if (existsSync(file)) return file;
  }
  assert.fail(`no Claude command file found for ${commandName}`);
}

/** Find the pm-* plugin dir that owns a given skill. */
function findSkillFile(skillName: string): string {
  for (const dir of readdirSync(REPO_ROOT, { withFileTypes: true })) {
    if (!dir.isDirectory() || !dir.name.startsWith("pm-")) continue;
    const file = join(REPO_ROOT, dir.name, "skills", skillName, "SKILL.md");
    if (existsSync(file)) return file;
  }
  assert.fail(`no SKILL.md found in the repo for skill ${skillName}`);
}

/** Extract **skill-name** references from a prompt template body. */
function referencedSkills(body: string): string[] {
  const matches = [...body.matchAll(/\*\*([a-z0-9-]+)\*\* skill/g)];
  const names = new Set<string>();
  for (const match of matches) {
    const name = match[1]!;
    if (/^(existing|new|full|static)$/.test(name)) continue;
    names.add(name);
  }
  return [...names].sort();
}

test("all 42 Claude commands have a prompt template (full parity)", () => {
  const onDisk: string[] = [];
  for (const dir of readdirSync(REPO_ROOT, { withFileTypes: true })) {
    if (!dir.isDirectory() || !dir.name.startsWith("pm-")) continue;
    const commandsDir = join(REPO_ROOT, dir.name, "commands");
    for (const file of readdirSync(commandsDir)) {
      if (file.endsWith(".md")) onDisk.push(file.replace(/\.md$/, ""));
    }
  }
  assert.equal(EXPECTED_COMMANDS.length, onDisk.length, "EXPECTED_COMMANDS out of sync with repo");
  assert.deepEqual([...EXPECTED_COMMANDS].sort(), onDisk.sort());
  for (const name of EXPECTED_COMMANDS) {
    assert.ok(existsSync(join(PROMPTS_DIR, `${name}.md`)), `missing prompt template: ${name}.md`);
  }
});

test("no unexpected prompt templates exist", () => {
  const onDisk = readdirSync(PROMPTS_DIR)
    .filter((f) => f.endsWith(".md"))
    .map((f) => f.replace(/\.md$/, ""))
    .sort();
  assert.deepEqual(onDisk, [...EXPECTED_COMMANDS].sort());
});

for (const name of EXPECTED_COMMANDS) {
  test(`parity: /${name} matches ${name}.md frontmatter`, () => {
    const template = readFileSync(join(PROMPTS_DIR, `${name}.md`), "utf8");
    const { frontmatter } = parseFrontmatter(template);

    const claudeText = readFileSync(findClaudeCommandFile(name), "utf8");
    const { frontmatter: claude } = parseFrontmatter(claudeText);

    assert.equal(
      frontmatter.description,
      claude.description,
      `description mismatch for /${name}`
    );
    assert.equal(
      frontmatter["argument-hint"],
      claude["argument-hint"],
      `argument-hint mismatch for /${name}`
    );
  });
}

for (const name of EXPECTED_COMMANDS) {
  test(`template: /${name} interpolates args and references real skills`, () => {
    const template = readFileSync(join(PROMPTS_DIR, `${name}.md`), "utf8");
    const { body } = parseFrontmatter(template);

    assert.ok(
      /\$(ARGUMENTS|@)|\$\{ARGUMENTS:-/.test(body),
      `body for /${name} does not use $ARGUMENTS`
    );
    assert.ok(body.length > 300, `body for /${name} is suspiciously short`);

    for (const skill of referencedSkills(body)) {
      assert.ok(
        existsSync(findSkillFile(skill)),
        `skill "${skill}" referenced by /${name} has no SKILL.md in the repo`
      );
    }
  });
}

test("no substitution hazards in template bodies", () => {
  // pi's template engine replaces $ARGUMENTS, $@, and $<digit>. A literal
  // "$5" in a body would silently become an empty string, so bodies must
  // never contain dollar-followed-by-digit outside of the Input placeholder.
  for (const name of EXPECTED_COMMANDS) {
    const template = readFileSync(join(PROMPTS_DIR, `${name}.md`), "utf8");
    const { body } = parseFrontmatter(template);
    const hazardous = body.match(/\$[0-9]/);
    assert.ok(!hazardous, `/${name} body contains a \$<digit> hazard: ${hazardous?.[0]}`);
  }
});

test("package manifests declare prompts and skills (declarative package)", () => {
  const manifests: Array<{ path: string; base: string }> = [
    { path: join(REPO_ROOT, "package.json"), base: REPO_ROOT },
    { path: join(PACKAGE_ROOT, "package.json"), base: PACKAGE_ROOT },
  ];

  for (const { path, base } of manifests) {
    const manifest = JSON.parse(readFileSync(path, "utf8")) as {
      name: string;
      version: string;
      pi?: { extensions?: string[]; prompts?: string[]; skills?: string[] };
    };
    assert.equal(manifest.name, "pm-skills-pi", `${path}: wrong package name`);
    assert.equal(manifest.version, "2.1.0", `${path}: version out of sync`);
    assert.ok(manifest.pi, `${path}: missing pi manifest`);
    assert.ok(manifest.pi.prompts?.length, `${path}: no prompts declared`);
    assert.ok(manifest.pi.skills?.length, `${path}: no skills declared`);
    // The package is fully declarative — no extension entry.
    assert.equal(manifest.pi.extensions, undefined, `${path}: extension entry should be gone`);

    for (const rel of [...(manifest.pi.prompts ?? [])]) {
      const abs = join(base, rel);
      assert.ok(existsSync(abs), `${path}: declared prompts path does not exist: ${rel}`);
    }

    // Every declared skill glob must resolve to exactly the repo's 68 SKILL.md files.
    const skillsDirs = manifest.pi.skills ?? [];
    let skillFiles = 0;
    for (const glob of skillsDirs) {
      // Manual glob expansion for the repo's shapes: "./pm-*/skills" and
      // "../pm-*/skills" (pi expands these with globSync at load time).
      const match = glob.match(/^((?:\.\.?\/)*)([^*]*)\*(.*)$/);
      assert.ok(match, `${path}: expected a glob for skills, got ${glob}`);
      const [, leading, prefix, suffix] = match as unknown as [string, string, string, string];
      const scanDir = resolve(base, leading); // "./" or "../" → base or its parent
      for (const entry of readdirSync(scanDir, { withFileTypes: true })) {
        if (!entry.isDirectory() || !entry.name.startsWith(prefix)) continue;
        const skillDir = join(scanDir, entry.name, suffix);
        if (!existsSync(skillDir)) continue;
        skillFiles += readdirSync(skillDir).filter((f) =>
          existsSync(join(skillDir, f, "SKILL.md"))
        ).length;
      }
    }
    assert.equal(skillFiles, 68, `${path}: expected 68 skills via manifest globs, got ${skillFiles}`);
  }
});

test("declared prompts dir covers every ported command (root manifest)", () => {
  const rootManifest = JSON.parse(
    readFileSync(join(REPO_ROOT, "package.json"), "utf8")
  ) as { pi?: { prompts?: string[] } };
  const declaredDir = join(REPO_ROOT, rootManifest.pi?.prompts?.[0]!);
  const onDisk = readdirSync(declaredDir)
    .filter((f) => f.endsWith(".md"))
    .map((f) => f.replace(/\.md$/, ""))
    .sort();
  assert.deepEqual(onDisk, [...EXPECTED_COMMANDS].sort());
});
