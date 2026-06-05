# gcode User Guide

A complete guide to using `gcode` for code search, symbol navigation, and dependency analysis.

## Getting Started

### Install

Download from [GitHub Releases](https://github.com/GobbyAI/gobby-cli/releases/latest) or build from source:

```bash
cargo install gobby-code
```

Graph and semantic features are configured at runtime. You do not need Cargo
feature flags to enable FalkorDB, Qdrant, or embeddings support.

Runtime indexing/search requires Gobby's PostgreSQL hub. gcode asks the local
daemon broker for the hub DSN first. If the daemon is unavailable, it checks
fallback sources in order: `GCODE_DATABASE_URL`, `GOBBY_POSTGRES_DSN`,
`~/.gobby/gcode.yaml` `database_url`, then bootstrap `database_url`.
Bootstrap fallback is valid only when `hub_backend: postgres` and bootstrap
contains an inline `database_url`. Bootstrap `database_url_ref` is rejected
during bootstrap validation; it is never resolved or used to restart the
fallback chain.

For daemon-independent service provisioning:

```bash
gcode setup --standalone
```

The default setup path is non-destructive. If incompatible existing code-index
PostgreSQL state is detected, setup fails with guidance instead of dropping
objects. For daemon adoption or explicit recovery, run:

```bash
gcode setup --standalone --overwrite-code-index
```

That advanced reset recreates only gcode-owned code-index PostgreSQL objects,
clears code-index graph nodes in FalkorDB, and deletes Qdrant collections named
with the `code_symbols_` prefix. It leaves Gobby project files, config,
secrets, tasks, sessions, memory, and other daemon-owned data untouched.

If you use [Gobby](https://github.com/GobbyAI/gobby), gcode is already installed.

### Initialize and Index

```bash
cd your-project
gcode init
```

`gcode init` does everything in one step:
1. Creates `.gobby/gcode.json` (project identity file)
2. Installs AI CLI skills for supported project-local targets
3. Indexes the entire project with tree-sitter AST parsing plus non-binary text files

You'll see a progress bar while indexing:

```text
[████████████░░░░░░░░] 18/32 : src/config.rs
```

After init, you can search immediately.

For non-Gobby-managed projects, `gcode init` installs the bundled `gcode` skill
for Claude Code, Codex, Droid, Grok, Qwen, Gemini CLI (deprecated
compatibility), and Antigravity CLI:

| CLI | Project-local files |
|-----|---------------------|
| Claude Code | `.claude-plugin/plugin.json`, `skills/gcode/SKILL.md` |
| Codex | `.codex/skills/gcode/SKILL.md` |
| Droid | `.factory/skills/gcode/SKILL.md` |
| Grok | `.grok/skills/gcode/SKILL.md` |
| Qwen | `.qwen/skills/gcode/SKILL.md` |
| Gemini CLI (deprecated) | `.gemini/skills/gcode/SKILL.md` |
| Antigravity CLI | `.agents/skills/gcode/SKILL.md` |

Gobby-managed projects skip these project-local writes because Gobby owns CLI
wiring. Gemini CLI remains installed for compatibility with older setups, but
it is deprecated.

### First Search

```bash
gcode search "handleAuth"
```

Returns matching symbols ranked by relevance — function names, class definitions, method signatures — with file paths, line numbers, and signatures. JSON output is wrapped in a pagination envelope showing `total`, `offset`, and `limit`.

## Search

gcode offers four search modes for different use cases.

### Hybrid Search (`gcode search`)

The default. Combines pg_search BM25 text matching with semantic similarity,
graph boost, and graph expansion using Reciprocal Rank Fusion. Full hybrid
ranking requires PostgreSQL with `pg_search`, Qdrant, FalkorDB, and a reachable
embedding endpoint; `gcode setup` provisions or validates that stack. When
semantic or graph services are unavailable, search degrades to the reachable
sources instead of failing as long as BM25 search is available. JSON results
still expose `score` as the final display rank score, `rrf_score` as the raw RRF
contribution, and sorted `sources` values for source attribution.

```bash
gcode search "database connection pool"
gcode search "auth" --limit 5
gcode search "handler" --kind function
gcode search "config" --offset 10              # Page 2 of results
gcode search "Memory" src/storage              # Scope to directory
gcode search "Memory" src/storage tests/**/*.rs
gcode search "Context" --language rust         # Scope to Rust sources
```

**When to use:** General-purpose queries. Best for natural language and conceptual searches.

**Options:**
- `--limit N` — Max results (default: 10)
- `--offset N` — Skip first N results for pagination (default: 0)
- `--kind <kind>` — Filter by symbol kind: `function`, `class`, `method`, `type`, etc. Use `gcode kinds` to list what's available in the current index.
- `--language <lang>` — Filter by source language (e.g. `rust`, `python`, `typescript`, `css`).
- Positional `PATH` arguments after the query — Filter by one or more paths or globs (e.g. `src`, `src/**/*.rs`, `tests/*`). Bare paths match the exact file path and descendants; multiple paths use OR semantics.

`--kind`, `--language`, and positional paths compose — combine them to narrow as far as you need. Globs that cannot be converted to SQL prefixes are still honored through post-filtering; JSON output includes a hint and text output prints a warning when that broader fetch path is used.

### Symbol Search (`gcode search-symbol`)

Exact-first symbol/name lookup with deterministic ranking. Resolves precise
matches (exact name, then qualified-name and case-insensitive variants) before
falling back to BM25. Useful when you already know (most of) the name and want
the canonical hit at rank 0 instead of letting hybrid ranking rerank it.

```bash
gcode search-symbol "outline"
gcode search-symbol "Context" --kind class --language rust
gcode search-symbol "ensure_fresh" crates/gcode
gcode search-symbol "Context" crates/gcode/src --kind class --language rust
gcode search-symbol "Context" --with-graph
```

**When to use:** You know the symbol's name (or close to it) and want a stable, top-ranked match — for example, before calling `gcode symbol <id>`.

**Options:** `--limit N`, `--offset N`, `--kind <kind>`, `--language <lang>`, `--with-graph`, positional `PATH ...`. `--with-graph` keeps exact-first ranking but adds FalkorDB graph neighbors when available.

### Text Search (`gcode search-text`)

pg_search BM25 search on symbol metadata: names, qualified names, signatures, and docstrings.

```bash
gcode search-text "parseConfig"
gcode search-text "parseConfig" src
gcode search-text "parseConfig" src/**/*.py tests
gcode search-text "parseConfig" --language python
```

**When to use:** You know the exact name or part of a symbol name. Fastest mode.

**Options:** `--limit N`, `--offset N`, `--language <lang>`, positional `PATH ...`

### Indexed Grep (`gcode grep`)

Exact indexed search over the same `code_content_chunks` corpus used by
`search-content`. It scans indexed chunks after path and glob filters, returns
stable `file_path` then line-number ordering, and never shells out to `rg`.

```bash
gcode grep "pattern" [PATH ...]
gcode grep "pattern" src -m 50
gcode grep "GOBBY_FALKORDB_HOST" -F -g "*.rs" crates/gcode/src
gcode grep "todo" --ignore-case -C 2 docs
```

**When to use:** You need grep-shaped exact matches with line numbers and
optional context. Text output uses `path:line:match` and `path-line-context`.
JSON output includes `project_id`, `pattern`, flags, `max_count`,
`matched_lines`, `truncated`, `scanned_chunks`, and per-line matches with
spans and context.

**Options:** `-n/--line-number` (accepted; text always shows line numbers),
`-i/--ignore-case`, `-F/--fixed-strings`, `-C/--context N`,
`-A/--after-context N`, `-B/--before-context N`, `-g/--glob GLOB`,
`-m/--max-count N`, positional `PATH ...`. `--limit` is intentionally rejected;
use `-m/--max-count` for matching-line caps. Use raw `rg` for filesystem grep
or unsupported ripgrep flags.

For `-g/--glob`, a bare glob such as `*.rs` matches basenames in any directory,
while a glob containing `/`, such as `src/*.rs`, matches the indexed path.

### Content Search (`gcode search-content`)

pg_search BM25 search across file content chunks. It covers AST-supported
source bodies and comments plus safe repo text files such as docs, Markdown,
skill files, configs (YAML/TOML/JSON/etc.), SQL/CSS, scripts,
`Dockerfile`/`Makefile`, and extensionless text.

```bash
gcode search-content "TODO: refactor"
gcode search-content "GOBBY_FALKORDB_HOST" *.py
gcode search-content "database_url" crates/gcode/src docs/**/*.md
gcode search-content "primary-color" --language css
```

**When to use:** Searching for string literals, comments, configuration values, stylesheet rules, or patterns that aren't symbol names.

Unsupported text files use their extension as the language label when one
exists, otherwise `text`. Binary, secret-like, excluded, empty, and >10MB files
are skipped.

**Options:** `--limit N`, `--offset N`, `--language <lang>`, positional `PATH ...`

## Symbol Retrieval

### Outline

Get the hierarchical symbol tree for a file:

```bash
gcode outline src/config.rs
```

Returns all functions, classes, methods, structs, Markdown headings, JSON/YAML
properties, etc. in the file with their line ranges and signatures. JSON output
uses a slim format (id, name, kind, line_start, line_end, signature) — use
`--verbose` for full symbol details. Much cheaper than reading the entire file.

### Symbol by ID

Fetch the exact source code of a symbol by its ID (from search or outline results):

```bash
gcode symbol "80abc77f-bdfe-5037-94a8-1ebcb753761d"
```

Returns the symbol with its full source code extracted via byte-offset read. Precise and minimal.

### Symbol by Location

Fetch the visible symbol containing a known file location:

```bash
gcode symbol-at src/auth.ts:42
gcode symbol-at src/auth.ts:42:7
gcode symbol-at src/auth.ts 42
```

Columns are 1-based byte columns. If no symbol contains the location, `symbol-at`
returns the nearest visible symbol and marks the JSON `lookup.match_kind` as
`nearest`; text output prints only the selected source and emits a concise stderr
fallback diagnostic unless `--quiet` is set.

### Batch Retrieve

Fetch multiple symbols in one call:

```bash
gcode symbols "id1" "id2" "id3"
```

### Symbol Kinds

List all distinct symbol kinds in the current project index:

```bash
gcode kinds
```

Returns kinds like `function`, `class`, `method`, `type`, `struct`, etc. Useful for understanding what `--kind` values are available for search filtering.

### File Tree

Get the project's file tree with symbol counts per file:

```bash
gcode tree
```

Useful for understanding project structure at a glance. Content-only text files
appear with a zero symbol count once indexed.

## Dependency Graph

Read-side graph commands require FalkorDB. Gobby-managed projects usually provide this
automatically, and daemon-independent projects can opt in with `GOBBY_FALKORDB_HOST`,
`GOBBY_FALKORDB_PORT`, and `GOBBY_FALKORDB_PASSWORD`. Without FalkorDB, graph read
commands return empty results gracefully.

All read-side graph commands resolve fuzzy input — you don't need the exact symbol name. Resolution tries exact match, then substring match, then BM25 search across names, signatures, and docstrings. When multiple matches are found, the best is used and alternatives are shown on stderr.

For Python, JavaScript, and TypeScript, graph edges are import-aware. Calls to
external packages/modules stay external instead of being misclassified as local
symbol-to-symbol edges.

### Graph Overview

```bash
gcode graph overview --limit 100
```

- `--limit N` caps the number of files used as overview graph roots
- Default: `100`
- Output uses the global `--format` flag; default output remains `json`

### Graph Lifecycle

`gcode` owns code-index lifecycle commands, including graph clear/rebuild. These
commands use the current resolved project context and require FalkorDB:

```bash
gcode graph clear
gcode graph clear --project-id <PROJECT_ID>
gcode graph sync-file --file <FILE>
gcode graph rebuild
```

- `gcode graph clear` clears the current project's graph projection
- `gcode graph clear --project-id <PROJECT_ID>` is for daemon stale-project cleanup and runs without cwd project-root resolution
- `gcode graph sync-file --file <FILE>` syncs one already-indexed file into the graph projection
- `gcode graph rebuild` rebuilds the current project's graph projection from PostgreSQL facts
- These commands fail if required project context cannot be resolved or if FalkorDB is unavailable
- They respect the existing global `--format` flag; default output remains `json`
- No confirmation prompt is shown; these are project-scoped graph projection operators, not full index invalidation
- Graph clears delete only code-index projection nodes and edges in FalkorDB; memory graph data is left untouched
- `gcode graph sync-file --allow-missing-indexed-file` is daemon/background-worker only. It converts a missing indexed file into a skipped JSON payload with `reason: "indexed_file_not_found"`; strict human defaults return a typed error with exit code `2`.

### Callers

Who calls this function?

```bash
gcode callers "handleAuth"
gcode callers "handleAuth" --limit 20
gcode callers "handleAuth" --offset 10    # Page 2
```

### Usages

Incoming call sites:

```bash
gcode usages "DatabasePool"
```

### Imports

Show the import graph for a file:

```bash
gcode imports src/auth/middleware.ts
```

### Blast Radius

Transitive impact analysis — what breaks if this changes?

```bash
gcode blast-radius "handleAuth" --depth 3
```

Walks the call graph to find all downstream dependents up to `--depth` levels deep.

## Project Management

### Status

Check the current project's index stats:

```bash
gcode status
```

Returns file count, symbol count, last indexed time, and duration.

### List Projects

See all indexed projects in the PostgreSQL hub:

```bash
gcode projects
```

### Cross-Project Queries

Query a different project by name or path:

```bash
# By name (matches against project directory basename)
gcode search --project myapp "query"

# By path
gcode search --project /home/user/projects/myapp "query"
```

Name resolution looks up the `code_indexed_projects` table in the configured PostgreSQL hub.

### Re-indexing

Incremental re-index (only changed files):

```bash
gcode index
```

Full re-index (re-processes all files, cleans stale external index entries):

```bash
gcode index --full
```

Index specific files:

```bash
gcode index --files src/config.rs docs/notes.md Dockerfile
```

`gcode index` writes symbols, files, chunks, imports, and calls to the
PostgreSQL hub. It marks graph/vector sync flags dirty; `gcode index
--sync-projections` updates FalkorDB graph edges and Qdrant code-symbol vectors
from Rust. Deleted-file cleanup removes code graph/vector projection rows before
PostgreSQL facts are deleted, including explicit `--files <deleted-file>` and
whole-project orphan cleanup.
BM25-specific modes (`search-text`, `search-content`) work as soon as the
transaction commits. Full hybrid search uses the required PostgreSQL, FalkorDB,
Qdrant, and embedding stack once graph and vector projections sync; configured
runtime outages are reported as degradations by callers that support partial
results.

Reset the current project and rebuild from scratch (destructive — prompts for confirmation):

```bash
gcode invalidate
gcode index
```

`invalidate` deletes only rows for the current project from PostgreSQL. When a
daemon URL or standalone service config is available, it also cleans only that
project's FalkorDB graph nodes and `code_symbols_{project_id}` Qdrant
projection. Use `--force` to skip the confirmation prompt.

For a full standalone code-index reset across projects and projections, use
`gcode setup --standalone --overwrite-code-index`. That command is intended for
daemon adoption and explicit recovery.

Graph projection lifecycle is separate:

```bash
gcode graph clear
gcode graph rebuild
```

Use those to clear or replay graph state for the current project without
performing a full destructive code-index invalidation. Code vector lifecycle is
similarly scoped to `code_symbols_{project_id}` and does not touch Gobby memory
vector collections.

## Operating Model

gcode is daemon-independent but not database-independent:
- Database: PostgreSQL hub from `~/.gobby/bootstrap.yaml`
- Required bootstrap: `hub_backend: postgres` plus `database_url`; bootstrap `database_url_ref` is rejected
- Identity: `.gobby/project.json`, `.gobby/gcode.json`, isolated root, linked worktree, or generated identity from `gcode init`
- Optional services: FalkorDB, Qdrant, and embeddings via env vars or PostgreSQL `config_store`

Graph commands and semantic search become available when the required services are configured.

### Isolated and worktree-derived identities

Two cases break the usual "one `.gobby/project.json` ↔ one project id" mapping. gcode handles them automatically:

- **Isolation marker** — when `.gobby/project.json` carries `parent_project_path` or `parent_project_id` fields, gcode treats the directory as its own code-index target rather than as part of the parent. The id is a deterministic UUID5 derived from the canonical filesystem path, so the directory gets its own symbol/file rows in the PostgreSQL hub and never collides with the parent's index.
- **Linked git worktrees** — runs from inside a `git worktree add` directory resolve to the worktree's own top-level (via `git rev-parse --show-toplevel` and `git worktree list --porcelain`). The code-index id is derived from the worktree path, not from any inherited `.gobby/project.json`. If an inherited id would have been used, gcode prints a warning naming the filesystem-derived id it picked instead.

Both cases are reported by `gcode init`'s status line (`isolated`, `linked-worktree`) so it's clear which identity source resolved.

## Configuration

gcode resolves graph/vector configuration in this order:

1. **Environment variables** — `GOBBY_FALKORDB_HOST`, `GOBBY_FALKORDB_PORT`, `GOBBY_FALKORDB_PASSWORD`, `GOBBY_QDRANT_URL`
2. **config_store table** — Key-value pairs in the PostgreSQL hub (`databases.falkordb.host`, `databases.falkordb.port`, `databases.falkordb.requirepass`, `databases.qdrant.*`, `embeddings.*`)
3. **Hardcoded defaults** — FalkorDB port `16379` and graph name `gobby_code` once a host is configured; no default FalkorDB host is assumed

Semantic search uses the same precedence rules:
1. **Environment variables** — `GOBBY_EMBEDDING_URL`, `GOBBY_EMBEDDING_MODEL`, `GOBBY_EMBEDDING_API_KEY`
2. **config_store table** — `embeddings.api_base`, `embeddings.model`, `embeddings.api_key`
3. **Hardcoded defaults** — model `nomic-embed-text` once an embeddings API base is configured

The database connection is resolved in this order:
1. Local daemon broker
2. `GCODE_DATABASE_URL`
3. `GOBBY_POSTGRES_DSN`
4. `~/.gobby/gcode.yaml` `database_url`
5. `~/.gobby/bootstrap.yaml` `database_url`

Bootstrap `database_url_ref` is rejected. Use the daemon broker path or an
explicit fallback source for daemonless access.

The daemon URL (used by `invalidate`) is resolved from:
1. `GOBBY_PORT` environment variable (e.g. `60887`)
2. `~/.gobby/bootstrap.yaml` `daemon_port` + `bind_host` keys
3. Default: `http://localhost:60887`

## Output Formats

All commands support `--format`:

```bash
gcode search "query" --format json   # Default — structured JSON
gcode search "query" --format text   # Human-readable text
```

JSON output for search/callers/usages is wrapped in a pagination envelope:

```json
{
  "project_id": "3bf57fe7-...",
  "total": 47,
  "offset": 0,
  "limit": 10,
  "results": [...]
}
```

Text output shows a pagination hint when more results are available:

```text
-- 10 of 47 results (use --offset 10 for more)
```

### Verbose output

`--verbose` currently affects `outline` output only:

```bash
gcode outline src/main.rs --verbose  # Full symbol details instead of slim
```

Default outline output is optimized for token efficiency — slim fields only.
Use `--verbose` when you need the full symbol record.

Suppress warnings and progress bars with `--quiet`:

```bash
gcode index --quiet
```

### Read-time freshness

By default, search, symbol, outline, and graph read commands check that the
indexed source still matches the on-disk file before returning results. If a
file has changed, gcode incrementally re-indexes the affected file(s)
transparently and then runs your command. This is meant to keep individual
reads honest — it is **not** a substitute for `gcode index` after a bulk
checkout or branch switch.

Disable per-call when you know the index is current and you want zero overhead:

```bash
gcode --no-freshness search "query"
gcode --no-freshness outline src/main.rs
```

Set `GCODE_FRESHNESS_INFLIGHT=1` in nested processes (or scripts that already
run their own re-index) to short-circuit the same checks. gcode also sets this
flag internally to prevent the indexer from recursing into itself.

Overlay indexing uses `git status` to find changed paths. Set
`GCODE_GIT_STATUS_TIMEOUT_SECS` to a positive number to override the default
5-second timeout; invalid or nonpositive values are ignored with a warning.

## Troubleshooting

### "No gcode project found"

You haven't initialized the project yet:

```bash
gcode init
```

Or specify a project explicitly:

```bash
gcode search --project /path/to/project "query"
```

### "Project 'foo' not found"

The project name doesn't match any indexed project. Check available projects:

```bash
gcode projects
```

### Empty search results

- Run `gcode status` to verify the project is indexed
- Try `gcode search-text` for exact name matches
- Try `gcode grep "pattern" [PATH ...]` for exact string/comment searches
- Try `gcode search-content` for ranked string/comment searches
- Run `gcode index` to pick up recently changed files

### Graph commands return empty results

If you get "No symbol matching 'X' found", the input didn't resolve to any indexed symbol. Try a different term or check what's indexed with `gcode search-text "X"`.

If results are empty but the symbol exists, this is expected when FalkorDB is not configured. In Gobby mode, check that FalkorDB is running and configured:

```bash
echo $GOBBY_FALKORDB_HOST
echo $GOBBY_FALKORDB_PORT
gcode status
```

### `gcode graph clear` / `gcode graph rebuild` fail immediately

- If you see a project-context error, initialize the project first with `gcode init` or use `--project <path>`
- If you see a FalkorDB configuration or connectivity error, confirm `GOBBY_FALKORDB_HOST` / `GOBBY_FALKORDB_PORT` or `config_store` are correct
- For stale-project cleanup where cwd has no project context, use `gcode graph clear --project-id <PROJECT_ID>`

### Slow first index

Tree-sitter parsing is fast but scales with codebase size. Subsequent runs are incremental — only changed files are re-indexed. Large `node_modules`, `target`, `.venv` directories are excluded automatically.
