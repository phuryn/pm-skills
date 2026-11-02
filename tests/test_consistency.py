"""Docs and manifest consistency checks, verified on every PR, push, and release.

What this locks in:
- marketplace.json lists exactly the plugin directories on disk;
- one version everywhere: newest CHANGELOG heading == marketplace.json == every plugin.json
  (CLAUDE.md rule: no independent per-plugin versioning);
- CHANGELOG headings are well-formed, dated, unique, and newest-first;
- README counts (headline, per-plugin summaries, plugin README section headers)
  match the skills and commands actually on disk;
- every /plugin:command reference in a plugin README resolves to a real command file.
"""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
CURSOR_MARKETPLACE = ROOT / ".cursor-plugin" / "marketplace.json"
CHANGELOG = ROOT / "CHANGELOG.md"
README = ROOT / "README.md"
CLAUDE_MD = ROOT / "CLAUDE.md"


def plugin_dirs():
    return sorted(
        p
        for p in ROOT.iterdir()
        if p.is_dir() and (p / ".claude-plugin" / "plugin.json").is_file()
    )


def skill_count(plugin: Path) -> int:
    skills = plugin / "skills"
    if not skills.is_dir():
        return 0
    return sum(1 for s in skills.iterdir() if s.is_dir())


def command_count(plugin: Path) -> int:
    cmds = plugin / "commands"
    if not cmds.is_dir():
        return 0
    return len(list(cmds.glob("*.md")))


def marketplace() -> dict:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))


def cursor_marketplace() -> dict:
    return json.loads(CURSOR_MARKETPLACE.read_text(encoding="utf-8"))


def latest_changelog_version() -> str:
    for line in CHANGELOG.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## v(\d+\.\d+\.\d+)\b", line)
        if m:
            return m.group(1)
    raise AssertionError("no ## vX.Y.Z heading found in CHANGELOG.md")


class TestMarketplaceList(unittest.TestCase):
    def test_marketplace_lists_exactly_the_plugins_on_disk(self):
        listed = {p["name"] for p in marketplace()["plugins"]}
        on_disk = {p.name for p in plugin_dirs()}
        self.assertEqual(
            listed,
            on_disk,
            f"marketplace.json vs disk — only listed: {sorted(listed - on_disk)}, "
            f"only on disk: {sorted(on_disk - listed)}",
        )

    def test_sources_point_at_matching_directories(self):
        for p in marketplace()["plugins"]:
            self.assertEqual(
                p["source"],
                f"./{p['name']}",
                f"plugin {p['name']} has source {p['source']}",
            )

    def test_cursor_marketplace_mirrors_claude_marketplace(self):
        claude_mp = marketplace()
        cursor_mp = cursor_marketplace()
        claude_plugins = [p["name"] for p in claude_mp["plugins"]]
        cursor_plugins = [p["name"] for p in cursor_mp["plugins"]]
        self.assertEqual(
            cursor_plugins,
            claude_plugins,
            "Cursor marketplace plugin list does not match Claude marketplace",
        )
        claude_by_name = {p["name"]: p for p in claude_mp["plugins"]}
        for p in cursor_mp["plugins"]:
            self.assertEqual(
                p["source"],
                p["name"],
                f"Cursor plugin {p['name']} has source {p['source']}",
            )
            self.assertEqual(
                p["description"],
                claude_by_name[p["name"]]["description"],
                f"Cursor marketplace description mismatch for {p['name']}",
            )
            self.assertEqual(
                p["category"],
                claude_by_name[p["name"]]["category"],
                f"Cursor marketplace category mismatch for {p['name']}",
            )


