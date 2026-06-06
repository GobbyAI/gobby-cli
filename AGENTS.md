# AGENTS.md — Guide for AI Agents

This file is for AI coding agents (Claude, Copilot, Cursor, etc.) working on the gobby-code codebase. It supplements CLAUDE.md with constraints and patterns that prevent common mistakes.

# Guiding Principles

These are enforced by hooks, rules and workflows in via the Gobby daemon.

Maintainer note: this section is the canonical source for agent rules. Update it here and link to it from other root instruction files instead of duplicating the list.

1. **ALWAYS use progressive tool discovery.** Do not try to call one step through another (e.g., don't use call_tool to invoke get_tool_schema).
2. **NEVER create or leave monoliths.** Keep code files under 1,000 lines. For code files, you *MUST* search for an existing refactor task or create it if one does not already exist in gobby-tasks. Leave these tasks for another agent to pick up. Markdown files, including `docs/guides/*.md` and repo-root instruction files, are documentation artifacts and are not subject to this 1,000-line source-file rule; do not create refactor tasks or block docs work based only on Markdown line count.
3. **ALWAYS create or claim a task before editing a file.** This applies to file edits only — no task needed for plan mode, research, investigation, or answering questions unless the user explicitly requests one.
4. **Validation runs when closing with a commit. If a commit is done, validation must run.** `skip_validation` is silently stripped when commits are attached.
5. **NEVER close a task without a commit if there are diffs.** If you changed something, you have to commit it.
6. **NEVER stop while you have a claimed task in progress.** Your stop hook is blocked while you have a claimed task. Task must be closed before stopping. If you claim a task, you finish a task.
7. **Escalate only when the user explicitly needs to review your work, your agent skill/workflow/pipeline directs escalation, or you are genuinely stuck and need guidance.** Do not use escalation as a workaround for committing, closing, or completing required validation.
8. **You found it, you own it.** Every error, test failure, lint warning, or type error you encounter is yours to fix — even if it's pre-existing, even if it's unrelated to your task. Fix it before closing your task. The only exception is something that genuinely requires multi-session architectural planning; even then, investigate thoroughly and attempt the fix before filing a task to defer it.
9. **ALWAYS use gobby-memory to record valuable memories.** You have access to a sophisticated memory system via gobby-memory through the MCP proxy. Use it to store and retrieve facts about the codebase, design decisions, and other relevant information.
10. **NEVER be a sycophant.** Do not agree with the user just for the sake of agreement. If you disagree with the user, you *MUST* voice your concerns and provide alternative solutions.
11. **NEVER leave options or unanswered questions in plans.** Plans are for execution, not exploration. If there are unanswered questions or ideas that need to be explored, explore them before finalizing the plan.
12. **ALWAYS choose/present the best approach to solve a problem. The best, most correct fix is *ALWAYS* in scope. NEVER choose or present the simplest approach if it is not the best or most complete/correct approach.**
13. **ALWAYS prefer gcode over grep/rg/sed/awk/nl.** gcode is an advanced code index/graph tool and is *FAR* superior to grep/rg/sed/awk/nl for code search and analysis.

## What This Is

`gobby-code` is a Rust CLI (`gcode`) that provides AST-aware code search, symbol navigation, and dependency graph analysis. It reads/writes the Gobby PostgreSQL hub for symbols/search, FalkorDB for call graphs, and Qdrant for semantic vectors. It works without the Gobby daemon process, but requires a migrated PostgreSQL hub bootstrap.

## Build & Test

```bash
cargo build --workspace --no-default-features       # CI-compatible build
cargo nextest run --workspace --no-default-features # Run non-doctest tests
cargo test --doc --workspace --no-default-features  # Run doctests
cargo clippy --workspace --no-default-features -- -D warnings  # Lint (must be zero warnings)
```

CI builds use `--no-default-features`.

## Architecture

```text
main.rs (clap CLI)
  → config::Context::resolve()     # Resolves project root, PostgreSQL DSN, service configs
  → commands/*::run()              # Command handler
    → db::connect_readwrite/readonly # PostgreSQL hub connection
    → index/*                      # Indexing pipeline (walker → parser → chunker → indexer)
    → search/*                     # Search pipeline (fts + semantic + graph_boost → rrf)
    → falkor::*                     # Graph queries via FalkorDB
```

## Critical Constraints

### 1. Non-destructive to Gobby databases

gcode must treat Gobby-owned hub schema as externally managed. Never:
- Write to `.gobby/project.json` (that's Gobby's file)
- CREATE, ALTER, or DROP tables that Gobby created
- Modify the `config_store` table

The schema module (`src/schema.rs`) only validates required PostgreSQL tables, the `pg_search` extension, and BM25 indexes. It must not create or migrate schema.

### 2. UUID5 parity with Python

Symbol IDs are deterministic UUID5 using:
- Namespace: `c0de1de0-0000-4000-8000-000000000000`
- Key: `{project_id}:{file_path}:{name}:{kind}:{byte_start}`

These must match the Python daemon's `Symbol.make_id()` exactly. See `src/models.rs`.

### 3. Config resolution order

Infrastructure and hub-connection config stays env-first: env vars (`GOBBY_FALKORDB_HOST`, `GOBBY_FALKORDB_PORT`, `GOBBY_FALKORDB_PASSWORD`, PostgreSQL DSN, etc.) → `config_store` table → hardcoded defaults. Don't short-circuit those paths.

AI capability config is the carve-out: `ai.*` keys resolve from `config_store` → standalone `~/.gobby/gcore.yaml` → defaults, with no `GOBBY_*` env-var layer. CLI flags may still override for a single invocation.

### 4. Do NOT run `gcode invalidate`

`invalidate` destroys the project's code index and requires interactive confirmation. It exists for human use only. Use `gcode index` for incremental re-indexing instead.

## Common Tasks

### Add a new CLI command

1. Add variant to `Command` enum in `src/main.rs`
2. Add handler in `src/commands/*.rs`
3. Wire dispatch in `main()` — commands that work on uninitialized projects go in the early-dispatch block before `Context::resolve()`

### Add a language

1. Add `tree-sitter-<lang>` to `Cargo.toml`
2. Map extensions in `src/index/languages.rs`
3. Add query patterns in `src/index/parser.rs` if needed

### Modify search ranking

Search uses Reciprocal Rank Fusion in `src/search/rrf.rs` to merge results from:
- `src/search/fts.rs` — pg_search BM25 symbol and content search
- `src/vector/code_symbols.rs` — Qdrant vector similarity
- `src/search/graph_boost.rs` — FalkorDB graph relevance

### Modify the indexing pipeline

The pipeline in `src/index/indexer.rs` orchestrates:
- `walker.rs` — file discovery
- `parser.rs` — tree-sitter AST extraction
- `chunker.rs` — content splitting for pg_search BM25 content search
- `hasher.rs` — SHA-256 for incremental detection

## What NOT to Do

- Don't modify Gobby-owned tables or files (see constraint #1)
- Don't change UUID5 generation without verifying Python parity
- Don't add `println!` for user output — use `eprintln!` for status, and `output::print_json` / `output::print_text` for command results
- Don't skip the `--no-default-features` test pass — CI runs both configurations
- Don't assume FalkorDB or Qdrant are available — all code must handle `None` configs gracefully
