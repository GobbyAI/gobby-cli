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

`crates/gwiki/src/commands/review_report.rs` exposes 37 indexed API symbols.
[crates/gwiki/src/commands/review_report.rs:28-105]
[crates/gwiki/src/commands/review_report.rs:108-113]
[crates/gwiki/src/commands/review_report.rs:115-143]
[crates/gwiki/src/commands/review_report.rs:116-135]
[crates/gwiki/src/commands/review_report.rs:137-142]

## API Symbols

- `execute` (function) component `execute [function]` (`152523ff-0977-56ed-88ae-e5fe3a199e54`) lines 28-105 [crates/gwiki/src/commands/review_report.rs:28-105]
  - Signature: `pub(crate) fn execute(`
  - Purpose: It resolves the requested wiki scope, validates and opens the read-only PostgreSQL/Falkor-backed index, loads wiki graph and provenance data, computes affected pages, degraded sources, neighborhoods, and health, and then conditionally assembles the review report `CommandOutcome` or returns a `WikiError` on any failure. [crates/gwiki/src/commands/review_report.rs:28-105]
- `ChangeSetInput` (class) component `ChangeSetInput [class]` (`29ab6167-38e2-5f22-a4bc-20b6632f9ca3`) lines 108-113 [crates/gwiki/src/commands/review_report.rs:108-113]
  - Signature: `struct ChangeSetInput {`
  - Purpose: `ChangeSetInput` is a data-carrying struct that bundles target file paths, symbol names, an optional diff file path, and an output string as inputs for change-set processing. [crates/gwiki/src/commands/review_report.rs:108-113]
- `ChangeSetInput` (class) component `ChangeSetInput [class]` (`9dd76cfa-ba2e-5ea1-9e0d-264ef809e7c8`) lines 115-143 [crates/gwiki/src/commands/review_report.rs:115-143]
  - Signature: `impl ChangeSetInput {`
  - Purpose: `ChangeSetInput` is a validated review-report input wrapper that merges explicit files with files extracted from an optional diff, deduplicates and filters empty file/symbol entries, rejects empty change sets, and can project itself into a `CodeChangeSet` containing only `files` and `symbols`. [crates/gwiki/src/commands/review_report.rs:115-143]
- `ChangeSetInput.from_options` (method) component `ChangeSetInput.from_options [method]` (`b4df68ed-9b31-5cac-9a6b-b6c758951785`) lines 116-135 [crates/gwiki/src/commands/review_report.rs:116-135]
  - Signature: `fn from_options(options: ReviewReportOptions) -> Result<Self, WikiError> {`
  - Purpose: `from_options` builds a `Self` by merging explicit files with files extracted from `diff_path`, deduplicating and dropping empties from both files and symbols, rejecting the input if neither collection is non-empty, and carrying through `diff_path` and `output` unchanged. [crates/gwiki/src/commands/review_report.rs:116-135]
- `ChangeSetInput.as_code_change_set` (method) component `ChangeSetInput.as_code_change_set [method]` (`5dd5d876-3423-59cf-ba6e-0aeb84f03846`) lines 137-142 [crates/gwiki/src/commands/review_report.rs:137-142]
  - Signature: `fn as_code_change_set(&self) -> CodeChangeSet {`
  - Purpose: Returns a new `CodeChangeSet` populated with cloned `files` and `symbols` from `self`. [crates/gwiki/src/commands/review_report.rs:137-142]
- `ReportParts` (class) component `ReportParts [class]` (`90126ba3-8a58-5668-bed6-6b65e5b6a6e5`) lines 146-154 [crates/gwiki/src/commands/review_report.rs:146-154]
  - Signature: `struct ReportParts {`
  - Purpose: `ReportParts` is an aggregate data structure that packages a report’s `ScopeIdentity`, `ChangeSetInput`, impacted and stale pages, code-graph neighborhood edges, an optional `AnalyticsGraph`, and identifiers for degraded sources. [crates/gwiki/src/commands/review_report.rs:146-154]
