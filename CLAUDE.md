# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Guiding Principles

These are enforced by hooks, rules and workflows in via the Gobby daemon.

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

A Cargo workspace with six members: five Gobby CLI binaries plus one shared foundation library.

- **gcode** (`crates/gcode/`) — AST-aware code search, symbol navigation, and dependency graph analysis. Reads/writes the Gobby PostgreSQL hub; reads FalkorDB and Qdrant when configured. External sync (embeddings, graph) is handled by the Gobby daemon.
- **gsqz** (`crates/gsqz/`) — YAML-configurable output compressor for LLM token optimization. Wraps shell commands and applies pattern-based compression pipelines.
- **gloc** (`crates/gloc/`) — Local LLM launcher. Auto-detects backends (LM Studio, Ollama), manages model lifecycle, and execs into AI CLI tools (Claude Code, Codex) with the right env vars.
- **gwiki** (`crates/gwiki/`) — Research/knowledge-vault CLI. Ingests multimodal sources (documents, PDFs, URLs, MediaWiki, git, audio/image/video) into a Markdown vault, then indexes/searches/compiles them. Shares gcode's hybrid BM25 + semantic + graph search stack.
- **ghook** (`crates/ghook/`) — Sandbox-tolerant hook dispatcher. Rust port of the Python `hook_dispatcher`; enqueues a hook envelope to `~/.gobby/hooks/inbox/` then POSTs to the daemon (enqueue-first).
- **gcore** (`crates/gcore/`) — Shared foundation library (`gobby-core`, no binary). Project discovery, bootstrap/daemon config, AI routing/context, and feature-gated datastore + search adapters consumed by the binaries above.

## Build & Test Commands

```bash
cargo build --workspace                    # Build everything
cargo build --workspace --release          # Release build (installed into ~/.gobby/bin)
cargo test --workspace                     # Test everything
cargo test -p gobby-code                   # Test gcode only
cargo test -p gobby-squeeze                # Test gsqz only
cargo test -p gobby-local                  # Test gloc only
cargo test -p gobby-wiki                   # Test gwiki only
cargo test -p gobby-hooks                  # Test ghook only
cargo test -p gobby-core                   # Test gcore only
cargo clippy --workspace -- -D warnings    # Lint all
cargo fmt --all --check                    # Check formatting
```

## Workspace Layout

```
crates/
  gcore/    — Shared foundation library (no binary; feature-gated datastore/AI adapters)
  gcode/    — Heavy binary (tree-sitter, PostgreSQL, FalkorDB, Qdrant, opt-level=3)
  gwiki/    — Heavy binary (multimodal ingest, ffmpeg/pdf, hybrid search, opt-level=3)
  gsqz/     — Tiny binary (regex pipelines, shell wrapper, opt-level="z")
  gloc/     — Tiny binary (local LLM launcher, backend detection, opt-level="z")
  ghook/    — Tiny binary (hook dispatcher, enqueue-first transport, opt-level="z")
```

Release profiles are in the root `Cargo.toml` with per-package overrides. Each binary has its own optimization level.

### Installing binaries

`cargo build --workspace --release` produces `target/release/{gcode,gwiki,gsqz,gloc,ghook}`. The deployed copies live in `~/.gobby/bin/`, each with a `.{name}-version` sidecar (and ghook additionally writes `.ghook-compatibility` on `ghook --version`). To update an installed binary, copy it over the existing one (an atomic `cp` to `<name>.new` then `mv` avoids "text file busy" if it is running) and refresh the matching `.{name}-version` sidecar.

## gcode Architecture

### Data Flow

`main.rs` parses CLI args via clap → resolves a `config::Context` (project root, PostgreSQL DSN, service configs) → dispatches to the appropriate command handler in `commands/`.

### Core Modules

- **`config`** — Resolves runtime context: `~/.gobby/bootstrap.yaml` PostgreSQL DSN → PostgreSQL `config_store` → FalkorDB/Qdrant configs. Detects project root by walking up from cwd looking for `.gobby/project.json`. Resolves `$secret:NAME` patterns via `secrets`.
- **`db`** — PostgreSQL bootstrap/keyring resolution plus read/write connection helpers. Runtime schema is validated, never created or migrated by gcode.
- **`models`** — All data types: `Symbol`, `IndexedFile`, `ContentChunk`, `SearchResult`, `GraphResult`, etc.
- **`secrets`** — Fernet decryption of Gobby secrets using `~/.gobby/machine_id` + `~/.gobby/.secret_salt` for key derivation.
- **`falkor`** — FalkorDB read client for graph queries (callers, usages, imports, blast radius). Graph writes are handled by the Gobby daemon.
- **`output`** — Output formatting (text vs JSON).

