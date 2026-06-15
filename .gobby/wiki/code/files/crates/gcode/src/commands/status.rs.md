---
title: crates/gcode/src/commands/status.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/status.rs
  ranges:
  - 18-42
  - 45-58
  - 60-134
  - 136-158
  - 160-185
  - 187-197
  - 200-227
  - 229-245
  - 248-256
  - 259-268
  - 271-293
  - 296-310
  - 313-316
  - 318-372
  - 375-389
  - 391-431
  - 433-457
  - 459-466
  - 468-481
  - 483-487
  - 489-529
  - 535-545
  - 547-561
  - 564-582
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/status.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

This file implements the `gcode` status and cleanup commands around indexed projects. It formats timestamps, converts DB rows into `IndexedProject` records, and provides helpers for display names, coverage strings, staleness checks, and project collection so the command handlers can report project status, list projects, and render repo outlines in text or JSON.

It also supports maintenance flows: `run` reads the current project’s indexing stats, `projects` and `repo_outline` print inventory views, `stale_projects` and `prune_stale_projects` find and invalidate broken or duplicate projects, and `prune_current_project_projections` cleans orphaned graph/vector data through the graph and vector backends. Supporting helpers like `cleanup_project_projections`, `overlay_status_json`, and `write_project_json` tie the status output to overlay metadata, project initialization, and backend cleanup.
[crates/gcode/src/commands/status.rs:18-42]
[crates/gcode/src/commands/status.rs:45-58]
[crates/gcode/src/commands/status.rs:60-134]
[crates/gcode/src/commands/status.rs:136-158]
[crates/gcode/src/commands/status.rs:160-185]

## API Symbols

- `format_timestamp` (function) component `format_timestamp [function]` (`7027693a-1411-5ccd-90be-cc3810418e85`) lines 18-42 [crates/gcode/src/commands/status.rs:18-42]
  - Signature: `fn format_timestamp(raw: &str) -> String {`
  - Purpose: Parses epoch seconds or ISO 8601 timestamp strings and normalizes them to YYYY-MM-DD HH:MM:SS UTC format, returning "never" for empty input or the original string if neither format matches. [crates/gcode/src/commands/status.rs:18-42]
- `days_to_ymd` (function) component `days_to_ymd [function]` (`a2c86830-61ee-56e0-a451-271f26a16c3a`) lines 45-58 [crates/gcode/src/commands/status.rs:45-58]
  - Signature: `fn days_to_ymd(mut days: i64) -> (i64, i64, i64) {`
  - Purpose: Converts an integer day count to proleptic Gregorian calendar date components (year, month, day) using the Hinnant algorithm. [crates/gcode/src/commands/status.rs:45-58]
