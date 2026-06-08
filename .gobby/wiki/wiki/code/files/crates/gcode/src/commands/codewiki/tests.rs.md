---
title: crates/gcode/src/commands/codewiki/tests.rs
type: code_file
source_files:
- file: crates/gcode/src/commands/codewiki/tests.rs
  ranges:
  - 7-41
  - 44-51
  - 54-127
  - 130-143
  - 146-148
  - 151-156
  - 159-171
  - 174-196
  - 199-226
  - 229-238
  - 241-248
  - 251-335
  - 338-406
  - 409-423
  - 426-456
  - 459-480
  - 483-521
  - 524-536
  - 539-555
  - 558-575
  - 578-592
  - 595-628
  - 631-680
  - 683-776
  - 779-802
  - 805-809
  - 813-827
  - 831-845
  - 847-855
  - 857-859
  - 861-889
  - 891-919
---

# crates/gcode/src/commands/codewiki/tests.rs

Module: [[modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/tests.rs` exposes 32 indexed API symbols. [crates/gcode/src/commands/codewiki/tests.rs:7-41] [crates/gcode/src/commands/codewiki/tests.rs:44-51] [crates/gcode/src/commands/codewiki/tests.rs:54-127] [crates/gcode/src/commands/codewiki/tests.rs:130-143] [crates/gcode/src/commands/codewiki/tests.rs:146-148] [crates/gcode/src/commands/codewiki/tests.rs:151-156] [crates/gcode/src/commands/codewiki/tests.rs:159-171] [crates/gcode/src/commands/codewiki/tests.rs:174-196] [crates/gcode/src/commands/codewiki/tests.rs:199-226] [crates/gcode/src/commands/codewiki/tests.rs:229-238] [crates/gcode/src/commands/codewiki/tests.rs:241-248] [crates/gcode/src/commands/codewiki/tests.rs:251-335] [crates/gcode/src/commands/codewiki/tests.rs:338-406] [crates/gcode/src/commands/codewiki/tests.rs:409-423] [crates/gcode/src/commands/codewiki/tests.rs:426-456] [crates/gcode/src/commands/codewiki/tests.rs:459-480] [crates/gcode/src/commands/codewiki/tests.rs:483-521] [crates/gcode/src/commands/codewiki/tests.rs:524-536] [crates/gcode/src/commands/codewiki/tests.rs:539-555] [crates/gcode/src/commands/codewiki/tests.rs:558-575] [crates/gcode/src/commands/codewiki/tests.rs:578-592] [crates/gcode/src/commands/codewiki/tests.rs:595-628] [crates/gcode/src/commands/codewiki/tests.rs:631-680] [crates/gcode/src/commands/codewiki/tests.rs:683-776] [crates/gcode/src/commands/codewiki/tests.rs:779-802] [crates/gcode/src/commands/codewiki/tests.rs:805-809] [crates/gcode/src/commands/codewiki/tests.rs:813-827] [crates/gcode/src/commands/codewiki/tests.rs:831-845] [crates/gcode/src/commands/codewiki/tests.rs:847-855] [crates/gcode/src/commands/codewiki/tests.rs:857-859] [crates/gcode/src/commands/codewiki/tests.rs:861-889] [crates/gcode/src/commands/codewiki/tests.rs:891-919]

## API Symbols

- `generates_hierarchical_docs` (function) component `generates_hierarchical_docs [function]` (`c7497bf8-9df5-5ad3-86dd-4a4f6d30c408`) lines 7-41 [crates/gcode/src/commands/codewiki/tests.rs:7-41]
  - Signature: `fn generates_hierarchical_docs() {`
  - Purpose: This test validates that `generate_hierarchical_docs` correctly generates a multi-tiered markdown documentation structure with proper cross-references organized across repository, module, and file-level documents containing extracted code symbols. [crates/gcode/src/commands/codewiki/tests.rs:7-41]
- `inline_code_uses_commonmark_backtick_delimiters` (function) component `inline_code_uses_commonmark_backtick_delimiters [function]` (`a3703e68-2b3c-5cb9-8d24-4616e036a0de`) lines 44-51 [crates/gcode/src/commands/codewiki/tests.rs:44-51]
  - Signature: `fn inline_code_uses_commonmark_backtick_delimiters() {`
  - Purpose: Tests that `inline_code()` wraps input strings in CommonMark-compliant backtick delimiters with sufficient backtick repetition to disambiguate embedded backticks and normalizes internal whitespace. [crates/gcode/src/commands/codewiki/tests.rs:44-51]
- `clusters_modules_from_graph` (function) component `clusters_modules_from_graph [function]` (`e1eff57a-cd58-54b9-90c3-79b57a7e4f2e`) lines 54-127 [crates/gcode/src/commands/codewiki/tests.rs:54-127]
  - Signature: `fn clusters_modules_from_graph() {`
  - Purpose: This function validates that source files connected by code dependency graph edges are correctly clustered into a common hierarchical module during documentation generation. [crates/gcode/src/commands/codewiki/tests.rs:54-127]
- `file_root_detection_breaks_parent_cycles` (function) component `file_root_detection_breaks_parent_cycles [function]` (`f707ffd7-adc4-55c8-8969-da82e52a4db6`) lines 130-143 [crates/gcode/src/commands/codewiki/tests.rs:130-143]
  - Signature: `fn file_root_detection_breaks_parent_cycles() {`
  - Purpose: This test verifies that `find_file_root` detects and resolves cycles in a parent-file mapping by identifying the root file and applying path compression to redirect all entries to point directly to it. [crates/gcode/src/commands/codewiki/tests.rs:130-143]
- `common_module_for_empty_files_is_root` (function) component `common_module_for_empty_files_is_root [function]` (`0bc06f26-e3cf-5172-925c-6ca4a8d6318f`) lines 146-148 [crates/gcode/src/commands/codewiki/tests.rs:146-148]
  - Signature: `fn common_module_for_empty_files_is_root() {`
  - Purpose: This test verifies that `common_module_for_files` returns an empty string (the root module) when given an empty file list. [crates/gcode/src/commands/codewiki/tests.rs:146-148]
- `module_depth_counts_only_non_empty_segments` (function) component `module_depth_counts_only_non_empty_segments [function]` (`fba04e4e-fa57-53bc-a8a7-0c92d5492876`) lines 151-156 [crates/gcode/src/commands/codewiki/tests.rs:151-156]
  - Signature: `fn module_depth_counts_only_non_empty_segments() {`
  - Purpose: This unit test verifies that `module_depth()` returns the count of non-empty slash-delimited segments in a path string, correctly ignoring empty segments and trailing slashes. [crates/gcode/src/commands/codewiki/tests.rs:151-156]
- `core_file_filter_excludes_specs_mocks_and_test_prefixes` (function) component `core_file_filter_excludes_specs_mocks_and_test_prefixes [function]` (`f7ba58bf-7961-5743-ad6f-bfd1ac2a1584`) lines 159-171 [crates/gcode/src/commands/codewiki/tests.rs:159-171]
  - Signature: `fn core_file_filter_excludes_specs_mocks_and_test_prefixes() {`
  - Purpose: Tests that `is_core_file()` correctly filters out files matching test prefix, spec suffix, and mock directory patterns while including standard source files. [crates/gcode/src/commands/codewiki/tests.rs:159-171]
- `import_targets_match_exact_path_or_module_components` (function) component `import_targets_match_exact_path_or_module_components [function]` (`0c74d454-173c-54f9-95e2-054533061372`) lines 174-196 [crates/gcode/src/commands/codewiki/tests.rs:174-196]
  - Signature: `fn import_targets_match_exact_path_or_module_components() {`
  - Purpose: This test function validates that `files_for_import_target` correctly resolves module-qualified import targets to matching file paths using exact component matching and hierarchical module path resolution. [crates/gcode/src/commands/codewiki/tests.rs:174-196]
- `mermaid_labels_escape_label_metacharacters` (function) component `mermaid_labels_escape_label_metacharacters [function]` (`75bf0315-d9a4-5729-a76b-35709d471996`) lines 199-226 [crates/gcode/src/commands/codewiki/tests.rs:199-226]
  - Signature: `fn mermaid_labels_escape_label_metacharacters() {`
  - Purpose: This function tests that `render_module_dependency_mermaid` properly escapes Mermaid metacharacters (brackets, braces, pipes) as HTML entities in module label output to prevent syntax injection. [crates/gcode/src/commands/codewiki/tests.rs:199-226]
- `graph_queries_use_requested_edge_limit` (function) component `graph_queries_use_requested_edge_limit [function]` (`9f4269bb-7bc3-5bba-8fa7-5cada9f19aa0`) lines 229-238 [crates/gcode/src/commands/codewiki/tests.rs:229-238]
  - Signature: `fn graph_queries_use_requested_edge_limit() {`
  - Purpose: This test function verifies that `codewiki_call_edges_query` and `codewiki_import_edges_query` correctly apply the requested edge limit parameter to the LIMIT clause of their generated SQL queries. [crates/gcode/src/commands/codewiki/tests.rs:229-238]
- `edge_limit_validation_rejects_zero_and_excessive_limits` (function) component `edge_limit_validation_rejects_zero_and_excessive_limits [function]` (`958553de-7107-571a-ac7e-d7dd9a60cf83`) lines 241-248 [crates/gcode/src/commands/codewiki/tests.rs:241-248]
  - Signature: `fn edge_limit_validation_rejects_zero_and_excessive_limits() {`
  - Purpose: # Summary

This test function verifies that `validate_edge_limit()` returns `Ok` for values in the range [1, MAX_EDGE_LIMIT] and `Err` for zero and values exceeding the maximum, with error messages referencing the `--edge-limit` flag. [crates/gcode/src/commands/codewiki/tests.rs:241-248]
- `clusters_without_falkordb` (function) component `clusters_without_falkordb [function]` (`02aa2337-478a-5e41-a295-088e9e3feeb4`) lines 251-335 [crates/gcode/src/commands/codewiki/tests.rs:251-335]
  - Signature: `fn clusters_without_falkordb() {`
  - Purpose: # Summary

Tests that `generate_hierarchical_docs` correctly clusters source code symbols into hierarchical module and file documentation when the code dependency graph is unavailable, while excluding test files from the generated documentation. [crates/gcode/src/commands/codewiki/tests.rs:251-335]
- `emits_bounded_mermaid` (function) component `emits_bounded_mermaid [function]` (`e5208fff-c688-5f00-983c-2f2d340bde1c`) lines 338-406 [crates/gcode/src/commands/codewiki/tests.rs:338-406]
  - Signature: `fn emits_bounded_mermaid() {`
  - Purpose: Tests that `generate_hierarchical_docs()` emits Mermaid diagrams bounded to relevant dependency chains, excluding unrelated components from the code graph output. [crates/gcode/src/commands/codewiki/tests.rs:338-406]
- `bounded_component_edges_prefers_edges_nearest_seed` (function) component `bounded_component_edges_prefers_edges_nearest_seed [function]` (`1449a405-1fa4-5bec-a2ff-6e6f3782da93`) lines 409-423 [crates/gcode/src/commands/codewiki/tests.rs:409-423]
  - Signature: `fn bounded_component_edges_prefers_edges_nearest_seed() {`
  - Purpose: This unit test verifies that `bounded_component_edges` filters a given edge set to return only edges incident to seed components within specified boundary constraints, selecting preferred edges based on proximity ordering. [crates/gcode/src/commands/codewiki/tests.rs:409-423]
- `mermaid_degrades_without_falkordb` (function) component `mermaid_degrades_without_falkordb [function]` (`dd82868f-838f-5b89-b50c-8801d89f7fbb`) lines 426-456 [crates/gcode/src/commands/codewiki/tests.rs:426-456]
  - Signature: `fn mermaid_degrades_without_falkordb() {`
  - Purpose: This test verifies that `generate_hierarchical_docs` gracefully degrades documentation generation by including a "degraded: graph-unavailable" marker while preserving module, file, and symbol documentation when the code graph is unavailable. [crates/gcode/src/commands/codewiki/tests.rs:426-456]
- `empty_available_graph_does_not_emit_degradation_marker` (function) component `empty_available_graph_does_not_emit_degradation_marker [function]` (`9a0af686-bbb4-579f-8f61-48fef60ed117`) lines 459-480 [crates/gcode/src/commands/codewiki/tests.rs:459-480]
  - Signature: `fn empty_available_graph_does_not_emit_degradation_marker() {`
  - Purpose: Tests that documentation generation with an available (non-empty) dependency graph does not include a "degraded: graph-unavailable" marker in the generated module output. [crates/gcode/src/commands/codewiki/tests.rs:459-480]
- `truncated_graph_emits_degradation_marker_with_partial_diagram` (function) component `truncated_graph_emits_degradation_marker_with_partial_diagram [function]` (`1ccde2ca-5e91-5bac-b781-89686582264c`) lines 483-521 [crates/gcode/src/commands/codewiki/tests.rs:483-521]
  - Signature: `fn truncated_graph_emits_degradation_marker_with_partial_diagram() {`
  - Purpose: Verifies that `generate_hierarchical_docs` emits a 'graph-truncated' degradation marker and produces a partial Mermaid dependency diagram when processing a truncated code dependency graph. [crates/gcode/src/commands/codewiki/tests.rs:483-521]
- `frontmatter_source_files_accept_unquoted_and_escaped_values` (function) component `frontmatter_source_files_accept_unquoted_and_escaped_values [function]` (`4bf1bb7b-ff41-53c3-9184-23d4a42730bc`) lines 524-536 [crates/gcode/src/commands/codewiki/tests.rs:524-536]
  - Signature: `fn frontmatter_source_files_accept_unquoted_and_escaped_values() {`
  - Purpose: This unit test verifies that `source_files_from_frontmatter()` correctly parses both unquoted and escaped-quoted file path values from YAML frontmatter. [crates/gcode/src/commands/codewiki/tests.rs:524-536]
- `frontmatter_source_files_parse_yaml_with_ranges` (function) component `frontmatter_source_files_parse_yaml_with_ranges [function]` (`c30aa4f1-ffc5-5177-9368-6b3ec76163ab`) lines 539-555 [crates/gcode/src/commands/codewiki/tests.rs:539-555]
  - Signature: `fn frontmatter_source_files_parse_yaml_with_ranges() {`
  - Purpose: Tests that `source_files_from_frontmatter()` correctly parses YAML frontmatter to extract source file paths with optional line ranges. [crates/gcode/src/commands/codewiki/tests.rs:539-555]
- `source_hashes_reject_frontmatter_paths_outside_project_root` (function) component `source_hashes_reject_frontmatter_paths_outside_project_root [function]` (`6982cbf3-0271-5aaa-851f-b01ccd3b2a0c`) lines 558-575 [crates/gcode/src/commands/codewiki/tests.rs:558-575]
  - Signature: `fn source_hashes_reject_frontmatter_paths_outside_project_root() {`
  - Purpose: This test validates that `source_hashes_for_doc` rejects frontmatter-declared source file paths that resolve outside the project root directory. [crates/gcode/src/commands/codewiki/tests.rs:558-575]
- `yaml_unquote_translates_common_escapes_and_rejects_incomplete_escape` (function) component `yaml_unquote_translates_common_escapes_and_rejects_incomplete_escape [function]` (`c02b373b-7ae5-5bc6-b37d-eb61577d7804`) lines 578-592 [crates/gcode/src/commands/codewiki/tests.rs:578-592]
  - Signature: `fn yaml_unquote_translates_common_escapes_and_rejects_incomplete_escape() {`
  - Purpose: Tests that `unquote_yaml_string` correctly translates standard, hexadecimal, and unicode YAML escape sequences while rejecting incomplete and malformed escape codes. [crates/gcode/src/commands/codewiki/tests.rs:578-592]
- `frontmatter_serializes_scalars_with_serde_yaml` (function) component `frontmatter_serializes_scalars_with_serde_yaml [function]` (`983cc9fe-00b5-5794-8cf0-c434b71a1647`) lines 595-628 [crates/gcode/src/commands/codewiki/tests.rs:595-628]
  - Signature: `fn frontmatter_serializes_scalars_with_serde_yaml() {`
  - Purpose: This test verifies that the `frontmatter` function correctly serializes and deserializes strings containing special characters (newlines, quotes, tabs, backslashes, null bytes, unicode escapes) as YAML scalars through `serde_yaml` without data corruption. [crates/gcode/src/commands/codewiki/tests.rs:595-628]
- `citations_validated_against_spans` (function) component `citations_validated_against_spans [function]` (`4ce3c3ba-a18f-5fe6-b35f-e38eeee4f3df`) lines 631-680 [crates/gcode/src/commands/codewiki/tests.rs:631-680]
  - Signature: `fn citations_validated_against_spans() {`
  - Purpose: This test validates that citations generated in hierarchical documentation are filtered to only those referencing code locations that fall within the defined symbol span ranges and available source files. [crates/gcode/src/commands/codewiki/tests.rs:631-680]
- `incremental_regenerates_only_changed` (function) component `incremental_regenerates_only_changed [function]` (`4f22467f-3af1-59e5-873f-86506d9d816c`) lines 683-776 [crates/gcode/src/commands/codewiki/tests.rs:683-776]
  - Signature: `fn incremental_regenerates_only_changed() {`
  - Purpose: This function tests that incremental documentation generation only regenerates documentation for modified source files while preserving documentation artifacts for unchanged files. [crates/gcode/src/commands/codewiki/tests.rs:683-776]
- `run_summary_serializes_daemon_contract_keys` (function) component `run_summary_serializes_daemon_contract_keys [function]` (`3e68f134-5071-5d5a-86ae-a76d366088cb`) lines 779-802 [crates/gcode/src/commands/codewiki/tests.rs:779-802]
  - Signature: `fn run_summary_serializes_daemon_contract_keys() {`
  - Purpose: This test function verifies that a `CodewikiRunSummary` struct correctly serializes to JSON with all expected field values preserved. [crates/gcode/src/commands/codewiki/tests.rs:779-802]
- `component_id_uses_stored_symbol_id` (function) component `component_id_uses_stored_symbol_id [function]` (`66ced279-5b0d-5199-9a75-bb71161116d7`) lines 805-809 [crates/gcode/src/commands/codewiki/tests.rs:805-809]
  - Signature: `fn component_id_uses_stored_symbol_id() {`
  - Purpose: This unit test verifies that a symbol's `id` field correctly retains an explicitly assigned string value. [crates/gcode/src/commands/codewiki/tests.rs:805-809]
- `write_doc_rejects_symlinked_parent` (function) component `write_doc_rejects_symlinked_parent [function]` (`5111b92e-c6b7-5709-830e-0456be460cc9`) lines 813-827 [crates/gcode/src/commands/codewiki/tests.rs:813-827]
  - Signature: `fn write_doc_rejects_symlinked_parent() {`
  - Purpose: Tests that `write_doc` rejects write operations to paths traversing symlinks within the codewiki directory to prevent symlink-based directory escape attacks. [crates/gcode/src/commands/codewiki/tests.rs:813-827]
- `write_doc_rejects_symlinked_target` (function) component `write_doc_rejects_symlinked_target [function]` (`e044d50f-fce0-5e0f-b3e8-14055e311128`) lines 831-845 [crates/gcode/src/commands/codewiki/tests.rs:831-845]
  - Signature: `fn write_doc_rejects_symlinked_target() {`
  - Purpose: Tests that `write_doc` rejects symlinked targets within the codewiki directory to prevent writes outside the directory boundary. [crates/gcode/src/commands/codewiki/tests.rs:831-845]
- `test_symbol` (function) component `test_symbol [function]` (`7572cc45-5cce-5c22-ab20-cb4022529773`) lines 847-855 [crates/gcode/src/commands/codewiki/tests.rs:847-855]
  - Signature: `fn test_symbol(`
  - Purpose: Creates a test Symbol by delegating to `test_symbol_with_qualified` with the provided name used as both the qualified and unqualified identifier. [crates/gcode/src/commands/codewiki/tests.rs:847-855]
- `test_component_id` (function) component `test_component_id [function]` (`24c80066-b942-58cd-8746-260f375c9933`) lines 857-859 [crates/gcode/src/commands/codewiki/tests.rs:857-859]
  - Signature: `fn test_component_id(file_path: &str, name: &str, kind: &str) -> String {`
  - Purpose: This function generates a Symbol identifier string for a component by delegating to `Symbol::make_id` with hardcoded project ID "project-1", the provided file path, name, and kind parameters, and a zero index. [crates/gcode/src/commands/codewiki/tests.rs:857-859]
- `test_symbol_with_qualified` (function) component `test_symbol_with_qualified [function]` (`b027ef14-421a-592e-9d7c-fb75b4763f92`) lines 861-889 [crates/gcode/src/commands/codewiki/tests.rs:861-889]
  - Signature: `fn test_symbol_with_qualified(`
  - Purpose: Creates a Symbol struct instance for unit testing with provided metadata (file path, name, qualified name, kind, line position, and signature) configured for a Rust language element. [crates/gcode/src/commands/codewiki/tests.rs:861-889]
- `test_symbol_range` (function) component `test_symbol_range [function]` (`f5fd2009-6855-590f-8c82-82ce2efdbf22`) lines 891-919 [crates/gcode/src/commands/codewiki/tests.rs:891-919]
  - Signature: `fn test_symbol_range(`
  - Purpose: Constructs and returns a `Symbol` struct populated with the provided file metadata, name, kind, line range, and signature while generating a composite ID and defaulting unspecified fields. [crates/gcode/src/commands/codewiki/tests.rs:891-919]

