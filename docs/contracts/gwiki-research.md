# gwiki Research Contract

`gwiki research` adds to or audits a wiki scope. It is a mutating command with
its own reason-act loop. It must run without the Gobby daemon, and Gobby may
enhance it through AI routing, cron, pipelines, or review agents.

This contract replaces the old daemon agent-spawn shape. `gwiki research` must
not call `/api/agents/spawn`, and the CLI surface must not expose
`--task-id`, `--agent-count`, or `--resume` as daemon-dispatch controls.
Checkpoint/session storage remains owned by `crates/gwiki/src/session.rs`, and
`gwiki compile` keeps consuming accepted research notes from that session model.

## Command Shape

The v1 research surface is:

```text
gwiki [--project <ROOT> | --topic <NAME>] [--format json|text] research [QUESTION]
    [--audit]
    [--source-constraint <TEXT>]...
    [--max-steps <N>]
    [--max-tokens <N>]
    [--max-sources <N>]
    [--ai auto|daemon|direct|off]
    [--require-ai]
```

Scope follows the shared gwiki scope contract: `--topic` wins over
`--project <ROOT>`, bare `--project` means the current directory, and no scope
flag detects the project from cwd. JSON output carries the resolved `scope`
identity.

`QUESTION` is required for enrichment mode and optional for `--audit`. If
omitted with `--audit`, the audit prompt is derived from wiki health, stale
pages, uncited claims, broken source references, and configured source
constraints.

`--ai off` is invalid for enrichment mode because research needs a model to
plan and synthesize notes. `--ai off --audit` is valid only for deterministic
audit checks and must return `ai_unavailable` for any finding that needs model
judgment. `--require-ai` makes AI unavailability fail before mutation.

## Reason-Act Loop

The loop runs inside gwiki:

1. Build a research state from the resolved scope, the checkpoint, wiki index
   metadata, source constraints, and command budgets.
2. Ask the model for the next action using the gcore AI route.
3. Execute one allowed action.
4. Validate outputs, update the checkpoint, and append an event.
5. Stop when a termination rule fires.

Allowed actions are deliberately small:

- `ask(query)`: call the read-only `gwiki ask` retrieval path.
- `search(query)`: call the read-only wiki search path.
- `read(path)`: read an in-scope wiki page or raw source note.
- `ingest_url(url)`: ingest a URL through gwiki's ingestion pipeline.
- `ingest_file(path)`: ingest an explicit local file inside the allowed scope.
- `accept_note(title, body, sources)`: write a research note under
  `raw/research/`.
- `record_gap(reason, evidence)`: checkpoint an unresolved or rejected claim.
- `finish(reason)`: terminate successfully.

No action may write final article pages directly. Research produces accepted
notes and audit findings; `gwiki compile` remains the article-generation step.

## Budgets

Defaults are conservative and must be visible in JSON output:

- `max_steps`: 12
- `max_tokens`: 24000 total model output and tool-observation budget
- `max_sources`: 8 newly ingested external sources
- `max_wall_time_seconds`: 900
- `max_note_bytes`: 24000 per accepted note

The implementation may add lower internal per-call caps, but it must never
exceed the command budget. A budget stop is a successful partial run when at
least one note, finding, or gap was recorded; otherwise it is `no_progress`.

## Termination Rules

The run must stop on the first matching rule:

- `finish`: model requested `finish(reason)` after validation.
- `budget_exhausted`: step, token, source, note-size, or wall-time cap reached.
- `no_progress`: three consecutive steps produced no new accepted note, source,
  finding, or gap.
- `duplicate_frontier`: three consecutive planned actions repeat an already
  observed query, URL, or source path without new evidence.
- `source_blocked`: all remaining proposed claims lack acceptable provenance.
- `write_conflict`: a concurrent writer changed the target note after draft
  validation and before commit.
- `ai_unavailable`: selected AI route could not produce a plan and fallback is
  not allowed.

Every stop emits `status`, `stop_reason`, `steps_used`, `tokens_used`,
`sources_added`, and `changed_paths`.

