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

# crates/gwiki/src/commands/review_report.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Implements the `gwiki review-report` command: it resolves the selected scope, normalizes review input, opens a read-only PostgreSQL-backed context when available, loads wiki/provenance facts, computes affected pages and code-graph neighborhoods, assesses degradation and dependency risk, and returns either a markdown `CommandOutcome` or a `WikiError`. The file is organized around small data carriers (`ChangeSetInput`, `ReportParts`, `ReviewReport`, `ReviewAffectedPage`, `RiskyDependencyShift`) plus helpers that deduplicate and sanitize change inputs, derive graph-based impact data, map degradation sources, and render the final report sections.
[crates/gwiki/src/commands/review_report.rs:28-105]
[crates/gwiki/src/commands/review_report.rs:108-113]
[crates/gwiki/src/commands/review_report.rs:115-143]
[crates/gwiki/src/commands/review_report.rs:116-135]
[crates/gwiki/src/commands/review_report.rs:137-142]

## API Symbols

- `execute` (function) component `execute [function]` (`35bfa54b-6c90-5664-b0ed-8297f5186faa`) lines 28-105 [crates/gwiki/src/commands/review_report.rs:28-105]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Resolves the scope and change set, opens a read-only PostgreSQL-backed graph context, loads wiki/provenance facts, computes affected pages and graph neighborhoods, checks repository health and graph readiness, and then assembles a review-report 'CommandOutcome' or returns a 'WikiError' on configuration/query failures. [crates/gwiki/src/commands/review_report.rs:28-105]
- `ChangeSetInput` (class) component `ChangeSetInput [class]` (`53e9eaa7-6daf-572d-a0f1-d3f052ea3138`) lines 108-113 [crates/gwiki/src/commands/review_report.rs:108-113]
  - Signature: `struct ChangeSetInput {`
  - Purpose: 'ChangeSetInput' is a data-transfer struct that captures untrusted change-set metadata: a list of file paths, a list of symbol names, an optional diff file path, and an output string. [crates/gwiki/src/commands/review_report.rs:108-113]
- `ChangeSetInput` (class) component `ChangeSetInput [class]` (`0991cff6-7a21-51d0-a12b-22ca5195d5c8`) lines 115-143 [crates/gwiki/src/commands/review_report.rs:115-143]
  - Signature: `impl ChangeSetInput {`
  - Purpose: 'ChangeSetInput' normalizes review-report CLI options into a validated input object by merging and de-duplicating file/symbol selections, optionally augmenting files from a diff, rejecting empty change sets, and exposing a conversion to 'CodeChangeSet'. [crates/gwiki/src/commands/review_report.rs:115-143]
- `ChangeSetInput.from_options` (method) component `ChangeSetInput.from_options [method]` (`87ccb057-6082-5975-9132-befabdf8a08a`) lines 116-135 [crates/gwiki/src/commands/review_report.rs:116-135]
  - Signature: `fn from_options(options: ReviewReportOptions) -> Result<Self, WikiError> {`
  - Purpose: 'from_options' builds a 'ReviewReport' from 'ReviewReportOptions' by merging file paths with files derived from an optional diff, deduplicating and dropping empties from files and symbols, rejecting requests with no file or symbol input, and then returning the assembled struct with the original diff path and output. [crates/gwiki/src/commands/review_report.rs:116-135]
- `ChangeSetInput.as_code_change_set` (method) component `ChangeSetInput.as_code_change_set [method]` (`78f91c6b-bcf0-5a6c-af97-611181823980`) lines 137-142 [crates/gwiki/src/commands/review_report.rs:137-142]
  - Signature: `fn as_code_change_set(&self) -> CodeChangeSet {`
  - Purpose: Returns a new 'CodeChangeSet' by cloning and copying the current instance’s 'files' and 'symbols' collections into it. [crates/gwiki/src/commands/review_report.rs:137-142]
