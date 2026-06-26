# Goal: Work the parity-plus backlog — epics #706 → #704/#705 → #692

You are an autonomous engineering agent working the post-certification backlog of the
gobby-cli Cargo workspace. You work in a dedicated git worktree on your own branch
(created off `dev` for you — never leave it). Every task ends in exactly one commit.
A separate reviewer (Fable) reviews your commits by sha and sends feedback; Josh merges.
You never merge, never push.

Read these before touching code, in order:
1. `AGENTS.md` — guiding principles. Principle 14 is binding: odd code is load-bearing
   until proven otherwise. Before removing or "simplifying" anything strange, check
   `git blame` and the task ref that introduced it. Three live-breaking regressions
   (#612, #670) came from batch fixes that deleted deliberate workarounds.
2. `CLAUDE.md` — workspace layout, per-crate architecture, build/test commands, key
   constraints. All of it applies.

## Task queue

Work epics in this order. Within an epic: priority ascending (1 highest), then seq
ascending. One task at a time, one commit per task.

Full task descriptions and acceptance/validation criteria live in the Gobby task DB —
they are binding and more detailed than the titles below. Fetch each before starting:
gobby MCP → `get_task` on `gobby-tasks` (progressive discovery: `list_mcp_servers` →
`list_tools("gobby-tasks")` → `get_tool_schema` → `call_tool` with `{"task_id": "#613"}`).
If gobby MCP is unavailable, stop and report — do not guess at acceptance criteria.
If `claim_task` works in your session, claim each task before editing; never `close_task`.

### Epic #706 — gcore cleanup (do this epic FIRST — every binary depends on gcore)

- #598 (P2 bug) Expand env patterns in AiConfigSource when the standalone layer is absent
- #599 (P2 bug) Log swallowed resolve_value errors in gcore config resolution
- #601 (P2 chore) Remove test-only local-backend discovery shim from ai_context
- #602 (P2 chore) Delete unused gcore public API (CoreContext, probe_local_backend, default_backends family)
- #604 (P3 refactor) Deduplicate the keyword-DSN tokenizer shared by degradation and postgres modules
- #605 (P3 chore) Remove stale migration-era comments from project.rs, config/types.rs, and the gcore dev guide
- #606 (P3 chore) Fix stale allow(dead_code) justifications in gcore test_http
- #607 (P3 test) Add serialization tests for cli_contract and document it in the module inventory
- #608 (P3 chore) Align invalid-value handling between resolve_port and resolve_config_bool
- #610 (P3 test) Add connector-construction tests for gcore postgres TLS modes

### Epic #704 — gcode backlog (after #706)

- #613 (P1 bug) Preserve unchanged-symbol summaries across file reindex instead of delete-then-insert
- #614 (P1 bug) Make scoped codewiki runs preserve out-of-scope docs
- #615 (P2 bug) Initialize a logger or route operator-facing log calls to stderr
- #616 (P2 bug) Skip AI prose regeneration for files unchanged since the last codewiki run
- #617 (P2 bug) Reconcile stale facts for discovered files that fail AST indexing
- #618 (P2 test) Add Postgres-backed tests for code-fact upsert SQL semantics
- #619 (P2 bug) Propagate database errors in embedding/AI config resolution
- #620 (P2 refactor) Batch codewiki symbol loading instead of one query per file
- #674 (P2 bug) repo.md provenance frontmatter is pathological (637KB landing page)
- #621 (P3 chore) Replace leaked blame worker threads with cancellable blame execution
- #622 (P3 docs) Update CLAUDE.md/gcode docs to reflect standalone projection sync ownership
- #623 (P3 bug) Report actual affected-row counts from import/call upserts; deduplicate MAX_FILE_SIZE
- #700 (P3 chore) codewiki: bound or summarize Components listings on high-level module pages

### Epic #705 — gwiki backlog (after #706; may interleave with #704)

- #626 (P2 chore) Remove legacy project-vault-relative checkpoint scope-root migration from session.rs
- #627 (P2 feature) Implement AI-assisted contradiction detection in gwiki citation-quality
- #628 (P2 bug) Surface Qdrant/FalkorDB sync degradations in gwiki index output
- #675 (P2 bug) gwiki audit misattributes generated code-doc claims to unrelated raw sources
- #631 (P3 bug) Use an accurate degradation kind for unimplemented global semantic fan-out
- #632 (P3 test) Run gwiki feature-gated tests in the canonical test invocation
- #633 (P3 docs) Fix stale "sync flags for daemon" description of gwiki indexing in CLAUDE.md
- #634 (P3 refactor) Narrow gwiki lib.rs blanket dead_code allowances per issue #357
- #635 (P3 docs) Document or gate the undocumented gwiki subcommands
- #636 (P3 refactor) Consolidate gwiki vision/transcription degradation constructors
- #637 (P3 bug) Record per-section provenance links during gwiki compile
- #702 (P3 chore) gwiki ask: strip model planning narration from synthesized answers

### Epic #692 — gsqz / gloc / ghook backlog (after #706; last or interleaved)

- #638 (P1 bug) gsqz: test_failures group fabricates "All tests passed." on compile errors
- #639 (P1 bug) gsqz: pipeline matching order is alphabetical, not config-file order
- #640 (P1 docs) gsqz: README/SKILL.md document removed bare `gsqz --` invocation (exits 2)
- #650 (P1 bug) gloc: apply --url override before backend validation/detection
- #660 (P1 bug) ghook: fall back to direct daemon POST when inbox enqueue fails
- #641 (P2 bug) gsqz: malformed config file makes every wrapped command exit 1
- #642 (P2 bug) gsqz: surface nonzero exit code in content for non-empty output
- #643 (P2 chore) gsqz: git_status/git_diff group modes are unreachable dead code
- #644 (P2 test) gsqz: binary-level integration tests for the exit-0 contract and output framing
- #651 (P2 bug) gloc: stream Ollama pull progress and remove the 600s hard cap
- #653 (P2 config) gloc: update codex client defaults for the current Rust codex CLI
- #655 (P2 test) gloc: mock-server tests for Ollama lifecycle; extract main.rs resolution for testing
- #661 (P2 feature) ghook: carry an envelope/idempotency ID on the live POST for drain dedupe
- #662 (P2 bug) ghook statusline: read downstream stdout concurrently to avoid pipe deadlock
- #665 (P2 bug) ghook: consolidate Gobby-home resolution on gobby_core::gobby_home
- #666 (P2 test) ghook: binary-level integration tests for the per-CLI hook contract
- #645 (P3 bug) gsqz: warn on stderr when config regexes fail to compile
- #646 (P3 bug) gsqz: ANSI stripping misses OSC and non-CSI escape sequences
- #647 (P3 refactor) gsqz: consolidate group-by-key and head/tail-omission scaffolding in primitives
- #648 (P3 refactor) gsqz: route input-mode stats/savings through CompressionResult
- #649 (P3 planning) gsqz: resolve "layered" config docs vs first-found-wins reality; auto-export freezes defaults
- #652 (P3 bug) gloc: stop silently flooring probe_timeout_ms to 5s in ollama_check_model
- #654 (P3 feature) gloc: add explicit default_client setting instead of alphabetical-first
- #656 (P3 task) gloc: rethink first-run auto-export of built-in config
- #657 (P3 bug) gloc: distinguish unreadable config from missing; centralize exit policy
- #659 (P3 bug) gloc: env injection hygiene — unset-on-empty, unknown-placeholder warning, redact tokens in --status
- #663 (P3 bug) ghook: make emit_action EPIPE-tolerant for detached survivors
- #664 (P3 chore) ghook: remove dead sdk-py branch in detect_source
- #667 (P3 refactor) ghook: deduplicate HTTP test helper and Python-truthiness predicate
- #668 (P3 bug) ghook: fsync inbox directory after envelope rename
- #658 (P4 chore) gloc: minor cleanups — redundant model-match arm, hand-rolled dump, duplicate gcore probe tests

## Per-task workflow

1. Fetch the task (`get_task`) and read its description and validation criteria in full.
2. Read the code it touches before editing. Use `gcode search` / `gcode outline` /
   `gcode symbol <uuid>` for navigation instead of dumping whole files.
3. Implement the minimal correct change. Match surrounding style. New behavior gets tests
   in the same commit; bug fixes get a regression test that fails before the fix.
4. Run the full gate suite (below). All green before committing.
5. Commit exactly once: `[gobby-cli-#NNN] <type>: <imperative summary>` where type is one
   of feat/fix/refactor/test/docs/chore — match the existing `git log` style. Stage
   explicit paths only (`git add <paths>`), verify `git diff --cached --stat`, commit with
   `-- <paths>`.
6. Append an entry to `AGENT_LOG.md` at the worktree root (do NOT commit this file):
   task ref, commit sha, gates run, decisions made, anything skipped or uncertain.

## Gates (before every commit)

```bash
cargo fmt --all --check
cargo clippy --workspace -- -D warnings
cargo nextest run --workspace --no-default-features
cargo test --doc --workspace --no-default-features
```

For commits adding/changing test files, also run the test-quality audit:
```bash
uv run gobby test-quality audit <changed-test-file> --baseline .gobby/test-quality-baseline.json --fail-on-new --min-severity high
```

gcore commits must keep the whole workspace green, not just gobby-core — its consumers
are the test. Never weaken, skip, or `#[ignore]` an existing test to get green; if a test
contradicts your change, the task description decides who is right — when unclear, stop
and log it.

## Hard rules

- **Never push. Never merge. Never `git add -A` or `git add .`. Never rebase, squash, or
  amend any commit that already exists** — the reviewer tracks your work by sha; rewritten
  history breaks the review map. Review feedback is addressed in follow-up commits:
  `[gobby-cli-#NNN] fix(review): <summary>`.
- One task, one commit. No drive-by fixes folded into unrelated commits — if you find a
  real bug outside your task, log it in AGENT_LOG.md and move on.
- No compatibility shims or legacy fallbacks. Delete-and-replace, don't deprecate.
- No hub-schema or config_store mutation from CLI code. gcode/gwiki validate Gobby-owned
  PostgreSQL schema; they never create or migrate it.
- Stay inside your worktree. Never touch `~/.gobby/bin`, `~/.gobby/bootstrap.yaml`, the
  daemon, or the main checkout. Never restart services. Binary deployment is not your job.
- Do not modify `.gobby/wiki/**`, `.gobby/plans/**`, or `fable-repo-analysis.md`.
- No long live-LLM jobs as validation (no full `gcode codewiki` runs, no `gwiki research`
  against live models). Unit/integration gates are your validation; if a task seems to
  require live-daemon verification, implement + test hermetically and flag the live check
  in AGENT_LOG.md for the reviewer.

## Crate invariants (violating any of these is an automatic review reject)

- **gsqz exits 0 always** — the LLM reads pass/fail from content, never from exit codes.
- **ghook per-CLI hook protocol is frozen** — stdout/stderr/exit codes must match the host
  CLI contracts; enqueue-first (inbox write before daemon POST) is internal and its
  observable behavior must not change.
- **UUID5 parity** (gcode) — namespace `c0de1de0-0000-4000-8000-000000000000`, key
  `{project_id}:{file_path}:{name}:{kind}:{byte_start}`; must match the Python daemon's
  `Symbol.make_id()` exactly. There are golden-vector tests; never touch them.
- **Tiny binaries use ureq, never reqwest** (gsqz/gloc/ghook) — gcore's reqwest transport
  stays behind its `ai` feature; never pull HTTP/async deps into always-compiled gcore.
- **Config resolution order** is contract: env vars → config_store → defaults (gcode);
  built-in → global → project → CLI override (gsqz/gloc layered config).
- **Graceful degradation** — FalkorDB/Qdrant/embedding/AI endpoints fail independently;
  features degrade with explicit markers, never panic, never silently succeed.

## Task-specific notes

- #602 removes public gcore API — workspace-wide gates are mandatory; check every consumer
  crate before assuming "unused".
- #618 / #610 (Postgres-backed tests): the hub DSN comes from `~/.gobby/bootstrap.yaml`;
  follow the repo's existing pattern so these tests skip gracefully when no hub is
  reachable. They must not fail CI-style hermetic runs.
- #644 / #666 (binary-level integration tests): hermetic only — spawn the built binary
  against temp dirs and a local mock HTTP listener; never depend on the live daemon.
- #649 / #656 (decision-shaped): write the options and your recommendation into the commit
  message body and AGENT_LOG.md, implement the conservative choice, and flag it for review.
- #653: verify against the actual current codex CLI's flags/env, and cite the source of
  truth you used in the commit body.
- #622 / #633 both edit CLAUDE.md — do them as scoped, surgical edits so they don't
  conflict.
- #674, #700, #702 were filed from live failures; their descriptions contain reproduction
  context — read them fully before coding.

## When blocked

Skip the task, record why in AGENT_LOG.md (what you tried, what's missing), and move to
the next one. Never invent a workaround that violates a hard rule or crate invariant.
At the end of the queue, AGENT_LOG.md is your completion report: every task listed as
done (with sha), skipped (with reason), or blocked (with what's needed).
