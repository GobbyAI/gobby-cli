# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Guiding Principles

See [AGENTS.md](AGENTS.md#guiding-principles) for the canonical agent rules enforced by Gobby hooks and workflows.

## What This Is

A Cargo workspace with four members: three Gobby CLI binaries plus one shared foundation library.

- **gcode** (`crates/gcode/`) — AST-aware code search, symbol navigation, and dependency graph analysis. Reads/writes the Gobby PostgreSQL hub and owns code graph/vector projection writes into FalkorDB and Qdrant when those services are configured. The Gobby daemon may trigger or schedule indexing/sync work, but Rust owns code projection mutation.
- **gwiki** (`crates/gwiki/`) — Research/knowledge-vault CLI. Ingests multimodal sources (documents, PDFs, URLs, MediaWiki, git, audio/image/video) into a Markdown vault, then indexes/searches/compiles them. Shares gcode's hybrid BM25 + semantic + graph search stack.
- **ghook** (`crates/ghook/`) — Sandbox-tolerant hook dispatcher. Rust port of the Python `hook_dispatcher`; enqueues a hook envelope to `~/.gobby/hooks/inbox/` then POSTs to the daemon (enqueue-first).
- **gcore** (`crates/gcore/`) — Shared foundation library (`gobby-core`, no binary). Project discovery, bootstrap/daemon config, AI routing/context, and feature-gated datastore + search adapters consumed by the binaries above.

## Build & Test Commands

```bash
cargo build --workspace                    # Build everything
cargo build --workspace --release          # Release build (installed into ~/.gobby/bin)
cargo nextest run --workspace              # Test everything except doctests
cargo test --doc --workspace               # Test doctests
cargo nextest run -p gobby-code            # Test gcode only
cargo nextest run -p gobby-wiki            # Test gwiki only
cargo nextest run -p gobby-hooks           # Test ghook only
cargo nextest run -p gobby-core            # Test gcore only
cargo clippy --workspace -- -D warnings    # Lint all
cargo fmt --all --check                    # Check formatting
```

During agent sessions, use default Cargo features for diagnosis and installs. Run `--no-default-features` only for CI-parity checks, release workflow validation, or explicit user requests.

## Workspace Layout

```
crates/
  gcore/    — Shared foundation library (no binary; feature-gated datastore/AI adapters)
  gcode/    — Heavy binary (tree-sitter, PostgreSQL, FalkorDB, Qdrant, opt-level=3)
  gwiki/    — Heavy binary (multimodal ingest, ffmpeg/pdf, hybrid search, opt-level=3)
  ghook/    — Tiny binary (hook dispatcher, enqueue-first transport, opt-level="z")
```

Release profiles are in the root `Cargo.toml` with per-package overrides. Each binary has its own optimization level.

### Installing binaries

`cargo build --workspace --release` produces `target/release/{gcode,gwiki,ghook}`. The deployed copies live in `~/.gobby/bin/`, each with a `.{name}-version` sidecar (and ghook additionally writes `.ghook-runtime.json` on `ghook --version`). To update an installed binary, copy it over the existing one (an atomic `cp` to `<name>.new` then `mv` avoids "text file busy" if it is running) and refresh the matching `.{name}-version` sidecar.

## gcode Architecture

### Data Flow

`main.rs` parses CLI args via clap → resolves a `config::Context` (project root, PostgreSQL DSN, service configs) → dispatches to the appropriate command handler in `commands/`.

### Core Modules

- **`config`** — Resolves runtime context: `~/.gobby/bootstrap.yaml` PostgreSQL DSN → PostgreSQL `config_store` → FalkorDB/Qdrant configs. Detects project root by walking up from cwd looking for `.gobby/project.json`. Resolves `$secret:NAME` patterns via `secrets`.
- **`db`** — PostgreSQL bootstrap/keyring resolution plus read/write connection helpers. Runtime schema is validated, never created or migrated by gcode.
- **`models`** — All data types: `Symbol`, `IndexedFile`, `ContentChunk`, `SearchResult`, `GraphResult`, etc.
- **`secrets`** — Fernet decryption of Gobby secrets using `~/.gobby/machine_id` + `~/.gobby/.secret_salt` for key derivation.
- **`graph`** — FalkorDB-backed code graph reads plus Rust-owned code graph projection lifecycle and sync. Daemon/UI callers delegate code graph projection work here; memory graph data stays daemon-owned.
- **`projection` / `vector`** — Rust-owned sync of code-index facts into FalkorDB and Qdrant `code_symbols_{project_id}` collections. Embedding calls for code vectors happen in Rust using resolved runtime config.
- **`output`** — Output formatting (text vs JSON).

### `commands/` — CLI Command Handlers

Each subcommand maps to a function: `index::run`, `search::search`, `symbols::outline`, `graph::callers`, etc. Commands accept `&Context` and an output `Format`.

### `index/` — Indexing Pipeline

`walker` (file discovery via `ignore` crate) → `parser` (tree-sitter AST extraction per language) → `chunker` (content splitting for BM25 content search) → `hasher` (SHA-256 for incremental indexing) → `indexer` (PostgreSQL hub writes + sync flags for Rust projection sync). `languages` maps extensions to tree-sitter grammars. `security` validates paths.

### `search/` — Search Pipeline

`fts` (pg_search BM25 symbol + content search) + `semantic` (Qdrant vector search via OpenAI-compatible embedding API) + `graph_boost` (FalkorDB relevance boost) → `rrf` (Reciprocal Rank Fusion to merge ranked results).

### Graceful Degradation

FalkorDB/Qdrant/embedding API can each be unavailable independently. Graph commands return `[]` when FalkorDB is down; semantic search returns `[]` when Qdrant or the embedding API is unavailable; BM25 search works when the PostgreSQL hub is configured and indexed.

## gwiki Architecture

### Data Flow

`main.rs` parses CLI args via clap → resolves a gwiki `Context` (project root, vault path, PostgreSQL hub, AI routing) → dispatches to a handler in `commands/`. Ingest path: `ingest/file.rs` routes a source by type → modality orchestrator (`ingest/{document,pdf,url,mediawiki,git,wayback,audio,image,video}.rs`) → derived Markdown written into the vault with frontmatter/provenance → `indexer` writes PostgreSQL hub rows → `commands/index.rs` synchronously updates Qdrant vectors and the FalkorDB graph for the same scope.

### Core Modules

- **`ingest/`** — Per-source ingestion. `file` routes by extension/type; `document`/`pdf`/`url`/`mediawiki`/`git`/`wayback` handle text-bearing sources; `audio`/`image`/`video` are the multimodal orchestrators (transcription/translation, vision, frame extraction).
- **`ai/`** — AI clients (`clients`), chunking (`chunk`), and translation (`translate`), routed through `gobby_core` AI transport. `transcribe.rs`/`vision.rs`/`video.rs` define the modality client traits and degradation vocabulary.
- **`search/`** — Same hybrid stack as gcode: `bm25` + `semantic` (Qdrant) + `graph_boost` (FalkorDB) merged via `rrf`.
- **`commands/`** — One handler per subcommand: `init`, `setup`, `collect`, `index`, `compile`, `export`, `search`, `ask`, `read`, `backlinks`, `sources`, `status`, `health`, `audit`, `lint`. `search` is the agent retrieval primitive (bounded query-token snippets, provenance, hit-tied code citations); `ask` is a thin bounded-evidence RAG layer over it (~12K-token prompt cap, daemon or direct OpenAI-compatible transport).
- **`vault`/`document`/`frontmatter`/`provenance`/`citations`/`credibility`** — The Markdown vault model: documents, frontmatter, source provenance, and citation/credibility tracking.

### Graceful Degradation

Multimodal endpoints (transcription, vision) and the AI transport degrade independently — ingest falls back to skeleton/derived output with explicit degradation markers when a capability is routed off or unavailable. Search degrades exactly like gcode (BM25 standalone; semantic/graph optional).

## ghook Architecture

### Data Flow & Modes

`ghook --gobby-owned --cli=<c> --type=<t> [--detach]` builds a hook `Envelope`, enqueues it to `~/.gobby/hooks/inbox/`, then attempts a POST to the daemon (`transport`). Enqueue-first means the hook is durable even if the daemon is down; stdout/stderr/exit codes follow the current per-CLI hook protocol. `--diagnose` prints JSON diagnostics with no network/envelope write. `--version` prints the version and writes `~/.gobby/bin/.ghook-runtime.json` (`{schema_version, ghook_version}`).

### Core Modules

- **`envelope`** — Hook payload built from stdin JSON + cli/type/flags.
- **`transport`** — Inbox enqueue + best-effort daemon POST.
- **`detach`** / **`planned_shutdown`** — Background detach and clean-shutdown handling.
- **`cli_config`** / **`statusline`** / **`terminal_context`** / **`diagnose`** — Per-CLI config, status line emission, terminal context capture, and diagnostics.

## gcore Architecture

Shared foundation library (`gobby-core`), kept dependency-light so small binaries do not inherit services they never call. Always-compiled modules are split from feature-gated adapters.

### Always-compiled modules

- **`bootstrap`** / **`daemon_url`** / **`project`** / **`provisioning`** — `~/.gobby/bootstrap.yaml` parsing, daemon URL resolution, project-root discovery (`.gobby/project.json`), and provisioning helpers.
- **`config`** / **`setup`** / **`cli_contract`** — Shared config types, setup helpers, and serialized CLI contract shapes reused across binaries.
- **`ai_context`** — AI config types, `AiContext` resolution, per-capability **routing decision** (daemon / direct / off), and an always-compiled concurrency limiter.
- **`ai_types`** — Pure AI result/error data types (no transport deps), kept separate from `ai_context`.
- **`degradation`** — Shared degradation vocabulary.

### Feature-gated adapters

`ai` (HTTP transport via `reqwest`), `postgres`, `falkor`, `qdrant`, `indexing`, `search` — each behind its own Cargo feature so a consumer pulls in only the datastores/transport it uses.

## Key Constraints

- **UUID5 parity with Python** (gcode): Symbol IDs are deterministic UUID5 using namespace `c0de1de0-0000-4000-8000-000000000000` and key format `{project_id}:{file_path}:{name}:{kind}:{byte_start}`. Must match the Python daemon's `Symbol.make_id()` exactly.
- **Config resolution order** (gcode): env vars (`GOBBY_FALKORDB_HOST`, `GOBBY_FALKORDB_PORT`, `GOBBY_FALKORDB_PASSWORD`, etc.) → `config_store` table → hardcoded defaults.
- **Tree-sitter grammars** (gcode): Tier 1 (Python/JS/TS/Go/Rust/Java/C/C++/C#/Ruby/PHP/Swift/Kotlin), Tier 2 (Dart/Elixir), Tier 3 (JSON/YAML). Markdown is indexed as content-only repo text, outside tree-sitter AST detection. Adding an AST language requires a new `tree-sitter-*` dep in `crates/gcode/Cargo.toml` and a grammar entry in `index/languages`.
- **Non-destructive to Gobby hub schema** (gcode): Validate existing Gobby-owned PostgreSQL tables and BM25 indexes. Never alter `project.json`, `config_store`, or Gobby-managed schema.
- **Per-CLI hook protocol** (ghook): stdout, stderr, and exit codes must match the current host-CLI hook contracts. Enqueue-first (inbox write before daemon POST) is an internal detail and must not change the observable contract.
- **AI ownership split** (gcore): AI config types, `AiContext` resolution, the per-capability routing decision, and the concurrency limiter live in `gobby_core::ai_context` (always-compiled, no `reqwest`); pure result/error data types live in `gobby_core::ai_types` (always-compiled); HTTP transport lives behind the `ai` feature in `gobby_core::ai`. Keep these layers separate — don't pull `reqwest` into the always-compiled modules.
