---
title: crates/gwiki/src/commands/review_report.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/review_report.rs
  ranges:
  - 28-105
  - 108-113
  - 115-143
  - 116-135
  - 137-142
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
  - 734-745
  - 748-761
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/review_report.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

`crates/gwiki/src/commands/review_report.rs` exposes 36 indexed API symbols.
[crates/gwiki/src/commands/review_report.rs:28-105]
[crates/gwiki/src/commands/review_report.rs:108-113]
[crates/gwiki/src/commands/review_report.rs:115-143]
[crates/gwiki/src/commands/review_report.rs:116-135]
[crates/gwiki/src/commands/review_report.rs:137-142]

## API Symbols

- `execute` (function) component `execute [function]` (`152523ff-0977-56ed-88ae-e5fe3a199e54`) lines 28-105 [crates/gwiki/src/commands/review_report.rs:28-105]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Indexed function `execute` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:28-105]
- `ChangeSetInput` (class) component `ChangeSetInput [class]` (`29ab6167-38e2-5f22-a4bc-20b6632f9ca3`) lines 108-113 [crates/gwiki/src/commands/review_report.rs:108-113]
  - Signature: `struct ChangeSetInput {`
  - Purpose: Indexed class `ChangeSetInput` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:108-113]
- `ChangeSetInput` (class) component `ChangeSetInput [class]` (`9dd76cfa-ba2e-5ea1-9e0d-264ef809e7c8`) lines 115-143 [crates/gwiki/src/commands/review_report.rs:115-143]
  - Signature: `impl ChangeSetInput {`
  - Purpose: Indexed class `ChangeSetInput` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:115-143]
- `ChangeSetInput.from_options` (method) component `ChangeSetInput.from_options [method]` (`b4df68ed-9b31-5cac-9a6b-b6c758951785`) lines 116-135 [crates/gwiki/src/commands/review_report.rs:116-135]
  - Signature: `fn from_options(options: ReviewReportOptions) -> Result<Self, WikiError> {`
  - Purpose: Indexed method `ChangeSetInput.from_options` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:116-135]
- `ChangeSetInput.as_code_change_set` (method) component `ChangeSetInput.as_code_change_set [method]` (`5dd5d876-3423-59cf-ba6e-0aeb84f03846`) lines 137-142 [crates/gwiki/src/commands/review_report.rs:137-142]
  - Signature: `fn as_code_change_set(&self) -> CodeChangeSet {`
  - Purpose: Indexed method `ChangeSetInput.as_code_change_set` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:137-142]
- `ReportParts` (class) component `ReportParts [class]` (`90126ba3-8a58-5668-bed6-6b65e5b6a6e5`) lines 146-154 [crates/gwiki/src/commands/review_report.rs:146-154]
  - Signature: `struct ReportParts {`
  - Purpose: Indexed class `ReportParts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:146-154]
- `ReviewReport` (class) component `ReviewReport [class]` (`ea689200-fe3b-52dc-950a-926184fbdd13`) lines 157-167 [crates/gwiki/src/commands/review_report.rs:157-167]
  - Signature: `struct ReviewReport {`
  - Purpose: Indexed class `ReviewReport` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:157-167]
- `ReviewAffectedPage` (class) component `ReviewAffectedPage [class]` (`4fe05110-53f8-5ae4-9d5a-b563efdec12e`) lines 170-174 [crates/gwiki/src/commands/review_report.rs:170-174]
  - Signature: `struct ReviewAffectedPage {`
  - Purpose: Indexed class `ReviewAffectedPage` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:170-174]
- `RiskyDependencyShift` (class) component `RiskyDependencyShift [class]` (`ed9d3bf5-d253-556d-bf42-8c8189d23e76`) lines 177-183 [crates/gwiki/src/commands/review_report.rs:177-183]
  - Signature: `struct RiskyDependencyShift {`
  - Purpose: Indexed class `RiskyDependencyShift` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:177-183]
- `build_report_from_parts` (function) component `build_report_from_parts [function]` (`6f0e4dee-f9a7-56b3-96d5-c0fe1ca1521f`) lines 185-211 [crates/gwiki/src/commands/review_report.rs:185-211]
  - Signature: `fn build_report_from_parts(parts: ReportParts) -> ReviewReport {`
  - Purpose: Indexed function `build_report_from_parts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:185-211]
- `render_markdown` (function) component `render_markdown [function]` (`f43dec01-c648-537d-869a-de68de19728f`) lines 213-229 [crates/gwiki/src/commands/review_report.rs:213-229]
  - Signature: `fn render_markdown(report: &ReviewReport) -> String {`
  - Purpose: Indexed function `render_markdown` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:213-229]
- `render_changes` (function) component `render_changes [function]` (`d412b22f-d83a-542e-9dd5-ad0a486824d4`) lines 231-241 [crates/gwiki/src/commands/review_report.rs:231-241]
  - Signature: `fn render_changes(markdown: &mut String, changes: &ChangeSetInput) {`
  - Purpose: Indexed function `render_changes` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:231-241]
- `render_affected_pages` (function) component `render_affected_pages [function]` (`253ebd51-a26e-5ec4-923d-c3a4de87e95f`) lines 243-260 [crates/gwiki/src/commands/review_report.rs:243-260]
  - Signature: `fn render_affected_pages(markdown: &mut String, pages: &[ReviewAffectedPage]) {`
  - Purpose: Indexed function `render_affected_pages` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:243-260]
