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
  - 319-322
  - 325-334
  - 337-341
  - 343-347
  - 349-358
  - 361-367
  - 369-423
  - 426-437
  - 439-452
  - 454-494
  - 496-520
  - 522-526
  - 528-547
  - 549-567
  - 569-597
  - 599-605
  - 607-614
  - 616-629
  - 631-635
  - 637-677
  - 683-693
  - 695-709
  - 712-717
  - 720-725
  - 728-746
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/status.rs:18-42](crates/gcode/src/commands/status.rs#L18-L42), [crates/gcode/src/commands/status.rs:45-58](crates/gcode/src/commands/status.rs#L45-L58), [crates/gcode/src/commands/status.rs:60-134](crates/gcode/src/commands/status.rs#L60-L134), [crates/gcode/src/commands/status.rs:136-158](crates/gcode/src/commands/status.rs#L136-L158), [crates/gcode/src/commands/status.rs:160-185](crates/gcode/src/commands/status.rs#L160-L185), [crates/gcode/src/commands/status.rs:187-197](crates/gcode/src/commands/status.rs#L187-L197), [crates/gcode/src/commands/status.rs:200-227](crates/gcode/src/commands/status.rs#L200-L227), [crates/gcode/src/commands/status.rs:229-245](crates/gcode/src/commands/status.rs#L229-L245), [crates/gcode/src/commands/status.rs:248-256](crates/gcode/src/commands/status.rs#L248-L256), [crates/gcode/src/commands/status.rs:259-268](crates/gcode/src/commands/status.rs#L259-L268), [crates/gcode/src/commands/status.rs:271-293](crates/gcode/src/commands/status.rs#L271-L293), [crates/gcode/src/commands/status.rs:296-310](crates/gcode/src/commands/status.rs#L296-L310), [crates/gcode/src/commands/status.rs:313-316](crates/gcode/src/commands/status.rs#L313-L316), [crates/gcode/src/commands/status.rs:319-322](crates/gcode/src/commands/status.rs#L319-L322), [crates/gcode/src/commands/status.rs:325-334](crates/gcode/src/commands/status.rs#L325-L334), [crates/gcode/src/commands/status.rs:337-341](crates/gcode/src/commands/status.rs#L337-L341), [crates/gcode/src/commands/status.rs:343-347](crates/gcode/src/commands/status.rs#L343-L347), [crates/gcode/src/commands/status.rs:349-358](crates/gcode/src/commands/status.rs#L349-L358), [crates/gcode/src/commands/status.rs:361-367](crates/gcode/src/commands/status.rs#L361-L367), [crates/gcode/src/commands/status.rs:369-423](crates/gcode/src/commands/status.rs#L369-L423), [crates/gcode/src/commands/status.rs:426-437](crates/gcode/src/commands/status.rs#L426-L437), [crates/gcode/src/commands/status.rs:439-452](crates/gcode/src/commands/status.rs#L439-L452), [crates/gcode/src/commands/status.rs:454-494](crates/gcode/src/commands/status.rs#L454-L494), [crates/gcode/src/commands/status.rs:496-520](crates/gcode/src/commands/status.rs#L496-L520), [crates/gcode/src/commands/status.rs:522-526](crates/gcode/src/commands/status.rs#L522-L526), [crates/gcode/src/commands/status.rs:528-547](crates/gcode/src/commands/status.rs#L528-L547), [crates/gcode/src/commands/status.rs:549-567](crates/gcode/src/commands/status.rs#L549-L567), [crates/gcode/src/commands/status.rs:569-597](crates/gcode/src/commands/status.rs#L569-L597), [crates/gcode/src/commands/status.rs:599-605](crates/gcode/src/commands/status.rs#L599-L605), [crates/gcode/src/commands/status.rs:607-614](crates/gcode/src/commands/status.rs#L607-L614), [crates/gcode/src/commands/status.rs:616-629](crates/gcode/src/commands/status.rs#L616-L629), [crates/gcode/src/commands/status.rs:631-635](crates/gcode/src/commands/status.rs#L631-L635), [crates/gcode/src/commands/status.rs:637-677](crates/gcode/src/commands/status.rs#L637-L677), [crates/gcode/src/commands/status.rs:683-693](crates/gcode/src/commands/status.rs#L683-L693), [crates/gcode/src/commands/status.rs:695-709](crates/gcode/src/commands/status.rs#L695-L709), [crates/gcode/src/commands/status.rs:712-717](crates/gcode/src/commands/status.rs#L712-L717), [crates/gcode/src/commands/status.rs:720-725](crates/gcode/src/commands/status.rs#L720-L725), [crates/gcode/src/commands/status.rs:728-746](crates/gcode/src/commands/status.rs#L728-L746)

</details>

# crates/gcode/src/commands/status.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

This file implements the gcode status and cleanup workflow for indexed projects. It formats timestamps for display, converts epoch days to calendar dates, and then uses the database, graph, vector, and visibility layers to load the current indexed project state, detect stale or missing project context, and report coverage and repository outline information. The prune helpers and `ProjectionPruneTotals` aggregate cleanup work across graph/vector projections, support different projection scopes, and write or print per-project JSON and totals while handling orphaned or duplicate-root cases and warning on cleanup failures.
[crates/gcode/src/commands/status.rs:18-42]
[crates/gcode/src/commands/status.rs:45-58]
[crates/gcode/src/commands/status.rs:60-134]
[crates/gcode/src/commands/status.rs:136-158]
[crates/gcode/src/commands/status.rs:160-185]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `format_timestamp` | function | `fn format_timestamp(raw: &str) -> String {` | `format_timestamp [function]` | `7027693a-1411-5ccd-90be-cc3810418e85` | 18-42 [crates/gcode/src/commands/status.rs:18-42] | Indexed function `format_timestamp` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:18-42] |
| `days_to_ymd` | function | `fn days_to_ymd(mut days: i64) -> (i64, i64, i64) {` | `days_to_ymd [function]` | `a2c86830-61ee-56e0-a451-271f26a16c3a` | 45-58 [crates/gcode/src/commands/status.rs:45-58] | Indexed function `days_to_ymd` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:45-58] |
| `run` | function | `pub fn run(ctx: &Context, format: Format) -> anyhow::Result<()> {` | `run [function]` | `bfc1cae3-4c00-5c73-9dc5-dce66f0eec85` | 60-134 [crates/gcode/src/commands/status.rs:60-134] | Indexed function `run` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:60-134] |
| `overlay_status_json` | function | `fn overlay_status_json(ctx: &Context, conn: &mut postgres::Client) -> Option<serde_json::Value> {` | `overlay_status_json [function]` | `a7f6bfd3-9618-5f95-8de9-75d4a7e252a7` | 136-158 [crates/gcode/src/commands/status.rs:136-158] | Indexed function `overlay_status_json` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:136-158] |
| `invalidate` | function | `pub fn invalidate(ctx: &Context, force: bool) -> anyhow::Result<()> {` | `invalidate [function]` | `0f76d4c3-4416-5c6a-a6fe-6412539a54ce` | 160-185 [crates/gcode/src/commands/status.rs:160-185] | Indexed function `invalidate` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:160-185] |
| `cleanup_project_projections` | function | `fn cleanup_project_projections(ctx: &Context) -> anyhow::Result<()> {` | `cleanup_project_projections [function]` | `f3af98c0-13ed-574c-9fa7-860777fee0f2` | 187-197 [crates/gcode/src/commands/status.rs:187-197] | Indexed function `cleanup_project_projections` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:187-197] |
| `collect_projects` | function | `fn collect_projects() -> anyhow::Result<Vec<IndexedProject>> {` | `collect_projects [function]` | `b8a64763-17fe-5978-849c-212a7193587d` | 200-227 [crates/gcode/src/commands/status.rs:200-227] | Indexed function `collect_projects` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:200-227] |
| `indexed_project_from_row` | function | `fn indexed_project_from_row(row: &postgres::Row) -> anyhow::Result<IndexedProject> {` | `indexed_project_from_row [function]` | `7da7842b-9070-53f3-af3d-0d4474453982` | 229-245 [crates/gcode/src/commands/status.rs:229-245] | Indexed function `indexed_project_from_row` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:229-245] |
| `format_coverage` | function | `fn format_coverage(indexed: usize, eligible: Option<usize>) -> String {` | `format_coverage [function]` | `d985b558-527d-54b5-b16c-83529d40b856` | 248-256 [crates/gcode/src/commands/status.rs:248-256] | Indexed function `format_coverage` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:248-256] |
| `display_name` | function | `fn display_name(p: &IndexedProject) -> String {` | `display_name [function]` | `fab3b435-7199-5e13-bf61-58fdb3c43510` | 259-268 [crates/gcode/src/commands/status.rs:259-268] | Indexed function `display_name` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:259-268] |
| `projects` | function | `pub fn projects(format: Format) -> anyhow::Result<()> {` | `projects [function]` | `a87c6b68-c8ad-56f5-8165-55fa8584c3e4` | 271-293 [crates/gcode/src/commands/status.rs:271-293] | Indexed function `projects` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:271-293] |
| `is_stale` | function | `fn is_stale(p: &IndexedProject) -> Option<&'static str> {` | `is_stale [function]` | `bcd80e7e-aab0-57be-88c2-e05d8885d0c2` | 296-310 [crates/gcode/src/commands/status.rs:296-310] | Indexed function `is_stale` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:296-310] |
| `StaleProject` | class | `struct StaleProject<'a> {` | `StaleProject [class]` | `64197fa3-d771-51b1-8afc-a20cda7fe2c8` | 313-316 [crates/gcode/src/commands/status.rs:313-316] | Indexed class `StaleProject` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:313-316] |
| `ProjectionCleanupScope` | type | `enum ProjectionCleanupScope {` | `ProjectionCleanupScope [type]` | `2850aa65-d097-5a0e-8abd-75e7d83faf24` | 319-322 [crates/gcode/src/commands/status.rs:319-322] | Indexed type `ProjectionCleanupScope` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:319-322] |
| `ProjectionPruneTotals` | class | `struct ProjectionPruneTotals {` | `ProjectionPruneTotals [class]` | `74fd99d5-e2e6-5ea6-98ba-6ce6bc9bac27` | 325-334 [crates/gcode/src/commands/status.rs:325-334] | Indexed class `ProjectionPruneTotals` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:325-334] |
| `ProjectionPruneTotals::record_graph_cleanup` | method | `fn record_graph_cleanup(&mut self, cleanup: crate::graph::code_graph::GraphOrphanCleanup) {` | `ProjectionPruneTotals::record_graph_cleanup [method]` | `7c05fe11-16ec-55cd-8184-81f9a8083d45` | 337-341 [crates/gcode/src/commands/status.rs:337-341] | Indexed method `ProjectionPruneTotals::record_graph_cleanup` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:337-341] |
| `ProjectionPruneTotals::record_vector_cleanup` | method | `fn record_vector_cleanup(&mut self, cleanup: code_symbols::VectorOrphanCleanup) {` | `ProjectionPruneTotals::record_vector_cleanup [method]` | `155548c1-76a7-577c-bf74-99bac55d9ba6` | 343-347 [crates/gcode/src/commands/status.rs:343-347] | Indexed method `ProjectionPruneTotals::record_vector_cleanup` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:343-347] |
| `ProjectionPruneTotals::add` | method | `fn add(&mut self, other: ProjectionPruneTotals) {` | `ProjectionPruneTotals::add [method]` | `a8ec4bc5-93a3-5a17-ad6a-e3a4f012771b` | 349-358 [crates/gcode/src/commands/status.rs:349-358] | Indexed method `ProjectionPruneTotals::add` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:349-358] |
| `projection_cleanup_scope` | function | `fn projection_cleanup_scope(project_override: Option<&str>) -> ProjectionCleanupScope {` | `projection_cleanup_scope [function]` | `4748f546-c81e-5481-acf4-b5a269f1ad9a` | 361-367 [crates/gcode/src/commands/status.rs:361-367] | Indexed function `projection_cleanup_scope` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:361-367] |
| `stale_projects` | function | `fn stale_projects(projects: &[IndexedProject]) -> Vec<StaleProject<'_>> {` | `stale_projects [function]` | `7d2bce73-6cb2-5021-8c3a-8599c668e7ee` | 369-423 [crates/gcode/src/commands/status.rs:369-423] | Indexed function `stale_projects` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:369-423] |
| `prune` | function | `pub fn prune(force: bool, project_override: Option<&str>, quiet: bool) -> anyhow::Result<()> {` | `prune [function]` | `d2dc4b48-98b5-53e5-94dc-84a6188556c2` | 426-437 [crates/gcode/src/commands/status.rs:426-437] | Indexed function `prune` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:426-437] |
| `prune_resolved_project_projections` | function | `fn prune_resolved_project_projections(` | `prune_resolved_project_projections [function]` | `428f208d-015d-5507-9cc5-cff224a25054` | 439-452 [crates/gcode/src/commands/status.rs:439-452] | Indexed function `prune_resolved_project_projections` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:439-452] |
| `prune_stale_projects` | function | `fn prune_stale_projects(force: bool) -> anyhow::Result<Option<usize>> {` | `prune_stale_projects [function]` | `47d5b4c1-eeed-5318-8e1d-734b125b7dea` | 454-494 [crates/gcode/src/commands/status.rs:454-494] | Indexed function `prune_stale_projects` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:454-494] |
| `prune_all_project_projections` | function | `fn prune_all_project_projections(quiet: bool) -> anyhow::Result<()> {` | `prune_all_project_projections [function]` | `fb6cfdcc-b84c-5025-9cfc-04c3c304280d` | 496-520 [crates/gcode/src/commands/status.rs:496-520] | Indexed function `prune_all_project_projections` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:496-520] |
| `prune_current_project_projections` | function | `fn prune_current_project_projections(ctx: &Context) -> anyhow::Result<()> {` | `prune_current_project_projections [function]` | `a3bab600-9978-5c4c-9a81-1272447b8081` | 522-526 [crates/gcode/src/commands/status.rs:522-526] | Indexed function `prune_current_project_projections` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:522-526] |
| `prune_project_orphan_projections` | function | `fn prune_project_orphan_projections(` | `prune_project_orphan_projections [function]` | `4f4ce9c0-302a-5726-ac30-e800d5be96a0` | 528-547 [crates/gcode/src/commands/status.rs:528-547] | Indexed function `prune_project_orphan_projections` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:528-547] |
| `print_current_project_projection_totals` | function | `fn print_current_project_projection_totals(totals: ProjectionPruneTotals) {` | `print_current_project_projection_totals [function]` | `ed59d9fd-2d62-5cad-8ab3-b560111d8146` | 549-567 [crates/gcode/src/commands/status.rs:549-567] | Indexed function `print_current_project_projection_totals` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:549-567] |
| `print_all_project_projection_totals` | function | `fn print_all_project_projection_totals(totals: ProjectionPruneTotals) {` | `print_all_project_projection_totals [function]` | `710966ea-3a4c-5899-b850-f07c4a63ed45` | 569-597 [crates/gcode/src/commands/status.rs:569-597] | Indexed function `print_all_project_projection_totals` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:569-597] |
| `warn_projection_cleanup_failure` | function | `fn warn_projection_cleanup_failure(store: &str, project_label: Option<&str>, error: anyhow::Error) {` | `warn_projection_cleanup_failure [function]` | `95a93486-649b-5868-8192-23e0e3c670e1` | 599-605 [crates/gcode/src/commands/status.rs:599-605] | Indexed function `warn_projection_cleanup_failure` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:599-605] |
| `prune_graph_orphans` | function | `fn prune_graph_orphans(` | `prune_graph_orphans [function]` | `4234eb74-4092-5f71-8a3a-cca5d5b2a41b` | 607-614 [crates/gcode/src/commands/status.rs:607-614] | Indexed function `prune_graph_orphans` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:607-614] |
| `prune_vector_orphans` | function | `fn prune_vector_orphans(` | `prune_vector_orphans [function]` | `7a0ce9a9-424c-5d17-a8f3-dba0f12ff4ef` | 616-629 [crates/gcode/src/commands/status.rs:616-629] | Indexed function `prune_vector_orphans` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:616-629] |
| `is_missing_project_context` | function | `fn is_missing_project_context(error: &anyhow::Error) -> bool {` | `is_missing_project_context [function]` | `dd8f5d17-d743-5696-8d3d-24616b21de8c` | 631-635 [crates/gcode/src/commands/status.rs:631-635] | Indexed function `is_missing_project_context` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:631-635] |
| `repo_outline` | function | `pub fn repo_outline(ctx: &Context, format: Format) -> anyhow::Result<()> {` | `repo_outline [function]` | `060e38f5-7a4e-50c7-ba38-eb8a0872cc08` | 637-677 [crates/gcode/src/commands/status.rs:637-677] | Indexed function `repo_outline` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:637-677] |
| `indexed_project` | function | `fn indexed_project(id: &str, root_path: &Path) -> IndexedProject {` | `indexed_project [function]` | `a8978517-66b7-56e6-8196-739455511587` | 683-693 [crates/gcode/src/commands/status.rs:683-693] | Indexed function `indexed_project` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:683-693] |
| `write_project_json` | function | `fn write_project_json(root: &Path, id: &str) {` | `write_project_json [function]` | `6a912344-7292-5eeb-a31b-25a2e1ed52da` | 695-709 [crates/gcode/src/commands/status.rs:695-709] | Indexed function `write_project_json` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:695-709] |
| `prune_without_project_uses_all_indexed_projection_scope` | function | `fn prune_without_project_uses_all_indexed_projection_scope() {` | `prune_without_project_uses_all_indexed_projection_scope [function]` | `7bfb8bd3-565a-5265-8ff3-6f60ce75c2ad` | 712-717 [crates/gcode/src/commands/status.rs:712-717] | Indexed function `prune_without_project_uses_all_indexed_projection_scope` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:712-717] |
| `prune_with_project_uses_single_resolved_projection_scope` | function | `fn prune_with_project_uses_single_resolved_projection_scope() {` | `prune_with_project_uses_single_resolved_projection_scope [function]` | `e7060ed5-9d92-5434-9942-642b67111810` | 720-725 [crates/gcode/src/commands/status.rs:720-725] | Indexed function `prune_with_project_uses_single_resolved_projection_scope` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:720-725] |
| `duplicate_root_prune_detection_keeps_resolved_project_id` | function | `fn duplicate_root_prune_detection_keeps_resolved_project_id() {` | `duplicate_root_prune_detection_keeps_resolved_project_id [function]` | `5131eb49-4684-5c4c-9969-90964a64f002` | 728-746 [crates/gcode/src/commands/status.rs:728-746] | Indexed function `duplicate_root_prune_detection_keeps_resolved_project_id` in `crates/gcode/src/commands/status.rs`. [crates/gcode/src/commands/status.rs:728-746] |
