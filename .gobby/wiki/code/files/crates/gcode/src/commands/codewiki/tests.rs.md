---
title: crates/gcode/src/commands/codewiki/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/tests.rs
  ranges:
  - 11-45
  - 48-110
  - 113-120
  - 123-196
  - 199-212
  - 215-217
  - 220-225
  - 228-240
  - 243-265
  - 268-295
  - 298-307
  - 310-317
  - 320-404
  - 407-475
  - 478-492
  - 495-525
  - 528-549
  - 552-590
  - 593-605
  - 608-624
  - 627-644
  - 647-661
  - 664-697
  - 700-750
  - 753-854
  - 857-880
  - 883-887
  - 891-905
  - 909-923
  - 925-933
  - 935-937
  - 939-967
  - 969-997
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/tests.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/tests.rs` exposes 33 indexed API symbols.
[crates/gcode/src/commands/codewiki/tests.rs:11-45] [crates/gcode/src/commands/codewiki/tests.rs:48-110] [crates/gcode/src/commands/codewiki/tests.rs:113-120] [crates/gcode/src/commands/codewiki/tests.rs:123-196]
[crates/gcode/src/commands/codewiki/tests.rs:199-212] [crates/gcode/src/commands/codewiki/tests.rs:215-217] [crates/gcode/src/commands/codewiki/tests.rs:220-225] [crates/gcode/src/commands/codewiki/tests.rs:228-240]
[crates/gcode/src/commands/codewiki/tests.rs:243-265] [crates/gcode/src/commands/codewiki/tests.rs:268-295] [crates/gcode/src/commands/codewiki/tests.rs:298-307] [crates/gcode/src/commands/codewiki/tests.rs:310-317]
[crates/gcode/src/commands/codewiki/tests.rs:320-404] [crates/gcode/src/commands/codewiki/tests.rs:407-475] [crates/gcode/src/commands/codewiki/tests.rs:478-492] [crates/gcode/src/commands/codewiki/tests.rs:495-525]
[crates/gcode/src/commands/codewiki/tests.rs:528-549] [crates/gcode/src/commands/codewiki/tests.rs:552-590] [crates/gcode/src/commands/codewiki/tests.rs:593-605] [crates/gcode/src/commands/codewiki/tests.rs:608-624]
[crates/gcode/src/commands/codewiki/tests.rs:627-644] [crates/gcode/src/commands/codewiki/tests.rs:647-661] [crates/gcode/src/commands/codewiki/tests.rs:664-697] [crates/gcode/src/commands/codewiki/tests.rs:700-750]
[crates/gcode/src/commands/codewiki/tests.rs:753-854] [crates/gcode/src/commands/codewiki/tests.rs:857-880] [crates/gcode/src/commands/codewiki/tests.rs:883-887] [crates/gcode/src/commands/codewiki/tests.rs:891-905]
[crates/gcode/src/commands/codewiki/tests.rs:909-923] [crates/gcode/src/commands/codewiki/tests.rs:925-933] [crates/gcode/src/commands/codewiki/tests.rs:935-937] [crates/gcode/src/commands/codewiki/tests.rs:939-967]
[crates/gcode/src/commands/codewiki/tests.rs:969-997]

## API Symbols

- `generates_hierarchical_docs` (function) component `generates_hierarchical_docs [function]` (`01538df9-7c01-54a1-8060-052c7bdf6ed2`) lines 11-45 [crates/gcode/src/commands/codewiki/tests.rs:11-45]
  - Signature: `fn generates_hierarchical_docs() {`
  - Purpose: This test function validates that `generate_hierarchical_docs()` correctly generates a multi-level markdown documentation hierarchy (repository, module, and file levels) with accurate inter-document cross-references and extracted API symbols from the input codebase. [crates/gcode/src/commands/codewiki/tests.rs:11-45]
- `codewiki_unified_vault_emits_code_paths_frontmatter_and_wikilinks` (function) component `codewiki_unified_vault_emits_code_paths_frontmatter_and_wikilinks [function]` (`e56e4ba0-1933-5422-925c-d7ddf0c6fef8`) lines 48-110 [crates/gcode/src/commands/codewiki/tests.rs:48-110]
  - Signature: `fn codewiki_unified_vault_emits_code_paths_frontmatter_and_wikilinks() {`
  - Purpose: Test verifying that `generate_hierarchical_docs` emits a unified documentation vault with hierarchical code paths, YAML frontmatter metadata, and wikilinks connecting modules and files. [crates/gcode/src/commands/codewiki/tests.rs:48-110]
- `inline_code_uses_commonmark_backtick_delimiters` (function) component `inline_code_uses_commonmark_backtick_delimiters [function]` (`eb6df6af-383b-5c9c-8049-ee0a821575ac`) lines 113-120 [crates/gcode/src/commands/codewiki/tests.rs:113-120]
  - Signature: `fn inline_code_uses_commonmark_backtick_delimiters() {`
  - Purpose: This test verifies that the `inline_code()` function correctly formats strings as CommonMark inline code by wrapping them in backtick delimiters, using additional backticks when necessary to prevent delimiter conflicts with backticks in the content. [crates/gcode/src/commands/codewiki/tests.rs:113-120]
- `clusters_modules_from_graph` (function) component `clusters_modules_from_graph [function]` (`b51414a5-90eb-5efb-8c4d-9b57722a63da`) lines 123-196 [crates/gcode/src/commands/codewiki/tests.rs:123-196]
  - Signature: `fn clusters_modules_from_graph() {`
  - Purpose: Tests that source files with call graph dependencies are correctly clustered into a hierarchical module structure in documentation generation. [crates/gcode/src/commands/codewiki/tests.rs:123-196]
- `file_root_detection_breaks_parent_cycles` (function) component `file_root_detection_breaks_parent_cycles [function]` (`1b365924-d750-5b1d-a235-38f3e337c259`) lines 199-212 [crates/gcode/src/commands/codewiki/tests.rs:199-212]
  - Signature: `fn file_root_detection_breaks_parent_cycles() {`
  - Purpose: This test verifies that `find_file_root` correctly traverses a cyclic parent chain, identifies the root file, and applies path compression by updating all parent pointers to reference that root. [crates/gcode/src/commands/codewiki/tests.rs:199-212]
- `common_module_for_empty_files_is_root` (function) component `common_module_for_empty_files_is_root [function]` (`15d2a1e8-8c4b-55bf-8c72-8b6736273637`) lines 215-217 [crates/gcode/src/commands/codewiki/tests.rs:215-217]
  - Signature: `fn common_module_for_empty_files_is_root() {`
  - Purpose: Tests that `common_module_for_files` returns an empty string (representing the root module) when passed an empty file list. [crates/gcode/src/commands/codewiki/tests.rs:215-217]
- `module_depth_counts_only_non_empty_segments` (function) component `module_depth_counts_only_non_empty_segments [function]` (`70693de8-2f1f-5f94-badb-65a92aec433d`) lines 220-225 [crates/gcode/src/commands/codewiki/tests.rs:220-225]
  - Signature: `fn module_depth_counts_only_non_empty_segments() {`
  - Purpose: This test function validates that `module_depth()` returns the count of non-empty path segments in a file path string, ignoring empty strings and trailing slashes. [crates/gcode/src/commands/codewiki/tests.rs:220-225]
- `core_file_filter_excludes_specs_mocks_and_test_prefixes` (function) component `core_file_filter_excludes_specs_mocks_and_test_prefixes [function]` (`d552e1fa-b58b-5166-a9bc-46e47a7fc83a`) lines 228-240 [crates/gcode/src/commands/codewiki/tests.rs:228-240]
  - Signature: `fn core_file_filter_excludes_specs_mocks_and_test_prefixes() {`
  - Purpose: Tests that `is_core_file()` correctly excludes files matching test, spec, and mock naming patterns while accepting standard source files. [crates/gcode/src/commands/codewiki/tests.rs:228-240]
- `import_targets_match_exact_path_or_module_components` (function) component `import_targets_match_exact_path_or_module_components [function]` (`afcca8ff-4edb-59af-9bab-8ddaa008a7ef`) lines 243-265 [crates/gcode/src/commands/codewiki/tests.rs:243-265]
  - Signature: `fn import_targets_match_exact_path_or_module_components() {`
  - Purpose: This test function verifies that `files_for_import_target()` correctly resolves import target strings to matching file paths using both exact module-path matching and hierarchical module-component matching. [crates/gcode/src/commands/codewiki/tests.rs:243-265]
- `mermaid_labels_escape_label_metacharacters` (function) component `mermaid_labels_escape_label_metacharacters [function]` (`0bcbe4fd-2f53-54ba-8464-1b2f9ecfc029`) lines 268-295 [crates/gcode/src/commands/codewiki/tests.rs:268-295]
  - Signature: `fn mermaid_labels_escape_label_metacharacters() {`
  - Purpose: Verifies that `render_module_dependency_mermaid` HTML-encodes metacharacters in module labels (brackets, braces, pipes) to prevent unintended mermaid diagram syntax interpretation. [crates/gcode/src/commands/codewiki/tests.rs:268-295]
- `graph_queries_use_requested_edge_limit` (function) component `graph_queries_use_requested_edge_limit [function]` (`8172fd89-840d-518e-bd70-7935e6143748`) lines 298-307 [crates/gcode/src/commands/codewiki/tests.rs:298-307]
  - Signature: `fn graph_queries_use_requested_edge_limit() {`
  - Purpose: This function tests that graph edge query builders (`codewiki_call_edges_query` and `codewiki_import_edges_query`) correctly embed the requested edge limit parameter into their generated SQL LIMIT clauses. [crates/gcode/src/commands/codewiki/tests.rs:298-307]
- `edge_limit_validation_rejects_zero_and_excessive_limits` (function) component `edge_limit_validation_rejects_zero_and_excessive_limits [function]` (`30693c91-fff2-55a4-a38e-50352ced59af`) lines 310-317 [crates/gcode/src/commands/codewiki/tests.rs:310-317]
  - Signature: `fn edge_limit_validation_rejects_zero_and_excessive_limits() {`
  - Purpose: This unit test verifies that the `validate_edge_limit` function accepts values in the range [1, MAX_EDGE_LIMIT] while rejecting zero and values exceeding the maximum, with error messages referencing the CLI option. [crates/gcode/src/commands/codewiki/tests.rs:310-317]
- `clusters_without_falkordb` (function) component `clusters_without_falkordb [function]` (`95f0b3d9-cc4e-545a-b041-51dd5eed9a90`) lines 320-404 [crates/gcode/src/commands/codewiki/tests.rs:320-404]
  - Signature: `fn clusters_without_falkordb() {`
  - Purpose: This test function verifies that `generate_hierarchical_docs` correctly clusters source code into hierarchical documentation by module and file when the code dependency graph is unavailable, while excluding test files from the generated documentation. [crates/gcode/src/commands/codewiki/tests.rs:320-404]
- `emits_bounded_mermaid` (function) component `emits_bounded_mermaid [function]` (`2d01efde-b192-5c64-a652-4de39ad68a7c`) lines 407-475 [crates/gcode/src/commands/codewiki/tests.rs:407-475]
  - Signature: `fn emits_bounded_mermaid() {`
  - Purpose: Validates that `generate_hierarchical_docs` generates scoped Mermaid diagrams containing only components within the transitive dependency closure of specified modules, excluding unrelated dependencies. [crates/gcode/src/commands/codewiki/tests.rs:407-475]
- `bounded_component_edges_prefers_edges_nearest_seed` (function) component `bounded_component_edges_prefers_edges_nearest_seed [function]` (`06106795-9bb9-5bef-b008-7709b56a5988`) lines 478-492 [crates/gcode/src/commands/codewiki/tests.rs:478-492]
  - Signature: `fn bounded_component_edges_prefers_edges_nearest_seed() {`
  - Purpose: This test validates that `bounded_component_edges` filters edges to include only those directly adjacent to seed components, respecting the specified limit parameters (2, 1) and excluding both non-incident edges and excess seed-adjacent edges. [crates/gcode/src/commands/codewiki/tests.rs:478-492]
- `mermaid_degrades_without_falkordb` (function) component `mermaid_degrades_without_falkordb [function]` (`69b83ce2-4de5-54ce-807a-3988863e31d7`) lines 495-525 [crates/gcode/src/commands/codewiki/tests.rs:495-525]
  - Signature: `fn mermaid_degrades_without_falkordb() {`
  - Purpose: Tests that `generate_hierarchical_docs()` produces valid module and file documentation with degradation markers when the code dependency graph is unavailable. [crates/gcode/src/commands/codewiki/tests.rs:495-525]
- `empty_available_graph_does_not_emit_degradation_marker` (function) component `empty_available_graph_does_not_emit_degradation_marker [function]` (`5fb7d3fa-b6ef-5c48-9029-d351668affa7`) lines 528-549 [crates/gcode/src/commands/codewiki/tests.rs:528-549]
  - Signature: `fn empty_available_graph_does_not_emit_degradation_marker() {`
  - Purpose: This test asserts that `generate_hierarchical_docs` omits the "degraded: graph-unavailable" marker from module documentation when the dependency graph is available but contains no edges. [crates/gcode/src/commands/codewiki/tests.rs:528-549]
- `truncated_graph_emits_degradation_marker_with_partial_diagram` (function) component `truncated_graph_emits_degradation_marker_with_partial_diagram [function]` (`e641ded9-0eec-53fc-839e-20df7fed572f`) lines 552-590 [crates/gcode/src/commands/codewiki/tests.rs:552-590]
  - Signature: `fn truncated_graph_emits_degradation_marker_with_partial_diagram() {`
  - Purpose: Tests that `generate_hierarchical_docs` produces module documentation with a 'degraded: graph-truncated' degradation marker and partial Mermaid diagram when the input graph's availability is marked as truncated. [crates/gcode/src/commands/codewiki/tests.rs:552-590]
- `frontmatter_source_files_accept_unquoted_and_escaped_values` (function) component `frontmatter_source_files_accept_unquoted_and_escaped_values [function]` (`b3f4d644-ea4a-5b47-8b20-6ac72f9fde06`) lines 593-605 [crates/gcode/src/commands/codewiki/tests.rs:593-605]
  - Signature: `fn frontmatter_source_files_accept_unquoted_and_escaped_values() {`
  - Purpose: Tests that `source_files_from_frontmatter` correctly parses both unquoted plain filenames and double-quoted filenames with escaped quotes from YAML frontmatter. [crates/gcode/src/commands/codewiki/tests.rs:593-605]
- `frontmatter_source_files_parse_yaml_with_ranges` (function) component `frontmatter_source_files_parse_yaml_with_ranges [function]` (`744db4b3-95d1-5f98-9876-7febb22e4271`) lines 608-624 [crates/gcode/src/commands/codewiki/tests.rs:608-624]
  - Signature: `fn frontmatter_source_files_parse_yaml_with_ranges() {`
  - Purpose: This test validates that `source_files_from_frontmatter()` correctly extracts source file paths from YAML frontmatter containing optional line range specifications. [crates/gcode/src/commands/codewiki/tests.rs:608-624]
- `source_hashes_reject_frontmatter_paths_outside_project_root` (function) component `source_hashes_reject_frontmatter_paths_outside_project_root [function]` (`08942093-d69a-5300-89f7-dc57bfc8f4d5`) lines 627-644 [crates/gcode/src/commands/codewiki/tests.rs:627-644]
  - Signature: `fn source_hashes_reject_frontmatter_paths_outside_project_root() {`
  - Purpose: This test verifies that `source_hashes_for_doc()` rejects frontmatter source file paths that resolve outside the project root directory. [crates/gcode/src/commands/codewiki/tests.rs:627-644]
- `yaml_unquote_translates_common_escapes_and_rejects_incomplete_escape` (function) component `yaml_unquote_translates_common_escapes_and_rejects_incomplete_escape [function]` (`66466d92-7d89-57c3-8dff-91525ec970fd`) lines 647-661 [crates/gcode/src/commands/codewiki/tests.rs:647-661]
  - Signature: `fn yaml_unquote_translates_common_escapes_and_rejects_incomplete_escape() {`
  - Purpose: # Summary

This test verifies that `unquote_yaml_string` correctly interprets standard (`\n`, `\t`, `\\`, `\"`), hexadecimal (`\xHH`), and Unicode (`\uHHHH`, `\UHHHHHHHH`) escape sequences in YAML strings while rejecting incomplete, malformed, and out-of-range escape sequences. [crates/gcode/src/commands/codewiki/tests.rs:647-661]
- `frontmatter_serializes_scalars_with_serde_yaml` (function) component `frontmatter_serializes_scalars_with_serde_yaml [function]` (`3a4759d0-90f4-5e0d-88a9-2439c772d51f`) lines 664-697 [crates/gcode/src/commands/codewiki/tests.rs:664-697]
  - Signature: `fn frontmatter_serializes_scalars_with_serde_yaml() {`
  - Purpose: Tests that the `frontmatter` function correctly serializes and preserves scalar values containing special characters (newlines, quotes, tabs, backslashes, null bytes) through YAML deserialization via serde_yaml. [crates/gcode/src/commands/codewiki/tests.rs:664-697]
- `citations_validated_against_spans` (function) component `citations_validated_against_spans [function]` (`280ba82f-3568-59af-a971-370c2c8a6132`) lines 700-750 [crates/gcode/src/commands/codewiki/tests.rs:700-750]
  - Signature: `fn citations_validated_against_spans() {`
  - Purpose: This test validates that generated documentation citations are filtered to include only those matching actual symbol source spans, while excluding citations that reference out-of-range line numbers or non-existent files. [crates/gcode/src/commands/codewiki/tests.rs:700-750]
- `incremental_regenerates_only_changed` (function) component `incremental_regenerates_only_changed [function]` (`1058ad2a-9df7-5417-9e58-91859748dcac`) lines 753-854 [crates/gcode/src/commands/codewiki/tests.rs:753-854]
  - Signature: `fn incremental_regenerates_only_changed() {`
  - Purpose: This test verifies that incremental documentation generation only regenerates output files for modified source files while preserving documentation for unchanged files. [crates/gcode/src/commands/codewiki/tests.rs:753-854]
- `run_summary_serializes_daemon_contract_keys` (function) component `run_summary_serializes_daemon_contract_keys [function]` (`ca1169c3-95ea-505c-899d-080138093c48`) lines 857-880 [crates/gcode/src/commands/codewiki/tests.rs:857-880]
  - Signature: `fn run_summary_serializes_daemon_contract_keys() {`
  - Purpose: Tests that `CodewikiRunSummary` correctly serializes to JSON with verified field values. [crates/gcode/src/commands/codewiki/tests.rs:857-880]
- `component_id_uses_stored_symbol_id` (function) component `component_id_uses_stored_symbol_id [function]` (`ee231216-e5f6-510d-8256-a877c2108869`) lines 883-887 [crates/gcode/src/commands/codewiki/tests.rs:883-887]
  - Signature: `fn component_id_uses_stored_symbol_id() {`
  - Purpose: This unit test verifies that a symbol's `id` field correctly stores and returns an explicitly assigned string value. [crates/gcode/src/commands/codewiki/tests.rs:883-887]
- `write_doc_rejects_symlinked_parent` (function) component `write_doc_rejects_symlinked_parent [function]` (`8d2f0ad3-95d5-5060-a0ff-b1218f7ffd37`) lines 891-905 [crates/gcode/src/commands/codewiki/tests.rs:891-905]
  - Signature: `fn write_doc_rejects_symlinked_parent() {`
  - Purpose: Tests that `write_doc()` rejects document writes through symlinked paths to prevent directory traversal escapes from the output directory. [crates/gcode/src/commands/codewiki/tests.rs:891-905]
- `write_doc_rejects_symlinked_target` (function) component `write_doc_rejects_symlinked_target [function]` (`5da67239-f403-5518-869b-05470d96b2ad`) lines 909-923 [crates/gcode/src/commands/codewiki/tests.rs:909-923]
  - Signature: `fn write_doc_rejects_symlinked_target() {`
  - Purpose: This test validates that `write_doc()` rejects write operations targeting symlinks that resolve outside the output directory, preventing directory traversal attacks. [crates/gcode/src/commands/codewiki/tests.rs:909-923]
- `test_symbol` (function) component `test_symbol [function]` (`64fd385c-8e96-53a1-a765-824643006be7`) lines 925-933 [crates/gcode/src/commands/codewiki/tests.rs:925-933]
  - Signature: `pub fn test_symbol(`
  - Purpose: Constructs a test `Symbol` with identical qualified and unqualified names by delegating to `test_symbol_with_qualified`. [crates/gcode/src/commands/codewiki/tests.rs:925-933]
- `test_component_id` (function) component `test_component_id [function]` (`99cc5be8-0851-5bc2-b52e-f1b3e41cc94e`) lines 935-937 [crates/gcode/src/commands/codewiki/tests.rs:935-937]
  - Signature: `pub fn test_component_id(file_path: &str, name: &str, kind: &str) -> String {`
  - Purpose: Constructs a symbol ID for a test component by delegating to `Symbol::make_id` with a hardcoded project identifier "project-1" and variant 0. [crates/gcode/src/commands/codewiki/tests.rs:935-937]
- `test_symbol_with_qualified` (function) component `test_symbol_with_qualified [function]` (`31582839-c08e-58fb-a9e9-8b6592cb93a4`) lines 939-967 [crates/gcode/src/commands/codewiki/tests.rs:939-967]
  - Signature: `fn test_symbol_with_qualified(`
  - Purpose: Constructs a Symbol struct for testing with specified qualified name, kind, and line position, initializing byte offsets to zero and optional fields to default or empty values. [crates/gcode/src/commands/codewiki/tests.rs:939-967]
- `test_symbol_range` (function) component `test_symbol_range [function]` (`77dc2561-03c6-5ce3-8cde-84ed13609525`) lines 969-997 [crates/gcode/src/commands/codewiki/tests.rs:969-997]
  - Signature: `fn test_symbol_range(`
  - Purpose: Constructs and returns a `Symbol` struct for testing with the provided file path, identifier metadata, line range, and signature, while initializing remaining fields with defaults. [crates/gcode/src/commands/codewiki/tests.rs:969-997]

