# gcode Development Guide

Technical internals for developers and agents working in the gcode codebase.

## Architecture Overview

```
CLI (main.rs, clap)
  → Context::resolve (config.rs)
    → detect_project_root / resolve_db_path / resolve_services
  → Command dispatch (main.rs match)
    → commands/{search,symbols,graph,index,status,init}.rs
      → search/ pipeline (FTS5 + optional semantic + optional graph sources → RRF)
      → index/ pipeline (walker → parser → chunker → hasher → indexer)
      → neo4j (HTTP Cypher queries)
      → db (SQLite WAL connections)
      → output (JSON/text formatting)
```

### Entry Point

`main.rs` parses CLI args via clap, resolves a `config::Context` (project root, DB path, service configs), and dispatches to the appropriate command handler. Commands that work without a project context (`init`, `projects`, `prune`) are dispatched before `Context::resolve()`.

`--verbose` is currently only consumed by `commands::symbols::outline()`, which
switches outline output from the slim projection to the full `Symbol` payload.

`gcode graph clear` and `gcode graph rebuild` are nested under a `graph`
subcommand group, but the existing read-side graph queries remain top-level:
`callers`, `usages`, `imports`, and `blast-radius`.

## Configuration Resolution

**File:** `src/config.rs`

`Context::resolve(project_override, quiet)` orchestrates the full resolution flow:

### Project Detection

1. If `--project` is a directory path, use it directly
2. If `--project` is a name, look up in `code_indexed_projects` table (basename suffix match)
3. Otherwise, walk up from cwd looking for `.gobby/project.json` (Gobby-managed) or `.gobby/gcode.json` (standalone)
4. Otherwise, prefer the git worktree top-level (`git rev-parse --show-toplevel`, including linked worktrees — see "Worktree-aware project root" below)
5. Fall back to VCS root markers (`.git`, `.hg`) or cwd

The walk-up and `project.json` reading steps use `gobby_core::project::find_project_root` and `gobby_core::project::read_project_id` (extracted from `gcode/src/project.rs` so `ghook` and other binaries can share the same logic). Bootstrap-config and daemon-URL helpers also come from `gobby-core`. See [gobby-core Development Guide](gcore-development-guide.md) for the shared API.

### Project Identity

**File:** `src/config.rs` — `ProjectIdentity`, `ProjectIdentitySource`, `MissingIdentity`, `resolve_project_identity()`

After the project root is detected, `resolve_project_identity()` decides which `project_id` to use and which identity source produced it. This replaces the old "either `.gobby/project.json` or `.gobby/gcode.json`" binary with five sources:

| Source | Trigger | `project_id` derived from | Writes `.gobby/gcode.json`? |
|--------|---------|---------------------------|-----------------------------|
| `IsolatedRoot` | `.gobby/project.json` carries `parent_project_path` or `parent_project_id` (read via `project::read_isolation_marker`) | UUID5 of canonical root path (`project::code_index_id_for_root`) | No |
| `LinkedWorktree` | `git::worktree_info()` reports `WorktreeKind::Linked` | UUID5 of the worktree top-level path | No |
| `ProjectJson` | `.gobby/project.json` exists, no isolation fields | `project_id` field from the file | No |
| `GcodeJson` | `.gobby/gcode.json` exists | `project_id` field from the file | No |
| `Generated` | None of the above | UUID5 of canonical root path | Only when `MissingIdentity::Generate` (i.e. `gcode init`) |

`MissingIdentity::Error` is the default for non-init commands — they fail with "Run `gcode init`" instead of silently creating a generated id. Linked-worktree resolution emits a warning when an inherited `project.json` id differs from the filesystem-derived id, so it's obvious that the latter is the one being used.

### Worktree-aware project root

**File:** `src/git.rs`

`git::worktree_info(path)` shells out to `git -C <path> rev-parse --show-toplevel`, then reads `git worktree list --porcelain` to classify the result as `WorktreeKind::Main`, `WorktreeKind::Linked`, or `WorktreeKind::NotGit`. `Context::resolve` calls this during root detection so commands invoked deep inside a `git worktree add` directory resolve to the worktree's own top-level (not the main repo's `.git`-bearing directory).

Failure modes degrade gracefully: if `git` is missing, the call errors and the resolver falls back to the generic VCS-root markers.

### Database Path Selection