- `ReportParts` (class) component `ReportParts [class]` (`8d8e8c76-8606-5655-b883-26b31356f7da`) lines 146-154 [crates/gwiki/src/commands/review_report.rs:146-154]
  - Signature: `struct ReportParts {`
  - Purpose: 'ReportParts' is a data-only aggregate struct that packages a report’s scope, change set input, affected and stale page paths, graph neighborhoods, optional analytics graph, and a list of degraded source identifiers. [crates/gwiki/src/commands/review_report.rs:146-154]
- `ReviewReport` (class) component `ReviewReport [class]` (`29ed9aee-730d-5af5-8b12-83f2ebe301e4`) lines 157-167 [crates/gwiki/src/commands/review_report.rs:157-167]
  - Signature: `struct ReviewReport {`
  - Purpose: 'ReviewReport' is a data-only struct that aggregates a review command’s scope, degradation state and sources, proposed changes, affected pages, stale documentation, changed code-graph neighborhoods, and risky dependency shifts. [crates/gwiki/src/commands/review_report.rs:157-167]
- `ReviewAffectedPage` (class) component `ReviewAffectedPage [class]` (`110949ba-94c9-5fae-8b50-99ad53221710`) lines 170-174 [crates/gwiki/src/commands/review_report.rs:170-174]
  - Signature: `struct ReviewAffectedPage {`
  - Purpose: 'ReviewAffectedPage' is a data structure that identifies a page by 'page_path' and records the associated source identifiers and source file paths in 'source_ids' and 'source_paths' for review impact tracking. [crates/gwiki/src/commands/review_report.rs:170-174]
- `RiskyDependencyShift` (class) component `RiskyDependencyShift [class]` (`f5bfa044-7a23-561c-97e0-f65f7beecfba`) lines 177-183 [crates/gwiki/src/commands/review_report.rs:177-183]
  - Signature: `struct RiskyDependencyShift {`
  - Purpose: 'RiskyDependencyShift' is a data-only struct that records a graph node reference, its dependency degree, a floating-point risk score, a bridge flag, and a list of explanatory reasons for the shift. [crates/gwiki/src/commands/review_report.rs:177-183]
- `build_report_from_parts` (function) component `build_report_from_parts [function]` (`39f0c0ea-2766-5b48-a5c9-ca2cf7f26332`) lines 185-211 [crates/gwiki/src/commands/review_report.rs:185-211]
  - Signature: `fn build_report_from_parts(parts: ReportParts) -> ReviewReport {`
  - Purpose: Constructs a 'ReviewReport' from 'ReportParts' by deduplicating non-empty degraded sources, deriving risky dependency shifts from the optional analytics graph, converting affected pages and stale page paths into report-ready forms, and setting the degraded flag based on whether any degraded sources remain. [crates/gwiki/src/commands/review_report.rs:185-211]
- `render_markdown` (function) component `render_markdown [function]` (`2e8e7a53-5c56-5574-b617-9b3debe174f9`) lines 213-229 [crates/gwiki/src/commands/review_report.rs:213-229]
  - Signature: `fn render_markdown(report: &ReviewReport) -> String {`
  - Purpose: Builds and returns a Markdown review report string with YAML front matter for 'command', 'scope', 'degraded', and 'degraded_sources', then appends sectioned content rendered from the report’s changes, affected pages, stale docs, graph neighborhoods, and risky shifts. [crates/gwiki/src/commands/review_report.rs:213-229]
- `render_changes` (function) component `render_changes [function]` (`73da148a-57c7-5d68-bd42-66c01c7304cb`) lines 231-241 [crates/gwiki/src/commands/review_report.rs:231-241]
  - Signature: `fn render_changes(markdown: &mut String, changes: &ChangeSetInput) {`
  - Purpose: Appends a “## Change set” section to the provided Markdown buffer, rendering the 'files' and 'symbols' lists and, when present, a quoted 'diff_path' line followed by a trailing blank line. [crates/gwiki/src/commands/review_report.rs:231-241]
