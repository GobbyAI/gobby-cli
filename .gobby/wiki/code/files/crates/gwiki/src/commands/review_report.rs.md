---
title: crates/gwiki/src/commands/review_report.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/review_report.rs
  ranges:
  - 28-105
  - 108-113
  - 115-143
  - 146-154
  - 157-167
  - 170-174
  - 177-183
  - 185-211
  - 213-229
  - 231-241
  - 243-260
  - 262-266
  - 268-294
  - 296-321
  - 323-362
  - 364-398
  - 400-429
  - 431-455
  - 457-470
  - 472-483
  - 485-492
  - 494-529
  - 531-533
  - 535-545
  - 547-561
  - 563-571
  - 573-587
  - 589-602
  - 604-611
  - 613-625
  - 639-706
  - 709-731
  - 734-741
  - 744-755
  - 758-771
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/review_report.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Implements the `gwiki review-report` command, which resolves the selected scope, loads PostgreSQL, optional Falkor graph config, wiki graph facts, provenance, and code-change input, then computes affected pages and degradation signals to produce a markdown review report. The file is organized around a top-level `execute` entrypoint plus helper types for change-set input and report parts, rendering helpers for markdown, changes, affected pages, neighborhoods, and risky dependency shifts, and analysis helpers that derive graph neighborhoods, centrality-based risk, changed nodes/files from diffs, and degradation classification. It also includes tests covering markdown rendering, degraded fallback behavior, partial-data degradation mapping, and diff-path parsing/sanitization.
[crates/gwiki/src/commands/review_report.rs:28-105]
[crates/gwiki/src/commands/review_report.rs:108-113]
[crates/gwiki/src/commands/review_report.rs:115-143]
[crates/gwiki/src/commands/review_report.rs:116-135]
[crates/gwiki/src/commands/review_report.rs:137-142]

## API Symbols

- `execute` (function) component `execute [function]` (`35bfa54b-6c90-5664-b0ed-8297f5186faa`) lines 28-105 [crates/gwiki/src/commands/review_report.rs:28-105]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Indexed function `execute` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:28-105]
- `ChangeSetInput` (class) component `ChangeSetInput [class]` (`53e9eaa7-6daf-572d-a0f1-d3f052ea3138`) lines 108-113 [crates/gwiki/src/commands/review_report.rs:108-113]
  - Signature: `struct ChangeSetInput {`
  - Purpose: Indexed class `ChangeSetInput` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:108-113]
- `ChangeSetInput` (class) component `ChangeSetInput [class]` (`0991cff6-7a21-51d0-a12b-22ca5195d5c8`) lines 115-143 [crates/gwiki/src/commands/review_report.rs:115-143]
  - Signature: `impl ChangeSetInput {`
  - Purpose: Indexed class `ChangeSetInput` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:115-143]
- `ChangeSetInput.from_options` (method) component `ChangeSetInput.from_options [method]` (`87ccb057-6082-5975-9132-befabdf8a08a`) lines 116-135 [crates/gwiki/src/commands/review_report.rs:116-135]
  - Signature: `fn from_options(options: ReviewReportOptions) -> Result<Self, WikiError> {`
  - Purpose: Indexed method `ChangeSetInput.from_options` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:116-135]
- `ChangeSetInput.as_code_change_set` (method) component `ChangeSetInput.as_code_change_set [method]` (`78f91c6b-bcf0-5a6c-af97-611181823980`) lines 137-142 [crates/gwiki/src/commands/review_report.rs:137-142]
  - Signature: `fn as_code_change_set(&self) -> CodeChangeSet {`
  - Purpose: Indexed method `ChangeSetInput.as_code_change_set` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:137-142]