### `commands/` — CLI Command Handlers

Each subcommand maps to a function: `index::run`, `search::search`, `symbols::outline`, `graph::callers`, etc. Commands accept `&Context` and an output `Format`.

### `index/` — Indexing Pipeline

`walker` (file discovery via `ignore` crate) → `parser` (tree-sitter AST extraction per language) → `chunker` (content splitting for BM25 content search) → `hasher` (SHA-256 for incremental indexing) → `indexer` (PostgreSQL hub writes + sync flags for daemon). `languages` maps extensions to tree-sitter grammars. `security` validates paths.

### `search/` — Search Pipeline

`fts` (pg_search BM25 symbol + content search) + `semantic` (Qdrant vector search via OpenAI-compatible embedding API) + `graph_boost` (FalkorDB relevance boost) → `rrf` (Reciprocal Rank Fusion to merge ranked results).

### Graceful Degradation

FalkorDB/Qdrant/embedding API can each be unavailable independently. Graph commands return `[]` when FalkorDB is down; semantic search returns `[]` when Qdrant or the embedding API is unavailable; BM25 search works when the PostgreSQL hub is configured and indexed.

## gsqz Architecture

### Data Flow

CLI parses args → loads layered config → executes shell command → strips ANSI codes → optionally fetches daemon config overrides → matches command against pipeline regexes (first match wins) → applies step sequence → optionally reports savings to daemon → prints compressed output.

**Always exits with code 0** — intentional to prevent Claude Code from framing compressed output as an error.

### Core Modules

- **`config`** — Layered config system: built-in `config.yaml` → global (`~/.gobby/gsqz.yaml`) → project (`.gobby/gsqz.yaml`) → CLI override. Custom `Visitor` deserializer for the polymorphic `Step` enum.
- **`compressor`** — Orchestrator that compiles pipeline regexes, matches commands, applies steps, and enforces thresholds (min output length, max compressed lines, 95% savings threshold).
- **`daemon`** — Feature-gated (`#[cfg(feature = "gobby")]`) HTTP integration with the gobby daemon for runtime config overrides and savings reporting. All HTTP calls are fire-and-forget with 1s timeouts.
- **`primitives/`** — Four composable operations on line collections: `filter`, `group` (8 modes), `dedup`, `truncate`.

## gloc Architecture

### Data Flow

CLI parses args → loads layered config → auto-detects backend (probes LM Studio then Ollama in config order) → resolves client and model (with alias lookup) → ensures model readiness (Ollama: check/pull/warmup; LM Studio: no-op JIT) → sets env vars from client template → `exec`s into client binary.

### Core Modules

- **`config`** — Layered config system (same pattern as gsqz): built-in `config.yaml` → global (`~/.gobby/gloc.yaml`) → project (`.gobby/gloc.yaml`) → CLI override. Template variable resolution (`{backend.url}`, `{backend.auth_token}`, `{backend.name}`, `{model}`).
- **`backend`** — Backend probing via HTTP GET, Ollama model lifecycle management (check via `/api/tags`, pull via `/api/pull`, warmup via `/api/generate`). LM Studio uses JIT loading (no explicit management needed).
- **`exec`** — Env var injection from client config templates, argument building, and `exec()` into the client binary (replaces process via `CommandExt::exec()`).

## gwiki Architecture

### Data Flow

`main.rs` parses CLI args via clap → resolves a gwiki `Context` (project root, vault path, PostgreSQL hub, AI routing) → dispatches to a handler in `commands/`. Ingest path: `ingest/file.rs` routes a source by type → modality orchestrator (`ingest/{document,pdf,url,mediawiki,git,wayback,audio,image,video}.rs`) → derived Markdown written into the vault with frontmatter/provenance → `indexer` writes the Gobby hub + sync flags for the daemon.

### Core Modules

- **`ingest/`** — Per-source ingestion. `file` routes by extension/type; `document`/`pdf`/`url`/`mediawiki`/`git`/`wayback` handle text-bearing sources; `audio`/`image`/`video` are the multimodal orchestrators (transcription/translation, vision, frame extraction).
- **`ai/`** — AI clients (`clients`), chunking (`chunk`), and translation (`translate`), routed through `gobby_core` AI transport. `transcribe.rs`/`vision.rs`/`video.rs` define the modality client traits and degradation vocabulary.
- **`search/`** — Same hybrid stack as gcode: `bm25` + `semantic` (Qdrant) + `graph_boost` (FalkorDB) merged via `rrf`.
- **`commands/`** — One handler per subcommand: `init`, `setup`, `collect`, `index`, `compile`, `export`, `search`, `read`, `backlinks`, `sources`, `status`, `health`, `audit`, `lint`, `research`.
- **`vault`/`document`/`frontmatter`/`provenance`/`citations`/`credibility`** — The Markdown vault model: documents, frontmatter, source provenance, and citation/credibility tracking.