- `render_affected_pages` (function) component `render_affected_pages [function]` (`8f3c0a89-c1a9-5e6a-afbb-52b03eab60b0`) lines 243-260 [crates/gwiki/src/commands/review_report.rs:243-260]
  - Signature: `fn render_affected_pages(markdown: &mut String, pages: &[ReviewAffectedPage]) {`
  - Purpose: Appends a “Affected wiki pages” Markdown section to 'markdown', emitting '- none' when 'pages' is empty, otherwise adding one bullet per page with the page path in single quotes and an optional 'from' clause listing comma-separated source paths. [crates/gwiki/src/commands/review_report.rs:243-260]
- `render_stale_docs` (function) component `render_stale_docs [function]` (`586fd394-1c1f-512e-a489-5b9b58f4f832`) lines 262-266 [crates/gwiki/src/commands/review_report.rs:262-266]
  - Signature: `fn render_stale_docs(markdown: &mut String, stale_docs: &[String]) {`
  - Purpose: Appends a '## Stale docs' section to the provided Markdown buffer, renders 'stale_docs' as a '"Docs"' string list, and then adds a trailing newline. [crates/gwiki/src/commands/review_report.rs:262-266]
- `render_neighborhoods` (function) component `render_neighborhoods [function]` (`ed8b9961-1e88-55b9-ae95-cbb711b90d91`) lines 268-294 [crates/gwiki/src/commands/review_report.rs:268-294]
  - Signature: `fn render_neighborhoods(markdown: &mut String, neighborhoods: &[CodeGraphEdge]) {`
  - Purpose: Appends a “Changed graph neighborhoods” section to the provided Markdown string, listing each 'CodeGraphEdge' as a bullet with its edge label, source and target nodes, and optional file path and line number, or '- none' if the slice is empty. [crates/gwiki/src/commands/review_report.rs:268-294]
- `render_risky_shifts` (function) component `render_risky_shifts [function]` (`286c3e93-3fff-594a-909f-e46840a6c55b`) lines 296-321 [crates/gwiki/src/commands/review_report.rs:296-321]
  - Signature: `fn render_risky_shifts(markdown: &mut String, report: &ReviewReport) {`
  - Purpose: Appends a “Risky dependency shifts” markdown section that either reports graph/analytics degradation, emits '- none' when no risky shifts exist, or lists each risky node with its degree, formatted score, and joined reasons. [crates/gwiki/src/commands/review_report.rs:296-321]
- `graph_neighborhoods` (function) component `graph_neighborhoods [function]` (`f2894f8c-9cdb-5bde-9a12-b872eb35290a`) lines 323-362 [crates/gwiki/src/commands/review_report.rs:323-362]
  - Signature: `fn graph_neighborhoods(`
  - Purpose: 'graph_neighborhoods' returns the deduplicated code-graph edges for the changed files and symbols in a project, but degrades to an empty result while recording unavailable-source markers if the scope is not a project or FalkorDB/config is missing. [crates/gwiki/src/commands/review_report.rs:323-362]
- `analytics_graph_from_edges` (function) component `analytics_graph_from_edges [function]` (`05dcb72b-1931-5544-9025-91a3b0f3f7f0`) lines 364-399 [crates/gwiki/src/commands/review_report.rs:364-399]
  - Signature: `fn analytics_graph_from_edges(changes: &ChangeSetInput, edges: &[CodeGraphEdge]) -> AnalyticsGraph {`
  - Purpose: Builds an 'AnalyticsGraph' by marking changed node IDs from the 'ChangeSetInput' as '"changed"' nodes with weight '3.0', adding any edge endpoints missing from the node set as '"neighbor"' nodes with weight '1.0', and converting each 'CodeGraphEdge' into an 'AnalyticsEdge' with a kind-based weight. [crates/gwiki/src/commands/review_report.rs:364-399]
