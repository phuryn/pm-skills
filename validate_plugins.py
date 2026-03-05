#!/usr/bin/env python3
"""
Plugin Collection Validator
===========================
Validates all plugins in the collection against the Claude Code plugin spec:
- plugin.json manifest: required fields, author attribution, keywords
- Skills: YAML frontmatter (name must match directory, description required)
- Commands: YAML frontmatter (description and argument-hint required)
- Cross-references: commands referencing skills that exist in the same plugin
- README: exists and has expected sections

Based on:
- Anthropic plugin-dev README (https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev)
- agentskills.io specification
- Claude Code plugins reference (https://code.claude.com/docs/en/plugins-reference)

Author: Paweł Huryn — The Product Compass Newsletter (https://www.productcompass.pm)
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Optional


# ─── Configuration ───────────────────────────────────────────────────────────

# Required plugin.json fields per spec
REQUIRED_MANIFEST_FIELDS = ["name", "version", "description"]
RECOMMENDED_MANIFEST_FIELDS = ["author", "keywords", "homepage", "license"]
REQUIRED_AUTHOR_FIELDS = ["name", "email"]
RECOMMENDED_AUTHOR_FIELDS = ["url"]

# Required skill frontmatter fields
REQUIRED_SKILL_FIELDS = ["name", "description"]

# Required command frontmatter fields
REQUIRED_COMMAND_FIELDS = ["description"]
RECOMMENDED_COMMAND_FIELDS = ["argument-hint"]

# Expected README sections (case-insensitive substring match)
EXPECTED_README_SECTIONS = ["overview", "install", "skill", "command"]


# ─── ANSI Colors ─────────────────────────────────────────────────────────────

class C:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"


# ─── Helpers ─────────────────────────────────────────────────────────────────

def parse_yaml_frontmatter(content: str) -> Optional[dict]:
    """Extract YAML frontmatter from a markdown file (between --- markers)."""
    if not content.startswith("---"):
        return None
    end = content.find("---", 3)
    if end == -1:
        return None
    fm_text = content[3:end].strip()
    # Simple YAML parser for flat key-value pairs
    result = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r'^(\S+):\s*(.+)$', line)
        if match:
            key = match.group(1)
            value = match.group(2).strip().strip('"').strip("'")
            result[key] = value
    return result


def count_words(content: str) -> int:
    """Count words in markdown content (excluding frontmatter)."""
    # Strip frontmatter
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            content = content[end + 3:]
    return len(content.split())


# ─── Validators ──────────────────────────────────────────────────────────────

class ValidationResult:
    def __init__(self):
        self.errors: list[str] = []      # Must fix
        self.warnings: list[str] = []    # Should fix
        self.info: list[str] = []        # FYI

    def error(self, msg: str):
        self.errors.append(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)

    def note(self, msg: str):
        self.info.append(msg)

    @property
    def ok(self) -> bool:
        return len(self.errors) == 0


def validate_manifest(plugin_dir: str) -> ValidationResult:
    """Validate plugin.json manifest."""
    result = ValidationResult()
    pj_path = os.path.join(plugin_dir, ".claude-plugin", "plugin.json")

    if not os.path.isfile(pj_path):
        result.error("Missing .claude-plugin/plugin.json")
        return result

    try:
        with open(pj_path, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        result.error(f"Invalid JSON in plugin.json: {e}")
        return result

    # Required fields
    for field in REQUIRED_MANIFEST_FIELDS:
        if field not in data or not data[field]:
            result.error(f"Missing required field: {field}")

    # Name must match directory name
    dir_name = os.path.basename(plugin_dir)
    if data.get("name") and data["name"] != dir_name:
        result.error(f"Name mismatch: plugin.json says '{data['name']}' but directory is '{dir_name}'")

    # Version format
    version = data.get("version", "")
    if version and not re.match(r'^\d+\.\d+\.\d+$', version):
        result.warn(f"Version '{version}' doesn't follow semver (x.y.z)")

    # Recommended fields
    for field in RECOMMENDED_MANIFEST_FIELDS:
        if field not in data:
            result.warn(f"Missing recommended field: {field}")

    # Author validation
    author = data.get("author")
    if isinstance(author, dict):
        for field in REQUIRED_AUTHOR_FIELDS:
            if field not in author or not author[field]:
                result.warn(f"Missing author.{field}")
        for field in RECOMMENDED_AUTHOR_FIELDS:
            if field not in author:
                result.note(f"Missing author.{field}")
    elif author is not None:
        result.warn("Author should be an object with name, email, url fields")

    # Keywords validation
    keywords = data.get("keywords", [])
    if not keywords:
        result.warn("No keywords defined")
    elif not isinstance(keywords, list):
        result.error("Keywords must be an array")

    # Description length check
    desc = data.get("description", "")
    if desc and len(desc) < 20:
        result.warn(f"Description is very short ({len(desc)} chars)")

    result.note(f"Version: {version}")
    result.note(f"Keywords: {len(keywords) if isinstance(keywords, list) else 0}")

    return result


def validate_skill(skill_dir: str) -> ValidationResult:
    """Validate a single skill directory."""
    result = ValidationResult()
    skill_name = os.path.basename(skill_dir)
    skill_md = os.path.join(skill_dir, "SKILL.md")

    if not os.path.isfile(skill_md):
        result.error("Missing SKILL.md")
        return result

    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()

    # Frontmatter check
    fm = parse_yaml_frontmatter(content)
    if fm is None:
        result.error("Missing YAML frontmatter (must start with ---)")
        return result

    # Required fields
    for field in REQUIRED_SKILL_FIELDS:
        if field not in fm or not fm[field]:
            result.error(f"Missing required frontmatter field: {field}")

    # Name must match directory name (agentskills.io spec)
    if fm.get("name") and fm["name"] != skill_name:
        result.error(f"Name mismatch: frontmatter says '{fm['name']}' but directory is '{skill_name}'")

    # Description quality
    desc = fm.get("description", "")
    if desc:
        if len(desc) < 30:
            result.warn(f"Description is very short ({len(desc)} chars)")
        # Check for trigger phrases (recommended)
        trigger_keywords = ["trigger", "use when", "use for"]
        has_triggers = any(kw in desc.lower() for kw in trigger_keywords)
        if not has_triggers:
            result.note("Description lacks explicit trigger phrases (e.g., 'Triggers: ...')")

    # Word count
    word_count = count_words(content)
    result.note(f"Word count: {word_count}")
    if word_count > 3000:
        result.warn(f"Skill is quite long ({word_count} words). Consider progressive disclosure with references/")
    elif word_count < 50:
        result.warn(f"Skill is very short ({word_count} words). May need more content.")

    return result


def validate_command(cmd_path: str) -> ValidationResult:
    """Validate a single command file."""
    result = ValidationResult()

    with open(cmd_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Frontmatter check
    fm = parse_yaml_frontmatter(content)
    if fm is None:
        result.error("Missing YAML frontmatter (must start with ---)")
        return result

    # Required fields
    for field in REQUIRED_COMMAND_FIELDS:
        if field not in fm or not fm[field]:
            result.error(f"Missing required frontmatter field: {field}")

    # Recommended fields
    for field in RECOMMENDED_COMMAND_FIELDS:
        if field not in fm or not fm[field]:
            result.warn(f"Missing recommended frontmatter field: {field}")

    # Description quality
    desc = fm.get("description", "")
    if desc and len(desc) < 10:
        result.warn(f"Description is very short ({len(desc)} chars)")

    # Check if command references skills (informational)
    skill_refs = re.findall(r'\*\*(\w[\w-]+)\*\*\s+skill', content)
    if skill_refs:
        result.note(f"References skills: {', '.join(skill_refs)}")

    return result


def validate_readme(plugin_dir: str) -> ValidationResult:
    """Validate plugin README.md."""
    result = ValidationResult()
    readme_path = os.path.join(plugin_dir, "README.md")

    if not os.path.isfile(readme_path):
        result.warn("Missing README.md")
        return result

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read().lower()

    # Check for expected sections
    for section in EXPECTED_README_SECTIONS:
        if section not in content:
            result.note(f"README may be missing '{section}' section")

    result.note(f"README: {count_words(content)} words")
    return result


def validate_cross_references(plugin_dir: str, skill_names: list[str]) -> ValidationResult:
    """Check that commands reference skills that actually exist in this plugin."""
    result = ValidationResult()
    cmds_dir = os.path.join(plugin_dir, "commands")

    if not os.path.isdir(cmds_dir):
        return result

    for cmd_file in sorted(os.listdir(cmds_dir)):
        if not cmd_file.endswith(".md"):
            continue
        cmd_path = os.path.join(cmds_dir, cmd_file)
        with open(cmd_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Find skill references like **skill-name** skill
        refs = re.findall(r'\*\*(\w[\w-]+)\*\*\s+skill', content)
        for ref in refs:
            if ref not in skill_names:
                result.warn(f"Command {cmd_file} references skill '{ref}' not found in this plugin")

    return result


# ─── Main Validator ──────────────────────────────────────────────────────────

def validate_plugin(plugin_dir: str) -> dict:
    """Run all validations on a single plugin."""
    plugin_name = os.path.basename(plugin_dir)
    results = {"name": plugin_name, "sections": {}}

    # 1. Manifest
    results["sections"]["manifest"] = validate_manifest(plugin_dir)

    # 2. Skills
    skills_dir = os.path.join(plugin_dir, "skills")
    skill_names = []
    skill_results = {}
    if os.path.isdir(skills_dir):
        for skill_name in sorted(os.listdir(skills_dir)):
            skill_path = os.path.join(skills_dir, skill_name)
            if os.path.isdir(skill_path):
                skill_names.append(skill_name)
                skill_results[skill_name] = validate_skill(skill_path)
    results["sections"]["skills"] = skill_results
    results["skill_count"] = len(skill_names)

    # 3. Commands
    cmds_dir = os.path.join(plugin_dir, "commands")
    cmd_results = {}
    if os.path.isdir(cmds_dir):
        for cmd_file in sorted(os.listdir(cmds_dir)):
            if cmd_file.endswith(".md"):
                cmd_path = os.path.join(cmds_dir, cmd_file)
                cmd_results[cmd_file] = validate_command(cmd_path)
    results["sections"]["commands"] = cmd_results
    results["command_count"] = len(cmd_results)

    # 4. README
    results["sections"]["readme"] = validate_readme(plugin_dir)

    # 5. Cross-references
    results["sections"]["cross-refs"] = validate_cross_references(plugin_dir, skill_names)

    return results


def print_validation_result(label: str, vr: ValidationResult, indent: int = 4):
    """Print a single validation result."""
    prefix = " " * indent
    if vr.errors:
        for e in vr.errors:
            print(f"{prefix}{C.RED}✗ ERROR:{C.RESET} {e}")
    if vr.warnings:
        for w in vr.warnings:
            print(f"{prefix}{C.YELLOW}⚠ WARN:{C.RESET}  {w}")
    if vr.info:
        for i in vr.info:
            print(f"{prefix}{C.DIM}ℹ {i}{C.RESET}")


def print_report(all_results: list[dict]):
    """Print the full validation report."""
    total_errors = 0
    total_warnings = 0
    total_skills = 0
    total_commands = 0

    print(f"\n{C.BOLD}{'='*70}")
    print(f" Plugin Collection Validator — Report")
    print(f"{'='*70}{C.RESET}\n")

    for plugin in all_results:
        name = plugin["name"]
        sc = plugin["skill_count"]
        cc = plugin["command_count"]
        total_skills += sc
        total_commands += cc

        # Count errors/warnings for this plugin
        p_errors = 0
        p_warnings = 0
        for key, section in plugin["sections"].items():
            if isinstance(section, ValidationResult):
                p_errors += len(section.errors)
                p_warnings += len(section.warnings)
            elif isinstance(section, dict):
                for vr in section.values():
                    p_errors += len(vr.errors)
                    p_warnings += len(vr.warnings)

        total_errors += p_errors
        total_warnings += p_warnings

        # Plugin header
        status = f"{C.GREEN}✓ PASS{C.RESET}" if p_errors == 0 else f"{C.RED}✗ FAIL{C.RESET}"
        warn_str = f" {C.YELLOW}({p_warnings} warnings){C.RESET}" if p_warnings > 0 else ""
        print(f"{C.BOLD}{C.CYAN}┌─ {name}{C.RESET}  [{sc} skills, {cc} commands]  {status}{warn_str}")

        # Manifest
        manifest = plugin["sections"]["manifest"]
        if manifest.errors or manifest.warnings:
            print(f"  {C.BOLD}Manifest:{C.RESET}")
            print_validation_result("manifest", manifest)

        # Skills with issues
        skill_results = plugin["sections"]["skills"]
        skills_with_issues = {k: v for k, v in skill_results.items() if v.errors or v.warnings}
        if skills_with_issues:
            print(f"  {C.BOLD}Skills with issues:{C.RESET}")
            for sname, vr in skills_with_issues.items():
                print(f"    {sname}:")
                print_validation_result(sname, vr, indent=6)

        # Commands with issues
        cmd_results = plugin["sections"]["commands"]
        cmds_with_issues = {k: v for k, v in cmd_results.items() if v.errors or v.warnings}
        if cmds_with_issues:
            print(f"  {C.BOLD}Commands with issues:{C.RESET}")
            for cname, vr in cmds_with_issues.items():
                print(f"    {cname}:")
                print_validation_result(cname, vr, indent=6)

        # README
        readme = plugin["sections"]["readme"]
        if readme.errors or readme.warnings:
            print(f"  {C.BOLD}README:{C.RESET}")
            print_validation_result("readme", readme)

        # Cross-references
        xrefs = plugin["sections"]["cross-refs"]
        if xrefs.errors or xrefs.warnings:
            print(f"  {C.BOLD}Cross-references:{C.RESET}")
            print_validation_result("cross-refs", xrefs)

        print(f"{C.CYAN}└{'─'*69}{C.RESET}\n")

    # Summary
    print(f"{C.BOLD}{'='*70}")
    print(f" Summary")
    print(f"{'='*70}{C.RESET}")
    print(f"  Plugins:   {len(all_results)}")
    print(f"  Skills:    {total_skills}")
    print(f"  Commands:  {total_commands}")
    print(f"  Total:     {total_skills + total_commands} components")
    print()
    if total_errors == 0:
        print(f"  {C.GREEN}{C.BOLD}✓ ALL CHECKS PASSED{C.RESET} ({total_warnings} warnings)")
    else:
        print(f"  {C.RED}{C.BOLD}✗ {total_errors} ERRORS{C.RESET}, {total_warnings} warnings")
    print()

    return total_errors


def main():
    """Find and validate all plugins in the collection."""
    # Ensure UTF-8 output on Windows
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Determine base path
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    if not os.path.isdir(base_path):
        print(f"Error: {base_path} is not a directory")
        sys.exit(1)

    # Find all plugin directories (those containing .claude-plugin/)
    plugin_dirs = []
    for entry in sorted(os.listdir(base_path)):
        full_path = os.path.join(base_path, entry)
        if os.path.isdir(full_path) and os.path.isdir(os.path.join(full_path, ".claude-plugin")):
            plugin_dirs.append(full_path)

    if not plugin_dirs:
        print(f"No plugins found in {base_path}")
        print("(Looking for directories containing .claude-plugin/)")
        sys.exit(1)

    print(f"Found {len(plugin_dirs)} plugins in {base_path}\n")

    # Validate each plugin
    all_results = []
    for pd in plugin_dirs:
        all_results.append(validate_plugin(pd))

    # Print report
    errors = print_report(all_results)

    sys.exit(1 if errors > 0 else 0)


if __name__ == "__main__":
    main()
