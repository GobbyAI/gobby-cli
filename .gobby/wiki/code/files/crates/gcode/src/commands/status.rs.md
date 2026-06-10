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
  - 375-415
  - 417-457
  - 463-473
  - 475-489
  - 492-510
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/status.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

`crates/gcode/src/commands/status.rs` exposes 19 indexed API symbols.
[crates/gcode/src/commands/status.rs:18-42]
[crates/gcode/src/commands/status.rs:45-58]
[crates/gcode/src/commands/status.rs:60-134]
[crates/gcode/src/commands/status.rs:136-158]
[crates/gcode/src/commands/status.rs:160-185]
[crates/gcode/src/commands/status.rs:187-197]
[crates/gcode/src/commands/status.rs:200-227]
[crates/gcode/src/commands/status.rs:229-245]
[crates/gcode/src/commands/status.rs:248-256]
[crates/gcode/src/commands/status.rs:259-268]
[crates/gcode/src/commands/status.rs:271-293]
[crates/gcode/src/commands/status.rs:296-310]
[crates/gcode/src/commands/status.rs:313-316]
[crates/gcode/src/commands/status.rs:318-372]
[crates/gcode/src/commands/status.rs:375-415]
[crates/gcode/src/commands/status.rs:417-457]
[crates/gcode/src/commands/status.rs:463-473]
[crates/gcode/src/commands/status.rs:475-489]
[crates/gcode/src/commands/status.rs:492-510]

## API Symbols

- `format_timestamp` (function) component `format_timestamp [function]` (`7027693a-1411-5ccd-90be-cc3810418e85`) lines 18-42 [crates/gcode/src/commands/status.rs:18-42]
  - Signature: `fn format_timestamp(raw: &str) -> String {`
  - Purpose: Indexed function `format_timestamp` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:18-42]
- `days_to_ymd` (function) component `days_to_ymd [function]` (`a2c86830-61ee-56e0-a451-271f26a16c3a`) lines 45-58 [crates/gcode/src/commands/status.rs:45-58]
  - Signature: `fn days_to_ymd(mut days: i64) -> (i64, i64, i64) {`
  - Purpose: Indexed function `days_to_ymd` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:45-58]