1. Check `~/.gobby/bootstrap.yaml` for `database_path` key
2. If `.gobby/project.json` exists → `~/.gobby/gobby-hub.db` (Gobby mode, shared DB)
3. Otherwise → `~/.gobby/gobby-code-index.db` (standalone mode)

### Service Configuration

Resolution order per service (Neo4j, Qdrant, embeddings):

| Priority | Source | Example |
|----------|--------|---------|
| 1 (highest) | Environment variables | `GOBBY_NEO4J_URL`, `GOBBY_QDRANT_URL`, `GOBBY_EMBEDDING_URL` |
| 2 | `config_store` table in SQLite | `databases.neo4j.url`, `databases.qdrant.url`, `embeddings.api_base` |
| 3 (lowest) | Hardcoded defaults | Neo4j `http://localhost:8474` / `neo4j`; embeddings model `nomic-embed-text` once an API base exists |

Config values are JSON-encoded in `config_store` — strings have surrounding quotes stripped. Secret patterns like `$secret:NAME` are resolved via `secrets.rs` (Fernet decryption using machine_id + salt, 600K PBKDF2 iterations).

### Operating Modes

| Mode | Trigger | Database | Services |
|------|---------|----------|----------|
| Standalone | `.gobby/gcode.json` only | `gobby-code-index.db` | SQLite by default; optional Neo4j/Qdrant/embeddings via env vars |
| Gobby | `.gobby/project.json` exists | `gobby-hub.db` | SQLite + config-store-managed Neo4j/Qdrant/embeddings |

Standalone mode has no `config_store` table, so hardcoded service defaults never
apply there. Graph and semantic features can still be enabled explicitly with
environment variables.

## Indexing Pipeline

**Files:** `src/index/{walker,parser,chunker,hasher,indexer}.rs`

### Data Flow

```
walker::discover_files(root, excludes)
  → (ast_candidates, content_only_candidates)
    → parser::parse_file(path, project_id, root, excludes)
      → tree-sitter AST → extract_symbols + extract_imports + extract_calls
      → link_parents (nest methods in classes, build qualified names)
    → chunker::chunk_file_content(source, rel_path, project_id, lang)
      → 100-line chunks with 10-line overlap
    → hasher::file_content_hash(path)
      → SHA-256 for incremental detection
    → indexer::upsert_symbols + upsert_file + upsert_chunks
      → SQLite writes + FTS5 population
      → upsert_imports + upsert_calls (if tables exist)
      → [daemon available] return early — flags stay 0, daemon syncs
      → [no daemon + services configured] direct Neo4j/Qdrant writes
      → [SQLite-only] skip external writes
```

### File Discovery (walker.rs)

Uses the `ignore` crate (`WalkBuilder`) which respects `.gitignore`, `.git/info/exclude`, and git global config. Files are partitioned into:

- **AST candidates**: Extensions matching a tree-sitter language spec (18 languages)
- **Content-only candidates**: Extensions like `.sh`, `.sql`, `.html`, `.css` — chunked for FTS but no AST parsing

Default excludes: `node_modules`, `__pycache__`, `.git`, `.venv`, `target`, `dist`, `build`, `.next`, `coverage`, etc.

### Tree-Sitter Parsing (parser.rs)

1. **Security checks**: Path validation, symlink safety, binary detection (8KB read), secret file detection, 10MB size limit
2. **Language detection**: Extension → `languages::detect_language()` → `LanguageSpec`
3. **AST parsing**: Tree-sitter grammar per language, execute symbol/import/call queries
4. **Symbol extraction**: Captures `@name` and `@definition.KIND` from query results. Kind is parsed from the capture name (e.g., `definition.function` → kind `function`)
5. **Parent linking**: For each symbol, find the largest enclosing class/type by byte range. Nested functions in classes become `method` kind. Qualified names built as `parent_name.symbol_name`
6. **Signature**: First line of definition, truncated at 200 chars
7. **Docstring**: Python/JS/TS only — first string literal in function/class body

### Import Resolution and Call Target Classification

Python, JavaScript, and TypeScript parsing now includes an import-resolution
pass before call targets are finalized:

- Local symbol calls resolve to canonical `callee_symbol_id` values
- Unmatched calls stay `unresolved`
- Import-bound external calls are marked `external` and retain their source module

This keeps external package calls out of the local call graph and improves Neo4j
correctness for `callers`, `usages`, `blast-radius`, and graph-backed search.