- `ReportParts` (class) component `ReportParts [class]` (`8d8e8c76-8606-5655-b883-26b31356f7da`) lines 146-154 [crates/gwiki/src/commands/review_report.rs:146-154]
  - Signature: `struct ReportParts {`
  - Purpose: Indexed class `ReportParts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:146-154]
- `ReviewReport` (class) component `ReviewReport [class]` (`29ed9aee-730d-5af5-8b12-83f2ebe301e4`) lines 157-167 [crates/gwiki/src/commands/review_report.rs:157-167]
  - Signature: `struct ReviewReport {`
  - Purpose: Indexed class `ReviewReport` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:157-167]
- `ReviewAffectedPage` (class) component `ReviewAffectedPage [class]` (`110949ba-94c9-5fae-8b50-99ad53221710`) lines 170-174 [crates/gwiki/src/commands/review_report.rs:170-174]
  - Signature: `struct ReviewAffectedPage {`
  - Purpose: Indexed class `ReviewAffectedPage` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:170-174]
- `RiskyDependencyShift` (class) component `RiskyDependencyShift [class]` (`f5bfa044-7a23-561c-97e0-f65f7beecfba`) lines 177-183 [crates/gwiki/src/commands/review_report.rs:177-183]
  - Signature: `struct RiskyDependencyShift {`
  - Purpose: Indexed class `RiskyDependencyShift` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:177-183]
- `build_report_from_parts` (function) component `build_report_from_parts [function]` (`39f0c0ea-2766-5b48-a5c9-ca2cf7f26332`) lines 185-211 [crates/gwiki/src/commands/review_report.rs:185-211]
  - Signature: `fn build_report_from_parts(parts: ReportParts) -> ReviewReport {`
  - Purpose: Indexed function `build_report_from_parts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:185-211]
- `render_markdown` (function) component `render_markdown [function]` (`2e8e7a53-5c56-5574-b617-9b3debe174f9`) lines 213-229 [crates/gwiki/src/commands/review_report.rs:213-229]
  - Signature: `fn render_markdown(report: &ReviewReport) -> String {`
  - Purpose: Indexed function `render_markdown` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:213-229]
- `render_changes` (function) component `render_changes [function]` (`73da148a-57c7-5d68-bd42-66c01c7304cb`) lines 231-241 [crates/gwiki/src/commands/review_report.rs:231-241]
  - Signature: `fn render_changes(markdown: &mut String, changes: &ChangeSetInput) {`
  - Purpose: Indexed function `render_changes` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:231-241]
- `render_affected_pages` (function) component `render_affected_pages [function]` (`8f3c0a89-c1a9-5e6a-afbb-52b03eab60b0`) lines 243-260 [crates/gwiki/src/commands/review_report.rs:243-260]
  - Signature: `fn render_affected_pages(markdown: &mut String, pages: &[ReviewAffectedPage]) {`
  - Purpose: Indexed function `render_affected_pages` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:243-260]
- `render_stale_docs` (function) component `render_stale_docs [function]` (`586fd394-1c1f-512e-a489-5b9b58f4f832`) lines 262-266 [crates/gwiki/src/commands/review_report.rs:262-266]
  - Signature: `fn render_stale_docs(markdown: &mut String, stale_docs: &[String]) {`
  - Purpose: Indexed function `render_stale_docs` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:262-266]
- `render_neighborhoods` (function) component `render_neighborhoods [function]` (`ed8b9961-1e88-55b9-ae95-cbb711b90d91`) lines 268-294 [crates/gwiki/src/commands/review_report.rs:268-294]
  - Signature: `fn render_neighborhoods(markdown: &mut String, neighborhoods: &[CodeGraphEdge]) {`
  - Purpose: Indexed function `render_neighborhoods` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:268-294]