- `run` (function) component `run [function]` (`bfc1cae3-4c00-5c73-9dc5-dce66f0eec85`) lines 60-134 [crates/gcode/src/commands/status.rs:60-134]
  - Signature: `pub fn run(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Indexed function `run` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:60-134]
- `overlay_status_json` (function) component `overlay_status_json [function]` (`a7f6bfd3-9618-5f95-8de9-75d4a7e252a7`) lines 136-158 [crates/gcode/src/commands/status.rs:136-158]
  - Signature: `fn overlay_status_json(ctx: &Context, conn: &mut postgres::Client) -> Option<serde_json::Value> {`
  - Purpose: Indexed function `overlay_status_json` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:136-158]
- `invalidate` (function) component `invalidate [function]` (`0f76d4c3-4416-5c6a-a6fe-6412539a54ce`) lines 160-185 [crates/gcode/src/commands/status.rs:160-185]
  - Signature: `pub fn invalidate(ctx: &Context, force: bool) -> anyhow::Result<()> {`
  - Purpose: Indexed function `invalidate` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:160-185]
- `cleanup_project_projections` (function) component `cleanup_project_projections [function]` (`f3af98c0-13ed-574c-9fa7-860777fee0f2`) lines 187-197 [crates/gcode/src/commands/status.rs:187-197]
  - Signature: `fn cleanup_project_projections(ctx: &Context) -> anyhow::Result<()> {`
  - Purpose: Indexed function `cleanup_project_projections` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:187-197]
- `collect_projects` (function) component `collect_projects [function]` (`b8a64763-17fe-5978-849c-212a7193587d`) lines 200-227 [crates/gcode/src/commands/status.rs:200-227]
  - Signature: `fn collect_projects() -> anyhow::Result<Vec<IndexedProject>> {`
  - Purpose: Indexed function `collect_projects` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:200-227]
- `indexed_project_from_row` (function) component `indexed_project_from_row [function]` (`7da7842b-9070-53f3-af3d-0d4474453982`) lines 229-245 [crates/gcode/src/commands/status.rs:229-245]
  - Signature: `fn indexed_project_from_row(row: &postgres::Row) -> anyhow::Result<IndexedProject> {`
  - Purpose: Indexed function `indexed_project_from_row` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:229-245]
- `format_coverage` (function) component `format_coverage [function]` (`d985b558-527d-54b5-b16c-83529d40b856`) lines 248-256 [crates/gcode/src/commands/status.rs:248-256]
  - Signature: `fn format_coverage(indexed: usize, eligible: Option<usize>) -> String {`
  - Purpose: Indexed function `format_coverage` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:248-256]
- `display_name` (function) component `display_name [function]` (`fab3b435-7199-5e13-bf61-58fdb3c43510`) lines 259-268 [crates/gcode/src/commands/status.rs:259-268]
  - Signature: `fn display_name(p: &IndexedProject) -> String {`
  - Purpose: Indexed function `display_name` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:259-268]
- `projects` (function) component `projects [function]` (`a87c6b68-c8ad-56f5-8165-55fa8584c3e4`) lines 271-293 [crates/gcode/src/commands/status.rs:271-293]
  - Signature: `pub fn projects(format: Format) -> anyhow::Result<()> {`
  - Purpose: Indexed function `projects` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:271-293]
- `is_stale` (function) component `is_stale [function]` (`bcd80e7e-aab0-57be-88c2-e05d8885d0c2`) lines 296-310 [crates/gcode/src/commands/status.rs:296-310]
  - Signature: `fn is_stale(p: &IndexedProject) -> Option<&'static str> {`
  - Purpose: Indexed function `is_stale` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:296-310]
- `StaleProject` (class) component `StaleProject [class]` (`64197fa3-d771-51b1-8afc-a20cda7fe2c8`) lines 313-316 [crates/gcode/src/commands/status.rs:313-316]
  - Signature: `struct StaleProject<'a> {`
  - Purpose: Indexed class `StaleProject` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:313-316]
- `stale_projects` (function) component `stale_projects [function]` (`375b29cf-84b3-59b6-a648-ecbf26843370`) lines 318-372 [crates/gcode/src/commands/status.rs:318-372]
  - Signature: `fn stale_projects(projects: &[IndexedProject]) -> Vec<StaleProject<'_>> {`
  - Purpose: Indexed function `stale_projects` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:318-372]
- `prune` (function) component `prune [function]` (`deaeb577-543f-579b-8a25-0519c5702ac8`) lines 375-415 [crates/gcode/src/commands/status.rs:375-415]
  - Signature: `pub fn prune(force: bool) -> anyhow::Result<()> {`
  - Purpose: Indexed function `prune` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:375-415]
- `repo_outline` (function) component `repo_outline [function]` (`aa1e91c4-0443-5cc8-b6a4-9a36c70af5ca`) lines 417-457 [crates/gcode/src/commands/status.rs:417-457]
  - Signature: `pub fn repo_outline(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Indexed function `repo_outline` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:417-457]
- `indexed_project` (function) component `indexed_project [function]` (`43ef187e-c632-5d90-832e-124e5cbfa1b7`) lines 463-473 [crates/gcode/src/commands/status.rs:463-473]
  - Signature: `fn indexed_project(id: &str, root_path: &Path) -> IndexedProject {`
  - Purpose: Indexed function `indexed_project` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:463-473]
- `write_project_json` (function) component `write_project_json [function]` (`b882d957-2812-51ff-8ff2-0c643ee8d36a`) lines 475-489 [crates/gcode/src/commands/status.rs:475-489]
  - Signature: `fn write_project_json(root: &Path, id: &str) {`
  - Purpose: Indexed function `write_project_json` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:475-489]
- `duplicate_root_prune_detection_keeps_resolved_project_id` (function) component `duplicate_root_prune_detection_keeps_resolved_project_id [function]` (`91e21d17-7eb1-53bf-82b4-53a51143ec83`) lines 492-510 [crates/gcode/src/commands/status.rs:492-510]
  - Signature: `fn duplicate_root_prune_detection_keeps_resolved_project_id() {`
  - Purpose: Indexed function `duplicate_root_prune_detection_keeps_resolved_project_id` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:492-510]