- `ReviewReport` (class) component `ReviewReport [class]` (`ea689200-fe3b-52dc-950a-926184fbdd13`) lines 157-167 [crates/gwiki/src/commands/review_report.rs:157-167]
  - Signature: `struct ReviewReport {`
  - Purpose: `ReviewReport` is an aggregate review result that captures the command and scope of analysis, whether the run was degraded and from which sources, and the computed change-impact metadata including the change set, affected pages, stale docs, graph-neighborhood diffs, and risky dependency shifts. [crates/gwiki/src/commands/review_report.rs:157-167]
- `ReviewAffectedPage` (class) component `ReviewAffectedPage [class]` (`4fe05110-53f8-5ae4-9d5a-b563efdec12e`) lines 170-174 [crates/gwiki/src/commands/review_report.rs:170-174]
  - Signature: `struct ReviewAffectedPage {`
  - Purpose: `ReviewAffectedPage` is a simple data structure that records a page’s path along with the source IDs and source paths that were affected by the review. [crates/gwiki/src/commands/review_report.rs:170-174]
- `RiskyDependencyShift` (class) component `RiskyDependencyShift [class]` (`ed9d3bf5-d253-556d-bf42-8c8189d23e76`) lines 177-183 [crates/gwiki/src/commands/review_report.rs:177-183]
  - Signature: `struct RiskyDependencyShift {`
  - Purpose: `RiskyDependencyShift` is a dependency-analysis record that ties a `NodeRef` to its graph `degree`, numeric `score`, `bridge` flag, and a list of textual `reasons` explaining why the dependency shift is considered risky. [crates/gwiki/src/commands/review_report.rs:177-183]
- `build_report_from_parts` (function) component `build_report_from_parts [function]` (`6f0e4dee-f9a7-56b3-96d5-c0fe1ca1521f`) lines 185-211 [crates/gwiki/src/commands/review_report.rs:185-211]
  - Signature: `fn build_report_from_parts(parts: ReportParts) -> ReviewReport {`
  - Purpose: Builds a `ReviewReport` from `ReportParts` by deduplicating non-empty degraded sources, deriving `degraded` from that list, computing risky dependency shifts from the optional analytics graph and changes, and mapping affected/stale pages and neighborhoods into the report fields. [crates/gwiki/src/commands/review_report.rs:185-211]
- `render_markdown` (function) component `render_markdown [function]` (`f43dec01-c648-537d-869a-de68de19728f`) lines 213-229 [crates/gwiki/src/commands/review_report.rs:213-229]
  - Signature: `fn render_markdown(report: &ReviewReport) -> String {`
  - Purpose: `render_markdown` builds a Markdown review report string with YAML-style front matter derived from `ReviewReport` metadata (`scope`, `degraded`, `degraded_sources`), then appends a शीर्ष-level “Review report” heading and renders the report’s changes, affected pages, stale docs, graph neighborhoods, and risky shifts into the body. [crates/gwiki/src/commands/review_report.rs:213-229]
- `render_changes` (function) component `render_changes [function]` (`d412b22f-d83a-542e-9dd5-ad0a486824d4`) lines 231-241 [crates/gwiki/src/commands/review_report.rs:231-241]
  - Signature: `fn render_changes(markdown: &mut String, changes: &ChangeSetInput) {`
  - Purpose: `render_changes` appends a `## Change set` Markdown section to `markdown`, renders the `files` and `symbols` lists, optionally adds a `Diff:` line with `diff_path`, and terminates the block with a blank line. [crates/gwiki/src/commands/review_report.rs:231-241]