### Language Support (languages.rs)

18 languages with tree-sitter queries for symbol definitions, imports, and call sites:

| Tier | Languages |
|------|-----------|
| Tier 1 | Python, JavaScript, TypeScript, Go, Rust, Java, C, C++, C#, Ruby, PHP, Swift, Kotlin |
| Tier 2 | Dart, Elixir |
| Tier 3 | JSON, YAML, Markdown (content structure only) |

Each language has a `LanguageSpec` with three tree-sitter queries: `symbol_query`, `import_query`, `call_query`. Empty queries mean that feature is disabled for the language.

### Content Chunking (chunker.rs)

Files are split into overlapping chunks for FTS5 content search:

- **Chunk size**: 100 lines
- **Overlap**: 10 lines (step = 90)
- **1-indexed**: line_start/line_end use 1-based indexing
- Empty/whitespace-only chunks are pruned

### Incremental Indexing (indexer.rs)

1. **Hash comparison**: SHA-256 content hash per file, stored in `code_indexed_files`
2. **Stale detection**: Compare current hashes against stored hashes; files with changed hashes are re-indexed. When the `graph_synced` column exists (Gobby mode), files where `graph_synced=0` are also detected as stale with reason `GraphSyncPending`
3. **Orphan cleanup**: Files in the DB that no longer exist on disk have their data deleted from SQLite. When daemon is available, external cleanup (Neo4j/Qdrant) is deferred to the daemon's `reconcile_stores`
4. **Per-file transactions**: SQLite writes (delete old data, upsert symbols, upsert file, upsert content chunks, upsert imports/calls) are wrapped in a single transaction to prevent half-indexed files on crash
5. **Deferred external writes** (Gobby mode with daemon): After the SQLite transaction commits, gcode returns early — `graph_synced` and `vectors_synced` stay at `0`. The daemon's background worker polls for pending files, generates embeddings, writes Qdrant vectors and Neo4j edges, and flips the flags independently
6. **Direct external writes** (no daemon, services configured): Neo4j/Qdrant writes happen after the SQLite transaction. If all succeed, `graph_synced` is set to `1`. If any fail, it stays `0` and the next incremental run retries
7. **Graph-sync-only path**: Files with `StaleReason::GraphSyncPending` skip the SQLite transaction entirely — only external writes are retried. When daemon is available, these files are skipped entirely (daemon handles retries)

The `--full` flag skips the hash comparison and re-indexes all files, ensuring stale external index entries are cleaned up.

### Read-time Freshness

**File:** `src/freshness.rs`

Search, symbol, outline, and graph read commands gate their work on `freshness::ensure_fresh()` (project-scoped) or `freshness::ensure_symbol_fresh()` (single-symbol). Both verify that the on-disk source still matches the index and incrementally re-index affected files transparently before the read returns.

- **Scopes**: `FreshnessScope::Project` (re-runs the standard incremental indexer over the whole project root) and `FreshnessScope::Files(Vec<PathBuf>)` (limits the re-index to the listed files — used for `outline` and other file-scoped commands).
- **Symbol scope**: `ensure_symbol_fresh` looks up the symbol's source file and re-indexes just that file when the stored byte range no longer matches the on-disk content.
- **Re-entrancy guard**: `freshness::ensure_fresh` checks `GCODE_FRESHNESS_INFLIGHT`; if set, it short-circuits. The `FreshnessGuard` RAII helper sets and clears the same env var so the indexer's own subprocesses don't recurse into freshness.
- **Disable from CLI**: the global `--no-freshness` flag (`Cli::no_freshness`) skips all of the above. `main.rs` wraps each freshness call in `ensure_project_fresh` / `ensure_files_fresh` / `ensure_symbol_fresh` thin helpers that respect the flag.
- **Boundary**: freshness is per-call repair, not a substitute for `gcode index` after bulk changes (branch switches, large refactors). It's optimized for "this single file changed since the last index run."

### Project-scoped path validation

**File:** `src/commands/scope.rs`

Search, symbol, outline, and graph commands all run resolved paths through the helpers in `commands::scope` before returning results, so stale rows from other projects sharing `gobby-hub.db` cannot leak across project boundaries:

- `normalize_file_arg(ctx, file)` — relativize a CLI-supplied path against the resolved project root.
- `path_exists_in_current_project(ctx, file_path)` — does the path exist on disk inside the current project root?
- `indexed_file_exists` / `content_chunks_exist` — does the file have rows in `code_indexed_files` / `code_content_chunks` for the current `project_id`?
- `current_indexed_path_is_valid` — composite check used as a gate before returning results.

### Import/Call SQLite Storage

When daemon migration v183 tables exist (`code_imports`, `code_calls`), gcode writes parsed relations during Phase 1:

- **`code_imports`**: `(project_id, source_file, target_module)` — from `parse_result.imports`
- **`code_calls`**: `(project_id, caller_symbol_id, callee_symbol_id, callee_name, callee_target_kind, callee_external_module, file_path, line)` — from `parse_result.calls`

Both use delete-then-insert per file. `callee_target_kind` distinguishes stable
local-symbol edges from unresolved or external calls, and
`callee_external_module` preserves package/module provenance for external calls.
Table existence is detected via `has_table()` (PRAGMA-based), so gcode works
whether or not the daemon has applied the migration.

### Graph Lifecycle RPCs

Read-side graph queries still go straight to Neo4j. Graph lifecycle operations
are daemon-backed orchestration commands instead:

- `gcode graph clear` → `POST /api/code-index/graph/clear?project_id=...`
- `gcode graph rebuild` → `POST /api/code-index/graph/rebuild?project_id=...`

These commands use the current resolved `Context.project_id`, require a daemon
URL, and fail hard on transport errors, non-2xx responses, or invalid JSON
success bodies. They do not talk to Neo4j directly.

### UUID5 Parity

Symbol IDs are deterministic UUID5 using namespace `c0de1de0-0000-4000-8000-000000000000` and key format `{project_id}:{file_path}:{name}:{kind}:{byte_start}`. This must match the Python daemon's `Symbol.make_id()` exactly — IDs are shared between gcode (Rust) and the Gobby daemon (Python).

## Search Pipeline

**Files:** `src/search/{fts,semantic,graph_boost,rrf}.rs`, `src/commands/search.rs`

### Hybrid Search (`gcode search`)

Four sources are queried and merged via Reciprocal Rank Fusion:

```
Source 1: FTS5 (SQLite full-text search)
  → search_symbols_fts (MATCH query on code_symbols_fts)
  → fallback: search_symbols_by_name (LIKE query)

Source 2: Semantic (Qdrant vector search)
  → embed query text via an OpenAI-compatible /v1/embeddings endpoint
  → POST to Qdrant /collections/{name}/points/search
  → returns (symbol_id, score) pairs

Source 3: Graph Boost (Neo4j)
  → find_callers + find_usages for query term
  → returns symbol IDs that are connected in the call/import graph

Source 4: Graph Expand (Neo4j)
  → seed from top FTS + semantic hits
  → expand through callees first, then callers

  ↓ All sources → RRF merge → Symbol resolution → Path filter (glob) → Pagination
```

When `--path` is provided, FTS queries include a SQL `LIKE` prefix pre-filter for index-assisted narrowing. After RRF merge and symbol resolution, a Rust `glob::Pattern` post-filter ensures exact glob semantics across all sources (including semantic/graph results that lack SQL-side filtering).

### RRF Merge (rrf.rs)

Reciprocal Rank Fusion with K=60:

```
score(symbol) = Σ 1/(K + rank) for each source containing the symbol
```

- Rank 0 is best (first in source list)
- Single-source max score: 1/60 ≈ 0.0167
- Multi-source: scores are additive across sources
- Results sorted by combined score, descending
- Source attribution preserved (e.g., `["fts", "graph_expand"]`)

### Symbol Resolution

After RRF merge, ALL symbol IDs are resolved against SQLite before computing `total`. This ensures `total` reflects the count of actually-resolvable symbols (stale Qdrant/Neo4j entries are silently skipped). Offset/limit pagination is applied after resolution.

The `total` for hybrid search is a best-effort estimate bounded by `fetch_limit`
per source — exact counts aren't feasible because RRF merges results from
multiple systems with deduplication.

### FTS Search (`search-text`, `search-content`)

These use dedicated `count_text`/`count_content` functions (FTS5 COUNT queries) for accurate totals, separate from the paginated result fetch.

### Pagination

All search/graph commands return a `PagedResponse` envelope:

```json
{
  "project_id": "uuid",
  "total": 47,
  "offset": 0,
  "limit": 10,
  "results": [...],
  "hint": null
}
```