### Graceful Degradation

Multimodal endpoints (transcription, vision) and the AI transport degrade independently — ingest falls back to skeleton/derived output with explicit degradation markers when a capability is routed off or unavailable. Search degrades exactly like gcode (BM25 standalone; semantic/graph optional).

## ghook Architecture

### Data Flow & Modes

`ghook --gobby-owned --cli=<c> --type=<t> [--critical] [--detach]` builds a hook `Envelope`, enqueues it to `~/.gobby/hooks/inbox/`, then attempts a POST to the daemon (`transport`). Enqueue-first means the hook is durable even if the daemon is down; stdout/stderr/exit codes mirror the legacy Python `hook_dispatcher.py` contract. `--diagnose` prints JSON diagnostics with no network/envelope write. `--version` prints the version and writes `~/.gobby/bin/.ghook-compatibility` (`{schema_version, ghook_version}`).

### Core Modules

- **`envelope`** — Hook payload built from stdin JSON + cli/type/flags.
- **`transport`** — Inbox enqueue + best-effort daemon POST.
- **`detach`** / **`planned_shutdown`** — Background detach and clean-shutdown handling.
- **`cli_config`** / **`statusline`** / **`terminal_context`** / **`diagnose`** — Per-CLI config, status line emission, terminal context capture, and diagnostics.

## gcore Architecture

Shared foundation library (`gobby-core`), kept dependency-light so small binaries do not inherit services they never call. Always-compiled modules are split from feature-gated adapters.

### Always-compiled modules

- **`bootstrap`** / **`daemon_url`** / **`project`** / **`provisioning`** — `~/.gobby/bootstrap.yaml` parsing, daemon URL resolution, project-root discovery (`.gobby/project.json`), and provisioning helpers.
- **`config`** / **`context`** / **`setup`** — Shared config types and runtime context resolution reused across binaries.
- **`ai_context`** — AI config types, `AiContext` resolution, per-capability **routing decision** (daemon / direct / off), and an always-compiled concurrency limiter.
- **`ai_types`** — Pure AI result/error data types (no transport deps), kept separate from `ai_context`.
- **`degradation`** / **`local_backend`** — Shared degradation vocabulary and local-LLM backend descriptors.

### Feature-gated adapters

`ai` (HTTP transport via `reqwest`), `postgres`, `falkor`, `qdrant`, `indexing`, `search` — each behind its own Cargo feature so a consumer pulls in only the datastores/transport it uses. Local backend descriptors are always available from `gobby_core::local_backend`.

## Key Constraints

- **UUID5 parity with Python** (gcode): Symbol IDs are deterministic UUID5 using namespace `c0de1de0-0000-4000-8000-000000000000` and key format `{project_id}:{file_path}:{name}:{kind}:{byte_start}`. Must match the Python daemon's `Symbol.make_id()` exactly.
- **Config resolution order** (gcode): env vars (`GOBBY_FALKORDB_HOST`, `GOBBY_FALKORDB_PORT`, `GOBBY_FALKORDB_PASSWORD`, etc.) → `config_store` table → hardcoded defaults.
- **Tree-sitter grammars** (gcode): Tier 1 (Python/JS/TS/Go/Rust/Java/C/C++/C#/Ruby/PHP/Swift/Kotlin), Tier 2 (Dart/Elixir), Tier 3 (JSON/YAML). Markdown is indexed as content-only repo text, outside tree-sitter AST detection. Adding an AST language requires a new `tree-sitter-*` dep in `crates/gcode/Cargo.toml` and a grammar entry in `index/languages`.
- **Non-destructive to Gobby hub schema** (gcode): Validate existing Gobby-owned PostgreSQL tables and BM25 indexes. Never alter `project.json`, `config_store`, or Gobby-managed schema.
- **Exit code 0** (gsqz): Always exit 0 regardless of subprocess exit code. The LLM reads pass/fail from content.
- **Python dispatcher contract** (ghook): stdout, stderr, and exit codes must match the legacy Python `hook_dispatcher.py`. Enqueue-first (inbox write before daemon POST) is an internal detail and must not change the observable contract.
- **AI ownership split** (gcore): AI config types, `AiContext` resolution, the per-capability routing decision, and the concurrency limiter live in `gobby_core::ai_context` (always-compiled, no `reqwest`); pure result/error data types live in `gobby_core::ai_types` (always-compiled); HTTP transport lives behind the `ai` feature in `gobby_core::ai`. Keep these layers separate — don't pull `reqwest` into the always-compiled modules.
