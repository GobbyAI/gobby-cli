---
title: crates/gcode/src/commands/status.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/status.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/status.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

`crates/gcode/src/commands/status.rs` exposes 38 indexed API symbols.

## How it fits

`crates/gcode/src/commands/status.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `format_timestamp` | function | Returns '"never"' for an empty input, formats an all-digit string as a naive UTC timestamp from epoch seconds, truncates ISO-8601-like strings to the first 19 characters with 'T' replaced by a space, and otherwise returns the input unchanged. [crates/gcode/src/commands/status.rs:18-42] |
| `days_to_ymd` | function | Converts an 'i64' count of days since the Unix epoch into a Gregorian '(year, month, day)' date using Howard Hinnant’s civil-from-days algorithm with a '719468'-day offset. [crates/gcode/src/commands/status.rs:45-58] |
| `run` | function | Queries the readonly database for the current project’s indexed-project record and prints it in either JSON or human-readable text, augmenting JSON with overlay status when available and formatting basic index statistics such as root path, file/symbol counts, last indexed time, and duration. [crates/gcode/src/commands/status.rs:60-134] |
| `overlay_status_json` | function | Returns 'None' unless 'ctx.index_scope' is an 'Overlay', otherwise builds and returns a JSON object containing the overlay and parent project/root IDs plus a 'tombstones' field when 'visibility::tombstone_count(conn, ctx)' is greater than zero. [crates/gcode/src/commands/status.rs:136-158] |
| `invalidate` | function | Prompts for confirmation unless 'force' is true, then opens a read-write database connection, invalidates the project’s code index via the indexer using the project ID and optional daemon URL, and finishes by cleaning up project projections. [crates/gcode/src/commands/status.rs:160-185] |
| `cleanup_project_projections` | function | Clears the project's FalkorDB projection when 'ctx.falkordb' is present and deletes the project's Qdrant collection when 'ctx.qdrant' is set, mapping any backend errors into contextual 'anyhow' failures. [crates/gcode/src/commands/status.rs:187-197] |
| `collect_projects` | function | Queries 'code_indexed_projects' in descending 'last_indexed_at' order, converts each row into an 'IndexedProject', filters out duplicate IDs with a 'HashSet', and returns the deduplicated list or an error. [crates/gcode/src/commands/status.rs:200-227] |
| `indexed_project_from_row` | function | Builds an 'IndexedProject' from a PostgreSQL row by extracting typed columns, converting 'i64' counts to 'usize'/'u64', defaulting a missing 'last_indexed_at' string to '""', and mapping an optional 'total_eligible_files' to 'Option<usize>'. [crates/gcode/src/commands/status.rs:229-245] |
| `format_coverage` | function | Formats coverage as 'indexed/eligible (pct%)' when 'eligible' is 'Some(total > 0)', otherwise returns just the 'indexed' count as a string. [crates/gcode/src/commands/status.rs:248-256] |
| `display_name` | function | Returns a human-readable project label using the root directory basename and a shortened ID when 'root_path' is a non-empty absolute path, otherwise falls back to '"<unknown> (id)"'. [crates/gcode/src/commands/status.rs:259-268] |
| `projects` | function | Collects all indexed projects and emits them as JSON or as human-readable text, printing a no-projects warning to stderr when the list is empty. [crates/gcode/src/commands/status.rs:271-293] |
| `is_stale` | function | Returns 'Some' with a static reason string when the project is a sentinel entry, has an empty or non-absolute 'root_path', or points to a path that does not exist, and otherwise returns 'None'. [crates/gcode/src/commands/status.rs:296-310] |
| `StaleProject` | class | 'StaleProject<'a>' is a borrowed wrapper around an 'IndexedProject' that pairs the project reference with a 'String' explaining why the project is considered stale. [crates/gcode/src/commands/status.rs:313-316] |
| `ProjectionCleanupScope` | type | Indexed type `ProjectionCleanupScope` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:319-322] |
| `ProjectionPruneTotals` | class | 'ProjectionPruneTotals' is a struct of 'usize' counters summarizing prune activity for graph and vector projections, including how many projects were cleaned or skipped and how many stale/orphan files, nodes, and vectors were deleted. [crates/gcode/src/commands/status.rs:325-334] |
| `ProjectionPruneTotals::record_graph_cleanup` | method | Increments the graph-cleanup counters by one project and accumulates the number of stale files and graph nodes deleted from the provided 'GraphOrphanCleanup' result. [crates/gcode/src/commands/status.rs:337-341] |
| `ProjectionPruneTotals::record_vector_cleanup` | method | Increments the cleanup counters by one and accumulates the deleted orphan files and deleted vectors from the provided 'VectorOrphanCleanup' into the struct’s running totals. [crates/gcode/src/commands/status.rs:343-347] |
| `ProjectionPruneTotals::add` | method | Adds the corresponding counters from 'other' into 'self' for all projection-prune totals, accumulating graph and vector cleaned/skipped/deleted metrics in place. [crates/gcode/src/commands/status.rs:349-358] |
| `projection_cleanup_scope` | function | Returns 'ProjectionCleanupScope::ResolvedProjectOverride' when 'project_override' is 'Some', otherwise returns 'ProjectionCleanupScope::AllIndexedProjects'. [crates/gcode/src/commands/status.rs:361-367] |
| `stale_projects` | function | Returns all projects deemed stale either because 'is_stale(project)' reports a reason or because they share a canonicalized root with another project and are superseded by the current project identity, tagging each with the corresponding stale reason. [crates/gcode/src/commands/status.rs:369-423] |
| `prune` | function | Returns early if 'prune_stale_projects(force)' removes nothing, otherwise determines the projection cleanup scope from 'project_override' and prunes either all indexed project projections or only the resolved override’s projections, propagating any error. [crates/gcode/src/commands/status.rs:426-437] |
| `prune_resolved_project_projections` | function | Resolves the current project context using the projection-cleanup service configuration and, if successful, prunes that project’s projections; if no project is set and the context is missing, it returns 'Ok(())', otherwise it propagates the error. [crates/gcode/src/commands/status.rs:439-452] |
| `prune_stale_projects` | function | 'prune_stale_projects' collects projects, identifies stale ones, reports them, optionally prompts for confirmation unless 'force' is set, invalidates each stale project's indexed data in the database via the daemon URL, and returns 'Ok(Some(count))' for pruned entries, 'Ok(Some(0))' when none are stale, or 'Ok(None)' if the user aborts. [crates/gcode/src/commands/status.rs:454-494] |
| `prune_all_project_projections` | function | Collects all indexed projects and, for each one, resolves a projection-cleanup context and prunes orphaned projections while accumulating and printing totals, warning on per-project resolution failures and exiting early if no projects remain. [crates/gcode/src/commands/status.rs:496-520] |

_11 more symbol(s) not shown — run `gcode outline crates/gcode/src/commands/status.rs` for the full list._

_Verified by 3 in-file unit tests._

