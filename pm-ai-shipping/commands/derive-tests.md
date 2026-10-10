---
description: Turn documented intent into a test-coverage map — inventory the tests that exist today, derive use-case cases from the system docs, separate existing coverage from proposed tests and unverified gaps, mark each unit / guarded-live / manual, and recommend a gate that follows the repo's stated gate policy (a green-before-merge CI gate where it states none). `check` mode writes nothing and reports where the coverage map is stale against the docs and the test suite
argument-hint: "[check] <repo path or area; defaults to the whole repository>"
---

# /derive-tests -- Turn Intent Into Tests

The docs say what the system *should* do. An audit finds where the code *doesn't*. Tests are what stop that gap from reopening after the next AI edit. This command reads the documented intent, turns each load-bearing rule into a concrete test case, sorts them into what to automate, what needs a guarded live run, and what stays manual — then recommends the gate that keeps `main` honest: the one the repo's own instructions define, or a green-before-merge CI gate where they define none.

This produces a coverage map (`tests.md`) and concrete test cases, not a finished suite — you or the next agent implement the deterministic ones. If the repo already keeps a test-coverage file, under any name, that file is the map: update it rather than starting a second one (the **shipping-artifacts** skill's *Locations and names* rule).

## Invocation

```
/derive-tests
/derive-tests the checkout flow
/derive-tests supabase/functions
/derive-tests check
/derive-tests check the checkout flow
```

A first argument of `check` runs **check-only mode** (below) on the scope that follows it, instead of the workflow.

## Prerequisite: documented intent

Tests are derived from the docs, so the docs come first. If the system docs (in the repo's docs location, or `documentation/` by default) are missing or thin, run `/document-app` (and `/derive-tests` reads `flows.md`, `permissions.md`, and `automation.md` most heavily). You cannot map coverage to rules you never wrote down — where intent is absent, say so rather than inventing rules to test.

## The workflow

### 1. Read the intent — and the tests that already exist

Read the applicable system docs (architecture, flows, permissions, variables, and any of emails, cron, seo, automation that exist). Apply the **shipping-artifacts** skill for what each doc should contain, and the **intended-vs-implemented** skill for the discipline of treating docs as claims to verify, not proof.

Then inventory the **existing test suite** — the test files, what they actually assert, and what runs in CI today. The map you produce must distinguish coverage that exists *now* from coverage you're *proposing*; skipping this step yields a falsely-green map that claims rules are pinned when nothing checks them. If there are no tests, say so plainly — that is itself a finding.

### 2. Extract the rules worth testing

Pull out the load-bearing, deterministic rules — the ones whose violation crosses a trust, data, money, tenant, or privacy boundary:

- authorization allow **and deny** cases (especially the boundary crossings in `flows.md` and the matrix in `permissions.md`),
- input validation and output encoding at each sink,
- idempotency of jobs and dedup keys,
- fail-closed defaults (error / timeout / cache-miss / flag paths that must deny, not allow),
- side-effect conditions (exactly when an email sends, a write commits, a paid action fires),
- public-data-only constraints on public or bot routes,
- the output-contract and tool-surface limits of any agent in `automation.md`.

Skip cosmetic behavior. A rule earns a test when getting it wrong harms someone other than the actor.

### 3. Build the coverage map

One row per use case: **rule → expected behavior (incl. the negative case) → evidence source (doc + code) → test type → status (existing / proposed / none)**. The status column is what keeps the map honest — mark a rule *existing* only when a test in the repo actually asserts it today.

Test types:

- **unit** — pure and deterministic, no external services.
- **integration (deterministic)** — exercises real wiring against a local or in-memory dependency (test DB, mocked provider) and runs the same way every time.
- **guarded live** — needs a real external DB, email provider, LLM, or third party. Runs only behind an explicit flag, never in the default gate run.
- **manual** — UI/visual or judgment calls. A reviewer checklist item, not an automated test.

**What the gate must require** (hosted CI, or whatever gate the repo runs): the deterministic local set — unit plus deterministic integration tests, the ones that pass or fail the same way on every run with no live dependencies. Prefer **unit** where the decision logic can be isolated; reach for **integration** when the rule lives in the wiring (middleware, RLS, auth guards) and only a real-but-local dependency can exercise it. Guarded-live and manual rows never gate the default run.

When a rule can only be exercised live, you can extract its *decision* into a pure helper so the logic is unit-testable — but only as a **complement, not a replacement** for testing the real enforcement. The unit test proves the helper's logic; it does **not** prove the framework actually calls it. Wiring and policy enforcement (route middleware, DB row-level security, auth guards, provider config) still needs an integration or guarded-live check, or the helper becomes a policy shadow that passes while the real path is unprotected.

### 4. Propose the tests

For each rule you can pin with a deterministic automated test (unit or integration), write the case: name, arrange/act/assert intent, and the negative case it must reject. Group cases by the doc or flow they defend. Prefer the smallest test that pins the rule — one clear assertion per boundary beats a sprawling integration test that fails for ten reasons.

### 5. Recommend the gate

Start from the repo's stated gate policy. Its agent instructions, contributing guide or release docs may already say what gates a merge or a release — a local command plus a human go, a hosted CI workflow, something else. Where they do, that policy is the gate: record it in the coverage map with its source, check that the deterministic set runs inside it, and don't recommend hosted CI or branch protection over it. If the deterministic set does not run inside that gate, say so as a finding for the owner rather than proposing a different gate.

Where the repo states no policy, recommend — don't silently install — a CI setup matched to the repo's stack and existing tooling:

- run the **deterministic local set on every pull request** (unit + any integration test that runs without live services),
- keep **guarded-live tests opt-in** (manual or scheduled, never blocking),
- **gate merges to `main` on green** via a required status check + branch protection.

Output the workflow file and the branch-protection setting as a clearly-labeled suggestion for the user to approve, not an applied change.

### 6. Report coverage and gaps

Write `tests.md` in three clearly separated sections:

- **Existing coverage** — rules a test in the repo pins *today* (from the Step 1 inventory).
- **Proposed tests** — the cases you're recommending but that don't exist yet, by type.
- **Gaps** — documented rules with **no verification at all**, ranked by what crossing them exposes.

The gaps are the backlog, and they are exactly where the next AI edit can silently break a boundary. Be honest that proposed ≠ existing: a rule isn't covered until a test actually asserts it.

## Check-only mode

For a repo whose coverage map is kept by hand, or by whoever runs the gate, so a release can confirm the map is current without this command rewriting it. **Write no file**: not the map, not a report. Read the tests; don't run them. Don't run `/document-app` when the docs are thin; list them under *Not checked*.

1. Find the coverage map the way the workflow does (the **shipping-artifacts** skill's *Locations and names* rule). If there is none, say so and stop.
2. Compare it, row by row, against the system docs and the test suite. It is stale where:
   - a documented rule has no row, or a row cites a rule the docs no longer state or now state differently;
   - a row marked existing names a test that is gone or doesn't assert the rule;
   - a test pins a rule the map marks proposed or none;
   - a cited path, test name or gate command no longer matches the tree.
3. Don't decide which side is wrong. The map may be behind, or a doc or test may have drifted from what the map records; that is the owner's call.

Output, printed in the conversation:

```
Coverage check: [scope] — check-only, no files written

### Stale entries
1. [rule or row]
   - Map says: [entry] — `[map path]:[line]`
   - Docs or tests say: [what they state or assert] — `[path]:[line]`
   - Owner decides: fix the map, the doc, or the test.

### Not checked
- [thin or absent docs, tests whose assertion couldn't be read, areas out of scope]

### Summary
Coverage check, [date], commit [short SHA], scope [scope]: [N] map rows read, [N] stale entries, [N] not checked. Tests read, not run. No files written. Which side to fix is the owner's call.
```

An empty *Stale entries* section says what was read to reach it. Then stop: don't offer to rewrite the map.

## Output

```
Test Coverage: [scope]

| Use case | Rule (doc) | Expected behavior (+ deny case) | Evidence | Type | Status |
|----------|-----------|---------------------------------|----------|------|--------|
[status: existing / proposed / none]

### Existing coverage
[tests already in the repo, each tied to the rule it pins]

### Proposed tests
[grouped by flow/doc — name · assert · negative case · type]

### Gate
[the repo's stated gate policy, with its source, and whether the deterministic set runs inside it — or, where it states none, a workflow snippet for the detected stack + "green-before-merge" branch-protection note]

### Gaps — documented but unverified
[rules with no test yet, ranked by what crossing them exposes]
```

Write the coverage map to the repo's existing coverage file, or `documentation/tests.md` if it has none, and the full report to the repo's reports location, or `reports/test_plan_{timestamp}.md` if it has none. Give the user both paths, and say which are plugin defaults.

## Notes

- This is the verification half of "documented == implemented": the audits find today's gap, these tests stop it from reopening tomorrow.
- Don't fabricate rules to manufacture coverage. If the docs are silent, the gap is in the docs — fix `/document-app` first.
- Don't wire external services into the default gate run, whatever the gate is; flaky live tests erode it until people start ignoring it.
- Covers test derivation only. For the gap audit itself use `/security-audit-static`; for the full document → audit → test → packet sequence use `/ship-check`.