- `render_risky_shifts` (function) component `render_risky_shifts [function]` (`286c3e93-3fff-594a-909f-e46840a6c55b`) lines 296-321 [crates/gwiki/src/commands/review_report.rs:296-321]
  - Signature: `fn render_risky_shifts(markdown: &mut String, report: &ReviewReport) {`
  - Purpose: Indexed function `render_risky_shifts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:296-321]
- `graph_neighborhoods` (function) component `graph_neighborhoods [function]` (`f2894f8c-9cdb-5bde-9a12-b872eb35290a`) lines 323-362 [crates/gwiki/src/commands/review_report.rs:323-362]
  - Signature: `fn graph_neighborhoods(`
  - Purpose: Indexed function `graph_neighborhoods` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:323-362]
- `analytics_graph_from_edges` (function) component `analytics_graph_from_edges [function]` (`05dcb72b-1931-5544-9025-91a3b0f3f7f0`) lines 364-398 [crates/gwiki/src/commands/review_report.rs:364-398]
  - Signature: `fn analytics_graph_from_edges(changes: &ChangeSetInput, edges: &[CodeGraphEdge]) -> AnalyticsGraph {`
  - Purpose: Indexed function `analytics_graph_from_edges` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:364-398]
- `risky_dependency_shifts` (function) component `risky_dependency_shifts [function]` (`509145ca-e06d-5dba-8a4a-66ab46a8f075`) lines 400-429 [crates/gwiki/src/commands/review_report.rs:400-429]
  - Signature: `fn risky_dependency_shifts(`
  - Purpose: Indexed function `risky_dependency_shifts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:400-429]
- `risk_from_score` (function) component `risk_from_score [function]` (`40164e03-5c4a-5bf5-9d5b-09b59435a879`) lines 431-455 [crates/gwiki/src/commands/review_report.rs:431-455]
  - Signature: `fn risk_from_score(`
  - Purpose: Indexed function `risk_from_score` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:431-455]
- `changed_node_ids` (function) component `changed_node_ids [function]` (`c724a678-1b84-56ad-8ff5-3dd6726d72bc`) lines 457-470 [crates/gwiki/src/commands/review_report.rs:457-470]
  - Signature: `fn changed_node_ids(changes: &ChangeSetInput, edges: &[CodeGraphEdge]) -> BTreeSet<String> {`
  - Purpose: Indexed function `changed_node_ids` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:457-470]
- `changed_node_ids_from_graph` (function) component `changed_node_ids_from_graph [function]` (`034afab3-419d-555a-b2eb-317540e07ac6`) lines 472-483 [crates/gwiki/src/commands/review_report.rs:472-483]
  - Signature: `fn changed_node_ids_from_graph(`
  - Purpose: Indexed function `changed_node_ids_from_graph` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:472-483]
- `changed_files_from_diff` (function) component `changed_files_from_diff [function]` (`f448f685-9f97-5f1b-9b2b-0632ff4e58a5`) lines 485-492 [crates/gwiki/src/commands/review_report.rs:485-492]
  - Signature: `fn changed_files_from_diff(path: &Path) -> Result<Vec<String>, WikiError> {`
  - Purpose: Indexed function `changed_files_from_diff` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:485-492]
- `parse_unified_diff_files` (function) component `parse_unified_diff_files [function]` (`93d11802-fe91-57a1-a758-ac6a9f70bdd7`) lines 494-529 [crates/gwiki/src/commands/review_report.rs:494-529]
  - Signature: `fn parse_unified_diff_files(contents: &str) -> Vec<String> {`
  - Purpose: Indexed function `parse_unified_diff_files` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:494-529]
- `trim_diff_path` (function) component `trim_diff_path [function]` (`216e2f5d-aab4-5735-abf7-29f85f8c9996`) lines 531-533 [crates/gwiki/src/commands/review_report.rs:531-533]
  - Signature: `fn trim_diff_path(path: &str) -> &str {`
  - Purpose: Indexed function `trim_diff_path` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:531-533]
- `review_affected_page` (function) component `review_affected_page [function]` (`7e977d42-9569-5c94-ba91-569df1f95327`) lines 535-545 [crates/gwiki/src/commands/review_report.rs:535-545]
  - Signature: `fn review_affected_page(page: AffectedPage) -> ReviewAffectedPage {`
  - Purpose: Indexed function `review_affected_page` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:535-545]
- `render_string_list` (function) component `render_string_list [function]` (`d4a5ff06-bbd0-5f42-8130-93cdd9734d18`) lines 547-561 [crates/gwiki/src/commands/review_report.rs:547-561]
  - Signature: `fn render_string_list(markdown: &mut String, label: &str, values: &[String]) {`
  - Purpose: Indexed function `render_string_list` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:547-561]
