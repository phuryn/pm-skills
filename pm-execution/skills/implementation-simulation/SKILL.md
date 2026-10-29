---
name: implementation-simulation
description: "Dry-run building a PRD, epic, or user stories with a panel of developer personas and a separate skeptic pass. Returns a Pre-Handoff Simulation Report with a punch list. Use when preparing an engineering handoff, checking build readiness, or asking what developers will get stuck on."
---

# Implementation Simulation: Find the Blockers Before Developers Do

## Purpose

You are a tech lead running a dry run of the build before a spec goes to engineering. A panel of developer personas, called seats, mentally builds the PRD, epic, or stories and logs only the friction that would stop a developer or force a silent guess.

## Context

A red-team asks whether the bet is right. A pre-mortem asks how the launch could fail. This skill assumes both and asks one question: can engineers build this as written without stopping to ask or silently guessing?

The altitude is build decisions and contracts, not code. It prepares engineering review; it does not replace it. Run it after the PRD, epic, and stories are drafted, before refinement or sprint planning.

## Instructions

1. **Read the whole spec.** If there is only an idea, say so and offer to draft the PRD or stories first.

2. **Decompose into build units.** Split the spec into build units: endpoints, data model changes, screens and states, integration calls, background jobs, state transitions, and migrations. Tag each unit with the seats it touches.

3. **Run the seats one at a time.** Each seat owns one area, asks what a developer in that seat would ask while building its units, and ignores the rest:
   - **Backend:** APIs and contracts, data model, state machines, idempotency, concurrency, partial failure and retry, migrations.
   - **Frontend and mobile:** every screen state (empty, loading, error, offline, pending, partial), validation, accessibility, error copy, perceived latency.
   - **Integrations:** third-party APIs and webhooks: auth, field mapping, rate limits, timeouts, retries, sandbox vs production, vendor failure modes.
   - **Data and analytics:** event and metric definitions, reporting, backfills, existing-data migration, retention, PII in logs.
   - **Security and privacy:** authentication and authorization, roles and permissions, abuse and fraud vectors, PII handling, audit trail, compliance hooks.
   - **QA and release:** edge cases, race conditions, double submit, test data, feature flags and rollout, rollback, observability and alerts, regression surface.

   Skip any seat that no build unit touches, and list only the seats that ran. A seat logs a finding only when a developer would have to stop and ask, silently guess, handle an unmentioned state or edge case, or make an integration call with a missing contract detail. No nits, no praise, no restating the spec. Empty is a valid answer; never manufacture findings.

4. **Record each finding** with: id; type (blocker, silent_assumption, missing_requirement, integration_gap); spec_ref (quote the sentence or name the missing section); what_is_unclear; decision_needed; options; recommended_default; severity (high, medium, low); confidence (spec_gap when the text proves it, verify_with_engineering when you suspect a conflict with the existing system, never asserted as fact); owner (PM, Engineering, Design, External, Legal).

5. **Run a separate skeptic pass.** After all seats finish, switch roles. The skeptic is independent and adversarial: it re-reads the spec from scratch and sorts every finding into **dev_blocker** (real, and it blocks building the specified work), **scope_question** (a real gap that is a PM scope or planning call, such as an unscoped surface, a deferred capability, or a missing story), or **noise** (already answered, cite where; speculation; a nit). Default to noise when uncertain. The skeptic may adjust severity and owner.

6. **Write the report.** Merge a finding raised by several seats into one item and name the seats; overlap signals importance. Group dev blockers by type. Mark verify_with_engineering items "Verify with engineering, not confirmed". Save as `Pre-Handoff-Simulation-[spec-name]-[date].md`:

   ```
   # Pre-Handoff Simulation Report: [spec name]
   Date: [date] | Seats run: [list]

   ## Summary
   Dev blockers by severity, scope question count, the single biggest risk

   ## Blockers (resolve before handoff)
   ## Silent assumptions to confirm
   ## Missing requirements (states and edge cases)
   ## Integration gaps
   [Per item: spec_ref, what is unclear, decision needed, options,
   recommended default, severity, confidence, owner, seats]

   ## Scope questions for the PM (not dev blockers)
   [Items with owners, or "None surfaced."]

   ## Dropped as noise
   [One line each, with the reason]

   ## Punch list (dev blockers only)
   | Item | Owner | Recommended default | Severity |
   ```

## Notes

- A finding without a spec_ref is noise.
- Seats run in sequence in one context, then the skeptic. If delegation is available, the seats may run in parallel; the skeptic still runs after them, on its own.
- An empty report is a good result: say the spec is ready to hand off.
- Scope questions never count as blockers; they are planning calls, not spec defects.
