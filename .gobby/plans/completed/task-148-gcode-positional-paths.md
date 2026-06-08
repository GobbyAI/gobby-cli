# gcode search: positional path filters

## Overview

Add ripgrep-style positional `[PATHS...]` arguments to `gcode search`, `gcode search-text`, and `gcode search-content` so a user can scope a query to one or more directories or globs after the query string. Today the three FTS-backed search subcommands accept exactly one path filter via the `--path` flag (single `Option<String>`), and passing extra positional paths fails:

```
$ gcode search-content "permissionDecisionReason" --limit 20 --format text src/gobby tests
error: unexpected argument 'src/gobby' found
```

Goal: `gcode search-content "QUERY" src/gobby tests crates/ghook` works and returns hits scoped to those subtrees, with the same shape applied uniformly across all three search subcommands.

## Constraints

- Backwards-compatible with `--path` — the existing flag continues to work and is merged into the same paths list.
- OR semantics across multiple paths: a hit is returned if its `file_path` matches **any** supplied pattern.
- Bare non-glob path args expand to two patterns (`arg` exact match + `arg/**` subtree) so a path like `src/gobby` matches files inside the directory without requiring fs probes.
- No JSON output schema changes — `PagedResponse` and `ContentSearchHit` / `SearchResult` / `SymbolMetaHit` are unchanged.
- Consistent surface and semantics across `search`, `search-text`, `search-content`.
- No changes to indexing or to graph commands (`callers`, `usages`, `imports`, `blast-radius`); they don't accept `--path` today and are out of scope.

## Phase 1: Multi-path search filters

**Goal**: All three FTS-backed search subcommands accept a positional `[PATHS...]` list (additive with `--path`), apply OR'd glob filtering at the SQL prefix-narrow layer (only when all expanded patterns yield prefixes, with `ESCAPE '\\'`) and at the post-query layer (always, before pagination and totals), and produce identical result schemas. Totals on `search-text` and `search-content` are exact under path filtering; the hybrid `search` total remains best-effort (RRF merge has no exact post-filter total).

### 1.1 Add path-list helpers `expand_paths` and `compile_patterns` in fts.rs [category: code]

Target: `crates/gcode/src/search/fts.rs` (alongside `glob_to_like_prefix` at line 31).

Add two pure helpers used by all FTS callers and by command handlers. They normalize raw user-supplied path strings into glob patterns and compile them.