class TestVersionSync(unittest.TestCase):
    """One version everywhere; the newest CHANGELOG heading is the released version."""

    def test_all_versions_identical_and_match_changelog(self):
        want = latest_changelog_version()
        mismatches = []
        mp_version = marketplace()["version"]
        if mp_version != want:
            mismatches.append(f"marketplace.json={mp_version}")
        cursor_mp_version = cursor_marketplace().get("metadata", {}).get("version")
        if cursor_mp_version != want:
            mismatches.append(f".cursor-plugin/marketplace.json={cursor_mp_version}")
        for p in plugin_dirs():
            manifest = p / ".claude-plugin" / "plugin.json"
            v = json.loads(manifest.read_text(encoding="utf-8"))["version"]
            if v != want:
                mismatches.append(f"{p.name}={v}")
            cursor_manifest = p / ".cursor-plugin" / "plugin.json"
            if not cursor_manifest.is_file():
                mismatches.append(f"{p.name}/.cursor-plugin/plugin.json=missing")
            else:
                cv = json.loads(cursor_manifest.read_text(encoding="utf-8")).get("version")
                if cv != want:
                    mismatches.append(f"{p.name}/.cursor-plugin={cv}")
        self.assertEqual(
            mismatches,
            [],
            f"CHANGELOG says v{want}; out of sync: {mismatches}",
        )

    def test_cursor_plugin_manifests_mirror_claude_manifests(self):
        for p in plugin_dirs():
            claude_data = json.loads(
                (p / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
            )
            cursor_data = json.loads(
                (p / ".cursor-plugin" / "plugin.json").read_text(encoding="utf-8")
            )
            for field in ("name", "version", "description", "keywords", "homepage", "license"):
                self.assertEqual(
                    cursor_data.get(field),
                    claude_data.get(field),
                    f"{p.name} Cursor vs Claude manifest mismatch on {field}",
                )


class TestChangelogFormat(unittest.TestCase):
    def test_headings_well_formed_dated_unique_descending(self):
        text = CHANGELOG.read_text(encoding="utf-8")
        headings = [l for l in text.splitlines() if l.startswith("## ")]
        self.assertTrue(headings, "CHANGELOG.md has no ## headings")

        versions = []
        for h in headings:
            if h.strip() == "## Unreleased":
                continue
            m = re.match(r"^## v(\d+\.\d+\.\d+) — \d{4}-\d{2}-\d{2}$", h)
            self.assertIsNotNone(
                m,
                f"malformed CHANGELOG heading {h!r} — expected '## vX.Y.Z — YYYY-MM-DD'",
            )
            versions.append(tuple(int(x) for x in m.group(1).split(".")))

        self.assertEqual(
            len(versions), len(set(versions)), "duplicate version headings"
        )
        self.assertEqual(
            versions,
            sorted(versions, reverse=True),
            "version headings are not newest-first",
        )


class TestReadmeCounts(unittest.TestCase):
    def _totals(self):
        plugins = plugin_dirs()
        return (
            sum(map(skill_count, plugins)),
            sum(map(command_count, plugins)),
            len(plugins),
        )

    def test_root_readme_headline_counts(self):
        skills, commands, plugins = self._totals()
        text = README.read_text(encoding="utf-8")
        m = re.search(
            r"(\d+) PM skills and (\d+) chained workflows across (\d+) plugins", text
        )
        self.assertIsNotNone(m, "headline count sentence not found in README.md")
        self.assertEqual(
            (int(m.group(1)), int(m.group(2)), int(m.group(3))),
            (skills, commands, plugins),
            "README.md headline counts don't match disk",
        )

    def test_marketplace_description_counts(self):
        skills, commands, plugins = self._totals()
        desc = marketplace()["description"]
        m = re.search(
            r"(\d+) domain-specific skills and (\d+) chained workflows across (\d+) PM plugins",
            desc,
        )
        self.assertIsNotNone(
            m, "count sentence not found in marketplace.json description"
        )
        self.assertEqual(
            (int(m.group(1)), int(m.group(2)), int(m.group(3))),
            (skills, commands, plugins),
            "marketplace.json description counts don't match disk",
        )
        cursor_desc = cursor_marketplace().get("metadata", {}).get("description", "")
        self.assertEqual(
            cursor_desc,
            desc,
            ".cursor-plugin/marketplace.json metadata.description does not match .claude-plugin/marketplace.json",
        )

    def test_claude_md_headline_counts(self):
        skills, commands, plugins = self._totals()
        text = CLAUDE_MD.read_text(encoding="utf-8")
        m = re.search(
            r"\*\*(\d+) independent plugins\*\* \((\d+) skills, (\d+) commands\)",
            text,
        )
        self.assertIsNotNone(m, "headline count sentence not found in CLAUDE.md")
        self.assertEqual(
            (int(m.group(2)), int(m.group(3)), int(m.group(1))),
            (skills, commands, plugins),
            "CLAUDE.md headline counts don't match disk",
        )

    def test_root_readme_per_plugin_counts(self):
        text = README.read_text(encoding="utf-8")
        found = {}
        for m in re.finditer(
            r"<strong>\d+\.\s*(pm-[\w-]+)</strong>[^)]*\((\d+) skills?, (\d+) commands?\)",
            text,
        ):
            found[m.group(1)] = (int(m.group(2)), int(m.group(3)))
        for p in plugin_dirs():
            self.assertIn(
                p.name,
                found,
                f"{p.name} has no '(N skills, M commands)' summary line in README.md",
            )
            self.assertEqual(
                found[p.name],
                (skill_count(p), command_count(p)),
                f"README.md counts wrong for {p.name}",
            )

    def test_plugin_readme_section_counts(self):
        for p in plugin_dirs():
            readme = p / "README.md"
            if not readme.is_file():
                continue
            text = readme.read_text(encoding="utf-8")
            m = re.search(r"^## Skills \((\d+)\)", text, re.M)
            if m:
                self.assertEqual(
                    int(m.group(1)),
                    skill_count(p),
                    f"{p.name}/README.md '## Skills (N)' header",
                )
            m = re.search(r"^## Commands \((\d+)\)", text, re.M)
            if m:
                self.assertEqual(
                    int(m.group(1)),
                    command_count(p),
                    f"{p.name}/README.md '## Commands (N)' header",
                )


class TestCommandReferences(unittest.TestCase):
    """Every /plugin:command mentioned in a plugin README must exist on disk."""

    def test_plugin_readme_command_refs_exist(self):
        for p in plugin_dirs():
            readme = p / "README.md"
            if not readme.is_file():
                continue
            text = readme.read_text(encoding="utf-8")
            for m in re.finditer(rf"/{re.escape(p.name)}:([\w-]+)", text):
                cmd = p / "commands" / f"{m.group(1)}.md"
                self.assertTrue(
                    cmd.is_file(),
                    f"{p.name}/README.md references /{p.name}:{m.group(1)} "
                    f"but commands/{m.group(1)}.md is missing",
                )


if __name__ == "__main__":
    unittest.main()
