---
title: Feature Catalog
type: code_features
provenance: []
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# Feature Catalog

This page is derived deterministically from the pinned CLI contracts (`crates/<binary>/contract/<binary>.contract.json`) plus the binaries' dispatch wiring — no LLM. It enumerates every subcommand each binary exposes: what it does, its key contract flags, the handler entry symbol, and a link to the source page that explains it. The command set per binary is exactly the contract's command set, so the catalog cannot drift from the real CLI surface.

## gcode

| Command | What it does | Key flags | Entry | Docs |
| --- | --- | --- | --- | --- |
| `contract` | Emit this CLI contract. | `--format` | `contract::contract` | [[code/files/crates/gcode/src/contract.rs\|crates/gcode/src/contract.rs]] |
| `init` | Initialize project context for the current repository. | — | `commands::init::run` | [[code/files/crates/gcode/src/commands/init.rs\|crates/gcode/src/commands/init.rs]] |
| `setup` | Create gcode-owned standalone database objects and local service config. | `--standalone` `--database-url` `--no-services` `--overwrite-code-index` `--schema` `--embedding-provider` `--embedding-api-base` `--embedding-model` | `commands::setup::run` | [[code/files/crates/gcode/src/commands/setup.rs\|crates/gcode/src/commands/setup.rs]] |
| `index` | Index a directory or specific files into the code index. | `--files` `--full` `--require-cpp-semantics` `--sync-projections` | `commands::index::run` | [[code/files/crates/gcode/src/commands/index.rs\|crates/gcode/src/commands/index.rs]] |
| `status` | Show project index status. | `--format` | `commands::status::run` | [[code/files/crates/gcode/src/commands/status.rs\|crates/gcode/src/commands/status.rs]] |
| `invalidate` | Clear index state and force re-index. | `--force` | `commands::status::invalidate` | [[code/files/crates/gcode/src/commands/status.rs\|crates/gcode/src/commands/status.rs]] |
| `search` | Hybrid symbol and content search over the code index. | `--limit` `--offset` `--kind` `--language` `--token-budget` | `commands::search::search` | [[code/files/crates/gcode/src/commands/search.rs\|crates/gcode/src/commands/search.rs]] |
| `search-symbol` | Exact-first symbol/name search with deterministic ranking. | `--limit` `--offset` `--kind` `--language` `--with-graph` | `commands::search::search_symbol` | [[code/files/crates/gcode/src/commands/search.rs\|crates/gcode/src/commands/search.rs]] |
| `search-text` | Search indexed symbol metadata with BM25 ranking. | `--limit` `--offset` `--language` | `commands::search::search_text` | [[code/files/crates/gcode/src/commands/search.rs\|crates/gcode/src/commands/search.rs]] |
| `search-content` | Search indexed file content chunks with BM25 ranking. | `--limit` `--offset` `--language` | `commands::search::search_content` | [[code/files/crates/gcode/src/commands/search.rs\|crates/gcode/src/commands/search.rs]] |
| `grep` | Indexed exact pattern search over code content chunks. | `--fixed-strings` `--ignore-case` `--word` `--before-context` `--after-context` `--context` `--glob` `--max-count` | `commands::grep::run` | [[code/files/crates/gcode/src/commands/grep.rs\|crates/gcode/src/commands/grep.rs]] |
| `outline` | Show a hierarchical symbol tree for a file. | `--summarize` | `commands::symbols::outline` | [[code/files/crates/gcode/src/commands/symbols.rs\|crates/gcode/src/commands/symbols.rs]] |
| `symbol` | Fetch symbol source code by ID. | `--format` | `commands::symbols::symbol` | [[code/files/crates/gcode/src/commands/symbols.rs\|crates/gcode/src/commands/symbols.rs]] |
| `symbol-at` | Fetch symbol source code at a file location. | `--format` | `commands::symbol_at::run` | [[code/files/crates/gcode/src/commands/symbol_at.rs\|crates/gcode/src/commands/symbol_at.rs]] |
| `symbols` | Batch retrieve symbols by ID. | `--format` | `commands::symbols::symbols` | [[code/files/crates/gcode/src/commands/symbols.rs\|crates/gcode/src/commands/symbols.rs]] |
| `kinds` | List distinct symbol kinds in the index. | `--format` | `commands::symbols::kinds` | [[code/files/crates/gcode/src/commands/symbols.rs\|crates/gcode/src/commands/symbols.rs]] |
| `tree` | Show file tree with symbol counts. | `--format` | `commands::symbols::tree` | [[code/files/crates/gcode/src/commands/symbols.rs\|crates/gcode/src/commands/symbols.rs]] |
| `callers` | Find callers of a symbol UUID or name. | `--limit` `--offset` `--format` | `commands::graph::callers` | [[code/files/crates/gcode/src/commands/graph/reads.rs\|crates/gcode/src/commands/graph/reads.rs]] |
| `usages` | Find incoming call usages of a symbol UUID or name. | `--limit` `--offset` `--format` `--token-budget` | `commands::graph::usages` | [[code/files/crates/gcode/src/commands/graph/reads.rs\|crates/gcode/src/commands/graph/reads.rs]] |
| `imports` | Show import graph for a file. | `--format` | `commands::graph::imports` | [[code/files/crates/gcode/src/commands/graph/reads.rs\|crates/gcode/src/commands/graph/reads.rs]] |
| `path` | Find the shortest CALLS path from one symbol query to another. | `--max-depth` `--format` | `commands::graph::path` | [[code/files/crates/gcode/src/commands/graph/reads.rs\|crates/gcode/src/commands/graph/reads.rs]] |
| `blast-radius` | Show transitive impact analysis for a symbol query. | `--depth` `--token-budget` `--format` | `commands::graph::blast_radius` | [[code/files/crates/gcode/src/commands/graph/reads.rs\|crates/gcode/src/commands/graph/reads.rs]] |
| `codewiki` | Generate vault-ready hierarchical code documentation. | `--out` `--scope` `--since` `--ai` `--ai-depth` `--ai-aggregate-profile` `--ai-verify-profile` `--ai-prose-depth` | `commands::codewiki::run` | [[code/files/crates/gcode/src/commands/codewiki/run.rs\|crates/gcode/src/commands/codewiki/run.rs]] |
| `graph sync-file` | Sync one indexed file into the code-index graph projection. | `--file` `--allow-missing-indexed-file` `--format` | `commands::graph::sync_file` | [[code/files/crates/gcode/src/commands/graph/lifecycle.rs\|crates/gcode/src/commands/graph/lifecycle.rs]] |
| `graph overview` | Show an overview graph for the current project. | `--limit` `--format` | `commands::graph::overview` | [[code/files/crates/gcode/src/commands/graph/payload.rs\|crates/gcode/src/commands/graph/payload.rs]] |
| `graph file` | Show graph nodes and links for one indexed file. | `--file` `--format` | `commands::graph::file` | [[code/files/crates/gcode/src/commands/graph/payload.rs\|crates/gcode/src/commands/graph/payload.rs]] |
| `graph neighbors` | Show graph neighbors for one symbol ID. | `--symbol-id` `--limit` `--format` | `commands::graph::neighbors` | [[code/files/crates/gcode/src/commands/graph/payload.rs\|crates/gcode/src/commands/graph/payload.rs]] |
| `graph blast-radius` | Show transitive graph impact for a symbol ID or file path. | `--symbol-id` `--file` `--depth` `--limit` `--format` | `commands::graph::graph_blast_radius` | [[code/files/crates/gcode/src/commands/graph/payload.rs\|crates/gcode/src/commands/graph/payload.rs]] |
| `graph clear` | Clear the current project's code-index graph projection. | `--project-id` `--format` | `commands::graph::clear` | [[code/files/crates/gcode/src/commands/graph/lifecycle.rs\|crates/gcode/src/commands/graph/lifecycle.rs]] |
| `graph rebuild` | Rebuild the current project's code-index graph projection from PostgreSQL facts. | `--format` | `commands::graph::rebuild` | [[code/files/crates/gcode/src/commands/graph/lifecycle.rs\|crates/gcode/src/commands/graph/lifecycle.rs]] |
| `graph cleanup-orphans` | Remove graph projection data for files missing from PostgreSQL. | `--format` | `commands::graph::cleanup_orphans` | [[code/files/crates/gcode/src/commands/graph/lifecycle.rs\|crates/gcode/src/commands/graph/lifecycle.rs]] |
| `graph report` | Generate a project graph report. | `--top-n` `--format` | `commands::graph::report` | [[code/files/crates/gcode/src/commands/graph/payload.rs\|crates/gcode/src/commands/graph/payload.rs]] |
| `vector sync-file` | Sync one indexed file into the code-symbol vector projection. | `--file` `--allow-missing-indexed-file` `--format` | `commands::vector::sync_file` | [[code/files/crates/gcode/src/commands/vector.rs\|crates/gcode/src/commands/vector.rs]] |
| `vector clear` | Clear the current project's code-symbol vector projection. | `--format` | `commands::vector::clear` | [[code/files/crates/gcode/src/commands/vector.rs\|crates/gcode/src/commands/vector.rs]] |
| `vector rebuild` | Rebuild the current project's code-symbol vector projection from PostgreSQL facts. | `--format` | `commands::vector::rebuild` | [[code/files/crates/gcode/src/commands/vector.rs\|crates/gcode/src/commands/vector.rs]] |
| `vector cleanup-orphans` | Remove Qdrant code-symbol vectors for files missing from PostgreSQL. | `--format` | `commands::vector::cleanup_orphans` | [[code/files/crates/gcode/src/commands/vector.rs\|crates/gcode/src/commands/vector.rs]] |
| `embeddings doctor` | Emit embedding configuration doctor JSON. | — | `commands::embeddings_doctor::run` | [[code/files/crates/gcode/src/commands/embeddings_doctor.rs\|crates/gcode/src/commands/embeddings_doctor.rs]] |
| `repo-outline` | Show directory-grouped project stats. | `--format` | `commands::status::repo_outline` | [[code/files/crates/gcode/src/commands/status.rs\|crates/gcode/src/commands/status.rs]] |
| `projects` | List indexed projects. | `--format` | `commands::status::projects` | [[code/files/crates/gcode/src/commands/status.rs\|crates/gcode/src/commands/status.rs]] |
| `prune` | Remove stale project records and reconcile projections across indexed projects. | `--force` | `commands::status::prune` | [[code/files/crates/gcode/src/commands/status.rs\|crates/gcode/src/commands/status.rs]] |

