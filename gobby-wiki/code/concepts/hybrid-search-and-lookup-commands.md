---
title: Hybrid Search and Lookup Commands
type: code_concept
provenance:
- file: crates/gcode/src/commands/codewiki/architecture_diagrams.rs
- file: crates/gcode/src/commands/codewiki/build_parts/audit.rs
- file: crates/gcode/src/commands/codewiki/cluster.rs
- file: crates/gcode/src/commands/codewiki/io.rs
- file: crates/gcode/src/commands/codewiki/ownership/tests.rs
- file: crates/gcode/src/commands/codewiki/paths.rs
- file: crates/gcode/src/commands/codewiki/prompts.rs
- file: crates/gcode/src/commands/codewiki/relationship_facts.rs
- file: crates/gcode/src/commands/codewiki/system_model.rs
- file: crates/gcode/src/commands/codewiki/text.rs
- file: crates/gcode/src/commands/codewiki/text/citations.rs
- file: crates/gcode/src/commands/codewiki/text/frontmatter.rs
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
- file: crates/gcode/src/commands/codewiki/text/verify.rs
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/commands/embeddings_doctor.rs
- file: crates/gcode/src/commands/graph/lifecycle.rs
- file: crates/gcode/src/commands/graph/reads.rs
- file: crates/gcode/src/commands/graph/tests.rs
- file: crates/gcode/src/commands/grep.rs
- file: crates/gcode/src/commands/grep/grep_matcher.rs
- file: crates/gcode/src/commands/index.rs
- file: crates/gcode/src/commands/search.rs
- file: crates/gcode/src/commands/setup.rs
- file: crates/gcode/src/commands/status.rs
- file: crates/gcode/src/commands/symbol_at.rs
- file: crates/gcode/src/commands/symbols.rs
- file: crates/gcode/src/commands/vector.rs
- file: crates/gcode/src/search/fts/common.rs
- file: crates/gcode/src/search/fts/tests.rs
provenance_truncated: 53
generated_by: gcode-codewiki
trust: generated
freshness: indexed
verify_notes:
- id: 3
  reason: Claims about an older module name and PostgreSQL hub are not shown in the excerpts.
- id: 6
  reason: Mentions CodeWiki generation and vector-index lifecycle without evidence in the supplied sources.
- id: 10
  reason: Attributes many `common.rs` responsibilities that are not shown in the excerpts.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/architecture_diagrams.rs](crates/gcode/src/commands/codewiki/architecture_diagrams.rs)
- [crates/gcode/src/commands/codewiki/build_parts/audit.rs](crates/gcode/src/commands/codewiki/build_parts/audit.rs)
- [crates/gcode/src/commands/codewiki/cluster.rs](crates/gcode/src/commands/codewiki/cluster.rs)
- [crates/gcode/src/commands/codewiki/io.rs](crates/gcode/src/commands/codewiki/io.rs)
- [crates/gcode/src/commands/codewiki/ownership/tests.rs](crates/gcode/src/commands/codewiki/ownership/tests.rs)
- [crates/gcode/src/commands/codewiki/paths.rs](crates/gcode/src/commands/codewiki/paths.rs)
- [crates/gcode/src/commands/codewiki/prompts.rs](crates/gcode/src/commands/codewiki/prompts.rs)
- [crates/gcode/src/commands/codewiki/relationship_facts.rs](crates/gcode/src/commands/codewiki/relationship_facts.rs)
- [crates/gcode/src/commands/codewiki/system_model.rs](crates/gcode/src/commands/codewiki/system_model.rs)
- [crates/gcode/src/commands/codewiki/text.rs](crates/gcode/src/commands/codewiki/text.rs)
- [crates/gcode/src/commands/codewiki/text/citations.rs](crates/gcode/src/commands/codewiki/text/citations.rs)
- [crates/gcode/src/commands/codewiki/text/frontmatter.rs](crates/gcode/src/commands/codewiki/text/frontmatter.rs)

_71 more source files omitted._

</details>

# Hybrid Search and Lookup Commands

## Purpose

Hybrid Search and Lookup Commands connect Gobby’s indexed code data to user-facing lookup workflows. The goal is to give engineers several search modes with different strengths: hybrid symbol search for fuzzy or conceptual queries, BM25 content search for ranked file-content matches, graph-aware ranking when call/import relationships are available, and grep for exact text matching over indexed chunks.