- `render_affected_pages` (function) component `render_affected_pages [function]` (`253ebd51-a26e-5ec4-923d-c3a4de87e95f`) lines 243-260 [crates/gwiki/src/commands/review_report.rs:243-260]
  - Signature: `fn render_affected_pages(markdown: &mut String, pages: &[ReviewAffectedPage]) {`
  - Purpose: Appends an “Affected wiki pages” Markdown section to `markdown`, emitting `- none` when `pages` is empty or otherwise listing each `page_path` as a bullet with an optional `from <source_paths>` suffix. [crates/gwiki/src/commands/review_report.rs:243-260]
- `render_stale_docs` (function) component `render_stale_docs [function]` (`86578dab-0dcf-548b-b932-e81bc173ee81`) lines 262-266 [crates/gwiki/src/commands/review_report.rs:262-266]
  - Signature: `fn render_stale_docs(markdown: &mut String, stale_docs: &[String]) {`
  - Purpose: It appends a `## Stale docs` section to the provided markdown buffer, renders the `stale_docs` entries as a labeled `Docs` list, and adds a trailing newline. [crates/gwiki/src/commands/review_report.rs:262-266]
- `render_neighborhoods` (function) component `render_neighborhoods [function]` (`4cff988a-a08b-5d9a-8398-61912b677a46`) lines 268-294 [crates/gwiki/src/commands/review_report.rs:268-294]
  - Signature: `fn render_neighborhoods(markdown: &mut String, neighborhoods: &[CodeGraphEdge]) {`
  - Purpose: Appends a `## Changed graph neighborhoods` markdown section that either records `- none` when the slice is empty or emits one bullet per `CodeGraphEdge` with its edge label, quoted `source` and `target`, and optional `file_path:line` annotation. [crates/gwiki/src/commands/review_report.rs:268-294]
- `render_risky_shifts` (function) component `render_risky_shifts [function]` (`94d887e8-f5f6-5f2f-958a-ddf9bb45f041`) lines 296-321 [crates/gwiki/src/commands/review_report.rs:296-321]
  - Signature: `fn render_risky_shifts(markdown: &mut String, report: &ReviewReport) {`
  - Purpose: Appends a `## Risky dependency shifts` Markdown section to `markdown`, emitting an omission notice if any degraded source blocks graph analytics, `- none` when no risks exist, or one bullet per `report.risky_dependency_shifts` entry with node id, degree, score, and joined reasons. [crates/gwiki/src/commands/review_report.rs:296-321]
- `graph_neighborhoods` (function) component `graph_neighborhoods [function]` (`1bb76d09-aa5c-5bcf-a732-531c64cf691a`) lines 323-362 [crates/gwiki/src/commands/review_report.rs:323-362]
  - Signature: `fn graph_neighborhoods(`
  - Purpose: `graph_neighborhoods` collects and deduplicates code-graph edges for all changed files and symbols in a project-scoped `SearchScope` via FalkorDB queries, while recording degradation reasons and returning an empty set when the scope is non-project or FalkorDB is unavailable, and converting query failures into `WikiError::Config`. [crates/gwiki/src/commands/review_report.rs:323-362]
- `analytics_graph_from_edges` (function) component `analytics_graph_from_edges [function]` (`9b5cdf2e-1ef8-5420-b7fe-4a6059045383`) lines 364-398 [crates/gwiki/src/commands/review_report.rs:364-398]
  - Signature: `fn analytics_graph_from_edges(changes: &ChangeSetInput, edges: &[CodeGraphEdge]) -> AnalyticsGraph {`
  - Purpose: Constructs an `AnalyticsGraph` by seeding `changed` nodes from `changes` and `edges` with weight `3.0`, adding any remaining edge endpoints as `neighbor` nodes with weight `1.0`, and copying the input edges into `AnalyticsEdge` records. [crates/gwiki/src/commands/review_report.rs:364-398]
- `risky_dependency_shifts` (function) component `risky_dependency_shifts [function]` (`79d07ba1-5f64-5371-b875-4de369718fc0`) lines 400-429 [crates/gwiki/src/commands/review_report.rs:400-429]
  - Signature: `fn risky_dependency_shifts(`
  - Purpose: It analyzes the graph, filters centrality results down to nodes changed by `changes`, converts each eligible node into a `RiskyDependencyShift` using bridge membership and the graph’s maximum centrality as context, and returns the shifts sorted by descending score with node ID as the tie-breaker. [crates/gwiki/src/commands/review_report.rs:400-429]