- `render_stale_docs` (function) component `render_stale_docs [function]` (`86578dab-0dcf-548b-b932-e81bc173ee81`) lines 262-266 [crates/gwiki/src/commands/review_report.rs:262-266]
  - Signature: `fn render_stale_docs(markdown: &mut String, stale_docs: &[String]) {`
  - Purpose: Indexed function `render_stale_docs` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:262-266]
- `render_neighborhoods` (function) component `render_neighborhoods [function]` (`4cff988a-a08b-5d9a-8398-61912b677a46`) lines 268-294 [crates/gwiki/src/commands/review_report.rs:268-294]
  - Signature: `fn render_neighborhoods(markdown: &mut String, neighborhoods: &[CodeGraphEdge]) {`
  - Purpose: Indexed function `render_neighborhoods` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:268-294]
- `render_risky_shifts` (function) component `render_risky_shifts [function]` (`94d887e8-f5f6-5f2f-958a-ddf9bb45f041`) lines 296-321 [crates/gwiki/src/commands/review_report.rs:296-321]
  - Signature: `fn render_risky_shifts(markdown: &mut String, report: &ReviewReport) {`
  - Purpose: Indexed function `render_risky_shifts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:296-321]
- `graph_neighborhoods` (function) component `graph_neighborhoods [function]` (`1bb76d09-aa5c-5bcf-a732-531c64cf691a`) lines 323-362 [crates/gwiki/src/commands/review_report.rs:323-362]
  - Signature: `fn graph_neighborhoods(`
  - Purpose: Indexed function `graph_neighborhoods` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:323-362]
- `analytics_graph_from_edges` (function) component `analytics_graph_from_edges [function]` (`9b5cdf2e-1ef8-5420-b7fe-4a6059045383`) lines 364-398 [crates/gwiki/src/commands/review_report.rs:364-398]
  - Signature: `fn analytics_graph_from_edges(changes: &ChangeSetInput, edges: &[CodeGraphEdge]) -> AnalyticsGraph {`
  - Purpose: Indexed function `analytics_graph_from_edges` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:364-398]
- `risky_dependency_shifts` (function) component `risky_dependency_shifts [function]` (`79d07ba1-5f64-5371-b875-4de369718fc0`) lines 400-429 [crates/gwiki/src/commands/review_report.rs:400-429]
  - Signature: `fn risky_dependency_shifts(`
  - Purpose: Indexed function `risky_dependency_shifts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:400-429]
- `risk_from_score` (function) component `risk_from_score [function]` (`5a4af537-59a5-5256-b863-50cbfe2c41ef`) lines 431-455 [crates/gwiki/src/commands/review_report.rs:431-455]
  - Signature: `fn risk_from_score(`
  - Purpose: Indexed function `risk_from_score` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:431-455]
- `changed_node_ids` (function) component `changed_node_ids [function]` (`48f7739e-0460-532f-98b5-fdc206c2955b`) lines 457-470 [crates/gwiki/src/commands/review_report.rs:457-470]
  - Signature: `fn changed_node_ids(changes: &ChangeSetInput, edges: &[CodeGraphEdge]) -> BTreeSet<String> {`
  - Purpose: Indexed function `changed_node_ids` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:457-470]
- `changed_node_ids_from_graph` (function) component `changed_node_ids_from_graph [function]` (`b65d824a-6bab-54c4-a0bf-12cf85ab9577`) lines 472-483 [crates/gwiki/src/commands/review_report.rs:472-483]
  - Signature: `fn changed_node_ids_from_graph(`
  - Purpose: Indexed function `changed_node_ids_from_graph` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:472-483]
- `changed_files_from_diff` (function) component `changed_files_from_diff [function]` (`563c9e10-7dae-55b6-9091-17c62dc72689`) lines 485-492 [crates/gwiki/src/commands/review_report.rs:485-492]
  - Signature: `fn changed_files_from_diff(path: &Path) -> Result<Vec<String>, WikiError> {`
  - Purpose: Indexed function `changed_files_from_diff` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:485-492]
- `parse_unified_diff_files` (function) component `parse_unified_diff_files [function]` (`0cc5aa25-3130-5ed1-999b-4d1a0ffcadaa`) lines 494-529 [crates/gwiki/src/commands/review_report.rs:494-529]
  - Signature: `fn parse_unified_diff_files(contents: &str) -> Vec<String> {`
  - Purpose: Indexed function `parse_unified_diff_files` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:494-529]