- `risky_dependency_shifts` (function) component `risky_dependency_shifts [function]` (`fa56147e-ff1b-5bd9-bb2a-35448e433bc3`) lines 401-430 [crates/gwiki/src/commands/review_report.rs:401-430]
  - Signature: `fn risky_dependency_shifts(`
  - Purpose: Computes dependency-risk candidates by analyzing the graph, selecting changed nodes with centrality scores that map to a risk via 'risk_from_score' using bridge nodes and the global max centrality as context, then returns the resulting 'Vec<RiskyDependencyShift>' sorted by descending score and ascending node ID. [crates/gwiki/src/commands/review_report.rs:401-430]
- `risk_from_score` (function) component `risk_from_score [function]` (`99d0b375-f107-5934-8959-b57579fea38d`) lines 432-456 [crates/gwiki/src/commands/review_report.rs:432-456]
  - Signature: `fn risk_from_score(`
  - Purpose: Returns 'Some(RiskyDependencyShift)' for a scored node when it is either a bridge node or has high centrality ('degree >= 2' or ties the maximum score), attaching the applicable reasons, and returns 'None' otherwise. [crates/gwiki/src/commands/review_report.rs:432-456]
- `changed_node_ids` (function) component `changed_node_ids [function]` (`3695bdd7-6b70-580a-8f3e-6b4430b84492`) lines 458-471 [crates/gwiki/src/commands/review_report.rs:458-471]
  - Signature: `fn changed_node_ids(changes: &ChangeSetInput, edges: &[CodeGraphEdge]) -> BTreeSet<String> {`
  - Purpose: Returns the union of all symbol IDs listed in 'changes.symbols' and the source/target node IDs of any 'edges' whose 'file_path' matches a path in 'changes.files', deduplicated in a 'BTreeSet<String>'. [crates/gwiki/src/commands/review_report.rs:458-471]
- `changed_node_ids_from_graph` (function) component `changed_node_ids_from_graph [function]` (`7a8e8ed3-2c00-57cf-8e39-f543abba64a5`) lines 473-484 [crates/gwiki/src/commands/review_report.rs:473-484]
  - Signature: `fn changed_node_ids_from_graph(`
  - Purpose: Returns a 'BTreeSet<String>' containing all symbol IDs from 'changes.symbols' plus the 'id' of every node in 'graph.nodes' whose 'kind' is '"changed"'. [crates/gwiki/src/commands/review_report.rs:473-484]
- `changed_files_from_diff` (function) component `changed_files_from_diff [function]` (`7a5c4fcd-0b43-5b6e-93dc-68c870a41d29`) lines 486-493 [crates/gwiki/src/commands/review_report.rs:486-493]
  - Signature: `fn changed_files_from_diff(path: &Path) -> Result<Vec<String>, WikiError> {`
  - Purpose: Reads the diff file at 'path' into a string and returns the list of changed file paths extracted by 'parse_unified_diff_files', mapping any read failure to 'WikiError::Io' with action '"read review-report diff"'. [crates/gwiki/src/commands/review_report.rs:486-493]
- `parse_unified_diff_files` (function) component `parse_unified_diff_files [function]` (`5c7366b9-abc3-5a0f-9ab5-701b1076f029`) lines 495-530 [crates/gwiki/src/commands/review_report.rs:495-530]
  - Signature: `fn parse_unified_diff_files(contents: &str) -> Vec<String> {`
  - Purpose: 'parse_unified_diff_files' scans unified diff text, extracts candidate file paths from '+++ b/', '--- a/', and 'diff --git' headers, sanitizes each path to reject unsafe entries, deduplicates them with sorted set semantics, and returns the resulting list of affected file paths. [crates/gwiki/src/commands/review_report.rs:495-530]
