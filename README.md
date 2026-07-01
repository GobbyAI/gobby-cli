<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <img src="logo.png" alt="Gobby" width="160" />
</p>

<h1 align="center">gobby-cli</h1>

<p align="center">
  <strong>Rust CLI tools for AI-assisted development.</strong><br>
  Code search, symbol navigation, hook dispatch, and multimodal research vaults — all from the terminal.
</p>

<p align="center">
  <a href="https://github.com/GobbyAI/gobby-cli/actions/workflows/ci.yml"><img src="https://github.com/GobbyAI/gobby-cli/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/GobbyAI/gobby-cli/releases/latest"><img src="https://img.shields.io/github/v/release/GobbyAI/gobby-cli" alt="Release"></a>
  <a href="https://github.com/GobbyAI/gobby-cli"><img src="built-with-gobby.svg" alt="Built with Gobby"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="License"></a>
</p>

---

## What's Inside

This workspace ships three Gobby CLI tools plus a shared library.

### Current Release Set

| Crate | Binary | Version | Release tag |
|---|---|---:|---|
| `gobby-code` | `gcode` | `1.4.0` | `gcode-v1.4.0` |
| `gobby-core` | n/a | `0.7.0` | `gobby-core-v0.7.0` |
| `gobby-hooks` | `ghook` | `0.7.0` | `ghook-v0.7.0` |
| `gobby-wiki` | `gwiki` | `0.7.0` | `gwiki-v0.7.0` |

### gcode — Code Search & Navigation

AST-aware code search powered by tree-sitter. Indexes 21 languages plus safe
repo text files into the Gobby PostgreSQL hub, with pg_search BM25 for symbol
lookup, exact indexed grep over repo content chunks, ranked repo-content search
across source/docs/config/scripts, file tree
navigation, and hybrid ranking. When FalkorDB, Qdrant, and an embedding
source are configured, gcode adds graph-aware search, semantic
search, opt-in graph expansion for exact symbol lookup
(`gcode search-symbol --with-graph`), dependency analysis (`callers`, `usages`,
`imports`, `blast-radius`, shortest CALLS `path`), and Rust-owned graph/vector
projection lifecycle. `--token-budget` trims high-volume reads (`search`,
`usages`, `blast-radius`) to an approximate token cap, and `gcode prune`
reconciles stale projects and orphaned graph/vector projection state across all
indexed projects. `gcode graph clear --project-id <PROJECT_ID>` is available for
daemon stale-project graph cleanup without cwd project resolution.

`gcode codewiki` generates vault-ready hierarchical code documentation
(repo → modules → files, plus architecture/onboarding/hotspots/changes/ownership
pages) from the index, with optional AI prose tiers (`--ai-depth`), validated
Mermaid architecture diagrams (workspace topology plus runtime/AI-generation
sequence diagrams), and citation-checked grounding against indexed source
spans. Aggregate pages can use the daemon-side agentic/tool-backed generation
route, and `gcode codewiki --purge --out <vault> --force` clears generated
CodeWiki output before a clean rebuild. gwiki indexes the output as normal
vault documents.

For non-Gobby-managed projects, `gcode init` installs the bundled `gcode` skill
for Claude Code, Codex, Droid, Grok, Qwen, and Antigravity CLI. Gobby-managed
projects skip those project-local skill writes because Gobby owns CLI wiring.

### ghook — Hook Dispatcher

Sandbox-tolerant hook dispatcher invoked by host AI CLIs (Claude Code, Codex, Qwen CLI, Droid, Grok, and Antigravity) on lifecycle and tool-use events. Spools envelopes to `~/.gobby/hooks/inbox/` *before* POSTing to the local Gobby daemon, so the daemon's drain worker can replay any delivery lost to a sandbox FS-read denial, network blip, or daemon restart. You don't usually invoke it directly — Gobby wires it into your AI CLI for you.

### gwiki — Research Knowledge Vault