- `risk_from_score` (function) component `risk_from_score [function]` (`5a4af537-59a5-5256-b863-50cbfe2c41ef`) lines 431-455 [crates/gwiki/src/commands/review_report.rs:431-455]
  - Signature: `fn risk_from_score(`
  - Purpose: Returns `Some(RiskyDependencyShift)` only when the scored node is a bridge or has high centrality (`degree >= 2` or equals `max_score` when `max_score > 0.0`), populating `bridge` and reason strings accordingly, otherwise returns `None`. [crates/gwiki/src/commands/review_report.rs:431-455]
- `changed_node_ids` (function) component `changed_node_ids [function]` (`48f7739e-0460-532f-98b5-fdc206c2955b`) lines 457-470 [crates/gwiki/src/commands/review_report.rs:457-470]
  - Signature: `fn changed_node_ids(changes: &ChangeSetInput, edges: &[CodeGraphEdge]) -> BTreeSet<String> {`
  - Purpose: Returns a `BTreeSet<String>` containing all symbols explicitly listed in `changes.symbols`, plus the `source` and `target` node IDs of any `edges` whose `file_path` matches one of the paths in `changes.files`. [crates/gwiki/src/commands/review_report.rs:457-470]
- `changed_node_ids_from_graph` (function) component `changed_node_ids_from_graph [function]` (`b65d824a-6bab-54c4-a0bf-12cf85ab9577`) lines 472-483 [crates/gwiki/src/commands/review_report.rs:472-483]
  - Signature: `fn changed_node_ids_from_graph(`
  - Purpose: Returns a `BTreeSet<String>` containing the union of `changes.symbols` and the `id` of every `graph.nodes` entry whose `kind` equals `"changed"`. [crates/gwiki/src/commands/review_report.rs:472-483]
- `changed_files_from_diff` (function) component `changed_files_from_diff [function]` (`563c9e10-7dae-55b6-9091-17c62dc72689`) lines 485-492 [crates/gwiki/src/commands/review_report.rs:485-492]
  - Signature: `fn changed_files_from_diff(path: &Path) -> Result<Vec<String>, WikiError> {`
  - Purpose: Reads the diff file at `path` into a string, maps any read failure into `WikiError::Io` with action `"read review-report diff"`, and returns the list of changed file paths extracted by `parse_unified_diff_files`. [crates/gwiki/src/commands/review_report.rs:485-492]
- `parse_unified_diff_files` (function) component `parse_unified_diff_files [function]` (`0cc5aa25-3130-5ed1-999b-4d1a0ffcadaa`) lines 494-529 [crates/gwiki/src/commands/review_report.rs:494-529]
  - Signature: `fn parse_unified_diff_files(contents: &str) -> Vec<String> {`
  - Purpose: It scans unified diff header lines, extracts candidate file paths from `+++ b/`, `--- a/`, and `diff --git a/... b/...` entries, sanitizes each path to reject empty/absolute/parent-traversal inputs, deduplicates them in sorted order, and returns the resulting `Vec<String>`. [crates/gwiki/src/commands/review_report.rs:494-529]
- `trim_diff_path` (function) component `trim_diff_path [function]` (`eaa08a75-1975-5102-bb09-a178f2efdf4e`) lines 531-533 [crates/gwiki/src/commands/review_report.rs:531-533]
  - Signature: `fn trim_diff_path(path: &str) -> &str {`
  - Purpose: `trim_diff_path` returns the input string slice with leading/trailing whitespace removed and any leading/trailing double quotes stripped from both ends. [crates/gwiki/src/commands/review_report.rs:531-533]