The search facade groups the main ranking pieces under `fts`, `graph_boost`, and `rrf`, while the command layer turns those lower-level search helpers into CLI behavior (`crates/gcode/src/search/mod.rs:1-11`, `crates/gcode/src/commands/search.rs:1-100`). The FTS layer keeps the older module name but executes PostgreSQL `pg_search` BM25 keyword search against the PostgreSQL hub (`crates/gcode/src/search/fts.rs:1-4`).

## Covers / Does not cover

This page covers the indexed search path: PostgreSQL-backed BM25 symbol/content search, graph boost inputs from FalkorDB, reciprocal-rank-style merging in the hybrid search command, and grep-style matching over indexed chunks. It also covers the option objects that define the public command behavior for `gcode search` and `gcode grep` (`crates/gcode/src/commands/search.rs:13-22`, `crates/gcode/src/commands/grep.rs:21-33`).

It does not cover indexing itself, vector index lifecycle, CodeWiki generation, or the full graph database implementation. Those are adjacent command-layer concerns, but the supplied evidence only shows them as dependencies imported by the search commands (`crates/gcode/src/commands/search.rs:1-100`, `crates/gcode/src/commands/grep.rs:1-100`).

| Command surface | Main options shown | Intended use |
| --- | --- | --- |
| `gcode search` | `limit`, `offset`, `kind`, `language`, `paths`, `format`, `with_graph`, `token_budget` | Hybrid/fuzzy symbol search with filters and optional graph participation (`crates/gcode/src/commands/search.rs:13-22`) |
| `gcode grep` | `pattern`, `paths`, `globs`, `fixed_strings`, `ignore_case`, `word`, context limits, `max_count`, `format` | Exact or regex-like matching over indexed content chunks (`crates/gcode/src/commands/grep.rs:21-33`) |
| `gcode search-content` | query, project, optional language, paths, limit | Ranked BM25 search across `code_content_chunks` (`crates/gcode/src/search/fts/content.rs:13-21`) |

## Architecture

The architecture is split between a reusable search facade and command-specific orchestration. The `crates/gcode/src/search` module owns ranking primitives: PostgreSQL BM25 search in `fts`, graph-derived boost candidates in `graph_boost`, and result fusion in `rrf` (`crates/gcode/src/search/mod.rs:1-11`). This lets commands compose search behavior without embedding SQL, graph lookups, and ranking logic directly in the CLI entry points.

The `fts` submodule is the PostgreSQL-facing layer. Shared helpers centralize pg_search query sanitation, trusted BM25 row IDs, SQL parameter binding, count execution, symbol ordering, and reusable filters for project, language, path, and visibility constraints (`crates/gcode/src/search/fts/common.rs:1-100`). Content search builds BM25 queries against `code_content_chunks`, joins `code_indexed_files`, applies filters, and orders by BM25 score plus deterministic tie-breakers (`crates/gcode/src/search/fts/content.rs:1-100`).

The command layer coordinates those primitives with resolved configuration and output rendering. `search` connects to the database, expands path filters, fetches more rows than requested so merged rankings have enough source candidates, then combines exact, BM25, vector, and graph-style results (`crates/gcode/src/commands/search.rs:1-100`). `grep` follows a simpler path: connect read-only, build path/glob filters, load indexed chunks, then run a local matcher over chunk text (`crates/gcode/src/commands/grep.rs:1-100`).

Graph support is deliberately optional. `graph_boost` uses FalkorDB callers and usages as an additional ranked source, but returns an empty list when graph configuration or a database connection is unavailable so lexical search can still produce results (`crates/gcode/src/search/graph_boost.rs:21-47`).

## Data flow

1. A user invokes a command with query text and filters. For hybrid symbol search, those inputs are captured in `SearchOptions`, including pagination, kind/language filters, path filters, output format, graph toggle, and optional token budget (`crates/gcode/src/commands/search.rs:13-22`). For grep, `GrepOptions` captures the pattern, paths, globs, matching flags, context options, count limit, and output format (`crates/gcode/src/commands/grep.rs:21-33`).

2. The command opens a read-only PostgreSQL connection through the resolved `Context`. `grep::run` calls `db::connect_readonly`, builds `GrepFilters`, loads indexed chunks, and passes them to the matcher pipeline (`crates/gcode/src/commands/grep.rs:94-100`). `search` follows the same connection pattern before expanding paths and compiling path patterns (`crates/gcode/src/commands/search.rs:24-33`).