- `trim_diff_path` (function) component `trim_diff_path [function]` (`7e6bd227-40f8-57f7-acc8-ece59ae816fd`) lines 532-534 [crates/gwiki/src/commands/review_report.rs:532-534]
  - Signature: `fn trim_diff_path(path: &str) -> &str {`
  - Purpose: Returns a string slice of 'path' with leading and trailing whitespace removed and any surrounding double quotes stripped. [crates/gwiki/src/commands/review_report.rs:532-534]
- `review_affected_page` (function) component `review_affected_page [function]` (`97f30df8-5858-5eb8-8f0a-813dbca7fbe0`) lines 536-546 [crates/gwiki/src/commands/review_report.rs:536-546]
  - Signature: `fn review_affected_page(page: AffectedPage) -> ReviewAffectedPage {`
  - Purpose: Converts an 'AffectedPage' into a 'ReviewAffectedPage' by stringifying 'page_path' and each 'source_path' while moving 'source_ids' through unchanged. [crates/gwiki/src/commands/review_report.rs:536-546]
- `render_string_list` (function) component `render_string_list [function]` (`39072454-0bae-53ad-badf-5f1daa074d74`) lines 548-562 [crates/gwiki/src/commands/review_report.rs:548-562]
  - Signature: `fn render_string_list(markdown: &mut String, label: &str, values: &[String]) {`
  - Purpose: Appends a Markdown bullet list to 'markdown' for the given 'label', emitting '- <label>: none' when 'values' is empty and otherwise emitting one quoted '- <label>: '<value>'' line per string in 'values'. [crates/gwiki/src/commands/review_report.rs:548-562]
- `unique_non_empty` (function) component `unique_non_empty [function]` (`a966dfc3-d6c6-576e-90d7-8db3f4c4caf1`) lines 564-572 [crates/gwiki/src/commands/review_report.rs:564-572]
  - Signature: `fn unique_non_empty(values: Vec<String>) -> Vec<String> {`
  - Purpose: Trims whitespace from each input string, discards empty results, deduplicates the remaining values with a 'BTreeSet' to return them in sorted order, and collects them into a 'Vec<String>'. [crates/gwiki/src/commands/review_report.rs:564-572]
- `unique_edges` (function) component `unique_edges [function]` (`183b1cd2-31f4-50cd-b33b-39ac7a162f59`) lines 574-588 [crates/gwiki/src/commands/review_report.rs:574-588]
  - Signature: `fn unique_edges(edges: Vec<CodeGraphEdge>) -> Vec<CodeGraphEdge> {`
  - Purpose: Returns a 'Vec<CodeGraphEdge>' containing only the first occurrence of each edge whose '(edge, source, target, file_path, line)' tuple is unique, using a 'BTreeSet' to filter out duplicates while preserving input order. [crates/gwiki/src/commands/review_report.rs:574-588]
- `degradation_source` (function) component `degradation_source [function]` (`5aeb21d1-226b-50df-bce1-025a03eb7aee`) lines 590-603 [crates/gwiki/src/commands/review_report.rs:590-603]
  - Signature: `fn degradation_source(degradation: &DegradationKind) -> String {`
  - Purpose: Returns a stable string identifier for a 'DegradationKind', with special handling for 'gcode_code_graph' service unavailability and formatted variants for partial search/data, stale index, and skipped artifacts cases. [crates/gwiki/src/commands/review_report.rs:590-603]
- `is_graph_blocking_degraded_source` (function) component `is_graph_blocking_degraded_source [function]` (`46308355-3e7b-5932-80e9-f38783dcc80a`) lines 605-612 [crates/gwiki/src/commands/review_report.rs:605-612]
  - Signature: `fn is_graph_blocking_degraded_source(source: &str) -> bool {`
  - Purpose: Returns 'true' only when 'source' exactly matches one of the three degraded graph-unavailable constants ('DEGRADED_FALKORDB_UNAVAILABLE', 'DEGRADED_GCODE_CODE_GRAPH_UNAVAILABLE', or 'DEGRADED_SHARED_CODE_GRAPH_UNAVAILABLE'), and 'false' otherwise. [crates/gwiki/src/commands/review_report.rs:605-612]