- `trim_diff_path` (function) component `trim_diff_path [function]` (`eaa08a75-1975-5102-bb09-a178f2efdf4e`) lines 531-533 [crates/gwiki/src/commands/review_report.rs:531-533]
  - Signature: `fn trim_diff_path(path: &str) -> &str {`
  - Purpose: Indexed function `trim_diff_path` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:531-533]
- `review_affected_page` (function) component `review_affected_page [function]` (`59895caf-8598-56e7-a8bc-7e92a82f2b95`) lines 535-545 [crates/gwiki/src/commands/review_report.rs:535-545]
  - Signature: `fn review_affected_page(page: AffectedPage) -> ReviewAffectedPage {`
  - Purpose: Indexed function `review_affected_page` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:535-545]
- `render_string_list` (function) component `render_string_list [function]` (`f0f2e308-cece-5593-bed5-82845620b973`) lines 547-561 [crates/gwiki/src/commands/review_report.rs:547-561]
  - Signature: `fn render_string_list(markdown: &mut String, label: &str, values: &[String]) {`
  - Purpose: Indexed function `render_string_list` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:547-561]
- `unique_non_empty` (function) component `unique_non_empty [function]` (`e3159784-2788-5a6c-a591-f2057bbfa5cf`) lines 563-571 [crates/gwiki/src/commands/review_report.rs:563-571]
  - Signature: `fn unique_non_empty(values: Vec<String>) -> Vec<String> {`
  - Purpose: Indexed function `unique_non_empty` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:563-571]
- `unique_edges` (function) component `unique_edges [function]` (`bf5e0a4e-7e35-59e9-a013-c1306cf4ab7d`) lines 573-587 [crates/gwiki/src/commands/review_report.rs:573-587]
  - Signature: `fn unique_edges(edges: Vec<CodeGraphEdge>) -> Vec<CodeGraphEdge> {`
  - Purpose: Indexed function `unique_edges` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:573-587]
- `degradation_source` (function) component `degradation_source [function]` (`297ef0fc-25a3-54dd-8422-7c753d9ee968`) lines 589-602 [crates/gwiki/src/commands/review_report.rs:589-602]
  - Signature: `fn degradation_source(degradation: &DegradationKind) -> String {`
  - Purpose: Indexed function `degradation_source` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:589-602]
- `is_graph_blocking_degraded_source` (function) component `is_graph_blocking_degraded_source [function]` (`f4262272-9f45-596a-b70c-ae68b3125fe2`) lines 604-611 [crates/gwiki/src/commands/review_report.rs:604-611]
  - Signature: `fn is_graph_blocking_degraded_source(source: &str) -> bool {`
  - Purpose: Indexed function `is_graph_blocking_degraded_source` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:604-611]
- `optional_falkor_config` (function) component `optional_falkor_config [function]` (`3747302d-1a4b-5f52-b22b-ca5caf22dc22`) lines 613-625 [crates/gwiki/src/commands/review_report.rs:613-625]
  - Signature: `fn optional_falkor_config(conn: &mut postgres::Client) -> Result<Option<FalkorConfig>, WikiError> {`
  - Purpose: Indexed function `optional_falkor_config` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:613-625]
- `review_report_renders_markdown_with_risks_and_metadata` (function) component `review_report_renders_markdown_with_risks_and_metadata [function]` (`1eab52e1-01fb-5acb-bd3a-0e9358bb8ad4`) lines 639-706 [crates/gwiki/src/commands/review_report.rs:639-706]
  - Signature: `fn review_report_renders_markdown_with_risks_and_metadata() {`
  - Purpose: Indexed function `review_report_renders_markdown_with_risks_and_metadata` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:639-706]
- `review_report_degrades_without_graph_analytics` (function) component `review_report_degrades_without_graph_analytics [function]` (`e0de044b-8932-538c-b060-253b7a98d3c4`) lines 709-731 [crates/gwiki/src/commands/review_report.rs:709-731]
  - Signature: `fn review_report_degrades_without_graph_analytics() {`
  - Purpose: Indexed function `review_report_degrades_without_graph_analytics` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:709-731]
- `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path` (function) component `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path [function]` (`4b6e2498-f7e5-5c9d-ac7f-8eaae9774f21`) lines 734-745 [crates/gwiki/src/commands/review_report.rs:734-745]
  - Signature: `fn parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path() {`
  - Purpose: Indexed function `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:734-745]
- `parse_unified_diff_files_sanitizes_unsafe_paths` (function) component `parse_unified_diff_files_sanitizes_unsafe_paths [function]` (`b61c3078-32f7-5e55-949e-d4765d95fe24`) lines 748-761 [crates/gwiki/src/commands/review_report.rs:748-761]
  - Signature: `fn parse_unified_diff_files_sanitizes_unsafe_paths() {`
  - Purpose: Indexed function `parse_unified_diff_files_sanitizes_unsafe_paths` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:748-761]