- `review_affected_page` (function) component `review_affected_page [function]` (`59895caf-8598-56e7-a8bc-7e92a82f2b95`) lines 535-545 [crates/gwiki/src/commands/review_report.rs:535-545]
  - Signature: `fn review_affected_page(page: AffectedPage) -> ReviewAffectedPage {`
  - Purpose: It converts an `AffectedPage` into a `ReviewAffectedPage` by copying `source_ids`, stringifying `page_path`, and mapping each `source_path` `Path` into a `String`. [crates/gwiki/src/commands/review_report.rs:535-545]
- `render_string_list` (function) component `render_string_list [function]` (`f0f2e308-cece-5593-bed5-82845620b973`) lines 547-561 [crates/gwiki/src/commands/review_report.rs:547-561]
  - Signature: `fn render_string_list(markdown: &mut String, label: &str, values: &[String]) {`
  - Purpose: Appends Markdown-formatted list entries to `markdown` by writing `- <label>: none` when `values` is empty, otherwise writing one bullet per string as `- <label>: \`value\``. [crates/gwiki/src/commands/review_report.rs:547-561]
- `unique_non_empty` (function) component `unique_non_empty [function]` (`e3159784-2788-5a6c-a591-f2057bbfa5cf`) lines 563-571 [crates/gwiki/src/commands/review_report.rs:563-571]
  - Signature: `fn unique_non_empty(values: Vec<String>) -> Vec<String> {`
  - Purpose: Returns a lexicographically sorted `Vec<String>` of the input strings after trimming whitespace, removing empty results, and deduplicating them with a `BTreeSet`. [crates/gwiki/src/commands/review_report.rs:563-571]
- `unique_edges` (function) component `unique_edges [function]` (`bf5e0a4e-7e35-59e9-a013-c1306cf4ab7d`) lines 573-587 [crates/gwiki/src/commands/review_report.rs:573-587]
  - Signature: `fn unique_edges(edges: Vec<CodeGraphEdge>) -> Vec<CodeGraphEdge> {`
  - Purpose: `unique_edges` deduplicates a `Vec<CodeGraphEdge>` by retaining only the first edge for each unique `(edge, source, target, file_path, line)` tuple, preserving the input order of the surviving entries. [crates/gwiki/src/commands/review_report.rs:573-587]
- `degradation_source` (function) component `degradation_source [function]` (`297ef0fc-25a3-54dd-8422-7c753d9ee968`) lines 589-602 [crates/gwiki/src/commands/review_report.rs:589-602]
  - Signature: `fn degradation_source(degradation: &DegradationKind) -> String {`
  - Purpose: It converts a `DegradationKind` into a canonical degradation source string, using a special constant for `ServiceUnavailable` when `service == "gcode_code_graph"` and otherwise formatting variant-specific identifiers from the service, unavailable items, component, or fixed labels like `stale_index` and `skipped_artifacts`. [crates/gwiki/src/commands/review_report.rs:589-602]
- `is_graph_blocking_degraded_source` (function) component `is_graph_blocking_degraded_source [function]` (`f4262272-9f45-596a-b70c-ae68b3125fe2`) lines 604-611 [crates/gwiki/src/commands/review_report.rs:604-611]
  - Signature: `fn is_graph_blocking_degraded_source(source: &str) -> bool {`
  - Purpose: Returns `true` when `source` exactly matches one of the three graph-blocking degraded-source constants (`DEGRADED_FALKORDB_UNAVAILABLE`, `DEGRADED_GCODE_CODE_GRAPH_UNAVAILABLE`, or `DEGRADED_SHARED_CODE_GRAPH_UNAVAILABLE`), and `false` otherwise. [crates/gwiki/src/commands/review_report.rs:604-611]