- `optional_falkor_config` (function) component `optional_falkor_config [function]` (`1ee04ed4-47fc-5e36-8f8b-59364abf91c7`) lines 614-626 [crates/gwiki/src/commands/review_report.rs:614-626]
  - Signature: `fn optional_falkor_config(conn: &mut postgres::Client) -> Result<Option<FalkorConfig>, WikiError> {`
  - Purpose: Resolves an optional 'FalkorConfig' by building a 'PostgresConfigSource' and 'AiConfigSource' from the provided PostgreSQL client and 'gobby_home', mapping any setup failures to 'WikiError::Config', and then delegating to 'gobby_core::config::resolve_falkordb_config'. [crates/gwiki/src/commands/review_report.rs:614-626]
- `review_report_renders_markdown_with_risks_and_metadata` (function) component `review_report_renders_markdown_with_risks_and_metadata [function]` (`92612fba-0461-5c1a-9c28-975bde936bed`) lines 642-711 [crates/gwiki/src/commands/review_report.rs:642-711]
  - Signature: `fn review_report_renders_markdown_with_risks_and_metadata() {`
  - Purpose: Builds a report from project changes, affected/stale pages, neighborhood and analytics graph data, and verifies that the generated Markdown includes risk information and associated metadata. [crates/gwiki/src/commands/review_report.rs:642-711]
- `review_report_degrades_without_graph_analytics` (function) component `review_report_degrades_without_graph_analytics [function]` (`698c0ffb-57cb-5aff-bb56-16d0de043e90`) lines 714-736 [crates/gwiki/src/commands/review_report.rs:714-736]
  - Signature: `fn review_report_degrades_without_graph_analytics() {`
  - Purpose: Verifies that 'build_report_from_parts' marks the report as degraded when 'analytics_graph' is absent, leaves 'risky_dependency_shifts' empty, and renders markdown that records the degraded flag, degraded source list, and a graph/analytics-unavailable note. [crates/gwiki/src/commands/review_report.rs:714-736]
- `review_report_maps_semantic_partial_data_degradation` (function) component `review_report_maps_semantic_partial_data_degradation [function]` (`bd30a0ea-59f3-5803-91dd-c8fbcdc1050c`) lines 739-746 [crates/gwiki/src/commands/review_report.rs:739-746]
  - Signature: `fn review_report_maps_semantic_partial_data_degradation() {`
  - Purpose: Asserts that 'degradation_source' maps a 'DegradationKind::PartialData' for the 'semantic' component with the specified message to the canonical source string '"semantic_partial"'. [crates/gwiki/src/commands/review_report.rs:739-746]
- `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path` (function) component `parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path [function]` (`c150bf4a-d8c1-5534-acb0-ffe70953c4c4`) lines 749-760 [crates/gwiki/src/commands/review_report.rs:749-760]
  - Signature: `fn parse_unified_diff_files_uses_new_rename_path_and_skips_empty_right_path() {`
  - Purpose: Verifies that 'parse_unified_diff_files' extracts the renamed file from the new right-hand path ('src/new.rs') and ignores a diff entry whose right-hand path is empty ('b/'), returning only 'src/deleted.rs' and 'src/new.rs'. [crates/gwiki/src/commands/review_report.rs:749-760]
- `parse_unified_diff_files_sanitizes_unsafe_paths` (function) component `parse_unified_diff_files_sanitizes_unsafe_paths [function]` (`c7d2767b-dce3-596f-920f-a3ad37bf0ecf`) lines 763-776 [crates/gwiki/src/commands/review_report.rs:763-776]
  - Signature: `fn parse_unified_diff_files_sanitizes_unsafe_paths() {`
  - Purpose: It parses unified diff headers into file paths, normalizes benign './' segments, and discards unsafe absolute or path-traversal targets so only sanitized repository-relative files are returned. [crates/gwiki/src/commands/review_report.rs:763-776]