- `run` (function) component `run [function]` (`bfc1cae3-4c00-5c73-9dc5-dce66f0eec85`) lines 60-134 [crates/gcode/src/commands/status.rs:60-134]
  - Signature: `pub fn run(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: # Summary

This function queries the `code_indexed_projects` table to retrieve indexing statistics (file count, symbol count, timestamp, duration) for a project and outputs the results in either JSON or prettified text format based on the provided `Format` parameter. [crates/gcode/src/commands/status.rs:60-134]
- `overlay_status_json` (function) component `overlay_status_json [function]` (`a7f6bfd3-9618-5f95-8de9-75d4a7e252a7`) lines 136-158 [crates/gcode/src/commands/status.rs:136-158]
  - Signature: `fn overlay_status_json(ctx: &Context, conn: &mut postgres::Client) -> Option<serde_json::Value> {`
  - Purpose: Constructs and returns a JSON object containing overlay project metadata and tombstone count if the context's index scope is an overlay configuration, otherwise returns `None`. [crates/gcode/src/commands/status.rs:136-158]
- `invalidate` (function) component `invalidate [function]` (`0f76d4c3-4416-5c6a-a6fe-6412539a54ce`) lines 160-185 [crates/gcode/src/commands/status.rs:160-185]
  - Signature: `pub fn invalidate(ctx: &Context, force: bool) -> anyhow::Result<()> {`
  - Purpose: Invalidates the code index for a project with optional user confirmation, then cleans up associated projections from the database. [crates/gcode/src/commands/status.rs:160-185]
- `cleanup_project_projections` (function) component `cleanup_project_projections [function]` (`f3af98c0-13ed-574c-9fa7-860777fee0f2`) lines 187-197 [crates/gcode/src/commands/status.rs:187-197]
  - Signature: `fn cleanup_project_projections(ctx: &Context) -> anyhow::Result<()> {`
  - Purpose: Clears the project from FalkorDB's code graph and deletes its vector collection from Qdrant, propagating any errors encountered. [crates/gcode/src/commands/status.rs:187-197]
- `collect_projects` (function) component `collect_projects [function]` (`b8a64763-17fe-5978-849c-212a7193587d`) lines 200-227 [crates/gcode/src/commands/status.rs:200-227]
  - Signature: `fn collect_projects() -> anyhow::Result<Vec<IndexedProject>> {`
  - Purpose: Queries the `code_indexed_projects` database table and returns a deduplicated vector of `IndexedProject` records sorted by descending `last_indexed_at` timestamp. [crates/gcode/src/commands/status.rs:200-227]
- `indexed_project_from_row` (function) component `indexed_project_from_row [function]` (`7da7842b-9070-53f3-af3d-0d4474453982`) lines 229-245 [crates/gcode/src/commands/status.rs:229-245]
  - Signature: `fn indexed_project_from_row(row: &postgres::Row) -> anyhow::Result<IndexedProject> {`
  - Purpose: Deserializes a PostgreSQL row into an `IndexedProject` struct by extracting typed columns, converting `i64` values to `usize`/`u64`, and applying defaults to optional fields. [crates/gcode/src/commands/status.rs:229-245]
- `format_coverage` (function) component `format_coverage [function]` (`d985b558-527d-54b5-b16c-83529d40b856`) lines 248-256 [crates/gcode/src/commands/status.rs:248-256]
  - Signature: `fn format_coverage(indexed: usize, eligible: Option<usize>) -> String {`
  - Purpose: Formats a coverage ratio as `indexed/eligible (percentage%)` when an eligible count is provided and positive, otherwise returns only the indexed count as a string. [crates/gcode/src/commands/status.rs:248-256]
- `display_name` (function) component `display_name [function]` (`fab3b435-7199-5e13-bf61-58fdb3c43510`) lines 259-268 [crates/gcode/src/commands/status.rs:259-268]
  - Signature: `fn display_name(p: &IndexedProject) -> String {`
  - Purpose: Constructs a display string from an `IndexedProject`'s directory basename and abbreviated ID, defaulting to `<unknown>` for invalid or relative root paths. [crates/gcode/src/commands/status.rs:259-268]
- `projects` (function) component `projects [function]` (`a87c6b68-c8ad-56f5-8165-55fa8584c3e4`) lines 271-293 [crates/gcode/src/commands/status.rs:271-293]
  - Signature: `pub fn projects(format: Format) -> anyhow::Result<()> {`
  - Purpose: Collects indexed projects and outputs them in either JSON or text format, displaying project path, file coverage statistics, symbol count, and last-indexed timestamp. [crates/gcode/src/commands/status.rs:271-293]
- `is_stale` (function) component `is_stale [function]` (`bcd80e7e-aab0-57be-88c2-e05d8885d0c2`) lines 296-310 [crates/gcode/src/commands/status.rs:296-310]
  - Signature: `fn is_stale(p: &IndexedProject) -> Option<&'static str> {`
  - Purpose: Returns `None` if an `IndexedProject` is valid (non-sentinel ID with an absolute, existing root path), or `Some` with a descriptive error message indicating why the project is stale. [crates/gcode/src/commands/status.rs:296-310]
- `StaleProject` (class) component `StaleProject [class]` (`64197fa3-d771-51b1-8afc-a20cda7fe2c8`) lines 313-316 [crates/gcode/src/commands/status.rs:313-316]
  - Signature: `struct StaleProject<'a> {`
  - Purpose: `StaleProject` is a struct that pairs a borrowed reference to an `IndexedProject` with a `String` reason explaining why that project is considered stale. [crates/gcode/src/commands/status.rs:313-316]
- `stale_projects` (function) component `stale_projects [function]` (`375b29cf-84b3-59b6-a648-ecbf26843370`) lines 318-372 [crates/gcode/src/commands/status.rs:318-372]
  - Signature: `fn stale_projects(projects: &[IndexedProject]) -> Vec<StaleProject<'_>> {`
  - Purpose: Identifies and collects stale projects by filtering those failing staleness validation and marking duplicate projects at shared roots as superseded by the resolved project identity. [crates/gcode/src/commands/status.rs:318-372]
- `prune` (function) component `prune [function]` (`deaeb577-543f-579b-8a25-0519c5702ac8`) lines 375-389 [crates/gcode/src/commands/status.rs:375-389]
  - Signature: `pub fn prune(force: bool, project_override: Option<&str>, quiet: bool) -> anyhow::Result<()> {`
  - Purpose: Prunes stale projects first, then resolves the current project context using the projection-cleanup service selection and prunes that project’s projections, treating a missing project context as a no-op when no override is provided. [crates/gcode/src/commands/status.rs:375-389]
- `prune_stale_projects` (function) component `prune_stale_projects [function]` (`8a39767e-8de1-5218-9d75-354f3e796d53`) lines 391-431 [crates/gcode/src/commands/status.rs:391-431]
  - Signature: `fn prune_stale_projects(force: bool) -> anyhow::Result<Option<usize>> {`
  - Purpose: Collects all projects, identifies stale ones, prints them, optionally prompts for confirmation unless 'force' is true, invalidates each stale project’s indexed data in the database via the daemon URL, and returns 'Ok(Some(count))' or 'Ok(None)' if aborted. [crates/gcode/src/commands/status.rs:391-431]
- `prune_current_project_projections` (function) component `prune_current_project_projections [function]` (`1977c2ec-dcd1-57c0-94a6-908d72d4cef6`) lines 433-457 [crates/gcode/src/commands/status.rs:433-457]
  - Signature: `fn prune_current_project_projections(ctx: &Context) -> anyhow::Result<()> {`
  - Purpose: Prunes orphaned graph and vector projections for the current project by invoking 'prune_graph_orphans' and 'prune_vector_orphans', logging cleanup, configuration-skipped, or warning messages for each, and always returning 'Ok(())'. [crates/gcode/src/commands/status.rs:433-457]
- `prune_graph_orphans` (function) component `prune_graph_orphans [function]` (`4ee88b33-5678-5b25-ada7-cf30ac7d882d`) lines 459-466 [crates/gcode/src/commands/status.rs:459-466]
  - Signature: `fn prune_graph_orphans(`
  - Purpose: Returns 'Ok(None)' when 'ctx.falkordb' is absent, otherwise runs 'cleanup_deleted_project_graph(ctx)' and wraps its 'GraphOrphanCleanup' result in 'Some'. [crates/gcode/src/commands/status.rs:459-466]
- `prune_vector_orphans` (function) component `prune_vector_orphans [function]` (`a39809c1-44f3-566f-953d-c780fb0da6d1`) lines 468-481 [crates/gcode/src/commands/status.rs:468-481]
  - Signature: `fn prune_vector_orphans(`
  - Purpose: Returns 'Ok(None)' when no Qdrant client is configured; otherwise it opens a read-only database connection, collects the project’s indexed file paths into a 'HashSet', and delegates to 'code_symbols::cleanup_orphan_file_vectors' to remove orphaned vector entries, wrapping the cleanup result in 'Some' and converting errors to 'anyhow::Error'. [crates/gcode/src/commands/status.rs:468-481]
- `is_missing_project_context` (function) component `is_missing_project_context [function]` (`e030dfc2-7f94-5b7c-9ee6-c05450347e42`) lines 483-487 [crates/gcode/src/commands/status.rs:483-487]
  - Signature: `fn is_missing_project_context(error: &anyhow::Error) -> bool {`
  - Purpose: Returns 'true' when the error’s string representation contains the exact message '"No gcode project found. Run 'gcode init'"', indicating a missing project context. [crates/gcode/src/commands/status.rs:483-487]
- `repo_outline` (function) component `repo_outline [function]` (`500cecf0-e5ad-5355-bcb7-43f3c75b3639`) lines 489-529 [crates/gcode/src/commands/status.rs:489-529]
  - Signature: `pub fn repo_outline(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: 'repo_outline' opens a read-only database connection, collects the visible repository files into JSON entries containing path, language, and symbol count, groups them by parent directory, and then prints either the grouped structure as JSON or a text summary of file and symbol totals per directory. [crates/gcode/src/commands/status.rs:489-529]
- `indexed_project` (function) component `indexed_project [function]` (`037e9731-a630-5615-95a7-9a47b6809ba8`) lines 535-545 [crates/gcode/src/commands/status.rs:535-545]
  - Signature: `fn indexed_project(id: &str, root_path: &Path) -> IndexedProject {`
  - Purpose: Constructs and returns an 'IndexedProject' with the given 'id' and 'root_path' stringified, and all indexing metrics hardcoded to '1' (including 'total_files', 'total_symbols', 'last_indexed_at', 'index_duration_ms', and 'total_eligible_files'). [crates/gcode/src/commands/status.rs:535-545]
- `write_project_json` (function) component `write_project_json [function]` (`11844013-6359-5063-9565-aad5694059f3`) lines 547-561 [crates/gcode/src/commands/status.rs:547-561]
  - Signature: `fn write_project_json(root: &Path, id: &str) {`
  - Purpose: Creates 'root/.gobby' if needed and writes a 'project.json' file containing the project 'id', a fixed '"project"' name, and the parent project path and id derived from 'root' and 'id'. [crates/gcode/src/commands/status.rs:547-561]
- `duplicate_root_prune_detection_keeps_resolved_project_id` (function) component `duplicate_root_prune_detection_keeps_resolved_project_id [function]` (`34dd2cc2-48c1-575f-848f-eb410a0b9d8b`) lines 564-582 [crates/gcode/src/commands/status.rs:564-582]
  - Signature: `fn duplicate_root_prune_detection_keeps_resolved_project_id() {`
  - Purpose: Verifies that when two indexed projects share the same canonical root, 'stale_projects' prunes only the duplicate stale entry and preserves the resolved current project ID. [crates/gcode/src/commands/status.rs:564-582]