- `--offset N` skips the first N results
- `--limit N` caps results per page (default: 10)
- `hint` is populated when Neo4j is unavailable (graph commands only)
- Text mode shows a pagination footer: `-- 10 of 47 results (use --offset 10 for more)`

## Database Schema

### Core Tables

**`code_symbols`** — Extracted AST symbols

| Column | Type | Notes |
|--------|------|-------|
| id | TEXT PK | UUID5 (deterministic, matches Python) |
| project_id | TEXT | Project identifier |
| file_path | TEXT | Relative to project root |
| name | TEXT | Symbol name |
| qualified_name | TEXT | `parent.name` for methods |
| kind | TEXT | function, class, method, type, etc. |
| language | TEXT | python, rust, etc. |
| byte_start, byte_end | INTEGER | Byte offsets for source extraction |
| line_start, line_end | INTEGER | 1-indexed line numbers |
| signature | TEXT | First line of definition (≤200 chars) |
| docstring | TEXT | Python/JS/TS only |
| parent_symbol_id | TEXT | Enclosing class/type ID |
| content_hash | TEXT | SHA-256 of symbol source |
| created_at, updated_at | TEXT | Epoch seconds as string |

**`code_indexed_files`** — File index metadata

| Column | Type | Notes |
|--------|------|-------|
| id | TEXT PK | UUID5(project_id:file_path) |
| project_id | TEXT | |
| file_path | TEXT | Relative path |
| language | TEXT | Detected language |
| content_hash | TEXT | SHA-256 for incremental detection |
| symbol_count | INTEGER | |
| byte_size | INTEGER | |
| indexed_at | TEXT | Epoch seconds |
| graph_synced | INTEGER | 0=pending, 1=Neo4j synced (Gobby mode only) |
| vectors_synced | INTEGER | 0=pending, 1=Qdrant synced (Gobby mode, daemon migration v183) |

**`code_imports`** — Import relations (daemon migration v183, Gobby mode only)

| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER PK | Auto-increment |
| project_id | TEXT | |
| source_file | TEXT | File that contains the import |
| target_module | TEXT | Imported module name |

UNIQUE constraint on `(project_id, source_file, target_module)`.

**`code_calls`** — Call relations (daemon migration v183, Gobby mode only)

| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER PK | Auto-increment |
| project_id | TEXT | |
| caller_symbol_id | TEXT | UUID5 of calling symbol |
| callee_symbol_id | TEXT | UUID5 of the resolved callee, or empty string |
| callee_name | TEXT | Display name of called symbol/function |
| callee_target_kind | TEXT | `symbol`, `unresolved`, or `external` |
| callee_external_module | TEXT | External package/module for `external` targets |
| file_path | TEXT | File containing the call |
| line | INTEGER | Line number of call site |

**`code_content_chunks`** — File content for FTS search

| Column | Type | Notes |
|--------|------|-------|
| id | TEXT PK | UUID5(project_id:file_path:chunk:N) |
| project_id | TEXT | |
| file_path | TEXT | |
| chunk_index | INTEGER | Sequential per file |
| line_start, line_end | INTEGER | 1-indexed, inclusive |
| content | TEXT | Chunk text (100 lines, 10-line overlap) |
| language | TEXT | |

**`code_symbols_fts`** / **`code_content_fts`** — FTS5 virtual tables for full-text search

**`code_indexed_projects`** — Project statistics

**`config_store`** — Key-value configuration (Gobby mode only)

## Neo4j Graph Model

### Nodes

- **CodeSymbol**: `{id, name, kind, project, line_start}`
- **UnresolvedCallee**: `{id, name, project}` placeholder for unresolved call targets
- **ExternalSymbol**: `{id, name, module, project}` placeholder for external package/module calls
- **CodeFile**: `{path, project}`
- **CodeModule**: `{name}`

### Edges

- **DEFINES**: `CodeFile -[:DEFINES]-> CodeSymbol` (file defines symbol)
- **CALLS**: `CodeSymbol -[:CALLS {file, line}]-> (CodeSymbol|UnresolvedCallee|ExternalSymbol)` (call relationship)
- **IMPORTS**: `CodeFile -[:IMPORTS]-> CodeModule` (import relationship)

### Query Patterns

