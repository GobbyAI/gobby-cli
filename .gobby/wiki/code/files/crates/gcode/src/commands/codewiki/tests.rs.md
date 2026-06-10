---
title: crates/gcode/src/commands/codewiki/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/tests.rs
  ranges:
  - 14-48
  - 51-113
  - 116-125
  - 128-201
  - 204-217
  - 220-222
  - 225-230
  - 233-245
  - 248-278
  - 281-293
  - 296-318
  - 321-348
  - 351-357
  - 360-381
  - 384-395
  - 398-405
  - 408-492
  - 495-563
  - 566-580
  - 583-613
  - 616-637
  - 640-678
  - 681-693
  - 696-712
  - 715-727
  - 730-747
  - 750-764
  - 767-800
  - 803-853
  - 856-961
  - 963-979
  - 981-997
  - 1000-1007
  - 1010-1015
  - 1018-1022
  - 1025-1056
  - 1059-1082
  - 1085-1089
  - 1093-1107
  - 1111-1125
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/tests.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/tests.rs` exposes 40 indexed API symbols.
[crates/gcode/src/commands/codewiki/tests.rs:14-48]
[crates/gcode/src/commands/codewiki/tests.rs:51-113]
[crates/gcode/src/commands/codewiki/tests.rs:116-125]
[crates/gcode/src/commands/codewiki/tests.rs:128-201]
[crates/gcode/src/commands/codewiki/tests.rs:204-217]
[crates/gcode/src/commands/codewiki/tests.rs:220-222]
[crates/gcode/src/commands/codewiki/tests.rs:225-230]
[crates/gcode/src/commands/codewiki/tests.rs:233-245]
[crates/gcode/src/commands/codewiki/tests.rs:248-278]
[crates/gcode/src/commands/codewiki/tests.rs:281-293]
[crates/gcode/src/commands/codewiki/tests.rs:296-318]
[crates/gcode/src/commands/codewiki/tests.rs:321-348]
[crates/gcode/src/commands/codewiki/tests.rs:351-357]
[crates/gcode/src/commands/codewiki/tests.rs:360-381]
[crates/gcode/src/commands/codewiki/tests.rs:384-395]
[crates/gcode/src/commands/codewiki/tests.rs:398-405]
[crates/gcode/src/commands/codewiki/tests.rs:408-492]
[crates/gcode/src/commands/codewiki/tests.rs:495-563]
[crates/gcode/src/commands/codewiki/tests.rs:566-580]
[crates/gcode/src/commands/codewiki/tests.rs:583-613]
[crates/gcode/src/commands/codewiki/tests.rs:616-637]
[crates/gcode/src/commands/codewiki/tests.rs:640-678]
[crates/gcode/src/commands/codewiki/tests.rs:681-693]
[crates/gcode/src/commands/codewiki/tests.rs:696-712]
[crates/gcode/src/commands/codewiki/tests.rs:715-727]
[crates/gcode/src/commands/codewiki/tests.rs:730-747]
[crates/gcode/src/commands/codewiki/tests.rs:750-764]
[crates/gcode/src/commands/codewiki/tests.rs:767-800]
[crates/gcode/src/commands/codewiki/tests.rs:803-853]
[crates/gcode/src/commands/codewiki/tests.rs:856-961]
[crates/gcode/src/commands/codewiki/tests.rs:963-979]
[crates/gcode/src/commands/codewiki/tests.rs:981-997]
[crates/gcode/src/commands/codewiki/tests.rs:1000-1007]
[crates/gcode/src/commands/codewiki/tests.rs:1010-1015]
[crates/gcode/src/commands/codewiki/tests.rs:1018-1022]
[crates/gcode/src/commands/codewiki/tests.rs:1025-1056]
[crates/gcode/src/commands/codewiki/tests.rs:1059-1082]
[crates/gcode/src/commands/codewiki/tests.rs:1085-1089]
[crates/gcode/src/commands/codewiki/tests.rs:1093-1107]
[crates/gcode/src/commands/codewiki/tests.rs:1111-1125]

## API Symbols

- `generates_hierarchical_docs` (function) component `generates_hierarchical_docs [function]` (`e8ec1943-e5bc-5bb1-a283-a69ee2b29be6`) lines 14-48 [crates/gcode/src/commands/codewiki/tests.rs:14-48]
  - Signature: `fn generates_hierarchical_docs() {`
  - Purpose: Tests that `generate_hierarchical_docs()` produces a hierarchically-organized markdown documentation structure with wiki-style cross-references between repository-level, module-level, and file-level documents containing code symbols. [crates/gcode/src/commands/codewiki/tests.rs:14-48]
- `codewiki_unified_vault_emits_code_paths_frontmatter_and_wikilinks` (function) component `codewiki_unified_vault_emits_code_paths_frontmatter_and_wikilinks [function]` (`ee4478d4-6837-5804-8c34-b08ec0c6c07c`) lines 51-113 [crates/gcode/src/commands/codewiki/tests.rs:51-113]
  - Signature: `fn codewiki_unified_vault_emits_code_paths_frontmatter_and_wikilinks() {`
  - Purpose: Test verifying that `generate_hierarchical_docs` produces a hierarchical vault structure with code paths (repo/modules/files), inter-document wikilinks, and valid YAML frontmatter metadata. [crates/gcode/src/commands/codewiki/tests.rs:51-113]
- `inline_code_uses_commonmark_backtick_delimiters` (function) component `inline_code_uses_commonmark_backtick_delimiters [function]` (`ad0e8f5d-731d-5948-8886-37ca3db2a0e9`) lines 116-125 [crates/gcode/src/commands/codewiki/tests.rs:116-125]
  - Signature: `fn inline_code_uses_commonmark_backtick_delimiters() {`
  - Purpose: This test verifies that the `inline_code` function correctly formats strings as CommonMark inline code by selecting backtick delimiters with collision avoidance and normalizing whitespace (collapsing newlines and spaces). [crates/gcode/src/commands/codewiki/tests.rs:116-125]
- `clusters_modules_from_graph` (function) component `clusters_modules_from_graph [function]` (`a7566ead-f759-5e00-a3c1-854e37349f31`) lines 128-201 [crates/gcode/src/commands/codewiki/tests.rs:128-201]
  - Signature: `fn clusters_modules_from_graph() {`
  - Purpose: This test verifies that `generate_hierarchical_docs` correctly clusters source files with call graph dependencies under their lowest common ancestor module in the generated hierarchical documentation structure. [crates/gcode/src/commands/codewiki/tests.rs:128-201]
- `file_root_detection_breaks_parent_cycles` (function) component `file_root_detection_breaks_parent_cycles [function]` (`933d1965-3664-5723-8d86-4a62594c07a4`) lines 204-217 [crates/gcode/src/commands/codewiki/tests.rs:204-217]
  - Signature: `fn file_root_detection_breaks_parent_cycles() {`
  - Purpose: Unit test verifying that `find_file_root` correctly identifies the acyclic root of a parent chain containing a cycle and applies path compression to redirect all file parent pointers to that root. [crates/gcode/src/commands/codewiki/tests.rs:204-217]
- `common_module_for_empty_files_is_root` (function) component `common_module_for_empty_files_is_root [function]` (`f5d4795e-0d22-53a1-a792-07111fa9cfa1`) lines 220-222 [crates/gcode/src/commands/codewiki/tests.rs:220-222]
  - Signature: `fn common_module_for_empty_files_is_root() {`
  - Purpose: Unit test asserting that `common_module_for_files` returns an empty string (representing the root module) when passed an empty file slice. [crates/gcode/src/commands/codewiki/tests.rs:220-222]
- `module_depth_counts_only_non_empty_segments` (function) component `module_depth_counts_only_non_empty_segments [function]` (`5fd2d3ff-c3d1-5621-a910-7e07178fb8dc`) lines 225-230 [crates/gcode/src/commands/codewiki/tests.rs:225-230]
  - Signature: `fn module_depth_counts_only_non_empty_segments() {`
  - Purpose: A unit test that verifies `module_depth()` correctly counts only non-empty path segments separated by slashes, returning zero for empty strings and bare slashes. [crates/gcode/src/commands/codewiki/tests.rs:225-230]
- `core_file_filter_excludes_specs_mocks_and_test_prefixes` (function) component `core_file_filter_excludes_specs_mocks_and_test_prefixes [function]` (`cdcfc318-fb43-5410-b1f3-4115f36f2f63`) lines 233-245 [crates/gcode/src/commands/codewiki/tests.rs:233-245]
  - Signature: `fn core_file_filter_excludes_specs_mocks_and_test_prefixes() {`
  - Purpose: Tests that `is_core_file()` correctly excludes files with test/spec/mock naming patterns and directories while accepting regular source files. [crates/gcode/src/commands/codewiki/tests.rs:233-245]
- `incremental_write_always_rewrites_docs_without_provenance` (function) component `incremental_write_always_rewrites_docs_without_provenance [function]` (`b18b554b-ca3f-5a38-bc43-76fb0a7d2b2a`) lines 248-278 [crates/gcode/src/commands/codewiki/tests.rs:248-278]
  - Signature: `fn incremental_write_always_rewrites_docs_without_provenance() {`
  - Purpose: # Summary

This test verifies that `write_incremental_doc_set` invariably rewrites documentation without provenance metadata while preserving provenance-tracked documents with matching content hashes during incremental updates. [crates/gcode/src/commands/codewiki/tests.rs:248-278]
- `core_file_filter_excludes_hidden_metadata_paths` (function) component `core_file_filter_excludes_hidden_metadata_paths [function]` (`5130e814-5556-5c71-be1e-21e70e5252b6`) lines 281-293 [crates/gcode/src/commands/codewiki/tests.rs:281-293]
  - Signature: `fn core_file_filter_excludes_hidden_metadata_paths() {`
  - Purpose: This test validates that the `is_core_file()` function correctly excludes files within dot-prefixed hidden metadata directories (`.gobby/`, `.github/`, `.claude/`, etc.) while including files in visible documentation directories. [crates/gcode/src/commands/codewiki/tests.rs:281-293]
- `import_targets_match_exact_path_or_module_components` (function) component `import_targets_match_exact_path_or_module_components [function]` (`a10264a7-6f64-5df3-8984-7a2fed43dc5b`) lines 296-318 [crates/gcode/src/commands/codewiki/tests.rs:296-318]
  - Signature: `fn import_targets_match_exact_path_or_module_components() {`
  - Purpose: This test validates that `files_for_import_target` correctly resolves import target queries to matching file paths using exact dotted-path matching and hierarchical module component prefix matching. [crates/gcode/src/commands/codewiki/tests.rs:296-318]
- `mermaid_labels_escape_label_metacharacters` (function) component `mermaid_labels_escape_label_metacharacters [function]` (`40f17390-bdd4-5380-886e-54fb0035820e`) lines 321-348 [crates/gcode/src/commands/codewiki/tests.rs:321-348]
  - Signature: `fn mermaid_labels_escape_label_metacharacters() {`
  - Purpose: This test verifies that the mermaid diagram renderer correctly escapes metacharacters (brackets, braces, pipes) in module labels to HTML entity sequences, preventing them from being interpreted as Mermaid syntax. [crates/gcode/src/commands/codewiki/tests.rs:321-348]
- `graph_queries_use_requested_edge_limit` (function) component `graph_queries_use_requested_edge_limit [function]` (`dc32ddd9-78fd-5d32-80b8-23c7f46e4e96`) lines 351-357 [crates/gcode/src/commands/codewiki/tests.rs:351-357]
  - Signature: `fn graph_queries_use_requested_edge_limit() {`
  - Purpose: Tests that both call and import edge query generators properly incorporate the requested limit parameter (17) into their SQL LIMIT clause. [crates/gcode/src/commands/codewiki/tests.rs:351-357]
- `import_edges_drop_non_core_source_files` (function) component `import_edges_drop_non_core_source_files [function]` (`d296a1d4-1067-5780-a5dc-17fe4c4f6675`) lines 360-381 [crates/gcode/src/commands/codewiki/tests.rs:360-381]
  - Signature: `fn import_edges_drop_non_core_source_files() {`
  - Purpose: This test verifies that `import_edges_from_pairs` filters import edges to include only those originating from core source files, excluding edges from non-core files like tests. [crates/gcode/src/commands/codewiki/tests.rs:360-381]
- `graph_queries_stay_small_and_carry_no_id_lists` (function) component `graph_queries_stay_small_and_carry_no_id_lists [function]` (`d97d9a4a-0bb5-593f-a640-f2a4b2bd8792`) lines 384-395 [crates/gcode/src/commands/codewiki/tests.rs:384-395]
  - Signature: `fn graph_queries_stay_small_and_carry_no_id_lists() {`
  - Purpose: This test function verifies that Cypher queries for code graph edges (calls and imports) are generated without embedded ID lists and remain sub-1KB in size to prevent socket-layer transmission failures. [crates/gcode/src/commands/codewiki/tests.rs:384-395]
- `edge_limit_validation_rejects_zero_and_excessive_limits` (function) component `edge_limit_validation_rejects_zero_and_excessive_limits [function]` (`e47545b3-2fea-550d-9c38-81551bd16365`) lines 398-405 [crates/gcode/src/commands/codewiki/tests.rs:398-405]
  - Signature: `fn edge_limit_validation_rejects_zero_and_excessive_limits() {`
  - Purpose: Tests that `validate_edge_limit` accepts limits in the range [1, MAX_EDGE_LIMIT] and rejects both zero and values exceeding the maximum with an error message referencing the `--edge-limit` flag. [crates/gcode/src/commands/codewiki/tests.rs:398-405]
- `clusters_without_falkordb` (function) component `clusters_without_falkordb [function]` (`f140bc6e-b262-5bec-9498-2564411f9427`) lines 408-492 [crates/gcode/src/commands/codewiki/tests.rs:408-492]
  - Signature: `fn clusters_without_falkordb() {`
  - Purpose: # Summary

Tests that `generate_hierarchical_docs` correctly generates hierarchical documentation with module and file-level structure while excluding test files when graph clustering data is unavailable. [crates/gcode/src/commands/codewiki/tests.rs:408-492]
- `emits_bounded_mermaid` (function) component `emits_bounded_mermaid [function]` (`1b2bda1f-aa83-5d98-b4d9-fe0ad5234966`) lines 495-563 [crates/gcode/src/commands/codewiki/tests.rs:495-563]
  - Signature: `fn emits_bounded_mermaid() {`
  - Purpose: # Summary

This function tests that `generate_hierarchical_docs` produces module-path-indexed hierarchical documentation from a bounded codebase dependency graph with predefined source files, import edges, and symbol definitions. [crates/gcode/src/commands/codewiki/tests.rs:495-563]
- `bounded_component_edges_prefers_edges_nearest_seed` (function) component `bounded_component_edges_prefers_edges_nearest_seed [function]` (`3b7fcf80-9854-5cc4-b227-73d71f9d83c1`) lines 566-580 [crates/gcode/src/commands/codewiki/tests.rs:566-580]
  - Signature: `fn bounded_component_edges_prefers_edges_nearest_seed() {`
  - Purpose: Verifies that `bounded_component_edges` with depth bound of 2 and preference parameter 1 filters edges to include only those directly adjacent to seed components. [crates/gcode/src/commands/codewiki/tests.rs:566-580]
- `mermaid_degrades_without_falkordb` (function) component `mermaid_degrades_without_falkordb [function]` (`a70d0e96-4bb8-5857-aa95-918c7722836e`) lines 583-613 [crates/gcode/src/commands/codewiki/tests.rs:583-613]
  - Signature: `fn mermaid_degrades_without_falkordb() {`
  - Purpose: Tests that `generate_hierarchical_docs` degrades gracefully when the code graph is unavailable, producing module and file documentation marked as degraded while preserving symbol information. [crates/gcode/src/commands/codewiki/tests.rs:583-613]
- `empty_available_graph_does_not_emit_degradation_marker` (function) component `empty_available_graph_does_not_emit_degradation_marker [function]` (`35eafe8b-7705-5c45-bd49-f009744d824f`) lines 616-637 [crates/gcode/src/commands/codewiki/tests.rs:616-637]
  - Signature: `fn empty_available_graph_does_not_emit_degradation_marker() {`
  - Purpose: This test verifies that generating hierarchical documentation with an available code graph (containing no edges) does not include a "degraded: graph-unavailable" marker in the output module documentation. [crates/gcode/src/commands/codewiki/tests.rs:616-637]
- `truncated_graph_emits_degradation_marker_with_partial_diagram` (function) component `truncated_graph_emits_degradation_marker_with_partial_diagram [function]` (`ebb53f17-e950-5dd4-b409-f88090e413f9`) lines 640-678 [crates/gcode/src/commands/codewiki/tests.rs:640-678]
  - Signature: `fn truncated_graph_emits_degradation_marker_with_partial_diagram() {`
  - Purpose: This function verifies that hierarchical documentation generation emits a `degraded: graph-truncated` degradation marker and still renders a partial mermaid dependency diagram when the code graph availability is marked as truncated. [crates/gcode/src/commands/codewiki/tests.rs:640-678]
- `frontmatter_provenance_accepts_unquoted_and_escaped_values` (function) component `frontmatter_provenance_accepts_unquoted_and_escaped_values [function]` (`45c0d422-7c92-51fe-9797-998a6d96e161`) lines 681-693 [crates/gcode/src/commands/codewiki/tests.rs:681-693]
  - Signature: `fn frontmatter_provenance_accepts_unquoted_and_escaped_values() {`
  - Purpose: This unit test verifies that the frontmatter parser correctly extracts provenance file entries whether specified as unquoted literals or quoted strings with escaped quote characters. [crates/gcode/src/commands/codewiki/tests.rs:681-693]
- `frontmatter_provenance_parse_yaml_with_ranges` (function) component `frontmatter_provenance_parse_yaml_with_ranges [function]` (`9ed20764-864d-5689-98e2-474c2cc818e9`) lines 696-712 [crates/gcode/src/commands/codewiki/tests.rs:696-712]
  - Signature: `fn frontmatter_provenance_parse_yaml_with_ranges() {`
  - Purpose: Tests that `source_files_from_frontmatter()` correctly extracts and deduplicates source file paths from YAML provenance metadata, handling both files with and without line range specifications. [crates/gcode/src/commands/codewiki/tests.rs:696-712]
- `frontmatter_legacy_source_files_are_ignored` (function) component `frontmatter_legacy_source_files_are_ignored [function]` (`72ceacf9-5db4-5714-9757-277bb2d4cd67`) lines 715-727 [crates/gcode/src/commands/codewiki/tests.rs:715-727]
  - Signature: `fn frontmatter_legacy_source_files_are_ignored() {`
  - Purpose: This test verifies that `source_files_from_frontmatter()` ignores legacy frontmatter key formats (`source_files` and `sources`), returning an empty collection. [crates/gcode/src/commands/codewiki/tests.rs:715-727]
- `source_hashes_reject_frontmatter_paths_outside_project_root` (function) component `source_hashes_reject_frontmatter_paths_outside_project_root [function]` (`9035bcec-9780-5df5-8355-5ac060582e69`) lines 730-747 [crates/gcode/src/commands/codewiki/tests.rs:730-747]
  - Signature: `fn source_hashes_reject_frontmatter_paths_outside_project_root() {`
  - Purpose: This test verifies that `source_hashes_for_doc` correctly rejects and errors when processing frontmatter containing file paths that resolve outside the project root. [crates/gcode/src/commands/codewiki/tests.rs:730-747]
- `yaml_unquote_translates_common_escapes_and_rejects_incomplete_escape` (function) component `yaml_unquote_translates_common_escapes_and_rejects_incomplete_escape [function]` (`c3092d5b-83ff-56b5-adae-113477ffcbd7`) lines 750-764 [crates/gcode/src/commands/codewiki/tests.rs:750-764]
  - Signature: `fn yaml_unquote_translates_common_escapes_and_rejects_incomplete_escape() {`
  - Purpose: This test verifies that `unquote_yaml_string` correctly translates YAML escape sequences (C-style escapes like `\n`, `\t`, `\\`, `\"`, and Unicode escapes like `\xHH`, `\uHHHH`, `\UHHHHHHHH`) while rejecting incomplete, malformed, and out-of-range escapes. [crates/gcode/src/commands/codewiki/tests.rs:750-764]
- `frontmatter_serializes_scalars_with_serde_yaml` (function) component `frontmatter_serializes_scalars_with_serde_yaml [function]` (`bb165e81-00da-5825-a733-25e7b10454ee`) lines 767-800 [crates/gcode/src/commands/codewiki/tests.rs:767-800]
  - Signature: `fn frontmatter_serializes_scalars_with_serde_yaml() {`
  - Purpose: Verifies that frontmatter serializes scalar field values with embedded special characters (newlines, quotes, tabs, null bytes) into valid YAML that serde_yaml can deserialize while preserving source file metadata. [crates/gcode/src/commands/codewiki/tests.rs:767-800]
- `citations_validated_against_spans` (function) component `citations_validated_against_spans [function]` (`f50b8608-6220-590a-8041-1642496f31d3`) lines 803-853 [crates/gcode/src/commands/codewiki/tests.rs:803-853]
  - Signature: `fn citations_validated_against_spans() {`
  - Purpose: This test validates that documentation generation includes only citations whose file paths and line ranges correspond to actual symbol spans, while filtering out citations referencing non-existent files or invalid line ranges. [crates/gcode/src/commands/codewiki/tests.rs:803-853]
- `incremental_regenerates_only_changed` (function) component `incremental_regenerates_only_changed [function]` (`fcbb1a07-3521-56fc-ae59-dd15807482e9`) lines 856-961 [crates/gcode/src/commands/codewiki/tests.rs:856-961]
  - Signature: `fn incremental_regenerates_only_changed() {`
  - Purpose: # Summary

Tests that incremental documentation regeneration only rewrites documentation files corresponding to modified source code while preserving unmodified documentation artifacts. [crates/gcode/src/commands/codewiki/tests.rs:856-961]
- `depth_probe_input` (function) component `depth_probe_input [function]` (`649ba769-d0a7-51c4-9c97-54de17bd98ed`) lines 963-979 [crates/gcode/src/commands/codewiki/tests.rs:963-979]
  - Signature: `fn depth_probe_input() -> CodewikiInput {`
  - Purpose: Constructs a `CodewikiInput` test fixture containing two source files (`src/lib.rs` and `src/nested/api.rs`) with their symbols (a `Client` struct and `serve` function) but no graph edges. [crates/gcode/src/commands/codewiki/tests.rs:963-979]
- `generation_systems_at_depth` (function) component `generation_systems_at_depth [function]` (`d4b28d3f-7259-56fe-9ccf-bdf9fd4cc517`) lines 981-997 [crates/gcode/src/commands/codewiki/tests.rs:981-997]
  - Signature: `fn generation_systems_at_depth(ai_depth: AiDepth) -> Vec<String> {`
  - Purpose: Collects and returns system prompt strings generated during hierarchical documentation generation at the specified AI depth level by intercepting them through a callback closure. [crates/gcode/src/commands/codewiki/tests.rs:981-997]
- `ai_depth_sections_skips_symbol_and_file_generation` (function) component `ai_depth_sections_skips_symbol_and_file_generation [function]` (`6b19bdbb-5a81-5216-821e-e6cfac28f34b`) lines 1000-1007 [crates/gcode/src/commands/codewiki/tests.rs:1000-1007]
  - Signature: `fn ai_depth_sections_skips_symbol_and_file_generation() {`
  - Purpose: This test verifies that the Sections AI depth level includes MODULE_SYSTEM, REPO_SYSTEM, and ARCHITECTURE_SYSTEM but excludes SYMBOL_SYSTEM and FILE_SYSTEM from its generation systems. [crates/gcode/src/commands/codewiki/tests.rs:1000-1007]
- `ai_depth_files_skips_symbol_generation_only` (function) component `ai_depth_files_skips_symbol_generation_only [function]` (`10664074-5376-5290-ac6a-6179f145d854`) lines 1010-1015 [crates/gcode/src/commands/codewiki/tests.rs:1010-1015]
  - Signature: `fn ai_depth_files_skips_symbol_generation_only() {`
  - Purpose: This function verifies that code generation at the Files depth includes FILE_SYSTEM and MODULE_SYSTEM but excludes SYMBOL_SYSTEM. [crates/gcode/src/commands/codewiki/tests.rs:1010-1015]
- `ai_depth_symbols_generates_symbol_purposes` (function) component `ai_depth_symbols_generates_symbol_purposes [function]` (`20f9bddc-eda0-5a39-b491-f5a2f66b1157`) lines 1018-1022 [crates/gcode/src/commands/codewiki/tests.rs:1018-1022]
  - Signature: `fn ai_depth_symbols_generates_symbol_purposes() {`
  - Purpose: This function tests that retrieving generation systems at the `AiDepth::Symbols` depth level includes both the `SYMBOL_SYSTEM` and `FILE_SYSTEM` prompts. [crates/gcode/src/commands/codewiki/tests.rs:1018-1022]
- `ai_mode_change_invalidates_unchanged_docs` (function) component `ai_mode_change_invalidates_unchanged_docs [function]` (`259f5ad1-101b-5e36-850c-077bd4da033c`) lines 1025-1056 [crates/gcode/src/commands/codewiki/tests.rs:1025-1056]
  - Signature: `fn ai_mode_change_invalidates_unchanged_docs() {`
  - Purpose: This test verifies that switching the AI documentation generation mode (from "off" to "sections") invalidates unchanged documents for rewriting, whereas maintaining the same mode preserves them without rewriting. [crates/gcode/src/commands/codewiki/tests.rs:1025-1056]
- `run_summary_serializes_daemon_contract_keys` (function) component `run_summary_serializes_daemon_contract_keys [function]` (`c34f5401-b822-508d-a817-d91c2fa9260a`) lines 1059-1082 [crates/gcode/src/commands/codewiki/tests.rs:1059-1082]
  - Signature: `fn run_summary_serializes_daemon_contract_keys() {`
  - Purpose: This function tests the JSON serialization of a `CodewikiRunSummary` struct by asserting that key fields (command, project identifiers, paths, counts, and flags) correctly serialize via `serde_json::to_value()`. [crates/gcode/src/commands/codewiki/tests.rs:1059-1082]
- `component_id_uses_stored_symbol_id` (function) component `component_id_uses_stored_symbol_id [function]` (`fc24ca84-22bc-5642-ae2b-f43b9d16907d`) lines 1085-1089 [crates/gcode/src/commands/codewiki/tests.rs:1085-1089]
  - Signature: `fn component_id_uses_stored_symbol_id() {`
  - Purpose: Tests that a Symbol struct's id field successfully stores a manually assigned string value. [crates/gcode/src/commands/codewiki/tests.rs:1085-1089]
- `write_doc_rejects_symlinked_parent` (function) component `write_doc_rejects_symlinked_parent [function]` (`aac02de8-6d4d-5aa3-81d5-0c7eb6d8c028`) lines 1093-1107 [crates/gcode/src/commands/codewiki/tests.rs:1093-1107]
  - Signature: `fn write_doc_rejects_symlinked_parent() {`
  - Purpose: This test verifies that `write_doc` rejects write operations through symlinked parent directories to prevent directory escape attacks. [crates/gcode/src/commands/codewiki/tests.rs:1093-1107]
- `write_doc_rejects_symlinked_target` (function) component `write_doc_rejects_symlinked_target [function]` (`0fba7a9c-f728-555a-b2ba-950414132de2`) lines 1111-1125 [crates/gcode/src/commands/codewiki/tests.rs:1111-1125]
  - Signature: `fn write_doc_rejects_symlinked_target() {`
  - Purpose: Unit test verifying that `write_doc` rejects writing to symlinked file targets within the codewiki directory. [crates/gcode/src/commands/codewiki/tests.rs:1111-1125]

