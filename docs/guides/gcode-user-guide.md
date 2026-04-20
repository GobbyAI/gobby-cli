# gcode User Guide

A complete guide to using `gcode` for code search, symbol navigation, and dependency analysis.

## Getting Started

### Install

Download from [GitHub Releases](https://github.com/GobbyAI/gobby-cli/releases/latest) or build from source:

```bash
cargo install gobby-code
```

Graph and semantic features are configured at runtime. You do not need Cargo
feature flags to enable Neo4j, Qdrant, or embeddings support.

If you use [Gobby](https://github.com/GobbyAI/gobby), gcode is already installed.

### Initialize and Index

```bash
cd your-project
gcode init
```

`gcode init` does everything in one step:
1. Creates `.gobby/gcode.json` (project identity file)
2. Installs AI CLI skills (Claude Code, etc.) if detected
3. Indexes the entire project with tree-sitter

You'll see a progress bar while indexing:

```text
[████████████░░░░░░░░] 18/32 : src/config.rs
```

After init, you can search immediately.

### First Search

```bash
gcode search "handleAuth"
```

Returns matching symbols ranked by relevance — function names, class definitions, method signatures — with file paths, line numbers, and signatures. JSON output is wrapped in a pagination envelope showing `total`, `offset`, and `limit`.

## Search

gcode offers three search modes for different use cases.

### Hybrid Search (`gcode search`)

The default. Combines FTS5 text matching with optional semantic similarity,
graph boost, and graph expansion using Reciprocal Rank Fusion. If Neo4j,
Qdrant, or the embeddings endpoint are unavailable, `gcode search` falls back
to the sources that are configured.

```bash
gcode search "database connection pool"
gcode search "auth" --limit 5
gcode search "handler" --kind function
gcode search "config" --offset 10          # Page 2 of results
gcode search "Memory" --path "src/storage/**"  # Scope to directory
```

**When to use:** General-purpose queries. Best for natural language and conceptual searches.

**Options:**
- `--limit N` — Max results (default: 10)
- `--offset N` — Skip first N results for pagination (default: 0)
- `--kind <kind>` — Filter by symbol kind: `function`, `class`, `method`, `type`, etc.
- `--path <glob>` — Filter by file path glob (e.g. `"src/**/*.rs"`, `"*.py"`, `"tests/*"`). Uses SQL prefix pre-filtering for performance with Rust glob matching for exact semantics.

### Text Search (`gcode search-text`)

FTS5 search on symbol metadata: names, qualified names, signatures, and docstrings.

```bash
gcode search-text "parseConfig"
gcode search-text "parseConfig" --path "src/**"
```

**When to use:** You know the exact name or part of a symbol name. Fastest mode.

**Options:** `--limit N`, `--offset N`, `--path <glob>`

### Content Search (`gcode search-content`)

FTS5 search across file content chunks — finds matches in comments, strings, configuration, and code bodies.

```bash
gcode search-content "TODO: refactor"
gcode search-content "GOBBY_NEO4J_URL" --path "*.py"
```

**When to use:** Searching for string literals, comments, configuration values, or patterns that aren't symbol names.

**Options:** `--limit N`, `--offset N`, `--path <glob>`

## Symbol Retrieval

### Outline

Get the hierarchical symbol tree for a file:

```bash
gcode outline src/config.rs
```

Returns all functions, classes, methods, structs, etc. in the file with their line ranges and signatures. JSON output uses a slim format (id, name, kind, line_start, line_end, signature) — use `--verbose` for full symbol details. Much cheaper than reading the entire file.

### Symbol by ID

Fetch the exact source code of a symbol by its ID (from search or outline results):

```bash
gcode symbol "80abc77f-bdfe-5037-94a8-1ebcb753761d"
```

Returns the symbol with its full source code extracted via byte-offset read. Precise and minimal.

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

Useful for understanding project structure at a glance.

## Dependency Graph

Read-side graph commands require Neo4j. Gobby-managed projects usually provide this
automatically, and standalone projects can opt in with `GOBBY_NEO4J_URL` and
`GOBBY_NEO4J_AUTH`. Without Neo4j, graph read commands return empty results
gracefully.

All read-side graph commands resolve fuzzy input — you don't need the exact symbol name. Resolution tries exact match, then substring match, then FTS5 search across names, signatures, and docstrings. When multiple matches are found, the best is used and alternatives are shown on stderr.

For Python, JavaScript, and TypeScript, graph edges are import-aware. Calls to
external packages/modules stay external instead of being misclassified as local
symbol-to-symbol edges.

### Graph Lifecycle

`gcode` owns code-index lifecycle commands, including graph clear/rebuild. These
commands use the current resolved project context and require the Gobby daemon:

```bash
gcode graph clear
gcode graph rebuild
```

- `gcode graph clear` clears the current project's graph projection through the daemon
- `gcode graph rebuild` asks the daemon to rebuild the current project's graph projection
- Both commands fail if project context cannot be resolved, if the daemon is unreachable, or if the daemon returns non-JSON success output
- They respect the existing global `--format` flag; default output remains `json`
- No confirmation prompt is shown; these are project-scoped graph projection operators, not full index invalidation

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

See all indexed projects across both databases:

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

Name resolution looks up the `code_indexed_projects` table in both `gobby-code-index.db` and `gobby-hub.db`.

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
gcode index --files src/config.rs src/main.rs
```

In Gobby mode with the daemon running, `gcode index` writes to SQLite only and
returns immediately (<1s for incremental). The daemon's background worker
handles Neo4j graph edges and Qdrant vector sync asynchronously. FTS search
(`search-text`, `search-content`) works instantly; graph and semantic search
follow once the daemon syncs.

Without the daemon, gcode still writes SQLite immediately and performs direct
Neo4j/Qdrant sync only when those services are configured.

Reset and rebuild from scratch (destructive — prompts for confirmation):

```bash
gcode invalidate
gcode index
```

In Gobby mode, `invalidate` also notifies the daemon to clean up Neo4j graph nodes and Qdrant vectors for the project. Use `--force` to skip the confirmation prompt.

Graph projection lifecycle is separate:

```bash
gcode graph clear
gcode graph rebuild
```

Use those when you want the daemon to clear or replay graph state for the current project without performing a full destructive code-index invalidation.

## Operating Modes

### Standalone Mode

When there's no `.gobby/project.json` in the project, gcode operates independently:
- Database: `~/.gobby/gobby-code-index.db`
- Services: SQLite by default; optional Neo4j, Qdrant, and embeddings via env vars
- Identity: `.gobby/gcode.json`

This is the default for projects not managed by Gobby. All indexing and FTS5 search work fully.

### Gobby Mode

When `.gobby/project.json` exists (Gobby manages the project):
- Database: `~/.gobby/gobby-hub.db` (or path from `bootstrap.yaml`)
- Services: SQLite plus config-store-managed Neo4j, Qdrant, and embeddings (if configured)
- Identity: `.gobby/project.json`

Graph commands and semantic search become available when the required services are configured.

## Configuration

gcode resolves configuration in this order:

1. **Environment variables** — `GOBBY_NEO4J_URL`, `GOBBY_NEO4J_AUTH`, `GOBBY_QDRANT_URL`, `GOBBY_PORT`
2. **config_store table** — Key-value pairs in the SQLite database (`databases.neo4j.*`, `databases.qdrant.*`, `embeddings.*`)
3. **Hardcoded defaults** — Neo4j at `http://localhost:8474`, database `neo4j` (only when `config_store` exists)

Semantic search uses the same precedence rules:
1. **Environment variables** — `GOBBY_EMBEDDING_URL`, `GOBBY_EMBEDDING_MODEL`, `GOBBY_EMBEDDING_API_KEY`
2. **config_store table** — `embeddings.api_base`, `embeddings.model`, `embeddings.api_key`
3. **Hardcoded defaults** — model `nomic-embed-text` once an embeddings API base is configured

The database path itself is resolved from:
1. `~/.gobby/bootstrap.yaml` `database_path` key
2. Default based on mode (standalone vs Gobby)

The daemon URL (used by `invalidate`, `graph clear`, and `graph rebuild`) is resolved from:
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
- Try `gcode search-content` for string/comment searches
- Run `gcode index` to pick up recently changed files

### Graph commands return empty results

If you get "No symbol matching 'X' found", the input didn't resolve to any indexed symbol. Try a different term or check what's indexed with `gcode search-text "X"`.

If results are empty but the symbol exists, this is expected in standalone mode (no Neo4j). In Gobby mode, check that Neo4j is running and configured:

```bash
echo $GOBBY_NEO4J_URL
gcode status
```

### `gcode graph clear` / `gcode graph rebuild` fail immediately

- If you see a project-context error, initialize the project first with `gcode init` or use `--project <path>`
- If you see a daemon connectivity error, confirm the Gobby daemon is running and `~/.gobby/bootstrap.yaml` points to the right port
- If you see an invalid-JSON success error, the daemon endpoint returned a malformed response and the command intentionally aborts instead of guessing

### Slow first index

Tree-sitter parsing is fast but scales with codebase size. Subsequent runs are incremental — only changed files are re-indexed. Large `node_modules`, `target`, `.venv` directories are excluded automatically.