Ingests multimodal sources — documents, PDFs, URLs, MediaWiki, git repos,
Wayback snapshots, audio/image/video, and archived Gobby session transcripts
(`gwiki sync-sessions`) — into a Markdown knowledge vault with frontmatter
provenance and citations, then indexes and searches them with the same hybrid
BM25 + semantic + graph stack as `gcode`. `gwiki search` is the bounded agent
retrieval primitive and `gwiki ask` is a thin bounded-evidence RAG layer over
it, both honoring `--token-budget`. Compiles vault material into cited briefs,
emits static agent exports (`llms.txt`, `llms-full.txt`, `graph.jsonld`), and
repairs on-disk markdown with `gwiki normalize`. Multimodal and AI capabilities
degrade gracefully when transcription, vision, or the configured datastores are
unavailable.

`gobby-core` underpins them all — a small shared-primitives library for project
root walk-up, bootstrap config, daemon URL composition, setup/provisioning
contracts, and datastore client adapters. It is not a standalone tool.

## Documentation

- [gcode User Guide](docs/guides/gcode-user-guide.md) — search, symbols, dependency graphs, project management
- [Codewiki Guide](docs/guides/codewiki.md) — generated code documentation, AI prose depth, citations, incremental runs
- [ghook User Guide](docs/guides/ghook-user-guide.md) — hook wiring, diagnose mode, inbox/replay, troubleshooting
- [gwiki User Guide](docs/guides/gwiki-user-guide.md) — vault setup, ingest, sync-sessions, search, ask, compile
- [gwiki Development Guide](docs/guides/gwiki-development-guide.md) — research vault ingest, indexing, and hybrid search
- [Release Guide](docs/guides/release-guide.md) — crate versions, tag order, and local binary installation
- [Changelog](CHANGELOG.md) — release history
- [gcode README](crates/gcode/README.md) — architecture and build details
- [gwiki README](crates/gwiki/README.md) — architecture and build details

## Install

### Pre-built binaries

Download from [GitHub Releases](https://github.com/GobbyAI/gobby-cli/releases/latest). Binaries are available for macOS (ARM/x86), Linux (x86/ARM), and Windows (x86/ARM).

### From crates.io

```bash
# gcode
cargo install gobby-code

# ghook
cargo install gobby-hooks

# gwiki
cargo install gobby-wiki
```

`gcode` graph and semantic features are configured at runtime. There are no
Cargo feature flags for FalkorDB, Qdrant, or embeddings support. Gobby-managed
projects read FalkorDB settings from `databases.falkordb.*`; daemon-independent
setups can use `GOBBY_FALKORDB_HOST`, `GOBBY_FALKORDB_PORT`, and
`GOBBY_FALKORDB_PASSWORD`.

`gcode` 0.8.0+ uses the migrated Gobby PostgreSQL hub. It asks the local daemon
broker for the hub DSN first. If the daemon is unavailable, it checks fallback
sources in order: `GCODE_DATABASE_URL`, `GOBBY_POSTGRES_DSN`,
`~/.gobby/gcore.yaml` `databases.postgres.dsn`, then bootstrap `database_url`.
Bootstrap fallback is valid only when `hub_backend: postgres` and bootstrap
contains an inline `database_url`.

For daemon-independent service provisioning, use `gcode setup --standalone`.
The default setup path is non-destructive. If incompatible code-index state is
already present, rerun with `gcode setup --standalone --overwrite-code-index`
only when you intend to reset all gcode-owned code-index PostgreSQL,
FalkorDB, and Qdrant projection state.

Graph/vector lifecycle is code-index scoped. FalkorDB clears target-only
code-index labels, and Qdrant clears target-only `code_symbols_{project_id}`;
Gobby memory graph and memory vector collections stay outside this boundary.

Installing from source or crates.io requires Rust 1.88+.

### From source

```bash
git clone https://github.com/GobbyAI/gobby-cli.git
cd gobby-cli
cargo install --path crates/gcode
cargo install --path crates/ghook
cargo install --path crates/gwiki
```

## Development

```bash
cargo build --workspace --no-default-features   # Build all tools
cargo nextest run --workspace --no-default-features # Test all tools except doctests
cargo test --doc --workspace --no-default-features  # Test doctests
cargo clippy --workspace --no-default-features -- -D warnings  # Lint all tools
cargo fmt --all --check                         # Check formatting
```

## License

Apache 2.0 — see [LICENSE](LICENSE).
