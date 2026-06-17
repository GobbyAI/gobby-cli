---
title: crates/gwiki/src/commands/review_report.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/review_report.rs
  ranges:
  - 28-105
  - 108-113
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
  - 364-399
  - 401-430
  - 432-456
  - 458-471
  - 473-484
  - 486-493
  - 495-530
  - 532-534
  - 536-546
  - 548-562
  - 564-572
  - 574-588
  - 590-603
  - 605-612
  - 614-626
  - 642-711
  - 714-736
  - 739-746
  - 749-760
  - 763-776
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/review_report.rs:28-105](crates/gwiki/src/commands/review_report.rs#L28-L105), [crates/gwiki/src/commands/review_report.rs:108-113](crates/gwiki/src/commands/review_report.rs#L108-L113), [crates/gwiki/src/commands/review_report.rs:116-135](crates/gwiki/src/commands/review_report.rs#L116-L135), [crates/gwiki/src/commands/review_report.rs:137-142](crates/gwiki/src/commands/review_report.rs#L137-L142), [crates/gwiki/src/commands/review_report.rs:146-154](crates/gwiki/src/commands/review_report.rs#L146-L154), [crates/gwiki/src/commands/review_report.rs:157-167](crates/gwiki/src/commands/review_report.rs#L157-L167), [crates/gwiki/src/commands/review_report.rs:170-174](crates/gwiki/src/commands/review_report.rs#L170-L174), [crates/gwiki/src/commands/review_report.rs:177-183](crates/gwiki/src/commands/review_report.rs#L177-L183), [crates/gwiki/src/commands/review_report.rs:185-211](crates/gwiki/src/commands/review_report.rs#L185-L211), [crates/gwiki/src/commands/review_report.rs:213-229](crates/gwiki/src/commands/review_report.rs#L213-L229), [crates/gwiki/src/commands/review_report.rs:231-241](crates/gwiki/src/commands/review_report.rs#L231-L241), [crates/gwiki/src/commands/review_report.rs:243-260](crates/gwiki/src/commands/review_report.rs#L243-L260), [crates/gwiki/src/commands/review_report.rs:262-266](crates/gwiki/src/commands/review_report.rs#L262-L266), [crates/gwiki/src/commands/review_report.rs:268-294](crates/gwiki/src/commands/review_report.rs#L268-L294), [crates/gwiki/src/commands/review_report.rs:296-321](crates/gwiki/src/commands/review_report.rs#L296-L321), [crates/gwiki/src/commands/review_report.rs:323-362](crates/gwiki/src/commands/review_report.rs#L323-L362), [crates/gwiki/src/commands/review_report.rs:364-399](crates/gwiki/src/commands/review_report.rs#L364-L399), [crates/gwiki/src/commands/review_report.rs:401-430](crates/gwiki/src/commands/review_report.rs#L401-L430), [crates/gwiki/src/commands/review_report.rs:432-456](crates/gwiki/src/commands/review_report.rs#L432-L456), [crates/gwiki/src/commands/review_report.rs:458-471](crates/gwiki/src/commands/review_report.rs#L458-L471), [crates/gwiki/src/commands/review_report.rs:473-484](crates/gwiki/src/commands/review_report.rs#L473-L484), [crates/gwiki/src/commands/review_report.rs:486-493](crates/gwiki/src/commands/review_report.rs#L486-L493), [crates/gwiki/src/commands/review_report.rs:495-530](crates/gwiki/src/commands/review_report.rs#L495-L530), [crates/gwiki/src/commands/review_report.rs:532-534](crates/gwiki/src/commands/review_report.rs#L532-L534), [crates/gwiki/src/commands/review_report.rs:536-546](crates/gwiki/src/commands/review_report.rs#L536-L546), [crates/gwiki/src/commands/review_report.rs:548-562](crates/gwiki/src/commands/review_report.rs#L548-L562), [crates/gwiki/src/commands/review_report.rs:564-572](crates/gwiki/src/commands/review_report.rs#L564-L572), [crates/gwiki/src/commands/review_report.rs:574-588](crates/gwiki/src/commands/review_report.rs#L574-L588), [crates/gwiki/src/commands/review_report.rs:590-603](crates/gwiki/src/commands/review_report.rs#L590-L603), [crates/gwiki/src/commands/review_report.rs:605-612](crates/gwiki/src/commands/review_report.rs#L605-L612), [crates/gwiki/src/commands/review_report.rs:614-626](crates/gwiki/src/commands/review_report.rs#L614-L626), [crates/gwiki/src/commands/review_report.rs:642-711](crates/gwiki/src/commands/review_report.rs#L642-L711), [crates/gwiki/src/commands/review_report.rs:714-736](crates/gwiki/src/commands/review_report.rs#L714-L736), [crates/gwiki/src/commands/review_report.rs:739-746](crates/gwiki/src/commands/review_report.rs#L739-L746), [crates/gwiki/src/commands/review_report.rs:749-760](crates/gwiki/src/commands/review_report.rs#L749-L760), [crates/gwiki/src/commands/review_report.rs:763-776](crates/gwiki/src/commands/review_report.rs#L763-L776)

</details>

# crates/gwiki/src/commands/review_report.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds a review-report command that resolves the requested scope, loads repository and graph metadata from PostgreSQL/Falkor/provenance sources, computes affected pages and risky dependency shifts from a change set, and returns a markdown report.

The helper types and functions split that work into three parts: parsing change-set input and diff paths, deriving analytics like neighborhoods/risk/degradation from graph data, and rendering the final report sections with metadata, affected pages, stale docs, and risk summaries.
[crates/gwiki/src/commands/review_report.rs:28-105]
[crates/gwiki/src/commands/review_report.rs:108-113]
[crates/gwiki/src/commands/review_report.rs:116-135]
[crates/gwiki/src/commands/review_report.rs:137-142]
[crates/gwiki/src/commands/review_report.rs:146-154]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(` | `execute [function]` | `35bfa54b-6c90-5664-b0ed-8297f5186faa` | 28-105 [crates/gwiki/src/commands/review_report.rs:28-105] | Indexed function `execute` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:28-105] |
| `ChangeSetInput` | class | `struct ChangeSetInput {` | `ChangeSetInput [class]` | `53e9eaa7-6daf-572d-a0f1-d3f052ea3138` | 108-113 [crates/gwiki/src/commands/review_report.rs:108-113] | Indexed class `ChangeSetInput` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:108-113] |
| `ChangeSetInput::from_options` | method | `fn from_options(options: ReviewReportOptions) -> Result<Self, WikiError> {` | `ChangeSetInput::from_options [method]` | `87ccb057-6082-5975-9132-befabdf8a08a` | 116-135 [crates/gwiki/src/commands/review_report.rs:116-135] | Indexed method `ChangeSetInput::from_options` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:116-135] |
| `ChangeSetInput::as_code_change_set` | method | `fn as_code_change_set(&self) -> CodeChangeSet {` | `ChangeSetInput::as_code_change_set [method]` | `78f91c6b-bcf0-5a6c-af97-611181823980` | 137-142 [crates/gwiki/src/commands/review_report.rs:137-142] | Indexed method `ChangeSetInput::as_code_change_set` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:137-142] |
| `ReportParts` | class | `struct ReportParts {` | `ReportParts [class]` | `8d8e8c76-8606-5655-b883-26b31356f7da` | 146-154 [crates/gwiki/src/commands/review_report.rs:146-154] | Indexed class `ReportParts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:146-154] |
| `ReviewReport` | class | `struct ReviewReport {` | `ReviewReport [class]` | `29ed9aee-730d-5af5-8b12-83f2ebe301e4` | 157-167 [crates/gwiki/src/commands/review_report.rs:157-167] | Indexed class `ReviewReport` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:157-167] |
| `ReviewAffectedPage` | class | `struct ReviewAffectedPage {` | `ReviewAffectedPage [class]` | `110949ba-94c9-5fae-8b50-99ad53221710` | 170-174 [crates/gwiki/src/commands/review_report.rs:170-174] | Indexed class `ReviewAffectedPage` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:170-174] |
| `RiskyDependencyShift` | class | `struct RiskyDependencyShift {` | `RiskyDependencyShift [class]` | `f5bfa044-7a23-561c-97e0-f65f7beecfba` | 177-183 [crates/gwiki/src/commands/review_report.rs:177-183] | Indexed class `RiskyDependencyShift` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:177-183] |
| `build_report_from_parts` | function | `fn build_report_from_parts(parts: ReportParts) -> ReviewReport {` | `build_report_from_parts [function]` | `39f0c0ea-2766-5b48-a5c9-ca2cf7f26332` | 185-211 [crates/gwiki/src/commands/review_report.rs:185-211] | Indexed function `build_report_from_parts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:185-211] |
| `render_markdown` | function | `fn render_markdown(report: &ReviewReport) -> String {` | `render_markdown [function]` | `2e8e7a53-5c56-5574-b617-9b3debe174f9` | 213-229 [crates/gwiki/src/commands/review_report.rs:213-229] | Indexed function `render_markdown` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:213-229] |
| `render_changes` | function | `fn render_changes(markdown: &mut String, changes: &ChangeSetInput) {` | `render_changes [function]` | `73da148a-57c7-5d68-bd42-66c01c7304cb` | 231-241 [crates/gwiki/src/commands/review_report.rs:231-241] | Indexed function `render_changes` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:231-241] |
| `render_affected_pages` | function | `fn render_affected_pages(markdown: &mut String, pages: &[ReviewAffectedPage]) {` | `render_affected_pages [function]` | `8f3c0a89-c1a9-5e6a-afbb-52b03eab60b0` | 243-260 [crates/gwiki/src/commands/review_report.rs:243-260] | Indexed function `render_affected_pages` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:243-260] |
| `render_stale_docs` | function | `fn render_stale_docs(markdown: &mut String, stale_docs: &[String]) {` | `render_stale_docs [function]` | `586fd394-1c1f-512e-a489-5b9b58f4f832` | 262-266 [crates/gwiki/src/commands/review_report.rs:262-266] | Indexed function `render_stale_docs` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:262-266] |
| `render_neighborhoods` | function | `fn render_neighborhoods(markdown: &mut String, neighborhoods: &[CodeGraphEdge]) {` | `render_neighborhoods [function]` | `ed8b9961-1e88-55b9-ae95-cbb711b90d91` | 268-294 [crates/gwiki/src/commands/review_report.rs:268-294] | Indexed function `render_neighborhoods` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:268-294] |
| `render_risky_shifts` | function | `fn render_risky_shifts(markdown: &mut String, report: &ReviewReport) {` | `render_risky_shifts [function]` | `286c3e93-3fff-594a-909f-e46840a6c55b` | 296-321 [crates/gwiki/src/commands/review_report.rs:296-321] | Indexed function `render_risky_shifts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:296-321] |
| `graph_neighborhoods` | function | `fn graph_neighborhoods(` | `graph_neighborhoods [function]` | `f2894f8c-9cdb-5bde-9a12-b872eb35290a` | 323-362 [crates/gwiki/src/commands/review_report.rs:323-362] | Indexed function `graph_neighborhoods` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:323-362] |
| `analytics_graph_from_edges` | function | `fn analytics_graph_from_edges(changes: &ChangeSetInput, edges: &[CodeGraphEdge]) -> AnalyticsGraph {` | `analytics_graph_from_edges [function]` | `05dcb72b-1931-5544-9025-91a3b0f3f7f0` | 364-399 [crates/gwiki/src/commands/review_report.rs:364-399] | Indexed function `analytics_graph_from_edges` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:364-399] |
| `risky_dependency_shifts` | function | `fn risky_dependency_shifts(` | `risky_dependency_shifts [function]` | `fa56147e-ff1b-5bd9-bb2a-35448e433bc3` | 401-430 [crates/gwiki/src/commands/review_report.rs:401-430] | Indexed function `risky_dependency_shifts` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:401-430] |
| `risk_from_score` | function | `fn risk_from_score(` | `risk_from_score [function]` | `99d0b375-f107-5934-8959-b57579fea38d` | 432-456 [crates/gwiki/src/commands/review_report.rs:432-456] | Indexed function `risk_from_score` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:432-456] |
| `changed_node_ids` | function | `fn changed_node_ids(changes: &ChangeSetInput, edges: &[CodeGraphEdge]) -> BTreeSet<String> {` | `changed_node_ids [function]` | `3695bdd7-6b70-580a-8f3e-6b4430b84492` | 458-471 [crates/gwiki/src/commands/review_report.rs:458-471] | Indexed function `changed_node_ids` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:458-471] |
| `changed_node_ids_from_graph` | function | `fn changed_node_ids_from_graph(` | `changed_node_ids_from_graph [function]` | `7a8e8ed3-2c00-57cf-8e39-f543abba64a5` | 473-484 [crates/gwiki/src/commands/review_report.rs:473-484] | Indexed function `changed_node_ids_from_graph` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:473-484] |
| `changed_files_from_diff` | function | `fn changed_files_from_diff(path: &Path) -> Result<Vec<String>, WikiError> {` | `changed_files_from_diff [function]` | `7a5c4fcd-0b43-5b6e-93dc-68c870a41d29` | 486-493 [crates/gwiki/src/commands/review_report.rs:486-493] | Indexed function `changed_files_from_diff` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:486-493] |
| `parse_unified_diff_files` | function | `fn parse_unified_diff_files(contents: &str) -> Vec<String> {` | `parse_unified_diff_files [function]` | `5c7366b9-abc3-5a0f-9ab5-701b1076f029` | 495-530 [crates/gwiki/src/commands/review_report.rs:495-530] | Indexed function `parse_unified_diff_files` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:495-530] |
| `trim_diff_path` | function | `fn trim_diff_path(path: &str) -> &str {` | `trim_diff_path [function]` | `7e6bd227-40f8-57f7-acc8-ece59ae816fd` | 532-534 [crates/gwiki/src/commands/review_report.rs:532-534] | Indexed function `trim_diff_path` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:532-534] |
| `review_affected_page` | function | `fn review_affected_page(page: AffectedPage) -> ReviewAffectedPage {` | `review_affected_page [function]` | `97f30df8-5858-5eb8-8f0a-813dbca7fbe0` | 536-546 [crates/gwiki/src/commands/review_report.rs:536-546] | Indexed function `review_affected_page` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:536-546] |
| `render_string_list` | function | `fn render_string_list(markdown: &mut String, label: &str, values: &[String]) {` | `render_string_list [function]` | `39072454-0bae-53ad-badf-5f1daa074d74` | 548-562 [crates/gwiki/src/commands/review_report.rs:548-562] | Indexed function `render_string_list` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:548-562] |
| `unique_non_empty` | function | `fn unique_non_empty(values: Vec<String>) -> Vec<String> {` | `unique_non_empty [function]` | `a966dfc3-d6c6-576e-90d7-8db3f4c4caf1` | 564-572 [crates/gwiki/src/commands/review_report.rs:564-572] | Indexed function `unique_non_empty` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:564-572] |
| `unique_edges` | function | `fn unique_edges(edges: Vec<CodeGraphEdge>) -> Vec<CodeGraphEdge> {` | `unique_edges [function]` | `183b1cd2-31f4-50cd-b33b-39ac7a162f59` | 574-588 [crates/gwiki/src/commands/review_report.rs:574-588] | Indexed function `unique_edges` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:574-588] |
| `degradation_source` | function | `fn degradation_source(degradation: &DegradationKind) -> String {` | `degradation_source [function]` | `5aeb21d1-226b-50df-bce1-025a03eb7aee` | 590-603 [crates/gwiki/src/commands/review_report.rs:590-603] | Indexed function `degradation_source` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:590-603] |
| `is_graph_blocking_degraded_source` | function | `fn is_graph_blocking_degraded_source(source: &str) -> bool {` | `is_graph_blocking_degraded_source [function]` | `46308355-3e7b-5932-80e9-f38783dcc80a` | 605-612 [crates/gwiki/src/commands/review_report.rs:605-612] | Indexed function `is_graph_blocking_degraded_source` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:605-612] |
| `optional_falkor_config` | function | `fn optional_falkor_config(conn: &mut postgres::Client) -> Result<Option<FalkorConfig>, WikiError> {` | `optional_falkor_config [function]` | `1ee04ed4-47fc-5e36-8f8b-59364abf91c7` | 614-626 [crates/gwiki/src/commands/review_report.rs:614-626] | Indexed function `optional_falkor_config` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:614-626] |
| `review_report_renders_markdown_with_risks_and_metadata` | function | `fn review_report_renders_markdown_with_risks_and_metadata() {` | `review_report_renders_markdown_with_risks_and_metadata [function]` | `92612fba-0461-5c1a-9c28-975bde936bed` | 642-711 [crates/gwiki/src/commands/review_report.rs:642-711] | Indexed function `review_report_renders_markdown_with_risks_and_metadata` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:642-711] |
| `review_report_degrades_without_graph_analytics` | function | `fn review_report_degrades_without_graph_analytics() {` | `review_report_degrades_without_graph_analytics [function]` | `698c0ffb-57cb-5aff-bb56-16d0de043e90` | 714-736 [crates/gwiki/src/commands/review_report.rs:714-736] | Indexed function `review_report_degrades_without_graph_analytics` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:714-736] |
| `review_report_maps_semantic_partial_data_degradation` | function | `fn review_report_maps_semantic_partial_data_degradation() {` | `review_report_maps_semantic_partial_data_degradation [function]` | `bd30a0ea-59f3-5803-91dd-c8fbcdc1050c` | 739-746 [crates/gwiki/src/commands/review_report.rs:739-746] | Indexed function `review_report_maps_semantic_partial_data_degradation` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:739-746] |
| `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path` | function | `fn parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path() {` | `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path [function]` | `c150bf4a-d8c1-5534-acb0-ffe70953c4c4` | 749-760 [crates/gwiki/src/commands/review_report.rs:749-760] | Indexed function `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:749-760] |
| `parse_unified_diff_files_sanitizes_unsafe_paths` | function | `fn parse_unified_diff_files_sanitizes_unsafe_paths() {` | `parse_unified_diff_files_sanitizes_unsafe_paths [function]` | `c7d2767b-dce3-596f-920f-a3ad37bf0ecf` | 763-776 [crates/gwiki/src/commands/review_report.rs:763-776] | Indexed function `parse_unified_diff_files_sanitizes_unsafe_paths` in `crates/gwiki/src/commands/review_report.rs`. [crates/gwiki/src/commands/review_report.rs:763-776] |