```rust
/// Normalize raw user-supplied path args into glob patterns.
/// - Empty input → empty output.
/// - Whitespace-only entry → skipped.
/// - Trailing `/` (after right-trim) → stripped, treated as subtree (`arg/**`).
/// - Contains glob meta (`*`, `?`, `[`) → used verbatim (after trim).
/// - Otherwise → expanded to TWO patterns: the literal arg (exact-file match)
///   AND `arg/**` (subtree match). Matches ripgrep "works for files and
///   directories" without fs probes.
pub fn expand_paths(raw: &[String]) -> Vec<String> {
    let mut out = Vec::with_capacity(raw.len() * 2);
    for p in raw {
        // Trim outer whitespace first so `"   "` is detected as empty before
        // any trailing-slash logic runs.
        let outer = p.trim();
        if outer.is_empty() {
            continue;
        }
        let trailing_slash = outer.ends_with('/');
        let trimmed = outer.trim_end_matches('/');
        if trimmed.is_empty() {
            continue;
        }
        let has_meta = trimmed.contains(|c: char| matches!(c, '*' | '?' | '['));
        if has_meta {
            out.push(trimmed.to_string());
        } else if trailing_slash {
            out.push(format!("{trimmed}/**"));
        } else {
            out.push(trimmed.to_string());
            out.push(format!("{trimmed}/**"));
        }
    }
    out
}

pub fn compile_patterns(patterns: &[String]) -> anyhow::Result<Vec<glob::Pattern>> {
    patterns
        .iter()
        .map(|s| glob::Pattern::new(s).map_err(|e| anyhow::anyhow!("invalid path glob `{s}`: {e}")))
        .collect()
}
```

Behavioral specs:
- `expand_paths(&[])` → `[]`.
- `expand_paths(&["   ".into()])` → `[]`.
- `expand_paths(&["src/foo".into()])` → `["src/foo", "src/foo/**"]`.
- `expand_paths(&["src/foo/".into()])` → `["src/foo/**"]`.
- `expand_paths(&["src/**/*.rs".into()])` → `["src/**/*.rs"]`.
- `expand_paths(&["*.rs".into()])` → `["*.rs"]`.
- `expand_paths(&["src/main.rs".into()])` → `["src/main.rs", "src/main.rs/**"]` (the `/**` form harmlessly matches nothing).
- `expand_paths(&["  src/foo  ".into()])` → `["src/foo", "src/foo/**"]` (outer whitespace trimmed).
- `compile_patterns` propagates the first invalid-glob error with the offending pattern in the message: `invalid path glob `[`: ...`.

### 1.2 Migrate FTS layer and command handlers to multi-path in lockstep [category: code] (depends: 1.1)

Target: `crates/gcode/src/search/fts.rs` and `crates/gcode/src/commands/search.rs`. This is one task — covering both modules — because changing FTS signatures without simultaneously updating all callers leaves the tree non-compiling between TDD wrappers, which masks failures and breaks incremental testing.

#### Functions to migrate (`crates/gcode/src/search/fts.rs`)

All six functions that currently take `path: Option<&str>` change to `paths: &[String]`. Order in this list mirrors the file:

| Fn | Line | Notes |
|----|------|-------|
| `search_symbols_fts` | 65 | symbol FTS5; SQL narrows on `cs.file_path LIKE ?` |
| `search_symbols_by_name` | 111 | LIKE fallback; SQL narrows on `file_path LIKE ?` |
| `count_text` | 249 | symbol count, FTS5 + LIKE-fallback branches |
| `count_content` | 435 | content count, FTS5 + LIKE-fallback branches |
| `search_text` | 494 | thin wrapper over `search_symbols_fts` + `search_symbols_by_name` |
| `search_content` | 509 | content FTS5; SQL narrows on `c.file_path LIKE ?`, plus LIKE-fallback branch |

Each function's signature changes from `path: Option<&str>` to `paths: &[String]`, in the same parameter slot. (`search_symbols_fts` and `search_symbols_by_name` keep their `kind: Option<&str>` parameter unchanged.)

#### SQL narrowing rule (the load-bearing correctness fix)

Replace the existing single-LIKE block:

```rust
// OLD
if let Some(like) = path.and_then(glob_to_like_prefix) {
    conditions.push("cs.file_path LIKE ?".to_string()); // alias varies by callsite
    params.push(Box::new(like));
}
```

with this conservative multi-pattern rule. **Only apply SQL prefix narrowing when EVERY expanded pattern yields a non-`None` LIKE prefix.** If any pattern is non-prefixable (e.g. `*.rs`, `**/main.rs`), skip SQL narrowing entirely and let post-query glob filtering enforce correctness. Every emitted path predicate must include `ESCAPE '\\'` because `glob_to_like_prefix` calls `escape_like` which inserts `\%` and `\_` — without the escape clause, a literal directory like `src/foo_bar` is treated as a wildcard pattern by SQLite and gets narrowed out:

```rust
// NEW
let prefixes: Option<Vec<String>> = paths
    .iter()
    .map(|p| glob_to_like_prefix(p))
    .collect(); // None if any element is None
if let Some(likes) = prefixes {
    if !likes.is_empty() {
        // ESCAPE '\\' is required: escape_like inserts \% and \_ for literal
        // metacharacters; SQLite needs the escape declared explicitly.
        let placeholders = likes
            .iter()
            .map(|_| "cs.file_path LIKE ? ESCAPE '\\'")
            .collect::<Vec<_>>()
            .join(" OR ");
        conditions.push(format!("({placeholders})"));
        for like in likes {
            params.push(Box::new(like));
        }
    }
}
```

(Use the correct table alias per callsite — `cs.` for the symbols joins, `c.` for the content FTS join, no alias for the LIKE-fallback branches that query `code_symbols`/`code_content_chunks` directly. The Rust string literal `"…ESCAPE '\\'"` produces the SQL fragment `…ESCAPE '\'` which is what SQLite expects; do **not** double-escape further.)

**Why the conservative rule:** mixing prefixable and non-prefixable patterns under OR'd LIKE drops valid rows for the non-prefixable patterns before post-query filter sees them. Example: paths `src/**` (prefix `src/`) + `*.rs` (no prefix) — narrowing on `cs.file_path LIKE 'src/%'` excludes a root-level `Cargo.toml` matching `*.rs` even though post-query glob filtering would keep it. The rule "all-or-nothing" is the simplest correct fix; rows are still narrowed (by FTS5 MATCH and project_id) and post-query filtering does the rest.

`idx_ccc_file (project_id, file_path)` and the symbols `file_path` indexes remain usable for each individual `LIKE 'prefix%'` branch when the all-prefixable case applies.

Apply this same `prefixes` block to BOTH the FTS5 branch and the LIKE-fallback branch inside `search_content` and `count_content` (and the count_text symmetric pair). Param-bind order must match placeholder order.

#### Internal call sites inside fts.rs

After the signature change, four internal call sites (currently passing `Option<&str>`) need updating:

| Line | Function | Old call | New call |
|------|----------|----------|----------|
| ~238 | `resolve_graph_symbol` | `search_symbols_by_name(conn, input, project_id, None, None, 6)` | `search_symbols_by_name(conn, input, project_id, None, &[], 6)` |
| ~244 | `resolve_graph_symbol` | `search_symbols_fts(conn, input, project_id, None, None, 6)` | `search_symbols_fts(conn, input, project_id, None, &[], 6)` |
| ~501 | `search_text` | `search_symbols_fts(conn, query, project_id, None, path, limit)` | `search_symbols_fts(conn, query, project_id, None, paths, limit)` |
| ~503 | `search_text` | `search_symbols_by_name(conn, query, project_id, None, path, limit)` | `search_symbols_by_name(conn, query, project_id, None, paths, limit)` |

(`resolve_graph_symbol` keeps using an empty slice since it scopes to a symbol input, not a path.)

#### Pagination and counts under path filtering (the second load-bearing correctness fix)

The post-query glob filter must run **before** pagination and **before** totals are reported. Today's handler shape (`fetch_limit = offset + limit` → fetch → post-filter → paginate) drops valid in-path hits whenever the first N FTS-ranked rows fall outside the requested paths; `count_*` similarly returns prefix-superset counts. Both bugs come from filtering after `LIMIT`.

Fix:

1. When `paths` is empty, keep today's behavior — fast path, no overfetch.
2. When `paths` is non-empty, fetch a generous candidate set, post-filter against compiled patterns, then derive both `total` and the page from the filtered set in memory.

Add a constant near the helpers in `fts.rs`:

```rust
/// Maximum candidates fetched from FTS when path filtering is active.
/// Past this cap, totals on `search-text` / `search-content` become
/// approximate. Sized to comfortably cover typical project corpora.
pub const FILTERED_FETCH_CAP: usize = 10_000;
```

Each handler then does count and pagination off the filtered candidate set when `patterns` is non-empty — see the reference shapes below. **The handler does not call `count_*` in the path-filtered branch**; total is `filtered.len()`. Counts are exact up to `FILTERED_FETCH_CAP`; if the cap is hit (i.e. `candidates.len() == FILTERED_FETCH_CAP`), append a `hint: Some("totals capped at <CAP>; refine query or paths for exact counts")` on the JSON response and emit a stderr warning in text mode.

`count_text` and `count_content` keep their new `paths: &[String]` signature for API symmetry (and for callers that want a fast prefix-superset estimate when the cap matters), but path-filtered handlers do not call them.

The hybrid `search` handler is an explicit exception: its `total` is already best-effort because RRF merges FTS / Qdrant / Neo4j sources whose post-filter overlap is non-additive. Document this in the comment that already explains the existing `fetch_limit = ((offset + limit) * 3).max(200)` heuristic — keep that heuristic unchanged but apply post-filter before pagination as before.

#### Command handler migration (`crates/gcode/src/commands/search.rs`)

Change the parameter on all three handlers from `path: Option<&str>` to `paths: &[String]`, expand and compile patterns at the entry, and apply the post-query filter using `any()` **before** pagination and totals. Each handler must compile and pass its own tests at the end of this task — no intermediate non-compiling state.

`commands::search::search` (line 10) — hybrid:

```rust
pub fn search(
    ctx: &Context,
    query: &str,
    limit: usize,
    offset: usize,
    kind: Option<&str>,
    paths: &[String],
    format: Format,
) -> anyhow::Result<()> {
    let conn = db::open_readonly(&ctx.db_path)?;
    let expanded = fts::expand_paths(paths);
    let patterns = fts::compile_patterns(&expanded)?;
    let fetch_limit = ((offset + limit) * 3).max(200);

    let mut fts_results =
        fts::search_symbols_fts(&conn, query, &ctx.project_id, kind, &expanded, fetch_limit);
    if fts_results.is_empty() {
        fts_results =
            fts::search_symbols_by_name(&conn, query, &ctx.project_id, kind, &expanded, fetch_limit);
    }
    // …RRF merge, semantic, graph_boost, graph_expand unchanged…

    // Post-query filter — semantic/graph results lack SQL-side filtering.
    let all_resolved = if patterns.is_empty() {
        all_resolved
    } else {
        all_resolved
            .into_iter()
            .filter(|r| patterns.iter().any(|p| p.matches(&r.file_path)))
            .collect()
    };
    // …pagination, output unchanged…
}
```

`commands::search::search_text` (line 141) and `commands::search::search_content` (line 230) — same shape, but they only call `fts::search_text` + `fts::count_text` and `fts::search_content` + `fts::count_content` respectively. Pass `&expanded` everywhere `path` used to flow.

Reference `search_content` shape:

```rust
pub fn search_content(
    ctx: &Context,
    query: &str,
    limit: usize,
    offset: usize,
    paths: &[String],
    format: Format,
) -> anyhow::Result<()> {
    let conn = db::open_readonly(&ctx.db_path)?;
    let expanded = fts::expand_paths(paths);
    let patterns = fts::compile_patterns(&expanded)?;

    let (results, total, hint): (Vec<ContentSearchHit>, usize, Option<String>) = if patterns.is_empty() {
        // Fast path: today's behavior, with new multi-path-aware fts API.
        let fetch_limit = offset + limit;
        let all = fts::search_content(&conn, query, &ctx.project_id, &expanded, fetch_limit);
        let total = fts::count_content(&conn, query, &ctx.project_id, &expanded);
        let results: Vec<_> = all.into_iter().skip(offset).take(limit).collect();
        (results, total, None)
    } else {
        // Path-filtered: fetch generously, post-filter, derive total from filtered set.
        let candidates = fts::search_content(&conn, query, &ctx.project_id, &expanded, fts::FILTERED_FETCH_CAP);
        let cap_hit = candidates.len() == fts::FILTERED_FETCH_CAP;
        let filtered: Vec<_> = candidates
            .into_iter()
            .filter(|r| patterns.iter().any(|p| p.matches(&r.file_path)))
            .collect();
        let total = filtered.len();
        let results: Vec<_> = filtered.into_iter().skip(offset).take(limit).collect();
        let hint = cap_hit.then(|| format!(
            "totals capped at {}; refine query or paths for exact counts",
            fts::FILTERED_FETCH_CAP
        ));
        (results, total, hint)
    };
    // …unchanged: empty-state messages, JSON output threads `hint` into `PagedResponse.hint`,
    // text mode prints the hint to stderr if present…
}
```

Mirror in `search_text`: same shape, swap `fts::search_content` → `fts::search_text`, `fts::count_content` → `fts::count_text`, `ContentSearchHit` → `SearchResult`.

Hybrid `search` keeps its `fetch_limit = ((offset + limit) * 3).max(200)` heuristic — do not switch to `FILTERED_FETCH_CAP` there. Apply the multi-pattern `any()` post-filter to the merged RRF result set before pagination as the current code already does for the single-pattern case; total stays best-effort.

#### Behavioral specs (whole task)

- Empty `paths` ⇒ no SQL narrowing, no post-query filter, no overfetch; today's behavior preserved across all FTS callsites.
- All `paths` prefixable ⇒ exactly one parenthesized OR'd LIKE block (with `ESCAPE '\\'` per branch) joined to existing conditions with AND, in both FTS5 and LIKE-fallback branches.
- Any pattern in `paths` is non-prefixable ⇒ no SQL narrowing applied; correctness is enforced by post-query `patterns.iter().any(|p| p.matches(&r.file_path))`.
- Multi-pattern hit semantics: a row is kept if its `file_path` matches **any** compiled pattern (`any(...)`).
- Path-filtered pagination & totals: handler fetches up to `FILTERED_FETCH_CAP` candidates, applies post-filter, derives `total = filtered.len()`, then pages. `count_*` is not called in the path-filtered branch.
- Path-filtered cap hit: when `candidates.len() == FILTERED_FETCH_CAP`, `PagedResponse.hint` is set to a clipping warning and text mode prints the hint to stderr.
- Underscore / metachar paths: a literal directory like `src/foo_bar` is **not** narrowed out by SQL because `LIKE … ESCAPE '\\'` honors the `\_` produced by `escape_like`. The post-query glob filter never sees the path predicate's escape behavior.
- Invalid glob ⇒ error from `compile_patterns` propagated as `anyhow::Result`, with the offending pattern in the message.
- The hybrid `search` handler's existing comment block (the `// Source 1: FTS5 …` / `// Source 2: Semantic …` / `// Source 3: Graph boost …` / `// Source 4: Graph expand …` markers and surrounding logic) is preserved; only the path arg threading and the multi-pattern `any()` post-filter change. Total remains best-effort.
- After this task, the workspace builds and existing tests pass: `cargo build -p gobby-code && cargo test -p gobby-code` end with exit 0.

### 1.3 Add positional `[PATHS...]` to clap variants and dispatch [category: code] (depends: 1.2)

Target: `crates/gcode/src/main.rs` — `Search`, `SearchText`, `SearchContent` variants in the `Command` enum (lines 42–164) and the corresponding match arms in `main`.

Add `paths: Vec<String>` as a positional **after** `query: String` and keep the existing `path: Option<String>` flag for backwards compatibility:

```rust
SearchContent {
    /// FTS5 query string.
    query: String,
    /// Paths or globs to scope the search (additive with --path).
    #[arg(num_args = 0..)]
    paths: Vec<String>,
    #[arg(long, default_value = "10")]
    limit: usize,
    #[arg(long, default_value = "0")]
    offset: usize,
    /// Filter by file path glob (deprecated alias; merged into PATHS).
    #[arg(long)]
    path: Option<String>,
},
```

(Mirror on `Search` and `SearchText`. `Search` additionally keeps its `--kind` flag. Do **not** use `trailing_var_arg = true` — it would consume `--limit` etc. as paths.)

In each dispatch arm, merge `--path` into the positional list before calling the handler:

```rust
Command::SearchContent { query, paths, limit, offset, path, .. } => {
    let mut paths = paths;
    if let Some(p) = path { paths.push(p); }
    commands::search::search_content(&ctx, &query, limit, offset, &paths, format)?;
}
```

Same shape for `Search` (also pass `kind.as_deref()`) and `SearchText`.

#### Test coverage for clap parsing

Use `clap::Parser::try_parse_from` directly in unit tests (no need for `assert_cmd` / spawning the binary). Example:

```rust
#[test]
fn search_content_accepts_positional_paths() {
    let cli = Cli::try_parse_from([
        "gcode", "search-content", "QUERY", "src/gobby", "tests",
        "--limit", "20", "--format", "text",
    ]).unwrap();
    match cli.command {
        Command::SearchContent { query, paths, limit, .. } => {
            assert_eq!(query, "QUERY");
            assert_eq!(paths, vec!["src/gobby", "tests"]);
            assert_eq!(limit, 20);
        }
        _ => panic!("expected SearchContent"),
    }
}

#[test]
fn search_content_flag_after_paths_parses() {
    let args = Cli::try_parse_from([
        "gcode", "search-content", "QUERY", "src/gobby", "--limit", "5",
    ]).unwrap();
    // …assert paths = ["src/gobby"], limit = 5
}

#[test]
fn search_content_path_flag_still_works() {
    let args = Cli::try_parse_from([
        "gcode", "search-content", "QUERY", "--path", "crates/ghook/**",
    ]).unwrap();
    // …assert paths is empty AND path == Some("crates/ghook/**")
    // (merge happens at dispatch, not at parse)
}
```

Place these in a `#[cfg(test)] mod tests { use super::*; … }` block at the bottom of `crates/gcode/src/main.rs`. The existing tests already use `Cli::try_parse_from(...)` with `Cli` and `Command` as private types, so the inline-module approach works without making either type `pub`.

#### Behavioral specs (whole task)

- No paths and no `--path` ⇒ unchanged (full-corpus search).
- One positional path ⇒ scoped to that path/subtree.
- Multiple positional paths ⇒ OR'd scoping.
- Positional + `--path "X"` ⇒ all merged into one list before dispatch; OR'd identically.
- Argument order irrelevant — `gcode search-content QUERY src/gobby --limit 20` and `gcode search-content QUERY --limit 20 src/gobby` produce the same parsed shape.
- Help text shows `[PATHS]...` after `<QUERY>` for each subcommand.

#### End-to-end smoke (run after this task lands)

```bash
gcode search-content "permissionDecisionReason" --limit 20 --format text src/gobby tests
gcode search-content "PreToolUse" --format text crates/ghook crates/gcode
gcode search-content "PreToolUse" --format text "crates/**/main.rs"
gcode search-content "PreToolUse" --path "crates/ghook/**" --format text     # backwards compat
gcode search-content "is_blocked" --format text crates/ghook/src/main.rs     # single-file scope
gcode search "Symbol" --format text crates/gcode                             # mirror on `search`
gcode search-text "Symbol" --format text crates/gcode                        # mirror on `search-text`
gcode search-content "PreToolUse" --format text crates/ghook "*.rs"          # mixed prefixable + non-prefixable
```

Each must succeed (exit 0), produce JSON or text output of the expected shape, and scope hits to the supplied paths. The mixed-prefixable case validates the F1 correctness fix from § 1.2.

## Task Mapping

<!-- Updated after task creation -->
| Plan Item | Task Ref | Status |
|-----------|----------|--------|