- **Callers**: `MATCH (caller)-[:CALLS]->(target {id, project}) RETURN caller`
- **Usages**: `MATCH (source:CodeSymbol)-[:CALLS]->(target {id, project}) RETURN source`
- **Imports**: `MATCH (f:CodeFile {path, project})-[:IMPORTS]->(m:CodeModule)`
- **Blast Radius**: Variable-length `CALLS` traversal with depth limit. Returns `affected.line_start AS line` for symbol line numbers.

Count queries use the same patterns with `RETURN count(...)` for accurate pagination totals.

### Symbol Name Resolution

**File:** `src/search/fts.rs` (`resolve_symbol_name`), `src/commands/graph.rs` (`resolve_name`)

All graph commands resolve user input to an actual symbol name before querying Neo4j. Resolution order:

1. **Exact match** — `SELECT name FROM code_symbols WHERE name = ?`
2. **LIKE match** — `WHERE name LIKE %input% OR qualified_name LIKE %input%`
3. **FTS5 search** — `search_symbols_fts()` across names, signatures, docstrings

Single match → used directly. Multiple matches → first used, alternatives shown on stderr. No match → error message, no Neo4j query issued.

## Semantic Search Integration

**File:** `src/search/semantic.rs`

### Embedding Request

- **Endpoint**: OpenAI-compatible `/v1/embeddings`
- **Config**: `GOBBY_EMBEDDING_URL` / `embeddings.api_base`
- **Model**: `GOBBY_EMBEDDING_MODEL` / `embeddings.model` / default `nomic-embed-text`
- **Auth**: optional bearer token via `GOBBY_EMBEDDING_API_KEY` / `embeddings.api_key`
- **Task prefix**: `search_query: ` for query embeddings

### Vector Lifecycle

1. **Index**: SQLite writes mark files dirty for external sync; the daemon or direct-sync path handles vector upserts when configured
2. **Re-index**: stale file cleanup and invalidation trigger corresponding Qdrant cleanup when the external sync path runs
3. **Search**: embed query text, search Qdrant, return `(symbol_id, score)` pairs

### Collection Naming

`{collection_prefix}{project_id}` — default prefix is `code_symbols_` from Qdrant config.

## Graceful Degradation

Each external service degrades independently:

| Service | When Unavailable | Impact |
|---------|-----------------|--------|
| Neo4j | No config or connection refused | Graph commands return `[]` with hint; search loses graph boost |
| Qdrant | No URL configured | Search loses semantic source; FTS5 still works |
| Embeddings API | No API base, auth failure, or request error | Semantic search disabled for that query |
| Daemon | Not running | `invalidate` can't notify; direct external sync runs only if Neo4j/Qdrant are configured |

The system always works with just SQLite — FTS5 search and outline are fully functional in standalone mode.

## Output Format

### Default (Slim)

- **Search**: `id`, `name`, `qualified_name`, `kind`, `file_path`, `line_start`, `score`, `signature`, `sources`
- **Outline**: `id`, `name`, `kind`, `line_start`, `line_end`, `signature` (6 fields vs full Symbol)
- **Graph**: `id`, `name`, `file_path`, `line`, `relation`, `distance`

### Verbose (`--verbose`)

- **Outline**: Returns full `Symbol` struct with all fields

Fields never shown even in verbose: `content_hash`, `created_at`, `updated_at`, `byte_start`, `byte_end`. `project_id` is hoisted to the `PagedResponse` envelope.

## Use Cases

### Agent Search Workflow

1. `gcode search "auth middleware"` → ranked results with file:line, signature
2. Pick result → `gcode symbol <id>` (exact source code) or `Read file_path offset=line_start`
3. Need more? → `gcode search "auth middleware" --offset 10`

### File Survey

1. `gcode outline src/config.rs` → slim symbol list (name, kind, lines, signature)
2. Identify relevant functions → `gcode symbol <id>` for source code

### Impact Analysis

1. `gcode blast-radius "handleAuth" --depth 3` → transitive dependents
2. `gcode callers "handleAuth"` → direct call sites
3. `gcode usages "DatabasePool"` → all references (calls + imports)

### Cross-Project Queries

```bash
gcode search --project myapp "query"        # by folder name
gcode search --project /path/to/myapp "query"  # by path
```

### Full Reindex

```bash
gcode index --full    # re-process all files, clean stale vectors
gcode invalidate      # destructive reset (drops all data, re-create)
```