3. Hybrid search expands path constraints and fetches generously for fusion. The command calculates a `fetch_limit` larger than the requested page because final results are merged from multiple sources and deduplicated, so source counts are not simply additive (`crates/gcode/src/commands/search.rs:29-35`).

4. Exact and BM25 symbol search run through the FTS facade. `search` first calls `search_symbols_exact_first_visible`, records whether visible search degraded, then calls `search_symbols_fts_visible` and merges its degraded state into the same flag (`crates/gcode/src/commands/search.rs:36-56`). The FTS helpers are responsible for visibility, project, language, and path filtering (`crates/gcode/src/search/fts/common.rs:1-100`).

5. Content BM25 search sanitizes the query before SQL execution. If the query is blank or the limit is zero, it returns no hits. If sanitation removes all pg_search terms, content BM25 is skipped and the user is directed toward `gcode grep` for exact text (`crates/gcode/src/search/fts/content.rs:22-37`).

6. Content search builds SQL over `code_content_chunks`, joins `code_indexed_files`, filters by project, optional language, and paths, then orders by BM25 score with stable tie-breakers (`crates/gcode/src/search/fts/content.rs:39-72`).

7. Graph boosting tries to resolve the query to a visible symbol, then asks FalkorDB for callers and usages. If FalkorDB is not configured, no PostgreSQL connection is supplied, no symbol resolves, or no neighbors are found, the helper returns an empty list rather than failing the whole hybrid search (`crates/gcode/src/search/graph_boost.rs:21-47`).

8. Grep compiles the user pattern locally. `GrepMatcher::new` rejects empty patterns, escapes fixed-string input when requested, applies case-insensitive compilation when requested, and reports regex build failures as an invalid `gcode grep` pattern (`crates/gcode/src/commands/grep/grep_matcher.rs:11-29`).

9. Grep matching returns spans, not rendered text. `find_spans` runs the regex over each line, ignores zero-width matches, converts matches to `GrepSpan`, and optionally filters to ASCII identifier boundaries for `-w` behavior (`crates/gcode/src/commands/grep/grep_matcher.rs:31-42`, `crates/gcode/src/commands/grep/grep_matcher.rs:72-75`). The parent command can then render matches, context, and metadata consistently through `GrepMatch`, `GrepResult`, and `GrepResponse` (`crates/gcode/src/commands/grep.rs:61-92`).

## Key components

The most important pieces to read are the option bundles at the command boundary, the command entry points that orchestrate backing services, and the small search helpers that define ranking or matching behavior.

| Symbol / module | Role |
| --- | --- |
| `SearchOptions<'a>` | Defines the hybrid search request: pagination, filters, output format, graph inclusion, and token budget (`crates/gcode/src/commands/search.rs:13-22`) |
| `GrepOptions<'a>` | Defines grep matching behavior, scope, context, result limit, and output format (`crates/gcode/src/commands/grep.rs:21-33`) |
| `search_content` | Runs BM25-ranked content search over indexed chunks, with sanitation and path/language filters (`crates/gcode/src/search/fts/content.rs:13-72`) |
| `graph_boost` | Produces graph-related symbol IDs from callers/usages, or an empty list when graph support is unavailable (`crates/gcode/src/search/graph_boost.rs:21-47`) |
| `GrepMatcher` | Compiles and applies grep patterns, returning match spans and optional word-boundary filtering (`crates/gcode/src/commands/grep/grep_matcher.rs:6-42`) |

## Where to start

Start with `crates/gcode/src/commands/search.rs`, especially `SearchOptions` and the beginning of `search`, because it shows how the command composes exact search, BM25, path expansion, graph participation, and result merging (`crates/gcode/src/commands/search.rs:13-56`).

Then read `crates/gcode/src/search/fts/content.rs` for the PostgreSQL BM25 shape, `crates/gcode/src/search/graph_boost.rs` for optional graph behavior, and `crates/gcode/src/commands/grep/grep_matcher.rs` for the exact-text lookup path (`crates/gcode/src/search/fts/content.rs:13-72`, `crates/gcode/src/search/graph_boost.rs:21-47`, `crates/gcode/src/commands/grep/grep_matcher.rs:6-42`).

## Explore

- [[code/modules/crates/gcode/src/search|crates/gcode/src/search]]
- [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]
- [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]
- [[code/modules/crates/gcode/src/commands/grep|crates/gcode/src/commands/grep]]