- `optional_falkor_config` (function) component `optional_falkor_config [function]` (`3747302d-1a4b-5f52-b22b-ca5caf22dc22`) lines 613-625 [crates/gwiki/src/commands/review_report.rs:613-625]
  - Signature: `fn optional_falkor_config(conn: &mut postgres::Client) -> Result<Option<FalkorConfig>, WikiError> {`
  - Purpose: Resolves an optional `FalkorConfig` by building an `AiConfigSource` from the provided PostgreSQL client and `Gobby` home directory, then delegating to `gobby_core::config::resolve_falkordb_config`, mapping any configuration lookup failures into `WikiError::Config`. [crates/gwiki/src/commands/review_report.rs:613-625]
- `review_report_renders_markdown_with_risks_and_metadata` (function) component `review_report_renders_markdown_with_risks_and_metadata [function]` (`1eab52e1-01fb-5acb-bd3a-0e9358bb8ad4`) lines 639-706 [crates/gwiki/src/commands/review_report.rs:639-706]
  - Signature: `fn review_report_renders_markdown_with_risks_and_metadata() {`
  - Purpose: I’m locating the test body so I can summarize the exact behavior rather than guessing from the truncated snippet.The exact symbol didn’t match in the index, so I’m widening the search to the surrounding test name and helper path.I haven’t found the symbol with a text search yet. Next I’m checking whether the code index is available so I can search the AST-backed symbol graph instead of raw text.This test builds a synthetic `ReportParts` input with changed files, affected/stale pages, graph edges, and analytics nodes/edges, then verifies that `build_report_from_parts` renders a Markdown review report containing the expected risk and metadata sections. [crates/gwiki/src/commands/review_report.rs:639-706]
- `review_report_degrades_without_graph_analytics` (function) component `review_report_degrades_without_graph_analytics [function]` (`e0de044b-8932-538c-b060-253b7a98d3c4`) lines 709-731 [crates/gwiki/src/commands/review_report.rs:709-731]
  - Signature: `fn review_report_degrades_without_graph_analytics() {`
  - Purpose: This test verifies that `build_report_from_parts` marks a report as degraded when `analytics_graph` is `None` and `degraded_sources` includes `shared_code_graph_unavailable`, leaves `risky_dependency_shifts` empty, and renders markdown that explicitly reports the degraded state and missing graph/analytics. [crates/gwiki/src/commands/review_report.rs:709-731]
- `review_report_maps_semantic_partial_data_degradation` (function) component `review_report_maps_semantic_partial_data_degradation [function]` (`28f51d74-41f1-5ad6-9f11-d831c6af519f`) lines 734-741 [crates/gwiki/src/commands/review_report.rs:734-741]
  - Signature: `fn review_report_maps_semantic_partial_data_degradation() {`
  - Purpose: This test asserts that `degradation_source` maps a `DegradationKind::PartialData` with `component = "semantic"` to the source label `"semantic_partial"`. [crates/gwiki/src/commands/review_report.rs:734-741]
- `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path` (function) component `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path [function]` (`822dfed8-a116-54e6-9d05-593c4e4caaa9`) lines 744-755 [crates/gwiki/src/commands/review_report.rs:744-755]
  - Signature: `fn parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path() {`
  - Purpose: Verifies that `parse_unified_diff_files` extracts the new right-hand path for a rename diff and omits entries whose right-hand path is empty, returning `["src/deleted.rs", "src/new.rs"]`. [crates/gwiki/src/commands/review_report.rs:744-755]
- `parse_unified_diff_files_sanitizes_unsafe_paths` (function) component `parse_unified_diff_files_sanitizes_unsafe_paths [function]` (`52f350c5-ef4b-5928-ace7-18fcde0eb7bc`) lines 758-771 [crates/gwiki/src/commands/review_report.rs:758-771]
  - Signature: `fn parse_unified_diff_files_sanitizes_unsafe_paths() {`
  - Purpose: Verifies that `parse_unified_diff_files` normalizes diff paths and filters out unsafe or non-file entries, returning only sanitized relative file paths like `src/deleted.rs` and `src/safe.rs`. [crates/gwiki/src/commands/review_report.rs:758-771]