## Write-Conflict Behavior

All research writes go through a vault-scoped lock:

- Notes are staged as temp siblings and renamed atomically.
- Existing accepted notes are idempotent by stable draft id.
- New title collisions use numeric suffixes.
- Raw research index updates happen under the existing index lock.
- If a target note changed since draft validation, the run records
  `write_conflict`, writes no partial note body, and exits without overwriting.

`gwiki research` must tolerate another process ingesting or indexing the same
vault while it runs. It may retry reads after index staleness, but it must not
stack multiple writers for the same accepted note.

## Source Provenance

Every accepted claim must cite a source. Accepted notes use frontmatter plus
inline source references:

- `research_session_id`
- `research_question`
- `accepted_at`
- `sources`: list of canonical URLs or vault-relative source paths
- `source_hashes`: optional content hashes when gwiki has them
- `claims`: list of claim ids mapped to source ids

Validation rejects an accepted note when:

- a factual claim has no source id,
- a source id is missing from frontmatter,
- a source path is outside the resolved scope,
- a URL was not ingested or recorded as intentionally external,
- a quoted passage has no location metadata when location is available.

The model may suggest unsupported claims, but unsupported claims become gaps,
not accepted notes.

## Audit Mode

`gwiki research --audit` inspects existing wiki content and writes findings. It
does not compile final pages.

Audit flags:

- uncited factual claims,
- source links that no longer resolve through gwiki source metadata,
- stale pages whose source material changed since the last accepted note or
  compile state,
- contradictory accepted notes for the same scope,
- orphaned raw research notes that were never compiled or rejected,
- pages with source provenance outside the resolved scope,
- duplicate source ingestion records for the same canonical source.

Audit may update checkpoint metadata and write `raw/research/audit-*.md`
finding notes. It may not edit article pages directly. A finding note must
include severity, evidence, source references, suggested remediation, and
validation status.

Acceptance criteria for audit implementation:

- deterministic checks pass with `--ai off`,
- model-assisted checks are skipped with an `ai_unavailable` warning when AI is
  unavailable and `--require-ai` is false,
- no finding is emitted without at least one concrete page, note, source record,
  or retrieval hit as evidence,
- repeated audit runs are idempotent by finding fingerprint,
- JSON output lists `findings`, `warnings`, `changed_paths`, and
  `stop_reason`.

## Gobby Enhancer Boundary

Gobby integrates with this command from outside gwiki:

- `--ai daemon` routes model calls through the Gobby daemon frontier.
- Cron schedules deliberate research jobs, including nightly enrichment and a
  pre-release vault audit.
- Pipelines may invoke `gwiki research --audit` as a build stage.
- A Gobby agent may review the resulting notes or findings after the command
  exits.

The CLI must not spawn or kill Gobby agents directly. Gobby owns fleet
management; gwiki owns wiki mutation and provenance.

The old blind six-hour research timer should be retired in favor of explicit
cron jobs configured per project/scope.

## JSON Output

The JSON result contains:

```json
{
  "command": "research",
  "scope": {"kind": "project", "id": "/repo"},
  "query": "question or derived audit question",
  "audit": false,
  "status": "ok",
  "stop_reason": "finish",
  "steps_used": 4,
  "tokens_used": 3200,
  "sources_added": [],
  "accepted_notes": [],
  "findings": [],
  "gaps": [],
  "warnings": [],
  "changed_paths": [],
  "session_id": "research-..."
}
```

Text output is a human summary of the same data. Daemon-facing code consumes
JSON only.

## Implementation Order

1. Add the new CLI flags and contract JSON while keeping `session.rs` and
   `compile` tests green.
2. Delete `GobbyDaemonResearchDispatcher` and daemon-dispatch options.
3. Extract a `ResearchLoop` module with injected model, wiki search, ask, read,
   ingest, and note writer traits.
4. Implement deterministic audit checks first.
5. Add model-planned enrichment with source validation.
6. Add Gobby daemon route/gateway support for `--ai daemon` and scheduled audit
   jobs.