- `unique_non_empty` (function) component `unique_non_empty [function]` (`d038cec6-9382-5f18-af14-c5a2a3a38c84`) lines 563-571 [crates/gwiki/src/commands/review_report.rs:563-571]
  - Signature: `fn unique_non_empty(values: Vec<String>) -> Vec<String> {`
  - Purpose: Indexed function `unique_non_empty` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:563-571]
- `unique_edges` (function) component `unique_edges [function]` (`37dd1b21-f299-5114-a149-ae4ee664a83d`) lines 573-587 [crates/gwiki/src/commands/review_report.rs:573-587]
  - Signature: `fn unique_edges(edges: Vec<CodeGraphEdge>) -> Vec<CodeGraphEdge> {`
  - Purpose: Indexed function `unique_edges` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:573-587]
- `degradation_source` (function) component `degradation_source [function]` (`3d8a0c7c-1cd3-5060-986c-322da3d2e9e7`) lines 589-602 [crates/gwiki/src/commands/review_report.rs:589-602]
  - Signature: `fn degradation_source(degradation: &DegradationKind) -> String {`
  - Purpose: Indexed function `degradation_source` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:589-602]
- `is_graph_blocking_degraded_source` (function) component `is_graph_blocking_degraded_source [function]` (`66799a3c-2fc3-537c-a72c-a6492124422f`) lines 604-611 [crates/gwiki/src/commands/review_report.rs:604-611]
  - Signature: `fn is_graph_blocking_degraded_source(source: &str) -> bool {`
  - Purpose: Indexed function `is_graph_blocking_degraded_source` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:604-611]
- `optional_falkor_config` (function) component `optional_falkor_config [function]` (`a567ea0e-a6b5-5da0-a900-8b4ef2ac155e`) lines 613-625 [crates/gwiki/src/commands/review_report.rs:613-625]
  - Signature: `fn optional_falkor_config(conn: &mut postgres::Client) -> Result<Option<FalkorConfig>, WikiError> {`
  - Purpose: Indexed function `optional_falkor_config` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:613-625]
- `review_report_renders_markdown_with_risks_and_metadata` (function) component `review_report_renders_markdown_with_risks_and_metadata [function]` (`71270fd0-73c4-503c-a7d6-032791e0f013`) lines 639-706 [crates/gwiki/src/commands/review_report.rs:639-706]
  - Signature: `fn review_report_renders_markdown_with_risks_and_metadata() {`
  - Purpose: Indexed function `review_report_renders_markdown_with_risks_and_metadata` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:639-706]
- `review_report_degrades_without_graph_analytics` (function) component `review_report_degrades_without_graph_analytics [function]` (`304675c9-bb9c-5273-b867-1664de917c61`) lines 709-731 [crates/gwiki/src/commands/review_report.rs:709-731]
  - Signature: `fn review_report_degrades_without_graph_analytics() {`
  - Purpose: Indexed function `review_report_degrades_without_graph_analytics` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:709-731]
- `review_report_maps_semantic_partial_data_degradation` (function) component `review_report_maps_semantic_partial_data_degradation [function]` (`602d0fdb-593d-563d-9c52-909af1eb71fe`) lines 734-741 [crates/gwiki/src/commands/review_report.rs:734-741]
  - Signature: `fn review_report_maps_semantic_partial_data_degradation() {`
  - Purpose: Indexed function `review_report_maps_semantic_partial_data_degradation` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:734-741]
- `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path` (function) component `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path [function]` (`a09d5fdb-1098-5daa-890b-c2b1fd5ddb99`) lines 744-755 [crates/gwiki/src/commands/review_report.rs:744-755]
  - Signature: `fn parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path() {`
  - Purpose: Indexed function `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:744-755]
- `parse_unified_diff_files_sanitizes_unsafe_paths` (function) component `parse_unified_diff_files_sanitizes_unsafe_paths [function]` (`84a9355a-c288-5445-ba20-0f3a019f30f2`) lines 758-771 [crates/gwiki/src/commands/review_report.rs:758-771]
  - Signature: `fn parse_unified_diff_files_sanitizes_unsafe_paths() {`
  - Purpose: Indexed function `parse_unified_diff_files_sanitizes_unsafe_paths` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:758-771]