## gwiki

| Command | What it does | Key flags | Entry | Docs |
| --- | --- | --- | --- | --- |
| `contract` | Emit this CLI contract. | `--format` | `contract::contract` | [[code/files/crates/gwiki/src/contract.rs\|crates/gwiki/src/contract.rs]] |
| `index` | Index markdown and source notes in the selected scope. | — | `commands::index::execute` | [[code/files/crates/gwiki/src/commands/index.rs\|crates/gwiki/src/commands/index.rs]] |
| `search` | Search wiki documents in the selected scope. | `--limit` `--no-semantic` | `commands::search::execute` | [[code/files/crates/gwiki/src/commands/search.rs\|crates/gwiki/src/commands/search.rs]] |
| `ask` | Ask a question about wiki documents in the selected scope. | `--llm` `--ai` `--require-ai` | `commands::ask::execute` | [[code/files/crates/gwiki/src/commands/ask.rs\|crates/gwiki/src/commands/ask.rs]] |
| `read` | Read a wiki page or document in the selected scope. | `--path` `--title` | `commands::read::execute` | [[code/files/crates/gwiki/src/commands/read.rs\|crates/gwiki/src/commands/read.rs]] |
| `refresh` | Refresh URL-backed raw source records. | `--id` `--dry-run` | `commands::refresh::execute` | [[code/files/crates/gwiki/src/commands/refresh/mod.rs\|crates/gwiki/src/commands/refresh/mod.rs]] |
| `ingest-file` | Capture a local source file into the wiki inbox. | `--no-ai` `--translate` `--target-lang` `--video-frame-interval` `--transcription-routing` `--vision-routing` `--text-routing` | `commands::index::execute_ingest_file` | [[code/files/crates/gwiki/src/commands/index.rs\|crates/gwiki/src/commands/index.rs]] |
| `ingest-url` | Fetch URL sources into the wiki inbox. | — | `commands::index::execute_ingest_url` | [[code/files/crates/gwiki/src/commands/index.rs\|crates/gwiki/src/commands/index.rs]] |
| `sync-sessions` | Sync archived Gobby session transcripts into the wiki vault. | `--archive-dir` `--limit` | `commands::session_sync::execute` | [[code/files/crates/gwiki/src/commands/session_sync.rs\|crates/gwiki/src/commands/session_sync.rs]] |
| `collect` | Collect recognized inbox drops into raw storage. | — | `commands::collect::execute` | [[code/files/crates/gwiki/src/commands/collect.rs\|crates/gwiki/src/commands/collect.rs]] |
| `compile` | Compile accepted research notes into wiki articles. | `--outline` `--source` `--kind` `--target` `--write-intent` `--ai` | `commands::compile::execute` | [[code/files/crates/gwiki/src/commands/compile.rs\|crates/gwiki/src/commands/compile.rs]] |
| `audit` | Report claims that lack source support. | — | `commands::audit::execute` | [[code/files/crates/gwiki/src/commands/audit.rs\|crates/gwiki/src/commands/audit.rs]] |
| `graph` | Export unified wiki graph artifacts under outputs. | — | `commands::graph::execute` | [[code/files/crates/gwiki/src/commands/graph.rs\|crates/gwiki/src/commands/graph.rs]] |
| `graph-context` | Build a compact wiki graph context pack. | — | `commands::graph_context::execute` | [[code/files/crates/gwiki/src/commands/graph_context.rs\|crates/gwiki/src/commands/graph_context.rs]] |
| `health` | Write wiki health snapshots under meta/health. | — | `commands::health::execute` | [[code/files/crates/gwiki/src/commands/health.rs\|crates/gwiki/src/commands/health.rs]] |
| `librarian` | Emit wiki upkeep proposals without rewriting canonical content. | — | `commands::librarian::execute` | [[code/files/crates/gwiki/src/commands/librarian.rs\|crates/gwiki/src/commands/librarian.rs]] |
| `review-report` | Emit a review report for changed files, symbols, or a diff. | `--file` `--symbol` `--diff` `--output` | `commands::review_report::execute` | [[code/files/crates/gwiki/src/commands/review_report.rs\|crates/gwiki/src/commands/review_report.rs]] |
| `citation-quality` | Emit source citation quality checks for wiki content. | — | `commands::citation_quality::execute` | [[code/files/crates/gwiki/src/commands/citation_quality.rs\|crates/gwiki/src/commands/citation_quality.rs]] |
| `sources` | List raw source manifest entries in the selected scope. | — | `commands::sources::execute` | [[code/files/crates/gwiki/src/commands/sources.rs\|crates/gwiki/src/commands/sources.rs]] |
| `backlinks` | Show backlinks for a wiki page. | — | `commands::backlinks::execute` | [[code/files/crates/gwiki/src/commands/backlinks.rs\|crates/gwiki/src/commands/backlinks.rs]] |
| `status` | Show shell readiness. | — | `commands::status::execute` | [[code/files/crates/gwiki/src/commands/status.rs\|crates/gwiki/src/commands/status.rs]] |
| `trust` | Show search, graph, freshness, and audit trust status. | — | `commands::trust::execute` | [[code/files/crates/gwiki/src/commands/trust.rs\|crates/gwiki/src/commands/trust.rs]] |
| `remove-source` | Remove a raw source, its manifest entry, and its raw asset. | `--id` `--dry-run` `--yes` `--keep-asset` | `commands::sources::execute_remove` | [[code/files/crates/gwiki/src/commands/sources.rs\|crates/gwiki/src/commands/sources.rs]] |

## ghook

`ghook` has no subcommand contract: it is a flag-driven hook dispatcher with a single entry point, so it is listed here for completeness without command rows. Its modes are:

- `ghook --gobby-owned --cli=<c> --type=<t> [--detach]` — build a hook envelope from stdin, enqueue it to `~/.gobby/hooks/inbox/`, then best-effort POST to the daemon (enqueue-first). `--detach` runs the dispatch in the background.
- `ghook --diagnose` — print JSON diagnostics with no network call and no envelope write.
- `ghook --version` — print the version and write `~/.gobby/bin/.ghook-runtime.json`.

**Docs:** [[code/files/crates/ghook/src/main.rs|crates/ghook/src/main.rs]]

